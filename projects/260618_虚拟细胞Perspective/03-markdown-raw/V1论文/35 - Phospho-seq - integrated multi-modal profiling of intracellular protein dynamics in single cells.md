Article

https://doi.org/10.1038/s41467-025-56590-7

# Phospho-seq: integrated, multi-modal pro<sup>fi</sup>ling of intracellular protein dynamics in single cells

Received: 15 November 2024

Accepted: 22 January 2025

Published online: 04 February 2025

Check for updates

John D. Blair<sup>1,2</sup>, Austin Hartman<sup>1,4</sup>, Fides Zenk <sup>3,4</sup>, Philipp Wahle <sup>3</sup>, Giovanna Brancati <sup>3</sup>, Carol Dalgarno<sup>1</sup>, Barbara Treutlein <sup>3</sup> & Rahul Satija <sup>1,2</sup>

Cell signaling plays a critical role in neurodevelopment, regulating cellular behavior and fate. While multimodal single-cell sequencing technologies are rapidly advancing, scalable and <sup>fl</sup>exible pro<sup>fi</sup>ling of cell signaling states alongside other molecular modalities remains challenging. Here we present Phospho-seq, an integrated approach that aims to quantify cytoplasmic and nuclear proteins, including those with post-translational modi<sup>fi</sup>cations, and to connect their activity with cis-regulatory elements and transcriptional targets. We utilize a simpli<sup>fi</sup>ed benchtop antibody conjugation method to create large custom neuro-focused antibody panels for simultaneous protein and scATACseq pro<sup>fi</sup>ling on whole cells, alongside both experimental and computational strategies to incorporate transcriptomic measurements. We apply our work-<sup>fl</sup>ow to cell lines, induced pluripotent stem cells, and months-old retinal and brain organoids to demonstrate its broad applicability. We show that Phosphoseq can provide insights into cellular states and trajectories, shed light on gene regulatory relationships, and help explore the causes and effects of diverse cell signaling in neurodevelopment.

The ability to carefully regulate responses to external and internal signals is essential for proper cellular function. Maintaining precise control of signaling networks enables cells to achieve homeostasis in response to environmental changes and to progress through key developmental and functional transitions<sup>1</sup>. Signal transduction links the activation of signaling pathways to downstream changes in cellular chromatin<sup>2</sup>, transcription<sup>3</sup>, and translation<sup>4</sup>, and is primarily regulated by changes in post-translational modi<sup>fi</sup>cations<sup>5</sup>. For example, changes in phosphorylation can signi<sup>fi</sup>cantly alter receptor kinetics<sup>6</sup>, enzymatic function<sup>7</sup>, and transcription factor localization and activity<sup>8</sup> via conformational changes<sup>9</sup>.

Cell signaling pathway activity is known to vary throughout neurodevelopment, and when disrupted, it can have signi<sup>fi</sup>cant effects on cell fate decisions. For instance, uncontrolled mTOR pathway activity caused by the loss of the upstream regulator TSC2 leads to a signi<sup>fi</sup>cant increase in astrogliosis, which is a hallmark of the neurodevelopmental disorder, tuberous sclerosis<sup>10</sup>. Additionally, changes in Wnt signaling have been associated with autism spectrum disorder<sup>11</sup>. To gain a deeper understanding of the causes and consequences of aberrant signaling, a crucial challenge is to connect heterogeneity in the activation of signaling pathways with broader changes in molecular state. Therefore, methods that can accurately measure and quantify phosphorylation states at single-cell resolution alongside additional molecular modalities offer substantial promise to improve our understanding of cellular activity and function.

Phospho-proteins are typically quanti<sup>fi</sup>ed in single cells using antibody-based methods including immunocytochemistry, <sup>fl</sup>ow cytometry<sup>12</sup>, or CyTOF<sup>13</sup>, which can be multiplexed to detect dozens of targets. Single-cell sequencing technologies offer an exciting opportunity to build upon these approaches, particularly with the recent introduction of multiomic technologies that enable the quanti<sup>fi</sup>cation of multiple modalities of information within the same cell<sup>14–21</sup>. For example, CITE-seq<sup>15</sup>, REAP-seq<sup>19</sup>, DOGMA-seq<sup>18</sup>, and TEA-seq<sup>20</sup> all stain cells with large panels of oligonucleotide-tagged antibodies against cell surface proteins in order to quantify cellular immunophenotypes alongside cellular transcriptomes, chromatin accessibility pro<sup>fi</sup>les, or both. While powerful, these technologies focus exclusively on the pro<sup>fi</sup>ling of cell surface proteins. They are therefore widely applied to analyze hematopoietic samples, where well-characterized panels of cell surface proteins are associated with distinct cell states, but have limited utility in other contexts, including neurodevelopment.

Multiple pioneering approaches have built upon these methods, aiming to utilize single-cell multimodal technologies to pro<sup>fi</sup>le intracellular and intranuclear proteins in diverse biological contexts. These include ASAP-seq<sup>18</sup>, which introduces a set of <sup>fi</sup>xation and permeabilization conditions that are compatible with chromatin accessibility pro<sup>fi</sup>ling in whole cells. Additionally, inCITE-seq<sup>21</sup> and NEAT-seq<sup>1</sup> utilize specialized approaches for intranuclear protein pro<sup>fi</sup>ling, which signi<sup>fi</sup>cantly reduce background signal originating from non-speci<sup>fi</sup>c electrostatic interactions between oligonucleotide-conjugated antibodies and charged cellular components. Alternatively, one can <sup>fi</sup>x, stain and sort cells into high and low populations of individual phospho-proteins, performing single-cell sequencing on the identi<sup>fi</sup>ed populations, as in INs-seq<sup>22</sup>. While each of these methods addresses key challenges, they perform pro<sup>fi</sup>ling of small (3–7) intracellular panels due to a reliance on commercially conjugated antibodies. QuRIE-seq aims to pro<sup>fi</sup>le larger panels, but requires custom instrumentation and is not compatible with primary cell samples<sup>17</sup>. Lastly, while NEAT-seq utilizes the 10x Multiome kit for trimodal nuclear pro<sup>fi</sup>ling, no existing approaches can quantify intracellular proteins (including phosphorylation states), transcriptional output, and chromatin pro<sup>fi</sup>ling in the same biological system.

Here we present Phospho-seq, a multi-modal single-cell work<sup>fl</sup>ow for quantifying cell signaling via phosphorylated cytoplasmic and nuclear proteins in conjunction with chromatin accessibility and gene expression levels (either directly measured experimentally, or integrated computationally<sup>23</sup>). By optimizing a broadly accessible antibody conjugation strategy<sup>24</sup>, we designed custom panels to pro<sup>fi</sup>le up to 64 intracellular proteins (including 20 phospho-states), and applied this work<sup>fl</sup>ow to both retinal organoids and brain organoids. We used the trimodal chromatin, RNA, and protein data to discover novel transcription factor-cis-regulatory element-gene associations including telencephalic and diencephalic lineage-speci<sup>fi</sup>c relationships. We further used the phosphorylated protein data to identify lineage-speci<sup>fi</sup>c patterns of Wnt and MAPK/ERK signaling, and to link these differences to upstream and downstream molecular networks. Overall, we demonstrate the utility of Phospho-seq for the high throughput discovery of interactions between cell signaling, gene regulation, and gene expression in neural tissue, opening the door for future discoveries in other cell types and tissues.

## Results

## Benchtop conjugation enables antibody panel customization in Phospho-seq

In developing Phospho-seq, we aimed to create a user-friendly, singlecell method to quantify proteins from the cell surface, cytoplasm, and nucleus alongside additional molecular modalities. To maximize utility, we aimed for the assay to 1) allow for maximum customizability by the user for which proteins to quantify, 2) rely only upon commercially available reagents and equipment, and 3) maintain the sensitivity and speci<sup>fi</sup>city of single-modality assays. Towards these goals, Phosphoseq combines aspects of previously established single-cell protein and chromatin accessibility quanti<sup>fi</sup>cation methods<sup>16,18</sup>. In brief, samples are dissociated into single-cells, <sup>fi</sup>xed, permeabilized, hashed, stained for intracellular proteins with self-conjugated DNA-bound antibodies, and run through the 10X Genomics single-cell ATAC-seq protocol (Fig. 1A and Methods).

A major limitation of large-scale sequencing-based intracellular pro<sup>fi</sup>ling is the lack of commercially available oligonucleotide-tagged antibodies. Premade antibody panels target immune cell surface antigens<sup>25</sup>, while custom commercial antibody conjugation is often prohibitively expensive, especially for larger panels. To overcome this issue, we optimized a simple benchtop click-chemistry-based conjugation protocol<sup>24</sup> (Fig. 1B) to generate panels of uniquely-indexed oligonucleotide-conjugated antibodies. This approach is scalable, cost-effective (\~\$8/conjugation), and compatible with unconjugated commercial antibodies that are routinely used for immuno-<sup>fl</sup>uorescence or <sup>fl</sup>ow cytometry, even those with carrier proteins (Fig. 1C, Fig. S1A, B). Phospho-seq is compatible with antibodies conjugated to different oligonucleotide sequences, including the widely used TotalSeq-A and TotalSeq-B sequences, through the use of a bridge oligonucleotide for capture on the gel beads<sup>18</sup>.

During the optimization of our conjugation protocol, we found that the ratio of antibody to oligonucleotide and post-conjugation puri<sup>fi</sup>cation steps were crucial for minimizing nonspeci<sup>fi</sup>c binding while maintaining a high recovery yield. Through titration experiments, we determined that adding 15 pmol of oligonucleotide per μg of antibody (equivalent to 2–4 copies of oligonucleotide per antibody molecule) was optimal (Fig. 1D, Fig. S1C). For post-conjugation puri<sup>fi</sup>cation, we found that two steps: an initial precipitation step using 40% ammonium sulfate<sup>26</sup>, followed by 5–7 washes through a 50 kDa molecular weight cut-off (MWCO) <sup>fi</sup>lter, were necessary to reduce unbound oligonucleotide while preserving antibody yield (Fig. S1D).

To optimize and con<sup>fi</sup>rm that our Phospho-seq procedure could retain cell-to-cell differences in intracellular antibody levels, we utilized <sup>fl</sup>ow cytometry experiments on whole cells. We <sup>fi</sup>rst con<sup>fi</sup>rmed that light <sup>fi</sup>xation and gentle detergent-based permeabilization, as suggested by ASAP-seq<sup>18</sup>, achieved the necessary balance between maintaining the structural integrity of the cell membrane while allowing the <sup>fl</sup>ow of unconjugated antibodies into the nucleus and cytoplasm (Methods, Fig. 1E). We also found that the addition of singlestranded DNA binding protein (SSB) to our antibody pool before staining, as pioneered for nuclear pro<sup>fi</sup>ling with NEAT-seq<sup>16</sup>, was essential to reduce background signal from oligonucleotideconjugated antibodies. Combining these approaches, we utilized <sup>fl</sup>ow cytometry to successfully quantify clear SOX2 expression differences in heterogeneous mixtures of whole cells using an oligonucleotide-conjugated antibody (Fig. 1E and Fig S1E,F).

## Phospho-seq simultaneously quanti<sup>fi</sup>es phosphorylated, cytoplasmic, and nuclear proteins

To evaluate the full Phospho-seq work<sup>fl</sup>ow on whole cells, we <sup>fi</sup>rst tested a small panel of both nuclear and cytoplasmic proteins on a heterogeneous cell line mixture. Our panel included antibodies against the transcription factors OCT4, SOX2, and GATA1, which are expected to be differentially expressed between K562 cells and induced pluripotent stem cells (iPSCs). We also aimed to quantify phosphorylated ribosomal protein S6 (pRPS6) expression, a readout of PI3K/AKT/ mTOR pathway activation, along with antibodies quantifying total RPS6 levels. We exposed cells to either epidermal growth factor for 1 h (EGF, activating) or PX-866 for 4 h (inhibiting) to modulate pathway activation, and utilized cell surface hashing antibodies<sup>27</sup> to perform multiplexed pro<sup>fi</sup>ling of cells in resting, activated, or inhibited conditions.

We found that Phospho-seq was able to quantify nuclear, cytoplasmic (including phosphorylated), and cell surface proteins alongside chromatin accessibility. Dimensional reduction of scATAC-seq pro<sup>fi</sup>les successfully discriminated the two cell lines and was concordant with the cell hashing-based demultiplexing. (Fig. 1F and S1G, H). Antibody-derived tags (ADTs) for the de<sup>fi</sup>ning canonical transcription factors OCT4, SOX2 (iPSCs) and GATA1 (K562) showed differences between the two cell types (OCT4 Staining Index (SI)I:1.22; < 0.001, SOX2 SI:0.56; < 0.001, GATA1

A  
![](images/69bc642ca47c4760924d52a1ec764f47e79d4f81f12b33eb4016e8931d5ccce1.jpg)  
B

![](images/be20dd2afd0626277fad402f1b155bb562d5a7ed0f365f346060398473c9baa2.jpg)  
C  
E

D  
![](images/fef99447a429d8165c987b8568e4673ae0388925bc87890397172c7ab1babc68.jpg)

![](images/c867e90790348dd45d2d1912546cbfdbc01c1ac8c0be90f252fae43a9e005b7a.jpg)

![](images/893dfffc16717f5c07678d55cdcdc32c6f6f290fc9c32b9b7ebe20d6854a8add.jpg)

![](images/471b083517ad5ea278d8a16eb5e5d7858b14b4fbb7f232cf53e322ed67e42ccd.jpg)

![](images/0f4717cdd2370f5ca65ad1ca066c8aecc6958e18164d717615aa873fee7bf4c2.jpg)

F  
![](images/fdaafdfcdc50852c89ce94612dd8945bb24eb492a39e4c82f3aabb9b3042c1cb.jpg)  
G

![](images/48be6bc92d885f7ace79e77bbbdad94dca4c8c2808a81bd20806928f24940688.jpg)

H  
![](images/14305eb9dfeaaa375d61118998e41117d43e518e129dd8af3928b5e2d62ca174.jpg)

![](images/aeb2d44c2a9486ba97c278b011f9e435725895f8b83058d05a81dd0219e38deb.jpg)

![](images/f7820f55c5b9134d20e3690cb4329c0b3d266c65186ac7c7c6827da9e602d91e.jpg)

![](images/c56171927d60b137cb48206058b85653a9b7a8fd7f4e944d2ecfbb99c0aca8cb.jpg)

![](images/26b41037c60d8f0b90e9d90d82d0562daf59d2e2549565040caec493f5b60ad1.jpg)  
ATAC sequencing Nuclear Protein Cytoplasmic Proteins Phosphorylated Proteins Surface Proteins (Hashing)

N  
![](images/e48b3be193c01e9def7c87ee833556ae7e71f18efef75e282bf08a5ba3a29eb1.jpg)

O  
![](images/1796e0c3694409a6b1f06a775e86f87f83460d4cd0e0bc6a561f639e3fb92297.jpg)  
P

![](images/c68d9d86fa11e7a354c87bc59ced12742e0de5c06ec780fb4db64c1441d9b919.jpg)

![](images/6259a95c2104126dca3533915a44d6b59e2c35bb5f4b98f1bd055e8ec91f634d.jpg)  
Fig. 1 | Phospho-seq experimental work<sup>fl</sup>ow and pilot experiment. A Schematic of Phospho-seq work<sup>fl</sup>ow. B Schematic of antibody conjugation procedure. C Protein gel results of two antibody (Ab) puri<sup>fi</sup>cation methods using the Abcam BSA Removal Kit (left panel) and Promega Magne Protein G beads (right panel). This experiment was performed once. D Protein gel of mTz-PEG4-NHS labeled antibodies incubated with different quantities of TCO-PEG4-NHS labeled ssDNA tags. This experiment was performed once. E Flow cytometry plots of K562 and iPS cells stained with unconjugated and conjugated SOX2 antibodies (left panel) and cells stained with unconjugated and conjugated + single-stranded DNA binding protein SOX2 antibodies (right panel) with unstained controls. F UMAP representation from scATAC-Seq of K562 and iPS cells colored by demultiplexed HTOs assigned to each cell. G UMAP representation of K562 and iPS cells colored by normalized ADT values for OCT4. H UMAP representation of K562 and iPS cells colored by  
normalized ADT values for GATA1. I Coverage plot of chromatin accessibility of K562 and iPS cells at the POU5F1 (OCT4) genomic locus. J Violin plot of chromVAR scores for the OCT4 TF binding motif (MA1115.1) in K562 and iPS cells. K Coverage plot of chromatin accessibility of K562 and iPS cells at the GATA1 genomic locus. L Violin plot of chromVAR scores for the GATA1 TF binding motif (MA0140.2) in K562 and iPS cells. M Schematic of PI3K/AKT/mTORC1 pathway activation and repression paradigm used in this experiment. N Scatter plot of pseudobulked chromatin accessibility data in 5 kb windows across the genome comparing inhibited K562 cells with stimulated K562 cells. Red line indicates perfect correlation between the two conditions. O Violin plot of normalized pRPS6 values in stimulated (Stim) and inhibited (Inhib) K562 cells. P Violin plot of normalized RPS6 values in stimulated (Stim) and inhibited (Inhib) K562 cells.

SI:1.29; $p { < } 0 . 0 0 1 )$ (Fig. 1G, H and Fig S1I). These pro<sup>fi</sup>les were also con-<sup>p</sup>cordant with the chromatin accessibility landscape at each protein’s genomic locus (Fig. 1I, K and S1J) and genome-wide transcription factor motif activity estimates as quanti<sup>fi</sup>ed by chromVAR<sup>28</sup> (Fig. 1J, L and S1K).

Moreover, while changes in PI3K/AKT/mTOR pathway (Fig. 1M) activity did not drive genome-wide changes in chromatin accessibility (Fig. 1N), we observed a clear increase in pRPS6 levels within stimulated cells compared to inhibited cells (Fig. 1O) independent of total

RPS6 levels (Fig. 1P). This re<sup>fl</sup>ects a biological context where phosphorylation measurements are highly informative for distinguishing cellular states even when genome-wide modalities cannot. We also observed higher phosphorylation of the nuclear transcription factor STAT3 in iPSCs compared to K562 cells, and found that only pSTAT3 levels (as opposed to total protein levels) correlated with STAT3 transcription factor activities (Fig S1L). We conclude that we can therefore measure phosphorylation states for both cytoplasmic and nuclear activities, and that phosphorylated protein levels are more re<sup>fl</sup>ective of cellular state and transcription factor activities compared to total protein levels.

We further observed that Phospho-seq was capable of quantifying more subtle differences, even within the same cell type. Epigenetic differences between iPS donor cell lines are frequently observed and often lead to biased differentiation tied to cell signaling differences<sup>29</sup>. In our dataset, we observe the segregation of the three iPSC donors used in this experiment based on chromatin accessibility (Fig S1M) as well as an enrichment of pRPS6 signal in one donor in particular (Fig. S1N). These types of observations may be highly informative when assessing the differentiation capacity of different iPSC lines.

While the previous analyses qualitatively demonstrate the multimodal capabilities of Phospho-seq, we next aimed to quantitatively assess the protein measurements from Phospho-seq, and to benchmark them against alternative technologies. We leveraged quantitative metrics—originally developed for <sup>fl</sup>ow cytometry—that are widely used to perform relative comparisons of protocols and experimental conditions - in particular, the staining index (SI) leverages both the median and variance of protein levels between two populations<sup>30</sup>. We performed two quantitative benchmarking experiments that leveraged this metric.

First, we performed both <sup>fl</sup>ow cytometry and Phospho-seq on two cell lines, K562 and HEK. We used antibodies against a panel of four cytoplasmic proteins (ELA2, VIM, APPL1, and IFITM1), a surface protein (CD55), and a nuclear protein (GATA1) that we expected to show abundance differences between the two cell lines (with the exception of ELA2, a negative control). Both technologies exhibited upregulation of GATA1, CD55, and IFITM1 in K562 cells, and VIM and APPL1 in HEK cells (Fig. S2A,B). While Phospho-seq exhibited a higher SI on average (mean SI = 1.26 vs. 0.74. for <sup>fl</sup>ow cytometry), we did not identify a statistically signi<sup>fi</sup>cant difference between the two ( = 0.375; <sup>p</sup>Fig. S2C), suggesting that our Phospho-seq data is comparable to goldstandard approaches. These <sup>fi</sup>ndings are consistent with previous work that suggests that the dynamic range of sequencing-based protein quanti<sup>fi</sup>cation matches and may in fact exceed traditional colorimetric cytometry, as the sequencing-based measurements are digital, contain unique molecular identi<sup>fi</sup>ers, and may be less affected by saturation of the detector<sup>15</sup>. Moreover, we quanti<sup>fi</sup>ed each protein in serial independent stains for <sup>fl</sup>ow cytometry (removing any possibility of spectral overlap), while the inherent multiplexing of Phospho-seq enabled all proteins to be quanti<sup>fi</sup>ed in a single experiment.

Second, we quantitatively benchmarked Phospho-seq with ASAPseq<sup>18</sup>, the only other technology that is described as being capable of simultaneous intracellular protein and chromatin pro<sup>fi</sup>ling at singlecell resolution. Here, we took a complementary approach where we obtained an estimate of ‘ground truth’ protein levels from <sup>fl</sup>ow cytometry, ran the same sample through the sequencing-based assay, and compared the two results. To accomplish this, we stained cells with a mixture of pRPS6 antibodies, enabling them to be <sup>fi</sup>rst pro<sup>fi</sup>led by FACS, and subsequently by sequencing. Using chemical stimulation (Methods) we generated a heterogeneous population of K562 cells, divided this into four gated populations based on pRPS6 measurements from <sup>fl</sup>ow cytometry, and subsequently pro<sup>fi</sup>led each gate with Phospho-seq, ASAP-seq and <sup>fl</sup>ow cytometry (Fig. S2D–J). Comparing the mean expression of pRPS6 between gated populations in Phosphoseq, we observed quantitative agreement ( <sup>2</sup> = 0.90), highlighting the <sup>R</sup>consistency of Phospho-seq with ground truth measurements (Fig. S2L). With ASAP-seq, we observed a weaker correlation ( <sup>2</sup> = 0.12; <sup>R</sup>(Fig. S2K). We conclude that Phospho-seq exhibits best-in-class performance for technologies measuring protein and chromatin at singlecell resolution, and that the dynamic range of the assay matches <sup>fl</sup>ow cytometry-based methods that lack Phospho-seq’s multiplexing and multimodal capabilities.

## Intracellular protein staining highlights cell type differences in human retinal organoids

To explore the applicability of Phospho-seq to neural tissue, we utilized human iPSC-derived retinal organoid models (Fig. 2A), which have been shown to recapitulate retinal development, producing a heterogeneous cell population including photoreceptors, glia, and epithelium<sup>31</sup>. We conjugated a custom panel of 46 antibodies, the majority previously used in an iterative indirect immuno<sup>fl</sup>uorescence imaging (4i) study<sup>32</sup>, consisting of mature retinal cell type markers as well as developmentally relevant transcription factors and one phospho-signaling antibody, pRPS6 (Supplementary Data 1). Running Phospho-seq with this panel on 34-week-old retinal organoids while <sup>fi</sup>ltering for doublets with cell hashing<sup>27</sup> produced a dataset with 8136 cells.

Utilizing dimensionality reduction and unsupervised clustering, we identi<sup>fi</sup>ed 16 cell clusters (Fig. S3A). While we could assign broad cell type labels using gene activity scores calculated from chromatin accessibility within gene bodies and promoters<sup>33</sup> (Fig. 2B and S3B), more <sup>fi</sup>ne-grained annotation is challenging for chromatin accessibility measurements in the absence of transcriptomic data. We found that ADTs were heterogeneously detected across differently assigned cell types, identifying markers of progenitors and glia (SOX9, VIM), photoreceptors (RCVRN, DNM1), Rods (RHO), and retinal pigment epithelium and glia (RLBP1) (Fig. 2C, D and Fig. S3C, D). Elevated protein marker expression detection was further supported by enriched chromatin accessibility in the same cell types for both intranuclear and intracellular proteins (Fig. 2C, D, and Fig. S3C). Correlating individual TF ADT values with accessibility of all possible binding motifs, as determined by chromVAR<sup>28</sup>, we found that for 6 out of the 10 TFs pro<sup>fi</sup>led, the correct binding motif was in the 80th rank-correlation percentile or above (Fig. S3E, F). For these instances where ADT capture and canonical motif accessibility are highly rank-correlated for a TF, this is evidence of direct, functional regulation of chromatin accessibility by the target protein.

Focusing on phosphorylation, we observed a large, previously unreported difference in pRPS6 signal between rods and cones (Fig. 2E), which we validated through immuno<sup>fl</sup>uorescent imaging (Fig. 2F, G and Fig. S3G). Photoreceptors are among the most metabolically demanding cell types in the body, requiring high levels of mTOR signaling, which in turn phosphorylates RPS6, to properly function<sup>34</sup>. Among photoreceptors, cones require more energy than rods due to their more consistent depolarized state<sup>35</sup> and the relative levels of pRPS6 we observe between these two cell types re<sup>fl</sup>ect this. This observation demonstrates the utility of Phospho-seq to discover signaling differences between cell types.

## Extending Phospho-seq to incorporate transcriptomic measurements

Our Phospho-seq protocol utilizes the 10x scATAC-seq kit to generate scalable and high-quality chromatin accessibility pro<sup>fi</sup>les but lacks transcriptomic measurements, which are highly valuable for <sup>fi</sup>ne-grained cell annotation and gene regulatory network reconstruction. We therefore considered both experimental and computational strategies to incorporate transcriptomic pro<sup>fi</sup>les into the Phospho-seq assay.

To experimentally obtain transcriptome information in a Phospho-seq experiment, we employed the 10X scATAC + RNA multiome kit, in place of the scATAC kit, and applied the Phospho-seqmulti work<sup>fl</sup>ow to retinal organoid samples (Methods) (Fig. 3A). We successfully generated libraries for all modalities and recovered 1474 cells from an input of 5000 with a median of 866 RNA UMIs, 8326 ATAC fragments and 39 ADT UMIs per cell (Supplementary Data 5). Dimensionality reduction and clustering Phospho-seq-multi data using weighted-nearest neighbors<sup>25</sup> revealed 7 clusters, which we assigned identities based on their RNA expression (Fig. 3B and Fig. S4A). We veri<sup>fi</sup>ed the expected accessibility and expression patterns of both celltype speci<sup>fi</sup>c enhancers as well as protein markers from the ADT pro-<sup>fi</sup>les, including canonical ADTs like RCVRN (photoreceptors), VIM (Precursors) and RLBP1 (RPE and glia) (Fig. S4B), demonstrating the capability of Phospho-seq to simultaneously pair intracellular protein pro<sup>fi</sup>les alongside both transcriptomic and chromatin accessibility measurements.

A  
B  
![](images/e643b79b821c4f466ce202f6df874f253ba6d80fa458c1e1532c568a248a68d8.jpg)

![](images/da1bd770a5967b30fe8c10c83521789a8b6b6a47066913ff981386402a8f7920.jpg)

![](images/74a597908fec8d2d97e98f493be966eaed02be2a5ad9d6539cf36d8c95f79444.jpg)  
F

![](images/bcb7dd86ca0958380e0232a1d3dd55391f9919918e72077937a5cb5b3a3a219b.jpg)  
Fig. 2 | Phospho-seq on retinal organoids. A Schematic of retinal organoid differentiation. B UMAP representation of cells and cell type assignments based on the ATAC-seq modality in Phospho-seq. RPC retinal precursor cell, MG müller glia, PC precursor cell, PR-PC photoreceptor precursor, RPE retinal pigment epithelium. C Coverage and violin plots of the gene promoter and protein level respectively of nuclear protein SOX9. Color and order are the same as in (B). D Coverage and violin plots of the gene promoter and protein level respectively of cytoplasmic protein

While this dataset was informative and enabled cell type identi<sup>fi</sup>- cation from transcriptomic pro<sup>fi</sup>les, the simultaneous acquisition of multiple modalities came at a substantial cost in data quality and throughput when compared to either our existing Phospho-seq data, or scRNA-seq on retinal organoids<sup>32</sup>. Speci<sup>fi</sup>cally, we observed a 70% reduction in molecular sensitivity for scATAC-seq pro<sup>fi</sup>les and a 91% reduction for gene expression pro<sup>fi</sup>les (Fig. S4C, D). We further observed a signi<sup>fi</sup>cant reduction in the staining index for both intracellular and intranuclear ADT levels, with a range of 45–70% reduction between three pairs of cell types (Fig. 3C and Fig. S4E and Supplementary Data 2). Lower ADT sensitivities may be mitigated through the use of direct capture (i.e. TotalSeq-A) ADT oligos, as in NEAT-seq<sup>16</sup> rather than indirect capture oligos (TotalSeq-B) due to the differing chemistry between the scATAC kit and the multiome kit. Regardless, these data are consistent with previous studies<sup>20</sup> that exhibit lower permodality molecular sensitivity when using the 10x multiome kit, and demonstrate the inherent challenges for multimodal technologies to generate high-quality data from each measurement type.

We, therefore, explored an alternative approach aiming to integrate Phospho-seq and scRNA-seq reference datasets using our recently introduced ‘bridge integration’ procedure (Fig. 3D)<sup>23</sup>. We have previously shown that this work<sup>fl</sup>ow can successfully integrate distinct modalities collected in different experiments by leveraging a separately obtained multiomic dataset as a ‘bridge’, even if the bridge dataset has reduced technical quality. The bridge integration procedure can successfully integrate data for both discrete cell types as well as continuous developmental trajectories, but requires that the multiomic dataset is biologically representative (i.e. inclusive of all cell types and states) of the single-modality datasets. In our study, the previously published bridge and reference datasets were generated from the same set of samples<sup>32</sup> (Fig. S4F, G), thereby satisfying this assumption and demonstrating that integrating Phospho-seq datasets does not require the generation of additional multiomic data if such data already exists.

G  
C  
![](images/6e85147c43073b6d864721ca64329e66c33a9f49acf9cd6390e235b5e54f2341.jpg)

D  
![](images/d4130db50412da037340cf48e12eae5a2d1de008d5790bd7daf7f950047cbcfd.jpg)

![](images/0d33085dea4e4e99cea332859bcac000f581c5375a4776d57cf71efdab023513.jpg)

![](images/702a977d661941fdec6ddd739c2b1a3f46918995896b92557b18007a8b196545.jpg)

![](images/ae231fd02459f4e0eafba0ec25646c9fcedb236ee9b1df2257b6bcfea0b2b9a7.jpg)

![](images/29a7a60a6483ac0141686b940031f6daba0a16928e3a1546d0d1cb91cdd342e8.jpg)  
RCVRN. Color and order are the same as in (B). E Violin Plot of pRPS6 ADT quanti<sup>fi</sup>cation in Rods and Cones. F Confocal images of 33-week-old retinal organoids harvested and immunostained with antibodies against the cone marker ARR3 (green), Rod marker RHO (blue), and pRPS6 (red) with examples of high-pRPS6 cones indicated by arrowheads. Scale bars are 50 μm. This experiment was performed once. G Quanti<sup>fi</sup>cation of ARR3, RHO, and pRPS6 in 240 Rods and 64 Cones from (F).

Applying this work<sup>fl</sup>ow, we used bridge integration to annotate each Phospho-seq pro<sup>fi</sup>le based on published labels (Fig. 3E). We found that these transferred annotations were consistent with those originally derived from gene activity scores, but increased the interpretability of annotation. For example, Phospho-seq cells that were annotated as Immature PRs fell into four categories after bridge integration: BCs, AC/HC, Early PRs, and non-retinal cells (Fig. 3F). After we performed bridge integration, we retrospectively identi<sup>fi</sup>ed differences in the chromatin accessibility pro<sup>fi</sup>les across high-resolution subsets that supported our transferred annotations. For instance, there were previously unobserved accessibility differences at canonical markers between progenitors and differentiated cells for Bipolar and Amacrine/Horizontal Cells (Fig. S4H). Moreover, we obtained high prediction scores (70% >0.50) for all cell types with the exception of cells that were not suf<sup>fi</sup>ciently represented in the bridge data, like Photoreceptor Precursors (PR-PC) or non-retinal cells (Fig. S4G, I).

![](images/5ca9dfdabc348574db21ce48e8b032b18bfb30d8ab0f2a45cf8046013606cc1c.jpg)  
C

![](images/74c60ce952d2e4d689c53688f6c3c2de0f339da562f29adfe0fcee7be0a731d8.jpg)

D  
E  
![](images/30f7da625c1a4b17b6624d0e4bb0ed76c155360a4aa463132f9677682aab67f1.jpg)  
F  
Fig. 3 | Extending Phospho-seq with transcriptomic measurements. A Schematic of Phospho-seq using the 10x multiome kit. B Weight-nearest neighbors UMAP of Phospho-seq-Multi experiment labeled by cell type. AC/HC amacrine cells/horizontal cells. C Heatmap comparison of 11 ADTs between Phospho-seq experiments using either the Multiome kit or the ATAC-seq kit. D Schematic of

We therefore utilized our integrated dataset to impute transcriptome-wide expression pro<sup>fi</sup>les for each Phospho-seq cell. We con<sup>fi</sup>rmed that these imputed pro<sup>fi</sup>les maintained high rankcorrelation for TF motif accessibility, as well as measured ADT levels for the same gene (Fig. S4J–L). These results con<sup>fi</sup>rm the applicability of bridge integration to obtain a high-quality RNA modality with Phospho-seq. We conclude that, while it is possible to use the Phosphoseq work<sup>fl</sup>ow to perform experimental trimodal pro<sup>fi</sup>ling, this comes with a cost in data quality and thus integrated analysis may result in improved data quality for multiple modalities.

![](images/0f43fa5c7c731839a2b97a086163aaff85369591fa642d9f23781e6a4e4da7ab.jpg)  
bridge integration procedure. E UMAP representation of retinal organoid cells based on ATAC-seq modality with cell type assignments from bridge integration. BC bipolar cells. IN intermediate. F Alluvial plot demonstrating cell label transfer when using bridge integration.

## Intracellular protein staining highlights cell type differences in human brain organoids

Finally, we chose to apply Phospho-seq to uncover signaling patterns in early neurodevelopment. For this, we used human iPSC-derived brain organoid models, which have provided valuable insights into neurodevelopmental processes that are otherwise dif<sup>fi</sup>cult to study in humans<sup>36,37</sup>. We <sup>fi</sup>rst designed and conjugated a custom panel of 64 antibodies comprising both neurodevelopmentally relevant transcription factors, as well as an expanded set of 40 paired cell-signaling antibodies (Fig. 4A and Supplementary Data 1). While previous studies have pro<sup>fi</sup>led chromatin and transcriptomic modalities from these models<sup>37,38</sup>, we reasoned that our Phospho-seq panel could illuminate relationships between cell signaling pathways, transcription factors, and gene regulatory elements. We separately generated 3-month-old organoids from four iPS donors, using a well-established protocol for unguided brain organoid differentiation (Fig. 4B)<sup>37,39</sup>. We performed cell hashing for doublet detection<sup>27</sup> and used genetic pro<sup>fi</sup>ling<sup>40</sup> for donor demultiplexing, subsequently pro<sup>fi</sup>ling 9,028 cells using Phospho-seq (Fig. S5A).

![](images/03118912de97e90f970eefe9798efeffbd7df16d83f0dc2fca7387c79fdf18f4.jpg)

B  
C  
![](images/df356fc7a07feb0ca2ad625db8204689f8a4b43f1b67eef8eb35bfe7c9b9e3dd.jpg)

![](images/77fa86d7931a12aa08480e9369bfaaed44df738d5c850d00d632d242a9b1d1ea.jpg)

D  
![](images/8b71486493c5972e67914b8725c0e08fa1fdbb5ff732c12ec1eac4d45ae7577b.jpg)

![](images/02c6af4a25269b015579cc7b6407d31e3a1f30ea05a6dcb40d565e87ef63ee69.jpg)  
E

![](images/937c8e0bf4348f5ad452e3578658ae4348c9291a4fb2b46ea968f1bccdf2f42b.jpg)  
G

![](images/5449526637ed5503d6ae90984b1aa3d26d3ca857f10785fa4f43386e7a57b08b.jpg)

![](images/cbe6cb8acd7d9b3bd55d6af4a3c67f21bc7249f1484eedca055ff80811ad5b8d.jpg)

![](images/893e0a30a6748f3ec44ab06e83a306afcf80892ca844ac7c764650b9ce189246.jpg)

![](images/35b8c049fa46587d90c5778a42f92903b20d29d2ee87bb4b3c91fa298d8e9985.jpg)

I  
H  
![](images/b8696bd2168cb51814f3853f8ad115b6d29acb9dfb8033af1becad2fd01f746a.jpg)

![](images/9be7f6531ed8289c361e0afd1f8691467915990f0f73f0fa60fa837d5653e66e.jpg)

J  
K  
![](images/62a27d412f348f0f5ac8fc6b9d58e5c4c95a55685440b96d2206d62bd0ef2ff8.jpg)

![](images/162dbecefa1879c0c8728a1cf0525120846f740c04cd3f5e229bdcfe0e338ce2.jpg)  
Fig. 4 | Phospho-seq on brain organoids. A Schematic of antibody panel used in brain organoid Phospho-seq experiment and the cellular compartment of the target protein. B Schematic of brain organoid differentiation. C UMAP representation of cells and cell type assignments based on the ATAC-seq modality in brain organoid Phospho-seq. GE ganglionic eminence. D Coverage and violin plots of the gene promoters and protein levels respectively of nuclear protein OTX2 and cytoplasmic protein S100B, color and order are same as in (C). E Diffusion MAP plot of diencephalic and telencephalic differentiation trajectories. Cell-type colors correspond to legend in (C). F Heatmap of ADT expression of proteins and phospho-proteins  
associated with MAPK/ERK and mTOR signaling. G Schematic of MAPK/ERK signaling. H Coverage plot of RPS6KA1 split into quantiles of pRPS6 levels across telencephalic and diencephalic differentiation trajectories with OTX2 binding motifs indicated. I Coverage plot of RPS6KB1 split into quantiles of pRPS6 levels across telencephalic and diencephalic differentiation trajectories. J Rankcorrelation plot showing correlation between pRPS6 levels and motif accessibility across the whole Phospho-seq dataset. The top hits are indicated in red. K Rankcorrelation plot showing correlation between pMAPK levels and motif accessibility across the whole Phospho-seq dataset.

Utilizing dimensionality reduction and unsupervised clustering, we identi<sup>fi</sup>ed 10 clusters representing heterogeneity both in neurodevelopmental lineage and donor identity (Fig. S5B) assigning broad cell type labels using gene activity scores<sup>33</sup> (Fig. S5C). To perform bridge integration for this dataset, we generated a new scRNA-seq reference dataset with 19,280 cells and a multiomic bridge dataset with 4958 cells, all from the same samples (Fig. S5D, E). Using canonical gene expression markers, we manually annotated the reference dataset (Fig. S5F) and transferred these labels onto the Phospho-seq dataset (Fig. S5G). We obtained high prediction scores (95% >0.5) for all cell types with the exception of astrocytes, which are one of the most rare cell populations in this system and were not suf<sup>fi</sup>ciently represented in the bridge data (Fig. S5H).

We found ADTs that were heterogeneously detected across differently assigned cell types, identifying markers of forebrain progenitors (SOX2, GLI3), diencephalic cells (OTX2), progenitors and glia (VIM, S100B), and intermediate progenitors (TBR2), again <sup>fi</sup>nding that elevated protein marker expression was further supported by enriched chromatin accessibility patterns in the same cell types for both intranuclear and intracellular proteins (Fig. 4D and S6A). We observed that 45 out of 64 proteins exhibited differential expression between at least one pair of clusters (Fig. S6B) and that most ADTs had high rank-correlation with their corresponding imputed RNA values compared to all other imputed RNAs (50% >80th percentile rank-correlation) (Fig. S6C).

We leveraged our integrated dataset to explore the relationship between chromatin accessibility, gene transcription, and protein levels across forebrain development. To do this, we <sup>fi</sup>rst constructed a developmental trajectory across 1,578 cells spanning from progenitors to neurons (Fig. S7A)<sup>41,42</sup>. While  gene expression decreased at the <sup>SOX2</sup>initial stages of differentiation, we observed a developmental lag in the decrease of downstream modalities including SOX2 ADT levels and SOX2 transcription factor activity as estimated by chromVAR (Fig. S7B). We identi<sup>fi</sup>ed a speci<sup>fi</sup>c stage of the developmental trajectory where protein and RNA levels were discordant and con<sup>fi</sup>rmed that in these cells, only SOX2 protein levels (and not RNA levels) were correlated with chromVAR scores (Fig. S7C). SOX2 is a well-established negative regulator of neuronal development<sup>43</sup>, and this analysis enabled us to identify genes whose downregulation preceded SOX2 protein downregulation, and are therefore unlikely to be direct or downstream targets of SOX2 itself, and vice-versa (Fig. S7D–F). We conclude that integrated Phospho-seq data can perform multimodal characterization of the distinct temporal patterns and gene regulatory relationships that drive cellular dynamics.

## Observing signaling network activity with Phospho-seq

One goal in developing Phospho-seq was to better characterize differences in signaling pathway activation across cell states and to connect these changes to gene regulatory networks. In this dataset, we observed an increase in phosphorylation of members of the MAPK/ ERK pathway in the diencephalic lineage compared to the telencephalic lineage (Fig. 4E, F, Fig. S8A), which we validated through immunocytochemistry in organoids of the same donor and age (Fig. S8B–E). Of particular interest, we found that pRPS6 was heterogeneously expressed across cell types. While pRPS6 is often utilized as an indicator for mTOR pathway activity, RPS6 can actually be phosphorylated by multiple kinases from different pathways—including the ERK pathway via RPS6KA1 or the mTOR pathway via RPS6KB1<sup>44</sup> (Fig. 4G). We found that our Phospho-seq data could help us better understand determinants of RPS6 phosphorylation. We observed that chromatin accessibility at the  gene correlated with pRPS6 <sup>RPS6KA1</sup>levels while accessibility at was not correlated with pRPS6 <sup>RPS6KB1</sup>levels (Fig. 4H, I). While the kinase activity of these proteins is determined by upstream phosphorylation, the variability of pRPS6 levels appears to be in part driven by variation at the locus, indi-<sup>RPS6KA1</sup>cating a more prominent role for ERK signaling over mTOR signaling in driving variable phosphorylation of pRPS6 in the diencephalic lineage.

As pRPS6 does not directly bind DNA, instead working to regulate gene expression through translation<sup>45</sup>, we aimed to determine which TFs worked in concert with pRPS6 to achieve this regulation. When applying our ADT/motif rank correlation analysis, we identi<sup>fi</sup>ed a clear association between pRPS6 levels with multiple TEA/ATTS domain (TEAD) motifs in both brain organoids (Fig. 4J) and retina (Fig. S8F). TEAD transcription factors are the effectors of YAP-TAZ/Hippo signaling pathway, which is known to work together with MAPK/ERK signaling to regulate cell size<sup>46</sup> in cancer cells. Similarly, we found that pERK and pMAPK ADT levels were associated with the accessibility of NR2F1 and NR2F2 motifs (Fig. 4K), representing an important neurodevelopmental regulator whose RNA expression was also elevated in cells with higher activation of MAPK/ERK signaling<sup>47,48</sup> (Fig. S8G).

We further applied Phospho-seq to discover underlying signaling differences between related but distinct cell types. Heterogeneity between glial cells during development is indicative of future identity and function<sup>49</sup>. In this dataset we observed multiple glial subtypes (Fig. S9A) expressing canonical glial marker genes including Oligodendrocyte PCs ( +), Glial PCs ( +), and two subtypes of +/ + astrocytes de<sup>fi</sup>ned by + or +(Fig. S9B). While <sup>AQP4 GFAP S100B GLI3</sup>some signaling markers (pRPS6, pSTAT3) were unchanged across populations, pPLCy $( p < 0 . 0 1 )$ and pAMPKa $( p < 0 . 0 5 )$ were elevated in <sup>p p</sup>S100B+ glia and depleted in SLC1A3+ glia (compared to S100B+ glia) respectively (Fig. S9C). These signaling pathways have been previously shown to re<sup>fl</sup>ect functional characteristics of cells, including energy usage $( \mathsf { p A M P K a } ) ^ { 5 0 }$ and calcium signaling $( \mathsf { p P l C y } ) ^ { 5 1 }$ . As these functional characteristics are known to vary across both cell types and brain regions, we reference-mapped these cells with an scRNA-seq atlas of <sup>fi</sup>rst-trimester developing human brains<sup>52</sup>, <sup>fi</sup>nding four groups of glial cells with high mapping scores that expressed similar markers (Fig. S9D). Interestingly, we found that subcategories of glial cells we identi<sup>fi</sup>ed matched to different regions in the developing brain: + <sup>GLI3</sup>glia and glial PCs were derived from the forebrain and telencephalon, and that + glia were from an equal distribution of non-<sup>S100B</sup>telencephalic origin (Fig. S9E). Future in-vivo experiments will reveal whether these signaling differences replicate in vivo, and how they in<sup>fl</sup>uence cellular decision-making and fate.

## Identi<sup>fi</sup>cation of transcriptional co-factors through ADT-motif correlation

We observed a rank-correlation of the 80th percentile or higher in 7 out of 16 TFs pro<sup>fi</sup>led (Fig. S10A). Looking closer, the OTX2 motif itself was the second-highest hit for OTX2 (Fig. S10B), with the other top hits having the same core motif. We observed similar results for SOX2 (Fig. S10C) and concluded that Phospho-seq data can help to identify and discover bona <sup>fi</sup>de links between cellular protein levels and DNA sequences that in<sup>fl</sup>uence gene expression. SOX2 and OTX2 are known to exhibit pioneer factor activity, where their binding alone can open heterochromatin<sup>53,54</sup>.

As not all TF have the ability to act as pioneers and independently regulate chromatin state, we were also interested to further exploring cases where we did not observe strong correlations between intracellular protein levels and canonical motif accessibility. In these cases, we expect that TFs may work alongside additional co-factors, which we could learn from Phospho-seq data. For example, we observe that GLI3 protein levels showed only a weak correlation with the accessibility of the canonical GLI3 binding motif, but instead were associated with motifs from the homeodomain-2 (HD/2) family<sup>55</sup>, which are known to affect neurodevelopment<sup>56</sup> (Fig. 5A). While this could in principle re<sup>fl</sup>ect non-speci<sup>fi</sup>c antibody binding, we found that GLI3 protein exhibited high correlation with RNA levels (Fig. 5B; <sup>2</sup> = 0.86), <sup>GLI3 R</sup>demonstrating that our GLI3 protein measurements are associated with the correct target.

We therefore hypothesized that other co-factors, such as those in the HD/2 family, may partner with GLI3 to regulate chromatin accessibility. Under this model, we propose that GLI3 does not individually act as a pioneer factor, but instead jointly regulates a subset of ATACseq peaks enriched for HD/2 family motifs. To test this model, we considered two additional data sources from the same neuronal organoid model as our Phospho-seq dataset<sup>37</sup>: a bulk GLI3 CUT&Tag dataset measuring genome-wide binding pro<sup>fi</sup>les, and a paired scRNAseq + scATAC-seq dataset (10x multiome) that included both WT and KO cells. While CUT&Tag data revealed 331,131 GLI3 binding sites <sup>GLI3</sup>across the genome, only a small percentage (5108, 1.5%) of these were associated with differential accessibility (DA) upon  perturbation. <sup>GLI3</sup>These DA regions were clearly enriched (fold-enrichment: 2.11) for GLI3 motifs over the background but even more strongly for HD/2 motifs (median fold-enrichment across HD/2 motifs: 3.02)(Fig. 5C), consistent with our Phospho-seq data. In addition, in the absence of chromatin changes, genes located adjacent to GLI3 binding sites showed no enrichment for differential expression after GLI3 perturbation, in contrast to the expression changes observed in DAR-adjacent genes (median average log2 fold-change: 0.04 vs −0.22; < 0.001) (Fig. 5D–F; <sup>p</sup>Supplementary Data 3). These <sup>fi</sup>ndings suggest that GLI3-binding alone is insuf<sup>fi</sup>cient to regulate chromatin accessibility and gene expression, and therefore, that CUT&Tag data is a poor predictor of which genomic regions will respond to  perturbation.

![](images/9344b136402dbbb799091d26664138b9e352d15f96e351f0f7c310797e14d6cd.jpg)

A  
B  
![](images/3c00f15d8b9820c770d4975754a53e6298954cb7909e902dde6e935f6860cd5c.jpg)

![](images/53b908d201dad7ed97d69931be96d4cc8ce9794faf8d98d2f45d403e0745e086.jpg)  
E  
D  
Fig. 5 | Identi<sup>fi</sup>cation of GLI3 transcriptional co-factors. A GLI3 protein levels correlate with the accessibility of HD/2 motifs (blue), but not the canonical GLI3 motif (red). Shown is a rank-correlation plot of all ADT/motif correlations. B GLI3 protein levels correlate with GLI3 RNA levels. Rank-correlation plot shows GLI3 ADT correlation with all genes. C Upon GLI3 perturbation, differentially accessible regions (DAR) are enriched for HD/2 motifs. Shown is the Rank-Fold Enrichment plot of motifs enriched in differentially accessible GLI3-bound regions in GLI3 knockout vs WT (left) and motifs enriched in non-differentially accessible regions (right). D Upon GLI3 perturbation, only genes linked to DAR are enriched for expression changes, which are predominantly negative as expected. Shown is a density plot of the fold change of genes linked to DAR and non-DAR. \*\* =

<sup>GLI3</sup>Strikingly, we found that our Phospho-seq data for GLI3 could help predict which genomic regions would respond to perturbation. Examining the 5108 DARs identi<sup>fi</sup>ed in the perturbation experiment, we found that the accessibility of these sites was correlated to GLI3 protein levels in our Phospho-seq data, in contrast to >300,000 non-DAR ( -value = <0.001)(Fig. 5G). Together these results demonstrate <sup>p</sup>that GLI3 does not act as a pioneer factor, but instead works with cofactors to regulate chromatin accessibility and gene expression as predicted by Phospho-seq. We conclude that Phospho-seq enables the identi<sup>fi</sup>cation of putative co-factors and the discrimination of functionally regulated regions and genes.

C  
![](images/9eff57e031f4717a342eb347f2c568d834e34f3e127fb56ceb3836c3940f9f53.jpg)

G  
![](images/1b01983037b454018585bf04d5b2247a1b6b6c334156957ab727f87cb2fab359.jpg)

![](images/17de50055749281ab1a36bebc9e6589b0d0bc7c7928c41a3327f89cd37077653.jpg)  
$\pmb { p = 3 . 8 9 \times 1 0 ^ { - 2 3 } }$ using a two-sided t-test. Phospho-seq data in WT cells predicts which regions will respond to functional perturbation. E, F show two exemplary loci, both bound by GLI3 in CUT&Tag data. The region in (E) contains HD/2 and GLI3 motifs. In the GLI3 KO data, the region is differentially accessible (middle), and in the Phospho-seq data, the accessibility is correlated with GLI3 protein expression. The region in (F) is also bound by GLI3 but contains no HD/2 motifs, is not associated with GLI3 ADT levels in Phospho-seq, and is not DAR upon GLI3 perturbation. Density plot in (G) shows that this pattern holds genome-wide: the correlation between peak accessibility and GLI3 ADT levels in Phospho-seq data discriminates responsive (DAR) and non-responsive (nonDAR) peaks in GLI3 KO cells \*\* = $p { = } 2 . 2 \times 1 0 ^ { - 1 6 }$ using a two-sided t-test.

## Using Phospho-seq data to identify gene regulatory networks in early neurodevelopment

By exploring relationships across modalities, multiomic datasets can help to reconstruct gene regulatory networks. While multiple groups have demonstrated how to leverage co-variation between chromatin accessibility and gene expression to link scATAC-seq peaks to the genes they regulate<sup>14,49,57</sup>, our Phospho-seq data also allows us to link these peaks to transcription factors (TF) that regulate their accessibility. Recently, Argelaguet $\mathrm { e t } \ \mathbf { a l . } ^ { 5 8 }$ proposed in-silico ChIP-seq, a computational approach to predict TF binding events from multiomic data, based on co-variation between the gene expression of a transcriptional regulator and an scATAC-seq peak. We reasoned that we could extend this analysis using protein measurements from our Phospho-seq panel, which may be more re<sup>fl</sup>ective of TF levels, rather than RNA measurements.

A  
![](images/75bfe91d0f50caba9e6fe98a89da9371114379eb8ff611ffe63bc7ec760cbadc.jpg)  
B

![](images/34e6fbc9b4295c601cb879099a0d721d98dfae27ff31bb15c511bc6bac23bba6.jpg)

![](images/69007f0439eedd1d8ca35e266216e20ac12d2b3d5c8c983f7bccaa8604a0a604.jpg)

C  
![](images/9ee0072600b897b2d238c092a2e1b30e6647db109b64d32ea3542c867144ad0a.jpg)

D  
![](images/44ce59b3c5a3e5f12f1cc1a3bd2472170b04787ea7baabca7d69336b3838d910.jpg)

E  
![](images/9bed664e50d18a9e6ed91293df82cca3652839c32b9faaf9559d18075ddce050.jpg)

F  
![](images/bddacf05d6a2ca3b6b09d605bb980a1b39e560b93e2551ae477393192e30fcd6.jpg)

G  
![](images/86771c7f15e67c70521279acefc06ad2c96ade30575329aaa363134d1e1a3017.jpg)

H  
![](images/307a37106f7261e7acb9ebf70d99c318e3f2ec4b167f112247d898a711403638.jpg)

I  
![](images/3a804fe2b691d5adc32a4e2ea549cce2c866e908a843fa6e07e1e7cb54d8a40d.jpg)  
Forebrain PCs IPCs Diencephalic PCs  
Non-Forebrain Glia Choroid PCs Glial PCs Astrocytes

For each TF, we identi<sup>fi</sup>ed peaks harboring the binding motif and whose accessibility was highly correlated with TF protein abundance (Fig. 6A) using a high-resolution pseudo-bulking approach (SEAcells) to reduce the sparsity of scATAC-seq data<sup>59</sup> (Fig. S11A). Furthermore, we identi<sup>fi</sup>ed the subset of these peaks whose accessibility was correlated (or anti-correlated) with proximal gene expression. This procedure enabled identi<sup>fi</sup>cation of downstream activating and repressive targets for individual TFs, as well as speci<sup>fi</sup>c enhancer elements that are likely to mediate these relationships.

We applied this procedure across multiple neurodevelopmentally relevant TFs - OTX2, SOX2, NFIB, GLI3 and TBR2. Focusing on OTX2, we identi<sup>fi</sup>ed 5,033 linked peaks. When performing footprinting analysis, which aggregates accessibility pro<sup>fi</sup>les across the collection of linked peaks, we observed a depletion of accessibility centered at the exact TF

Fig. 6 | Gene regulation inference with Phospho-seq. A Schematic approach to use metacelling to discover cis-regulatory elements associated with individual proteins. B Tn5 cut-site footprinting between cells with high OTX2 expression and low OTX2 expression in peaks that are highly correlated with OTX2 (left panel) and uncorrelated with OTX2 (right panel). C Example of an inferred transcription activating peak associated with indicated proximal gene expression for OTX2. Coverage plots and violin plots are ordered by quantile ADT expression. Red lines indicated the location of an OTX2 binding motif. D Example of an inferred transcription repressing peak associated with indicated proximal gene expression for OTX2. Coverage plots and violin plots are ordered by quantile ADT expression. Red

binding site, which is indicative of TF binding (Fig. 6B and Fig. S11B, C). This footprint was speci<sup>fi</sup>c only to cells expressing the TF, and to correlated peaks. For SOX2, further validation of predicted sites was performed using a ChIP-seq dataset<sup>60</sup> (Fig. S11D, E). We conclude that Phospho-seq enables the identi<sup>fi</sup>cation of bona <sup>fi</sup>de transcription factor binding sites by leveraging correlations across multiple modalities at single-cell resolution.

Linking the candidate peaks to genes, we identi<sup>fi</sup>ed 3200 candidate targets (1772 activating, 1428 repressive) for OTX2 (Fig. 6C, D; Supplementary Data 4). Interestingly, we observed numerous cases where individual genes were regulated by multiple CREs, which were associated with different TFs. This included cases where putatively activating and repressive peaks were adjacently located, as is the case with OTX2 and SOX2 at the  locus (Fig. S12A–C). When con-<sup>OTX2-AS1</sup>sidering the additional TFs (Fig. S12D–G) and quantifying the overlap between activated and repressed gene lists, we identi<sup>fi</sup>ed some pairs of TFs, including SOX2 and GLI3, that regulate numerous overlapping genes in the same direction (activation or repression) and others, like OTX2 and SOX2, that act in opposing directions. (Fig. S12H).

We found that Gene Ontology (GO) enrichments for predicted target genes were consistent with each TF’s known functional properties, including an enrichment for axon guidance amongst targets of TBR2 (a positive regulator of neuronal differentiation<sup>61</sup>), and an enrichment among SOX2 (a radial glial cell regulator<sup>62</sup>) targets for glial cell differentiation genes (Supplementary Data 6). For multiple TFs, we also observed an enrichment for genes associated with Wnt signaling, which is essential for brain patterning along the anterior-posterior axis. The pathway is known to increase activity in the posterior portion of the neural tube<sup>63,64</sup>, supporting our observation of increased Wntrelated gene expression and increased chromVAR activities of Wntresponsive TFs in diencephalic cells compared to forebrain (Fig. S13A). Furthermore, we observed a concordance in Wnt signaling with the activity of the Hippo pathway, which we associated earlier with MAPK/ ERK signaling, providing further evidence, in concert with what has been shown<sup>65</sup>, of the interconnectivity of signaling pathways in determining cell fate choice during early neurodevelopment (Fig. S13B). We conclude that our integrated Phospho-seq dataset can effectively identify relationships across modalities and reconstruct gene regulatory relationships.

## Linking phosphorylated proteins to gene regulatory elements with Phospho-seq

Using the pipeline above, we linked our previously observed pRPS6:TEAD1 relationship with speci<sup>fi</sup>c cis-regulatory regions. We identi<sup>fi</sup>ed 481 putative TEAD-regulated CREs (Fig. 6E and Supplementary Data 4). GO analysis of activating gene links revealed enrichment for genes associated with cell division, growth, and morphogenesis, as would be expected for targets of both MAPK/ERK and Hippo (Fig. S14A and Supplementary Data 6). This suggests a model where activation of the Hippo pathway in neural cells leads to simultaneous phosphorylation of RPS6 through the interconnecting signaling pathways. If this model is true, there should be observable TEAD binding at the identi<sup>fi</sup>ed pRPS6:TEAD1 CREs. As our computational inference relies on Phospho-seq’s predicted association between pRPS6-associated CREs lines indicated the location of an OTX2 binding motif. E Coverage and violin plots of GAS7 split by quantiles of pRPS6 levels across the whole dataset with TEAD1 motifs indicated by red lines. F Density plot showing ChIP-Seq depth at all peaks with a TEAD1 motif compared to pRPS6:TEAD1 peaks identi<sup>fi</sup>ed in this study. The signi<sup>fi</sup>cance of $\pmb { p = 1 . 9 \times 1 0 ^ { - 1 5 } }$ is determined by a Wilcoxon rank-sum test (two-sided). G Violin plot of normalized pSTAT3 ADT levels in a subset of progenitor and glial cells. H Violin Plot of STAT3 motif chromVAR scores in a subset of progenitor and glial cells. I Violin plot of STAT3 activated gene module scores in a subset of progenitor and glial cells.

and binding of TEAD TFs, we had to validate this <sup>fi</sup>nding using ChIP-seq data quantifying TEAD1 binding<sup>66,67</sup>. We found that many of these pRPS6:TEAD1 peaks are observed to be bound by TEAD1 in cells of neural origin (Fig. S14B), with signi<sup>fi</sup>cantly more signal in this set of peaks compared to all genome-wide peaks with a TEAD1 motif (Fig. 6F). These results extend previously identi<sup>fi</sup>ed links between signaling pathways and TFs, originally identi<sup>fi</sup>ed in cancer cells, to cell state speci<sup>fi</sup>cation in neurodevelopment<sup>68</sup>.

Finally, Phospho-seq can be used to measure phosphorylation among nuclear proteins, including transcription factors. Increased phosphorylation of the TF STAT3, which enhances its DNA-binding activity, is a characteristic feature of astrogliogenesis<sup>69</sup>. In our dataset, we con<sup>fi</sup>rmed a high-rank correlation of pSTAT3 with STAT3 motif accessibility, performing better than just STAT3 protein or RNA alone (Fig. S14C–E). We also saw an increase in pSTAT3 levels and STAT3 motif accessibility amongst glial cells in our dataset compared to progenitors or non-glial cells (Fig. 6G, H), con<sup>fi</sup>rming previous biological observations<sup>70</sup>. We then found 582 peak-gene links of CREs that harbored a STAT3 motif and whose proximal gene expression correlated with pSTAT3 levels. The expression of this gene set was speci<sup>fi</sup>- cally enriched in glial cells (Fig. 6I), and included canonical astrocyte markers such as  (Supplementary Data 4). We conclude that by <sup>AQP4</sup>exploring relationships across multiple molecular modalities, Phospho-seq can highlight the role of cell signaling pathways in neurodevelopmental fate speci<sup>fi</sup>cation.

## Discussion

Here we present Phospho-seq, a scalable approach to detect intracellular and intranuclear proteins, including phospho-speci<sup>fi</sup>c states, alongside additional molecular modalities. We con<sup>fi</sup>rmed the sensitivity and speci<sup>fi</sup>city of our approach in cell lines, and subsequently applied Phospho-seq to pro<sup>fi</sup>le both retinal and brain organoids. We added transcriptomic information to these data using bridge integration, allowing us to maximize the data quality obtained from each modality. With this integrated dataset we linked protein expression levels to the accessibility of -regulatory elements and the expression <sup>cis</sup>of proximal genes. We demonstrate how these connections can assist in reconstructing gene regulatory relationships and provide insight to the causes and consequences of heterogeneous signaling during neurodevelopment.

We demonstrate that Phospho-seq is compatible with custom panels of user-conjugated antibodies, which can be easily and costeffectively generated. While oligonucleotide-conjugated panels against cell surface proteins are readily available in both individual and pooled formats, these reagents are not widely available for intracellular targets, which has prevented the applicability of single-cell protein pro<sup>fi</sup>ling to neuroscienti<sup>fi</sup>c applications. Moreover, Phospho-seq enables the user to perform a multiplexed evaluation of the sensitivity and speci<sup>fi</sup>city for large panels of phospho-speci<sup>fi</sup>c antibodies, by identifying correlations between ADT levels and chromatin and transcription states. We therefore expect that sequencing-based intracellular protein technologies will enable the identi<sup>fi</sup>cation and optimization of large intracellular panels, and that combining information across studies and biological systems will increase the generalizability of these results.

While pioneering technologies enable trimodal measurements of RNA, ATAC and surface protein or intranuclear abundance<sup>16,18,20</sup>, in this study, we utilized bridge integration<sup>23</sup> to harmonize molecular modalities collected in separate scRNA-seq and Phospho-seq datasets. Although this approach requires running additional experiments, we and others have found that simultaneous pro<sup>fi</sup>ling of ATAC and RNA in cells or nuclei reduces the data quality associated with each modality<sup>49</sup>. Improved <sup>fi</sup>xation-compatible scATAC and scRNA methods may be helpful for addressing this issue in the future, but we note that a bridge-based experimental design may represent a <sup>fl</sup>exible alternative for multimodal analysis where only a subset of samples need to be pro<sup>fi</sup>led with multiomic technologies. Importantly, we have previously shown that even small (<5000 cells) 10x Multiome datasets can serve as effective bridges for large unimodal datasets, as long as they are biologically representative<sup>23</sup>. Moreover, users of Phospho-seq may bene<sup>fi</sup>t from increasingly available reference atlases of either scRNAseq or Multiome data<sup>71,72</sup>, which would reduce the need for additional experimentation.

We anticipate that future studies will extend Phospho-seq to capture additional modalities related to chromatin state, and may shed additional light towards our understanding of how transcription factors regulate cellular chromatin. For example, combining Phospho-seq with scCUT&Tag<sup>73</sup> or NTT-seq<sup>74</sup> would identify TFs whose abundance correlated not only with chromatin accessibility, but with the presence of either activating or repressive chromatin marks. Further extensions that enable guide RNA capture (i.e. Perturb-ATAC<sup>75</sup>, Spear-ATAC<sup>76</sup>) would enable multiplexed genetic screens to utilize Phospho-seq to perform massively parallel identi<sup>fi</sup>cation and characterization of signaling regulators. Finally, applying Phospho-seq in concert with spatially-resolved pro<sup>fi</sup>ling technologies<sup>77</sup> may shed light on both intercellular and intracellular signaling networks. We hope that the broad applicability of Phospho-seq will facilitate its adoption in diverse biological contexts, including development, immunology, neuroscience, and cancer, to discover how cell signaling determines cellular behavior and fate.

## Methods

## Antibody selection

To select antibodies for use in the Phospho-seq assay, we used a hierarchical selection criteria based on available manufacturer’s information. Antibodies were likely to be good candidates if they were <sup>fi</sup>rst reported to work in intracellular <sup>fl</sup>ow cytometry and barring that, in immunocytochemistry on <sup>fi</sup>xed cells. Antibodies that are reported to only work in western blot are less likely to work in Phospho-seq. Finally, the antibodies must be available in quantities of >5 μg in order to account for antibody loss in conjugation ef<sup>fi</sup>ciency con<sup>fi</sup>rmation and post-conjugation processing. Antibodies from a variety of commercial vendors were used in this study including Abcam, Novus, R&D, ThermoFisher, Thomas Scienti<sup>fi</sup>c, and BioLegend. A full list of antibodies and catalog numbers is available in Supplementary Data 1.

## Antibody puri<sup>fi</sup>cation

We used two methods of purifying antibodies from solutions with carrier proteins. For antibodies with BSA as a carrier protein, we used a BSA removal kit (Abcam: ab173231) following manufacturers instructions. For solutions that had more than just BSA contaminants (i.e. Ascites, gelatin), we used Magne Protein G beads (Promega: G7471). We followed manufacturer’s instructions, eluting twice into a 100 mM Glycine-HCl solution (pH 2.7) and neutralizing with 2 M Trisbuffer (pH 7.5).

## Antibody conjugation and pooling

For antibody conjugation steps prior to puri<sup>fi</sup>cation, we followed the protocol described here with minor alterations (https://citeseq.<sup>fi</sup>les. wordpress.com/2019/03/cite-seq\_hyper\_conjugation\_190321.pdf), which leverages a cost-ef<sup>fi</sup>cient and <sup>fl</sup>exible conjugation strategy originally developed for immuno-PCR<sup>24</sup>. Brie<sup>fl</sup>y, TotalSeq-style oligos were ordered from IDT with sequences of /5AmMC12/CCTTGGCACCCGAGAATTCCA XXXXXXXXXXXXXXXBAAAAAAAAAAAAAAAAAAAAAAAAAAAA\*A\*A for hashing, and /5AmMC12/GTGACTGGAGTTCAGACGTGTGCTCTTCCGAT CTNNNNNNNNNNXXXXXXXXXXXXXXXNNNNNNNNNGCTTTAAGGCC GGTCCTAGC\*A\*A for antibody tags where X’s represent the antibody barcode and N’s represent UMI tags. We attached a TCO-PEG4 linker to each oligo through incubation with TCO-PEG4-NHS reagent (Click Chemistry Tools: A137-25) and then column puri<sup>fi</sup>ed them with Micro Bio-Spin 6 Columns (Bio-Rad: 732–6221), con<sup>fi</sup>rming labeling through observation of a size shift compared to unlabeled oligos on a 4% agarose gel. The concentration of each oligo was quanti<sup>fi</sup>ed and diluted to 100 μM. As ordered, \~50 nmoles of oligo can be used for labeling \~3 mg of antibodies, thus requiring the labeling process to only be performed once per oligo-tag sequence for hundreds of experiments.

Next, 5 μg or more of puri<sup>fi</sup>ed antibody was labeled with mTz-PEG4 (Click Chemistry Tools: 1069-10) for 30 min and conjugated to the TCO-PEG4 labeled oligo at a target concentration of 15 pmol per 1 μg of antibody overnight. This leaves each antibody conjugated to 2–4 copies of each oligo on average. Each conjugation was con<sup>fi</sup>rmed through running 1 μg of conjugated antibody on a 4–12% protein gel (Thermo: XP04125BOX) and observing a laddered size shift in increments of 30 kDa above the unconjugated IgG size of 155 kDa. The <sup>fi</sup>nal concentration of each conjugated antibody was estimated through a BCA assay (Thermo: 23227).

Finally, for each experiment, 3–5 μg of each antibody was pooled together and treated with 40% saturated (\~4.32 M) Ammonium Sulfate to salt out the conjugated antibodies from the unconjugated oligos still present in the antibody solution. After the majority of the remaining oligos were removed, the pooled solution was passed through a 50 kDa MWCO <sup>fi</sup>lter (EMD Millipore: UFC505024) 5–7 times —checking the <sup>fl</sup>owthrough solution for ssDNA (leftover oligos) concentration after each centrifugation. When the <sup>fl</sup>owthrough solution is at or below 0.2 ng/ul, the leftover antibody is resuspended from the <sup>fi</sup>lter and checked on a 4% agarose gel for two bands, one lower oligo band (90 nt) and one higher antibody band (\~400 nt), with the aim of having the oligo band as faint as possible. The <sup>fi</sup>nal antibody pool was then quanti<sup>fi</sup>ed through a BCA assay as there is an expected material loss (quanti<sup>fi</sup>ed up to 60% loss) of antibody bulk in this step due to the use of MWCO <sup>fi</sup>lters.

## Cell culture

K562 cells were maintained in IMDM media (ThermoFisher: 31980030) supplemented with 10% FBS (Corning:35-010-CV), 1 mM Pen-Strep (Sigma: P0781-50ML), and 1X Non-essential amino acids (Sigma:M7145- 100ML). In experiments with stimulation and inhibition, 4 h before harvesting, K562 cells were removed from maintenance media, centrifuged for 5 min at 300 × , and resuspended in IMDM media with no supple-<sup>g</sup>ments. Cells were counted and 1 × 10<sup>6</sup> cells were transferred into two separate <sup>fl</sup>asks. In one <sup>fl</sup>ask, cells were immediately treated with 500 nM PX-866 (Cayman Chemical: 13645) while in the other <sup>fl</sup>ask, 50 ng/ml EGF (R&D Systems: 236-EG-200) was added 15 min before harvest.

HEK cells were maintained in DMEM media (Caisson Labs: DML10) supplemented with 10% FBS, 1 mM Pen-Strep, and 1X Non-essential amino acids.

Three lines of iPSCs were obtained from the New York Stem Cell Foundation (51050,50828,50975). Cells were thawed into feeder-free conditions with mTESR1 (STEMCELL: 85850) and 10% CloneR (STEM-CELL: 05888) with a Geltrex substrate (Fisher: A1413301). After two days, cells were changed into maintenance media – mTESR1 supplemented with 1 mM Pen–Strep. Throughout culture, media was changed daily and cell colonies were passaged by treatment with 1:3 Accutase (STEMCELL: 07920) diluted with PBS (Caisson Labs:PBL06-500ML) for 5 min. Cell lines were passaged a maximum of <sup>fi</sup>ve times before an experiment in order to reduce the number of cell-culture related chromosomal abnormalities.

## FACS

iPS cells were harvested through dissociation with accutase for 5 min and centrifuged in growth media at 300 × g for 5 min. K562 cells in suspension were harvested through centrifugation in growth media. Both cell lines were resuspended in 1 ml $\mathsf { P B S } + 0 . 0 4 \%$ BSA (Fisher: BP9706-100) and run through a 40 μm <sup>fi</sup>lter to obtain a single cell suspension. These suspensions were further centrifuged for 5 min at $3 0 0 \times g$ in a tabletop swinging bucket centrifuge. Cells were resus-<sup>g</sup>pended in $4 5 0 \mu \mathrm { l }$ of PBS and were <sup>fi</sup>xed by adding 30 μl of 16% formaldehyde (Sigma: F8775-25ML) (<sup>fi</sup>nal concentration, 1% FA in PBS). Cell suspensions were left to <sup>fi</sup>x for 10 min at RT, with inversion every 3 min. The <sup>fi</sup>xation reaction was quenched by adding 68.5 μl 1 M glycine and <sup>fi</sup>lling the tubes with ice-cold PBS. The suspensions were centrifuged for 5 min at 400 ×  at $4 ^ { \circ } \mathrm { C } ,$ after which the supernatant <sup>g</sup>was removed. The cells were resuspended in 1 ml PBS was added and the centrifugation was repeated. After the second centrifugation, the cells were resuspended in 100 μl of lysis buffer (10 mM Tris-HCl, 10 mM NaCl, 3.33 mM MgCl<sub>2</sub>, 0.1% ${ \mathsf { N P - 4 0 } }$ (Thermo: 28324), 1% BSA in H O) and incubated on ice for 5 min for permeabilization. After 5 min, wash buffer #1 (10 mM Tris-HCl, 10 mM NaCl, 3.33 mM $\mathsf { M g C l } _ { 2 } ,$ 1% BSA in ${ \sf H } _ { 2 } \mathbf { O } )$ was added up to 1 ml and cells were centrifuged for 5 min at $5 0 0 \times g$ after which the supernatant was discarded and the cells were resuspended in staining buffer (3% BSA in PBS) for blocking and placed in a tube rotator at RT for 30 min.

For cells that received a primary antibody bound by EcoRI singlestranded DNA binding protein (SSB) (Promega: M3011), the SSB binding reaction happened during the blocking step. Brie<sup>fl</sup>y, 1 μg of antibody was incubated with 8 μg of SSB in a solution of 1x NEB buffer 4 (NEB:B7004S) for 30 min at $3 7 ^ { \circ } \mathrm { C }$ . After this incubation, BSA and PBS were added to make a <sup>fi</sup>nal solution of 3% BSA in 1X PBS.

For staining, the blocking buffer was removed through centrifugation at $6 0 0 \times g$ for 5 min and washing in wash buffer #2 (3% BSA in $\mathrm { P B S } + 0 . 1 \%$ <sup>g</sup>Tween) three times. Cells were then resuspended in 100 μl of staining buffer with the appropriate antibodies and placed on the tube rotator for 1 h at RT. After this 1 h, the cells were washed three times in wash buffer #2 and then resuspended in staining buffer with a compatible secondary antibody (BioLegend: 406605, 407507, 406707, 408205) and stained for 30 min in the dark. Following three more washes, the cells were resuspended in MACS buffer (2 mM EDTA and 0.5% BSA in PBS) and run through the <sup>fl</sup>ow cytometry protocol on a Sony MH800 cell sorter with secondary only stained K562 cells acting as the negative control and a goal of 20,000 cells per condition. Flow cytometry analysis and plotting were performed using FlowJo v9.3.2.

For <sup>fl</sup>ow cytometry experiments with HEK and K562 cells, equal numbers of each of the cell types were processed in the same way as above.

For comparative experiments with ASAP-Seq and Phospho-seq, the cells were processed and stained as written below, but additionally stained during the primary staining step with a <sup>fl</sup>uorescently conjugated primary pRPS6 antibody (BioLegend: 608603). Cells for each experiment were sorted into four bins representing quartiles (Fig. S2E). After sorting, the cells were hashed and processed (see below) and 3000 cells from each bin were sent into the 10x pipeline. The remaining cells for each bin were run through <sup>fl</sup>ow cytometry a second time using the pRPS6-PE <sup>fl</sup>uorescence as a readout.

## Phospho-seq

The <sup>fi</sup>xation and permeabilization steps for the Phospho-seq experiments proceeded the same as in FACS up until the blocking step, at which point in Phospho-seq, we also performed cell hashing<sup>27</sup>. For the pilot experiment, the iPS, K562-Stim, and K562-Inhib were separately stained with unique, home-conjugated hashing antibodies, while for the organoid experiments, the <sup>fi</sup>xed permeabilized cells were split equally into four tubes for hashing. Brie<sup>fl</sup>y, 1 μg of TotalSeqAconjugated CD298 and B2M antibody mix was added into the blocking buffer. Additionally, we included 100 μg of 30-nt 3’ blocked singlestranded DNA oligo to act as an additional block within the cells (NNNNNNNNNNNNNNNNNNNNNNNNNNNNN/3ddC/). For the organoid experiments, we also included an additional 4 nM of four mixed unconjugated TSA oligos (free TotalSeq-A) that could be detected in each cell as a spiked-in control. The degree of free TotalSeq-A oligo helps to control for cellular differences in either the degree of permeabilization, or the degree of non-speci<sup>fi</sup>c oligo binding. Cells were blocked for 30 min at room temperature on a tube rotator. During this blocking step, the primary antibody pool was incubated with SSB as above in preparation for primary antibody staining. For the pilot experiments, we used 0.5 μg/antibody for primary staining while for the retinal and brain organoid experiments we used 0.25 μg/antibody. After blocking, cells were centrifuged at $6 0 0 \times g$ for 5 min and washed <sup>g</sup>once in wash buffer #2. Cells from each partition were resuspended in wash buffer #2, counted and combined in equal proportions up to 1 million cells total. Combined cells were centrifuged again at $6 0 0 \times { \bf g }$ for 5 min, resuspended in the primary antibody solution and placed in a tube rotator for 1 h at RT. After primary antibody staining, cells were washed twice in wash buffer #2 and resuspended in 1x nuclei buffer (10×). The cell suspension was sent through a 40 μm <sup>fi</sup>lter and centrifuged at $6 0 0 \times g$ for 5 min. At this point, enough supernatant was removed to leave \~50 μl cell suspension. 5 μl of this cell suspension was used for quanti<sup>fi</sup>cation and the concentration was adjusted to 6000 cells/μl if possible. 5 μl of this solution (30,000 cells) was added to a solution of 7 μl ATAC buffer B and 3 μl ATAC enzyme (10x) and the rest of the protocol followed 10x scATAC kit v1.1 (10x Genomics: 100175) protocols with minor alterations in line with the ASAP-Seq protocol (below).

After tagmentation, 0.5 μl of 1 μM each of bridge oligo A and bridge oligo B was added to the barcoding reaction to allow for TotalSeq-A and TotalSeq-B oligo capture. To allow for better hybridization between the capture oligo, bridge oligo and antibody tags there was a 5 min $4 0 \%$ step added at the beginning of the GEM incubation. After silane bead elution (Step 3.1o), 43.5 μl instead of 40.5 μl Elution Solution I was added for elution—40 μl was kept for regular SPRI cleanup while 3 μl was set aside for added complexity in the tag library PCR. After the <sup>fi</sup>rst SPRI cleanup (Step 3.2 d), the supernatant was saved instead of discarded. This supernatant contains all of the captured hashing and antibody tags, while the DNA on the beads contains the ATAC fragments and can proceed normally as written. The supernatant was treated with 32 μl of SPRI beads, allowed to bind for 5 min and subsequently cleaned up with 80% EtOH and eluted in 42 μl Buffer EB. This elute was combined with the 3 μl set aside from above and split into two tubes for ampli<sup>fi</sup>cation of TotalSeq-A and TotalSeq-B respectively. These two PCRs commenced separately with conditions as follows: 50 μl 2x KAPA HotStart ReadyMix (KAPA biosystems:07958935001), 2.5 μl 10 μM P5 primer (AATGATACGGCGAC CACCGA), 10 μM P7 primer (CAAGCAGAAGACGGCATACGAGATXXXXX XXXGTGACTGGAGTTCCTTGGCACCCGAGAATTCCA for TotalSeq-A and CAAGCAGAAGACGGCATACGAGATXXXXXXXXGTGACTGGAGTTCAGA CGTGTGC for TotalSeq-B, where Xs are i7 index nucleotides), 22.5 μl H O and 22.5 μl input fragments. The thermal cycler program is: 95 C for 3 min, 14–18 cycles of $9 5 ^ { \circ } \mathrm { C } - 2 0 \thinspace s , \thinspace 6 0 ^ { \circ } \mathrm { C } - 3 0 \thinspace s , \thinspace 7 2 ^ { \circ } \mathrm { C } - 2 0 \thinspace s ,$ then <sup>fi</sup>nally $7 2 ^ { \circ } \mathrm { C }$ for 5 min. These reactions were then cleaned up with 1.6X SPRI beads and eluted in 20 μl Buffer EB.

A step-by-step protocol can be found here: https://phospho-seq. com/post/protocol\_2/PhosphoSeq\_Protocol.pdf.

For the FACS-sorted benchmarking experiment, hashing was performed after sorting by incubating the cells within each bin in staining buffer with 1 μg hashing antibody, after which the cells were washed three times with 3% BSA in $\mathrm { P B S } + 0 . 1 \%$ Tween before inputting into the 10x scATAC-seq processing.

## ASAP-seq

For benchmarking experiments, ASAP-seq was performed as written<sup>18</sup> with intracellular staining buffer replaced by 3% BSA in PBS. Hashing was performed after sorting as detailed above. After pre-processing, all steps for ASAP-seq and Phospho-seq are identical.

## Sequencing and alignment

Assembled sequencing libraries were quanti<sup>fi</sup>ed by a Bioanalyzer High-Sensitivity DNA chip (Agilent: 5067-4626) and combined at a molar proportion of 25% ADT, 10% HTO, and 65% ATAC. These combined libraries were sequenced on a NextSeq 550 instrument using a 75-cycle high-output kit (Illumina: 20024906) with 34 bp Read 1, 8 bp i7, 16 bp i5 and 34 bp Read 2 parameters. ATAC Sequencing data were demultiplexed and aligned to the hg38 reference genome using CellRanger-ATAC v2.0.0 (10x genomics). ADT, HTO, and Free TotalSeq-A tag sequencing data were demultiplexed and aligned to index references using alevin<sup>78</sup>. Sequencing metrics for all experiments can be found in Supplementary Data 5.

## Data processing for pilot and benchmarking experiments

Chromatin data was processed with Signac ${ \bf v 1 . 9 } ^ { 7 9 } .$ . We performed peak calling using the MACS3 algorithm<sup>80</sup>, and performed downstream analysis using standard work<sup>fl</sup>ows (TFIDF, SVD, and LSI for dimensionality reduction) and default parameters. ChromVAR<sup>28</sup> was called within Signac for TF accessibility. HTOs were normalized using CLR normalization, and we performed demultiplexing and doublet detection using the HTOdemux function with default parameters. Only cells classi<sup>fi</sup>ed as singlets were kept, leaving 14,931 cells. Additional demultiplexing to assign cells to individual iPS donors was performed using Vireo $\mathsf { v } 0 . 5 . 6 ^ { 4 0 }$ , and relied on variant calling from 1000 Genomes Project and GnomAD common variants using Vartrix v1.1.22. ADTs were processed using default parameters from Seurat, including CLR normalization.

For benchmarking against FACS, staining indices for each protein tested were calculated according to the formula below<sup>81</sup>. Using the negative control sample, the median of the positive sample was subtracted from the median of the negative control samples and divided by two times the standard deviation of the negative control sample. This metric takes into account both the dynamic range of the assay, as well as the variation in the negative population.

$$
\text {Staining Index} = \frac {\text {Positive Sample Median} - \text {Negative Sample Median}}{2 \times (\text {SD Negative Sample})}\tag{1}
$$

## Retinal organoid culture and harvesting

To produce retinal organoids, we used the 01F49i-N-B7 (B7) iPS cell line from the Institute of Molecular and Clinical Ophthalmology Basel, which has been previously shown to reliably produce retinal organoids<sup>31</sup>. The organoids were generated using the AMASS protocol<sup>31</sup> exactly as used in Wahle, Brancati, Harmel, and ${ \mathsf { H e } } ^ { 3 2 } .$ . iPSCs were cultured in mTeSR1 (STEMCELL Technologies, 85857) or mTeSR Plus (STEMCELL Technologies, 100–0276) supplemented with penicillin–streptomycin (1:200, Gibco, 15140122) on Matrigel-coated plates (Corning, 354277). Cells were split 1–2 times per week after dissociation with EDTA in DPBS (0.5 mM) (Gibco, 12605010). Media were supplemented with rho-associated protein kinase (ROCK) inhibitor Y-27632 (5 μM, STEM- CELL Technologies, 72302) after thawing. To generate retinal organoids, 600 cells were seeded in each microwell of an agarose chamber (MicroTissues 3D Petri Dish micro-mold, Z764019). At the time points of interest, organoids of the same batch were pooled and dissociated. Organoids were washed three times with HBSS without $\mathrm { C a } ^ { 2 + } / \mathrm { M g } 2 +$ (STEM- CELL Technologies, 37250). Singlecell suspensions were obtained using a papain-based dissociation kit (Miltenyi Biotec, 130-092-628). In brief, 1 ml of pre-warmed papain solution was added to the organoids and incubated for 10 min at $3 7 ^ { \circ } \mathrm { C } .$ To facilitate dissociation, the mix was pipette-mixed every 5 min with a p1000. Enzyme mix A was added and mixed by inversion and incubated for 10 min at $3 7 ^ { \circ } \mathrm { C } .$ . Samples were pipette-mixed until tissue dissociation was con<sup>fi</sup>rmed via visual inspection. After incubation, cells were centrifuged for 5 min at 300  and $4 ^ { \circ } \mathrm { C } .$ The cells were then resuspended in $2 5 0 \mu \mathrm { l }$ of $\mathsf { P B S } + 0 . 0 4 \%$ BSA and sequentially <sup>fi</sup>ltered through a 70-μm <sup>fi</sup>lter (pluriSelect Mini, 43-10070-50) and a 40-μm <sup>fi</sup>lter (pluriSelect Mini, 43-10040-40) and subsequently cryopreserved in CryoStor CS10 (STEMCELL Technologies: 07952) $\mathbf { a t } - 8 0 ^ { \circ } \mathbf { C }$ before moving to liquid nitrogen storage the following day.

On the day of the experiment, cells were removed from cryopreservation and thawed at $3 7 ^ { \circ } \mathrm { C } .$ Cells were deposited into Neurobasal media (Thermo: 21103049) supplemented with 5% FBS and centrifuged for 5 min at $3 0 0 \times g .$ Cell pellets were resuspended in $4 5 0 \mu \mathrm { l }$ <sup>g</sup> PBS, and run through a 40 μm <sup>fi</sup>lter, after which <sup>fi</sup>xative was added and the Phospho-seq experiment continued as written above.

## Initial data processing for retinal organoid experiment

Sequencing and data processing were performed as detailed in the pilot experiment. We removed both cells with low sequencing depth for either the ADT or ATAC as well as doublets de<sup>fi</sup>ned by hashing and HTOdemux. This left 8136 cells in total in the <sup>fi</sup>nal dataset. The ADT signal was normalized using scTransform $\mathbf { v } 2 ^ { 8 2 }$ When running scTransform, we regressed against the number of free TotalSeq-A counts, which represent the degree of cell permeabilization. This allows us to control for cellular variation in the degree of both, and/or higher degrees of intracellular stickiness for free oligo, both of which are re<sup>fl</sup>ected in the single-cell quanti<sup>fi</sup>cations of free oligo<sup>83,84</sup>. While we recommend this procedure in general for Phospho-seq experiments, standard CLR normalization yields very similar values, and does not modify our biological conclusions.

## Immuno<sup>fl</sup>uorescence for retinal organoid experiment

To validate Phospho-seq observations, a small iterative indirect immuno<sup>fl</sup>uorescent imaging (4i) experiment with two imaging rounds was performed on week 39 retinal organoids using identical techniques and samples as Wahle, Brancati, Harmel, and ${ \mathsf { H } } { \mathsf { e } } ^ { 3 2 }$ <sup>2</sup>. The antibodies used in this experiment are listed in Supplementary Supplementary Data 1.

## Phospho-seq-multi on retinal organoids

To run Phospho-seq-multi, retinal organoids were cultured as detailed above. Organoids aged 18 and 24 weeks were harvested separately and processed in parallel for the initial Phospho-seq-multi steps including <sup>fi</sup>xation, permeabilization, blocking, and hashing before being combined at the primary staining step. The processing for the Phospho-seq-multi protocol is identical to the Phospho-seq protocol with the following changes, as inspired by DOGMA-seq<sup>18</sup>. First, NxGen RNAse Inhibitor (Lucigen: 30281-1) was added at 1 U/μl for all wash buffers and at 2U/μl for permeabilization and staining buffers. Correspondingly, DTT (Invitrogen: y00147) was added to these buffers at 1 mM <sup>fi</sup>nal concentration. Next, the 10x Multiome kit (10x Genomics: 1000285) was used in place of the scATAC kit. To facilitate the capture of TSB-tagged ADTs, Bridge Oligo B (0.5 μl of 1 μM) was spiked into the barcoding master mix (Step 2.1a). Bridge Oligo A spike-in was not necessary due to the direct poly-A capture of TSA oligos in the multiome procedure. As there is a $3 7 ^ { \circ } \mathrm { C }$ step immediately following GEM generation, the additional 5 min $4 0 \%$ incubation as in Phospho-seq-ATAC is also not necessary here. From there, the protocol proceeds as written until the preampli<sup>fi</sup>cation PCR (Step 4.1) where 1 μl of $0 . 2 \mu \mathrm { M }$ HTO additive (CCTTGGCACCCGAGA ATT\*C\*C) and ADT additive (GTGACTGGAGTTCAGACGTGTGC\*T\*C) oligos were added to the master mix to amplify the TSA and TSB oligos. After preampli<sup>fi</sup>cation and SPRI cleanup (Step 4.3k), the products are eluted in 100 μl buffer EB as opposed to 160 μl as written. The ATAC library is ampli<sup>fi</sup>ed using 25 μl (25%) elute as the input with $1 5 \mu \mathrm { l } \mathsf { H } _ { 2 } \mathrm { O } .$ . The cDNA library is ampli<sup>fi</sup>ed using 35 μl (35%) of the elute as input and then the ADTs and HTOs are ampli<sup>fi</sup>ed using 20 μl (20%) each of the elute inputs combined with $2 5 \mu \mathrm { l } \mathrm { \sf ~ H } _ { 2 } \mathrm { O } .$ The ATAC and cDNA ampli<sup>fi</sup>cation proceed as written in the protocol and the ADT and HTO ampli<sup>fi</sup>cations proceed as written above for Phospho-seq using the same P7 primers but with the SI-PCRP5 primer (AATGATACGGCGACCACCGAGATCTACACTC TTTCCCTACACGACGC\*T\*C). A step-by-step protocol can be found here: https://phospho-seq.com/post/protocol\_3/PhosphoseqMulti\_ Protocol.pdf

## Phospho-seq-multi sequencing and alignment

Libraries were quanti<sup>fi</sup>ed using a Bioanalyzer as above and sequenced on a NextSeq 550 instrument. The cDNA library was sequenced using a 75-cycle high-output kit (Illumina: 20024906) with 40 bp Read1, 8 bp Index i7, and 44 bp Read 2. The ATAC and ADT libraries were sequenced using a custom sequencing recipe with a 150-cycle midoutput kit (Illumina: 20024904) with 50 bp Read 1, 8 bp Index i7, 86 bp Read 2, and 16 bp Index i5 (with 8 dark cycles). ATAC and cDNA libraries were aligned and processed using CellRanger-arc 2.0.0 to the hg38 genome. ADTs were processed using Alevin as above.

## Initial data processing for Phospho-seq-multi experiment

Cells were processed as above, while removing outliers with either >10,000 or <100 RNA UMIs and >100,000 or <1000 peaks. This left 1474 cells in this dataset with all other processing remaining the same.

## Bridge integration on retinal organoids

Previously processed and published scRNA reference datasets for Week 38 and scMultiome bridge for Week 36 retinal organoids were obtained from public sources<sup>32</sup>. The reference dataset had 22,011 cells and the bridge dataset had 4926 cells. Bridge integration and RNA imputation for the Phospho-seq dataset were performed using the standard bridge integration work<sup>fl</sup>ow<sup>23</sup> described here: https:// satijalab.org/seurat/articles/seurat5\_integration\_bridge. First, we recalled peaks in the Phospho-seq ATAC dataset using only those peaks present in the bridge dataset. This procedure identi<sup>fi</sup>es ‘anchors’ between the Phospho-seq and scRNA-seq datasets, after representing them both based on the same multi-omic dictionary. After the transfer anchors were determined, the cell labels and RNA modality were transferred onto the Phospho-seq dataset using the TransferData function in Seurat.

## Brain organoid culture and harvesting

We used four human iPS cell lines (Hoik1 and Wibj2 from the HipSci resource<sup>85</sup>, 01F49i-N-B7 (B7) from the Institute of Molecular and Clinical Ophthalmology Basel, and WTC from the Allen Institute). Stem cell lines were cultured in mTESR1 and supplemented with penicillin–streptomycin (1:200, Gibco: 15140122) on Matrigel-coated plates (Corning: 354277). Cells were passaged 1–2 times per week after dissociation with TryplE (Gibco: 12605010) or EDTA in DPBS (<sup>fi</sup>nal concentration 0.5 mM) (Gibco:12605010). The medium was supplemented with Rho-associated protein kinase (ROCK) inhibitor Y-27632 (<sup>fi</sup>nal concentration 5 μM, STEMCELL Technologies: 72302) the <sup>fi</sup>rst day after passage. Cells were tested for mycoplasma infection regularly using PCR validation (Venor GeM Classic, Minerva Biolabs) and found to be negative. A total of 2000–3000 cells were aggregated in ultra low-attachment plates (Corning: CLS7007) to generate brain organoids using a whole-brain organoid differentiation protocol<sup>86</sup>.

Single-cell suspensions were acquired by dissociation of the organoids with a papain-based dissociation (Miltenyi Biotec: 130-092- 628). The organoids were cut into pieces and washed with HBSS (no magnesium, no calcium, Gibco: 14170120) to remove debris before prewarmed papain solution (2 ml) was added and incubated for 15 min at $3 7 ^ { \circ } \mathrm { C } .$ . Enzyme mix A was added before the tissue pieces were triturated 5–10 times with 1000 μl wide-bore and P1000 pipette tips. The tissue pieces were incubated twice for 10 min at $3 7 ^ { \circ } \mathrm { C }$ with trituration steps in between and after with P200 and P1000 pipette tips. Cells were <sup>fi</sup>ltered consecutively with a 30 μm pre-separation <sup>fi</sup>lter and centrifuged. Cells were counted and 1–3 million cells pre-sample were cryopreserved in CryoStor CS10 (STEMCELL Technologies: 07952) at $- 8 0 { } ^ { \circ } \mathrm { C }$ before moving to liquid nitrogen storage the following day.

On the day of the experiment, cells were processed and sequenced identically to the retinal organoids.

## Initial data processing for brain organoid experiment

Chromatin data was quanti<sup>fi</sup>ed, normalized, and processed using the same work<sup>fl</sup>ow as above. We removed one cluster of cells that was de<sup>fi</sup>ned by low sequencing depth. We assigned each cell to its organoid line and donor-of-origin using Vireo $\mathsf { v } 0 . 5 . 6 ^ { 4 0 }$ , and relied on variant calling from 1000 Genomes Project and GnomAD common variants using Vartrix v1.1.22.

For ADT processing, cells with over 10,000 ADT counts were removed from the analysis, as these were outliers in ADT data. This left 9,034 cells total in the <sup>fi</sup>nal dataset. ADT signal was normalized using scTransform $\mathbf { v } 2 ^ { 8 2 }$ and regressed against the number of free TotalSeq-A counts as above. To identify relationships between ADT levels and TF activity scores, we calculated Pearson correlations between each ADT value and each TF motif chromVAR scores across all cells. These correlations were then plotted according to their rank compared to every other TF motif in the JASPAR2020 motif dataset.

## Brain organoid bridge integration

Additional single-cell experiments were performed for bridge integration on the same Day 90 organoid samples. For the bridge dataset, nuclei were extracted from cells and run through the 10X Multiome ATAC + Gene Expression protocol according to manufacturer’s instructions (10X Genomics:1000285). Libraries were sequenced on a NextSeq 550 instrument using a 150-cycle high-output kit with 50 bp R1, 8 bp i7, 16 bp i5, and 86 bp R2. Data was aligned using CellRangerarc v 2.0.0 to hg38. Aligned data was processed using default parameters in Seurat and Signac including a cutoff of 500 counts and SCT normalization for the RNA modality. Nuclei were demultiplexed using variant calling on the ATAC modality and only singlet nuclei were used. This left 4958 nuclei in the bridge dataset.

For the whole cell scRNA-Seq dataset, whole, un<sup>fi</sup>xed cells were hashed with four homemade hashing antibodies, loaded at 25,000 cells/lane, and run through the 10x scRNA-Seq v3.1 kit according to manufacturer’s instructions (10x Genomics: 1000268). Separate HTO and RNA libraries were constructed and sequenced on a NextSeq 550 instrument at a ratio of 90% RNA and 10% HTOs using a 75-cycle highthroughput kit with 28 bp R1, 8 bp i7, and 56 bp R2. Transcriptomic data were aligned using CellRanger v7.0.0 to hg38 and HTO data was aligned to indices using Alevin. Cells were processed using default parameters in Seurat with SCT normalization. HTOs were quanti<sup>fi</sup>ed and cells were clustered according to HTO expression, with clusters representing doublets removed from subsequent analysis. This processing resulted in 19,280 cells in the <sup>fi</sup>nal reference dataset.

Bridge integration and RNA imputation for the Phospho-seq dataset were performed using the standard bridge integration work-<sup>fl</sup>ow as above.

## Pseudotime and trajectory analysis

To look for gene expression, protein, and chromVAR patterns across a trajectory, cells were <sup>fi</sup>rst subset by both donor and cell type lineage - Hoik1 cells and forebrain neuronal lineage or B7 cells and diencephalic lineage. The destiny<sup>42</sup> package in R was used to create diffusion maps based on the lsi embeddings from these subset datasets. Monocle3<sup>41</sup> was then run on the diffusion maps to calculate pseudotime, setting the cell with the minimum value in diffusion component 1 as the origin.

## Immuno<sup>fl</sup>uorescence on brain organoids

Organoids were <sup>fi</sup>xed overnight in 4% PFA. The next day, the organoids were washed three times for 5 min with DPBS and then transferred into 30% sucrose in DPBS until they sank to the bottom of the tube. Following the organoids were transferred into cryomolds (Sakura, #4565) and embedded in Tissue-Tek O.C.T. (Sakura, #16-004004) on dry ice. The organoids were then sliced at the Cryostar NX70 (Thermo Scienti<sup>fi</sup>c) into 20 µm thick slices $\mathsf { a t } - \mathsf { 1 7 } ^ { \circ } \mathsf { C } .$ . The slices were transferred to SuperFrost® Plus glass slides and washed with PBS. After a quick wash, antigen retrieval was performed for 20 min at 70 C in 1x preheated HistoVT one (Nacalai, #06380). Slides were washed three times for 5 min with PBS + 0.2% Tween and then transferred to blocking and permeabilization (PBS, 0.1% Triton, 5% Serum, 0.2% Tween, 0.5% BSA) for 1 h. The antibodies were added in blocking solution overnight at $4 ^ { \circ } \mathrm { C } .$ . The next day the slides were washed again three times for 5 min with PBS + 0.2% Tween and the secondary antibody was added to the blocking solution for 2 h at room temperature. Last, the slides were washed again three times for 5 min with PBS + 0.2% Tween adding DAPI to the last wash. The slides were then mounted with Prolong Glass Antifade and imaged using a confocal Zeiss LSM980 microscope (Airyscan).

## Identifying relationships between ADT and cis-regulatory elements

Before linking scATAC-seq peaks to putative protein levels, we <sup>fi</sup>rst ran the SEACells algorithm to increase the robustness of the chromatin data. We ran SEACells using the suggested parameters of 75 cells per metacell (120 metacells for the Phospho-seq dataset), n\_waypoint\_eigs = 10 and waypoint\_proportion = 0.9. Based on the SEACells grouping, we calculated cumulative count values from the ATAC, ADT, and RNA modalities. All three modalities were normalized after aggregation: ADT using CLR normalization, ATAC using TF-IDF and RNA using log-normalization.

To determine candidate peaks associated with ADTs that show regulatory potential for proximal genes, we <sup>fi</sup>rst found peaks that were correlated to each protein. For this we ran the Pearson correlation between each peak and ADT within the metacell object. We <sup>fi</sup>rst <sup>fi</sup>ltered the peaks with a correlation of >0.5, which for SOX2 and OTX2 represents the top \~2.5% of correlated peaks. For ADTs without any peaks with >0.5 correlation, we reduced the correlation cut-off by 0.1 until we observed >1% of peaks correlating. This resulted in a correlation cut-off of 0.4 for TBR2 and 0.3 for pRPS6 and pSTAT3. We next <sup>fi</sup>ltered these peaks for those that harbored the corresponding TF binding motif as indicated by the JASPAR database, using a probability score cutoff of >400. Peaks that passed both the correlation-based and sequence-based criteria were linked to the associated ADT.

We next aimed to link these peaks to putative target genes. To do this, we used the LinkPeaks function in Signac with parameters pvalue\_cutoff = 0.10, score\_cutoff = 0.01. We only considered gene-peak links that fell within 500 kb. For each identi<sup>fi</sup>ed gene-peak link, we calculated the Pearson correlation across meta-cells between peak accessibility and gene expression, and retained all peaks with correlation >0.2 (activating) or <−0.2 (repressive). These cut-offs represented approximately the top 10% positively and negatively correlated genes with ADT expression for each ADT. The lists of each of these peak-gene relationships are in Supplementary Data 4.

## Processing additional GLI3 data

To process previously published<sup>37</sup> GLI3 Cut & Tag data performed on Week 3 brain organoids, we <sup>fi</sup>rst aligned raw FASTQ <sup>fi</sup>les to the human genome using Bowtie2. The alignment reads were then deduplicated using Picard v2.8 and peaks representing GLI3 bound fragments were called using Genrich v0.6 using default settings.

Next, we obtained previously published multiome data from Week 3 GLI3 KO and GLI3 WT organoids. Since the CUT&Tag dataset was performed on a bulk sample, we used all cells in the multiome dataset. Aiming to focus on direct regulation, we quanti<sup>fi</sup>ed a cell-peak accessibility matrix using the previously identi<sup>fi</sup>ed GLI3 CUT&Tag binding sites. We identi<sup>fi</sup>ed differentially accessible sites between wildtype and knockout organoids using the FindMarkers function in Signac. Motifs enriched in both differentially accessible and nondifferentially accessible regions were discovered using the FindMotifs function in Signac, which identi<sup>fi</sup>es enriched motifs in a peak set against a set of matching background peaks. Links between GLI3 protein expression, ATAC-seq peaks, and downstream peaks were calculated as described above.

## TF footprinting

For TF footprinting analysis, motifs were <sup>fi</sup>rst identi<sup>fi</sup>ed using the Signac function AddMotifs with JASPAR2020 motif dataset. We only considered motifs within called peaks and then split the peaks into categories based on correlation between peak accessibility and TF protein expression. We selected highly correlated peaks in the top third of expression and a second set of peaks with negative correlation. The Footprint function in Signac was used to sum Tn5 insertion events surrounding motif instances in the highly correlated and negatively correlated peaks. We partitioned cells into ten quantiles based on TF protein expression and displayed Tn5 insertion enrichment for the <sup>fi</sup>rst and tenth expression quantile using the PlotFootprint function in Signac.

## ChIP-Seq benchmarking

For benchmarking our SOX2 candidate peaks, we relied upon a previously published SOX2 ChIP-Seq dataset performed on in vitro differentiated human neural progenitor cells (hNPCs) and human embryonic stem cells (hESCs)<sup>60</sup>. We plotted the ChIP-Seq data alongside our ATAC-seq data by converting the raw data into a BigWig format and plotting with the CoveragePlot function in Signac. Additional benchmarking was performed by quantifying the depth of SOX2 signal across 1180 SOX2 candidate peaks - those with correlated chromatin accessibility with SOX2 ADT, possessing a SOX2 binding motif and high correlation for proximal RNA, as outlined in Fig. 6. We repeated this analysis for all 31,782 peaks that possessed a SOX2 motif, excluding those correlated peaks and compared the two signals using a Wilcoxon rank-sum test. For benchmarking TEAD1:pRPS6 candidate peaks, data from a TEAD1 ChIP-seq experiment in glioblastoma cells<sup>66</sup> was downloaded and quanti<sup>fi</sup>ed in the same way as the SOX2 ChIP-seq dataset across all peaks in our dataset with a TEAD1 motif as well as the 481 TEAD1:pRPS6 peaks that we identi<sup>fi</sup>ed. For visualization, the data along with another TEAD1 ChIP dataset from K562 cells<sup>66</sup> was converted to a BigWig <sup>fi</sup>le and plotted as above.

## Gene ontology analysis

The genes associated with the top 500 peak-gene links for each TF were used to analyze gene ontology category enrichment using the enrichr R package<sup>87</sup>. For instances where there were fewer than 500 peak-gene links, all the peaks were used. The GO categories were then <sup>fi</sup>ltered to include only those with ≥5 genes as hits.

## Glial subsetting and reference mapping

Cells that mapped to glial cell identities in the Phospho-seq dataset were subset and reclustered. These clusters were assigned their described identity based on previously reported glial markers<sup>88,89</sup>. To determine regional identity of these clusters, cells of class Glioblast, Radial Glia and Oligo from an atlas of <sup>fi</sup>rst trimester developing brain<sup>52</sup> were reference mapped against these clusters and cells with high mapping scores for any cluster were subset and analyzed for gene expression of marker genes and regional identity from the metadata.

## STAT3 active module score

To calculate and plot the STAT3 active module score per cell, we extracted the gene names for all peak-gene links associated with high pSTAT3 signal and increased proximal gene expression. We then used the AddModuleScore() function in Seurat to calculate the collective expression of those genes from the RNA modality in each cell.

## Data availability

The processed Phospho-seq data are available at: https://zenodo.org/ record/7754315. The sequencing data generated in this study have been deposited in the GEO database under accession code GSE285561.

## Code availability

Seurat and Signac are freely available as open-source software packages at: https://github.com/satijalab/seurat. https://github.com/stuartlab/signac.

## References

1. Valls, P. O. & Esposito, A. Signalling dynamics, cell decisions, and homeostatic control in health and disease. Curr. Opin. Cell Biol. 75, 102066 (2022).

2. Badeaux, A. I. & Shi, Y. Emerging roles for chromatin as a signal integration and storage platform. Nat. Rev. Mol. Cell Biol. 14, 211–224 (2013).

3. Karin, M. & Smeal, T. Control of transcription factors by signal transduction pathways: the beginning of the end. Trends Biochem. Sci. 17, 418–422 (1992).

4. Thoreen, C. C. et al. A unifying model for mTORC1-mediated regulation of mRNA translation. Nature 485, 109–113 (2012).

5. Lee, M. J. & Yaffe, M. B. Protein regulation in signal transduction. Cold Spring Harb. Perspect. Biol. 8, (2016).

6. Sturani, E. et al. Kinetics and regulation of the tyrosine phosphorylation of epidermal growth factor receptor in intact A431 cells. Mol. Cell. Biol. 8, 1345–1351 (1988).

7. Johnson, L. N. & Barford, D. The effects of phosphorylation on the structure and function of proteins. Annu. Rev. Biophys. Biomol. Struct. 22, 199–232 (1993).

8. Vandromme, M., Gauthier-Rouvière, C., Lamb, N. & Fernandez, A. Regulation of transcription factor localization: <sup>fi</sup>ne-tuning of gene expression. Trends Biochem. Sci. 21, 59–64 (1996).

9. Salazar, C. & Höfer, T. Multisite protein phosphorylation-from molecular mechanisms to kinetic models. FEBS J 276, 3177–3198 (2009).

10. Blair, J. D., Hockemeyer, D. & Bateup, H. S. Genetically engineered human cortical spheroid models of tuberous sclerosis. Nat. Med. 24, 1568–1578 (2018).

11. Kumar, S. et al. Impaired neurodevelopmental pathways in autism spectrum disorder: a review of signaling mechanisms and crosstalk. J. Neurodev. Disord. 11, 10 (2019).

12. Krutzik, P. O. & Nolan, G. P. Intracellular phospho-protein staining techniques for <sup>fl</sup>ow cytometry: monitoring single cell signaling events. Cytometry A 55, 61–70 (2003).

13. Glassberg, J. et al. Application of phospho-CyTOF to characterize immune activation in patients with sickle cell disease in an ex vivo model of thrombosis. J. Immunol. Methods 453, 11–19 (2018).

14. Ma, S. et al. Chromatin Potential Identi<sup>fi</sup>ed by Shared Single-Cell Pro<sup>fi</sup>ling of RNA and Chromatin. Cell 183, 1103–1116.e20 (2020).

15. Stoeckius, M. et al. Simultaneous epitope and transcriptome measurement in single cells. Nat. Methods 14, 865–868 (2017).

16. Chen, A. F. et al. NEAT-seq: simultaneous pro<sup>fi</sup>ling of intra-nuclear proteins, chromatin accessibility and gene expression in single cells. Nat. Methods https://doi.org/10.1038/s41592-022-01461-y (2022).

17. Rivello, F. et al. Single-cell intracellular epitope and transcript detection reveals signal transduction dynamics. Cell Rep Methods 1, 100070 (2021).

18. Mimitou, E. P. et al. Scalable, multimodal pro<sup>fi</sup>ling of chromatin accessibility, gene expression and protein levels in single cells. Nat. Biotechnol. 39, 1246–1258 (2021).

19. Wong, M., Kosman, C., Takahashi, L. & Ramalingam, N. Simultaneous quanti<sup>fi</sup>cation of single-cell proteomes and transcriptomes in integrated <sup>fl</sup>uidic circuits. Methods Mol. Biol. 2386, 219–261 (2022).

20. Swanson, E. et al. Simultaneous trimodal single-cell measurement of transcripts, epitopes, and chromatin accessibility using TEA-seq. Elife 10, e63632 (2021).

21. Chung, H. et al. Joint single-cell measurements of nuclear proteins and RNA in vivo. Nat. Methods 18, 1204–1212 (2021).

22. Katzenelenbogen, Y. et al. Coupled scRNA-Seq and intracellular protein activity reveal an immunosuppressive role of TREM2 in cancer. Cell 182, 872–885.e19 (2020).

23. Hao, Y. et al. Dictionary learning for integrative, multimodal, and scalable single-cell analysis. Nat. Biotechnology. 42, 293–304 (2024).

24. van Buggenum, J. A. G. L. et al. A covalent and cleavable antibody-DNA conjugation strategy for sensitive protein detection via immuno-PCR. Sci. Rep. 6, 22675 (2016).

25. Hao, Y. et al. Integrated analysis of multimodal single-cell data. Cell 184, 3573–3587.e29 (2021).

26. Fishman, J. B. & Berg, E. A. Ammonium sulfate fractionation of antibodies. Cold Spring Harbor Protoc. 6, 472–474 (2018).

27. Stoeckius, M. et al. Cell Hashing with barcoded antibodies enables multiplexing and doublet detection for single cell genomics. Genome Biol 19, 224 (2018).

28. Schep, A. N., Wu, B., Buenrostro, J. D. & Greenleaf, W. J. chromVAR: inferring transcription-factor-associated accessibility from singlecell epigenomic data. Nat. Methods 14, 975–978 (2017).

29. Bar, S. & Benvenisty, N. Epigenetic aberrations in human pluripotent stem cells. EMBO J 38, e101033 (2019).

30. Maecker, H. T., Frey, T., Nomura, L. E. & Trotter, J. Selecting <sup>fl</sup>uorochrome conjugates for maximum sensitivity. Cytometry A 62, 169–173 (2004).

31. Cowan, C. S. et al. Cell types of the human retina and its organoids at single-cell resolution. Cell 182, 1623–1640.e34 (2020).

32. Wahle, P. et al. Multimodal spatiotemporal phenotyping of human retinal organoid development. Nat. Biotechnol. https://doi.org/10. 1038/s41587-023-01747-2 (2023).

33. Stuart, T. et al. Comprehensive integration of single-cell data. Cell 177, 1888–1902.e21 (2019).

34. Ma, S. et al. Loss of mTOR signaling affects cone function, cone structure and expression of cone-speci<sup>fi</sup>c proteins without affecting cone survival. Exp. Eye Res. 135, 1–13 (2015).

35. Ingram, N. T., Fain, G. L. & Sampath, A. P. Elevated energy requirement of cone photoreceptors. Proc. Natl. Acad. Sci. USA 117, 19599–19603 (2020).

36. Kanton, S. et al. Organoid single-cell genomic atlas uncovers human-speci<sup>fi</sup>c features of brain development. Nature 574, 418–422 (2019).

37. Fleck, J. S. et al. Inferring and perturbing cell fate regulomes in human brain organoids. Nature 621, 365–372 (2023).

38. Yoon, S.-J. et al. Reliability of human cortical organoid generation. Nat. Methods 16, 75–78 (2019).

39. Lancaster, M. A. et al. Cerebral organoids model human brain development and microcephaly. Nature 501, 373–379 (2013).

40. Huang, Y., McCarthy, D. J. & Stegle, O. Vireo: Bayesian demultiplexing of pooled single-cell RNA-seq data without genotype reference. Genome Biol. 20, 273 (2019).

41. Cao, J. et al. The single-cell transcriptional landscape of mammalian organogenesis. Nature 566, 496–502 (2019).

42. Angerer, P. et al. destiny: diffusion maps for large-scale single-cell data in R. Bioinformatics 32, 1241–1243 (2016).

43. Graham, V., Khudyakov, J., Ellis, P. & Pevny, L. SOX2 functions to maintain neural progenitor identity. Neuron 39, 749–765 (2003).

44. Roux, P. P. et al. RAS/ERK signaling promotes site-speci<sup>fi</sup>c ribosomal protein S6 phosphorylation via RSK and stimulates cap-dependent translation. J. Biol. Chem. 282, 14056–14064 (2007).

45. Bohlen, J., Roiuk, M. & Teleman, A. A. Phosphorylation of ribosomal protein S6 differentially affects mRNA translation based on ORF length. Nucleic Acids Res. 49, 13062–13074 (2021).

46. Mugahid, D. et al. YAP regulates cell size and growth dynamics via non-cell autonomous mediators. Elife 9, e53404 (2020).

47. Faedo, A. et al. COUP-TFI coordinates cortical patterning, neurogenesis, and laminar fate and modulates MAPK/ERK, AKT, and betacatenin signaling. Cereb. Cortex 18, 2117–2131 (2008).

48. Kanatani, S. et al. The COUP-TFII/Neuropilin-2 is a molecular switch steering diencephalon-derived GABAergic neurons in the developing mouse brain. Proc. Natl. Acad. Sci. USA 112, E4985–E4994 (2015).

49. Trevino, A. E. et al. Chromatin and gene-regulatory dynamics of the developing human cerebral cortex at single-cell resolution. Cell 184, 5053–5069.e23 (2021).

50. Hardie, D. G., Ross, F. A. & Hawley, S. A. AMPK: a nutrient and energy sensor that maintains energy homeostasis. Nat. Rev. Mol. Cell Biol. 13, 251–262 (2012).

51. Patterson, R. L., van Rossum, D. B., Nikolaidis, N., Gill, D. L. & Snyder, S. H. Phospholipase C-gamma: diverse roles in receptor-mediated calcium signaling. Trends Biochem. Sci. 30, 688–697 (2005).

52. Braun, E. et al. Comprehensive cell atlas of the <sup>fi</sup>rst-trimester developing human brain. Science 382, eadf1226 (2023).

53. Vanzan, L. et al. High throughput screening identi<sup>fi</sup>es SOX2 as a super pioneer factor that inhibits DNA methylation maintenance at its binding sites. Nat. Commun. 12, 3337 (2021).

54. Boulay, G. et al. OTX2 activity at distal regulatory elements shapes the chromatin landscape of Group 3 medulloblastoma. Cancer Discov. 7, 288–301 (2017).

55. Vierstra, J. et al. Global reference mapping of human transcription factor footprints. Nature 583, 729–736 (2020).

56. Leung, R. F. et al. Genetic regulation of vertebrate forebrain development by homeobox genes. Front. Neurosci. 16, 843794 (2022).

57. Kartha, V. K. et al. Functional inference of gene regulation using single-cell multi-omics. Cell Genom. 2, 100166 (2022).

58. Argelaguet, R. et al. Decoding gene regulation in the mouse embryo using single-cell multi-omics. Preprint at https://doi.org/10.1101/ 2022.06.15.496239.

59. Persad, S. et al. SEACells infers transcriptional and epigenomic cellular states from single-cell genomics data. Nat. Biotechnol. 41, 746–1757 (2023).

60. Zhou, C. et al. Comprehensive pro<sup>fi</sup>ling reveals mechanisms of SOX2-mediated cell fate speci<sup>fi</sup>cation in human ESCs and NPCs. Cell Res. 26, 171–189 (2016).

61. Arnold, S. J. et al. The T-box transcription factor Eomes/Tbr2 regulates neurogenesis in the cortical subventricular zone. Genes Dev. 22, 2479–2484 (2008).

62. Pollen, A. A. et al. Molecular identity of human outer radial glia during cortical development. Cell 163, 55–67 (2015).

63. Polevoy, H. et al. New roles for Wnt and BMP signaling in neural anteroposterior patterning. EMBO Rep. 20, e45842 (2019).

64. Metzis, V. et al. Nervous system regionalization entails axial allocation before neural differentiation. Cell 175, 1105–1118.e17 (2018).

65. Jain, A. et al. Morphodynamics of human early brain organoid development. bioRxiv 2023.08.21.553827 https://doi.org/10.1101/ 2023.08.21.553827 (2023).

66. Stein, C. et al. YAP1 exerts its transcriptional control via TEADmediated activation of enhancers. PLoS Genet. 11, e1005465 (2015).

67. Li, J. et al. TEAD1 and TEAD3 play redundant roles in the regulation of human epidermal proliferation. J. Investig. Dermatol. 140, 2081–2084.e4 (2020).

68. Gay, F. et al. Multiple phosphorylation events control chicken ovalbumin upstream promoter transcription factor I orphan nuclear receptor activity. Mol. Endocrinol. 16, 1332–1351 (2002).

69. Moon, C. et al. Leukemia inhibitory factor inhibits neuronal terminal differentiation through STAT3 activation. Proc. Natl. Acad. Sci. USA 99, 9015–9020 (2002).

70. Bonni, A. et al. Regulation of gliogenesis in the central nervous system by the JAK-STAT signaling pathway. Science 278, 477–483 (1997).

71. Regev, A. et al. The Human Cell Atlas. Elife 6, (2017).

72. HuBMAP Consortium. The human body at cellular resolution: the NIH Human Biomolecular Atlas Program. Nature 574, 187–192 (2019).

73. Kaya-Okur, H. S. et al. CUT&Tag for ef<sup>fi</sup>cient epigenomic pro<sup>fi</sup>ling of small samples and single cells. Nat. Commun. 10, 1930 (2019).

74. Stuart, T. et al. Nanobody-tethered transposition enables multifactorial chromatin pro<sup>fi</sup>ling at single-cell resolution. Nat. Biotechnol. https://doi.org/10.1038/s41587-022-01588-5 (2022).

75. Coupled single-cell CRISPR screening and epigenomic pro<sup>fi</sup>ling reveals causal gene regulatory networks. Cell 176, 361–376.e17 (2019).

76. Pierce, S. E., Granja, J. M. & Greenleaf, W. J. High-throughput singlecell chromatin accessibility CRISPR screens enable unbiased identi<sup>fi</sup>cation of regulatory networks in cancer. Nat. Commun. 12, 1–8 (2021).

77. Deng, Y. et al. Spatial pro<sup>fi</sup>ling of chromatin accessibility in mouse and human tissues. Nature 609, 375–383 (2022).

78. Srivastava, A., Malik, L., Smith, T., Sudbery, I. & Patro, R. Alevin ef<sup>fi</sup>ciently estimates accurate gene abundances from dscRNA-seq data. Genome Biol. 20, 65 (2019).

79. Stuart, T., Srivastava, A., Madad, S., Lareau, C. A. & Satija, R. Singlecell chromatin state analysis with Signac. Nat. Methods 18, 1333–1341 (2021).

80. Zhang, Y. et al. Model-based analysis of ChIP-Seq (MACS). Genome Biol. 9, R137 (2008).

81. Zheng, Y. et al. ADTnorm: robust integration of single-cell protein measurement across CITE-seq datasets. bioRxiv https://doi.org/10. 1101/2022.04.29.489989 (2022).

82. Choudhary, S. & Satija, R. Comparison and evaluation of statistical error models for scRNA-seq. Genome Biol. 23, 27 (2022).

83. Kim, H.-J. et al. Nuclear oligo hashing improves differential analysis of single-cell RNA-seq. Nat. Commun. 13, 2666 (2022).

84. Srivatsan, S. R. et al. Massively multiplex chemical transcriptomics at single-cell resolution. Science 367, 45–51 (2020).

85. Kilpinen, H. et al. Common genetic variation drives molecular heterogeneity in human iPSCs. Nature 546, 370–375 (2017).

86. Giandomenico, S. L., Sutcliffe, M. & Lancaster, M. A. Generation and long-term culture of advanced cerebral organoids for studying later stages of neural development. Nat. Protoc. 16, 579–602 (2020).

87. Kuleshov, M. V. et al. Enrichr: a comprehensive gene set enrichment analysis web server 2016 update. Nucleic Acids Res. 44, W90–W97 (2016).

88. Trevino, A. E. et al. Chromatin accessibility dynamics in a model of human forebrain development. Science 367, https://doi.org/10. 1126/science.aay1645 (2020).

89. Sloan, S. A. et al. Human astrocyte maturation captured in 3d cerebral cortical spheroids derived from pluripotent stem cells. Neuron 95, 779–790 e6 (2017).

## Acknowledgements

The authors would like to thank all the members of the Satija Lab and Treutlein Labs for thoughtful discussions related to this work, and

speci<sup>fi</sup>cally Sophie Jansen in the Treutlein Lab. J.D.B. is a postdoctoral fellow of the Jane Cof<sup>fi</sup>n Childs Memorial Fund for Medical Research. This work was supported by the Chan Zuckerberg Initiative (EOSS-0000000082, HCA-A-1704-01895 to R.S.), and the NIH (RM1HG011014- 02, 1OT2OD026673- 01, DP2HG009623-01, R01HD096770, R35NS097404 to R.S.). B.T. was supported by the European Research Council (758877-Organomics), the Swiss National Science Foundation (Project Grant-310030\_192604), and F.Z. was supported by EMBO Long-Term Fellowship ALTF 36-2021.

## Author contributions

J.D.B. and R.S. conceived of the study and wrote the manuscript. J.D.B. developed the Phospho-seq technology with intellectual guidance by R.S. J.D.B., and C.D. generated the <sup>fl</sup>ow cytometry and sequencing data. P.W., G.B., and F.Z. grew the organoids and generated the immuno-<sup>fl</sup>uorescence data under the supervision of B.T. J.D.B. and A.H. performed the data analysis.

## Competing interests

In the past three years, R.S. has worked as a consultant for Bristol-Myers Squibb, Regeneron, and Kallyope and served as an SAB member for ImmunAI, Resolve Biosciences, Nanostring, and the NYC Pandemic Response Lab. The other authors declare no competing interests.

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41467-025-56590-7.

Correspondence and requests for materials should be addressed to Rahul Satija.

Peer review information Nature Communications thanks Klaas Mulder and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. A peer review <sup>fi</sup>le is available.

Reprints and permissions information is available at http://www.nature.com/reprints

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional af<sup>fi</sup>liations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by/4.0/.

© The Author(s) 2025