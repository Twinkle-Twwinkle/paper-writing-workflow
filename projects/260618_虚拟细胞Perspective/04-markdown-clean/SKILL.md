---
name: 论文清洗2.0
description: 清洗 MinerU 生成的论文 Markdown 文件：移除图片链接及前置编码数字、将 Figure 描述汇总到文末、确保正文连贯、标准化文档结构（标题→Abstract→正文→Acknowledgements→References→作者→Figure描述列表）。所有修改必须先 Read 原文再用 Edit 精确操作，禁止正则批量替换。输出为新文件（原文件保留）。触发：'论文清洗2.0'/'清洗论文2.0'/'帮我用2.0清洗这篇论文'/'用新版清洗MD'/给一个 MD 文件路径说要用2.0清洗。
---

# 论文清洗 2.0

用户会给你一个 MinerU 生成的论文 `.md` 文件路径。你要用 **Read + Bash(cp) + Edit** 工具完成清洗，**原文件不动**，所有修改在新建的 `_cleaned.md` 上进行。

---

## 核心约束（整个清洗过程全程遵守）

1. **原文件全程不触碰**，所有 Edit 操作均针对 `_cleaned.md`
2. **禁止正则批量替换**：不写 `sed`、`awk`、`perl -pe` 等脚本批量改文本。每一处改动都必须先用 Read 看到原文内容，再用 Edit 做精确替换
3. **禁止凭空生成任何标签**：`<sup>`、`<sub>`、`<b>`、`<i>` 等 HTML 标签，只能在 `old_string` 中读到了才能在 `new_string` 中保留，绝不新增
4. **不改写任何正文学术内容**：措辞、专业术语、数据、引用格式均原样保留
5. **不删除 Table 描述**（`Table 1:` 等），只处理 Figure
6. **保留所有 Markdown 结构**：标题层级、代码块、LaTeX 公式（`$...$`、`$$...$$`）、表格

---

## 目标文档结构

清洗后文档的最终顺序：

```
标题
Abstract / SUMMARY
Introduction
... 正文各 section ...
Acknowledgements / Declaration of Interests 等（若有）
References
## Authors（所有作者名 + 机构编号列表 + 通讯作者 + DOI）
## Figure Descriptions
```

**关键原则**：
- 作者名单和机构信息**不出现在文档开头**（标题下方），统一移至文末 References 之后
- Figure Descriptions 始终是文档**最后一个 section**

---

## 执行顺序

### 步骤 0：复制文件 + 通读全文

1. 确定输出路径：原文件名加 `_cleaned` 后缀：
   - 原文件：`/path/to/paper.md`
   - 新文件：`/path/to/paper_cleaned.md`

2. 用 Bash 复制：
   ```bash
   cp "/path/to/paper.md" "/path/to/paper_cleaned.md"
   ```

3. 用 `Read` 读取**新文件**全文，通读并记录：
   - 标题在第几行；作者/机构块的完整范围（第几行到第几行）
   - 图片链接的分布和数量
   - Figure 描述段落的位置
   - 文末结构（References、Acknowledgements、Declaration of Interests 等的顺序）
   - 结构错位情况：作者信息是否混入 Introduction / Abstract；正文是否被 Figure 描述截断

后续所有 Edit 操作均针对**新文件**，原文件全程不触碰。

---

### 步骤 1：移除图片链接及前置编码数字

**目标格式**（MinerU 常见）：
```
![](images/xxx.png)
![alt text](path/to/image.jpg)
```

**前置编码数字**：图片链接前紧邻的孤立行，常见形式：
- 纯数字：`42`
- 方括号数字：`[42]`
- 数字加点：`42.`
- HTML 注释：`<!-- 42 -->`

**操作要求**：
1. 逐一定位每个图片链接
2. 用 Read 确认其上方是否有孤立编码行
3. **逐个** 用 Edit 删除（图片链接 + 前置编码行一并删除）
4. 删除后若产生连续空行（≥2 行），用 Edit 合并为单个空行

**不删除**：LaTeX 公式、表格、代码块内的任何内容。

---

### 步骤 2：收集 Figure 描述，同时从正文中移除

**识别规则**（以下形式开头的段落即为 Figure 描述）：
- `Figure 1:` / `Figure 1.` / `Figure 1 `（后接描述文字）
- `Fig. 1:` / `Fig. 1.` / `Fig. 1 `
- `FIGURE 1`（全大写变体）
- 描述标题也可能以 `## Figure 1.` 形式出现（MinerU 有时将其识别为 section 标题）
- 描述可能跨多行，直到空行或新段落为止

**操作要求**：
1. 按文中出现顺序，用 Read 确认每条 Figure 描述的**完整原文**（含所有子段落），记录内容备用
2. **逐条** 用 Edit 从正文中删除该 Figure 描述
3. 删除后立即检查上下文：
   - 若 Figure 描述插在一个句子中间（上文以逗号/连词结尾，下文以小写字母开头），将上下两段合并为一个连续段落，**不改写文字**，只把两个独立段落拼成一段
   - 若正文中出现因 PDF 分页导致的断词（如上段末尾为 `indi-`，下段开头为 `vidual`），拼合时需将断词还原为完整单词（`individual`）
   - 若删除后只剩孤立空行，合并为单个空行

---

### 步骤 3：整理作者信息块

MinerU 转换时常把作者名单和机构信息拆成多段，散落在文档各处（标题下方、Introduction 中间、Abstract 内部）。目标是把所有作者相关内容**集中提取**，最终放到文末 References 之后。

**需要识别并提取的内容**：
- 作者姓名行（形如 `Charlotte Bunne,<sup>1,2</sup> ...`）
- 机构编号列表（形如 `<sup>1</sup>Department of ...`）
- 通讯作者行（形如 `*Correspondence: ...`）
- DOI 行（形如 `https://doi.org/...`）
- PDF 分页产物行（`(Author list continued on next page)`、`(Affiliations continued on next page)` 等）——**直接删除，不保留**

**常见错位场景及处理**：

**场景 A：作者/机构信息在标题下方（文档开头）**
- 直接用 Edit 从文档开头删除整个作者/机构块（标题保留，SUMMARY/Abstract 保留）

**场景 B：部分作者/机构信息混入 Introduction 中间**
- 症状：Introduction 首段被一段人名或机构列表截断，上下文句子语义不连贯
- 操作：用 Edit 删除这段错位内容，同时修复被截断的句子（合并上下两半）

**场景 C：PDF 分页产物混入 Abstract/SUMMARY 内**
- 直接用 Edit 删除该行

**处理后**，将所有收集到的作者/机构内容统一整理，在步骤 4 中作为 `## Authors` section 插入文末。

---

### 步骤 4：将 Authors 和 Figure Descriptions 追加到文末

文末最终顺序：
```
References（最后一条参考文献）
## Authors
## Figure Descriptions
```

**## Authors 格式**：
```markdown
## Authors

[所有作者姓名，连成一行或按原文分行] ... Jure Leskovec,<sup>1,3,</sup>* and Stephen R. Quake<sup>3,7,49,</sup>*

<sup>1</sup>Department of ...
<sup>2</sup>...
...
<sup>N</sup>...

*Correspondence: ...

https://doi.org/...
```

格式细则：
- 作者姓名保留原文中已有的 `<sup>` 编号标注
- 机构列表每条单独一行
- 通讯作者和 DOI 放在机构列表之后

**## Figure Descriptions 格式**：
```markdown
## Figure Descriptions

**Figure 1.** [标题若有，写在此处]

(A) ...

(B) ...

**Figure 2.** [标题若有，写在此处]

(A and B) ...
```

格式细则：
- 统一使用 `**Figure N.**` 加粗编号，后跟一个空格
- 描述内容**必须从步骤 2 记录的原文逐字复制**，包括原有的 `<sup>`、`<sub>` 等 HTML 标签——原文有才保留，原文没有绝不添加
- 若原描述跨多行被图片打断，将两段文字直接拼接（加一个空格），**不补充任何新文字**
- 各条之间空一行
- 若原文 Figure 编号不连续，按实际出现顺序排，不补充缺失编号

---

## 关于 HTML 标签的硬性规则

**绝对禁止**：
- 在 Edit 的 `new_string` 中凭空生成任何 `<sup>`、`<sub>` 标签
- 用脚本或正则批量替换文本中的字符为标签形式
- 对正文段落做任何「顺手」的 HTML 标签修改

**正确做法**：
- `old_string` 和 `new_string` 中，**原样保留**原文已有的标签
- Figure Descriptions 和 Authors 的文字必须从步骤 2/3 的原文记录中逐字复制，不得凭记忆重新输入
- 每次 Edit 之前，先 Read 当前段落确认实际内容

---

## 完成后的报告

```
清洗完成：
- 原文件：<原路径>（未修改）
- 清洗后文件：<_cleaned.md 路径>
- 删除图片链接：X 处（含前置编码数字 Y 处）
- Figure 描述：共 N 条，已按出现顺序移至文末 ## Figure Descriptions
- 结构调整：[列出每项移动操作，或"无需调整"]
- 不确定项：[若有，列出；否则"无"]
```
