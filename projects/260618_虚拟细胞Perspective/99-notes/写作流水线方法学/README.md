# 写作流水线 · 方法学精华

> 本目录是 260618 跑这篇 Perspective 时所用「论文 + 地基 context → 可审计 Perspective」流水线的**方法学精华存档**（只留 .md 精华；cards.json / evidence-matrix 等重件在 [`../../05-distilled/`](../../05-distilled/)，outline/draft 在 [`../../06-outline-and-draft/`](../../06-outline-and-draft/)）。
> 完整原始素材包（含脚本、上游精练技能、两份存档全量）在桌面 `补充/` 下，未全部入库。

## 这套流水线 6 阶段（与本仓库 00→06 编号互补：它是 05→06 内部怎么跑的细化）

```
P1 抽取  每篇论文 → excerpt-centric JSON 证据卡（精练4.0，每条逐字原句自带 touchpoints）
P2 矩阵  N 张卡按 claim 转置 → 证据矩阵 + 引用注册表 + scoreboard（纯代码，零 agent）
P3 修正  读「矩阵 + context」用真实证据修正 thesis（confirm/sharpen/overclaim/insufficient）★人工拍板
P4 成骨  落成可审计骨架：每条论断绑 [引用号] + 逐字原句 + anchor
P5 审计  每条引文回 _cleaned.md 逐字核验（HTML/glyph 归一化）
编译     骨架扩写成 1500–2000 字英文 Perspective
```

## 文件导览

| 文件 | 内容 |
|---|---|
| `总体设计与思路.md` | 先读：6 阶段流水线、为什么这么设计、6 条核心原则、两层引用体系 |
| `决策与教训.md` | 关键决策日志 + **跑出来才暴露的 3 个坑**（claimId 碎裂 / 过度打标 / 逐字审计假警报）——最值钱 |
| `交接文档_原始思路与坑.md` | 上一会话最完整的思路与坑清单 |
| `prompts-与-schema总览.md` | 实际用过的 agent prompt 要点 + JSON schema + 规范 claim 词表 |
| `prompts/P3_thesis修正_agent-prompt.md` | P3 agent 完整 prompt 原文 |
| `prompts/P4_成骨_agent-prompt.md` | P4 agent 完整 prompt 原文 |
| `prompts/prompt设计要点.md` | 可迁移的 prompt 手法 |
| `thesis-revision_P3产物.md` | P3 产物：thesis 裁决/锐化 + 作者最终裁定（= outline 的结构蓝图） |
| `audit-report_P5产物.md` | P5 审计报告（逐字保真 PASS、零编造） |

## 3 个坑（一句话）

1. **claimId 碎成 60 种** → 下游要确定性聚合时，claim/类别字段必须用枚举/受控词表。
2. **过度打标** → 衡量 claim 多硬，数「几篇不同论文支持」，不数触点条数。
3. **逐字审计假警报** → 审计前先归一化源端格式垃圾（标点字形 + HTML 标签 + 引用标记）。
