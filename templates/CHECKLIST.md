# 论文流程 Checklist · <论文名>

> 标准化流程:从上往下,**一步一步**做。每步分「执行」和「✅ 人工核验」两道勾。
> 上一步没核验通过,不进入下一步。

---

## 第 1 步 · 找 40 篇 source
- [ ] 填好 `00_context.md`(标题/结构/会议/讨论/种子文献)
- [ ] Claude 据 context 找出 40 篇,写入 `01_sources.md`
- [ ] ✅ 核验:相关性过硬?覆盖面够?有没有漏掉的必读文献?
- 产出:`01_sources.md`(含纯 DOI 列表)

## 第 2 步 · 下载 PDF（skill：论文下载）
- [ ] 把 DOI 列表交给「论文下载」skill 批量下载
- [ ] ✅ 核验:看成功/失败清单,失败的(`_需手动下载.md`)手动补齐放进 `pdfs/`
- 产出:`pdfs/*.pdf`

## 第 3 步 · PDF → Markdown（skill：MinerU）
- [ ] 用「MinerU」skill 转换 `pdfs/` 里所有 PDF
- [ ] ✅ 核验:转换完整?公式/表格/图注大体可读?
- 产出:`markdown_raw/*.md`

## 第 4 步 · 清洗（skill：论文清洗 2.0）
- [ ] 用「论文清洗 2.0」skill 拍版矫正、移除图片、图注归文末、标准化结构
- [ ] ✅ 核验:结构规范?正文连贯?原文件保留、输出为新文件?
- 产出:`markdown_clean/*.md`

## 第 5 步 · 精练（skill：精练）
- [ ] 用「精练」skill 对照本文论点逐篇提炼,输出纯英文 md
- [ ] ✅ 核验:抓住与本文的关联?文献定性准确?未核实元数据没当事实?
- 产出:`distilled/*.md`

## 第 6 步 · Outline → 成文
- [ ] 6a 综合 context + 全部 distilled,写 `outline.md`
- [ ] ✅ 核验:论证主线?各节逻辑?论点都有文献支撑?
- [ ] 6b 依据核验过的 outline 逐节填充为 `draft.md`
- [ ] ✅ 核验:事实准确?引用对得上?与 outline 一致?
- 产出:`outline.md`、`draft.md`

---

✅ 全部完成 → 论文初稿成形。
