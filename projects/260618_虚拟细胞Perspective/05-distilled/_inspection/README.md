# Inspection Views（人工检查视图）

本目录存放从主产物（`../cards.json`）派生出来的**人工检查视图**，用于核验、浏览和辅助写作，**不是 source of truth**。

| 文件 | 是什么 | 给谁看 |
|---|---|---|
| `evidence-matrix.md` | 把 `cards.json` 按 claim 转置成的证据矩阵 + scoreboard + 逐字引文 | 给人看哪条论点证据硬 / 有反方 / 偏薄 |
| `citation-registry.md` | `citationKey` → 作者/年份/期刊映射 + `meta?=⚠` 待核验书目 | 编译参考文献前的核验视图 |

## 规矩

- 这些文件**可删除、可重建**，不应手工维护为主管线状态。
- 若与 `../cards.json` 或 `../../04-markdown-clean/*` 原文冲突，**以 `cards.json` / 原文为准**。
- 主管线（下一步真正依赖的）只认 `../cards.json`；本目录纯属辅助。
