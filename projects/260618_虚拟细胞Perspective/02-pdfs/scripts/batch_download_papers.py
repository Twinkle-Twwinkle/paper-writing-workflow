#!/usr/bin/env python3
"""Batch download papers by DOI into mapped folders.

Features:
- Parse items from markdown/csv/tsv/json
- Multi-strategy download (DOI, publisher pattern, OpenAlex, Crossref, Europe PMC)
- Optional Cloudflare fallback via cloudscraper
- Strict PDF validation (%PDF header)
- JSON + markdown report output
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple
from urllib.parse import urljoin

import requests

DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
FOLDER_BACKTICK_RE = re.compile(r"`(\[[0-9]+\]-[^`]+)`")
HREF_RE = re.compile(r"(?:href|src)=[\"']([^\"']+)[\"']", re.IGNORECASE)
CITATION_PDF_META_RE = re.compile(
    r"<meta[^>]+(?:name|property)=[\"']citation_pdf_url[\"'][^>]+content=[\"']([^\"']+)[\"']",
    re.IGNORECASE,
)
HTTP_RE = re.compile(r"https?://[^\"'\s<>]+")

# Publisher-specific PDF patterns for HTML scraping
MDPI_PDF_RE = re.compile(r'https://www\.mdpi\.com/[^"\s]+/pdf(?:\?version=\d+)?')
OUP_PDF_RE = re.compile(r'https://academic\.oup\.com/[^"\s]*article-pdf[^"\s]*\.pdf')
HINDAWI_PDF_RE = re.compile(r'https://downloads\.hindawi\.com/journals/[^"\s]+\.pdf')
ELSEVIER_PII_RE = re.compile(r'/pii/([A-Z0-9]+)')
WILEY_HOST_RE = re.compile(r'https?://([^/]*onlinelibrary\.wiley\.com)')


@dataclass
class Item:
    doi: str
    folder: str
    id: Optional[int] = None
    title: Optional[str] = None


@dataclass
class Attempt:
    url: str
    method: str
    status: str


@dataclass
class Result:
    doi: str
    folder: str
    id: Optional[int]
    title: Optional[str]
    status: str
    file: str
    source_url: Optional[str]
    attempts: List[Dict[str, str]]
    size_bytes: int


class Downloader:
    def __init__(self, timeout: int = 45, sleep_sec: float = 0.2):
        self.timeout = timeout
        self.sleep_sec = sleep_sec
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
                ),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            }
        )
        self.scraper = None

    def _ensure_scraper(self):
        if self.scraper is not None:
            return self.scraper
        try:
            import cloudscraper  # type: ignore

            self.scraper = cloudscraper.create_scraper(
                browser={"browser": "chrome", "platform": "darwin", "desktop": True}
            )
            return self.scraper
        except Exception:
            self.scraper = False
            return None

    @staticmethod
    def is_pdf(content: bytes, content_type: str) -> bool:
        ct = (content_type or "").lower()
        if "application/pdf" in ct:
            return True
        return content.startswith(b"%PDF-")

    def fetch(self, url: str, headers: Optional[Dict[str, str]] = None):
        return self.session.get(url, headers=headers or {}, allow_redirects=True, timeout=self.timeout)

    def fetch_scraper(self, url: str, headers: Optional[Dict[str, str]] = None):
        scraper = self._ensure_scraper()
        if not scraper:
            return None
        return scraper.get(url, headers=headers or {}, allow_redirects=True, timeout=self.timeout)

    def extract_candidates_from_html(self, html: str, base_url: str) -> List[str]:
        out: List[str] = []

        for m in CITATION_PDF_META_RE.findall(html):
            out.append(urljoin(base_url, m.strip()))

        # Publisher-specific patterns (high priority)
        for m in MDPI_PDF_RE.findall(html):
            out.append(m)
        for m in OUP_PDF_RE.findall(html):
            out.append(m)
        for m in HINDAWI_PDF_RE.findall(html):
            out.append(m)

        for m in HREF_RE.findall(html):
            u = urljoin(base_url, m.strip())
            if "pdf" in u.lower() or "/epdf/" in u.lower() or "/doi/pdf/" in u.lower():
                out.append(u)

        for m in HTTP_RE.findall(html):
            if "pdf" in m.lower():
                out.append(m)

        return dedupe(out)

    def openalex_candidates(self, doi: str) -> List[str]:
        url = f"https://api.openalex.org/works/https://doi.org/{doi}"
        try:
            r = self.fetch(url)
            if r.status_code != 200:
                return []
            j = r.json()
        except Exception:
            return []

        cands: List[str] = []

        def push(u: Optional[str]):
            if u and isinstance(u, str):
                cands.append(u)

        push((j.get("open_access") or {}).get("oa_url"))
        push((j.get("best_oa_location") or {}).get("pdf_url"))
        push((j.get("best_oa_location") or {}).get("landing_page_url"))
        push((j.get("primary_location") or {}).get("pdf_url"))
        push((j.get("primary_location") or {}).get("landing_page_url"))

        for loc in j.get("locations") or []:
            push((loc or {}).get("pdf_url"))
            push((loc or {}).get("landing_page_url"))

        return dedupe(cands)

    def crossref_candidates(self, doi: str) -> List[str]:
        url = f"https://api.crossref.org/works/{doi}"
        try:
            r = self.fetch(url)
            if r.status_code != 200:
                return []
            msg = r.json().get("message", {})
        except Exception:
            return []

        cands: List[str] = []
        for lk in msg.get("link") or []:
            u = lk.get("URL")
            if u:
                cands.append(u)

        rel = msg.get("relation") or {}
        for rel_key in ["has-preprint", "is-preprint-of"]:
            for v in rel.get(rel_key) or []:
                d = v.get("id")
                if d:
                    cands.append(f"https://doi.org/{d}")
                    if d.startswith("10.1101/"):
                        cands.append(f"https://www.biorxiv.org/content/{d}v1.full.pdf")
                        cands.append(f"https://www.biorxiv.org/content/{d}v2.full.pdf")
                        cands.append(f"https://www.biorxiv.org/content/{d}v3.full.pdf")

        return dedupe(cands)

    def pmc_candidates(self, doi: str) -> List[str]:
        cands: List[str] = []

        # Try NCBI idconv first
        try:
            url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids={doi}&idtype=doi&format=json"
            r = self.fetch(url)
            if r.status_code == 200:
                rec = (r.json().get("records") or [{}])[0]
                pmcid = rec.get("pmcid")
                if pmcid:
                    cands.append(f"https://europepmc.org/articles/{pmcid}?pdf=render")
                    cands.append(f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmcid}&blobtype=pdf")
        except Exception:
            pass

        # Fallback: Europe PMC direct search (bypasses NCBI, works when NCBI times out)
        if not cands:
            try:
                r = self.fetch(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{doi}&format=json")
                if r.status_code == 200:
                    results = (r.json().get("resultList") or {}).get("result") or []
                    for rec in results:
                        pmcid = rec.get("pmcid")
                        if pmcid:
                            cands.append(f"https://europepmc.org/articles/{pmcid}?pdf=render")
                            cands.append(f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmcid}&blobtype=pdf")
                            break
            except Exception:
                pass

        return dedupe(cands)

    def unpaywall_candidates(self, doi: str) -> List[str]:
        cands: List[str] = []
        try:
            r = self.fetch(f"https://api.unpaywall.org/v2/{doi}?email=test@example.com")
            if r.status_code != 200:
                return []
            data = r.json()
            for loc in [data.get("best_oa_location")] + (data.get("oa_locations") or []):
                if not isinstance(loc, dict):
                    continue
                for key in ("url_for_pdf", "url"):
                    u = loc.get(key)
                    if isinstance(u, str) and u:
                        cands.append(u)
        except Exception:
            pass
        return dedupe(cands)

    def semantic_scholar_candidates(self, doi: str) -> List[str]:
        cands: List[str] = []
        try:
            r = self.fetch(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}?fields=openAccessPdf")
            if r.status_code == 200:
                oa = r.json().get("openAccessPdf") or {}
                u = oa.get("url")
                if isinstance(u, str) and u:
                    cands.append(u)
        except Exception:
            pass
        return cands

    def publisher_guess_candidates(self, doi: str, landing_url: Optional[str]) -> List[str]:
        cands: List[str] = []

        # Science
        cands.append(f"https://www.science.org/doi/pdf/{doi}?download=true")
        cands.append(f"https://www.science.org/doi/pdf/{doi}")
        cands.append(f"https://www.science.org/doi/epdf/{doi}")

        # ACS
        if doi.startswith("10.1021/"):
            cands.append(f"https://pubs.acs.org/doi/pdf/{doi}")

        # MDPI (open access): DOI 10.3390/<journal_code> -> /pdf endpoint
        if doi.startswith("10.3390/"):
            cands.append(f"https://doi.org/{doi}")  # resolves to mdpi.com landing, then append /pdf

        # Future Medicine
        if doi.startswith("10.2217/"):
            cands.append(f"https://www.futuremedicine.com/doi/pdf/{doi}?download=true&needAccess=true")

        if landing_url:
            u = landing_url.rstrip("/")
            lu = u.lower()

            # Nature
            if "nature.com/articles/" in lu and not lu.endswith(".pdf"):
                cands.append(u + ".pdf")

            # Science
            if "science.org/doi/" in lu and "/doi/pdf/" not in lu:
                cands.append(u.replace("/doi/", "/doi/pdf/") + "?download=true")
                cands.append(u.replace("/doi/", "/doi/pdf/"))
                cands.append(u.replace("/doi/", "/doi/epdf/"))

            # Cell
            if "cell.com/" in lu and not lu.endswith(".pdf"):
                cands.append(u + "/pdf")
                cands.append(u + ".pdf")

            # PNAS
            if "pnas.org/" in lu and "/doi/pdf/" not in lu:
                cands.append(u.replace("/doi/", "/doi/pdf/"))

            # MDPI: landing is mdpi.com/ISSN/vol/issue/article -> append /pdf
            if "mdpi.com/" in lu and "/pdf" not in lu:
                cands.append(u + "/pdf")

            # ACS
            if "pubs.acs.org/doi/" in lu:
                cands.append(f"https://pubs.acs.org/doi/pdf/{doi}")

            # Wiley: epdf and pdfdirect
            m_wiley = WILEY_HOST_RE.match(landing_url)
            if m_wiley:
                host = m_wiley.group(1)
                cands.append(f"https://{host}/doi/epdf/{doi}")
                cands.append(f"https://{host}/doi/pdfdirect/{doi}?download=true")

            # Elsevier: extract PII -> pdfft
            if "elsevier.com/" in lu or "sciencedirect.com/" in lu:
                m_pii = ELSEVIER_PII_RE.search(landing_url)
                if m_pii:
                    pii = m_pii.group(1)
                    cands.append(f"https://www.sciencedirect.com/science/article/pii/{pii}/pdfft?isDTMRedir=true&download=true")

            # OUP
            if "academic.oup.com/" in lu:
                cands.append(u.replace("/article/", "/article-pdf/") + ".pdf")

            # Hindawi (may resolve to Wiley but PDF on downloads.hindawi.com)
            if "hindawi.com/" in lu or "10.1155/" in doi:
                # article_id is the last numeric segment of DOI
                parts = doi.split("/")
                if len(parts) >= 2:
                    article_id = parts[-1]
                    cands.append(f"https://downloads.hindawi.com/journals/jir/{article_id}.pdf")
                    cands.append(f"https://downloads.hindawi.com/journals/bmri/{article_id}.pdf")
                    cands.append(f"https://downloads.hindawi.com/journals/omcl/{article_id}.pdf")

            # Future Medicine
            if "futuremedicine.com/" in lu:
                cands.append(f"https://www.futuremedicine.com/doi/pdf/{doi}?download=true&needAccess=true")

        return dedupe(cands)

    def try_save_pdf(self, url: str, out_path: Path, method: str, referer: Optional[str] = None, accept_pdf: bool = False) -> Tuple[bool, str, Optional[str]]:
        headers: Dict[str, str] = {}
        if referer:
            headers["Referer"] = referer
        if accept_pdf:
            headers["Accept"] = "application/pdf"

        # Try requests first
        try:
            r = self.fetch(url, headers=headers)
            if self.is_pdf(r.content[:8], r.headers.get("Content-Type", "")):
                out_path.write_bytes(r.content)
                return True, f"ok:{method}:requests:{r.status_code}", r.url
        except Exception as e:
            _ = e

        # Cloudflare fallback
        try:
            rs = self.fetch_scraper(url, headers=headers)
            if rs is not None and self.is_pdf(rs.content[:8], rs.headers.get("Content-Type", "")):
                out_path.write_bytes(rs.content)
                return True, f"ok:{method}:cloudscraper:{rs.status_code}", rs.url
        except Exception as e:
            _ = e

        return False, f"fail:{method}", None

    def download_one(self, item: Item, base_dir: Path, overwrite: bool = False) -> Result:
        folder_dir = base_dir / item.folder
        folder_dir.mkdir(parents=True, exist_ok=True)
        out_pdf = folder_dir / "paper.pdf"

        if out_pdf.exists() and not overwrite:
            try:
                head = out_pdf.read_bytes()[:5]
                if head == b"%PDF-":
                    return Result(
                        doi=item.doi,
                        folder=item.folder,
                        id=item.id,
                        title=item.title,
                        status="exists",
                        file=str(out_pdf),
                        source_url=None,
                        attempts=[],
                        size_bytes=out_pdf.stat().st_size,
                    )
            except Exception:
                pass

        attempts: List[Attempt] = []
        source_url = None

        doi_url = f"https://doi.org/{item.doi}"
        landing_url = None
        landing_html = ""

        # A) DOI with PDF accept header
        ok, msg, final_url = self.try_save_pdf(
            doi_url,
            out_pdf,
            method="doi_accept_pdf",
            referer=None,
            accept_pdf=True,
        )
        attempts.append(Attempt(doi_url, "doi_accept_pdf", msg))
        if ok:
            source_url = final_url or doi_url
            return self._ok_result(item, out_pdf, attempts, source_url)

        # B) landing page parse
        try:
            lr = self.fetch(doi_url)
            landing_url = lr.url
            landing_html = lr.text or ""
            cands = self.extract_candidates_from_html(landing_html, landing_url)
            for c in dedupe(cands + self.publisher_guess_candidates(item.doi, landing_url)):
                ok, msg, final_url = self.try_save_pdf(c, out_pdf, method="landing_or_guess", referer=landing_url)
                attempts.append(Attempt(c, "landing_or_guess", msg))
                if ok:
                    source_url = final_url or c
                    return self._ok_result(item, out_pdf, attempts, source_url)
        except Exception as e:
            attempts.append(Attempt(doi_url, "landing", f"error:{type(e).__name__}"))

        # C) OpenAlex/Crossref/PMC/Unpaywall/Semantic Scholar
        meta_candidates = []
        meta_candidates.extend(self.openalex_candidates(item.doi))
        meta_candidates.extend(self.crossref_candidates(item.doi))
        meta_candidates.extend(self.pmc_candidates(item.doi))
        meta_candidates.extend(self.unpaywall_candidates(item.doi))
        meta_candidates.extend(self.semantic_scholar_candidates(item.doi))
        meta_candidates.extend(self.publisher_guess_candidates(item.doi, landing_url))

        for c in dedupe(meta_candidates):
            ok, msg, final_url = self.try_save_pdf(c, out_pdf, method="meta_fallback", referer=landing_url)
            attempts.append(Attempt(c, "meta_fallback", msg))
            if ok:
                source_url = final_url or c
                return self._ok_result(item, out_pdf, attempts, source_url)

        return Result(
            doi=item.doi,
            folder=item.folder,
            id=item.id,
            title=item.title,
            status="not_found",
            file=str(out_pdf),
            source_url=None,
            attempts=[asdict(a) for a in attempts[-20:]],
            size_bytes=out_pdf.stat().st_size if out_pdf.exists() else 0,
        )

    @staticmethod
    def _ok_result(item: Item, out_pdf: Path, attempts: Sequence[Attempt], source_url: str) -> Result:
        size = out_pdf.stat().st_size if out_pdf.exists() else 0
        return Result(
            doi=item.doi,
            folder=item.folder,
            id=item.id,
            title=item.title,
            status="downloaded",
            file=str(out_pdf),
            source_url=source_url,
            attempts=[asdict(a) for a in attempts[-20:]],
            size_bytes=size,
        )


def dedupe(values: Iterable[str]) -> List[str]:
    out: List[str] = []
    seen = set()
    for v in values:
        if not v:
            continue
        if v in seen:
            continue
        seen.add(v)
        out.append(v)
    return out


def parse_markdown_items(path: Path) -> List[Item]:
    items: List[Item] = []
    cur_doi: Optional[str] = None
    cur_folder: Optional[str] = None
    cur_id: Optional[int] = None
    cur_title: Optional[str] = None

    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()

        # id + title in heading line
        m_head = re.search(r"^###\s*\[(\d+)\]\s*(.+)$", line)
        if m_head:
            if cur_doi and cur_folder:
                items.append(Item(doi=cur_doi, folder=cur_folder, id=cur_id, title=cur_title))
                cur_doi = None
                cur_folder = None
            cur_id = int(m_head.group(1))
            cur_title = m_head.group(2).strip()

        m_doi = DOI_RE.search(line)
        if m_doi:
            cur_doi = m_doi.group(0).strip().rstrip(".")

        m_folder = FOLDER_BACKTICK_RE.search(line)
        if m_folder:
            folder = m_folder.group(1).strip()
            if folder.startswith("["):
                cur_folder = folder

        if cur_doi and cur_folder:
            items.append(Item(doi=cur_doi, folder=cur_folder, id=cur_id, title=cur_title))
            cur_doi = None
            cur_folder = None

    return items


def parse_csv_items(path: Path, delimiter: str = ",") -> List[Item]:
    items: List[Item] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        rd = csv.DictReader(f, delimiter=delimiter)
        for row in rd:
            doi = (row.get("doi") or row.get("DOI") or "").strip()
            folder = (row.get("folder") or row.get("Folder") or row.get("dir") or "").strip()
            if not doi or not folder:
                continue
            id_val = row.get("id") or row.get("ID") or None
            items.append(Item(doi=doi, folder=folder, id=int(id_val) if str(id_val).isdigit() else None, title=row.get("title")))
    return items


def parse_json_items(path: Path) -> List[Item]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(raw, dict):
        raw = raw.get("items") or []
    items: List[Item] = []
    for row in raw:
        doi = str(row.get("doi", "")).strip()
        folder = str(row.get("folder", "")).strip()
        if not doi or not folder:
            continue
        id_val = row.get("id")
        items.append(Item(doi=doi, folder=folder, id=int(id_val) if isinstance(id_val, int) else None, title=row.get("title")))
    return items


def parse_plain_doi_list(path: Path) -> List[Item]:
    """Parse plain text file with one DOI (or DOI URL) per line."""
    items: List[Item] = []
    for i, raw in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = DOI_RE.search(line)
        if m:
            doi = m.group(0).strip().rstrip(".")
            safe = re.sub(r"[/\\:*?\"<>|]", "_", doi)
            items.append(Item(doi=doi, folder=f"{i:03d}-{safe}", id=i))
    return items


def load_items(path: Path) -> List[Item]:
    ext = path.suffix.lower()
    if ext == ".json":
        items = parse_json_items(path)
    elif ext == ".csv":
        items = parse_csv_items(path, delimiter=",")
    elif ext == ".tsv":
        items = parse_csv_items(path, delimiter="\t")
    elif ext == ".txt":
        items = parse_plain_doi_list(path)
    else:
        items = parse_markdown_items(path)

    # normalize and dedupe by (doi,folder)
    uniq: Dict[Tuple[str, str], Item] = {}
    for it in items:
        doi = it.doi.lower().strip()
        if doi.startswith("https://doi.org/"):
            doi = doi.split("https://doi.org/", 1)[1]
        it.doi = doi
        uniq[(it.doi, it.folder)] = it

    return list(uniq.values())


def write_md_report(path: Path, results: Sequence[Result]):
    now = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ok = sum(1 for r in results if r.status in ("downloaded", "exists"))

    with path.open("w", encoding="utf-8") as f:
        f.write(f"# Paper Download Report\n\nUpdated: {now}\n\n")
        f.write(f"Success: {ok}/{len(results)}\n\n")
        f.write("| id | folder | doi | status | size_bytes | source_url |\n")
        f.write("|---|---|---|---|---:|---|\n")
        for r in sorted(results, key=lambda x: (x.id if x.id is not None else 10**9, x.folder)):
            rid = f"[{r.id}]" if r.id is not None else "-"
            src = (r.source_url or "").replace("|", "%7C")
            f.write(f"| {rid} | {r.folder} | {r.doi} | {r.status} | {r.size_bytes} | {src} |\n")


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Batch download papers by DOI into mapped folders")
    p.add_argument("--items-file", required=True, help="Input file (.md/.csv/.tsv/.json) with DOI and folder mapping")
    p.add_argument("--base-dir", required=True, help="Base directory containing target subfolders")
    p.add_argument("--overwrite", action="store_true", help="Overwrite existing valid paper.pdf")
    p.add_argument("--timeout", type=int, default=45, help="HTTP timeout seconds")
    p.add_argument("--sleep", type=float, default=0.2, help="Sleep seconds between items (serial mode only)")
    p.add_argument("--workers", type=int, default=8, help="Parallel download workers (default 8, set 1 for serial)")
    p.add_argument("--report-json", default="_download_report.json", help="JSON report filename or absolute path")
    p.add_argument("--report-md", default="_download_report.md", help="Markdown report filename or absolute path")
    return p


def resolve_report_path(base_dir: Path, value: str) -> Path:
    p = Path(value)
    return p if p.is_absolute() else base_dir / p


def main() -> int:
    args = build_arg_parser().parse_args()
    items_file = Path(args.items_file).expanduser().resolve()
    base_dir = Path(args.base_dir).expanduser().resolve()

    if not items_file.exists():
        print(f"ERROR: items file not found: {items_file}", file=sys.stderr)
        return 2
    if not base_dir.exists():
        print(f"ERROR: base dir not found: {base_dir}", file=sys.stderr)
        return 2

    items = load_items(items_file)
    if not items:
        print("ERROR: no valid items parsed (need doi + folder)", file=sys.stderr)
        return 2

    workers = max(1, args.workers)
    results: List[Result] = []
    t0 = time.time()

    print(f"Start download: {len(items)} items, {workers} worker(s)")

    if workers == 1:
        # Serial mode
        dl = Downloader(timeout=args.timeout, sleep_sec=args.sleep)
        for i, it in enumerate(items, start=1):
            label = f"[{it.id}]" if it.id is not None else f"#{i}"
            print(f"{i}/{len(items)} {label} {it.doi} -> {it.folder}")
            res = dl.download_one(it, base_dir=base_dir, overwrite=args.overwrite)
            results.append(res)
            print(f"  status={res.status} size={res.size_bytes} source={res.source_url or '-'}")
            time.sleep(args.sleep)
    else:
        # Parallel mode
        def _download_one(item: Item) -> Result:
            dl = Downloader(timeout=args.timeout, sleep_sec=0)
            return dl.download_one(item, base_dir=base_dir, overwrite=args.overwrite)

        done_count = 0
        ok_count = 0
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(_download_one, it): it for it in items}
            for future in as_completed(futures):
                it = futures[future]
                done_count += 1
                try:
                    res = future.result()
                    results.append(res)
                    if res.status in ("downloaded", "exists"):
                        ok_count += 1
                    elapsed = time.time() - t0
                    eta = elapsed / done_count * (len(items) - done_count)
                    print(f"[{done_count}/{len(items)}] {res.status:12s} {it.doi[:55]}  "
                          f"({ok_count} ok, ETA {eta:.0f}s)")
                except Exception as e:
                    print(f"[{done_count}/{len(items)}] ERROR {it.doi}: {e}")
                    results.append(Result(
                        doi=it.doi, folder=it.folder, id=it.id, title=it.title,
                        status="error", file="", source_url=None,
                        attempts=[{"error": str(e)}], size_bytes=0,
                    ))

    rj = resolve_report_path(base_dir, args.report_json)
    rm = resolve_report_path(base_dir, args.report_md)

    rj.write_text(json.dumps([asdict(r) for r in results], ensure_ascii=False, indent=2), encoding="utf-8")
    write_md_report(rm, results)

    ok = sum(1 for r in results if r.status in ("downloaded", "exists"))
    elapsed = time.time() - t0
    print(f"\nDone: {ok}/{len(results)} success in {elapsed:.0f}s ({workers} workers)")
    print(f"JSON report: {rj}")
    print(f"MD report:   {rm}")

    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
