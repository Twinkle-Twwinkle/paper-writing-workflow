# 02 · 实际用过的 Prompt 与 Schema

> 把本次真正发出去的 agent prompt、JSON schema、规范词表都抄在这里，方便提炼技能时直接复用/改写。
> 运行件本体在 `workflow-scripts/` 和 `skills/`；本文件给的是"串起来的胶水"。

---

## 0. 规范 claim/轴 词表（受控词表——务必枚举化）
来源 = 地基 context 第 4 节（三轴）+ 第 5 节（Claim 1–10）。**坑①教训：claimId 必须用这套精确键，别让 agent 自由发挥。**

```
Claim 1  — 数据(非模型)是瓶颈；纯 data-driven 基础模型泛化差
Claim 2  — 解离式 scRNA-seq 丢失空间信息
Claim 3  — 破坏性测序无法成对观测同一细胞的时间
Claim 4  — 各模态正交/彼此不可替代（RNA 代偿不了蛋白/代谢/PTM…）
Claim 5  — 蛋白/代谢等模态对功能与表型不可或缺
Claim 6  — 高通量(空间)蛋白质组学/高质量测量可行且在进步
Claim 7  — 空间组织/微环境改变细胞状态与扰动响应
Claim 8  — 多模态提供正交信息、需整合
Claim 9  — 数据孤岛/跨论文不可比/缺标准
Claim 10 — 分辨率 × 通量 × 破坏性 的"三难"权衡
Axis A   — 模态（measure WHAT）
Axis B   — 时间（time course / 轨迹）
Axis C   — 空间（亚细胞→细胞→组织微环境）
Standard — QC、跨实验室/平台可比、跨模态配对、统一参照系
Other    — roadmap 之外的新角度（须填 otherLabel；保守使用）
```

---

## 1. P1A —— refined.md → 证据卡 JSON（早期方案，已被 v4 取代）
脚本：`workflow-scripts/P1A-extract_refined到json_workflow.js`。**claim 为中心、每 claim 一句**（有损），但 **schema 里 `claimId` 用了 `enum`（这点是对的，v4 反而丢了，导致坑①）**。

CARD_SCHEMA（要点）：
```js
claims[]: { claimId: {enum: CLAIM_IDS}, otherLabel?, 
            direction: enum[supports,challenges,nuances],
            strength: enum[strong,moderate,weak],   // ← v4 已去掉
            keyExcerpt(verbatim), note }
+ citationKey, shortName, title, venue, year, doi, oneSentence, primarySources[], flags[]
```
prompt 核心：读 refined.md → 用 Claim Touchpoints 表作脊柱 → 每 (claim,方向) 给一条**逐字**最佳引文 → claimId 必须取自枚举、别造 "Claim 4 (foil)" → 一篇若同时支持又反对同一 claim 就拆两条。

---

## 2. P1B —— 精练 4.0 跑全文 → excerpt-centric JSON（现行）
脚本：`workflow-scripts/P1B-distill-v4_cleaned到json_workflow.js`；技能：`skills/精练4.0-index.md`（schema 在里面）。
**workflow 里每个 subagent 的 prompt（原文）**：

```
Execute the "精练 4.0" skill on ONE paper and WRITE its JSON Source Index to disk.
STEP 1 — Read and follow this skill spec EXACTLY: <精练4.0-index.md 路径>
STEP 2 — Read the project context file; its claim/axis identifiers are the ONLY
         allowed claimId values (plus "Other"): <context 路径>
STEP 3 — Distill this cleaned paper (read it fully): "<…_cleaned.md>"
STEP 4 — Write the normalized excerpt-centric JSON to EXACTLY this path: <…/<key>_refined.json>
This paper's citationKey is "<key>".
Critical reminders from the skill:
- excerpt-centric: each excerpt carries its own touchpoints[{claimId,direction}]; NO strength.
- HIGH RECALL verbatim (keep OCR quirks), but DO NOT restamp the same (claimId,direction)
  across many excerpts that make the same point — strongest few distinct statements only.
- Capture counter-evidence/foils as eagerly as support. Resolve primarySources.
  Unverified metadata → flags, never asserted. Validate well-formed JSON before finishing.
Return ONLY the structured counts for the file you wrote.
```

返回的 SUMMARY schema（让 workflow 收回结构化计数）：
```js
{ citationKey, excerpts:int, touchpoints:int, figuresNumbers:int,
  primarySources:int, flags:int, jsonValid:bool }
```

v4 卡 schema（详见 `skills/精练4.0-index.md` 的 Output Schema；形状）：
```jsonc
{ schemaVersion, citationKey, title, authors, venue, year, doi, readOn, sourceFile,
  oneSentence, orientation,
  excerpts:[ { id, text(verbatim), anchor,
               touchpoints:[ {claimId, direction, otherLabel?} ], note } ],
  figuresNumbers:[ {item, contains} ],
  primarySources:[ {topic, citation, refN} ],
  flags:[ ... ] }
```

---

## 3. P2 —— 无 prompt（纯代码）
脚本：`workflow-scripts/P2-build_matrix_v4.py`。读 `v4-cards/*.json` →
`canon()` 折回 14 规范键 → 转置 + scoreboard(按支持论文数) + 引用登记表 +
三道质量闸（缺卡/逐字溯源率(glyph+HTML 归一化)/过度打标浓度）。重跑命令：
```bash
cd /Users/augustsirius/Desktop/已清洗_260617 && python3 _build/build_matrix_v4.py
```

---

## 4. P3/P4/P5 —— prompt 模板（尚未固化，给后续）

**P3 修正 thesis**（1 个高推理 agent，输入 `evidence-matrix.md` + context，输出 `thesis-revision.md`）：
```
你拿到一份按 claim 转置的证据矩阵（含 scoreboard 的"支持论文数"、逐字引文、涌现主题）
和一份地基 context（thesis + 7 步逻辑链 + 三轴 + Claim 1–10）。
1) 逐条裁决 7 步逻辑链 + thesis：confirmed / 需锐化 / 过度宣称 / 证据不足
   —— 用"支持论文数"做依据，不要用触点数。
2) 点名必须正面处理的张力/反方（矩阵里 challenges 多的、以及 Other 里的对立论题）。
3) 给出精简后的主线骨架（~2000 字够装的几条）：哪条头条/哪些降为支撑句/哪些砍。
4) 产出修正后的 thesis 与逻辑链。
然后停下等人工审，再进 P4。
```

**P4 成骨**（每节一个 agent）：按修正后的逻辑链写 outline 骨架，**每条论断后挂 `[citationKey]` + 一句逐字原句**（从 cards.json 取，不许改写），产出 `outline.md`。

**P5 审计**（对抗式 agent）：逐条核 ① 引用号指向真论文 ② 原句去对应 `_cleaned.md` 搜得到（先 glyph+HTML 归一化）③ direction 没用反 ④ 哪条 claim 证据薄/书目存疑 → `audit-report.md`。
