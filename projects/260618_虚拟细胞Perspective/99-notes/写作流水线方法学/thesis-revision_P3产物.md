# Thesis Revision (P3) —— 用真实文献证据修正地基假设

> 输入：① 地基 context（第 3 节 7 步逻辑链 + thesis、第 4 节三轴、第 5 节 Claim 1–10）；② evidence-matrix.md（41 篇、1003 条逐字引文）。
> 裁决依据：**supports 以 distinct papers 为准**（不看 touchpoints，防单篇灌水）。
> 本文档给作者拍板用，有判断、有取舍、敢推翻 context。

---

## ✅ 作者最终裁定（蒋恒拍板，2026-06-18）

- **决策 A 通过**：时间段排在空间段之前、篇幅相当或更长（靠 workaround 扎堆论证撑起，把"证据薄"转成"洞见利"）。
- **决策 B 通过**：第 1 步软化为"不是单靠更大模型或更多同质 RNA 数据能突破的"（保留"瓶颈在数据"旗号，软化"不在模型"绝对表述）。
- **决策 C 通过**：开篇用三反方（数据已够多 / model-first / 噪声）先发制人。
- **★产能不强调（推翻原 outline 第 6 段定位）**：这篇文章**不为郭组打广告**，靠论证本身立住。把空间蛋白质组学证据（17/19/18/32）从"我们能补"的销售段，**降格为"这些缺口并非不可补"的可行性佐证**（证明算据标准要求的数据是可生产的）。结尾落在**算据标准 + 呼吁社区共同定义**（对接八月 AIVC Week 作为社区议程，而非郭组招牌）；郭组至多一句轻提，不单独成段。省下的 ~250 字回填三轴与反方。

> 下游（P4 成骨）以上述裁定为准；本文档 4、5 节的原 outline 第 6 段按此降格处理。

---

## 0. 一句话总览（先给结论）

证据**整体确认**了 context 的大方向（瓶颈在数据、模态不可替、空间被剥离、数据孤岛无标准），但要求三处**结构性修正**：
1. **空间与时间必须解耦、不再并列平铺**——空间是"已被广泛承认、解法在路上"的缺口（28 篇 0 challenge）；时间是"源于测量破坏性这一物理硬约束、整个领域被迫发明 workaround"的更锋利缺口（直接证据仅 9–12 篇，却被 25+ 条 workaround 反向坐实）。
2. **第 1 步"瓶颈在数据不在模型"要锐化为"数据与模型互锁"**，并正面点名 model-first 对立论题（论文 03）——不能写成"模型已解决、只剩数据"。
3. **模态不可替（第 4 步 / Claim 4）是全文真正的弹药库（22 篇）**，但必须先拆掉论文 34 这颗"脱钩=噪声"的地雷，否则整条立论被一句"大半是测量误差"击穿。

---

## 1. 逐条裁决：7 步逻辑链 + thesis

### 第 1 步「瓶颈在数据，不在模型」 → **SHARPEN（锐化，且必须软化"不在模型"的绝对表述）**

- **支持强度**：Claim 1 = 105 tp / **23 篇** supports，全场第二多论文。硬证据扎实：论文 04 实测 Geneformer/scGPT 零样本"do not consistently outperform simpler baselines"、HVG 这种最朴素基线全面胜出（04, Conclusions）；论文 05"there is no 'one-size-fits-all' method"、加细胞加扰动"did not lead to performance"（05）；论文 07"data diversity (not sheer cell count) drives model performance"（07）。
- **但有 3 条 challenge，且方向关键**：论文 01 本身的中心论点是"AI plus omics now enable fully data-driven cell models"（01, Main）——即数据-AI 已经足够；论文 01 还称生物数据"doubling every six months"。这说明"数据是瓶颈"在领域内**不是共识**，存在"数据已经够多"的对立声音。
- **裁决**：方向成立但**表述过强**。证据支持的是"**模型上限被数据的多样性/模态/时空覆盖卡住，纯靠堆模型与堆同质数据已边际递减**"，而非"模型本身没问题"。建议把"不在模型"改写为"**不是单靠更大模型或更多同质 RNA 数据能突破的**"。这同时为第 2 节论文 03（model-first）的对置留出接口。

### 第 2 步「当前数据丢了时间」 → **CONFIRMED + 升级为更锋利的缺口（见第 3 节）**

- **支持强度看似最弱**：Claim 3 = 35 tp / **仅 12 篇** supports，Axis B = 31 tp / **仅 9 篇**（全场最薄）；且伴随 30 nuance + 25 challenge（全场最争议）。
- **但这是假象，必须读 note 列**：那 25 条 challenge **几乎没有一条在反驳"我们丢了时间"**，全部是 workaround 工具——RNA velocity（24）、Monocle/pseudotime（27）、Waddington-OT（21）、谱系追踪 SCLT（22/23）、活细胞成像（30）。它们恰恰在用替代品绕开同一个硬约束。
- **硬约束的逐字铁证**：论文 21"**Because scRNA-seq destroys cells in the course of recording their profiles, one cannot follow expression of the same cell**"；论文 25"the destructive nature of single-cell RNA sequencing (scRNA-seq), which reveals only static snapshots"；论文 24"this approach captures only a static snapshot at a point in time"；论文 22"single-cell sequencing is destructive"。
- **workaround 自承是赝品**：论文 27"This 'pseudotemporal' scale of differentiation is **numerically arbitrary** and will of course vary from experiment to experiment"；论文 22"transcriptome-only trajectory inference **lacks true temporal**[context]"；论文 21 自承推断只是"distribution-to-distribution"、"only intended to capture the time-varying components of a distribution"。
- **裁决**：**CONFIRMED，且证据比 context 预想的更强、更深**——它不是"少几篇文献"的弱点，而是源于物理破坏性、被全领域 workaround 反向坐实的结构性缺口。**该升格为头条级缺口**（详见第 3、4 节）。

### 第 3 步「当前数据丢了空间」 → **CONFIRMED（最硬、可直接做主轴之一）**

- **支持强度全场最硬之一**：Claim 2 = 67 tp / **28 篇** supports / **0 challenge**；Axis C = **27 篇**；Claim 7（空间微环境改变细胞态）= 71 tp / **19 篇 / 0 challenge**。
- **逐字铁证密集且零反对**：论文 13"**tissue dissociation inevitably leads to the loss of spatial information**"；论文 11"these methods require dissociation of the tissue, thereby **destroying the spatial relationships**"；论文 07 实测"models trained only on dissociated data **fail to recover** the complexity of spatial microenvironments"，且"training on dissociated data alone (even **three times** the amount of spatial data) resulted in lower performance"；论文 14"profound impact of the cellular neighborhood on the expression of protein receptors"。
- **裁决**：**CONFIRMED，无需软化**。这是全文最安全的承重墙。但正因为太硬、太被广泛承认，它在 2000 字里应作为"**已确立、解法在路上**"的缺口处理，把更多张力分配给时间（见第 3 节不对称判断）。

### 第 4 步「模态太窄 + 各模态彼此不可替代」 → **CONFIRMED（弹药最足），但须先拆论文 34 地雷**

- **支持强度**：Claim 4 = 110 tp / **22 篇** supports；Claim 5（蛋白/代谢对功能不可缺）= 37 tp / **14 篇 / 0 challenge / 0 nuance**（罕见的零争议）；Axis A = 23 篇。
- **正交性逐字铁证**：论文 33"**Less than 20% of these loci had concordant effects on mRNA and protein**...Most loci influenced protein but not mRNA"；论文 31 关键一击"Improved accuracy in both proteomics and transcriptomics measurements **should have increased** reported correlations...but"（即测得更准也没把相关性拉上去 → 脱钩是真生物学）；论文 37"CD8+ and CD4+ T cells were partially blended together when analyzing the transcriptome but **separated clearly**"by protein；论文 11"weak global correlation between transcript and protein levels (~0.1) versus ~0.7 in bulk"；论文 35 phosphorylation 状态（非总蛋白量）才追踪细胞态；论文 36 单细胞代谢组 AUC 预测表型。
- **7 条 challenge 的真相**：多为"作者承认自己方法当前局限"（如论文 31 自承单细胞蛋白组目前限于表达层、论文 40 自承 Census 当前只有 RNA）——**这些不削弱"模态不可替"，反而印证"现状窄"**。唯一真正威胁的是论文 34（见第 2 节）。
- **裁决**：**CONFIRMED，且是全文论证密度最高、最该当主轴的一条**。但 thesis 必须把论文 34"脱钩大半是测量噪声"先正面化解（第 2 节给弹药），否则"不可替"被一句话击穿。

### 第 5 步「数据是孤岛、不可比、缺标准」 → **CONFIRMED（全场最硬、最多论文）**

- **支持强度全场之最**：Claim 9 = 152 tp / **31 篇** supports / **0 challenge**；Standard = 55 tp / 13 篇 / 0 challenge。31 篇里横跨综述、基准、平台、方法各类，几乎所有论文都顺手承认这点。
- **逐字铁证**：论文 34"reported mRNA-protein correlations are **not directly comparable across** studies"（一个分析选择就改变结论）；论文 11"same-sample profiling across platforms is what enables direct comparison"（反衬不 same-sample 就不可比）；论文 40"only ~25% of public datasets can be[reused]"、CZ CELLxGENE 靠"enforcement of a standardized schema"；论文 31"intensity values across different MS workflows are **not directly comparable**"；论文 26 要"standardization of the input and output interfaces"。
- **裁决**：**CONFIRMED，是全文最不可撼动的地基**。这条直接对接 context 的"算据标准"落点，也对接八月 AIVC Week 议程，应作为 thesis 收尾的承重句。

### 第 6 步「结论 = 算据标准（模态 × 时空 × 可整合可比）」 → **CONFIRMED**

- 由第 3/4/5 步直接推出；Standard 轴 13 篇 0 challenge 支撑。论文 01 直接背书"open data resources, data standards"、"The same entity, profiled with different technologies, should have **the same internal representation**"（01）——连最 model-first 的对手论文都认同需要统一参照系。
- **裁决**：**CONFIRMED**。这是全文的 thesis 落点，证据支持把它写成"建设性出口"。

### 第 7 步「我们能补（郭组高通量时空蛋白质组学对位）」 → **SHARPEN（可行性确认，但须诚实标注当前 trade-off）**

- **可行性支持**：Claim 6 = 69 tp / **16 篇**。逐字证据强：论文 17 DVP"links protein abundance to...phenotypes while preserving spatial context"；论文 19 scDVP 单肝细胞 ~1,700（up to 2,700）蛋白且"49% of detected proteins differ significantly between[zones]"；论文 18 S4P">9000 proteins...largest spatial proteome to date"；论文 32 单 HEK 细胞平均 3500 蛋白。
- **但 5 条 challenge 是诚实信号**：空间蛋白组**比转录组难得多**（论文 20"resolving the proteome at single-cell resolution...is much more challenging"）、当前仍需多张相邻切片重建（论文 18"eight adjacent slices are needed"）、scDVP 起步于解离单细胞悬液（论文 19）、深度随面积折损。**时间维在蛋白组里几乎是空白**（论文 19 自承"did not cover the temporal/time-course"）。
- **裁决**：**SHARPEN**。把"我们能补"写成"**高通量时空蛋白质组学已跨过可行性门槛、正是补'蛋白+空间'缺口的对位产能**"，但**不要宣称已补上时间**——蛋白组的时间维同样受破坏性约束，诚实地把它列为"标准要求、产能正在逼近"的开放项，反而更可信、也更呼应第 2 步的时间缺口。

### 总 THESIS 裁决 → **CONFIRMED 但需重构（把空间/时间并列改为分层，并先发制人处理两个反方）**

- context 原 thesis 把"空间与时间"并列、把"模态偏窄"和"不可比"顺带。证据支持每一条，但**强度极不均衡**：不可比（31p）> 空间（28p）> 模态不可替（22p）>> 时间直接证据（12p，但被 workaround 反坐实）。
- thesis 不应平铺这四块，而应**分层**：以"破坏性解离测量"作为统一病因（它**同时**制造了丢时间、丢空间、不可比三个症状），把"模态不可替"作为"为什么只补 RNA 不够"的并行支柱，最后收到"算据标准"。修正版见第 5 节。

---

## 2. 必须正面处理的张力 / 反方

### 反方 A：论文 34 = "脱钩 = 噪声" foil（直击 Claim 4 模态不可替）

- **它的逐字主张**（核实于 Claim 4 challenges / nuances 行）：
  - "**Our technical ability to accurately and reproducibly quantify both mRNAs and proteins is potentially a major factor**[that depresses correlation]"（34, Introduction）。
  - "noise in the quantification of protein abundances explains **much more (on average 3 times)** of the vari[ance in mRNA-protein correlation]"（34, Results）。
  - "the reproducibility of protein and transcript measurements is a **very significant factor**...claims about post-transcriptional[regulation must be cautious]"（34, Discussion）。
  - 即：**人们观察到的 mRNA–蛋白低相关，大半是测量误差，不是正交生物学**。如果成立，"蛋白携带 RNA 无从代偿的信息"这条核心弹药被釜底抽薪。
- **反驳路线（弹药已核实）**：
  1. **论文 31 的"测得更准也没拉上相关性"是直接反证**："Improved accuracy in both proteomics and transcriptomics measurements should have increased reported correlations by reducing the noise...[但并没有]"（31, Expression proteomics）。这正面顶住论文 34 的因果方向。
  2. **论文 33 提供因果级、非相关性证据**：它用同样本同条件配对测量、做到"equalize all environmental confounders and most of the technical biases"（33, Introduction），结论仍是"**Less than 20% of these loci had concordant effects on mRNA and protein**"、"Most loci influenced protein but not mRNA"（33, Abstract），并定位到**蛋白降解**这一具体机制、还有 YAK1→Gpd1 的**实验验证因果例子**。这是"脱钩源于真调控、非噪声"的最强一击——因为它不是统计相关，而是遗传因果。
  3. **论文 35 给机制级正交**：只有**磷酸化状态**（非总蛋白量、非 RNA）追踪 STAT3/T 细胞态；GLI3 蛋白量预测哪些基因组区域响应扰动——这是 RNA 与总蛋白都给不出的信息层。
  4. **把论文 34 收编进 Claim 9 而非让它对抗 Claim 4**：论文 34 真正证明的是"**没有统一 QC/标准，跨研究相关性根本不可比**"（"reported mRNA-protein correlations are not directly comparable across studies"，34）——这恰好是 Claim 9（31p/0 challenge）的弹药。**正确招法：承认测量噪声确实污染了一部分观测 → 但这正说明需要算据标准（QC/可比性），而非说明脱钩是假的；论文 33/31/35 在控制了噪声后脱钩依然存在 → 不可替成立。** 一举把反方转化为我方第 5 步的论据。
- **文中落位**：在模态不可替段落里用一句 steelman + 一句反转（"即便把测量噪声扣除——如 paired 因果研究 33 与去噪后仍不升的 31 所示——蛋白对 RNA 的不可替代性依然成立；噪声问题本身恰恰指向标准缺位"）。

### 反方 B：论文 03 = model-first 对立论题（全文的对手）

- **它的逐字主张**（核实于 Claim 1/3/4/8 supports 行）：
  - 主张用**引入先验知识 / compositional 架构**克服数据稀缺："Incorporating biological prior knowledge into multimodal single-cell foundation models can improve learning efficiency...[under] data sparsity"（03, Integrating prior knowledge）——即数据不够可以靠先验补。
  - "GRNs encode directed TF-target relationships"、"PPI networks capture post-transcriptional regulation"——主张用网络先验替代部分缺失测量。
  - compositional 路线：把模态拆成可组合模块，用已有模态推断缺失模态。
- **Steelman（先把对手讲到最强）**：在数据天然稀缺、配对多模态极少（这点论文 03 自己也供认："paired multimodal measurements limits their capabilities"）的现实下，纯堆数据不现实；用生物先验（GRN/PPI/通路）和组合式架构确实能在有限数据下提升泛化、做跨模态插补。这是务实且有文献支持的方向，不能稻草人化。
- **反驳路线（弹药已核实，且大量来自论文 03 自身的供认）**：
  1. **论文 03 自己划了红线**："**Without diverse observations, even the most effective models and largest datasets will fall short of capturing the true**[biology]"（03, Multi-modality）。即对手自己承认：先验补不出"从未被观测过的维度"。这是 thesis 最有力的反击——**用对手的话反驳对手**。
  2. **先验本身是脏的、不可比的**：论文 39"prior-knowledge resources are heterogeneous, and results can differ **solely[from] the choice of resource**"（39）——先验知识不是免费午餐，它继承了同样的标准缺位问题。
  3. **跨模态插补有硬天花板**：论文 20"no transcriptomics integration tool exceeded **Pearson 0.5**"（20）；论文 03 自承"cross-modal pairing is often imperfect"。当 mRNA→蛋白的真实相关只有 ~0.1–0.5（11/18/33），靠 RNA + 先验"算出"蛋白在原理上就受限。
  4. **核心论点（你方）**：再强的 compositional/prior 也**补不出从未被测量的模态与时空维度**——空间组织、真实时间轨迹、降解驱动的蛋白态，都不是 RNA + 网络先验能反推的（论文 18"protein transport away from synthesis sites...makes direct[measurement indispensable]"；论文 21 破坏性测量使真配对时间根本不存在）。**先验能压缩搜索空间，不能凭空生成观测。**
- **文中落位**：**开篇即点名对置**。用论文 03 当"主流乐观叙事"的代表（model/prior-first），steelman 一句，再用它自己的"without diverse observations...fall short"反转，自然引出 thesis："瓶颈不在能否更聪明地建模，而在我们喂给模型的细胞，从源头就被剥掉了时间、空间与多数功能模态。"

### 反方 C（context 未预见，通读全量后浮现）：「数据已经够多 / 还在指数增长」乐观论

- **逐字主张**：论文 01"the exponential increase in the throughput of measurement technologies has led to the collection of large[datasets]"、生物数据"doubling every six months"、"AI plus omics now enable fully data-driven cell models"（01, Main / challenges）。论文 13 也提 33M+ 细胞训练的基础模型。
- **为什么必须处理**：这是比论文 03 更朴素、更广泛的反方——"我们有几千万细胞、PB 级数据，何谈数据瓶颈？" thesis 若不回应，会被读者第一反应驳倒。
- **反驳路线**：把矛头从"**量**"转向"**维度/可比性**"。论文 01 自己紧接着供认"**data diversity (not just size) is critical**"（01, nuances）；论文 05"increasing the number of cells or perturbations...did not lead to performance[gains]"；论文 04"larger pretraining datasets do not always increase...performance"、33M 细胞的 scGPT 被更小模型打败。**核心反转：海量 ≠ 有用。 90%+ 是解离式 RNA snapshot——同一个被剥掉时空、缺多数模态的窟窿，复制了几千万遍。** 论文 40 直接坐实模型就绪的 Census 语料"covering all RNA non-spatial...transcriptomic data"。这条反方反而成了 thesis 最有冲击力的开场对比："数据在以每六个月翻倍的速度增长，模型却在更大的同质数据上边际递减——因为我们扩张的是同一种残缺。"

### 反方 D（次要、诚实标注）：多模态联测会降低各模态质量（trade-off 内生）

- 论文 35"simultaneous profiling of[multiple modalities]degrades each modality"、"experimental trimodal measurement trades off data quality"；论文 31/32 throughput-vs-depth。
- **应对**：这不削弱 thesis，反而强化"为什么需要标准+整合"——既然完美的 same-cell 全模态联测目前物理受限，就更需要可比、可整合的标准把分别测的模态拼起来（对接 Claim 8 = 30p、Claim 9 = 31p）。一笔带过即可，不展开。

---

## 3. 空间 vs 时间不对称的最终判断

### 判断：不对称**成立**，且应在文中明确写成"时间是比空间更锋利、更结构性的缺口"。

理由三层：

**(1) 证据形态不同，不是证据多寡的问题。**
- 空间：28 篇直接 supports、**0 challenge**（Claim 2），证据是"大家都同意、且在补"。它是**广度型共识**。
- 时间：直接 supports 仅 12 篇（Claim 3）、Axis B 仅 9 篇，但 challenge 高达 25。**关键在于：那 25 条 challenge 没有一条说"时间没丢"，全是 workaround**。所以时间的真实证据强度不能用 supports 论文数读，要用"**领域被迫发明多少替代品**"来读——这是**深度型铁证**。

**(2) 病因层级不同，时间更深。**
- 空间缺口的病因是"**解离这一步骤**"——可以通过 in situ / 空间组学**绕过**（论文 13/11/15/07 都在演示绕过方案，解法在路上）。
- 时间缺口的病因是"**测序是破坏性的、测完即死**"——这是**测量的物理本质**，无法靠换一种测序方式绕过。论文 21 一句定性："**Because scRNA-seq destroys cells in the course of recording their profiles, one cannot follow expression of the same cell**"。**你无法对同一个已死的细胞再测第二个时间点。** 这比"解离丢了邻居"更不可逆。

**(3) "workaround 扎堆"本身就是缺口的铁证——这是全文最聪明的一个论证，应重点展开。**
- 论证结构："如果真配对时间数据存在，就不会有这么多互相竞争、各自承认不可靠的替代品。替代品的繁荣 = 真数据的缺席。"
- **支撑逐字原句（按 workaround 类型，全部带论文号）**：
  - **破坏性硬约束（病因）**：论文 21"scRNA-seq destroys cells...one cannot follow expression of the same cell"；论文 25"the destructive nature of single-cell RNA sequencing, which reveals only static snapshots"；论文 24"captures only a static snapshot at a point in time"；论文 33"Standard methods for mRNA quantification require **lysis** of cell cultures or tissues"。
  - **替代品 1 · 伪时序自承是赝品**：论文 27"This 'pseudotemporal' scale of differentiation is **numerically arbitrary** and will of course vary from experiment to experiment"；论文 27"distinct individual cells are treated as surrogate[time points]"（把不同细胞当成同一细胞的不同时刻——这是一个不得已的概念偷换）；论文 26"Real per-cell sampling times are **often unavailable** and are substituted[by inference]"。
  - **替代品 2 · RNA velocity 建在假设上**：论文 23"RNA velocity inference...rests on assumptions such as constant gene-specific[kinetics]"；论文 24 自承时间视界仅"a few hours"、velocity"embedding-dependent"。
  - **替代品 3 · 轨迹推断只能"分布到分布"**：论文 21"distribution-to-distribution"、"only intended to capture the time-varying components of a distribution"；论文 21 综述 62 种轨迹方法"**none both incorporate time and model cell growth**"。
  - **替代品 4 · 谱系追踪是工程黑客且不能用于人**：论文 22"single-cell sequencing is **destructive**, motivating[synthetic barcodes]"；论文 22"both approaches require transgenesis, **restricting their use to model organisms**"（人体里连这条 workaround 都用不了）。
  - **替代品 5 · 活细胞成像只读形态、非分子**：论文 30"Time-lapse microscopy is the **only** method that can directly capture the dynamics...of[live cells]"——但它只读 shape/size，读不出分子态（Emergent theme 已标注"imaging modality reads only shape/size"）。
- **一句话收口（可直接进文章）**：领域不是没意识到时间——它发明了伪时序、RNA velocity、最优传输、谱系条形码、活细胞成像五套互不相容、各自承认不可靠的替代方案，**正是因为唯一能消除歧义的东西——对同一个细胞跨时间的成对观测——被测量的破坏性从物理上禁止了。**

### 落位建议
- 空间：写成"**已确立、解法在路上**"——快速、密集、零争议地确立，不必反复论证。
- 时间：写成"**更深、更被掩盖**"——用 workaround 扎堆这一反直觉论证制造文章的智识高点。**这是把一个"看起来证据薄"的 claim 转成"全文最锋利洞见"的关键操作。**

---

## 4. 精简后的主线骨架（~2000 字够装的那几条）

2000 字英文装不下 10 个 claim 平铺。取舍原则：**1 个对置开场 + 3 根主轴（时间/空间/模态）+ 1 个标准出口 + 1 个产能落点**，其余降为支撑句或一笔带过。

| Claim | 角色 | 处理 |
|---|---|---|
| Claim 1（瓶颈在数据） | **开场对置的靶心** | 锐化为"模型-数据互锁"，借论文 03/01 对置引出 |
| Claim 4（模态不可替） | **主轴①** | 头条级，弹药最足（22p），先拆论文 34 |
| Claim 2 + 7（丢空间 / 微环境改态） | **主轴②** | 合并，最硬（28p+19p/0ch），写成"已确立缺口" |
| Claim 3 / Axis B（丢时间） | **主轴③ + 智识高点** | workaround 扎堆论证，写成"最锋利缺口" |
| Claim 9（孤岛/不可比/缺标准） | **收口承重句** | 最硬（31p/0ch），通向算据标准 |
| Claim 8（需整合） | 支撑句 | 并入主轴②③与标准段，不独立成段 |
| Claim 5（蛋白/代谢功能不可缺） | 支撑句 | 并入主轴①，作"为什么蛋白不可省"的脚注 |
| Claim 6（时空蛋白组可行） | 产能落点 | 并入结尾"我们能补"，诚实标注 trade-off |
| Claim 10（三难困境） | 一笔带过 | 仅在解释"为何不能既要分辨率又要通量又要无损"时点一句 |
| Standard 轴 | 出口主旨 | 与 Claim 9 合并成 thesis 落点 |

### 段落级 outline（每段一句主旨 + 挂 claim + 用哪几篇）

1. **开场 · 对置**（~250字）：主旨——"AIVC 在模型上狂奔，主流乐观叙事认为 AI+omics 或 compositional/prior 已能补足数据稀缺（论文 03/01），但这绕过了一个更根本的问题：我们喂给模型的细胞，从测量源头就被剥掉了时间、空间与多数功能模态。" 挂 Claim 1。证据：01（"fully data-driven"乐观 + "data diversity is critical"自我软化）、03（compositional/prior，但"without diverse observations...fall short"）、04/05（更大模型/更多同质数据边际递减）。**先发制人处理反方 C（数据已够多）。**

2. **主轴③ · 时间（先打最锋利的）**（~400字）：主旨——"最深的缺口是时间，因为测序是破坏性的：测完即死，同一细胞无法被前后成对观测；领域被迫发明五套互不相容的替代品，这种 workaround 的繁荣本身就是真数据缺席的铁证。" 挂 Claim 3 / Axis B。证据：21（destroys cells）、25/24（static snapshot）、27（pseudotime numerically arbitrary）、22（destructive + 人体不可用）、30（成像只读形态）。**把"证据薄"转成"洞见利"。**

3. **主轴② · 空间**（~300字）：主旨——"第二个缺口是空间，已被广泛确立、解法在路上：解离不可逆地摧毁组织架构，而邻域微环境实质改变细胞态。" 挂 Claim 2 + 7。证据：13（dissociation loses spatial info）、07（解离数据 3 倍量仍输）、14（neighborhood 改变蛋白受体）、11（空间 RNA-蛋白相关仅 ~0.1）。写得快、密、不缠斗（因为零争议）。

4. **主轴① · 模态不可替**（~400字）：主旨——"即便补上时空，只测 RNA 仍拼不出细胞：各模态承载彼此无从代偿的信息。" 挂 Claim 4 + 5。证据：33（<20% loci concordant，因果级）、31（测得更准也不升相关 → 真生物学）、37（蛋白分开 CD4/CD8）、35（磷酸化态才追踪细胞态）、36（代谢组预测表型）。**在此段内拆论文 34 地雷（steelman + 反转，见第 2 节）。**

5. **收口 · 算据标准**（~350字）：主旨——"这三个缺口加上一个共同后果——各数据集各自为政、跨实验室不可比——指向同一个出口：虚拟细胞需要一套显式编码时空、覆盖不可互替模态、可整合可比的算据标准。" 挂 Claim 9 + 8 + Standard。证据：40（仅 25% 数据可复用 / 标准化 schema）、34（相关性跨研究不可比 → 收编反方 A）、01（同一实体不同技术应同一表示）、26/31（呼吁统一接口/格式）。

6. **落点 · 我们能补**（~250字）：主旨——"高通量时空蛋白质组学已跨过可行性门槛，正对位'蛋白+空间'缺口，并有条件参与定义这套标准（呼应八月 AIVC Week）。" 挂 Claim 6（SHARPEN）。证据：17（DVP 保空间）、19（scDVP 单肝细胞 1700+ 蛋白、49% 分区差异）、18（>9000 蛋白空间组）、32（单细胞 3500 蛋白）。**诚实标注：时间维仍是开放项（论文 19 自承未覆盖 time-course），把它留作标准的待补格，而非夸口已解决。**

> 结构如何体现不对称：**时间段排在空间段之前、且篇幅相当甚至更长**（与"直接证据更少"形成张力，靠 workaround 论证撑起），空间段写得最快最密。读者会感到"越被广泛承认的缺口反而越快带过，越被掩盖的缺口越值得停留"——这正是证据对 context 的修正在结构上的落地。

---

## 5. 修正后的 thesis 与逻辑链

### 修正后的 thesis 段落（中文，1 段）

> AI 虚拟细胞正在模型一侧狂奔，主流乐观叙事认为：只要 AI 足够强、或引入足够的生物学先验与组合式架构，就能补足数据的稀缺。但这绕过了一个更根本的事实——问题不在我们能否更聪明地建模，而在我们喂给模型的"细胞"，**从测量源头就是残缺的**。主流范式（解离式单细胞测序）的一次破坏性操作，同时制造了三个不可替代品弥补的窟窿：测序**破坏性地杀死细胞**，使同一细胞无法被跨时间成对观测——这是最深的缺口，深到整个领域只能发明伪时序、RNA velocity、最优传输、谱系条形码等一系列**互不相容、各自承认不可靠的替代品**，而替代品的繁荣恰恰证明真配对时间数据并不存在；解离又**不可逆地摧毁了组织的空间架构**，而邻域微环境实质性地改变细胞状态；同时这套范式**几乎只测 RNA**，而蛋白、PTM、代谢、空间分布等模态承载着 RNA 无从代偿的信息——即便扣除测量噪声，配对因果研究显示同一基因的 mRNA 与蛋白也大多不一致。更糟的是，这些本就残缺的数据还**各自为政、跨实验室不可比**，一个分析选择就能翻转结论。因此，虚拟细胞真正缺的不是模型或更多同质数据——是一套**显式编码时空、覆盖彼此不可替代的多模态、且可整合可比的"算据标准"**。本文论证这套标准应包含什么、为什么、现在缺在哪；而高通量时空蛋白质组学，正是补上"蛋白+空间"缺口、并参与定义这一标准的对位产能。

### 修正后的逻辑链（替换 context 第 3 节 7 步，精简为 6 步）

1. **不是模型问题、也不是数据量问题——是数据维度问题。** 基础模型在更大的同质 RNA 数据上边际递减（04/05），数据以每六个月翻倍却仍卡住（01）；因为我们扩张的是**同一种残缺**。对手主张靠 compositional/prior 补（03），但其自承"without diverse observations, even the best models and largest datasets fall short"——先验补不出从未被观测的维度。
2. **一次破坏性解离，制造三个同源缺口。** 把"丢时间/丢空间/不可比"统一到**测量的破坏性 + 解离**这一共同病因，而非三个孤立现象。
3. **缺口①时间（最深）：破坏性测量禁止成对观测。** 测完即死（21/25/33），真配对时间数据从物理上不存在；五套 workaround 的繁荣（27 伪时序"numerically arbitrary"、24 velocity、21 OT、22 谱系、30 成像）= 缺口的铁证。
4. **缺口②空间（已确立）：解离不可逆摧毁组织架构。** 邻域微环境实质改变细胞态（14/07/13/11），零争议（Claim 2 = 28p/0ch），解法在路上。
5. **缺口③模态不可替：只测 RNA 拼不出细胞。** 模态正交（33 因果级 <20% concordant、31 去噪后仍不升、35 磷酸化态、36 代谢）；先正面化解"脱钩=噪声"（34）——噪声确实存在，但控制噪声后脱钩仍在，且噪声问题本身指向标准缺位。
6. **共同后果 + 出口：不可比 → 算据标准 → 我们能补。** 残缺数据还各自为政、不可比（Claim 9 = 31p/0ch，40/34/01）；出口是显式编码时空 × 跨不可替模态 × 可整合可比的算据标准（Standard 13p/0ch）；高通量时空蛋白质组学对位"蛋白+空间"缺口（6 = 16p，17/19/18/32），诚实地把"时间维"留作标准的待补格。

---

## 附：裁决速查表

| context 逻辑链步骤 | 裁决 | supports 论文数 | 一句话理由 |
|---|---|---|---|
| 1 瓶颈在数据不在模型 | SHARPEN | 23p (Claim 1) | 软化"不在模型"→"非更大模型/更多同质数据可破"；点名对手 03 |
| 2 丢时间 | CONFIRMED↑升格 | 12p 直接 / 9p Axis B，但 25 workaround 反坐实 | 物理破坏性 + workaround 扎堆 = 最锋利缺口 |
| 3 丢空间 | CONFIRMED | 28p / 0ch（最硬之一） | 已确立、零争议、解法在路上 |
| 4 模态不可替 | CONFIRMED（须先拆 34） | 22p；Claim5=14p/0ch | 弹药最足；33/31/35 反驳"脱钩=噪声" |
| 5 孤岛/不可比/缺标准 | CONFIRMED | 31p / 0ch（最硬） | 全文承重地基，通向算据标准 |
| 6 结论=算据标准 | CONFIRMED | Standard 13p/0ch | 连对手 03/01 都认同需统一参照系 |
| 7 我们能补 | SHARPEN | 16p（Claim 6） | 可行性确认；诚实标注时间维仍开放、trade-off 仍在 |
| 总 thesis | CONFIRMED 但重构 | —— | 空间/时间从并列改分层；先发制人处理 34/03/数据量乐观论 |
