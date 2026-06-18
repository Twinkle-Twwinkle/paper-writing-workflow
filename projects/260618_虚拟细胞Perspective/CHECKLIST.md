# 论文流程 Checklist · 虚拟细胞·细胞级时空数据 input（Perspective）

> 标准化流程:**编号文件夹 = 时间顺序的步骤**,从 `00-` 走到 `06-`。
> 每步分「执行」和「✅ 人工核验」两道勾;上一步没核验通过,不进入下一步。
>
> **本项目状态（260618）**：00→06 已先用一套自建流水线跑通一轮（产物已落各阶段文件夹，流水线方法学见 `99-notes/写作流水线方法学/`）。下方勾选反映当前进度；**仍待办**：① 据郭天南 v2（VC≠DT）增补范围界定段并回炉 outline/draft；② 书目核验（registry 里 33 篇推断的 DOI/期刊）。

---

## 步骤 1 · 找 source　→　`00-context/` `01-sources/`
- [x] 填好 `00-context/context.md`（v1 地基；v2 新增 VC≠DT 见同目录两份补充）
- [~] source 清单：当前以 `05-distilled/citation-registry.md` 为引用注册表（41 篇），`01-sources/sources.md` 尚未单列
- [ ] ✅ 核验:相关性过硬?覆盖面够?有没有漏掉的必读文献?

## 步骤 2 · 下载 PDF（skill：论文下载）　→　`02-pdfs/`
- [x] 41 篇 PDF 已下载（原始 PDF 体量大，未入库；见原项目语料目录）
- [ ] ✅ 核验:成功/失败清单

## 步骤 3 · PDF → Markdown（skill：MinerU）　→　`03-markdown-raw/`
- [x] 已转 raw markdown（未入库）
- [ ] ✅ 核验:转换完整?

## 步骤 4 · 清洗（skill：论文清洗 2.0）　→　`04-markdown-clean/`
- [x] 已清洗为 `*_cleaned.md`（未入库；P5 审计的逐字回搜对象）
- [ ] ✅ 核验:结构规范?正文连贯?

## 步骤 5 · 精练（skill：精练3.0 → 本项目升级为 4.0/JSON）　→　`05-distilled/`
- [x] 41 篇高召回打捞为 `cards.json`（excerpt-centric），转置成 `evidence-matrix.md` + `citation-registry.md`（说明见 `05-distilled/README.md`）
- [ ] ✅ 核验:支持/反方引文都抓到?引文逐字无改写?claim-touchpoint 键对得上 context?未核实元数据进 Flags(`meta?=⚠`)?

## 步骤 6 · Outline → 成文　→　`06-outline-and-draft/`
- [x] 6a `outline.md` = 可审计骨架（45 论断，每条绑 [引用号] + 逐字原句）
- [x] 6b `draft.md` = 编译出的 1714 字英文成稿（P5 审计 PASS、零编造）
- [ ] ✅ 核验:论证主线?引用对得上?**并入 v2 的 VC≠DT 范围界定段**?书目核验?

---

✅ 一轮跑通 → 待按 v2 回炉 + 书目核验后定稿。　废弃产物丢 `_archive/`,杂项/方法学丢 `99-notes/`。
