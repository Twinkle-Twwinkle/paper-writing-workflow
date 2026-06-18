# Agent 写作工作流（Paper Writing Workflow）

一套用 **Claude Code 技能（skills）** 串起来的论文写作**标准化流程**。
从「给定研究 context」到「完成论文初稿」，共 6 步，**每一步都需要人工核验后再进入下一步**。

**核心约定:编号文件夹 = 时间顺序的步骤。** 每个项目里 `00-` → `06-` 的文件夹就是流程本身,照着编号往下做即可。

本仓库的作用：
1. **文档化流程** —— 写清每一步做什么、用哪个 skill、核验什么。
2. **可复用模板** —— 每写一篇新论文，复制 `projects/_example/` 为新项目，照着编号文件夹和 `CHECKLIST.md` 走。

---

## 项目文件夹结构（= 流程）

```
<论文名>/
├── CHECKLIST.md          # 从 00 勾到 06 的标准流程清单
├── 00-context/           # 步骤1输入:你给的 context(标题/结构/会议/讨论/种子文献)
├── 01-sources/           # 步骤1产出:Claude 找的 40 篇 source(含 DOI 列表)
├── 02-pdfs/              # 步骤2 · skill:论文下载    → 下载的 PDF
├── 03-markdown-raw/      # 步骤3 · skill:MinerU       → PDF 转的 raw md
├── 04-markdown-clean/    # 步骤4 · skill:论文清洗2.0  → 清洗后的 md
├── 05-distilled/         # 步骤5 · skill:精练         → 纯英文 distilled md
├── 06-outline-and-draft/ # 步骤6:outline.md → draft.md
├── 99-notes/             # 杂项:临时笔记 / 一次性脚本 / 会议记录
└── _archive/             # 归档:废弃版本、走偏的尝试(别删,留痕)
```

> ⚠️ **人在环中（human-in-the-loop）**:这不是全自动流水线。每个文件夹的产物出来后停下来核验、修正,确认无误再进下一个编号。

---

## 6 步详解

### 00 / 01 · 找 source（Claude 完成，无 skill）
- **输入**：`00-context/context.md` —— 论文的结构、标题、过去相关的会议、已有的讨论、相关论文等。
- **动作**：Claude 根据 context 找 **40 篇** 强相关、对写本文有用的论文，整理成 `01-sources/sources.md`（含 DOI）。
- **核验点**：相关性是否过硬？覆盖面够不够？有没有该引而漏掉的奠基性文献？

### 02 · 下载 PDF（skill：论文下载）
- **动作**：把 `01-sources/` 的 DOI 列表交给 **论文下载** skill，批量下载 PDF 到 `02-pdfs/`。
- **核验点**：成功 / 失败清单；失败的（`_需手动下载.md`）需手动补齐。

### 03 · PDF → Markdown（skill：MinerU）
- **动作**：用 **MinerU** skill 把 `02-pdfs/` 里的 PDF 转成 markdown 到 `03-markdown-raw/`。
- **核验点**：转换完整性；公式、表格、图注是否大体可读。

### 04 · 清洗 Markdown（skill：论文清洗 2.0）
- **动作**：用 **论文清洗 2.0** skill 对 raw md 拍版矫正(移除图片、图注归文末、标准化结构)，输出到 `04-markdown-clean/`。
- **核验点**：结构规范、正文连贯、原文件保留（03 不动）。

### 05 · 精练（skill：精练）
- **动作**：用 **精练** skill 精读每篇清洗后的论文，对照本文逐条提炼相关原文与意义，输出纯英文 md 到 `05-distilled/`。
- **核验点**：是否抓住与本文论点的关联；文献定性是否准确；未核实的元数据没被当事实。

### 06 · 写 outline → 填充成文（Claude 完成）
- **6a**：综合 context + 全部 `05-distilled/`，写 `06-outline-and-draft/outline.md`。核验论证主线、各节逻辑、论点是否有文献支撑。
- **6b**：依据核验过的 outline，逐节填充为 `06-outline-and-draft/draft.md`。核验事实准确、引用对得上、与 outline 一致。

---

## 怎么开一篇新论文

1. 复制模板项目并重命名（建议加日期前缀，如 `260618_virtual-cell-perspective`）：
   ```bash
   cp -r projects/_example projects/<日期>_<论文名>
   ```
2. 填好 `00-context/context.md`（见 `templates/00_context_template.md`）。
3. 打开该项目的 **`CHECKLIST.md`**，按编号从 00 勾到 06；每步产出后核验，再继续。
4. 阶段性提交存档：
   ```bash
   git add . && git commit -m "step N: <做了什么>"
   ```

---

## 用到的 Claude Code 技能

| 文件夹 | 技能 | 作用 |
|--------|------|------|
| 02-pdfs | 论文下载 | 按 DOI 批量下载 PDF（9 层策略 + Sci-Hub 兜底） |
| 03-markdown-raw | MinerU | PDF → markdown |
| 04-markdown-clean | 论文清洗 2.0 | 清洗 / 拍版 raw markdown |
| 05-distilled | 精练 | 对照本文论点提炼文献，输出英文 distilled md |

> 00/01 与 06 由 Claude 直接完成，不依赖专门 skill。
