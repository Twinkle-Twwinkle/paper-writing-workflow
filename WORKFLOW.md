# WORKFLOW — 稳定流程入口

> **这是进入任何一个 project 时第一份要读的文档。** 它只讲「稳定的流程」，不随某篇文章的进度变。
> 当前进度看该 project 的 `CHECKLIST.md`；方法学复盘 / 旧坑看 `99-notes/`（**遇到设计疑问才翻，不是每次跑流程的必读入口**）。
>
> 形态：一个**清爽的手动挡**半自动流程——人启动一步 → agent 按该步 `SKILL.md` 执行 → 人按该步核验清单检查 → 人决定进下一步。不做全自动 dispatcher / 一键全流程。

---

## 编号文件夹 = 时间顺序的步骤

| 步骤 | 人手动启动什么 | 产物写在哪 | 人核验什么 | 通过后进入 |
|---|---|---|---|---|
| **00 context** | 填 `00-context/context.md`（地基）；固化 `evidence-questions.md`（固定 ClaimID） | `00-context/` | 主线清楚？ClaimID 定齐？ | 01 |
| **01 sources** | 据 context 找强相关文献，整理 DOI | `01-sources/sources.md` | 相关性硬？覆盖够？有无漏掉的必读？ | 02 |
| **02 pdfs** | 跑 `论文下载` skill | `02-pdfs/` | 成功/失败清单；失败的手动补 | 03 |
| **03 markdown-raw** | 跑 `MinerU` skill | `03-markdown-raw/` | 转换完整？公式/表/图注可读？ | 04 |
| **04 markdown-clean** | 跑 `论文清洗` skill | `04-markdown-clean/` | 结构规范？正文连贯？原 raw 保留？ | 05 |
| **05 distilled** | 对每篇跑 `精练` skill（读 cleaned md + `evidence-questions.md`） | `05-distilled/cards.json`（主产物）；派生视图进 `_inspection/` | 支持/反方都抓到？引文逐字？claimId 用规范 key？`meta?=⚠` 进核验？ | 06 |
| **06 outline+draft** | 综合 context + `cards.json` 写 outline → 编译 draft | `06-outline-and-draft/vN/{outline,draft}.md` | 论证主线？引用对得上？字数/体裁？ | 07（如需迭代） |
| **07 iteration** | 跑 `论文迭代` skill | 新版回写 `06/vN/`；账记 `07-iteration/迭代日志.md` | 见 07 README | 回 06 / 定稿 |

> ⚠️ **人在环**：每个文件夹产物出来后停下核验，确认无误再进下一编号。上一步没核验通过，不进下一步。

---

## 迭代怎么理解（第 07 步）

**迭代不是另一套系统**，就是带着新输入重走同一条管线：

> 新 context → `00-context/` 加一个新文件 → 沿 `01→06` 再走一遍（**没变的步骤核验后跳过，顺序不乱**）→ `06` 出新版本目录 `vN/` → `07-iteration/迭代日志.md` 记一条 + 顶部 `CURRENT` 指过去。

- 文献主库（01–05）**只增不改**；已蒸馏论文默认不重做，只 targeted backfill。
- `06` 版本化为 `vN/`，旧版只读不覆盖；当前接受版本只认 `迭代日志.md` 顶部 `CURRENT`。
- 详见 `论文迭代` skill（每个 project 的 `07-iteration/SKILL.md`）。

---

## 目录责任边界（一句话各管各的）

```
00-context/   地基 context + 导师意见 + 新范围（旧地基不覆盖，新意见增量追加）；
              evidence-questions.md = 蒸馏时唯一读取的固定 ClaimID 取证清单。
01-sources/   source 清单 / DOI / 候选文献。
02-pdfs/      下载说明 / 脚本 / 失败清单（真实 PDF 体量大可不入库）。
03-markdown-raw/   MinerU raw md（只管 PDF→raw）。
04-markdown-clean/ 清洗后 md（保留原 raw，不在这改学术内容）。
05-distilled/ cards.json + 单篇卡（证据层核心）；evidence-matrix / citation-registry 进 _inspection/。
06-outline-and-draft/  vN/ 版本化的 outline + draft；CURRENT 由 07-iteration/迭代日志.md 指明。
07-iteration/ 迭代规则（SKILL.md）+ 总日志（迭代日志.md）；材料回写 00–06，不另建 runs/。
99-notes/     方法学 / 设计复盘 / 旧坑 / 一次性笔记。【参考资料，不是正常运行入口】
_archive/     废弃版本 / 走偏尝试，留痕但不参与正常运行。
```

> **正常跑流程只读：本文件 + 当前步骤的 `README.md` / `SKILL.md`。** 要复盘旧坑或改造 workflow 时，再去 `99-notes/`。

---

## 不采用的复杂设计（保持简单，导师定）

❌ 全自动 dispatcher / `STATE.json` / 一键全流程　❌ 每轮固定 `runs/<轮次>/`　❌ 另建 `06-iterations/` 替代 `06-outline-and-draft/`　❌ 每轮强制扇出重读全部文献　❌ 强制 CSV 台账 / 一致性脚本（除非确实需要）。

真正要维护的，是每一步的「输入 / 输出 / 核验合同」。
