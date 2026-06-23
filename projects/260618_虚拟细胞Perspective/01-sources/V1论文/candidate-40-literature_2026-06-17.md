# 候选文献 40 篇（联网检索 · 2026-06-17）

> **任务**：依据三份地基文件（reading-list / Foundational-Context / 会议信息提取），沿 perspective 三条主线（**时空丢失 × 模态不可替代 × 孤岛不可比 → 算据标准**）联网检索，筛出相关性最高、**高 IF 或权威期刊**的 40 篇。
> **排序原则**：按"对 thesis 的论证强度 × 期刊权威度"综合排序，分 8 个论证组（A–H），组内按相关性。
> **去重说明**：已剔除 reading-list 现有 13 篇 core/supplementary 与 references.bib 已有 6 篇补充核心引用中的**完全重复项**；少数奠基文献（如 Waddington-OT、Nicheformer、How to Build VC）因检索命中且是组内锚点而保留，并在备注标注「已在清单」。
> **核验提醒**：年份/卷期以检索返回为准，个别 2026 文献为预印本或在审，入库前请二次核验 DOI 与最终发表信息。
> **【2026-06-17 修订】editorial 剔除**：editorial / "Method of the Year" 等编辑部汇总短文不作正式学术引用，已替换为其所综述的**原始研究或同行评审综述**：
> - 原 #8《Method of the Year 2021: spatial transcriptomics》(Nat Methods, editorial) → 拆为 **#8a Ståhl et al. Science 2016**（测序型奠基）+ **#8b MERFISH/Chen et al. Science 2015**（成像型奠基）。
> - 原 #14《Method of the Year 2024: spatial proteomics》(Nat Methods, editorial) → **#14 CODEX / Goltsev, Nolan et al. Cell 2018**（空间蛋白原始研究）。
> - 原 #15《An update on spatial proteomics》(Nat Methods 2026, news/editorial 性质) → **#15 Cancer and Metastasis Reviews 2025**（同行评审综述）。
> - 保留判定为正式 **Perspective** 而非 editorial 的 #1 / #2 / #3，及 Annual Review、Genome Biology 等同行评审综述。
> **【2026-06-17 修订②】预印本剔除**：bioRxiv / arXiv 未正式发表者不作正式引用，已替换为**已正式发表**的权威版本：
> - 原 #5《Benchmarking and Evaluation of AI Models in Biology》(CZI, arXiv 预印本) → **#5 Nature Methods 2025**《Benchmarking algorithms for generalizable single-cell perturbation response prediction》。
> - 原 #28《LivecellX》(bioRxiv 2025) → **#28 Mesmer/DeepCell, Greenwald et al. Nat Biotechnol 2022**（全细胞分割+TissueNet，已发表）。
> - 原 #29《Caliban》(bioRxiv) → **#29 Cellpose, Stringer et al. Nature Methods 2021**（通用细胞分割奠基，已发表）。
> - ⚠️ 注：原 reading-list 清单中的 010-LivecellX 同为预印本、012-Caliban 亦未正式发表——若它们也要进正文引用，建议一并替换；本表组 E 已改用上述已发表版本。

---

## 组 A · 虚拟细胞愿景 / 评估 / 泛化批评（thesis 顶层背书 + 反方靶子）

| # | 论文 | 期刊 / 年份 | 角色（对本文） | 链接 |
|---|---|---|---|---|
| 1 | How to Build the Virtual Cell with AI: Priorities and Opportunities（Bunne, Roohani, Theis, Leskovec, Quake 等） | **Cell** 2024 | 领域"宪法"，数据列五大优先事项【已在清单 001】 | [Cell](https://www.cell.com/cell/fulltext/S0092-8674(24)01332-1) |
| 2 | Grow AI virtual cells: three data pillars and closed-loop learning | **Cell Research** 2025 | "数据三支柱"——直接对位本文"算据标准"切口 | [Nature](https://www.nature.com/articles/s41422-025-01101-y) |
| 3 | From modality-specific to compositional foundation models for cell biology | **Cell Systems** 2026 | 论证"单模态 → 组合式多模态"的转向，支撑模态不可替代 | [Cell Systems](https://www.cell.com/cell-systems/abstract/S2405-4712(26)00016-5) |
| 4 | Zero-shot evaluation reveals limitations of single-cell foundation models | **Genome Biology** 2025 | 主流 SC 基础模型 zero-shot 常输给简单基线——"瓶颈在数据非模型"硬证据 | [Genome Biol](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03574-x) |
| 5 | Benchmarking algorithms for generalizable single-cell perturbation response prediction | **Nature Methods** 2025 | benchmark 不可比 / 泛化评估标准缺位——呼应 8 月 AIVC Week 议程（已正式发表，替原 CZI arXiv 预印本） | [Nat Methods](https://www.nature.com/articles/s41592-025-02980-0) |
| 6 | Insights, opportunities, and challenges provided by large cell atlases | **Genome Biology** 2025 | 大图谱的标准化/整合挑战，承上启下到组 H | [Genome Biol](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-025-03771-8) |

## 组 B · 空间维度：丢失空间 + 空间组学里程碑（主线②）

| # | 论文 | 期刊 / 年份 | 角色 | 链接 |
|---|---|---|---|---|
| 7 | Nicheformer: a foundation model for single-cell and spatial omics | **Nature Methods** 2025 | "空间必须当 input"最强证据【已在清单 002】 | [Nat Methods](https://www.nature.com/articles/s41592-025-02814-z) |
| 8a | Visualization and analysis of gene expression in tissue sections by spatial transcriptomics（Ståhl et al.） | **Science** 2016 | 测序型空间转录组奠基（Visium 前身）——把"空间"确立为可测 input 的原始研究 | [Science](https://www.science.org/doi/10.1126/science.aaf2403) |
| 8b | Spatially resolved, highly multiplexed RNA profiling in single cells（MERFISH, Chen et al.） | **Science** 2015 | 成像型单细胞空间转录组奠基——空间 input 的另一技术源 | [Science](https://www.science.org/doi/10.1126/science.aaa6090) |
| 9 | A practical guide for choosing an optimal spatial transcriptomics technology（Lim et al.） | **BMC Genomics** 2025 | 三难困境弹药：单细胞尺度只能测几百-上千基因【已在清单 005】 | [BMC Genomics](https://link.springer.com/article/10.1186/s12864-025-11235-3) |
| 10 | Systematic benchmarking of high-throughput subcellular spatial transcriptomics platforms across human tumors | **Nat Commun** 2025 | 各平台到底能产出什么 input 的硬基准【已在清单 013】 | [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12534522/) |
| 11 | A technical comparison of spatial transcriptomics platforms across six cancer types | (2025/2026, 综合期刊) | 分辨率×基因数×通量 trade-off 实测，补强第 4 节 | [PubMed](https://pubmed.ncbi.nlm.nih.gov/41526977/) |
| 12 | A comprehensive review of spatial transcriptomics data alignment and integration | **Nucleic Acids Research** 2025 | 空间数据对齐/整合——统一参照系缺口 | [NAR](https://academic.oup.com/nar/article/53/12/gkaf536/8174767) |
| 13 | Challenges and Opportunities in Clinical Translation of High-Resolution Spatial Transcriptomics | **Annual Review of Pathology** 2024 | 权威综述，空间数据落地约束 | [Annual Reviews](https://www.annualreviews.org/content/journals/10.1146/annurev-pathmechdis-111523-023417) |

## 组 C · 空间蛋白 / 多组学空间（蛋白 + 空间双缺口，郭组优势区）

| # | 论文 | 期刊 / 年份 | 角色 | 链接 |
|---|---|---|---|---|
| 14 | Deep Profiling of Mouse Splenic Architecture with CODEX Multiplexed Imaging（Goltsev, Nolan et al.） | **Cell** 2018 | 高重数组织成像蛋白组学奠基（CODEX）——空间蛋白 input 的原始研究 | [Cell](https://www.cell.com/cell/fulltext/S0092-8674(18)30904-8) |
| 15 | Spatial omics: applications and utility in profiling the tumor microenvironment | **Cancer and Metastasis Reviews** 2025 | 同行评审综述（非 editorial），空间组学现状与微环境应用 | [Springer](https://link.springer.com/article/10.1007/s10555-025-10304-z) |
| 16 | DBiTplus: imaging-based and sequencing-based spatial omics on the same tissue section | **Nature Methods** 2025 | 同一切片联测转录组+多重蛋白——可整合可配对范例 | [Nat Methods](https://www.nature.com/articles/s41592-025-02948-0) |
| 17 | Deep Visual Proteomics defines single-cell identity and heterogeneity | **Nat Biotechnol** 2022 | AI 引导的空间单细胞蛋白组学范式（郭组方向相邻） | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9371970/) |
| 18 | In-depth and high-throughput spatial proteomics for whole-tissue slice profiling（deep-learning sparse sampling） | **Cell Discovery** 2024 | 高通量全切片空间蛋白组学——直接对位郭组产能叙事 | [Nature](https://www.nature.com/articles/s41421-024-00764-y) |
| 19 | Spatial single-cell mass spectrometry defines zonation of the hepatocyte proteome | **Nature Methods** 2023 | 空间分辨蛋白揭示 RNA 测不到的功能分区 | [Nat Methods](https://www.nature.com/articles/s41592-023-02007-6) |
| 20 | Spatial multi-omics: novel tools to study complexity of cardiovascular diseases | **Genome Medicine** 2024 | 空间多组学综述，多模态空间整合 | [Genome Med](https://link.springer.com/article/10.1186/s13073-024-01282-y) |

## 组 D · 时间维度：破坏性测量 + 轨迹/谱系（主线③）

| # | 论文 | 期刊 / 年份 | 角色 | 链接 |
|---|---|---|---|---|
| 21 | Optimal-Transport Analysis... Developmental Trajectories in Reprogramming（Waddington-OT, Schiebinger et al.） | **Cell** 2019 | 从破坏性快照反推时间动力学的范式起点【已在清单 003】 | [Cell](https://www.cell.com/cell/fulltext/S0092-8674(19)30039-X) |
| 22 | Evolving strategies for lineage tracing: genetic markers, synthetic barcodes, and natural variants | **Cell Stem Cell** 2026（已正式见刊, CC BY） | 谱系追踪综述——绕过破坏性、把时间记进基因组 | [Cell Stem Cell](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(26)00193-1) |
| 23 | Connecting past and present: single-cell lineage tracing | **Protein & Cell** 2022 | 谱系追踪原理综述，时间轴反推 vs 真实记录 | [Springer](https://link.springer.com/article/10.1007/s13238-022-00913-7) |
| 24 | RNA velocity of single cells（La Manno et al.） | **Nature** 2018 | 从剪接比例外推"未来状态"——快照外推非真实观测【已在 bib】 | [Nature](https://www.nature.com/articles/s41586-018-0414-6) |
| 25 | Generalizing RNA velocity to transient cell states through dynamical modeling（scVelo, Bergen et al.） | **Nat Biotechnol** 2020 | velocity 动态模型；同时暴露稳态假设的局限 | [bioRxiv](https://www.biorxiv.org/content/10.1101/820936.full.pdf) |
| 26 | A comparison of single-cell trajectory inference methods（Saelens et al.） | **Nat Biotechnol** 2019 | 系统比较 45 种轨迹推断方法、揭示其局限与不一致——"从快照推时间方法学受限/不可比"弹药（替原偏免疫应用的 velocity 综述） | [Nat Biotechnol](https://www.nature.com/articles/s41587-019-0071-9) |
| 27 | Reversed graph embedding... single-cell trajectories（Monocle, Trapnell/Qiu et al.） | **Nature Methods** 2017 / **Nat Biotechnol** 2014 | 伪时间排序源头：从静态快照"推"时间【已在 bib】 | [Nat Biotechnol](https://www.nature.com/articles/nbt.2859) |

## 组 E · 时间维度：非破坏性活成像（破坏性的对照解法）

| # | 论文 | 期刊 / 年份 | 角色 | 链接 |
|---|---|---|---|---|
| 28 | Whole-cell segmentation of tissue images with human-level performance using large-scale data annotation and deep learning（Mesmer / DeepCell, Greenwald, Van Valen et al.） | **Nat Biotechnol** 2022 | 全细胞分割+人机协同标注（TissueNet 百万级），非破坏性活成像/谱系的工程基底（已正式发表，替原 LivecellX 预印本） | [Nat Biotechnol](https://www.nature.com/articles/s41587-021-01094-0) |
| 29 | Cellpose: a generalist algorithm for cellular segmentation（Stringer et al.） | **Nature Methods** 2021 | 通用细胞分割奠基——活成像时序定量的上游使能（已正式发表，替原 Caliban 预印本） | [Nat Methods](https://www.nature.com/articles/s41592-020-01018-x) |
| 30 | DeepSea: deep-learning model for single-cell segmentation and tracking of time-lapse microscopy | **Cell Reports Methods** 2023 | 非破坏性时间序列定量——真·时间数据源 | [Cell Rep Methods](https://www.cell.com/cell-reports-methods/fulltext/S2667-2375(23)00129-7) |

## 组 F · 模态不可替代：蛋白/PTM/代谢 ⊥ RNA（核心弹药，主线④⑤）

| # | 论文 | 期刊 / 年份 | 角色 | 链接 |
|---|---|---|---|---|
| 31 | Mass-spectrometry-based proteomics: from single cells to clinical applications | **Nature** 2025 | 单细胞蛋白组学权威综述——蛋白模态可行且不可替代 | [Nature](https://www.nature.com/articles/s41586-025-08584-0) |
| 32 | Automated single-cell proteomics with sufficient proteome depth beyond cell-type classification | **Nat Commun** 2024 | 单细胞蛋白深度已达"超越分型"——产能背书（timsTOF Ultra） | [Nature](https://www.nature.com/articles/s41467-024-49651-w) |
| 33 | Simultaneous quantification of mRNA and protein in single cells reveals post-transcriptional effects | **eLife** 2020 | 36% 位点 mRNA-蛋白方向不一致——RNA 代偿不了蛋白的直接证据 | [eLife](https://elifesciences.org/articles/60645) |
| 34 | Experimental reproducibility limits the correlation between mRNA and protein abundances（tumor proteomics） | **Cell Reports Methods** 2022 | mRNA-蛋白相关性低——模态正交弹药（含方法学校正） | [Cell Rep Methods](https://www.cell.com/cell-reports-methods/fulltext/S2667-2375(22)00170-9) |
| 35 | Phospho-seq: integrated multi-modal profiling of intracellular protein dynamics in single cells（Satija 组） | **Nat Commun** 2025（已正式发表, s41467-025-56590-7） | PTM/信号活性单细胞测量——"活性开关"层 RNA 测不出 | [Nat Commun](https://www.nature.com/articles/s41467-025-56590-7) |
| 36 | Integrative single-cell metabolomics and phenotypic profiling reveals metabolic heterogeneity (oxidation/senescence) | **Nat Commun** 2025 | 代谢=最接近表型的功能读出——模态不可替代 | [Nature](https://www.nature.com/articles/s41467-025-57992-3) |

## 组 G · 整合 / 微环境 / 通讯（多模态正交 + 空间邻域效应，主线⑦⑧）

| # | 论文 | 期刊 / 年份 | 角色 | 链接 |
|---|---|---|---|---|
| 37 | Integrated analysis of multimodal single-cell data（WNN, Seurat v4, Hao et al.） | **Cell** 2021 | 多模态整合奠基（CITE-seq, 228 抗体）——各模态各有效用 | [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8238499/) |
| 38 | Modeling intercellular communication in tissues using spatial graphs of cells（NCEM, Fischer et al.） | **Nat Biotechnol** 2022 | 解离数据推通讯假阳性高、必须空间邻接——空间作 input | [Nature](https://www.nature.com/articles/s41587-022-01467-z) |
| 39 | LIANA+: an all-in-one framework for cell–cell communication inference | **Nature Cell Biology** 2024 | 通讯推断现状与局限（蛋白层≠基因层）——模态/空间双约束 | [Nat Cell Biol](https://www.nature.com/articles/s41556-024-01469-w) |

## 组 H · 数据标准 / 语料 / 孤岛不可比（主线⑨ + 8月议程对接）

| # | 论文 | 期刊 / 年份 | 角色 | 链接 |
|---|---|---|---|---|
| 40 | CZ CELLxGENE Discover: a single-cell data platform for scalable exploration, analysis and modeling | **Nucleic Acids Research** 2025（D 区） | 社区级语料几乎全解离数据——时空标准化缺口 + 标准化 schema 范例【bib 有早期 biorxiv 版，建议升级为 NAR 正式版】 | [NAR](https://academic.oup.com/nar/article/53/D1/D886/7912032) |

---

## 备注与下一步

- **篇数**：剔除 3 篇 editorial、新增 1 篇拆分项后，当前为 **40 个条目**（#8 拆成 8a/8b）。题目已不强求满 40，全部为可正式引用的研究/同行评审综述/Perspective。
- **editorial 复核结论**：经逐条核查，**已无 editorial / "Method of the Year" / news-feature 类**条目。保留的综述均为同行评审（Annual Review of Pathology、Genome Biology、NAR、Cancer and Metastasis Reviews、Protein & Cell 等）；#1/#2/#3 为正式 Perspective。
- **预印本复核结论（已全部解决）**：#5/#28/#29 三篇预印本已替换为已正式发表版本（详见顶部修订②）。追加核实的三篇结论——**#22** Cell Stem Cell 2026 已正式见刊（保留）；**#35** Phospho-seq 已正式发表于 **Nat Commun 2025**（链接已升级为正刊版，保留）；**#26**《RNA velocity and beyond》虽已发表但刊于 *Allergology International*、主题偏免疫病，相关性弱，已替换为 **Saelens et al., Nat Biotechnol 2019**（45 种轨迹推断方法系统比较，更对口）。
- **现状**：全表条目均为**已正式发表**的研究 / 同行评审综述 / Perspective，无 editorial、无预印本。仅 #11、#3 等少数 2026 条目年份卷期请入库前二次核验 DOI。
- **覆盖核对**：8 条论证组对应 Foundational-Context 第 5 节 claim 1–10 全部命中（瓶颈在数据→A；丢空间→B/C；丢时间→D/E；模态正交→F；微环境/整合→G；孤岛标准→H；三难困境→B#9/11 + 会议素材）。
- **与现有 13 篇的关系**：标注【已在清单/已在 bib】者为锚点，**净新增约 27 篇**；可全部并入 `references.bib`，按本表 A–H 分区。
- **可升级项**：#40 建议把 bib 里的 `czi2023cellxgene`（bioRxiv）升级为 NAR 2025 正式版。
- **待你确认**：是否要我（1）逐条补 DOI / 完整作者并生成 BibTeX 入 `references.bib`；（2）按 4+1 动笔顺序标"必读/选读"；（3）对其中高价值者（如 #2 Cell Research 三支柱、#3 Cell Systems 组合式模型、#33/#34 mRNA-蛋白不一致）做速读笔记。
