---
name: 精练
description: 给定一篇论文（PDF 或清洗后的 MD）+ 一份项目 context 文件，精读全文，把对你论点承重的整段原文逐字打捞、连出处与所触论点一起索引，解析元数据与一手引用，输出一份**规范化 JSON「源索引」**（excerpt-centric，纯英文键与注解，可回溯原文），直接作为下游 outline 与全文写作 agent / 聚合脚本的结构化输入。高召回抽取、低解读、可回溯原文、机读优先。触发：'精练'/'精练这篇论文'/'帮我精练'/'提炼文献'/'distill this paper'/给一个论文路径+context 路径说想精练。
---

# 精练 4.0 → Structured Source Index (JSON, excerpt-centric, English-only authored fields)

> **What changed from 3.0:** the output is no longer a Markdown note — it is **one normalized JSON file**, the single source of truth. The extraction work (Steps 1–6) is unchanged; only the *shape* of the output changes, so downstream aggregation needs no per-paper re-parsing agent. JSON is machine-keyed, so a transposition/audit script can collate the same claim across all papers deterministically. There is **no `strength` field** (that is a downstream, cross-paper judgment, not this skill's call) and **no second Markdown artifact** (render one on demand from the JSON if a human needs to read it).

## Design principle — who consumes this, and what that demands

The consumer is **(a)** a deterministic aggregation script that transposes excerpts by claim and builds an evidence matrix, and **(b)** a chain of capable agents (outline → writing) that read MANY of these at once with the **raw cleaned sources on disk**. That dictates the shape:

1. **High-recall EXTRACTION, not interpretation.** Surface the exact load-bearing lines (with provenance), resolve metadata, point to primary sources. Do **not** pre-write the argument, do **not** compose sample rewrites, do **not** assign a strength/verdict, do **not** lock a paper into a single role. A pre-baked conclusion *anchors* an equally-smart downstream agent, *homogenizes* prose, and *freezes in* your reading errors. Give clean material, not verdicts.

2. **The file is an INDEX into the raw, not a replacement.** Record the source path; use the paper's own section names as `anchor`s so a downstream agent can jump back. Because raw is reachable, stay lean: capture every relevant quote, carry no prose the agent could regenerate.

3. **Grounding comes from the project context file — you READ it, you never invent it.** Our thesis, our claim/evidence roadmap, and our scope boundaries live in a separate context file passed at runtime. Judge every excerpt against *that file's* claims. The allowed `claimId` values are **the context file's own claim/axis identifiers**, plus the literal escape hatch `"Other"`. If no context file is given, ask for it.

4. **The excerpt→touchpoint mapping is the load-bearing feature.** Each verbatim excerpt carries its own `touchpoints` (which roadmap claims it bears on, and in which direction). This *merges* 3.0's separate "Load-Bearing Excerpts" + "Claim Touchpoints router" into one structure, so the two can never drift out of sync. That is exactly what lets a downstream script aggregate evidence *per claim, across all papers*.

> **Rule of thumb:** per token, a verbatim quote is worth far more to this consumer than a sentence of your analysis. The file is **dense in quotes, light in conclusions.** Brevity comes from cutting interpretation and off-scope material — never from rationing relevant quotes.

> ⚠️ **The output is a single valid JSON file (UTF-8).** All **keys** and all **authored** string values (`oneSentence`, `orientation`, `note`, `flags`) must be in **English — zero Chinese**. The only non-ASCII permitted is *inside* a value that is genuinely non-ASCII in the source: the `sourceFile` path, and verbatim names/quotes that contain accented characters (e.g. "Ståhl", "Csárdi"). Your chat reasoning can be Chinese; the *file* cannot, except for those unavoidable in-value cases.

---

## Inputs (two — both required)

1. **The paper** — a PDF or a cleaned `…_cleaned.md`.
2. **The project context file** — a Markdown file describing the paper *we* are writing: its thesis, its claim/evidence roadmap, its organizing axes, and its scope boundaries (what NOT to collect). **Read it first and treat its claim list as the routing keys.** If the user gives a paper but no context file, ask for the context-file path before proceeding — do not reconstruct our thesis from memory.

**Output file:** `<source-basename>_refined.json`, saved **in the same folder as the source**. If the source location is unclear, fall back to `~/Desktop/`.

---

## Workflow

### Step 1 — Read the context file, lock the grounding
Read the project context file end to end. Extract and hold:
- **Our thesis** (the one claim the paper defends).
- **The claim / evidence roadmap** — the list of points we collect literature for. **These are your routing keys**, and the *exact* identifiers (e.g. its numbered claims `Claim 1…N`, and its organizing axes such as modality / temporal / spatial / standard) become the allowed `claimId` values. Copy them verbatim; do not invent or renumber.
- **Scope boundaries** — what the paper explicitly will NOT cover. Anything that falls only under an out-of-scope topic is **filler — do not capture it** (unless it doubles as a skeptical/counter line bearing on a roadmap claim).

### Step 2 — Ingest the paper
- **Cleaned MD**: `Read` it directly (preferred). **Record its absolute path** for `sourceFile`.
- **PDF**: `pdftotext "<path>.pdf" "<path>.txt"`, then `Read` the `.txt`; also `Read` the PDF (`pages`, ≤20/call) for figures and section boundaries.

### Step 3 — Forced metadata scan (do not eyeball the header)
DOI, received/accepted/published dates, and sometimes the venue live at the END of the body or before the references. Explicitly scan:
- `grep -nE '10\.[0-9]{4,}/' <source>` for the DOI.
- `grep -niE 'received|accepted|published|doi' <source>` for dates/venue clues; check self-citations for venue.
Anything you cannot confirm from the text → a `flags` entry, never asserted as fact in `venue`/`doi` (use `"unverified; see flags"` / `null` there).

### Step 4 — Read the whole paper, build a map
Read end to end. Identify the central claim, where the real evidence is, which figures/tables are load-bearing, the limitations the authors concede, and **where the paper discusses the very problems our thesis is about** — these are highest value whether they agree with us or not.

### Step 5 — High-recall capture (the core step)
Run **each roadmap claim from the context file** as a coverage checklist. For each, ask: does the paper state anything bearing on it? Capture the **exact line** whether it **supports or contradicts** us. Then sweep these high-value categories:
- **Precise quantitative statements** (numbers are the most citable) — also record them in `figuresNumbers`.
- **Author-conceded limitations / trade-offs / "we cannot…" admissions.**
- **The paper proposing the very approach we critique, or conceding the very fact we build on** — these counter/conceded lines are often the single most valuable quotes; a downstream agent can deploy them as support OR as a named opponent. **Do not sanitize into all-agreement** — that is the most common failure and it strips the writer's best material.

Copy everything **verbatim** — exact wording, keep OCR quirks as-is, do not fix them. **Relevance to a roadmap claim is the gate: cut everything off-roadmap (no filler), but capture every on-roadmap line even if that's 15–25 of them.** No arbitrary count cap.

For each captured excerpt, build its `touchpoints`: one `{claimId, direction}` per roadmap claim it bears on. The **same excerpt may support one claim and challenge another** — emit a separate touchpoint per (claim, direction). `direction ∈ supports | challenges | nuances`. Use `claimId: "Other"` (with an `otherLabel`) **only** for a genuinely new angle that fits no roadmap id — be conservative.

> **Do NOT restamp the same `(claimId, direction)` across many excerpts that make the *same* point.** Tag a (claim, direction) on an excerpt only when that excerpt adds **new** evidence for it. If a paper's central thesis is itself a foil to (or strong support for) one of our claims, capture its few **strongest distinct** statements of that — not every sentence that echoes it. High recall means covering many *different* points; it does NOT mean repeating one point N times. A downstream script counts these touchpoints to build an evidence matrix, so near-duplicate touchpoints from one paper flood and distort it.

### Step 6 — Resolve primary sources behind key quotes
For each load-bearing quote that cites a primary paper, look it up in the reference list and record the real citation (`Author Year, Journal Vol:Pages`, `refN`) so the writer cites first-hand. Never list a source whose link to the quote you doubt — put doubts in `flags` instead.

### Step 7 — Write the JSON file
Emit `<basename>_refined.json` (schema below) via `Write`. Before saving: validate it is **well-formed JSON**, and re-scan authored fields for stray Chinese.

---

## Output Schema

```json
{
  "schemaVersion": "精练-4.0",
  "citationKey": "string — the leading id of the source filename if it is a clear id (e.g. \"04\", \"08a\"); else null",
  "title": "string — full paper title, verbatim",
  "authors": "string — exactly as printed; if the source gives only initials, KEEP initials",
  "venue": "string — \"Name, Year, Vol(Issue):Pages\"  OR  \"unverified; see flags\"",
  "year": "string",
  "doi": "string \"doi:...\"  OR  null",
  "readOn": "YYYY-MM-DD",
  "sourceFile": "string — absolute path to the source (raw on disk; anchors below jump back)",
  "oneSentence": "string — what the paper did + its main finding. Plain description; no positioning.",
  "orientation": "string — 1-3 sentences: where this paper sits vs our thesis, which roadmap claims/axes it most likely feeds; if it can serve as BOTH support and foil, say so. A ROUTING HINT, non-binding.",
  "excerpts": [
    {
      "id": "e1",
      "text": "string — the EXACT quote, unaltered (keep OCR quirks)",
      "anchor": "string — Section name / p.X (jump-back anchor)",
      "touchpoints": [
        { "claimId": "string — a context-file claim/axis id, or \"Other\"", "direction": "supports | challenges | nuances", "otherLabel": "string — REQUIRED iff claimId == \"Other\", else omit" }
      ],
      "note": "string — one neutral clause: what the paper claims here"
    }
  ],
  "figuresNumbers": [
    { "item": "string — e.g. \"Table 1\", \"Fig. 2\", or a metric name", "contains": "string — factual description / the numbers" }
  ],
  "primarySources": [
    { "topic": "string — what the quote is about", "citation": "string — Author Year, Journal Vol:Pages", "refN": "string — e.g. \"12\"  OR null" }
  ],
  "flags": [
    "string — e.g. 'Metadata unverified: venue inferred from DOI prefix', 'Read at source: ref #6 worth first-hand', 'Source inconsistency: ...', 'Scope note: ...'"
  ]
}
```

**Notes on the schema:**
- `excerpts` is the heart — it is **excerpt-centric**: one entry per verbatim quote, carrying its own `touchpoints`. A downstream script transposes (excerpt × touchpoint) → per-claim evidence rows.
- Capture EVERY on-roadmap excerpt, including lines that cut against us. No filler, no paraphrase, no "how to use", no sample rewrites.
- `figuresNumbers`: omit (empty array) if nothing on-roadmap. Numbers belong here AND, when quoted verbatim, also as an excerpt.
- `primarySources`: omit (empty array) if the paper is itself the primary source. Never list a source whose link to a quote is in doubt.
- No `strength` field anywhere. No second Markdown file.

---

## Quality Rules

**Extraction (do more):**
- **Verbatim is verbatim.** Never paraphrase — one changed word misrepresents the source. Keep OCR quirks; flag them.
- **High recall on roadmap-relevant lines.** Run every context-file claim as a checklist; capture counter-evidence as eagerly as support. An all-"supports" file has missed the writer's best material.
- **Numbers first.** Never drop quantitative results.
- **Resolve primary sources** behind key quotes so the writer can cite first-hand.

**Interpretation (do less — this is the point):**
- **No pre-written argument**, no sample rewrites, no "how the writer should phrase it."
- **No strength / no verdicts.** `direction` is a one-word routing tag (supports/challenges/nuances) — nothing more. Do not rank or weight.
- **No locked roles.** `orientation` is one non-binding hint; never pre-commit a paper to foil/ally as settled.
- **No restamping.** One `(claimId, direction)` per *distinct* piece of evidence; do not stamp a paper's central theme onto every excerpt that touches it (that floods the downstream matrix with near-duplicates). Strongest few distinct statements, not every echo.
- **`note` stays neutral and descriptive** — "what the paper claims here," not "deploy this to crush the opposition."

**Honesty (never violate):**
- **No hallucinated metadata or citations.** Initials stay initials. Unconfirmed venue/DOI → `flags` + `"unverified; see flags"`/`null`, never asserted. Uncertain page → `(approx. p.X)` inside the `anchor`. Reconstructions labeled as such, in `flags`.
- **Scope discipline.** Out-of-scope topics (per the context file) are not captured unless they double as a counter line on a roadmap claim.
- **Valid JSON, English authored fields.** Validate well-formedness; re-scan `oneSentence`/`orientation`/`note`/`flags` for Chinese before saving.
- **Always Write the file** — don't just print to chat.
```
