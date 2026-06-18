# 论文流程 Checklist · <论文名>

> 标准化流程:**编号文件夹 = 时间顺序的步骤**,从 `00-` 走到 `06-`。
> 每步分「执行」和「✅ 人工核验」两道勾;上一步没核验通过,不进入下一步。

---

## 步骤 1 · 找 40 篇 source　→　`00-context/` `01-sources/`
- [ ] 填好 `00-context/context.md`(标题/结构/会议/讨论/种子文献)
- [ ] Claude 据 context 找出 40 篇,写入 `01-sources/sources.md`
- [ ] ✅ 核验:相关性过硬?覆盖面够?有没有漏掉的必读文献?

## 步骤 2 · 下载 PDF（skill：论文下载）　→　`02-pdfs/`
- [ ] 把 `01-sources/` 的 DOI 列表交给「论文下载」skill 批量下载
- [ ] ✅ 核验:看成功/失败清单,失败的(`_需手动下载.md`)手动补齐

## 步骤 3 · PDF → Markdown（skill：MinerU）　→　`03-markdown-raw/`
- [ ] 用「MinerU」skill 转换 `02-pdfs/` 里所有 PDF
- [ ] ✅ 核验:转换完整?公式/表格/图注大体可读?

## 步骤 4 · 清洗（skill：论文清洗 2.0）　→　`04-markdown-clean/`
- [ ] 用「论文清洗 2.0」skill 拍版矫正、移除图片、图注归文末、标准化结构
- [ ] ✅ 核验:结构规范?正文连贯?原文件保留(03 不动)?

## 步骤 5 · 精练（skill：精练3.0）　→　`05-distilled/`
- [ ] 用「精练3.0」skill,输入「清洗稿 + `00-context/context.md`」逐篇高召回打捞,输出纯英文 Source Index
- [ ] ✅ 核验:支持/反方引文都抓到?引文逐字无改写?claim-touchpoint 表键对得上 context?未核实元数据没当事实(进 Flags)?

## 步骤 6 · Outline → 成文　→　`06-outline-and-draft/`
- [ ] 6a 综合 context + 全部 `05-distilled/`,写 `outline.md`
- [ ] ✅ 核验:论证主线?各节逻辑?论点都有文献支撑?
- [ ] 6b 依据核验过的 outline 逐节填充为 `draft.md`
- [ ] ✅ 核验:事实准确?引用对得上?与 outline 一致?

---

✅ 全部完成 → 论文初稿成形。　废弃产物丢 `_archive/`,杂项笔记/脚本丢 `99-notes/`。
