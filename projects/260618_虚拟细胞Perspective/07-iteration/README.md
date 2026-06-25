# 07 · 迭代（Iteration）

> **迭代不是单独的系统。** 每一轮 = 往 `00-context/` 丢一个新 context 文件 → 沿 `01→06` 同一条管线再走一遍（没变的步骤核验后跳过，顺序不乱）→ `06-outline-and-draft/` 出一个新版本目录 `vN/` → 在本目录 `迭代日志.md` 记一条，并把顶部 `CURRENT` 指过去。

## 本目录放什么

| 文件 | 作用 |
|---|---|
| `SKILL.md` | 迭代规则（怎么跑一轮）；同步自全局 `论文迭代` skill |
| `迭代日志.md` | 总日志：顶部 `CURRENT: vN` + 每轮一条 changelog。**只放日志，不放材料。** |

> 真正的材料（新 context、新文献、新 outline/draft）都回写到 `00–06` 对应目录，本目录不另建 `runs/`。

## 一轮怎么跑（速查，详见 SKILL.md）

1. **新 context 进 00**：逐字保真存档（不覆盖旧 context），需要时由人更新 `00-context/evidence-questions.md`。
2. **判断重跑范围**：只改写作口径 → 01–05 跳过，直奔 06；有新增文献 → 01 补到 05（已蒸馏的不重做，只 targeted backfill）。
3. **出 06/vN**：以 `CURRENT` 版为基底**最小改动**，写新版 `06-outline-and-draft/vN/{outline,draft}.md`，旧版只读不覆盖。
4. **登账**：`迭代日志.md` 加一条，`CURRENT → vN`。
