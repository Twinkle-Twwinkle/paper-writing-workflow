# 05 · 精练

步骤5 · skill：**精练**。每篇 `04-markdown-clean/` 的清洗稿 + `00-context/context.md` 一起喂给 skill，高召回逐字打捞承重原文，连出处与所触论点索引；不预写论点、不示范改写、不锁定论文角色。每条原句带 `touchpoints`，键到 `00-context` 的 claim/axis 标识符，供下游 outline agent 跨论文按 claim 聚合。

> ⚠️ **本项目用的是精练 4.0（输出 JSON），不是模板默认的 3.0（输出 `<basename>_refined.md`）**。
> 4.0 把每篇的输出从 markdown 升级为**一份规范化 JSON 卡**（excerpt-centric，每条逐字原句自带 `touchpoints:[{claimId,direction}]`），下游聚合无需再逐篇解析回 JSON、且无损。本文件夹的 `SKILL.md` 即精练 4.0 源。

因此本目录的产物不是 `*_refined.md`，而是：

**主产物（下游唯一数据源，放显眼处）：**

| 文件 | 是什么 |
|---|---|
| `cards.json` | 41 篇的 JSON 证据卡合集（下游唯一数据源） |
| `V1论文/` `V2补充论文/` | 逐篇 JSON 证据卡（分片） |
| `样例卡-08a_refined.json` | 单篇卡样例（看结构用） |

**派生检查视图（给人核验，已移入 `_inspection/`，非 source of truth）：**

| 文件 | 是什么 |
|---|---|
| `_inspection/evidence-matrix.md` | 41 张卡按 claim 转置成的证据矩阵 + scoreboard + 逐字引文（P2 纯代码产出） |
| `_inspection/citation-registry.md` | 引用注册表 + 审计红线（`meta?=⚠` = 推断的 DOI/期刊，编译期须核验） |

> ClaimID 的规范集见 `../00-context/evidence-questions.md`（蒸馏时唯一读取的取证清单；agent 不许自造编号）。

> 跑这套（P1 精练 → P2 矩阵 → … → 编译）的方法学精华见 [`../99-notes/写作流水线方法学/`](../99-notes/写作流水线方法学/)。
