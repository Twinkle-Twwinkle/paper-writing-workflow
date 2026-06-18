# 论文写作工作流（Paper Writing Workflow）

一套用 **Claude Code 技能（skills）** 串起来的论文写作流程模板。
从「给定研究 context」到「完成论文初稿」，共 **6 步**，**每一步都需要人工核验后再进入下一步**。

本仓库的作用：
1. **文档化流程** —— 写清每一步做什么、用哪个 skill、核验什么。
2. **可复用模板** —— 每写一篇新论文，复制 `projects/_example/` 为新项目文件夹，照着流程走。

---

## 流程总览

```
[第1步] 我给 context ──► Claude 找 40 篇强相关 source（DOI 列表）
   │  核验：论文是否真的相关、覆盖面是否够、是否有遗漏的必读文献
   ▼
[第2步] skill：论文下载 ──► 把 40 篇 PDF 全部下载到 pdfs/
   │  核验：哪些下载成功、哪些进了 _需手动下载.md，需手动补齐
   ▼
[第3步] skill：MinerU ──► 把 PDF 转成 raw markdown 到 markdown_raw/
   │  核验：转换是否完整、公式/表格/图注是否大体可读
   ▼
[第4步] skill：论文清洗 2.0 ──► 拍版矫正、移除图片等，输出到 markdown_clean/
   │  核验：结构是否规范、正文是否连贯、图注是否归到文末
   ▼
[第5步] skill：精练 ──► 对照本文论点提炼每篇文献，输出到 distilled/
   │  核验：提炼是否抓住与本文相关的点、定性是否准确
   ▼
[第6步] 写 outline ──► 再据 outline 填充成文（outline.md → draft.md）
      核验：outline 的论证逻辑；填充后的事实/引用准确性
```

> ⚠️ **人在环中（human-in-the-loop）**：这不是全自动流水线。每一步产出后停下来，由你核验、修正，确认无误再继续下一步。

---

## 6 步详解

### 第 1 步 · 找 source（Claude 完成，无 skill）
- **输入**：`00_context.md` —— 论文的结构、标题、过去相关的会议、已有的讨论、相关论文等。
- **动作**：Claude 根据 context 找 **40 篇** 强相关、对写本文有用的论文，整理成 `01_sources.md`（含 DOI）。
- **核验点**：相关性是否过硬？覆盖面够不够？有没有该引而漏掉的奠基性文献？
- **产出**：`01_sources.md`（DOI 列表）。

### 第 2 步 · 下载 PDF（skill：论文下载）
- **动作**：把 `01_sources.md` 里的 DOI 列表交给 **论文下载** skill，批量下载 PDF。
- **核验点**：成功 / 失败清单；失败的（`_需手动下载.md`）需手动补齐再放进 `pdfs/`。
- **产出**：`pdfs/*.pdf`。

### 第 3 步 · PDF → Markdown（skill：MinerU）
- **动作**：用 **MinerU** skill 把 `pdfs/` 里的 PDF 转成 markdown。
- **核验点**：转换完整性；公式、表格、图注是否大体可读。
- **产出**：`markdown_raw/*.md`。

### 第 4 步 · 清洗 Markdown（skill：论文清洗 2.0）
- **动作**：用 **论文清洗 2.0** skill 对 raw md 拍版矫正：移除图片链接及前置编码、图注汇总到文末、标准化结构（标题→Abstract→正文→Acknowledgements→References→作者→Figure 描述列表）。
- **核验点**：结构规范、正文连贯、原文件保留、输出为新文件。
- **产出**：`markdown_clean/*.md`。

### 第 5 步 · 精练（skill：精练）
- **动作**：用 **精练** skill 精读每篇清洗后的论文，对照本文（正在写的 Perspective）逐条提炼相关原文与意义，输出纯英文 Markdown。
- **核验点**：是否抓住与本文论点的关联；文献定性是否准确；未核实的元数据没被当事实。
- **产出**：`distilled/*.md`。

### 第 6 步 · 写 outline → 填充成文（Claude 完成）
- **6a 写 outline**：综合所有 context + 全部 `distilled/` 产出，写出论文 `outline.md`。
  - 核验点：论证主线、各节逻辑、每个论点是否有文献支撑。
- **6b 填充成文**：依据核验过的 outline，逐节填充为完整论文 `draft.md`。
  - 核验点：事实准确、引用对得上、与 outline 一致。
- **产出**：`outline.md`、`draft.md`。

---

## 怎么开一篇新论文

1. 复制模板项目文件夹并重命名（例如 `virtual-cell-perspective`）：
   ```bash
   cp -r projects/_example projects/<你的论文名>
   ```
2. 填好 `projects/<你的论文名>/00_context.md`（见 `templates/00_context_template.md`）。
3. 打开该项目里的 **`CHECKLIST.md`**，按时间顺序从第 1 步勾到第 6 步；每步产出后核验，再继续。
4. 阶段性提交存档：
   ```bash
   git add . && git commit -m "step N: <做了什么>"
   ```

---

## 用到的 Claude Code 技能

| 步骤 | 技能 | 作用 |
|------|------|------|
| 2 | 论文下载 | 按 DOI 批量下载 PDF（9 层策略 + Sci-Hub 兜底） |
| 3 | MinerU | PDF → markdown |
| 4 | 论文清洗 2.0 | 清洗 / 拍版 raw markdown |
| 5 | 精练 | 对照本文论点提炼文献，输出英文 distilled md |

> 第 1、6 步由 Claude 直接完成，不依赖专门 skill。
