---
name: 论文下载
description: 【文献】批量下载学术论文 PDF。9 层下载策略 + Sci-Hub curl 兜底 + Cell.com Playwright，按 DOI 列表自动下载。强制 _build/ + pdfs/ 目录组织 + _需手动下载.md 失败清单。触发："下载这些论文"/"批量下载文献"/"论文下载"/给一个 DOI 列表。⚠️边界：只负责下载（DOI→PDF），不做检索/速读/引用管理。
---

# 论文/文献自动下载

批量下载学术论文 PDF。两种模式可选，根据数量自动推荐。

> **`SKILL_DIR`** = 本技能文件夹绝对路径：
> `<本技能文件夹路径>/论文下载`
> 下文所有 `${SKILL_DIR}/...` 均指技能内自带文件，**无外部依赖**。

## 选择哪个脚本？

| 场景 | 脚本 | 说明 |
|------|------|------|
| **少量 (<100篇)** | `scripts/batch_download_papers.py` | 9 层策略，同步多线程，生成详细报告 |
| **大批量 (>100篇)** | `scripts/fast_download_papers.py` | **PMC async 优先 + 多层兜底**，50 并发，速度快数倍 |

> `fast_download_papers.py` 会 `import` 同目录的 `batch_download_papers.py`（复用 9 层 Downloader）。两个脚本必须在同一 `scripts/` 目录下——本技能已收编好，开箱即用。

## ⚠️ 文件夹组织约定（强制）

**中间文件放 `_build/`，PDF 放 `pdfs/`，失败清单单独生成到根目录。**

保持 ref-master 根目录只有 4 类东西：
- 原始引用清单（如 `00-*引用清单*.txt` / `index.txt`）
- `pdfs/` — PDF 成品
- `_build/` — 所有中间文件（DOI 提取、下载脚本、日志、报告）
- `_需手动下载.md` — **失败清单单独文件**（供用户手动下载时查看）

**约定结构**：
```
{项目}/ref-master/
├── 00-XXX引用清单.txt           # 用户提供的原始清单
├── _需手动下载.md               # ★ 失败条目清单（用户操作入口）
├── pdfs/                        # PDF 成品（paper.pdf 分文件夹存放）
│   ├── 0001-10.xxx_yyy/paper.pdf
│   └── ...
└── _build/                      # 所有中间产物（脱手即弃）
    ├── _dois.txt                # 提取的全部 DOI
    ├── _dois_valid.txt          # 过滤后有效 DOI
    ├── _dois_invalid.txt        # 幻觉/无效 DOI
    ├── _download.log            # 主下载日志
    ├── _scihub_retry.py         # Sci-Hub 兜底脚本（若生成）
    ├── _scihub_retry.log        # Sci-Hub 兜底日志
    ├── _download_report.md      # 完整 Markdown 报告（含成功/失败/无DOI/幻觉）
    └── _download_report.json    # 结构化报告
```

**强制要求**：
1. 开始任务前必须 `mkdir -p <ref-master>/_build <ref-master>/pdfs`
2. 所有临时脚本、DOI 列表、日志、完整报告一律输出到 `_build/`
3. **下载全部完成后必须在根目录生成 `_需手动下载.md`**（见下一节格式）

## ★ `_需手动下载.md` 生成规范（强制）

下载全部完成后（包括 Sci-Hub 兜底），从 `_build/_download_report.json` 中提取 3 类失败：
- 付费墙失败（`failed`）
- 无 DOI 条目（`no_doi`）
- 幻觉 DOI（`invalid_doi`，如 `10.64898/` 前缀）

生成 `<ref-master>/_需手动下载.md`，每条是 checkbox list `- [ ] **[NNN]**`，含：
- DOI / 来源链接（可点击）
- 完整引用（前 250-300 字符）
- 目标存放路径（`pdfs/{四位序号}-{DOI下划线化}/paper.pdf`）
- 对幻觉 DOI：留一行 `真实 DOI: ______________________________` 供用户填写

用户下载 PDF 后只需放到指定路径、在 checkbox 前打 `[x]` 即可。

**生成模板脚本**（放在 `_build/_gen_manual_list.py`，或直接 inline python）：
```python
import json
with open("_build/_download_report.json") as f: r = json.load(f)
entries = r["entries"]
lines = ["# 待手动下载清单\n",
         f"**总计**: {len(r['failed'])+len(r['no_doi'])+len(r['invalid_doi'])} 条\n",
         f"- ❌ 付费墙失败: {len(r['failed'])}\n",
         f"- 📄 无 DOI: {len(r['no_doi'])}\n",
         f"- ⚠️ 幻觉 DOI: {len(r['invalid_doi'])}\n\n",
         "下载后把 PDF 放到 `pdfs/{序号}-{DOI-url-encoded}/paper.pdf`。\n",
         "序号 4 位 0-padding，DOI 中 `/` 换 `_`。完成后打 `[x]`。\n\n---\n\n"]
for title, key in [("❌ 付费墙失败","failed"),("📄 无 DOI","no_doi"),("⚠️ 幻觉 DOI","invalid_doi")]:
    lines.append(f"## {title}（{len(r[key])} 条）\n\n")
    for n in r[key]:
        e = entries[n]
        doi = e.get("doi") or "(无 DOI)"
        lines.append(f"- [ ] **[{n}]** `{doi}`\n")
        if e.get("doi"): lines.append(f"  - 链接: https://doi.org/{e['doi']}\n")
        lines.append(f"  - 引用: {e['summary'][:280]}\n")
        if e.get("doi") and not e['doi'].startswith('10.64898/'):
            lines.append(f"  - 存放: `pdfs/{int(n):04d}-{e['doi'].replace('/','_')}/paper.pdf`\n")
        lines.append("\n")
with open("_需手动下载.md","w") as f: f.writelines(lines)
```

## 快速使用

### 大批量模式（推荐）

```bash
BASE=<ref-master目录>
mkdir -p "$BASE/_build" "$BASE/pdfs"

PYTHONUNBUFFERED=1 python3 "${SKILL_DIR}/scripts/fast_download_papers.py" \
  --items-file "$BASE/_build/_dois_valid.txt" \
  --base-dir "$BASE/pdfs" \
  --workers 50 > "$BASE/_build/_download.log" 2>&1
```

两阶段策略：
1. **Phase 1**: 批量查 PMCID (Europe PMC API) → 有 PMCID 的走 PMC 直连 (aiohttp async, 50 并发，最快)
2. **Phase 2**: 没 PMCID 的走 9 层多策略下载 (ThreadPool, 50 线程)

### 标准模式

```bash
BASE=<ref-master目录>
mkdir -p "$BASE/_build" "$BASE/pdfs"

python3 "${SKILL_DIR}/scripts/batch_download_papers.py" \
  --items-file "$BASE/_build/_items.md" \
  --base-dir "$BASE/pdfs" \
  --workers 8 \
  --report-json "$BASE/_build/_download_report.json" \
  --report-md "$BASE/_build/_download_report.md"
```

可选参数：
- `--workers <N>`: 并行线程数（默认 8）
- `--overwrite`: 覆盖已存在的有效 `paper.pdf`
- `--timeout <sec>`: HTTP 超时（默认 45s）

## 触发方式

- "帮我下载这些论文" + DOI 列表
- "批量下载文献到 refs 目录"
- 给一个包含 DOI 的文件（支持纯文本/markdown/csv/json）

## 9 层下载策略（标准模式）

1. **DOI 直连**：带 `Accept: application/pdf` header 请求 DOI
2. **落地页解析**：`citation_pdf_url` meta、MDPI/OUP/Hindawi 特定模式
3. **出版商 URL 猜测**：Nature/Science/Cell/PNAS/ACS/MDPI/Wiley/Elsevier/OUP/Hindawi/Future Medicine
4. **OpenAlex API**：OA URL、PDF URL、落地页
5. **Crossref API**：链接和预印本关系（bioRxiv 自动尝试）
6. **PMC 查询**：NCBI idconv + Europe PMC 直搜双路径
7. **Unpaywall API**：所有 OA 位置的 PDF URL
8. **Semantic Scholar API**：openAccessPdf
9. **Cloudflare 兜底**：`cloudscraper` 绕过 Cloudflare 保护

每层同时尝试 `requests` 和 `cloudscraper`。

## 第 10 层：Sci-Hub curl 兜底（2026-03-19 新增）

**适用场景**：前 9 层全部失败的付费墙论文（Elsevier/Nature/ACS/Springer 等）。

**关键踩坑**：Python `requests` 连接 Sci-Hub CDN（`sci.bban.top`）会 TLS 握手失败，但 `curl` 完全正常。**必须用 `subprocess.run(['curl', ...])` 代替 `requests.get()`**。

**当前可用镜像**（2026-03 测试）：`sci-hub.ren`、`sci-hub.ee`、`sci-hub.wf`（`sci-hub.se` 已不可达）

**工作流程**：
1. curl 访问 `https://sci-hub.ren/<DOI>` 获取 HTML
2. 从 HTML 中提取 `src="...bban.top/pdf/<DOI>.pdf#..."` 格式的 CDN URL
3. curl 下载该 CDN URL（带 Referer header）
4. 验证 `%PDF-` 文件头 + 文件大小 > 10KB

**代码模板**：
```python
import subprocess, re, os

def scihub_curl(doi, dest_path):
    mirrors = ['https://sci-hub.ren', 'https://sci-hub.ee', 'https://sci-hub.wf']
    ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    for mirror in mirrors:
        r = subprocess.run(
            ['curl', '-sL', '--max-time', '20', '-H', f'User-Agent: {ua}', f'{mirror}/{doi}'],
            capture_output=True, text=True, timeout=25)
        if r.returncode != 0: continue
        for m in re.finditer(r'src="([^"]*\.pdf[^"]*)"', r.stdout):
            pdf_url = m.group(1)
            if pdf_url.startswith('//'): pdf_url = 'https:' + pdf_url
            pdf_url = pdf_url.split('#')[0]
            dl = subprocess.run(
                ['curl', '-sL', '-o', dest_path, '--max-time', '45',
                 '-H', f'User-Agent: {ua}', '-H', f'Referer: {mirror}/', pdf_url],
                capture_output=True, timeout=50)
            if dl.returncode == 0 and os.path.getsize(dest_path) > 10000:
                with open(dest_path, 'rb') as f:
                    if f.read(5) == b'%PDF-': return True
    return False
```

**仍然无法下载的情况**：JBC 机器人检测、OUP Cloudflare、部分最新论文未被 Sci-Hub 收录 → 需手动通过学校 VPN 下载。

## 2026-03 新增下载经验

### 各出版商自动化下载可行性

| 出版商 | curl/requests | Playwright headless | 备注 |
|--------|--------------|-------------------|------|
| Cell.com (Elsevier/Cell Press) | ❌ 403 | ✅ 可下载 | `showPdf?pii=` 链接配合 Playwright `expect_download` |
| OUP (NAR 等) | ❌ Cloudflare 403 | ❌ managed challenge 无法通过 | Cloudflare turnstile 检测自动化特征，headless/非headless 均被拦。需 `undetected-chromedriver` 或真人浏览器 |
| PMC (NCBI) | ❌ JS PoW 挑战 | ❌ 超时 | 同样有 proof-of-work JS 挑战，E-fetch 只返回 XML |
| Semantic Scholar | ✅ API 可查 OA PDF URL | - | 但 URL 通常指向被封的出版商 |

> **OUP/Cloudflare 深入测试结论 (2026-03-19)**：即使用 Playwright 非无头模式 + `--disable-blink-features=AutomationControlled` + 移除 `navigator.webdriver`，Cloudflare managed challenge 仍然不放行（标题从 "Just a moment..." 变为 "请稍候…" 但不会解锁到真实内容）。NAR 等 OUP 期刊的 OA 论文，用浏览器点链接就是直接下载 PDF，非常简单，但自动化工具做不到。**结论：OUP 论文直接让用户手动下载，不浪费时间尝试自动化。**

### Playwright 下载 Cell.com 论文的代码模板

> 此模板需要 `pip3 install playwright && playwright install chromium`（可选增强，非两脚本默认依赖）。

```python
import asyncio
from playwright.async_api import async_playwright
import os

async def download_cell_pdf(pii, output_path):
    """下载 Cell Press / Elsevier 的 OA 论文 PDF
    pii: 如 S0167779925000459
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            accept_downloads=True
        )
        page = await context.new_page()
        url = f"https://www.cell.com/action/showPdf?pii={pii}"

        async with page.expect_download(timeout=60000) as download_info:
            try:
                await page.goto(url, wait_until="commit", timeout=60000)
            except Exception as e:
                if "Download is starting" not in str(e):
                    raise

        download = await download_info.value
        await download.save_as(output_path)
        size = os.path.getsize(output_path)

        with open(output_path, 'rb') as f:
            header = f.read(4)
        if header != b'%PDF' or size < 10000:
            os.remove(output_path)
            raise ValueError(f"Downloaded file is not a valid PDF ({size} bytes)")

        await browser.close()
        return size
```

### 元数据 API 优先级（查 OA PDF URL）

1. **Crossref API** (`https://api.crossref.org/works/{DOI}`) — 最可靠，直接返回出版商 PDF URL
2. **OpenAlex API** (`https://api.openalex.org/works/doi:{DOI}`) — OA 状态最准，`best_oa_location.pdf_url`
3. **Semantic Scholar** (`https://api.semanticscholar.org/graph/v1/paper/DOI:{DOI}?fields=isOpenAccess,openAccessPdf`) — 补充查询
4. **Unpaywall** (`https://api.unpaywall.org/v2/{DOI}?email=xxx`) — 2026年数据覆盖差，新论文常返回 null。**注意**：脚本里 email 用的是占位符 `test@example.com`，正式大量调用建议换成你自己的邮箱（Unpaywall 要求）。
5. **PMC ID 转换** (`https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids={DOI}&format=json`) — 查是否有 PMC 版本

### 注意事项

- OUP/NAR 论文虽标记为 OA，但自动化工具全被 Cloudflare 挡，只能手动浏览器下载
- PMC 的 E-fetch (`efetch.fcgi?db=pmc&id=PMCxxx&rettype=pdf`) 返回 XML 不是 PDF
- 下载前一定要用 Crossref 验证 DOI 对应的标题是否正确，避免 DOI 错误导致下载错误论文

## 详细策略指南

旧版曾由 Codex GPT-5.4 生成过一份 18KB 的完整下载策略参考文档（各出版商 URL 模式、API 用法、成功率分析），但它是**项目内产物**（`<项目>/ref-master/_download_strategy_guide.md`），非本技能自带文件。如某项目里已有该文件，可作为通用参考；本技能不携带它。

## PDF 验证

严格校验 `%PDF-` 文件头 + 最小文件大小，不会把 HTML 页面误存为 PDF。

## 输入格式

### 纯文本 DOI 列表（.txt）—— 最简单

```txt
https://doi.org/10.1038/s44160-022-00231-0
10.1038/s41586-023-06792-0
```

### Markdown / CSV / JSON

同时支持带文件夹映射的格式（详见 `scripts/batch_download_papers.py --help`）。

## 输出（三件套）

1. `pdfs/{序号}-{DOI-url-encoded}/paper.pdf` — PDF 成品
2. `_build/_download_report.json` + `_build/_download_report.md` — 完整下载结果
3. **`_需手动下载.md`** — ★ 根目录单独文件，列出所有失败条目供用户手动处理

**禁止**：中间文件、临时脚本、日志直接写到 ref-master 根目录（除 `_需手动下载.md`）。全部进 `_build/`。

## 依赖

```bash
pip3 install requests aiohttp aiofiles
pip3 install cloudscraper        # 可选，增强反爬
pip3 install playwright && playwright install chromium  # 可选，仅 Cell.com 模板需要
```

## 文件位置（本技能自带）

- **快速脚本**: `${SKILL_DIR}/scripts/fast_download_papers.py`
- **标准脚本**: `${SKILL_DIR}/scripts/batch_download_papers.py`
- **本技能文档**: `${SKILL_DIR}/SKILL.md`

## 相关技能

- 拿到 DOI 之前的检索 → 旧库「学术文献检索」
- 下载完速读 PDF → 本地池「快速阅读论文」
- 引用清单核对 → 旧库「论文引用审计」/「参考文献管理」
