---
name: 精练3.0
description: 给定一篇论文（PDF 或清洗后的 MD）+ 一份项目 context 文件，精读全文，把对论点承重的整段原文逐字打捞、连出处与所触论点一起索引，解析元数据与一手引用，输出一份纯英文的「源索引（Source Index）」中间产物，直接作为下游 outline 与全文写作 agent 的输入。高召回抽取、低解读、可回溯原文。3.0 相对 2.0 的转向：不再预写论点/示范改写/锁定论文角色（Ally/Foil），改为中立索引 + claim-touchpoint 路由表，且强制要求传入独立 context 文件作为路由键（缺失则先索要）。触发：'精练3.0'/'精练这篇论文3.0'/'帮我精练3.0'/'用3.0精练'/'distill this paper 3.0'/给一个论文路径+context 路径说想用3.0精练。
---

# 精练 → Source Index for downstream outline & writing agents (English-only output)

## Design principle — who consumes this, and what that demands

The consumer is a **chain of highly capable agents** (Opus-class): first an **outline agent** that buckets evidence across many papers, then a **writing agent** that drafts from those buckets. Both read MANY of these notes at once and have the **raw cleaned sources on disk**. That dictates the shape:

1. **High-recall EXTRACTION, not interpretation.** Surface the exact load-bearing lines (with provenance), resolve metadata, point to primary sources. Do **not** pre-write the argument, do **not** compose sample rewrites, do **not** lock a paper into a single role. A pre-baked conclusion *anchors* an equally-smart downstream agent, *homogenizes* prose across many notes, and *freezes in* your reading errors. Give clean material, not verdicts.

2. **The note is an INDEX into the raw, not a replacement.** Record the source path and use the paper's own section names as anchors so the downstream agent can jump back. Because raw is reachable, the note stays lean: capture every relevant quote, carry no prose the agent could regenerate.

3. **Grounding comes from the project context file — you READ it, you never invent it.** Our thesis, our claim/evidence roadmap, and our scope boundaries live in a separate context file passed in at runtime. Judge every excerpt against *that file's* claims. Never guess our argument; if no context file is given, ask for it.

4. **The claim-touchpoint router is the load-bearing feature.** It maps our roadmap claims → the excerpts that touch them. That is exactly what lets the downstream outline agent aggregate evidence *per claim, across all papers*. Make it accurate and keyed to the context file's own claim/axis identifiers.

> **Rule of thumb:** per token, a verbatim quote is worth far more to this consumer than a paragraph of your analysis. The note is **dense in quotes, light in conclusions.** Brevity comes from cutting interpretation and off-scope material — never from rationing relevant quotes.

> ⚠️ **The entire output file must be in English. Zero Chinese characters** — not in headings, metadata, notes, or comments. (Your chat reasoning can be Chinese; the *file* cannot. The one unavoidable exception is a non-ASCII character inside the literal source file path.)

---

## Inputs (two — both required)

1. **The paper** — a PDF or a cleaned `…_cleaned.md`.
2. **The project context file** — a Markdown file describing the paper *we* are writing: its thesis, its claim/evidence roadmap, its organizing axes, and its scope boundaries (what NOT to collect). This replaces any hand-filled template. **Read it first and treat its claim list as the routing keys.** If the user gives a paper but no context file, ask for the context-file path before proceeding — do not reconstruct our thesis from memory.

**Output file:** `<source-basename>_refined.md`, saved **in the same folder as the source**. If the source location is unclear, fall back to `~/Desktop/`.

---

## Workflow

### Step 1 — Read the context file, lock the grounding
Read the project context file end to end. Extract and hold:
- **Our thesis** (the one claim the paper defends).
- **The claim / evidence roadmap** — the list of points we collect literature for. **These are your routing keys.** Use the file's own identifiers (e.g. its numbered claims, and its organizing axes such as modality / temporal / spatial / standard). Do **not** invent section numbers the paper hasn't committed to yet.
- **Scope boundaries** — what the paper explicitly will NOT cover. Anything that falls only under an out-of-scope topic is **filler — do not capture it** (unless it doubles as a skeptical/counter line bearing on a roadmap claim).

### Step 2 — Ingest the paper
- **Cleaned MD**: `Read` it directly (preferred). **Record its absolute path** for the note header.
- **PDF**: `pdftotext "<path>.pdf" "<path>.txt"`, then `Read` the `.txt`; also `Read` the PDF (`pages`, ≤20/call) for figures and section boundaries.

### Step 3 — Forced metadata scan (do not eyeball the header)
DOI, received/accepted/published dates, and sometimes the venue live at the END of the body or before the references. Explicitly scan:
- `grep -nE '10\.[0-9]{4,}/' <source>` for the DOI.
- `grep -niE 'received|accepted|published|doi' <source>` for dates/venue clues; check self-citations for venue.
Anything you cannot confirm from the text → **Flags**, never the header as fact.

### Step 4 — Read the whole paper, build a map
Read end to end. Identify the central claim, where the real evidence is, which figures/tables are load-bearing, the limitations the authors concede, and **where the paper discusses the very problems our thesis is about** — these are highest value whether they agree with us or not.

### Step 5 — High-recall capture (the core step)
Run **each roadmap claim from the context file** as a coverage checklist. For each, ask: does the paper state anything bearing on it? Capture the **exact line** whether it **supports or contradicts** us. Then sweep these high-value categories:
- **Precise quantitative statements** (numbers are the most citable).
- **Author-conceded limitations / trade-offs / "we cannot…" admissions.**
- **The paper proposing the very approach we critique, or conceding the very fact we build on** — these counter/conceded lines are often the single most valuable quotes; a downstream agent can deploy them as support OR as a named opponent. **Do not sanitize the note into all-agreement** — that is the most common failure and it strips the writer's best material.

Copy everything **verbatim** — exact wording, section name, page. **Relevance to a roadmap claim is the gate: cut everything off-roadmap and out-of-scope (no filler), but capture every on-roadmap line even if that's 15 of them.** No arbitrary count cap; no filler padding.

### Step 6 — Resolve primary sources behind key quotes
For each load-bearing quote that cites a primary paper, look it up in the reference list and record the real citation (Author Year, Journal Vol:Pages, ref #) so the writer cites first-hand. Never list a source whose link to the quote you doubt — put doubts in Flags instead.

### Step 7 — Write the index file
Produce `<basename>_refined.md` with the template below via `Write`. Re-scan for stray Chinese before saving.

---

## Output Template

```markdown
# [Full Paper Title] — Source Index

**Authors:** [exactly as printed — if the source gives only initials, KEEP initials]
**Journal / Venue:** [Name, Year, Vol(Issue):Pages — or "unverified; see Flags"]
**DOI:** [doi:… — or "not found in text; see Flags"]
**Read on:** [today's date]
**Source file:** [absolute path to the source — raw is on disk; section names below are jump-back anchors]

---

## In One Sentence
[What the paper did + its main finding. Plain description; no positioning.]

## Orientation (non-binding)
[1–3 sentences: where this paper sits relative to our thesis, and which roadmap claims/axes it most
likely feeds. If it can serve as BOTH support and foil, say so. This is a ROUTING HINT, not a committed
role — the downstream agent decides how to deploy it.]

---

## Load-Bearing Excerpts
> "[exact quote — unaltered]"
> — [Section name / p.X] · bears on: [claim/axis IDs from the context file] · [one neutral clause: what the paper claims here]

> "[exact quote]"
> — [Section name / p.X] · bears on: [claim/axis IDs] · [one neutral clause]

[Capture EVERY excerpt that bears on a roadmap claim — including lines that cut against us. No filler.
The quotes ARE the product: do not paraphrase, do not append "how to use," do not write sample rewrites.]

---

## Claim Touchpoints (router — the downstream aggregation key)
| Roadmap Claim / Axis | Relevant Excerpt (lead words / section) | Direction |
|---|---|---|
| [claim ID + short label, from the context file] | "[lead words…]" / [§] | supports / challenges / nuances / — |

[Key this table to the context file's OWN claim/axis identifiers so the outline agent can collate the same
claim across many papers. One-word direction tag only — no deployment prose.]

---

## Figures / Tables / Numbers
| Item | What it contains (factual) |
|---|---|
| Table 1 | [...] |

*(Omit if nothing on-roadmap.)*

---

## Primary Sources Behind Key Quotes
- [quote topic] → [Author Year, Journal Vol:Pages, ref #N]

*(Omit if the paper is itself the primary source. Never list a source whose link to the quote is in doubt.)*

---

## Flags
- [ ] Metadata unverified: [what, and on what basis]
- [ ] Reconstructed (NOT in source text): [e.g. full author names guessed from initials]
- [ ] Read at source: [primary papers worth reading first-hand instead of via this one]
- [ ] Source inconsistency: [e.g. a reference number that mismatches its citation]
```

---

## Quality Rules

**Extraction (do more):**
- **Verbatim is verbatim.** Never paraphrase — one changed word misrepresents the source.
- **High recall on roadmap-relevant lines.** Run every context-file claim as a checklist; capture counter-evidence as eagerly as support. An all-"supports" note has missed the writer's best material.
- **Numbers first.** Never drop quantitative results.
- **Resolve primary sources** behind key quotes so the writer can cite first-hand.

**Interpretation (do less — this is the point):**
- **No pre-written argument.** No sample rewrites, no "how the writer should phrase it." Surface material; let the downstream agents write.
- **No locked roles.** Orientation is one non-binding hint; never pre-commit a paper to foil/ally as if settled.
- **Context clauses stay neutral and descriptive** — "what the paper claims here," not "deploy this to crush the opposition."
- **Route, don't editorialize.** The touchpoint table carries a one-word direction tag, nothing more.

**Honesty (never violate):**
- **No hallucinated metadata or citations.** Initials stay initials. Unconfirmed venue/DOI → Flags, never the header. Uncertain page → `(approx. p.X)`. Reconstructions labeled as such, in Flags only.
- **Scope discipline.** Out-of-scope topics (per the context file) are not captured unless they double as a counter line on a roadmap claim.
- **English-only file.** Re-scan for Chinese before saving.
- **Always Write the file** — don't just print to chat.
