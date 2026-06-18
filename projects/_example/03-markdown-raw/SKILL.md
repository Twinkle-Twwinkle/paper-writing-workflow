---
name: MinerU
description: 【文献】把 PDF 转成 Markdown。用 MinerU 命令行（venv 安装）批量把 02-pdfs/ 里的论文 PDF 解析成 raw markdown（含公式/表格/图注），落到 03-markdown-raw/。触发："PDF转markdown"/"MinerU"/"把这些PDF转成md"/给一批 PDF 说要转成 markdown。⚠️边界：只负责 PDF→raw md，不做清洗（清洗交给「论文清洗 2.0」）。
---

# MinerU · PDF → Markdown（步骤 03）

把 `02-pdfs/` 里的论文 PDF 批量解析成 raw markdown，输出到 `03-markdown-raw/`。
本步只做**解析转换**，不做清洗——图片、图注、零碎结构原样保留，清洗交给下一步「论文清洗 2.0」。

> ⚠️ **人在环中**：转换完成后停下来核验（转换完整性 / 公式、表格、图注是否大体可读），确认无误再进入 04。

---

## 前置条件

- **MinerU 已装在 Python venv 里**（本机：`~/mineru-env`，版本 3.3.1）。
- **首次运行会自动下载模型**（约几分钟，从 modelscope 拉到 `~/.cache`），之后离线可用。
- 配置文件 `~/mineru.json`（latex 定界符、可选 LLM 辅助等），一般用默认即可。

```bash
# 激活环境（每个新 shell 都要）
source ~/mineru-env/bin/activate
mineru --version   # 应输出 mineru, version 3.3.x
```

---

## 命令用法

### 单篇

```bash
mineru -p 02-pdfs/Spateo.pdf -o 03-markdown-raw/ -b hybrid-engine --effort high -l en
```

### 批量（整个 02-pdfs 目录）

```bash
mineru -p 02-pdfs/ -o 03-markdown-raw/ -b hybrid-engine --effort high -l en
```

`-p` 支持传**目录**，MinerU 会遍历目录内所有 PDF 逐个转换。

### 常用参数

| 参数 | 含义 | 建议 |
|------|------|------|
| `-p` | 输入 PDF 文件或目录（必填） | 指向 `02-pdfs/` |
| `-o` | 输出目录（必填） | 指向 `03-markdown-raw/` |
| `-b` | 后端：`pipeline`/`vlm-engine`/`hybrid-engine`… | 默认 `hybrid-engine`（高精度，本地算力） |
| `--effort` | `medium`（快、关图表分析）/ `high`（带图表分析、更准但慢） | 论文图多用 `high` |
| `-l` | OCR 语言（`en`/`ch`/…） | 英文论文用 `en` 提升准确率 |
| `-m` | 解析方法 `auto`/`txt`/`ocr` | 默认 `auto`；扫描件/图片型 PDF 用 `ocr` |
| `-f` / `-t` | 公式 / 表格解析开关 | 默认开，保持开 |
| `-s` / `-e` | 起止页（从 0 开始） | 只转某几页时用 |

---

## 输出结构

每个 PDF 会生成一个同名子文件夹，markdown 在其中的 `auto/` 下：

```
03-markdown-raw/
└── <pdf名>/
    └── auto/
        ├── <pdf名>.md          ← 这就是要的 raw markdown
        ├── images/             ← 抽出的图片
        ├── <pdf名>_content_list.json
        ├── <pdf名>_middle.json
        ├── <pdf名>_layout.pdf  ← 版面可视化，便于核验
        └── …（model/span/origin 等中间产物）
```

下一步「论文清洗 2.0」吃的就是 `auto/<pdf名>.md`。

---

## 核验点（转完必做）

1. **完整性**：每篇 PDF 都生成了对应的 `auto/<名>.md`，没有中途失败。
2. **公式**：行内/行间公式是否被识别成 `$...$` / `$$...$$`，而不是乱码或图片。
3. **表格**：表格是否转成可读的 markdown/HTML 表，而不是糊成一团。
4. **图注**：figure caption 文本是否保留（图片本身在 04 清洗时会移除，但图注要留到文末）。
5. 失败的单篇：换 `--effort high` 或 `-m ocr` 重试；仍不行的记到 `99-notes/` 待手动处理。

---

## 边界

- ✅ 只做 **PDF → raw markdown**。
- ❌ 不做清洗（移图片/图注归位/标准化结构）——那是步骤 04「论文清洗 2.0」。
- ❌ 不做下载（步骤 02「论文下载」）、不做精练（步骤 05「精练」）。
