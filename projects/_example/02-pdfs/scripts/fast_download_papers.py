#!/usr/bin/env python3
"""Fast paper download: PMC async (50 concurrent) → multi-layer fallback.

Two-phase strategy:
  Phase 1: Batch lookup PMCIDs via Europe PMC → async download from PMC (fastest)
  Phase 2: Papers without PMCID → multi-layer 9-strategy download (ThreadPool)

Usage:
    python3 fast_download_papers.py \
      --items-file dois.txt \
      --base-dir ./papers \
      --workers 50

Input: .txt file with one DOI (or DOI URL) per line.
Output: papers in base-dir/<NNN-doi_slug>/paper.pdf + download report.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import aiohttp

# Import multi-layer downloader
sys.path.insert(0, str(Path(__file__).parent))
from batch_download_papers import Downloader, Item, write_md_report

DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")


def load_dois(path: Path) -> List[str]:
    dois = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = DOI_RE.search(line)
        if m:
            doi = m.group(0).strip().rstrip(".")
            if doi.startswith("https://doi.org/"):
                doi = doi.split("https://doi.org/", 1)[1]
            dois.append(doi.lower())
    # dedupe preserving order
    seen = set()
    out = []
    for d in dois:
        if d not in seen:
            seen.add(d)
            out.append(d)
    return out


def doi_to_folder(idx: int, doi: str) -> str:
    safe = re.sub(r'[/\\:*?"<>|]', '_', doi)
    return f"{idx:04d}-{safe}"


def get_existing_dois(base_dir: Path) -> set:
    existing = set()
    if not base_dir.exists():
        return existing
    for folder in base_dir.iterdir():
        if not folder.is_dir():
            continue
        pdf = folder / "paper.pdf"
        if pdf.exists() and pdf.stat().st_size > 1000:
            try:
                if pdf.read_bytes()[:5] == b"%PDF-":
                    m = re.match(r'\d+-(.+)', folder.name)
                    if m:
                        doi = m.group(1).replace('_', '/', 1)
                        existing.add(doi.lower())
            except Exception:
                pass
    return existing


# --- Phase 1: PMCID lookup + PMC async download ---

async def batch_lookup_pmcids(dois: List[str], concurrency: int = 10) -> Dict[str, str]:
    """Batch lookup PMCIDs via Europe PMC API."""
    doi_to_pmcid: Dict[str, str] = {}
    sem = asyncio.Semaphore(concurrency)

    async with aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=30),
        headers={"User-Agent": "Mozilla/5.0"}
    ) as session:
        async def lookup_one(doi: str):
            async with sem:
                try:
                    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{doi}&format=json"
                    async with session.get(url) as r:
                        if r.status == 200:
                            data = await r.json()
                            for rec in (data.get("resultList") or {}).get("result") or []:
                                pmcid = rec.get("pmcid")
                                if pmcid:
                                    doi_to_pmcid[doi] = pmcid
                                    return
                except Exception:
                    pass

        batch_size = 200
        tasks = [lookup_one(doi) for doi in dois]
        for i in range(0, len(tasks), batch_size):
            batch = tasks[i:i+batch_size]
            await asyncio.gather(*batch, return_exceptions=True)
            done = min(i + batch_size, len(tasks))
            print(f"  PMCID lookup: {done}/{len(dois)}, found {len(doi_to_pmcid)}")

    return doi_to_pmcid


async def download_pmc_batch(
    pairs: List[Tuple[str, str, str]],  # (doi, pmcid, folder_name)
    base_dir: Path,
    concurrency: int = 50,
) -> Tuple[List[str], List[str]]:
    """Async download from PMC. Returns (succeeded_dois, failed_dois)."""
    succeeded = []
    failed = []
    sem = asyncio.Semaphore(concurrency)
    done = [0]
    t0 = time.time()

    async with aiohttp.ClientSession(
        timeout=aiohttp.ClientTimeout(total=60),
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
    ) as session:
        async def download_one(doi: str, pmcid: str, folder_name: str):
            folder = base_dir / folder_name
            folder.mkdir(parents=True, exist_ok=True)
            pdf_path = folder / "paper.pdf"

            # Skip if already valid
            if pdf_path.exists() and pdf_path.stat().st_size > 1000:
                try:
                    if pdf_path.read_bytes()[:5] == b"%PDF-":
                        done[0] += 1
                        succeeded.append(doi)
                        return
                except Exception:
                    pass

            urls = [
                f"https://europepmc.org/articles/{pmcid}?pdf=render",
                f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmcid}&blobtype=pdf",
                f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/",
            ]

            async with sem:
                for url in urls:
                    try:
                        async with session.get(url, ssl=False) as r:
                            if r.status == 200:
                                content = await r.read()
                                if content[:5] == b"%PDF-" and len(content) > 1000:
                                    pdf_path.write_bytes(content)
                                    done[0] += 1
                                    succeeded.append(doi)
                                    if done[0] % 50 == 0:
                                        elapsed = time.time() - t0
                                        eta = elapsed / done[0] * (len(pairs) - done[0]) if done[0] else 0
                                        print(f"  PMC: [{done[0]}/{len(pairs)}] {len(succeeded)} ok, ETA {eta:.0f}s")
                                    return
                    except Exception:
                        pass

            done[0] += 1
            failed.append(doi)

        tasks = [download_one(doi, pmcid, folder_name) for doi, pmcid, folder_name in pairs]
        await asyncio.gather(*tasks, return_exceptions=True)

    return succeeded, failed


# --- Phase 2: Multi-layer fallback ---

def download_multilayer(
    items: List[Tuple[str, str]],  # (doi, folder_name)
    base_dir: Path,
    workers: int = 50,
    timeout: int = 45,
) -> Tuple[int, int]:
    """Download via 9-layer strategy. Returns (ok_count, fail_count)."""

    def _download_one(args):
        doi, folder_name = args
        item = Item(doi=doi, folder=folder_name)
        dl = Downloader(timeout=timeout, sleep_sec=0)
        return dl.download_one(item, base_dir=base_dir, overwrite=False)

    ok_count = 0
    fail_count = 0
    done_count = 0
    t0 = time.time()

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_download_one, item): item for item in items}
        for future in as_completed(futures):
            done_count += 1
            try:
                res = future.result()
                if res.status in ("downloaded", "exists"):
                    ok_count += 1
                else:
                    fail_count += 1
                if done_count % 50 == 0:
                    elapsed = time.time() - t0
                    eta = elapsed / done_count * (len(items) - done_count) if done_count else 0
                    print(f"  Multi-layer: [{done_count}/{len(items)}] {ok_count} ok, ETA {eta:.0f}s")
            except Exception:
                fail_count += 1

    return ok_count, fail_count


# --- Main ---

async def async_main(args):
    items_file = Path(args.items_file).expanduser().resolve()
    base_dir = Path(args.base_dir).expanduser().resolve()
    base_dir.mkdir(parents=True, exist_ok=True)
    workers = max(1, args.workers)
    t0 = time.time()

    # Load DOIs
    all_dois = load_dois(items_file)
    existing = get_existing_dois(base_dir)
    pending = [d for d in all_dois if d not in existing]
    print(f"Total: {len(all_dois)}, Already downloaded: {len(existing)}, Pending: {len(pending)}")

    if not pending:
        print("All papers already downloaded!")
        return

    # Build DOI -> folder mapping for pending
    doi_folders = {}
    for i, doi in enumerate(all_dois, 1):
        doi_folders[doi] = doi_to_folder(i, doi)

    # Phase 1: Batch lookup PMCIDs
    print(f"\n=== Phase 1: PMCID lookup + PMC async download ===")
    doi_to_pmcid = await batch_lookup_pmcids(pending, concurrency=10)
    pmc_pairs = [(doi, doi_to_pmcid[doi], doi_folders[doi]) for doi in pending if doi in doi_to_pmcid]
    no_pmcid = [(doi, doi_folders[doi]) for doi in pending if doi not in doi_to_pmcid]
    print(f"  With PMCID: {len(pmc_pairs)} → fast PMC path")
    print(f"  Without PMCID: {len(no_pmcid)} → multi-layer fallback")

    total_ok = 0

    # Phase 1: PMC async download
    if pmc_pairs:
        print(f"\n  Downloading {len(pmc_pairs)} papers via PMC ({workers} concurrent)...")
        pmc_ok, pmc_failed = await download_pmc_batch(pmc_pairs, base_dir, concurrency=workers)
        total_ok += len(pmc_ok)
        print(f"  PMC result: {len(pmc_ok)} success, {len(pmc_failed)} failed")
        # PMC failures join multi-layer
        no_pmcid.extend([(doi, doi_folders[doi]) for doi in pmc_failed])

    # Phase 2: Multi-layer for the rest
    if no_pmcid:
        print(f"\n=== Phase 2: Multi-layer download ({len(no_pmcid)} papers, {workers} threads) ===")
        ml_ok, ml_fail = download_multilayer(no_pmcid, base_dir, workers=workers, timeout=args.timeout)
        total_ok += ml_ok

    # Final stats
    elapsed = time.time() - t0
    final_pdfs = sum(
        1 for f in base_dir.iterdir()
        if f.is_dir() and (f / "paper.pdf").exists()
        and (f / "paper.pdf").stat().st_size > 1000
    )

    print(f"\n{'='*60}")
    print(f"DONE in {elapsed:.0f}s ({elapsed/60:.1f} min)")
    print(f"New downloads this run: {total_ok}")
    print(f"Total valid PDFs: {final_pdfs}/{len(all_dois)}")
    print(f"{'='*60}")


def main():
    parser = argparse.ArgumentParser(description="Fast paper download: PMC async + multi-layer fallback")
    parser.add_argument("--items-file", required=True, help="DOI list file (.txt, one per line)")
    parser.add_argument("--base-dir", required=True, help="Output directory for paper PDFs")
    parser.add_argument("--workers", type=int, default=50, help="Concurrent downloads (default 50)")
    parser.add_argument("--timeout", type=int, default=45, help="HTTP timeout for multi-layer (default 45s)")
    args = parser.parse_args()
    asyncio.run(async_main(args))


if __name__ == "__main__":
    main()
