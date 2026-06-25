# Outline (P4 成骨) — Auditable Skeleton for the AIVC Data-Standard Perspective

> 形态 = 段落结构 + 每段一串 compile-ready 英文论断句（assertions），每条论断绑定其证据。
> 引文 `text` 一字不差复制自 `cards.json` 的 `text` 字段（下游审计逐字回搜 `*_cleaned.md`）。
> 结构蓝图 = `thesis-revision.md` 第 4/5 节 + 顶部「✅ 作者最终裁定」（决策 A/B/C 通过；★产能降格、不为郭组打广告）。
> 段序：开场对置 → 时间（先打最锋利，篇幅最长）→ 空间（快、密、零争议）→ 模态不可替（含 34 拆弹）→ 算据标准收口（产能并入为可行性佐证 + 社区议程）。

---

## ¶1 · 开场 · 对置（目标 ~250 词）

**主旨（中文一句）**：AIVC 在模型一侧狂奔，主流乐观叙事认为 AI+omics 或 compositional/prior 已能补足数据稀缺，但这绕过了一个更根本的问题——喂给模型的细胞，从测量源头就被剥掉了时间、空间与多数功能模态；瓶颈不是单靠更大模型或更多同质 RNA 数据能突破的。

**Assertions（英文，compile-ready，按行文顺序）：**

- **A1.1** The dominant narrative around AI virtual cells (AIVCs) is one of data abundance: two revolutions, in AI and in omics, are said to now enable cell models learned directly from data.
    - [01] (Main) "Two exciting revolutions in science and technology— in AI and in ’omics—now enable the construction of cell models learned directly from data." — {Claim 1, challenges}（注：方向=challenges，此处作"先把乐观反方A立到最强、随后反转"用）
    - [01] (Main) "Experimentally, the exponential increase in the throughput of measurement technologies has led to the collection of large and growing reference datasets within and across diferent cell and tissue systems <sup>27,28,29,30</sup>, with data doubling every six months for the past several years <sup>31</sup>, along with the ability to couple these measurements with systematic perturbations <sup>32,33,34,35</sup>." — {Claim 1, challenges}（注：方向=challenges，"数据每六个月翻倍=数据已够多"乐观论的最硬版本，先发制人）

- **A1.2** But quantity is not the same as usefulness, and the field's own benchmarks show that scaling more of the same data yields diminishing returns.
    - [01] (Data needs and requirements) "In addition to data size, data diversity is critical to ensure model quality<sup>144</sup>. Data from humans and model organisms like mice and E. coli are unequally represented in sequence and literature databases, which when used for training, encode strong species biases <sup>144</sup>. Other biases, for example towards specific diseases or human ancestral populations could also reduce the impact of AIVC models <sup>145</sup>." — {Claim 1, supports}（注：用反方A论文自身的自我软化反转之）
    - [04] (Conclusions) "Additionally, we demonstrate that larger pretraining datasets do not always increase the performance of scGPT, and that datasets seen in pretraining still have poor cell type clustering performance." — {Claim 1, supports}
    - [05] (Results — Limitations of current methods in the perturbation generalization scenario) "As shown in our results, increasing the number of cells or perturbations in the training data did not lead to performance gains across all evaluation metrics (Supplementary Note 11 and Supplementary Figs. 13 and 14)." — {Claim 1, supports}

- **A1.3** The competing optimism is methodological rather than empirical — that compositional architectures and biological priors can substitute for missing measurements — yet its own proponents concede the hard limit.
    - [03] (Integrating prior knowledge) "Incorporating biological prior knowledge into multimodal singlecell foundation models can improve learning efficiency, model robustness, and interpretability—particularly in settings where purely data-driven approaches fall short due to data sparsity, noise, or limited coverage across biological contexts." — {Claim 1, supports}（注：先 steelman 反方B（model/prior-first））
    - [03] (MULTI-MODALITY AND COMPOSITIONAL AI) "Without diverse observations, even the most effective models and largest datasets will fall short of capturing the true complexity of the underlying biology." — {Claim 1, supports}（注：用对手自己的红线反转——先验补不出从未被观测的维度）

- **A1.4** The bottleneck, then, is not whether we can model more cleverly but that the cells we feed our models are stripped at the source of time, space, and most functional modalities — three holes opened by a single destructive step, dissociated single-cell sequencing.
    - [01] (Data needs and requirements) "Data generation will require simultaneous exploration of temporal and physical scales, while allowing for system perturbations." — {Claim 3, supports}（注：连最乐观的反方A论文也承认数据须同时覆盖时间与空间尺度）

---

## ¶2 · 主轴③ · 时间（先打最锋利的）（目标 ~400 词）

**主旨（中文一句）**：最深的缺口是时间，因为测序是破坏性的——测完即死，同一细胞无法被前后成对观测；领域被迫发明伪时序、RNA velocity、最优传输、谱系条形码、活细胞成像五套互不相容、各自承认不可靠的替代品，这种 workaround 的繁荣本身就是真配对时间数据缺席的铁证。

**Assertions（英文，compile-ready，按行文顺序）：**

- **A2.1** The deepest gap is temporal, and its cause is physical, not procedural: sequencing destroys the cell it records, so the same cell can never be observed at two time points.
    - [21] (Introduction) "Because scRNA-seq destroys cells in the course of recording their profiles, one cannot follow expression of the same cell and its direct descendants across time. While various approaches can record information about cell lineage, they currently provide only very limited information about a cell’s state at earlier time points (Kester and van Oudenaarden, 2018)." — {Claim 3, supports}
    - [25] (Introduction) "A central challenge in trajectory inference is the destructive nature of single-cell RNA sequencing (scRNA-seq), which reveals only static snapshots of cellular states. To move from descriptive toward predictive trajectory models, additional information is required to constrain the space of possible dynamics that could give rise to the same trajectory." — {Claim 3, supports}
    - [24] (Abstract / Introduction) "However, this approach captures only a static snapshot at a point in time, posing a challenge for the analysis of time-resolved phenomena such as embryogenesis or tissue regeneration." — {Claim 3, supports}

- **A2.2** Because true paired-in-time observation is physically forbidden, the field has been forced to invent a profusion of mutually incompatible surrogates — and each, by its own admission, is unreliable; this proliferation of workarounds is itself the strongest evidence that the data are missing.
    - [27] (Online Methods - cell ordering problem (Definition 2)) "This ‘pseudotemporal’ scale of differentiation is numerically arbitrary and will of course vary from experiment to experiment, but nevertheless is useful for downstream analysis." — {Claim 3, nuances}（注：方向=nuances，此处作"伪时序自承 numerically arbitrary=替代品扎堆铁证"用）
    - [23] (Introduction) "However, the ability to infer cell fate transitions for RNA velocity relies on assumptions such as constant gene-specific splicing rates, which may be violated in some situations (La Manno et al., 2018; Svensson and Pachter, 2018; Tritschler et al., 2019; Bergen et al., 2020; Lederer and La Manno, 2020)." — {Claim 3, supports}（注：RNA velocity 建在可被违反的假设上）
    - [21] (Discussion: An Optimal Transport Framework to Model Cell Differentiation) "Optimal-transport analysis is only intended to capture the time-varying components of a distribution $\mathbb { P } _ { t } .$ For systems in dynamic equilibrium, $\mathbb { P } _ { t }$ does not change over time and optimal transport would infer that each cell is stationary. (An example would be cells that are asynchronously undergoing cell division. Although each cell is changing, the overall distribution $\mathbb { P } _ { t }$ is constant across time.)" — {Claim 3, nuances}（注：方向=nuances，最优传输只能"分布到分布"、对动态平衡失明=替代品的内在局限）

- **A2.3** Surveying the workaround landscape confirms that none of these tools recovers what destructive measurement removed: of 62 reviewed trajectory approaches, none jointly used time and modeled cell growth.
    - [21] (Discussion: An Optimal Transport Framework to Model Cell Differentiation) "To set Waddington-OT in context, we comprehensively reviewed 62 other approaches (Table S6), which fall into three classes: category 1 (33 tools) is not applicable to developmental time courses with scRNA-seq, category 2 (25 tools) is applicable but does not incorporate time information, and category 3 (4 tools) leverages time information, but does not model cell growth rates over time." — {Claim 1, supports}（注：方向=Claim1/supports，作"workaround 谱系全景"用）
    - [22] (Computational integration of lineage and state dynamics) "Although scRNA-seq data alone can be utilized to infer differentiation dynamics via pseudotime analysis or RNA velocity, these approaches are inherently limited by the absence of true temporal constraints and are shown to perform poorly in distinguishing early fate bias among progenitors. By explicitly integrating lineage history with transcriptomic state information, the underlying differentiation processes can be captured with significantly higher fidelity." — {Claim 3, supports}

- **A2.4** Even lineage barcoding, the most direct workaround, requires genetic engineering that confines it to model organisms — so in the very systems that matter most, human tissue, the surrogate is unavailable.
    - [22] (Practical design guidance) "Crucially, both approaches require transgenesis, restricting their use to model organisms. Finally, natural variants eliminate the need for genetic engineering entirely, making them uniquely applicable to human samples. Although they capture high lineage diversity, their lineage recovery varies depending on the natural variant used and sequencing depth; furthermore, they lack temporal control and pose significant computational challenges for data interpretation." — {3, nuances}（注：方向=nuances，作"连这条 workaround 在人体里都用不了/无时间控制"用）

- **A2.5** The one method that watches the same living cell over time reads only its shape, not its molecules — so even the live-imaging escape hatch cannot recover molecular state dynamics.
    - [30] (SUMMARY) "Time-lapse microscopy is the only method that can directly capture the dynamics and heterogeneity of fundamental cellular processes at the single-cell level with high temporal resolution." — {Claim 3, challenges}（注：方向=challenges，先承认它是唯一能直接看活细胞动态的方法，随即由下一条限定为"只读形态"）
    - [30] (INTRODUCTION) "Widely available microscopy techniques such as label-free phasecontrast live microscopy allow for monitoring the dynamics of morphological features such as the size and shape of the cells." — {Claim 3, challenges}（注：方向=challenges，作"成像只读 size/shape、读不出分子态"用）

---

## ¶3 · 主轴② · 空间（已确立、解法在路上）（目标 ~300 词）

**主旨（中文一句）**：第二个缺口是空间，已被广泛确立、零争议、解法在路上：解离这一步不可逆地摧毁组织的空间架构，而邻域微环境实质性地改变细胞状态。

**Assertions（英文，compile-ready，按行文顺序）：**

- **A3.1** The second hole is spatial, and unlike the temporal one it is universally acknowledged: the same dissociation that enables single-cell sequencing irreversibly destroys tissue architecture.
    - [13] (Background) "tissue dissociation inevitably leads to the loss of spatial information." — {Claim 2, supports}
    - [11] (Background) "Yet, these methods require dissociation of the tissue, thereby destroying the spatial relationships between cells and their microenvironment. Tis information is critical the context of most diseases, including solid tumors, where spatial organization infuences cell signaling, immune infltration, and therapeutic response." — {Claim 2, supports}

- **A3.2** Lost spatial context is not cosmetic: the cellular neighborhood materially rewrites cell state, changing which proteins a cell displays.
    - [14] (Summary) "We observed an unexpected, profound impact of the cellular neighborhood on the expression of protein receptors on immune cells." — {Claim 7, supports}
    - [01] (Unlocking the power of spatial biology to fight cancer) "Thus, immune resistance must be understood in the spatial context of the cellular neighborhood in order to identify the specific cell states and gene signatures involved." — {Claim 7, supports}

- **A3.3** And the gap cannot be papered over with more dissociated data — a foundation model trained on dissociated cells fails to recover spatial complexity even when given three times the data.
    - [07] (Results — Model design and training / p.2) "Specifically, training on dissociated data alone (even three times the amount of spatial data) resulted in lower performance across downstream tasks (Extended Data Fig. 2a,b), indicating that dissociated data alone cannot capture spatial variation." — {Claim 2, supports}
    - [07] (Abstract / p.1) "Critically, we show that models trained only on dissociated data fail to recover the complexity of spatial microenvironments, underscoring the need for multiscale integration." — {Claim 2, supports}

---

## ¶4 · 主轴① · 模态不可替（含论文 34 拆弹）（目标 ~400 词）

**主旨（中文一句）**：即便补上时空，只测 RNA 仍拼不出细胞——各模态承载彼此无从代偿的信息；先正面化解"脱钩=测量噪声"（论文 34），再用配对因果（33）、去噪后仍不升（31）、磷酸化态（35）、代谢组（36）反转之，证明扣除噪声后不可替代性依然成立，且噪声问题本身指向标准缺位。

**Assertions（英文，compile-ready，按行文顺序）：**

- **A4.1** Even with time and space restored, RNA alone cannot reconstruct a cell, because the modalities carry complementary, non-substitutable information — surface protein resolves cell identities that the transcriptome blurs.
    - [37] (Results: Quantifying the relative utility of each modality in each cell) "For example, CD8<sup>+</sup> and CD4<sup>+</sup> T cells were partially blended together when analyzing the transcriptome but separated clearly in the protein data. Contrastingly, conventional dendritic cells (cDCs), along with a rare population of erythroid progenitors and spiked-in murine 3T3 controls, formed distinct clusters when analyzing RNA but were intermixed with other cell types based on surface protein abundance." — {Claim 4, supports}
    - [35] (Results — Phospho-seq simultaneously quantifies phosphorylated, cytoplasmic, and nuclear proteins) "We also observed higher phosphorylation of the nuclear transcription factor STAT3 in iPSCs compared to K562 cells, and found that only pSTAT3 levels (as opposed to total protein levels) correlated with STAT3 transcription factor activities (Fig S1L). We conclude that we can therefore measure phosphorylation states for both cytoplasmic and nuclear activities, and that phosphorylated protein levels are more re<sup>fl</sup>ective of cellular state and transcription factor activities compared to total protein levels." — {Claim 4, supports}（注：磷酸化态——非 RNA、非总蛋白量——才追踪细胞态）

- **A4.2** One might object that the observed mRNA–protein discordance is largely measurement error, not orthogonal biology — and the steelman is real: noise depresses the correlation, on average several-fold more than any biological factor.
    - [34] (Introduction) "Our technical ability to accurately and reproducibly quantify both mRNAs and proteins is potentially a major factor that influences the mRNA-protein correlation. If the error in our measurements is large, we would expect this error to reduce the correlation between mRNA and protein even in the absence of the biological factors outlined above." — {Claim 4, nuances}（注：方向=nuances，此处先 steelman 反方"脱钩=噪声"）
    - [34] (Results: Proteins with higher reproducibility have higher mRNA-protein correlation) "This suggests that noise in the quantification of protein abundances explains much more (on average 3 times) of the variance in mRNA-protein correlation than the most predictive previously identified factor." — {Claim 4, nuances}（注：方向=nuances，反方34最硬的一击，先正面摆出）

- **A4.3** But the steelman fails where it matters: improving measurement accuracy did not raise the correlation, which is exactly the opposite of what the noise hypothesis predicts.
    - [31] (Expression proteomics, p.3) "Improved accuracy in both proteomics and transcriptomics measurements should have increased reported correlations by reducing independent experimental noise, but this does not seem to have happened<sup>52</sup>. Instead, it has become apparent that transcriptome and proteome regulation are distinct in many dynamic situations, such as during development or disease progression<sup>53</sup>." — {Claim 4, supports}

- **A4.4** Causal, noise-controlled genetics settles it: when confounders and most technical bias are equalized, fewer than 20% of genetic loci act concordantly on mRNA and protein — the discordance is regulation, not artifact.
    - [33] (Abstract) "Less than 20% of these loci had concordant effects on mRNA and protein of the same gene. Most loci influenced protein but not mRNA of a given gene." — {Claim 4, supports}
    - [33] (Introduction) "We reasoned that such an approach would equalize all environmental confounders and most of the technical biases that could obscure the relationship between eQTLs and pQTLs." — {Claim 9, supports}（注：方向=Claim9/supports，此处用其"配对设计扣除噪声"的方法学语句支撑"控噪后脱钩仍在"）

- **A4.5** And the orthogonality extends beyond protein: the single-cell metabolome alone predicts cellular phenotype with near-perfect accuracy, information no transcriptome encodes.
    - [36] (Results — The SCLIMS reveals capability of the single-cell metabolome in predicting cellular OS status) "Machine learning is utilized to ascertain whether the metabolic pro<sup>fi</sup>le of individual cells can accurately predict heterogeneous subtypes with distinct OS levels. ... In multiclassi<sup>fi</sup>cation, the ROC curve had an average area under curve (AUC) of 0.98 (Fig. 4b). In cluster prediction, the model achieved an accuracy ranging from 77.8% to 100% (Fig. 4c). These results demonstrate that the single-cell metabolic pro<sup>fi</sup>les can directly predict metabolic subtypes." — {Claim 5, supports}

- **A4.6** Crucially, the noise objection does not vanish — it relocates: the very reason correlations are "not comparable" is that there is no shared standard, which converts the foil into an argument for the standard we are about to call for.
    - [34] (Results: A standardized pipeline reveals differences in the mRNA-protein correlation across studies) "The average mRNA-protein correlation reported for different tumor proteomic profiling efforts varies substantially across studies—ranging from 0.23 in an early proteomic study of colorectal cancer (Zhang et al., 2014) to 0.53 in a recent study of lung adenocarcinoma (Gillette et al., 2020) (Table 1). However, it is not meaningful to directly compare the reported correlations because the methods used to quantify the mRNA-protein correlation have varied across studies—different studies have used different summary statistics (mean versus median), different correlation metrics (Pearson versus Spearman), and different criteria for protein inclusion (e.g., no missing values, at least 30% measured values, only the 10% most variable proteins) (Table 1)." — {Claim 9, supports}（注：方向=Claim9/supports，把反方34收编为算据标准段的弹药）

---

## ¶5 · 收口 · 算据标准 + 可行性佐证 + 社区议程（目标 ~450 词，吸收原 ¶6 降格后的产能内容）

**主旨（中文一句）**：三个缺口加上一个共同后果——数据各自为政、跨实验室不可比——指向同一个出口：虚拟细胞需要一套显式编码时空、覆盖不可互替模态、可整合可比的"算据标准"；这些缺口并非不可补（高通量时空蛋白质组学已跨过可行性门槛，证明标准要求的数据是可生产的），但时间维仍是诚实的待补格；本文呼吁社区共同定义这套标准（可对接八月 AIVC Week 议程）。

**Assertions（英文，compile-ready，按行文顺序）：**

- **A5.1** These three gaps share a fourth consequence: the data we do have are siloed and not comparable across labs — only about a quarter of public datasets even carry the metadata needed for reuse.
    - [40] (Introduction) "Built-for-purpose portals enable rapid publication of studies and dissemination of unique biological features in specific datasets but lack the scalability and standardization needed for efficient meta-analysis. Even in the presence of such portals, efforts to explore or (re)analyze many datasets face a requirement to first standardize across individual data portals and resources, with only an estimated 25% of publicly available datasets providing the cell-level metadata needed for reuse (9)." — {9, supports}

- **A5.2** Incomparability is not a peripheral nuisance — a single analysis choice can flip a reported conclusion, so without shared standards the same data yield different science.
    - [34] (Results: A standardized pipeline reveals differences in the mRNA-protein correlation across studies) "For example, the correlation recalculated for endometrial cancer (0.48) was the same as originally reported (Dou et al., 2020), while the recalculated correlation for colon cancer was much lower than that reported by the authors (0.27 versus 0.48) (Vasaikar et al., 2019). This is because the colon cancer study reported the mean mRNA-protein correlation for only the 10% most variable proteins rather than the full set of proteins. These highly variable proteins have higher than average mRNA-protein correlations." — {Claim 9, supports}
    - [31] (Bringing proteomics to the clinic, p.6) "Given that the intensity values of different MS workflows are not directly comparable, such models are likely to be constrained to specific instruments unless spike-in standards are used." — {Claim 9, supports}

- **A5.3** The exit is therefore not more models or more homogeneous data but a data standard that explicitly encodes space and time, spans the non-substitutable modalities, and is integrable and comparable — a requirement even the most model-first voices endorse.
    - [01] (Box 1: Grand challenges (Establishing self-consistency)) "The same entity, profiled with diferent technologies, should have the same internal representation in an AIVC." — {standard, supports}
    - [40] (Results — A minimal cell-level schema) "To avoid deterring or inhibiting data submission and adoption, we limit the schema to 11 required fields considered most valuable for data integration and reuse." — {standard, supports}（注：以 CZ CELLxGENE 的最小 schema 作"标准可落地"的范例）

- **A5.4** Such a standard is buildable, not aspirational: high-throughput spatial proteomics has already crossed the feasibility threshold, recovering deep proteomes while preserving spatial context — evidence that the data the standard asks for can in fact be produced.
    - [17] (Abstract) "DVP links protein abundance to complex cellular or subcellular phenotypes while preserving spatial context." — {Claim 2, supports}
    - [19] (Abstract) "scDVP resolves the context-dependent, spatial proteome of murine hepatocytes at a current depth of 1,700 proteins from a cell slice. Half of the proteome was diferentially regulated in a spatial manner, with protein levels changing dramatically in proximity to the central vein." — {Claim 6, supports}
    - [18] (Abstract) "In this way, we generated the largest spatial proteome to date, mapping more than 9000 proteins in the mouse brain, and discovered potential new regional or cell type markers." — {Claim 6, supports}
    - [32] (Abstract) "the newest generation timsTOF Ultra identi<sup>fi</sup>es up to 4000 with an average of 3500 protein groups per single HEK-293T without a carrier or match-between runs." — {Claim 6, supports}

- **A5.5** Feasibility, though, must be claimed honestly — the temporal axis remains open even for the most advanced spatial proteomics, so time stays a square the standard must still fill, not one already solved.
    - [19] (Discussion) "A rhythmic expression pattern has been previously shown for a large number of liver transcripts and proteins<sup>16,19</sup>. While we have not covered the temporal aspect here, the scDVP approach could contribute to such studies by adding a spatial dimension." — {Claim 3, challenges}（注：方向=challenges，作者自承"未覆盖时间维"——诚实标注产能的开放项，呼应 ¶2）
    - [20] (Non-NGS-based spatial multi-omics) "Compared to the transcripts, resolving the proteome at single-cell resolution or in tissues is much more challenging. Cells typically contain 30,000× more protein molecules than mRNA molecules [67], and proteins are very heterogeneous in size and structure and, unlike nucleic acids, cannot be amplifed. Tis has limited the multiplexing and throughput of spatial proteome measurements." — {6, challenges}（注：方向=challenges，诚实标注 trade-off 仍在）

- **A5.6** Defining what this standard must contain — which modalities, which spatial and temporal coordinates, integrable and comparable by construction — is a community task, and the field should take it up now rather than discover its absence one incompatible dataset at a time.
    - [26] (Discussion) "In addition, further discussion within the field is required to arrive at a consensus concerning a common interface for trajectory models, which can include additional features such as uncertainty and gene importance." — {Claim 9, supports}（注：以一篇基准论文的"需社区达成共识"语句对接"呼吁社区共同定义算据标准"的落点；郭组至多一句轻提，不单独成段）
    - [01] (An open collaborative approach) "These eforts would greatly benefit from open data resources and data standards, a collaborative platform for cell modeling, and especially open benchmark datasets and common validation strategies to ensure their biological fidelity and real-world utility." — {Claim 9, supports}

---

## 附录 A · 引用清单（本 outline 实际用到的 citationKey + registry meta? 标记）

| citationKey | 用在哪段 | registry meta? |
|---|---|---|
| 01 | ¶1, ¶3, ¶5 | ⚠（书目推断，编译期核验） |
| 03 | ¶1 | ⚠ |
| 04 | ¶1 | ⚠ |
| 05 | ¶1 | ⚠ |
| 07 | ¶3 | ⚠ |
| 11 | ¶3 | ⚠ |
| 13 | ¶3 | ok |
| 14 | ¶3 | ⚠ |
| 17 | ¶5 | ⚠ |
| 18 | ¶5 | ⚠ |
| 19 | ¶5 | ⚠ |
| 20 | ¶5 | ⚠ |
| 21 | ¶2 | ⚠ |
| 22 | ¶2 | ⚠ |
| 23 | ¶2 | ⚠ |
| 24 | ¶2 | ⚠ |
| 25 | ¶2 | ⚠ |
| 26 | ¶5 | ⚠ |
| 27 | ¶2 | ⚠ |
| 30 | ¶2 | ok |
| 31 | ¶4, ¶5 | ⚠ |
| 32 | ¶5 | ⚠ |
| 33 | ¶4 | ⚠ |
| 34 | ¶4, ¶5 | ⚠ |
| 35 | ¶4 | ok |
| 36 | ¶4 | ⚠ |
| 37 | ¶4 | ⚠ |
| 40 | ¶5 | （列内未标 ⚠，registry 显示 venue 为 "unverified; see flags"——编译期一并核验） |

> 共 29 个 citationKey（含同一论文在多段复用）。除 13/30/35 在 registry 标 `ok` 外，其余均带 `meta?=⚠`，提示编译期须核验期刊/DOI 书目（不影响逐字引文审计）。

---

## 附录 B · 审计交接说明（给下游 P5 审计员）

逐条把每条 assertion 下绑定的引文 `text`（双引号内整段）放到对应论文的 `*_cleaned.md` 里逐字搜索，应命中；命中即判该引文逐字保真通过。注意：(1) OCR 小错（如 `infltration` `amplifed` `re<sup>fl</sup>ects` `<sup>fi</sup>` 等）是 cards.json 原样照搬，搜索时须容忍/按原文匹配，不要"修正"。(2) 标 `（注：方向=challenges/nuances …）` 的引文，其 touchpoint 原方向并非 supports，但在本文语境作"workaround 扎堆=缺口铁证"或"先 steelman 再反转"用，已逐条中文括注理由，审计只验逐字命中与方向标注是否诚实，不必推翻其修辞用法。(3) 本 outline **未出现 `⚠ UNBACKED` 标记**——所有 assertion 的引文均来自 cards.json 真实 `text`（详见下方"对 P3 的反审备注"，其中记录了 thesis-revision 引用与 cards.json 真实原句的若干偏差，均已改用真实原句，故无编造）。

### 对 P3（thesis-revision）的反审备注（重要，非 UNBACKED 但需知会）

P4 成骨时发现 thesis-revision.md 若干引文是**释义/拼接**，并非 cards.json 逐字原句。P4 已一律改绑 cards.json 真实 `text`，故 outline 无 UNBACKED；但下列偏差应回流给 P3/编译期知悉：

- **论文 27 "distinct individual cells are treated as surrogate time points"**：cards.json 中**无此原句**；真实最近似原句为 27-e2 "In essence, one RNA-Seq experiment would constitute a time series, with each cell representing a distinct time point along a continuum."（本 outline 改用更硬的 27-e5 "numerically arbitrary"，未使用 surrogate 释义）。P3 此处为释义，非逐字。
- **论文 26 "Real per-cell sampling times are often unavailable and are substituted [by inference]"**：cards.json 中**无此原句**；真实相关原句为 26-e23（time course "directly extracted from the reference trajectory; otherwise the geodesic distance from the root milestone was used"）。本 outline 未采用该 P3 释义句，改用 26-e20 的"需社区共识统一接口"原句作收口。P3 此处为释义，非逐字。
- **论文 22 "transcriptome-only trajectory inference lacks true temporal [context]"**：cards.json 真实原句为 22-e3 "...inherently limited by the absence of true temporal constraints..."（本 outline 已用真实原句 A2.3，P3 的 "lacks true temporal" 为压缩转写）。
- **论文 34 "reported mRNA-protein correlations are not directly comparable across studies"**：cards.json 真实原句为 34-e6 "it is not meaningful to directly compare the reported correlations because the methods ... have varied across studies"（本 outline A4.6/A5.2 已用真实原句，P3 的引号串为释义）。
- **论文 18 "S4P >9000 proteins...largest spatial proteome to date"**：cards.json 真实原句为 18-e4 "...the largest spatial proteome to date, mapping more than 9000 proteins in the mouse brain..."（本 outline A5.4 已用真实原句；"S4P" 命名 P3 自加，非原文）。
- **论文 33 "equalize all environmental confounders and most of the technical biases"**：逐字命中 cards.json 33-e12，P3 此处准确。
- **论文 03 "without diverse observations ... fall short"**：逐字命中 cards.json 03-e31，P3 此处准确。

> 结论：以上均系 P3 在 thesis-revision 中为行文流畅做的**释义压缩**，方向无误、证据真实存在，P4 已全部替换为 cards.json 逐字原句，无虚构、无 UNBACKED。
