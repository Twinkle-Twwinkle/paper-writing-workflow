Article

# Integration of imaging-based and sequencing-based spatial omics mapping on the same tissue section via DBiTplus

Received: 5 November 2024

Accepted: 27 October 2025

Published online: xx xx xxxx

Check for updates

Archibald Enninful<sup>1,10</sup>, Zhaojun Zhang<sup>2,10</sup>, Dmytro Klymyshyn<sup>3</sup>, Matthew Ingalls  <sup>4</sup>, Mingyu Yang  <sup>1</sup>, Hailing Zong<sup>3</sup>, Zhiliang Bai  <sup>1</sup>, Negin Farzad<sup>1</sup>, Graham Su<sup>1</sup>, Alev Baysoy<sup>1</sup>, Jungmin Nam  <sup>1</sup>, Yao Lu<sup>1</sup>, Shuozhen Bao<sup>1</sup>, Siyan Deng<sup>1</sup>, Nancy R. Zhang  <sup>2</sup>, Oliver Braubach<sup>4</sup>, Mina L. Xu  <sup>5</sup> , Zongming Ma  <sup>6</sup> & Rong Fan  <sup>1,5,7,8,9</sup>

Spatially mapping the transcriptome and proteome in the same tissue section can profoundly advance our understanding of cellular heterogeneity and function. Here we present Deterministic Barcoding in Tissue sequencing plus (DBiTplus), an integrative multimodal spatial omics approach combining sequencing-based spatial transcriptomics and multiplexed protein imaging on the same section, enabling both single-cell-resolution cell typing and transcriptome-wide interrogation of biological pathways. DBiTplus utilizes spatial barcoding and RNase H-mediated cDNA retrieval, preserving tissue architecture for multiplexed protein imaging. We developed computational pipelines to integrate these modalities, allowing imaging-guided deconvolution to generate single-cell-resolved spatial transcriptome atlases. We demonstrate DBiTplus across diverse samples including frozen mouse embryos, and formalin-fxed parafn-embedded human lymph nodes and lymphoma tissues, highlighting its compatibility with challenging clinical specimens. DBiTplus uncovered mechanisms of lymphomagenesis, progression and transformation in human lymphomas. Thus, DBiTplus is a unifed workfow for spatially resolved single-cell atlasing and unbiased exploration of biological mechanisms in a cell-by-cell manner at transcriptome scale.

The advent of high-throughput single-cell technologies has revolutionized our understanding of biological systems, enabling comprehensive analyses at the molecular level across diverse biological contexts<sup>1</sup>. These approaches lack spatial context, limiting our understanding of intercellular interactions within tissues. Spatial omics addresses this limitation using a wide range of approaches. Array-based approaches such as Slide-seq<sup>2</sup> utilize spatially barcoded surfaces to capture mRNA transcripts. Tissue barcoding approaches such as DBiT-seq<sup>3</sup>, spatial CITE-seq<sup>4</sup> and spatial ATAC-seq<sup>5</sup> use spatially defined delivery of DNA barcodes to profile the transcriptome, proteome or epigenome. Imaging-based methods such as MERFISH<sup>6</sup> utilize combinatorial labeling and sequential imaging to achieve subcellular resolution. Similarly, technologies such as STARmap<sup>7</sup> sequence nucleic acids directly within tissues or cells. Broadly, in situ sequencing or imaging techniques offer higher spatial resolution and sensitivity but may lack transcriptome-wide coverage, whereas sequencing-based methods provide transcriptome-wide coverage, often at the expense of high spatial resolution. Multiplexed protein imaging technologies such as CODEX<sup>8</sup> have also been developed, offering single-cell resolution profiling of protein markers for in situ cell typing.

Currently, most spatial multi-omic technologies involve running single spatial omics assays separately on adjacent or serial tissue sections, followed by computational data integration of the multimodal datasets. Due to heterogeneity in cellular composition and tissue architecture, even between adjacent sections from the same block, integrating multimodal data computationally may be suboptimal, as perfect concordance between tissue sections is almost unattainable. Thus, new methods for spatially resolved multimodal and multi-omics measurements on the same tissue sections are necessary. Single-cell spatial multimodal metabolomics approaches such as REDCAT combine protein and metabolite measurements in the same tissue section<sup>9</sup>. IN-DEPTH was also recently developed for same-slide spatial multi-omics integration<sup>10</sup>.

Here, we developed DBiTplus, which combines spatially resolved transcriptomics sequencing with multiplexed immunofluorescence (mxIF) imaging for the unbiased co-profiling of the wholetranscriptome and protein markers on the same tissue section. We tested several cDNA retrieval methods, settling on an enzymatic approach using RNase H after spatial barcoding, which maintains tissue integrity and morphology before mxIF imaging. A computational approach, modified from the MaxFuse algorithm<sup>11</sup>, was developed to integrate the multi-omic spatial transcriptomic and mxIF datasets, and a robust cell-type decomposition (RCTD)-like approach<sup>12</sup> used for DBiTplus spot cell-type deconvolution and spot splitting to generate pure cell-type sub-spots. We applied DBiTplus to elucidate the process of embryogenesis in optimal cutting temperature (OCT)-frozen and paraffin-embedded C57BL/6 (C57) mouse embryo sections. Applying DBiTplus to healthy human lymph node and lymphoma tissues demonstrated the capability to generate high-quality single-cell-resolved transcriptome and protein data from the same tissue section, addressing the hurdles associated with data integration and registration from adjacent sections.

## Results

## Design and overview of DBiTplus

In the standard DBiT-seq workflow, mRNAs are reverse-transcribed in situ within the tissue matrix, and DNA barcodes A (Ai; i = 1–50) and B $( \mathbf { B j } ; \mathbf { j } = \mathbf { 1 } - 5 \mathbf { 0 } )$ ) delivered perpendicularly through microfluidic chips with 50 parallel channels. The barcodes ligate to form a unique two-dimensional array of barcoded spots. After tissue lysis, barcoded cDNAs are recovered, purified and amplified for paired-end sequencing to generate spatial gene expression maps. This technique has been adapted to profile the transcriptome, epigenome and proteome and, more recently, applied to archival formalin-fixed paraffin-embedded (FFPE) tissue blocks<sup>3–5,13</sup>. Central to the efforts to combine DBiT-seq with mxIF was to develop techniques to release cDNA from tissue sections while maintaining tissue integrity. Two chemical approaches (using sodium hydroxide (NaOH) and dimethylsulfoxide (DMSO)) and an enzymatic approach (using RNase H) were tested (Extended Data Fig. 1a). Following successful retrieval of the cDNA and preparation of a sequencing library, the intact tissue section was imaged using Akoya Biosciences’ PhenoCycler-Fusion platform or Bruker Spatial Biology’s CellScape platform, and routine hematoxylin and eosin (H&E) staining performed on the same tissue section (Fig. 1a). For FFPE samples, the Patho-DBiT workflow<sup>13</sup> was used (until spatial barcoding was completed), following which the tissue section was incubated at $5 5 ^ { \circ } \mathrm { C }$ with a mix of Triton X-100 and Thermostable RNase H enzyme to break down RNA strands in RNA–DNA hybrids and to facilitate the diffusion through the permeabilized cell membranes. Another overnight incubation a $3 7 ^ { \circ } \mathrm { C }$ was performed to increase cDNA recovery from the tissue. The retrieved cDNAs were pooled and a sequencing library built. The intact tissue section can be stored at $- 2 0 { } ^ { \circ } \mathrm { C }$ until mxIF imaging. FFPE tissue sections underwent brief rehydration and antigen retrieval steps before mxIF imaging. After successful imaging, the flow cell could be removed from the slide and routine H&E staining performed on the same section. For fresh frozen samples, the DBiTplus workflow was identical, excluding FFPE-specific steps.

## Development of a computational framework for DBiTplus

We developed a workflow integrating the mxIF cell-by-protein and DBiTplus spot-by-gene matrices into a unified feature matrix with cell-type labels and spatial coordinates (Fig. 1b), starting with whole-cell segmentation of the mxIF data using Mesmer<sup>14</sup> and quality-control steps. The mxIF datasets were annotated via MaxFuse<sup>11</sup> integration with a reference single-cell RNA-sequencing (scRNA-seq) dataset such as the Mouse Organogenesis Cell Atlas<sup>15</sup>. Utilizing tissue boundary detection and image transformation, mxIF and DBiT-seq images were co-registered to enable accurate matching and alignment of the same cells across modalities (Extended Data Fig. 1e). Cell-type counts from mxIF segmentation masks were mapped to DBiTplus spots, which were subdivided into pure cell-type sub-spots for cell-type-specific gene expression estimation, enabling single-cell annotation beyond existing deconvolution tools (Fig. 1b).

## Workflow, development and optimization in fresh frozen and FFPE samples

Preliminary experiments on OCT-frozen embryonic day 13 (E13) mouse C57 embryo sections tested cDNA retrieval methods. The barcoded region of the tissue was covered with a clean polydimethylsiloxane (PDMS) well gasket and incubated at room temperature with 50 μl of 0.1 M NaOH for 15 min, which was then collected and neutralized with equimolar hydrochloric acid (HCl). NaOH disrupted tissue morphology (Extended Data Fig. 1b). In mouse spleen serial sections, each section was subjected to a different cDNA retrieval approach: 0.1 M NaOH for 5 min, 90% DMSO for 30 min and 10 U of RNase H at $3 7 ^ { \circ } \mathrm { C }$ for 30 min. The samples were then imaged with a 25-marker mouse immune panel by Akoya Biosciences. DMSO-treated and NaOH-treated sections yielded poor-quality CODEX staining, whereas the RNase H-treated section yielded 14 positively staining markers including CD45R (B cell lineage) and CD169 (macrophages; Extended Data Fig. 1c). Thus, the enzymatic approach was selected for further optimization (Extended Data Fig. 1d).

A new Thermostable RNase H (New England Biolabs, M0523S; optimal activity $> 6 5 ^ { \circ } \mathrm { C } )$ was introduced. E13 mouse embryo sections underwent spatial barcoding with proteinase K lysing (control) or RNase H-mediated cDNA release (test). Sequencing detected 24,102 and 20,973 genes, respectively (Extended Data Fig. 2a and Supplementary Table 2). Adding 0.5% Triton X-100 to the RNase H mix did not compromise tissue integrity, but saw an increase in mean gene counts per spot (Extended Data Fig. 2b and Supplementary Table 2). Replicates showed high correlation within and between test and control slides $( R = 0 . 8 7 \mathrm { a n d } R = 0 . 7 2$ , respectively), and strong consistency was observed between test replicates (R = 0.84; Extended Data Fig. 2c). Spatial clustering identified eight clusters, with clusters 2 and 3 corresponding to the diencephalon, mesencephalon and telencephalon, evidenced by the expression of Zbtb20 and Id4 (embryonic neocortex, forebrain; Extended Data Fig. 2d,e). Spatial patterns of select genes— Sox11, Col2a1 and Sox2—matched in situ hybridization data from the Allen Brain Atlas and the Mouse Organogenesis Spatiotemporal Transcriptomic Atlas (MOSTA) from STOmicsDB<sup>16</sup> (Extended Data Fig. 2f). Clusters 0 (control) and 2 (test) showed remarkably similar spatial distributions and 1,109 overlapping genes, underscoring the ability of DBiTplus to generate high-quality spatial transcriptome data and recapitulate tissue biology (Extended Data Fig. 2g).

We assessed the feasibility of the workflow in FFPE tissues, the ‘gold standard’ for preserving clinical tissues. We profiled human cerebellum and lymph node FFPE sections, which retained their architecture after spatial barcoding and cDNA recovery (cDNA size ranged from 200 to 800 base pairs; Supplementary Fig. 1a–c). CODEX imaging resolved distinct cerebellar layers (granular, Purkinje and molecular layers). AQP4<sup>+</sup> glial cells were observed across all three layers, and the single layer of large pear-shaped CALB1<sup>+</sup> Purkinje cell bodies was most prominent in the Purkinje cell layer (Supplementary Fig. 1d). Lymph node CODEX staining recapitulated expected architecture, including CD20<sup>+</sup> B cells and CD21<sup>+</sup> follicular dendritic cells in the follicle, and CD3ε<sup>+</sup> T cells in interfollicular regions (Supplementary Fig. 1e).

![](images/648d66a9ee4f40bda14efc5056cb1ea87da6d60f5e96812da1397d1cfe4f3dfc.jpg)

![](images/69fbae097c553fd69a65fa9c17c9d0b0c6994f633010a957220ba2e9c0491e72.jpg)

![](images/40c8a8549b77cb8b84e49f7244b6389374eae55ad8a5603c3cb5879e62c00bca.jpg)

![](images/96d9514299a1362fb0d19fd984ac9127f0123a8ec4ae79f93e86ebaef58e6f43.jpg)  
Fig. 1 | DBiTplus workflow and overview of bioinformatic workflow for integrative multimodal data analysis. a, Workflow of DBiTplus technology. b, The three steps of the integrative analysis. DBIT-seq, Deterministic Barcoding in Tissue sequencing; NGS, next-generation sequencing. Created with BioRender.com.

## Multimodal mapping of mouse embryo

DBiTplus was applied to an E11 paraffin-embedded mouse embryo (Fig. 2a) and showed a strong correlation (R = 0.99) with the standard DBiT-seq workflow (on the adjacent section) with 27,884 overlapping genes. Each spot captured \~1,200 genes and 3,300 unique molecular identifiers (UMIs; Fig. 2b–d). The same section was stained with a 26-marker CODEX panel. Unsupervised clustering identified ten transcriptomic clusters, which closely aligned with anatomic structures and spatial protein patterns from the CODEX data (Fig. 2e and Extended Data Fig. 3a,b). Cluster 4 expressed liver markers (Hba.a1, Hba.a2, Hbb.bt, Afp and Serpina6), while cluster 8 expressed embryonic heart markers (Myh6, Myl7, Myh7 and Tnnt2; Extended Data Fig. 3c). mRNA and protein expression showed consistent spatial patterns for genes such as Mki67, Nefl and Sox2 (Fig. 2f). Furthermore, spatial expression of Sox2 (pluripotency, cluster 0) Hoxa10 (limb muscle development, cluster 1) and Sox11 (progenitor cell behavior regulation including neurogenesis, cluster 2) matched in situ hybridization data from the Allen Brain Atlas and the MOSTA dataset (Extended Data Fig. 3d).

a  
![](images/2662c3d635742852e8a786674dd5db88e0ed0d635a7914bb4ab9c84adf231dc7.jpg)

![](images/681865b3a4cba38a98deb6561503374e45646a071fd082aa2672fefbb522f19f.jpg)

![](images/b51aea6018f0d28061db29c36e7551c2f26b4a152338ace811b781c7273f4a27.jpg)

![](images/e865ce5d4256d8498135f89f2317f97bf883e18ff12cba3e8e2aae6a730952f7.jpg)

e  
f  
![](images/97715a7e0bd8b4f22e488fef5cb329e1d1af0b4bdfdbff735e2f7e4c040e7985.jpg)

g  
![](images/0b5ecfb5ec451d0577de4b43b130b3418fbfb338ff71b97dc74fb63f87acf048.jpg)  
Fig. 2 | DBiTplus performance and spatial multi-omic analysis of FFPE mouse embryo. a, Brightfield images of an E11 FFPE mouse embryo section before (top) and after (bottom) the DBiTplus workflow, showing that tissue integrity and morphology are preserved following cDNA retrieval (n = 2). b, Correlation analysis between two FFPE E11 mouse embryo section samples comparing the standard DBiT-seq and the DBiTplus workflows from a two-sided Pearson correlation test (Pearson correlation = 0.99 and P value < 2.2 × 10<sup>−16</sup>). c, Venn diagram showing overlap of genes sequenced between the standard DBiT workflow and the DBiTplus workflow. d, Distribution of detected genes and

![](images/9474cf9845ad3cfc2685eddad15f84843eb28a4cc68c69587ebf173fbcd14ac5.jpg)

![](images/8478f9ea95c92fbb466a725ab83d30f071b7f91ca5ff2a49e2115e8f67d0e0a9.jpg)

UMIs per spatial spot. Blue and red dashed lines represent the average gene and UMI counts, respectively. e, Top, UMAP clustering of spatial transcriptomic data identified ten distinct transcriptomic clusters from the E11 mouse embryo. Bottom, mxIF staining performed on the same tissue section. SMA, smooth muscle actin. f, Comparison of the spatial gene expression (DBiTplus) and protein expression (CODEX) for selected markers reveals concordant spatial localization across both modalities. g, CODEX-informed spot deconvolution of DBiTplus data. Cells were annotated by label transfer from the MOCA dataset using MaxFuse.

A trained support vector machine model enabled comprehensive cell-type annotation of the whole CODEX dataset (Supplementary Figs. 2 and 3). Integration of CODEX and DBiT-seq allowed deconvolution of DBiTplus spots into constituent cell types (Fig. 2g), outperforming TACCO (Supplementary Fig. 4). Using Seurat weighted-nearestneighbor (WNN) methodology, further enhanced cell-type separation, clearly distinguishing epithelial cells from other cell types.

## Multimodal mapping of normal human lymph nodes

We applied DBiTplus to adjacent sections of a benign human lymph node, using 50-μm (Fig. 3) and 25-μm microfluidic devices, respectively (Supplementary Fig. 5). After cDNA retrieval, sections were stained with a 35-plex CODEX panel and H&E staining was done (Fig. 3a). Unsupervised clustering revealed five transcriptomic clusters, including B cells (MS4A1, cluster 1), smooth muscle cells in the medulla (MYH11 and CALD1, cluster 3) and macrophages lining the medullary cords (MARCO, cluster 4; Fig. 3b,c). DBiTplus and CODEX images were co-registered, aligning the cellular-level data from the CODEX images with the spatial transcriptomic data from the DBiTplus spots (Fig. 3d). Uniform manifold approximation and projection (UMAP) embedding of the reference scRNA-seq and CODEX datasets using MaxFuse is shown in Fig. 3e. Endothelial cells had the highest f1-scores (for label-transfer accuracy), while germinal center B cells (GCB cells) had lowest scores (Extended Data Fig. 4a). Cell-type distributions matched known lymph node biology, with T cells and B cells predominating (Fig. 3f and Extended Data Fig. 4b,c). Joint embedding of DBiTplus and CODEX (Fig. 3g) and violin plots of the cell-type-specific modality weights from WNN analysis, showed that the CODEX (protein) contributed more for T cell-subtype identification, relative to DBiTplus (transcriptome), and the converse was observed for B cell subtypes such as GCB and plasma B cells (Fig. 3h). This can be explained by the marker composition of the CODEX panel, which included more T cell than B cell markers.

Each DBiTplus spot was subdivided into pure cell-type sub-spots, with cell-type identities assigned through MaxFuse label transfer and validated against CODEX markers (4′,6-diamidino-2-phenylindole (DAPI), CD20, CD8, CD4, FOXP3, CD31) from the same region of the tissue. The imprint of the microfluidic channels, visible in the β-actin channel, provided additional confirmation of spot locations. Three methods—TACCO (Optimal transport-based)<sup>17</sup>, Cell2location (Bayesian probabilistic model)<sup>18</sup> and RCTD (Poisson regression-based deconvolution)<sup>12</sup>—were tested to benchmark spatial cell-type deconvolution, relative to the ground-truth CODEX-informed spot-level cell-type dataset (Fig. 3i). TACCO performed best, with 50% of spots showing Pearson scores > 0.6, versus 36% for Cell2location (Fig. 3j,k). Metrics for RCTD are shown in Extended Data Fig. 4d. Average silhouette width (ASW) scores, with or without CODEX (0.47 versus 0.46), were similar

## Fig. 3 | Spatial multi-omic profiling of FFPE human lymph node tissue Fig.3|Spatial multi-omic profiling ofFFPEhuman lymph node tissue

section. a, Spatial transcriptomic profiling of an FFPE benign human lymph node section at 50-μm resolution using DBiTplus (n = 1). Left, brightfield and H&E images of the same tissue section after DBiTplus and CODEX. Right, spatial clustering of spots reveals five distinct transcriptomic regions that spatially correspond to distinct histological regions within the human lymph. b, Heat map showing the top five differentially expressed genes (DEGs) across spatial transcriptomic clusters. c, mxIF staining using CODEX on the same tissue section (n = 1). Cell-type markers CD20 (B cells), SMA (vasculature) and CD3E (T cells) are visualized. Bottom, high-resolution view of the boxed region. d, Image registration of CODEX and DBiTplus data using affine transformation and landmark alignment. e, UMAP projection of integrated protein (CODEX) and RNA (DBiTplus) modalities shows strong concordance following MaxFuse integration. f, Cell-type composition derived from CODEX-labeled cells within DBiTplus spots, visualized as bar plots (left) and pie charts (right) for T cells and B cells. g, UMAP plots of DBiTplus, CODEX and Seurat WNN-integrated datasets colored by cell-type annotation. h, Seurat WNN-derived modality weights for each cell type. The strongest weights were observed for T cell subtypes and the for the DBiTplus transcriptome dataset, indicating comparable clustering structure in the DBiTplus dataset alone. However, adjusted Rand index (ARI) scores improved from 0.09 to 0.21 with CODEX guidance, reflecting more accurate cell-type assignment (Extended Data Fig. 4e).

UMAP of the DBiTplus (transcriptome) revealed diverse immune (B cell and T cell subsets) and stromal populations (Extended Data Fig. 5a). Cell-type-specific markers MS4A1 (canonical B cell marker), IL7R (naive CD4<sup>+</sup> T cells), CTLA4 (regulatory T cells) and CALD1 and MYH11 (endothelial and vascular smooth muscle cells) distinguished immune subsets (Extended Data Fig. 5b). Exploring B cell activation and maturation, violin plots revealed distinct transcriptional profiles— MS4A1, POU2F2 and CD22—broadly expressed across naive B cells, memory B cells and activated B cell populations, but downregulated in plasma B cells with concurrent upregulation of IGHM, consistent with plasma B cell maturation. IL4R was enriched in GCB/naive/activated B cell subsets, indicating activation or a poised state for activation, while MKI67 and TOP2A were upregulated in cycling B cells, indicating active proliferation. These patterns validate B cell-subtype annotations and capture functional transitions from naive to proliferative and terminally differentiated states (Extended Data Fig. 5c).

To delineate transcriptional differences between antigeninexperienced and antigen-experienced B cells, we compared naive and activated B cells using differential gene expression and pathway analysis. Naive B cells upregulated MS4A1, IGHM, IL4R and POU2F2, consistent with a resting phenotype capable of antigen sensing and homing. Correspondingly, B cell antigen receptor (BCR) signaling, CXCR4 signaling and RHO GTPase cycle pathways were upregulated, whereas apoptosis signaling was downregulated, underscoring reflecting migratory readiness and pro-survival status. In contrast, activated B cells upregulated IL4R, CD2, POU2F2 and LPP genes and EIF2 signaling, BCR signaling and antigen presentation pathways, consistent with immune activation and survival (Extended Data Fig. 5d–f). These findings underscore functional divergence between naive and activated B cells and validate the resolution of our spatial transcriptomic profiling.

## Evaluating RNA–protein concordance in DBiTplus

We evaluated RNA–protein concordance in DBiTplus, comparing spatial transcriptomics with CODEX imaging. This is important because the relationship between protein levels and their coding transcripts can be discordant, influenced by spatial and temporal mRNA variations and the protein biosynthesis machinery<sup>19</sup>. Of the 35 markers in the human lymph node CODEX panel, CD68 was the only gene transcript missing (Extended Data Fig. 6a). As validation, we compared our normalized gene expression to a reference lymph node dataset from Bai et al.<sup>13</sup> (also using Patho-DBiT), noting generally consistent gene expression levels $( R = 0 . 8 9 , P < 2 . 2 \times 1 0 ^ { - 1 6 } )$ ), particularly for highly

lowest were observed for B cell subtypes. These contributions are influenced by the composition of the CODEX marker panel. i, CODEX-informed spatial deconvolution of DBiTplus transcriptomic spots. Left, deconvolved spatial map, number of cells and cell types inferred from CODEX cell segmentation and cell-type annotation; middle: zoomed-in spot-level cell-type compositions; right, multiplexed image of the same region from CODEX (DAPI, CD20, CD8, CD4, FOXP3, CD31). Imprint of DBiTplus microfluidic channel on the tissue section observed in the beta-actin channel. j, Spatial deconvolution of DBiTplus data using TACCO. Left, deconvolved map; middle, spot-level pie chart visualization of cell types; right, correlation heat map and histogram of distribution of correlations. 50% of spots have Pearson correlation scores >0.6 when compared with ground truth (CODEX-informed spot-level cell-type deconvolution from i). k, Cell2location-based deconvolution and spatial mapping of cell types. Left to right, cell-type map, spot-level pie charts, correlation heat map and correlation score distribution. 36% of spots have Pearson correlation scores >0.6 when compared with ground truth (CODEX-informed spot-level cell-type deconvolution from i). VSMCs, vascular smooth muscle cells; T<sub>reg</sub> cells, regulatory T cells; NK, natural killer cells; Pct, percentage.

a  
![](images/1033f31365f085a9e6d38ee6701d5b33786b5a0a274fcad28f5566d54b0ec1d3.jpg)

![](images/5a48438b7bffcb2f8dbdc2951fc49791f224dcd12b71bc96b7e8a51844e3bb3b.jpg)

![](images/66e062f8c3692bb1996eca5033b529f9272e75aa0584187c8bb7323658f8737f.jpg)

![](images/326d574cd0f740a6eb0d7113158fef78dbc728e13088be0109577211d37cf215.jpg)

![](images/44343c649bdb9c2784a8031c8838d2f131f8724299832bb5d97545afd803073f.jpg)

![](images/d23ae1641182498e68344e5974bb4f3e721771ee2b0127e2d323743a7a82521f.jpg)

e  
![](images/d083542461db88fd89d32b9e813d8acfb53eb3b828631d72fcae62a03525b010.jpg)

![](images/c9173911d452f7649f59cc310bc855bcffa12ca83c03ec513722321ce66a3dd8.jpg)

![](images/4e89f5389f379ee8b520caa633618c94b3527d332bd3a712abc72b1eac0c0939.jpg)

![](images/e022251b614db836a76d3d83e8cf361b272abfd2672b0adde85c1f42e500c87d.jpg)  
j

![](images/d43d7298c46cb257bf8176c28109b4bfd596871686db1faa2bef7bbf0cd2683c.jpg)

![](images/18d1ed8880eab1f743909b48946d413ed30b5b2a0dbcead8cab18cf7266a681d.jpg)

![](images/16b971360916b12f35e5cf5d5764fd44df3a554686f26efaf82e624f7513c589.jpg)

k  
![](images/b80bed4f02de611f5c76473d5cfe832c11258b0798316750130fee98c907b9a0.jpg)

![](images/4b106602e566a4f15821d67d8fec629644ec1ccec0a4243f359b5f330af0523d.jpg)

![](images/ad11cbbfca219584778f0adcc1bfb6109a83f4847d5ed7c94c2fa23d35a7f040.jpg)

abundant transcripts like PTPRC, ACTB and HLA.DRA. Low-expressing genes, such as GZMB and IFNG, were present at low levels in both datasets. Interestingly, CD68 transcripts were detectable in the reference dataset (Extended Data Fig. 6b,c). Given the documented discrepancies between transcript and protein expression in immune cells, we evaluated the correlation between average normalized mRNA and protein levels in our dataset<sup>20</sup>. As expected, we observed minimal correlation (R = 0.23, P = 0.18), consistent with prior findings in peripheral blood mononuclear cells, particularly for T cell markers such as CD4 (Extended Data Fig. 6d). CD68 protein expression was clearly visible in the CODEX images (Extended Data Fig. 6e,f), and other macrophage-associated markers such as CD14 and CD163 were detected in both modalities (Extended Data Fig. 6g,h). These findings underscore the strength of DBiTplus in co-mapping RNAs and proteins on the same tissue section, allowing for cross-validation and enhancing confidence in cell-type annotation and spatial localization.

## Assessment of mxIF imaging and H&E staining

Assessment of CODEX data from the DBiTplus workflow revealed staining quality comparable to control lymph node sections (two sections away from the Fig. 3 sample), with strong correlations (Pearson > 0.85) for key cell-type markers including CD3ε, CD20 and podoplanin (Supplementary Figs. 6a,b and 7). H&E staining after DBiTplus, evaluated against standard H&E and post-CODEX H&E (no prior DBiT), showed partially diminished nuclear detail, but still allowed trained pathologists to identify major cell types based on cellular morphology and spatial context (Supplementary Fig. 6c). This suggests the utility of these H&E images for inferring single-cell spatial gene expression in the dead space regions of the microfluidic channels using tools like iStar<sup>21</sup>. It is worth noting that post-CODEX H&E imaging can be challenging due to potential tissue damage during the flow cell removal, which may compromise reliable histological analysis.

## Multimodal mapping of the progression of MZL using DBiTplus

To investigate lymphoma progression, we profiled a marginal zone lymphoma (MZL) sample that showed increased large cell populations, high proliferation index and clinical progression without overt histological transformation (Fig. 4a). Unlike healthy lymph nodes with well-defined follicular structure, MZL is characterized by effacement of normal tissue architecture through the infiltration of large, atypical B cells and proliferation of small to medium-sized lymphocytes with irregular nuclei, condensed chromatin and scant cytoplasm (Supplementary Fig. 8a and Fig. 4b). Clinical immunohistochemical staining was performed for relevant clinical markers (Supplementary Fig. 8b). Interestingly, we observed robust follicular dendritic cell networks marked by CD21, with clusters of CD3<sup>+</sup> and CD5<sup>+</sup> T cells.

A 2.5-mm × 2.5-mm region was profiled with DBiTplus (25-μm microfluidic device) and CODEX (44-marker panel) on the same tissue section. CODEX revealed extensive CD20<sup>+</sup> Ki67<sup>+</sup> proliferating B cells (Fig. 4c). B cells were classified as large or small B cells based on size and CD20 intensity. Integration of protein and RNA data revealed concordant expression of CD31, CD4 and TIGIT in the joint UMAP embedding (Supplementary Fig. 8c). The tumor microenvironment (TME) is composed primarily of malignant B cells (both large and small, \~55%) and T cells (\~30%), consistent with mxIF and clinical immunohistochemical images for CD20 and CD3 (Fig. 4d,e). The transcriptional profile of large B cells was consistent with biological evolution with upregulated genes like IL6ST (interleukin-6 signaling), CLU (apoptosis inhibition) and SYNE2, AHNAK and MARCKSL1 (protein synthesis and cell growth)<sup>22,23</sup> indicating increased survival, and dysregulated inflammatory signaling (Extended Data Fig. 7a). DEG analysis between small and large B cells showed upregulation of NFKBIA, suggesting potential dysregulation of the frequently overactive nuclear factor (NF)-κB pathway, as well as upregulation of PPRX1, ANTRX1 and VMP1, associated with migration/metastasis, PI3K–AKT–mTOR signaling and autophagy, respectively, in large B cells<sup>24–26</sup>. Small B cells showed upregulation of PKHD1L1 and EXOSC10, associated with B cell lymphoma growth, activation and DNA repair<sup>27,28</sup> (Fig. 4f,g and Extended Data Fig. 7b,c). Pathway analysis highlighted the upregulation of the NF-κB signaling pathways and WNT–β-catenin signaling, and a downregulation of epigenetic and chromatin organization, PI3K/AKT and BCR signaling in small B cells, while large B cells revealed upregulation in noncanonical NF-κB signaling, chromatin and histone modification and PI3K–AKT signaling pathways (Fig. 4h,i and Extended Data Fig. 7d).

Upstream regulator analysis of DEGs in large B cells identified SOX4 (a MYC upstream regulator through ATK family and TP53 inhibitor) and downregulation of RAD21 (cohesion complex gene), whose reduced expression in diffuse large B cell lymphoma (DLBCL) correlates with decreased survival, suggesting underlying pro-tumor survival mechanisms<sup>29</sup> (Extended Data Fig. 7e,f). Causal network analysis (which identifies upstream regulators of gene expression in large B cells) highlighted SYK, an SRC family kinase involved in BCR and PI3K–AKT signaling, as a key master regulator. Additional regulators included upregulated DOCK2 (proliferation regulator through RAC and ERK activation in B cell lymphomas) and downregulated SPEN (Notch signaling pathway regulator; Extended Data Fig. 7g,h), These transcriptional shifts offer insight into the biological programs underlying biological progression of MZL.

## Loss of B cell identity and activation of oncogenic programs characterize the progression of MZL along the pseudotime axis

We performed pseudotime analysis on the deconvoluted data of small and large B cell transcriptomes using Monocle 3 (ref. 15) and found small and large B cells on a differentiation continuum, revealing dynamic transcriptional changes across MZL progression (Fig. 4j,k). UMAP of B cell markers showed that both small and large B cells expressed POU2F2 and MS4A1, whereas ANTXR1 and SP4 were restricted to large and small B cells, respectively (Extended Data Fig. 7i). ANTXR1 is known to be elevated in the progression of several cancers and has recently been identified as a therapeutic target in DLBCL<sup>30</sup>. PTMA, PRRX1, FOXP1 and ASH1L increased, reflecting enhanced proliferation and transcriptional and epigenetic programs, while B cell-specific genes MS4A1 and PAX5 reduced in pseudotime, consistent with the molecular evolution of indolent MZL (Extended Data Fig. 7j and Fig. 4l). These findings suggest that MZL progression (with the increased presence of large B cells as well as aggressive clinical features) is driven by a coordinated loss of B cell identity and immune function, coupled with the upregulation of proliferation, transcriptional reprogramming and epigenetic remodeling pathways, characteristic of aggressive lymphoma transformation.

a  
![](images/55d635b1cd45058b0ab385eb83cfa8eb34314b9dea96278032133d3ad3685dfe.jpg)  
c

![](images/790af8e5885a7c61a3542a11fdda509696af8f7b36a196b2ad0d2eb19e532a1e.jpg)  
b

![](images/326d3fd870556806ea3390215ee104ffcfa0ff2720f0df3382c46ce0dfe06528.jpg)

![](images/7ad6d768a860f9eab4e073826fd3aa0fb8bd425c4635e83670e96e463c1739e1.jpg)

![](images/e34662f1b7c91584dc86650526551bceb0ea3a46e990e927845a05dc3475d31b.jpg)  
g Upregulated in small B cells Upregulated in large B cells

![](images/ceab74a0007ad4e222af69b409e6ead990cc085165f44614be97ddf9838535ef.jpg)  
f  
h

![](images/8ede8e70ad72a0b6d2bbdfa57199c2dbab359fd92fb76723a1ef59138c0b8b6c.jpg)

![](images/16247da876373d843f114b17b7d984774c21ee73a162e6ca01ebc67ba0336e75.jpg)

![](images/4eebf92e4c4afc8b919cb80524b517b85550583252cf49e381a03c1c5df66d16.jpg)

![](images/22d12d7d0655139beb615b2e60f22d42d7610fcf9387ed874eb586eb12861876.jpg)  
l

![](images/da7d38cdd98d435fc81300ebdb69f16544c21098c759f1dc5c0a961062363ada.jpg)

![](images/580f013516833d1e81402b59e8cb428ef951a4edfa7c6d12fa9d8d9fc9c6d387.jpg)

![](images/83a500bcdc01e8e08bc1f40c5aa04e14a2422ccb5dd30fd98fdc0f392f0d0d56.jpg)

## Multimodal mapping of the transformation of CLL to DLBCL using DBiTplus

Richter’s transformation is the evolution of chronic lymphocytic leukemia (CLL) into aggressive lymphomas, often DLBCL, although rare cases involve Hodgkin or T cell lymphomas<sup>31</sup>. Recent multi-omics studies have identified distinct Richter’s transformation subtypes, clonal origins and high-risk genomic features<sup>32</sup>. Most DLBCL-Richter’s transformation cases (\~80%) are clonally related to the original CLL, representing true transformations, with poor prognosis (median overall survival <1 year), although de novo DLBCL can occur in individuals with concurrent CLL<sup>33</sup>. We profiled a rare case of concurrent CLL and Richter’s transformation-DLBCL within the same lymph node, providing a unique spatially contiguous context to study Richter’s transformation (Fig. 5a). H&E staining revealed a region of densely packed small monomorphic cells transitioning into a sheet of large pleomorphic cells with open chromatin corresponding to the CLL and DLBCL regions, respectively (Fig. 5b and Extended Data Fig. 8a). We applied DBiTplus to 5-µm-thick sections followed by imaging with a 30-marker panel (using CellScape, with relevant CLL/DLBCL markers such as CD5, LEF1 and CD20). An adjacent section was also imaged as a quality-control measure (Extended Data Fig. 8b,c). mxIF imaging revealed proliferating CD20<sup>bright</sup>Ki67<sup>high</sup> large B cells (DLBCL region), contrasting with the CD20<sup>dim</sup>Ki67<sup>low</sup> small B cells (CLL region), as well as a higher density of T cells within the DLBCL region (Fig. 5c,d). Leveraging the distinct features of CLL and DLBCL (CD20<sup>dim</sup>Ki67<sup>low</sup> versus $\mathbf { \bar { C } } \mathbf { D } \bar { 2 } \mathbf { 0 } ^ { \mathrm { { b r i g h t } } } \mathbf { K i } 6 7 ^ { \mathrm { { h i g h } } } )$ , B cells were initially classified as large or small based on size, and the remaining cells in the TME, annotated using MaxFuse (Fig. 5e), with B cells making up \~60% of all cells (Fig. 5f). T cell infiltration was higher in DLBCL than CLL, with small B cells, on average, located closer to the nearest T cell compared to large B cells (Extended Data Fig. 8d–f). Large B cells had the largest diameters of \~20 μm (Fig. 5g and Extended Data Fig. 8g,h). Some overlap of large B cells in CLL and small B cells in DLBCL suggested a gradual transition between the two regions (Extended Data Fig. 8i,l). To refine CLL cell

Fig. 5 | Spatial multi-omics characterization of Richter’s transformation from CLL to DLBCL. a, Schematic overview of transformation from CLL (CD5<sup>+</sup>CD20<sup>dim</sup>CD23<sup>+</sup>LEF1<sup>+</sup>Ki67<sup>low</sup>) to DLBCL (CD5<sup>+</sup>CD20<sup>bright</sup>CD23<sup>+</sup>LEF1<sup>−</sup>Ki67<sup>high</sup>). Created with BioRender.com. b, H&E staining of FFPE lymph nodes showing histologically distinct regions of CLL and DLBCL (n = 1). Zoomed-in region highlighting the transition between the two regions. Right, brightfield image of the DBiTplus-barcoded region. c, mxIF imaging (using CellScape) of the same tissue section showing CD20, CD3E, Ki67, COL4A1 and DAPI staining (n = 1). The regions below and above the dashed line represent the CLL and DLBCL regions, respectively. Zoomed-in region demonstrating differences in proliferation and immune infiltration between DLBCL and CLL regions. Arrowheads point to highly proliferative large B cells. d, Spatial distribution of T cell markers (CD4, CD45RO, CD3E and CD45RA) in DLBCL versus CLL regions, highlighting increased T cell infiltration in transformed zones. e, Spatial cell-type deconvolution using CellScape-guided DBiTplus transcriptomics reveals regional differences in immune cell composition across the tissue section. Cell-type annotation legend shown in f. f, Bar plot showing cell-type proportions; large B cells dominate DLBCL regions, while small B cells are enriched in CLL regions. g, Violin plot comparing large B cell and small B cell sizes. Significance level was calculated with unpaired two-tailed Welch t-test, \*\*\*\*P < 0.0001. $( n _ { \mathrm { l a r g e B c e l l s } } = 6 , 1 4 0$ and $n _ { \mathrm { s m a l l B c e l l s } } = 1 5 { , } 7 0 7 )$ . The shape of the violin represents the kernel density estimate of the data distribution. The solid white dashed line indicates the median, and the classification, we applied a gating strategy based on cell with size and normalized CD20 and Ki67 expression (Extended Data Fig. 8j,k).

Aberrant immune regulation contributes to CLL initiation and progression, and Richter’s transformation is associated with increased FOXP3<sup>+</sup> regulatory T cells and CD163<sup>+</sup> macrophages, and elevated LAG-3 compared to de novo DLBCL<sup>34,35</sup>. Spatial gradient plots revealed enrichment of CD163<sup>+</sup> macrophages, CD274 (PD-L1) and CD20<sup>+</sup> cells in DLBCL regions (Fig. 5h), indicating an immunologically active yet suppressed microenvironment. Regional scores for activation (CD38, CD45RO), cytotoxicity (granzyme B, CD56, CD8), proliferation (Ki67), immunosuppression (CD274, FOXP3, CD163) and exhaustion (CD279) using multiplexed imaging data (Fig. 5i and Extended Data Fig. 9) were all higher in DLBCL than CLL regions (two-tailed Mann–Whitney test, $^ { * * * * } P < 0 . 0 0 0 1 )$ ), mirroring the distribution of CD8<sup>+</sup> T cells with highest exhaustion and large B cells, macrophages and regulatory T cells showing highest immunosuppression scores within the TME. This aligns with reports of aberrant PD-1<sup>+</sup> neoplastic B cells and increased infiltration of FOXP3<sup>+</sup> T cells and CD163<sup>+</sup> macrophages in Richter’s transformation versus CLL, potentially influencing responses to immune checkpoint blockade. Additionally, CLL cells have been shown to overexpress PD-L1, which engages PD-1 on T cells, promoting immune tolerance through downstream inhibitory signaling<sup>36</sup>.

Spatial transcriptomic landscape of Richter’s transformation Distinct genetic and transcriptional alterations characterize Richter’s transformation, including TP53 and CDKN2A deletions, NOTCH1 gain-of-function mutations and c-MYC hyperactivation<sup>37</sup>. UMAP and spatial clustering revealed clear separation of cell types (Extended Data Fig. 9b and Fig. 5j). Large B cells uniquely expressed ROR2, SMOC2 and PDE1C, implicated in proliferation, migration and regulation of the PI3K–Akt pathway, while small B cells overexpressed anti-apoptotic BCL2, consistent with their more indolent and chronic nature, and AFF3, suggesting IGHV-mutated CLL (Extended Data Fig. 9c–e and Fig. 5k). Pathways upregulated in small B cells included BCR signaling, histone modification and T cell exhaustion, whereas CTLA4 signaling in cytotoxic T lymphocytes was downregulated (Fig. 5l). In large B cells, p53 and apoptosis signaling were upregulated, although PTEN was downregulated, suggesting activation of intrinsic stress responses, whereas canonical proliferative and epigenetic programs such as mTOR, ERK/MAPK, PI3K signaling, and DNA methylation and transcriptional repression were downregulated. This reflects the hypomethylation typically observed in Richter’s transformation versus CLL and de novo DLBCL and indicates a shift from canonical

upper and lower black dotted lines indicate the 25th and 75th percentiles. The full vertical extent of the violin represents the range of the data. h, Spatial gradient expression of selected protein markers (CD20, CD3, CD274/PD-L1, CD163) highlights differences in tumor and immune cell distribution across the tissue. i, Violin plot of the quantification of functional immune signatures (exhaustion, activation, cytotoxicity, suppression and proliferation) comparing DLBCL and CLL regions. Significance level was calculated with a two-tailed Mann–Whitney test, and \*\*\*\*P < 0.0001, $( n _ { \mathrm { C L L } } = 2 8 , 3 3 1$ and $n _ { \mathrm { D L B C L } } = 1 0 , 3 3 6 )$ . The shape of the violin represents the kernel density estimate of the data distribution. The solid white dashed line indicates the median, and the upper and lower black dotted lines indicate the 25th (first quartile, Q ) and 75th (3rd quartile, Q3) percentiles. The full vertical extent of the violin represents the range of the data, j, Spatial spot-level cell-type deconvolution mapping of lymphoma tissue. k, Volcano plot showing DEGs in the small cells. Each dot represents a specific gene, colored in blue (downregulated) and red (upregulated), respectively. (Differential gene expression computed from two-sided Wilcoxon rank-sum test, adjusted P value on the basis of Bonferroni correction.) l, Pathway analysis of small B cells. z-score is computed and used to reflect the predicted activation level. m, Heat map showing differential expression of immune checkpoint and cytotoxicity genes across large B cells, small B cells and T cells. n, Spatial BCR activation score map derived from DBiTplus transcriptomics, revealing localized activation patterns across the tissue section.

a  
![](images/bde002af80d3f98937aabde922634e410cbee853d76a06d2327f896e96b8e2e7.jpg)  
b

c  
![](images/528fef08b4601d0afa65f50a976b88d248d2aa38df13d19065f654e390a81a90.jpg)

![](images/db690d6dbdbc0150c504bd189d1bfc55b804d4e399b093de9fe25982d7dedf0c.jpg)

![](images/996b0138ecaafce96cd8db05212e3e646f408e6e0ecce55a02ab90350c7b72a1.jpg)

![](images/1f330d174e2437fdb7457d0bd861bb0c6315f56506b5e836e55b3aeee136123b.jpg)

![](images/21f7bb032a6e5219b992db929c667c8006f09204f7e9a90415313895ee1424ac.jpg)

![](images/e7fde022c8e03db97f15cce998fcda5b7fc2dd88f5231c33e1883f18683e7768.jpg)

f  
![](images/85e2abee8b80469feda799f2f50eef334737fbb0d25f7002201980fc6da6f05a.jpg)

![](images/3a325081ef1bf6171de519fb2b1225a2f83dcac7e5682bb7c07e0e265a136de1.jpg)

![](images/6e9c90351992072cbd6abe4346487c68f16a45b1a3f2ab4c20e72eca2f39dbdd.jpg)

![](images/a5e2ebe840c2f61ca254fc28d477658ce52ddbd5ccabe0edfee062060eaad33b.jpg)

j  
![](images/1614fe711f918fcd9f8c0914ad9239ae906135f47dcee2d1fcb2e95f72415887.jpg)

![](images/8bb1a1cc7de916e1c41e4f9855640e6881837d47411286d7e6277cf1a7efc5ab.jpg)  
n

k  
![](images/14049d7fe78eb0c05a81ce922946d208d461d6f639622eaadc998520fe520da4.jpg)  
m

![](images/2bc5c03fc06ccbb09642bce31b93a4cea771105800eccb370b606a8d33f279f8.jpg)

![](images/8c49446ec32d48af779bfa0719adda648158302f3249090da129c24d8ad8b1a5.jpg)

proliferative circuits. Additionally, suppression of T cell antigen receptor signaling may reflect impaired immune engagement, and upregulation of extracellular matrix remodeling suggests altered tumor–stroma interactions (Extended Data Fig. 9f). Aberrant cell-surface expression of co-inhibitory receptors CTLA4 and LAG-3 on large B cells may play a role in immune escape (Fig. 5m). Spatial scoring of T cell activation and exhaustion (based on previously published gene lists<sup>38–40</sup>) highlighted DLBCL hotspots, while higher scores of BCR activation were observed in the CLL region, suggesting reduced BCR survival signaling dependency in the transformed lymphoma (Supplementary Fig. 9a,b and Fig. 5n),

## Investigating the role of miRNAs in Richter’s transformation

DBiTplus further enables spatial profiling of small noncoding RNAs such as microRNAs (miRNAs), which regulate mRNA synthesis and gene expression<sup>41</sup>. The miR-17-92 cluster, miR-150 and miR-15b are critical for B cell differentiation and germinal center selection, whereas miR-21, miR-155 and miR-222 are known to be upregulated in lymphoid malignancies, with high miR-21 expression linked to the activated B cell subtype of DLBCL<sup>42</sup>. Unsupervised clustering at the DBiTplus spot level revealed seven distinct miRNA clusters, with clusters 0 and 1 corresponding to the histological transition from CLL to DLBCL (Extended Data Fig. 10a,b). Differential analysis identified several miRNAs relevant to disease progression: miR-34a, miR-21 and miR-155 (Extended Data Fig. 10c). Interestingly, miR-21 is known to inhibit expression of PTEN and activate the PI3K–AKT pathway, increasing chemotherapy resistance<sup>43</sup>, confirming the small and large B cell pathway analysis (Extended Data Fig. 10d). Other miRNAs such as miR-342 and miR-132, implicated in other lymphomas, warrant further investigation in the context of Richter’s transformation. These findings demonstrate the unique capability of DBiTplus to spatially map miRNAs and interrogate their roles in hematological malignancies.

## Single-cell pseudotime dissects the molecular evolution of CLL-transformed B cells

We applied Monocle 3 to the DBiTplus-deconvoluted single-cell transcriptomes of this CLL-DLBCL transformation. UMAP visualization revealed distinct clusters for large B cells and small B cells, indicating substantial transformation-associated transcriptional shifts (Extended Data Fig. 10e). Pseudotime analysis of small B cells revealed dynamic gene expression changes: ATM (linked to NF-κB activation), MKI67 (proliferation) and LEF1 (diagnostic CLL marker) increased over pseudotime, whereas AFF3, BCL2 and TCL1A decreased (Extended Data Fig. 10f–h). Pseudotime heat map highlighted progressive upregulation of several CLL-associated genes across multiple pathways such as DNA damage response (TP53, ATM), chromatin modification (ASXL1, SETD2) and RNA splicing (SF3B1; Extended Data Fig. 10i). BIRC3, a tumor suppressor and negative regulator of noncanonical NF-κB signaling in CLL, exhibited transient upregulation before declining, consistent with 11q deletion-associated poor prognosis. These transcriptional dynamics reveal gradual remodeling of the CLL transcriptome toward a more aggressive state, underscoring the molecular changes that may underlie Richter’s transformation.

## Discussion

Spatial multi-omics integrates genomics, transcriptomics, proteomics and metabolomics while preserving spatial context, providing a comprehensive view of molecular processes in tissues. Traditional approaches utilize separate assays on adjacent tissue sections limiting alignment and multimodal integration accuracy due to tissue heterogeneity. To overcome this, we developed DBiTplus, which combines unbiased transcriptome-wide spatial sequencing with mxIF (CODEX or CellScape) on the same tissue section, compatible with both OCT-frozen and FFPE samples. We optimized enzymatic cDNA retrieval using RNase H, while preserving tissue architecture for multiplexed imaging.

By registering DBiTplus data with high-resolution imaging, we achieve precise colocalization of transcriptomic and proteomic data. This enabled mxIF-informed DBiTplus spot deconvolution, allowing for accurate identification of cell types. Our approach involved splitting spots into pure cell-type sub-spots and utilizing the Seurat WNN methodology for reliable cell-type deconvolution and splitting the transcriptomes of individual sub-spots into single-cell transcriptional profiles. Thus, leveraging mxIF data to guide the splitting of DBiT spatial transcriptomes can enable the creation of truly single-cell-level spatially resolved transcriptome atlases.

Application to human lymph node and lymphoma samples revealed distinct spatial organization and enabled high-resolution mapping of lymphoma progression and transformation. DBiTplus also captures the whole milieu of small RNAs, particularly miRNAs, providing insights into the molecular biological mechanism of disease evolution.

DBiTplus shares common limitations with sequencing-based spatial transcriptomics approaches; low capture depth can lead to dropout of low-abundance transcripts, which may be exacerbated by the lower transcript recovery rate of DBiTplus, compared to the standard DBiT-seq workflow, an important consideration when profiling rare cell populations. Further, the tight clamping of the tissue during the DBiTplus workflow may disrupt tissue architecture outside the clamped region and may lead to reduced imaging signal. Nonetheless, these limitations are counterbalanced by several strengths: DBiTplus enables whole-transcriptome spatial profiling without being constrained by predesigned panels, can be integrated with high-plex protein imaging on the same tissue section, and is flexible and cost-effective for broad adoption. While Xenium and CosMx achieve single-cell spatial resolution through direct imaging of transcripts, DBiTplus even allows for unbiased profiling of total RNAs including small noncoding RNAs (that is, miRNAs), which is unique for discovery of new RNA biological mechanisms.

In summary, DBiTplus represents a spatial multi-omics approach that integrates sequencing-based and imaging-based spatial assays on the same tissue section, enabling image-guided deconvolution into single-cell-resolved spatial transcriptomes. By combining multiple molecular layers at single-cell resolution, DBiTplus provides unprecedented insights into tissue architecture and cellular interactions, opening new avenues for spatial multi-omics.

## Online content

Any methods, additional references, Nature Portfolio reporting summaries, source data, extended data, supplementary information, acknowledgements, peer review information; details of author contributions and competing interests; and statements of data and code availability are available at https://doi.org/10.1038/s41592-025-02948-0.

## References

1. Baysoy, A., Bai, Z., Satija, R. & Fan, R. The technological landscape and applications of single-cell multi-omics. Nat. Rev. Mol. Cell Biol. 24, 695–713 (2023).

2. Rodriques, S. G. et al. Slide-seq: a scalable technology for measuring genome-wide expression at high spatial resolution. Science 363, 1463–1467 (2019).

3. Liu, Y. et al. High-spatial-resolution multi-omics sequencing via deterministic barcoding in tissue. Cell 183, 1665–1681.e18 (2020).

4. Liu, Y. et al. High-plex protein and whole transcriptome co-mapping at cellular resolution with spatial CITE-seq. Nat. Biotechnol. 41, 1405–1409 (2023).

5. Farzad, N. et al. Spatially resolved epigenome sequencing via Tn5 transposition and deterministic DNA barcoding in tissue. Nat. Protoc. https://doi.org/10.1038/s41596-024-01013-y (2024).

6. Xia, C., Fan, J., Emanuel, G., Hao, J. & Zhuang, X. Spatial transcriptome profiling by MERFISH reveals subcellular RNA compartmentalization and cell cycle-dependent gene expression. Proc. Natl Acad. Sci. USA 116, 19490–19499 (2019).

7. Wang, X. et al. Three-dimensional intact-tissue sequencing of single-cell transcriptional states. Science https://doi.org/10.1126/ science.aat5691 (2018).

8. Black, S. et al. CODEX multiplexed tissue imaging with DNA-conjugated antibodies. Nat. Protoc. 16, 3802–3835 (2021).

9. Li, Y. et al. All-optical multimodal mapping of single cell-type– specific metabolic activities via REDCAT. Preprint at bioRxiv https://doi.org/10.1101/2024.11.07.622511 (2024).

10. Yeo, Y. Y. et al. Same-slide spatial multi-omics integration reveals tumor virus-linked spatial reorganization of the tumor microenvironment. Preprint at bioRxiv https://doi.org/10.1101/ 2024.12.20.629650 (2024).

11. Chen, S. et al. Integration of spatial and single-cell data across modalities with weakly linked features. Nat. Biotechnol. 42, 1096–1106 (2024).

12. Cable, D. M. et al. Robust decomposition of cell type mixtures in spatial transcriptomics. Nat. Biotechnol. 40, 517–526 (2022).

13. Bai, Z. et al. Spatially exploring RNA biology in archival formalin-fixed parafin-embedded tissues. Cell https://doi.org/ 10.1016/j.cell.2024.09.001 (2024).

14. Greenwald, N. F. et al. Whole-cell segmentation of tissue images with human-level performance using large-scale data annotation and deep learning. Nat. Biotechnol. 40, 555–565 (2022).

15. Cao, J. et al. The single-cell transcriptional landscape of mammalian organogenesis. Nature 566, 496–502 (2019).

16. Chen, A. et al. Spatiotemporal transcriptomic atlas of mouse organogenesis using DNA nanoball-patterned arrays. Cell 185, 1777–1792.e21 (2022).

17. Mages, S. et al. TACCO unifies annotation transfer and decomposition of cell identities for single-cell and spatial omics. Nat. Biotechnol. 41, 1465–1473 (2023).

18. Kleshchevnikov, V. et al. Cell2location maps fine-grained cell types in spatial transcriptomics. Nat. Biotechnol. 40, 661–671 (2022).

19. Liu, Y., Beyer, A. & Aebersold, R. On the dependency of cellular protein levels on mRNA abundance. Cell 165, 535–550 (2016).

20. Li, J., Zhang, Y., Yang, C. & Rong, R. Discrepant mRNA and protein expression in immune cells. Curr. Genomics 21, 560–563 (2020).

21. Zhang, D. et al. Inferring super-resolution tissue architecture by integrating spatial transcriptomics with histology. Nat. Biotechnol. https://doi.org/10.1038/s41587-023-02019-9 (2024).

22. Arribas, A. J. et al. Resistance to PI3Kδ inhibitors in marginal zone lymphoma can be reverted by targeting the IL-6/PDGFRA axis. Haematologica 107, 2685–2697 (2022).

23. Bret, C., Klein, B. & Moreaux, J. Gene expression-based risk score in difuse large B-cell lymphoma. Oncotarget 3, 1700–1710 (2012).

24. Cai, C. et al. Anthrax toxin receptor 1/tumor endothelial marker 8 promotes gastric cancer progression through activation of the PI3K/AKT/mTOR signaling pathway. Cancer Sci. 111, 1132–1145 (2020).

25. Ferreres, J. R. et al. PRRX1 silencing is required for metastatic outgrowth in melanoma and is an independent prognostic of reduced survival in patients. Mol. Oncol. 18, 2471–2494 (2024).

26. Flumann, R. et al. Distinct genetically determined origins of Myd88/BCL2-driven aggressive lymphoma rationalize targeted therapeutic intervention strategies. Blood Cancer Discov. 4, 78–97 (2023).

27. Liu, Y. et al. Palmitoylation by ZDHHC family members regulate B-cell lymphoma growth. Int. J. Biol. Macromol. 320, 145876 (2025).

28. Zhang, W. et al. Exosome complex genes mediate RNA degradation and predict survival in mantle cell lymphoma. Oncol. Lett. 18, 5119–5128 (2019).

29. Rivas, M. A. et al. Cohesin core complex gene dosage contributes to germinal center derived lymphoma phenotypes and outcomes. Front. Immunol. 12, 688493 (2021).

30. Puvvada, S. D. et al. Pharmacogenetic approaches identify ANTXR1 as a potential mediator of response to therapeutic NF-κB inhibition in difuse large B cell lymphoma. Blood 118, 234 (2011).

31. Broséus, J. et al. Molecular characterization of Richter syndrome identifies de novo difuse large B-cell lymphomas with poor prognosis. Nat. Commun. https://doi.org/10.1038/s41467-022- 34642-6 (2023)

32. Parry, E. M. et al. Evolutionary history of transformation from chronic lymphocytic leukemia to Richter syndrome. Nat. Med. 29, 158–169 (2023).

33. Parikh, S. A. et al. Difuse large B-cell lymphoma (Richter syndrome) in patients with chronic lymphocytic leukaemia (CLL): a cohort study of newly diagnosed patients. Br. J. Haematol. 162, 774–782 (2013).

34. Kipps, T. J. et al. Chronic lymphocytic leukaemia. Nat. Rev. Dis. Primers 3, 16096 (2017).

35. Sun, C. et al. The immune microenvironment shapes transcriptional and genetic heterogeneity in chronic lymphocytic leukemia. Blood Adv. 7, 145–158 (2023).

36. Mahmoud, A. M., Gaidano, G. & Mouhssine, S. Immunological aspects of Richter syndrome: from immune dysfunction to immunotherapy. Cancers 15, 1015 (2023).

37. Mouhssine, S. & Gaidano, G. Richter syndrome: from molecular pathogenesis to druggable targets. Cancers 14, 4644 (2022).

38. Zhang, C. et al. Prioritizing exhausted T cell marker genes highlights immune subtypes in pan-cancer. iScience 26, 106484 (2023).

39. Rouillard, A. D. et al. The harmonizome: a collection of processed datasets gathered to serve and mine knowledge about genes and proteins. Database 2016, baw100 (2016).

40. Diamant et al. Harmonizome 3.0: integrated knowledge about genes and proteins from diverse multi-omics resources. Nucleic Acids Res. 53, D1016–D1028 (2025).

41. Ademokun, A. & Turner, M. Regulation of B-cell diferentiation by microRNAs and RNA-binding proteins. Biochem. Soc. Trans. 36, 1191–1193 (2008).

42. Malpeli, G. et al. MYC-related microRNAs signatures in non-Hodgkin B-cell lymphomas and their relationships with core cellular pathways. Oncotarget 9, 29753–29771 (2018).

43. Lawrie, C. H. et al. Microrna expression distinguishes between germinal center B cell-like and activated B cell-like subtypes of difuse large B cell lymphoma. Int. J. Cancer 121, 1156–1161 (2007).

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons. org/licenses/by/4.0/.

© The Author(s) 2026

<sup>1</sup>Department of Biomedical Engineering, Yale University, New Haven, CT, USA. <sup>2</sup>Department of Statistics and Data Science, The Wharton School, University of Pennsylvania, Philadelphia, PA, USA. <sup>3</sup>Akoya Biosciences, Menlo Park, CA, USA. <sup>4</sup>Bruker Spatial Biology, St Louis, MO, USA. <sup>5</sup>Department of Pathology, Yale School of Medicine, New Haven, CT, USA. <sup>6</sup>Department of Statistics and Data Science, Yale University, New Haven, CT, USA. <sup>7</sup>Yale Stem Cell Center and Yale Cancer Center, Yale School of Medicine, New Haven, CT, USA. <sup>8</sup>Human and Translational Immunology Program, Yale School of Medicine, New Haven, CT, USA. <sup>9</sup>Yale Center for Research on Aging (Y-Age), Yale School of Medicine, New Haven, CT, USA. <sup>10</sup>These authors contributed equally: Archibald Enninful, Zhaojun Zhang.  e-mail: mina.xu@yale.edu; zongming.ma@yale.edu; rong.fan@yale.edu

## Methods

## Human specimens

De-identified archived benign FFPE human lymph node and lymphoma tissue blocks were obtained from Yale Pathology Tissue Services (YPTS). The tissue retrieval and distribution for research was conducted with the approval of the Yale University Institutional Review Board (approved IRB no. 1401013259) and oversight by the Tissue Resource Oversight Committee. Written informed consent for participation in any cases where identification was collected alongside the specimen, was obtained from individuals or their guardians, in accordance with the principles of the Declaration of Helsinki. Each sample was handled in strict compliance with HIPAA regulations, University Research Policies, Pathology Department diagnostic requirements and Hospital bylaws.

## Mouse tissue slides

The mouse tissue used in this study was obtained from a commercial vendor, Zyagen (San Diego, CA), which procured and handled the animals under their in-house Institutional Animal Care and Use Committee (IACUC)-approved protocols. Because no live animal procedures were conducted at our institution, separate IACUC approval was not required. C57 embryo sagittal frozen sections, E13 (MF-104-13-C57), C57 spleen frozen sections (MF-701-C57) and C57 embryo sagittal paraffin sections, E11 (MP-104-11-C57), were purchased from Zyagen. Mouse embryo frozen sagittal sections and mouse C57 spleen frozen sections were made of freshly collected tissues, snap frozen in OCT blocks. E11 mouse whole-embryo paraffin sagittal sections were made of freshly collected tissues, fixed in 10% neutral buffered formalin, and processed for paraffin embedding. Both OCT and paraffin blocks were also sectioned at a thickness o $\mathsf { f } 7 \mathrm { - } 1 0$ μm and mounted on the center of poly-L-lysine-covered glass slides (63478-AS, Electron Microscopy Sciences).

## Human tissue section preparation

After review and selection by a board-certified pathologist, optimal paraffin blocks were sectioned by YPTS at a thickness of 7–10 μm and mounted on the center of poly-L-lysine-coated 1 × 3-inch glass slides. Serial tissue sections were collected simultaneously for DBiT-seq and H&E staining. Human brain cerebellum paraffin sections (HP-202) were purchased from Zyagen and made of freshly collected tissues, fixed in 10% neutral buffered formalin and processed for paraffin embedding. Paraffin sections were stored at $- 8 0 { } ^ { \circ } \mathrm { C }$ until use.

## RNA quality assessment

To perform RNA integrity number tests, 15–20-μm-thick curls were obtained from YPTS. The RNeasy FFPE Kit for RNA Extraction from Qiagen was used. Following RNA extraction, the High Sensitivity RNA ScreenTape assay was used with the Agilent TapeStation system to assess RNA quality. The RNA integrity number equivalent, which automatically assesses RNA degradation, and the $\begin{array} { r } { \mathsf { D V } _ { 2 0 0 } , } \end{array}$ the percentage of RNA fragments > 200 nucleotides, were used as metrics for determining RNA quality.

## Fabrication of microfluidic device

Details of the fabrication process for the PDMS wafers and microfluidic chips can be found in a prior publication<sup>3</sup>.

## DNA barcode annealing

The DNA oligonucleotides were obtained from Integrated DNA Technologies, with the sequences provided in Supplementary Tables 6 and 7. The barcodes (100 μM) and ligation linker (100 μM) were annealed at a 1:1 ratio in 2× annealing buffer (20 mM Tris-HCl pH 8.0, 100 mM NaCl, 2 mM EDTA). The mixes were placed in a thermal cycle and heated t ${ } _ { 3 9 7 } { } ^ { \circ } \mathbf { C }$ to anneal and slowly cooled to room temperature at a rate of $- 0 . 1 ^ { \circ } \mathsf C \mathsf s ^ { - 1 }$ . The barcodes can be stored at $- 2 0 { } ^ { \circ } \mathrm { C }$ for up to 6 months.

## DBiTplus profiling of fresh frozen tissues

OCT-embedded tissue sections stored in a $- 8 0 { } ^ { \circ } \mathrm { C }$ freezer were allowed to equilibrate to room temperature. The section was then fixed with 4% formaldehyde for 20 min and washed three times with 0.5× DPBS-RI (1× DPBS diluted with nuclease-free water and $0 . 0 5 \mathsf { U } \mathsf { \mu l } ^ { - 1 }$ RNase Inhibitor). The tissue was permeabilized for 20 min at room temperature using 0.5% Triton X-100 in DPBS, followed by a wash with 0.5× DPBS-RI (1× DPBS diluted with nuclease-free water and $0 . 0 5 \mathrm { U } \mu \mathrm { I } ^ { - }$ <sup>−1</sup> RNase Inhibitor) to stop the permeabilization. After air-drying, a PDMS reservoir was placed over the region of interest (ROI) on the tissue slide. In situ polyadenylation was performed with Escherichia coli poly(A) polymerase. The samples were first equilibrated by adding 100 μl wash buffer (88 μl nuclease-free water, 10 μl 10× Poly(A) Reaction Buffer, $2 \mu \mu 0 \mathsf { U } \mu \mathsf { I } ^ { - 1 }$ RNase Inhibitor) and incubating at room temperature for 5 min. After removing the wash buffer, 60 μl of the Poly(A) enzymatic mix (38.4 μl nuclease-free water, $6 \mu \mu$ 10× Poly(A) Reaction Buffer, $6 \mu 1 5 \mathrm { U } \mu \mathrm { l } ^ { - 1 } \mathsf { P o l y } ( \mu )$ Polymerase, 6 μl 10 mM ATP, 2.4 μl 20 U μl<sup>−1</sup> SUPERase•In RNase Inhibitor, $1 . 2 \mu \updownarrow 4 0 \mathsf { U } \mu \mathsf { I } ^ { - 1 }$ RNase Inhibitor) was added to the reaction chamber and incubated in a humidified box at $3 7 ^ { \circ } \mathrm { C }$ for 30 min. To remove excess reagents, the slide was dipped in 50 ml DPBS and shake-washed for 5 min. Next, 60 μl of the reverse transcription mix (20 μl 25 μM RT Primer, 16.3 μl 0.5× DPBS-RI, $1 2 \mu \updownarrow 5 \times \ R \tau$ Buffer, $6 \mu 1 2 0 0 \mathsf { U } \mu \mathrm { I } ^ { - 1 }$ Maxima H Minus Reverse Transcriptase, $4 . 5 \mu \mathrm { l } 1 0$ mM dNTPs, 0.8 μl 20 U μl<sup>−1</sup> SUPERase•In RNase Inhibitor, 0.4 μl $4 0 \mathsf { U } \mu \mathsf { I } ^ { - 1 }$ RNase Inhibitor) was loaded into the PDMS reservoir and sealed with parafilm. The sample was incubated at room temperature for 30 min and then at $4 2 ^ { \circ } \mathrm { C }$ for 90 min, followed by a wash with 50 ml DPBS. For the in situ ligation of barcode A, the first PDMS device was carefully aligned over the tissue slide, positioning the 50 center channels over the ROI. The chip was imaged to record positions for downstream alignment and analysis. An acrylic clamp was used to secure the PDMS to the slide, preventing interchannel leakage. The ligation mix (100 μl 1× NEBuffer 3.1, 61.3 μl nuclease-free water, 26 μl 10× T4 ligase buffer, 15 μl T4 DNA ligase, 5 μl 5% Triton $\mathsf { X } { \cdot } 1 0 0 , 2 \mu \mathsf { l } 4 0 \mathsf { U } \mu \mathsf { I } ^ { - 1 }$ RNase Inhibitor and $0 . 7 \mu \mathrm { l } 2 0 \mathsf { U } \mu \mathrm { l } ^ { - 1 }$ SUPERase•In RNase Inhibitor) was prepared. For the barcoding reaction, 5 μl of a ligation solution (comprising 4 μl of ligation mix and 1 μl of 25 μM DNA barcode A (A1-A50)) was added to each of the 50 inlets. The solution was drawn through the channels using a gently controlled vacuum. After incubating at $3 7 ^ { \circ } \mathrm { C }$ for 30 min, the PDMS chip was removed, and the slide was washed with 50 ml of DPBS. Next, a second PDMS device with 50 perpendicular channels was attached to the air-dried slide over the ROI. A brightfield image was taken, and barcode B was ligated similarly. The tissue section was then washed with nuclease-free water to remove any residual salts, and a final brightfield image was taken to mark the boundaries of the microfluidic channels on the tissue ROI.

## Tissue deparaffinization and decrosslinking

FFPE tissue sections were allowed to equilibrate to room temperature from the $- 8 0 { } ^ { \circ } \mathrm { C }$ freezer. Tissue sections were baked for 1 h a $6 0 ^ { \circ } \mathrm { C }$ to facilitate the removal of paraffin and increase adhesion of the tissue section to the slide. The tissue slide was then immersed into xylene twice for 5 min for deparaffinization. This was followed by rehydration steps in a series of ethanol dilutions: two rounds of 100% ethanol, and one each of 90%, 70%, 50% and 30% ethanol. Finally, the tissue sections were immersed in distilled water for 5 min. Next, the tissue slide was immersed into preheated antigen retrieval buffer (Discovery CC1 buffer (Roche, Basel) or Tris-EDTA Buffer, pH 9.0 (Abcam)) and allowed to boil at $9 5 \mathrm { - } 1 0 0 ^ { \circ } \mathrm { C }$ for 10 min and then allowed to cool to room temperature. The intact tissue slide was then imaged using the ×10 objective on the M7000 Imaging EVOS System and the same profiling approach described above applied.

## cDNA retrieval post-spatial barcoding

For cDNA retrieval, the barcoded region of the tissue was covered with a clean PDMS well gasket, and 100 μl cDNA extraction solution (10 μl 5% Triton X-100, 74 μl nuclease-free water, 10 μl 1× RNase H

Reaction Buffer and 6 μl Thermostable RNase H (M0523S, New England Biolabs)) was loaded into it. The reservoir was then clamped tightly with the slide to avoid any leakage and sealed with parafilm. The clamped tissue slide was incubated in a humidified box at $. 5 5 ^ { \circ } \mathrm { C }$ for 3 h. Following this, the cDNA extraction solution was collected and 1 μl of 0.5 M EDTA was added to inactivate the RNase H enzyme. The intact tissue slide was washed with 100 μl of nuclease-free water, which was then collected. Following this, 100 μl of cDNA extraction solution was added to the tissue slide as described previously, and the clamped slide was incubated in a humidified box at $3 7 ^ { \circ } \mathrm { C }$ overnight. The cDNA extraction solution was collected and 1 μl of 0.5 M EDTA was added to inactivate the RNase H enzyme. The intact tissue slide was washed with 100 μl of nuclease-free water, which was also collected and an additional wash step with 0.1× SSC buffer done. The collected cDNA extraction solution was then pooled and stored $\mathsf { a t } - 8 0 ^ { \circ } \mathsf C$ until use. For control slides, the standard lysing process described in previous publications from the lab was followed<sup>3</sup>.

## DAPI staining

The tissue clamps were removed, and the intact tissue was washed in nuclease-free water and then with 1× PBS. Following this, the tissue slide was incubated with 500 μl of DAPI solution (two drops of NucBlue Fixed Cell ReadyProbes Reagent in 500 μl of 1× PBS) and incubated at room temperature for 5 min. The tissue slide was then imaged in the DAPI channel using the ×20 objective on the EVOS M7000 Imaging System. This image is used to co-register the DBiTplus and mxIF images. The tissue slide was then washed with 1× PBS three times and stored at $- 8 0 { } ^ { \circ } \mathrm { C }$ until the multiplexed fluorescence imaging step.

## cDNA purification, template switch and PCR amplification

To construct the sequencing library, the pooled cDNA extraction solution was first purified using the Zymo DNA Clean & Concentrator-5 kit, following the recommended 5:1 ratio and eluted into 100 μl of nuclease-free water. Biotinylated cDNAs were captured using streptavidin beads (Dynabeads MyOne Streptavidin C1, Invitrogen). Before use, the beads were washed three times with 1× B&W buffer containing 0.05% Tween 20 and resuspended in 100 µl of 2× B&W buffer (10 mM Tris-HCl pH $7 . 5 ,$ 1 mM EDTA, 2 M NaCl). The beads were then mixed with the purified cDNA in a 1:1 volume ratio and incubated with gentle rotation at room temperature for 60 min. The beads were subsequently washed twice with 1× B&W buffer and once with 1× Tris buffer containing 0.1% Tween 20. Streptavidin beads bound with cDNA molecules were resuspended in 200 μl of TSO Mix (75 μl nuclease-free water, 40 μl 5× RT buffer, 40 μl 20% Ficoll PM-400, 20 μl 10 mM dNTPs, 10 μl 200 U μl<sup>−1</sup> Maxima H Minus Reverse Transcriptase, $5 \mu \mathrm { l } 4 0 \mathrm { U } \mu \mathrm { l } ^ { - 1 }$ RNase Inhibitor, 10 μl 100 μM TSO Primer). The template switch reaction was performed at room temperature for 30 min and then at $4 2 ^ { \circ } \mathrm { C }$ for 90 min with gentle rotation. Afterward, the beads underwent a single wash with 10 mM Tris-HCl pH 7.5 containing 0.1% Tween 20 and another wash with nuclease-free water. Second-strand synthesis was then performed as follows: the beads were washed twice with TE-TW buffer (10 mM Tris pH 8, 1 mM EDTA, 0.01% Tween 20) and resuspended in freshly prepared 200 μl 0.1 M NaOH for 5 min with gentle rotation. The beads were washed once with 500 μl of TE-TW, and once with 500 μl 1× TE buffer (10 mM Tris pH 8, 1 mM EDTA). The beads were then resuspended in 200 μl second-strand synthesis reaction solution (40 μl Maxima 5× RT Buffer, 20 μl 10 mM dNTPs, 2 μl 1 mM dN-SMRT oligo, 5 μl Klenow Enzyme 133 μ ${ \mathsf { I H } } _ { 2 } { \mathsf { O } } )$ and rotated end-over-end at $3 7 ^ { \circ } \mathrm { C }$ for 1 h. The beads were washed with nuclease-free water and were resuspended in 200 μl of PCR Mix (100 μl 2× KAPA HiFi HotStart ReadyMix, 84 μl nuclease-free water, 8 μl 10 μM PCR Primer 1, 8 μl 10 μM PCR Primer 2). This suspension was then distributed into PCR strip tubes. An initial amplification was performed with the following PCR program: $9 5 ^ { \circ } \mathrm { C }$ for 3 min, five cycles at $9 8 ^ { \circ } \mathrm { C }$ for $2 0 \mathsf { s } , 6 3 ^ { \circ } \mathsf { C }$ for 45 seconds, $7 2 ^ { \circ } \mathrm { C }$ for 3 min, followed by an extension a $7 2 ^ { \circ } \mathrm { C }$ for 3 min and a hold at 4 °C. The PCR product was purified using SPRIselect beads at a $\phantom { - } 0 . 8 \times$ ratio, according to the manufacturer’s standard protocol. The resulting cDNA amplicon was then analyzed using the TapeStation system with D5000 DNA Screen-Tape and reagents. The purified PCR product can be stored at $- 2 0 { } ^ { \circ } \mathrm { C }$ until the next steps if necessary.

## rRNA removal, library preparation and sequencing

The SEQuoia RiboDepletion Kit was used to remove rRNA and mitochondrial rRNA from the amplified cDNA, following the manufacturer’s instructions. 20 ng of cDNA was used as the input amount, and three rounds of depletion were performed. We observed that two rounds of depletion could suffice. Next, following the PCR steps described in the previous step, ten PCR cycles were sufficient to directly ligate sequencing primers, using a 100 μl system consisting of 50 μl 2× KAPA HiFi HotStart ReadyMix, \~27 μl solution from the rRNA removal step, 4 μl 10 μM P5 primer, and 4 μl 10 μM P7 primer and \~15 μl of water. The library product was purified using SPRIselect beads at a 0.7× ratio, according to the manufacturer’s standard protocol, and sent out to Novogene Corporation to be sequenced on an Illumina NovaSeq 6000 or NovaSeq X Plus Sequencing System with paired-end reads of 150 base pairs in length.

## CODEX spatial multiplexing using PhenoCycler-Fusion

A modified version of the CODEX PhenoCycler-Fusion protocol (https:// www.akoyabio.com/wp-content/uploads/2021/01/CODEX-User-Manual.pdf) was adopted for tissue sections used in the DBiTplus workflow. Since the tissue had already been deparaffinized and rehydrated during the DBiTplus workflow, the CODEX process began with a gentle antigen retrieval step using 1× AR9 buffer for 5–10 min. The tissue was then allowed to cool to room temperature and was rinsed twice with nuclease-free water and hydration buffer, followed by staining buffer as the antibody cocktail was prepared. The tissue slide was incubated with the antibody cocktail at room temperature for 3 h in a humidified chamber. After incubation, the tissue underwent a series of steps including post-fixation, ice-cold methanol incubation and a final fixation step. Attached to the flow cell, the tissue section was incubated in 1× PhenoCycler buffer with additive for at least 10 min to improve adhesion. The CODEX cycles were then set up, the reporter plate was prepared and loaded, and the imaging process began. A final .qptiff file was generated, at the end that could be viewed using QuPath $( \mathsf { V } 0 . 5 . 1 ) ^ { 4 4 }$ For further details on the PhenoCycler antibody panels, experimental cycle design and reporter plate volumes, see Supplementary Data 1.

## CellScape mxIF staining and imaging

MxIF staining and imaging was performed using the CellScape platform (Bruker Spatial Biology). Human FFPE CLL samples were prepared as previously described and shipped to Bruker Spatial Biology in Saint Louis at $4 ^ { \circ } \mathrm { C } .$ . Pre-DBIT samples were shipped in standard slide mailers. Post-DBIT samples were shipped in 50 ml conical tubes with PBS to prevent sample dehydration in transit. In preparation for staining, pre-DBIT samples were deparaffinized and rehydrated according to the CellScape user manual. Briefly, pre-DBIT samples were washed for 5 min three times in HistoClear II (Electron Microscopy Sciences, Hatfield), two times in 100% ethanol (EtOH), one time each in 90% EtOH, 70% EtOH, 50% EtOH, 30% EtOH and, finally, CellScape Wash Buffer. Immediately following deparaffinization (pre-DBIT samples), or 24 h before running the CellScape experiment (post-DBIT), heat-induced epitope retrieval was performed at 110– $- 1 2 0 { } ^ { \circ } \mathrm { C }$ under low pressure in a pressure cooker with samples placed in plastic Coplin jars (Fisher, Waltham) filled with Discovery CC1 buffer (Roche, Basel) for 15 min. Thereafter, samples were allowed to cool for 25 min on the benchtop. Slides were then washed with CellScape Wash Buffer, mounted in the CellScape Whole-Slide Imaging Chamber, which was immediately filled with CellScape Storage Buffer and stored at $4 ^ { \circ } \mathrm { C }$ until use. The multiplex proteomic assay was performed on the CellScape platform using automated iterative cycles of fluorophore-conjugated primary antibody staining, imaging and photobleaching. The assay consisted of 12 cycles, with each cycle beginning with a 10-s photobleach and subsequent background measurement for each channel to be stained. This was followed by automated staining of up to three antibodies incubated for 15 min per cycle. Antibodies were subsequently washed off and fluorescence images were acquired. The 31-plex assay included Sytox Green (Thermo, S7020), the VistaPlex Cell Boundaries (Bruker Spatial Biology, VISTAPLEX3101), Immune Profiling (Bruker Spatial Biology, VISTAPLEX3102) and Architecture (Bruker Spatial Biology, VISTAPLEX 3103) kits, as well as the following custom-conjugated primary antibodies: LEF1 (Abcam, ab137872), CD5 (Leica, CD5-4C7-L-U) and CD23 (Leica, CD23-1B12-L-U).

## Flow cell removal and H&E staining

Following the mxIF imaging, the flow cell can be removed and histological H&E staining performed on the same tissue section. To remove the flow cell, the tissue slide with the flow cell is immersed in xylene or HistoClear for a minimum of 20 min to weaken the adhesive. A razor was then used to carefully detach the flow cell from the tissue slide. The tissue slide was then rinsed thoroughly with deionized water and then with 1× PhenoCycler Buffer without additive three times for 10 min each. Histological H&E staining on the FFPE sections was conducted by YPTS. The H&E images were taken using the Motic EasyScan digital slide scanner at a magnification of ×40.

## Assessing quality of mxIF imaging data after DBiTplus

The standard CODEX data preprocessing and filtering pipeline was first applied to extract cell positions and cell-level features from two adjacent CODEX slices separately. Six marker points were then manually identified from the two stacked CODEX images. The optimal affine transformation, which minimized the distance between paired marker points, was estimated using the ‘transform’ module from the Python package ‘skimage’. This transformation was subsequently applied to align cell positions from the two slices into a common coordinate system. To ensure statistical robustness, the spatial dimensions were discretized into bins with a pixel size of 100 (\~4,000 common bins), and the mean values of selected features were computed by aggregating the cells within each bin. Common bins across both datasets were identified, and Pearson correlation coefficients were calculated to quantify the strength of linear relationships between corresponding features, and scatterplots were generated to visually represent the correlations.

Sequence alignment and generation of gene expression matrix Read 2 from the FASTQ file was processed to extract UMIs and spatial barcodes A and B. Read 1, containing cDNA sequences, was aligned to the mouse GRCm39 or human GRCh38 reference genome using STAR (V2.7.8a)<sup>45</sup>. Spatial barcode sequences were demultiplexed with ST\_Pipeline (V1.8.1)<sup>46</sup>, using the predefined coordinates of the microfluidic channels, and ENSEMBL IDs were converted to gene names. This generated a gene-by-spot expression matrix for downstream analysis. Entries in the matrix that corresponded to spot positions without tissue were excluded.

## Read mapping of noncoding RNA species

The spatial transcriptomic data from the Richter’s transformation (Fig. 5) was preprocessed following the ASTRO Pipeline<sup>47</sup>, also utilized by Bai et al.<sup>13</sup>.

## Downsampling for gene and UMI comparison across samples

For comparative analyses, and to account for varying sequencing depths, the raw sequencing reads were uniformly downsampled to the read count of the sample with the minimum number of reads using Seqkit (V2.3.1)<sup>48</sup>. The downsampled reads were processed as described in the sequence alignment and generation of gene expression matrix section above. The average number of UMIs and genes per pixel were calculated during the spatial gene expression analysis using the Seurat (V4.3.0)<sup>49</sup> pipeline, taking into account only useful pixels (pixels actually covering tissue) and were visualized as violin plots.

## Spot-level gene data normalization and unsupervised clustering analysis

Spatial gene expression analysis at the spot level was conducted using the Seurat V4.3.0 pipeline. Initially, gene expression within each spot was normalized and variance-stabilized using the SCTransform method, specifically designed for scRNA-seq datasets. Linear dimensional reduction was then performed with the ‘RunPCA’ function, and the optimal number of principal components for further analysis was determined using a heuristic approach, visualized by an ‘Elbow plot’ that ranks principal component analysis (PCA) components by their variance percentages. Subsequently, the ‘FindNeighbors’ function embedded spots into a k-nearest-neighbor graph structure based on Euclidean distance in PCA space, and the ‘FindClusters’ function applied a modularity optimization technique to cluster the spots. The ‘RunUMAP’ function was used to visually explore spatial heterogeneities through the UMAP algorithm. Finally, DEGs defining each cluster were identified using the ‘FindMarkers’ function for pairwise comparisons between spot groups or ‘FindAllMarkers’ for DEGs for each identity (cluster or cell type) versus all other cells combined.

## scRNA-seq reference data

All scRNA-seq data utilized in this study are publicly available. The scRNA-seq dataset for the mouse embryo was obtained from the Mouse Organogenesis Cell Atlas Project, which can be accessed at https:// oncoscape.v3.sttrcancer.org/atlas.gs.washington.edu.mouse.rna/ landing/. For this study, cells with a ‘development\_stage’ of 10.5 to 11.5 days post-coitum were selected to correspond with CODEX measurements, using the MaxFuse method as described below. Doublet removal and cell annotations were conducted by the original authors of the dataset. The scRNA-seq dataset for human lymph nodes was retrieved from the Cell2location repository, and is available for download at https://urldefense.com/v3/\_\_https:/cell2location.cog.sanger. ac.uk/paper/integrated\_lymphoid\_organ\_scrna/RegressionNBV4To rch\_57covariates\_73260cells\_10237genes/sc.h5ad\_\_;!!IBzWLUs!XDu d8EZcXLnWNMGYjYHAFdgJyM\_lWL-\_j9l6RweZDqQXLP1uY3a78B7\_- BgAEzSHFVLk6TfuCwekjLtKGhyb4z8FJVvCtJhUcRVGqg\$/. Cell-type annotations were provided by the original study.

## Preprocessing of CODEX/CellScape (mxIF) imaging data

Whole-cell segmentation was performed using the Mesmer method<sup>14</sup> using pretrained weights. For cell mask prediction, the default training resolution of 0.5 μm per spot was adopted. Cells within the [0.05, 0.95] cell-size quantile range and possessing DAPI signal intensities exceeding the 0.1 quantile threshold were retained for analysis. mxIF features were extracted by summing the signal for each feature per cell. For each mxIF feature, the 0.05 and 0.95 quantiles were calculated, and each single-cell-level mxIF feature was subsequently scaled to a [0, 1] range, with the 0.05 quantile mapped to 0 and the 0.95 quantile mapped to 1. Values exceeding this range were clipped to 0 or 1, as appropriate.

## Integration of mxIF imaging data with scRNA-seq

The integration of scRNA-seq data and mxIF data was accomplished utilizing the MaxFuse algorithm<sup>11</sup>. Before integration, standard preprocessing protocols were applied to all scRNA-seq data using Scanpy. This preprocessing included count normalization, log1p transformation and the identification of highly variable genes, resulting in the selection of 5,000 genes exhibiting the highest variability. Linked features between the scRNA-seq and mxIF datasets were identified based on corresponding protein and gene names. From these linked features, those with a standard deviation greater than 0.01 were selected to enhance integration performance. During the pivot matching process, the number of principal components used to construct the nearest-neighbor graph was determined by examining the elbow of the singular value decomposition plot. A smoothing weight of 0.3 was applied, as recommended by the MaxFuse method, to account for the weak linkage between the two modalities. Following integration, low-quality pivots were removed to ensure the reliability of the cross-modal pivot pairs. Approximately 10% of cells from the mxIF datasets, representing high-confidence matches, were selected to construct these pivot pairs. For each pivot pair, cell-type labels from the scRNA-seq data were transferred to the matched mxIF cells. To extend cell-type annotation to the entire mxIF dataset, a support vector machine model was trained on the pivot mxIF cells to predict cell-type labels based on protein expression measurements. Once trained, the model was applied to the remaining non-pivot cells within the mxIF dataset, thereby achieving comprehensive cell-type annotation across the dataset.

## Large B cell annotation

To isolate the highly proliferative, enlarged B cell population in the MZL and CLL to DLBCL samples, we applied a three-way thresholding strategy based on protein abundance and morphometric size. For each of the markers CD20 and Ki67, as well as for the per-cell area measurement, we calculated the 60th-percentile value across all cells in the tissue section. Any cell whose CD20 intensity exceeded the CD20 0.6 quantile and whose Ki67 intensity exceeded the Ki67 0.6 quantile and whose physical cell size exceeded the area 0.6 quantile simultaneously was labeled as a ‘large B cell’. Cells failing to meet this simultaneous triple threshold were not assigned to this category. All cells that did not satisfy the ‘large B’ criteria were subsequently merged with the scRNA-seq reference using the MaxFuse pipeline, followed by the label-transfer procedure detailed in the ‘Integration of mxIF imaging data with scRNA-seq’ section. Conversion of cell size from pixel to area was based on the resolution of 0.5 μm per pixel. Diameter was inferred by modeling the cell as a circle and computing the diameter based on number of pixels in the segmentation mask.

## mxIF-DBIT alignment

To align the high-resolution mxIF image with the low-resolution DBiTplus spot image of the FFPE mouse embryo dataset, tissue boundaries were initially identified in both images. The input image was first smoothed using a Gaussian filter (implemented via the ‘filters.gaussian’ function from the scikit-image package) to reduce noise and enhance relevant structures. Subsequently, Otsu’s thresholding method (used through the ‘filters.threshold\_otsu’ function from the scikit-image package) was applied to the smoothed image to compute an optimal threshold value. This threshold was then used to generate a binary image, effectively separating the foreground (potential tissue) from the background. To ensure the detected regions were solid, any holes within the binary regions were filled using a binary hole-filling algorithm (utilizing the ‘binary\_fill\_holes’ function from the SciPy package). The final output was a binary image with no holes enabling identification of the tissue’s outer boundary. Following the identification of tissue boundaries, an optimal similarity transformation was determined and applied to the mxIF image. This transformation was computed using the ‘transform’ module from the scikit-image package, aiming to minimize the squared error loss between the transformed mxIF image and the DBiTplus image. Given the cell positions in the mxIF image and spot positions in the DBiTplus image, the learned image transformation can be utilized to register the cells. This registration ensures that cellular-level data from the mxIF images are correctly aligned with the spatial transcriptomics data from the DBiTplus spots.

## DBiTplus spot cell-type deconvolution and splitting

The reference scRNA-seq dataset was normalized to a common total count per cell corresponding to the dataset’s median sequencing depth. Specifically, total counts were calculated for each cell in the scRNA-seq dataset, the median value was determined and this value was used as the ‘target\_sum‘ in the function ‘scanpy.pp.normalize\_total’. Following normalization, the average expression profile for each cell type was computed based on the normalized counts. $\mu _ { k , j }$ denotes the average raw expression of gene j of cell type k in the scRNA-seq data. The deconvolution of DBiTplus spots is achieved by computing the cell-type proportions of mxIF cells aligned to each spot. Let $\beta _ { k , i }$ denote the proportion of the contribution of cell type k to spot i, and $x _ { i , j }$ denote the total raw expression of gene j in DBiTplus spot i. To attribute gene expression to specific cell types within each DBiTplus spot, we split each spot into pure cell-type sub-spots. This is done by computing the expected cell-type-specific gene expression at each DBiTplus spot. The calculation uses the formula shown in equation (1):

$$
\hat {x} _ {i, j, k} = \frac {x _ {i , j} \times \beta_ {k , i} \times \mu_ {k , j}}{\sum_ {k ^ {\prime} = 1} ^ {K} \beta_ {k ^ {\prime} , i} \times \mu_ {k ^ {\prime} , j}}\tag{1}
$$

## Single-cell-level gene data normalization and unsupervised clustering analysis

For single-cell-level gene data analysis, to normalize gene expression values, we first calculated the median UMI counts per pure cell-type sub-spot. This median value was then used as the scale.factor in the NormalizeData function so that all sub-spots are normalized to a common library size representative of the dataset’s central tendency. Linear dimension reduction was then performed with the ‘RunPCA’ function, and the optimal number of principal components for further analysis was determined using a heuristic approach, visualized by an ‘elbow plot’ that ranks PCA components by their variance percentages. Subsequently, the ‘FindNeighbors’ function embedded spots into a k-nearest-neighbor graph structure based on Euclidean distance in PCA space, and the ‘FindClusters’ function (resolution = 0.7, all other parameters at default values) applied a modularity optimization technique to cluster the sub-spots. The ‘RunUMAP’ function was used to visually explore spatial heterogeneities through the UMAP algorithm. Finally, DEGs defining each cluster were identified using the ‘FindMarkers’ function for pairwise comparisons between spot groups or ‘FindAll-Markers’ for differential expression for each identity (cluster or cell type) versus all other cells combined.

## Seurat WNN analysis

mxIF cells were aggregated into pure cell-type sub-spots, and DBiTplus spots were similarly divided into pure cell-type sub-spots. Subsequent analyses were performed using the Seurat WNN methodology, with measurements from the pure cell-type sub-spots serving as input data. The RNA data underwent normalization using a scale factor derived from the median UMI count. Following normalization, variable features were identified, and PCA was conducted on the RNA assay. Subsequently, the default assay was switched to the protein modality, variable features were identified, and PCA was performed on the protein data under the reduction name ‘apca’. For each cell, the nearest neighbors within the dataset were determined based on a weighted combination of RNA and protein similarities. The cell-specific modality weights and multimodal neighbors were calculated using the ‘FindMultiModalNeighbors’ function. The integrated results were then utilized for visualization and clustering.

## Deconvolution comparisons with other methods

We used Cell2location for the deconvolution analysis. First, a negative binomial regression model was trained to estimate reference transcriptomic profiles for all cell types profiled with scRNA-seq data (sc\_subsampled\_park2020.h5ad). The ‘major celltype’ annotation was used to ensure consistency. Lowly expressed genes were excluded using the filtering strategy recommended by Cell2location (cell\_count\_ cutoff = 5, cell\_percentage\_cutoff2 = 0.03, nonz\_mean\_cutoff = 1.12).

The model was trained for 600 epochs and reached convergence. Next, we estimated cell-type abundances in the spatial transcriptomics dataset (LN50UM) using the reference profiles. The following Cell2 location hyperparameters were applied: N\_cells\_per\_location = 33 (estimated from nuclei counts in H&E images using QuPath, version 0.50). Training was stopped after 50,000 iterations, with all other parameters set to default values. To assess concordance between our mxIF-guided deconvolution and the Cell2location results, we calculated, for each spot, the Pearson correlation between the vectors of cell-type proportions produced by the two methods. Correlations were summarized by: (i) the proportion of spots above thresholds (>0.9, >0.8, >0.7, >0.6), and (ii) spatial heat maps of correlation values derived from spot coordinates. We also plotted the overall correlation distribution using 0.1-wide bins. RCTD provides a principled, likelihood-based framework for inferring which single-cell transcriptional programs underlie the mRNA captured in each spatial spot. Conceptually, it treats the observed counts as a mixture of reference cell-type profiles and estimates the mixture fractions that best explain the data, while explicitly accounting for technical variability such as total UMI depth. In our workflow, the analysis was implemented in R (spacexr v2.2.1) with Seurat, SeuratDisk and zellkonverter facilitating seamless interchange between Seurat and AnnData formats. The DBiTplus dataset supplied the query layer: raw spot-level counts were extracted from the Spatial assay, two-dimensional spot coordinates were obtained through Get-TissueCoordinates() and spot-specific library sizes were computed with colSums(counts). These three components were wrapped in a SpatialRNA() object, which together with a preprocessed single-cell reference served as input to create.RCTD(). Model fitting proceeded via run.RCTD() with doublet\_mode = ‘full’. The resulting cell-type weight matrix was normalized so that proportions across all reference types sum to one in every spot (normalize\_weights()), appended to the DBiT Seurat object with AddMetaData(), and finally exported for downstream comparison with other deconvolution methods and for integration into our spatial analyses. Cell-type deconvolution with TACCO (v0.2.2) was performed in Python. Deconvolution was carried out with tc.tl.annotate, which treats every spatial spot as a compositional mixture of the single-cell expression profiles. Specifically, we passed the DBiT AnnData object (adata) and the gene-matched reference (ref) to tc.tl.annotate, using ‘celltype’ as the label to be transferred, result\_key = ‘TACCO’ to store the output, and reconstruction\_key = ‘rec’ to save reconstructed expression values. Setting multi\_center = 1 let the algorithm place a single, data-driven centroid in expression space for each cell type, striking a balance between flexibility and over-fitting. After inference, ‘tc.pp.filter’ was applied to mirror any gene or cell filtering decisions across reference and query, ensuring that subsequent comparisons rested on an identical feature space.

## Pseudotime analysis

Pseudotemporal analysis was performed with Monocle 3 (ref. 15) on average gene expressions of pure cell-type sub-spots obtained from proteome-informed cell-type deconvolution of the DBiTplus spots. The Seurat object was subset to include only cell types of interest. The raw count matrix was converted converted to a monocle cell dataset using the ‘new\_cell\_data\_set’ function. The raw count matrix was normalized with the ‘preprocess\_cds’ function. Dimensionality reduction was performed with the ‘reduce\_dimension’ function with default parameters (reduction\_method = ‘UMAP’, umap.n\_neighbors = 15, umap.min\_dist = 0.1, preprocess\_method = ‘PCA’). Next, the cells were clustered using the ‘cluster\_cell’ function and the ‘learn\_graph’ function to generate a principal graph from the reduced dimension space. The ‘order\_cells’ function was used to order the observations in a pseudotemporal manner and the trajectory visualized with the ‘plot\_cells’ function. Pseudotime plots of specific genes were plotted using the ‘plot\_genes\_in\_pseudotime’ function. The ‘graph\_test’ function was used to identify DEGs and the heat map of the DEGs plotted (both k-means and hierarchical clustering) with a modified version of code from ref. 50.

## Ingenuity pathway analysis

Ingenuity pathway analysis (Qiagen)<sup>51</sup> was used to explore the biological pathways implicated in the DEGs from our Seurat clusters or cell types. The gene expression profile of each pure cell-type sub-spot was replicated m times where m is the number of cells of the corresponding cell type in the corresponding spot. This replication step ensured proper sample sizes for P-value calculations. The DEGs per cluster or cell type are generated using the FindAllMarkers function or FindMarkers (for pairwise comparisons) in Seurat. The list of genes with corresponding log<sub>2</sub>fold change values, P value and adjusted P value of each gene, was exported as a CSV file and used as input for the Qiagen ingenuity pathway analysis software. The Ingenuity Knowledge Base (genes only) served as the reference set for performing core expression analysis. The z-score assesses the activation or inhibition level of specific pathways by measuring the congruence between the observed gene expression profile and the pathway’s known regulatory pattern from the literature. Positive z-scores denote predicted activation or upregulation, whereas negative z-scores indicate inhibition or downregulation. A z-score ≥ 2 signifies a statistically significant upregulation in pathway activity whereas a z-score ≤ −2 denotes significant downregulation of a specific pathway. The significance (−log<sub>10</sub>P value) of each pathway enrichment is further evaluated using a right-tailed Fisher’s exact test. Pathways were plotted as bar charts using Prism V10 or R (4.2.0-foss-2020b). The graphical summary provides a quick overview of the major biological themes in the ingenuity pathway analysis core analysis. The upstream regulator analysis identifies a list of upstream regulators that may be responsible for the observed gene expression changes in the list of DEGs in our datasets. The enhanced causal network analysis provides a comprehensive approach to identifying upstream molecules that control the expression of the DEGs in our datasets.

## Statistical analysis

Prism V10 (GraphPad) was used for statistical analyses and the specific tests used are indicated in the main text and figure captions.

## Reporting summary

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

## Data availability

Raw and processed data reported are deposited in the Gene Expression Omnibus under accession GSE308167. The resulting fastq files were aligned to the mouse reference genome (GRCm39) or human reference genome (GRCh38). mxIF imaging datasets and histological images are available at https://doi.org/10.5281/zenodo.17153112 (ref. 52) and https://zenodo.org/records/17153187 (ref. 53). Published data for data comparison are available online at STOmicsDB MOSTA (E13.5\_E1S2. MOSTA.h5ad; https://db.cngb.org/stomics/mosta/spatial/) and Allen Mouse Brain Atlas (Developing Mouse Brain—age, E13.5; Theiler stage, TS21; https://developingmouse.brain-map.org/). Patho-DBiT reference lymph node data are available on the Gene Expression Omnibus under accession number GSE274641 (sample GSM8454083).

## Code availability

The code for the analyzing the processed mxIF imaging datasets and the sequencing datasets are available on Zenodo (https://doi. org/10.5281/zenodo.16827046)<sup>54</sup> and GitHub (https://github.com/ Janezjz/DBiT-plus/).

## References

44. Bankhead, P. et al. QuPath: open source software for digital pathology image analysis. Sci. Rep. 7, 16878 (2017).

45. Dobin, A. et al. STAR: ultrafast universal RNA-seq aligner. Bioinformatics 29, 15–21 (2013).

46. Navarro, J. F., Sjostrand, J., Salmen, F., Lundeberg, J. & Stahl, P. L. ST Pipeline: an automated pipeline for spatial mapping of unique transcripts. Bioinformatics 33, 2591–2593 (2017).

47. Zhang, D. et al. ASTRO: automated spatial whole-transcriptome RNA-expression workflow. Preprint at bioRxiv https://doi.org/ 10.1101/2025.01.24.634814 (2025).

48. Shen, W., Le, S., Li, Y. & Hu, F. SeqKit: a cross-platform and ultrafast toolkit for FASTA/Q file manipulation. PLoS ONE 11, e0163962 (2016).

49. Hao, Y. et al. Integrated analysis of multimodal single-cell data. Cell 184, 3573–3587.e29 (2021).

50. Tambalo, M., Mitter, R. & Wilkinson, D. G. A single cell transcriptome atlas of the developing zebrafish hindbrain. Development 147, dev184143 (2020).

51. Kramer, A., Green, J., Pollard, J. Jr & Tugendreich, S. Causal analysis approaches in ingenuity pathway analysis. Bioinformatics 30, 523–530 (2014).

52. Enninful, A. Integration of imaging-based and sequencing-based spatial omics mapping on the same tissue section via DBiTplus-multiplexed IF images. Zenodo https://doi.org/10.5281/ zenodo.17153112 (2025).

53. Enninful, A. Integration of imaging-based and sequencing-based spatial omics mapping on the same tissue section via DBiTplus-multiplexed IF and H&E images. Zenodo https://doi.org/ 10.5281/zenodo.17153187 (2025).

54. Enninful, A. DBiTplus\_updated. Zenodo https://doi.org/10.5281/ zenodo.16827046 (2025).

## Acknowledgements

We thank Yale West Campus cleanroom team for assistance with microfluidic wafer fabrications and the YPTS team for FFPE tissue sectioning and staining. Computational data analysis was conducted with Yale High Performance Computing clusters. We acknowledge support received from US National Institutes of Health grants U54CA274509, U54CA268083, UH3CA257393, RF1MH128876, U54AG079759, U54AG076043, R01CA245313 and RM1MH132648

(all to R.F.) and U01CA294514 (to R.F., M.L.X. and Z.M.), and from the US National Science Foundation grants DMS 2345215 (to Z.M.) and 2245575 (to N.R.Z. and Z.M.).

## Author contributions

Conceptualization: R.F. and O.B. Methodology: A.E., H.Z., D.K, O.B., Z.Z., M.I. and R.F.; experimental investigation: A.E., H.Z., D.K., O.B., G.S., M.I. and A.B. Data analysis: A.E., Z.Z., Z.B., M.Y., Y.L., S.D., M.I. and Z.M. Data interpretation: M.L.X., R.F., O.B. and Z.M. Resources and valuable inputs: A.E., Z.Z., J.N., N.F., S.B. and N.R.Z. Original draft: A.E., Z.Z. and R.F. All authors reviewed, edited and approved the manuscript.

## Competing interests

R.F. is scientific founder and adviser for IsoPlexis, Singleron Biotechnologies and AtlasXomics. The interests of R.F. were reviewed and managed by Yale University Provost’s Ofice in accordance with the University’s conflict of interest policies. M.L.X. has served as consultant for Treeline Biosciences, Pure Marrow and Seattle Genetics. The other authors declare no competing interests.

## Additional information

Extended data is available for this paper at https://doi.org/10.1038/s41592-025-02948-0.

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s41592-025-02948-0.

Correspondence and requests for materials should be addressed to Mina L. Xu, Zongming Ma or Rong Fan.

Peer review information Nature Methods thanks Qiangyuan Zhu and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Primary Handling Editors: Rita Strack and Lei Tang, in collaboration with the Nature Methods team.

Reprints and permissions information is available at www.nature.com/reprints.

a  
![](images/de607f623d3737ef4323f947b8e63d80f7861f562e1d956f65fdae235a095989.jpg)

b  
![](images/d77a62ac56a6379b28f82f45423a11c3376c7069a01b427212e41a79af79a10e.jpg)  
d

C  
![](images/80a588f03cf23bf0633eaa0901fbb675958604609342e66d25ebb986d4746df8.jpg)

e  
![](images/f346cc96cff8b6eeab1adffeaf99ed2eb60b7efc7050989691e8d1a37e0de1e3.jpg)

![](images/b954f2eae2c402a39f4d749f573f54cc91d5ffb81c04bff3873a2d964f7ecd01.jpg)

![](images/ae0751c51dbb6a982073793f4e60200f62fbd535e343f5289eaab9828ed90fde.jpg)

![](images/19fc5ed5187faf7022598200cee5afb13f4a135929f66b0567030c2a40295433.jpg)

![](images/f0659b8377c7383787aa715aa34d833a551ab25953f72d1ad5643c9813255d01.jpg)

![](images/7c935dd26e98ef09bc9197bce56d59a91c31f4dfa7b989045e9f23e30ee7dad5.jpg)

![](images/74ce4363810367aae93238dceab01aff6850a133a6f65cc33a45da07b0439831.jpg)  
Extended Data Fig. 1 | Evaluation of cDNA retrieval strategies for compatibility with DBiTplus and downstream multiplexed immunofluorescence imaging. a, Schematic overview of three tested approaches for cDNA release from FF or FFPE tissue sections. Created with BioRender.com. b, Brightfield images of E13 mouse embryo FF sections before and after cDNA retrieval using NaOH, DMSO, or RNase H. Morphology is best preserved with the RNase H condition. c, Assessing the quality of CODEX imaging on FF mouse spleen after DBiTplus workflow  
(n = 1). The RNase H-treated sample shows positive staining makers including CD45R (B cell lineage) and CD169 (macrophages) similar to control staining. d, Schematic overview for RNase H cDNA retrieval protocol. The three tubes are pooled for cDNA purification, PCR amplification, and library preparation. Created with BioRender.com. e, Image registration pipeline between DBiTplus and mxIF datasets.

a  
![](images/a41a90759b3aae6497899ef57622d69693a592419444c8d92172a807a91e4e44.jpg)

![](images/01f05f4a87281a5758725b92e31062dc559b46823a6d788013665457f87b43db.jpg)

b  
![](images/be6a9411c32c686f0e6d2feaec62a436e66a5980c8448feac2441db5f002cc38.jpg)  
d

![](images/158da8bbce201e0c03cf5d690b8769320a416f3549d35d79d8ddb3fed460abbc.jpg)

![](images/32c1bd9e418b94bc2092af29b9e3fec228bdbc095f9de7e899d8d8279a0a0758.jpg)

![](images/f94e1769405bfbb76b7e038a0052098616d5398a9e07f514460fa9ad063d2b72.jpg)

![](images/11716b869bf98df2110f22df3ca53387e7536efbdc544c110424a2880a113d7b.jpg)  
e

![](images/af74b9e58d9f143af1726f751a1eafd8a6216cae7ff86e134d020129cae5da79.jpg)

f  
![](images/ac9d764176b62d02a7fd7ec3dc89b4408219f188b030aee61d7dd6b3ab99db01.jpg)

g  
![](images/49ce6e95518bb48bcebbae140734ae6e26b36236e013e9a6c935d01892dd90be.jpg)  
Extended Data Fig. 2 | See next page for caption.

![](images/8cae225eb2817a69afece981d8dc6cdc29b1f0ef3fdb3e4051bbfecb4caf2e05.jpg)

Extended Data Fig. 2 | Spatial profiling of gene expression in FF mouse embryo using DBiTplus. a Violin plot showing the number of detected genes/UMI counts per spatial spot from from two controls and two replicates FF E13 mouse embryo samples. All samples were downsampled to the same number of reads for comparison (99,000,000 reads). Box plots show the median (center line), the first and third quartiles (box limits) and 1.5x interquartile range (whiskers). b Brightfield image of E13 FF mouse embryo. Black box represents the region spatially barcoded during the DBiTplus workflow. Right: spatial mRNA and UMI count maps demonstrates average of 1,029 genes and 1,601 UMIs detected per 25 μm spot. c Pairwise correlation plots between replicates (DBiTplus workflow) and control (standard DBiT-seq workflow) showing the reproducibility of the DBiTplus workflow from a two-sided Pearson correlation test, with a Pearson correlation coefficient of 0.87 and 0.72 respectively. Pearson correlation between the two replicates is 0.84. For Replicate 2, 0.5% Triton X-100 was added to the RNase H to further improve cDNA release efficiency. d Spatial UMAP reveals 8 transcriptionally distinct clusters that align with anatomical features of the E13 mouse embryo. e Heat map of the top 5 differentially expressed genes per spatial cluster. f Validation of DBiTplus gene expression using independent reference datasets. In-situ Hybridization (ISH) staining image from the Allen Mouse Brain Atlas (Developing Mouse Brain - Age: E13.5, Theiler Stage: TS21) and gene expression from Mouse Organogenesis Spatiotemporal Transcriptomic Atlas (MOSTA) dataset (E13.5\_E1S2.MOSTA.h5ad). Scale bar 1 mm for Allen Mouse Brain Atlas images. g Gene Ontology (GO) enrichment analysis showing the biological process associated with E13 mouse embryos (cluster 0 from the standard DBiT-seq workflow and cluster 2 from DBiTplus workflow), both of which are associated with the embryonic diencephalon. Venn diagram shows the overlap of genes between the two clusters.

b  
![](images/75d614381e989eabcca9a139edc53d8b2f16d311f1a8c9a0f6727f1d5cf2dc68.jpg)  
Extended Data Fig. 3 | See next page for caption.

Extended Data Fig. 3 | Spatial profiling of gene expression in FFPE mouse embryo using DBiTplus. a UMAP showing 10 distinct clusters of DBiTplus spots/ spots. b Spatial distribution of the 10 clusters of DBiTplus spots. c Heat map showing the top 5 differentially expressed genes for each spatial cluster. d Spatial distribution of clusters 0, 1, and 2 alongside their principal defining genes. In-situ

Hybridization (ISH) staining image from the Allen Mouse Brain Atlas (Developing Mouse Brain - Age: E13.5, Theiler Stage: TS21) and gene expression from STOmics Mouse Organogenesis Spatiotemporal Transcriptomic Atlas (MOSTA) dataset (E13.5\_E1S1.MOSTA.h5ad). Scale bar 1.5 mm for Allen Mouse Brain Atlas images.

![](images/d6d7cd5e3b43b8b09e35b1fbf9f8b3c85828b80eda975eabcf115d1b37f043cc.jpg)

![](images/ef90ba6a2b1b54c2c13ff49ccbdba8fed2e2087cdb6f2add9524f8349a0b7f90.jpg)

a  
Label prediction test set assessment

<table><tr><td></td><td>precision</td><td>recall</td><td>f1-score</td><td>support</td></tr><tr><td>B_Cycling</td><td>0.66</td><td>0.81</td><td>0.72</td><td>26</td></tr><tr><td>B_GC</td><td>0.53</td><td>0.53</td><td>0.53</td><td>19</td></tr><tr><td>B_activated</td><td>0.84</td><td>0.70</td><td>0.76</td><td>410</td></tr><tr><td>B_mem</td><td>0.88</td><td>0.95</td><td>0.91</td><td>2229</td></tr><tr><td>B_naive</td><td>0.76</td><td>0.66</td><td>0.71</td><td>573</td></tr><tr><td>B_plasma</td><td>0.89</td><td>0.62</td><td>0.73</td><td>13</td></tr><tr><td>DC</td><td>0.92</td><td>0.91</td><td>0.91</td><td>74</td></tr><tr><td>Endo</td><td>0.99</td><td>0.96</td><td>0.97</td><td>117</td></tr><tr><td>ILC</td><td>0.88</td><td>0.82</td><td>0.85</td><td>34</td></tr><tr><td>Macrophages</td><td>0.67</td><td>0.62</td><td>0.64</td><td>13</td></tr><tr><td>Monocytes</td><td>0.95</td><td>0.98</td><td>0.96</td><td>55</td></tr><tr><td>NK</td><td>0.92</td><td>0.92</td><td>0.92</td><td>214</td></tr><tr><td>NKT</td><td>0.91</td><td>0.91</td><td>0.91</td><td>254</td></tr><tr><td>T_CD4+</td><td>0.89</td><td>0.92</td><td>0.90</td><td>1032</td></tr><tr><td>T_CD4+_naive</td><td>0.75</td><td>0.63</td><td>0.68</td><td>371</td></tr><tr><td>T_CD8+</td><td>0.93</td><td>0.93</td><td>0.93</td><td>816</td></tr><tr><td>T_CD8+_naive</td><td>0.77</td><td>0.72</td><td>0.75</td><td>260</td></tr><tr><td>T_Treg</td><td>0.86</td><td>0.90</td><td>0.88</td><td>407</td></tr><tr><td>VSMC</td><td>0.75</td><td>1.00</td><td>0.86</td><td>3</td></tr><tr><td>accuracy</td><td></td><td></td><td>0.87</td><td>6920</td></tr><tr><td>macro avg</td><td>0.83</td><td>0.81</td><td>0.82</td><td>6920</td></tr><tr><td>weighted avg</td><td>0.86</td><td>0.87</td><td>0.86</td><td>6920</td></tr></table>

![](images/82e13fd5e820ad36020a50799a58cf3a78aa505a20b24d2653a6bc0380fe69d6.jpg)

C  
![](images/80d8f5a369b5d8b50cdf599a1f13e853111fb96f8e243804f0ec36222f33d633.jpg)

![](images/14b1c6a36f83b309384db328276dde04aff0ba50a8a66a274483ba995d4db614.jpg)

y  
![](images/b408cf5c4afc85816d274e6079516341d336d8757723165ac37d7570c82a8800.jpg)

![](images/c4436ef2081e8358adae44686b5ac93ff1fe65bdca40ee176405e97ee3bdea10.jpg)  
d

![](images/0e0782f6f580121df8c586023c1cdc97358e53db50e37d93576e177bf0453297.jpg)

![](images/6dd3323183dace9e42ec8bae21f56339ff8576bba7c0c2f573f1a7f7a10c0d19.jpg)

![](images/6ef1509f6826bcc49d684b5fbe88edf47cd0a67b93cedb7dfb2b069a4901b348.jpg)

e

<table><tr><td></td><td>With CODEX</td><td>Without CODEX</td></tr><tr><td>ASW</td><td>0.47</td><td>0.46</td></tr><tr><td>ARI</td><td>0.21</td><td>0.09</td></tr></table>

## Extended Data Fig. 4 | Evaluation of cell type classification and

CODEX-informed deconvolution in FFPE human lymph node. a Label

prediction metrics (precision, recall, F1-score, and support) for immune and stromal cell types from the integrated CODEX and single-cell RNA-seq dataset. Highest F1-scores were observed for endothelial cells, macrophages, dendritic cells, and multiple B cell subsets. b Spatial distribution of annotated cell types across the entire lymph node tissue. c Left: Spatial expression patterns of key lineage markers - CD14 (myeloid lineage), CD20 (B cells), and CD3ε (T cells) derived from the CODEX dataset. Right: spatial plots showing subtypes corresponding to each major lineage, including T cell subsets, B cell subsets and myeloid populations. d Spatial deconvolution results from RCTD. Left: whole-slide deconvolution maps; middle: spot-level pie chart visualization of cell types; right: correlation heat map and histogram of distribution of correlations. e Performance metrics for CODEX-informed versus uninformed deconvolution.

![](images/b82c95c37d169a91c13e3f9827009c39e5660fd98be9040676486e0cd4f943cd.jpg)

b  
![](images/81572ee0d59faab14e689a75fa28b3b764afe2ed15c48a949ff894e85c170e2f.jpg)

![](images/f86db6e104268fb078e6e31d401a38ccd029c9387ea42748998978522cbab226.jpg)

![](images/4a06f3a2045207753160776ad40d4ed851d8fedd999dd776801a414542748ac4.jpg)

![](images/c2054ec1278308a922e5661f73e43b4fffc98be931cd4307ba90356790e6cb13.jpg)

![](images/185927caee4700a396d2c7ae4f95ecd6942aa4c2ea86a8d4a17ca41b454f7cac.jpg)

![](images/042aa02de9c4650b6389deb538504209e6e5b635cea3ba3b218eb226edf99335.jpg)

Extended Data Fig. 5 | Transcriptomic profiling and pathway analysis of B cells populations from FFPE human lymph node. a UMAP embedding from DBiTplus following CODEX-guided deconvolution reveals distinct immune and stromal cell populations, including naive B cells, activated B cells, cycling B cells, memory B cells, plasma B cells, and T cell subsets. b Heat map of differentially expressed genes across annotated cell types. c Violin plots of representative (canonical) marker genes for various B cell subtypes. d Volcano plots showing differentially expressed genes in naive (left) and activated (right) B cells compared to all other cells. Differential gene expression computed from two-sided Wilcoxon rank-sum test, adjusted P value on the basis of Bonferroni correction) e Pathway analysis comparing enriched pathways between naïve B cells and activated B cells. f Ingenuity Pathway Analysis (IPA) graphical summary showing predicated canonical pathways, upstream regulators and transcriptional and translational programs in activated B cells.

b  
![](images/8c9a75c69500235df8a744d9b8425c0c699e75984cdea2b505a9be7c25c07214.jpg)  
C

![](images/80df2de29fba4c7e0ecf33730ed270f27adaebbf7f5e56f13fc67031fb1939f0.jpg)

d  
![](images/54e7c13b3262d29b3ce557da7f42740080d9ba0c19f78a8316784d4c6597c02c.jpg)  
e

![](images/b84a6a12c41c6150e457cc066c33fb4a82a9ab3ceb817f5493c699b8d5156566.jpg)

f  
![](images/a7fa2e55f85660466c16924322cf88a2250ca50cbdd0c66a01bb82014d708f98.jpg)

g  
![](images/6b238201a1c6b2673f156a30b550ab7519f14619d54fee7f8e5f7c9db236a615.jpg)  
Extended Data Fig. 6 | See next page for caption.

![](images/7b9afa9429bfb6ef0574d0dd73086ca6e7d3991f97ec855510608ef4d2a26da0.jpg)

Extended Data Fig. 6 | Concordance of transcriptomic and protein-level data across DBiTplus and CODEX platforms, with spatial analysis of macrophages. a Venn diagram comparing 35 markers in the CODEX panel with corresponding gene expression data from DBiTplus. CD68 is the only protein marker without a corresponding gene transcript detected in DBiTplus. b Bar plot showing normalized expression of matched genes between DBiTplus lymph node (blue) and a Patho-DBiT reference lymph node (green). c Scatter plot showing correlation of log-transformed gene expression between DBiTplus (n = 1) and Patho-DBiT reference lymph node sample (n = 1). Each dot represents a gene, the red line indicates linear regression fits and the shaded gray area indicates the 95% confidence interval for the regression line. The correlation analysis is from a two-sided Pearson correlation test. Strong concordance observed (Pearson $\mathsf { R } = 0 . 8 9 , p < 2 . 2 \times 1 0 ^ { - 1 6 } )$ . d Correlation between protein expression

(CODEX) and gene expression (DBiTplus) across matched markers. Each dot represents a gene, the red line indicates linear regression fits and the shaded gray area indicates the 95% confidence interval for the regression line. Correlation analysis from a two-sided Pearson correlation test. Weak but positive association $( \mathsf { R } = 0 . 2 3 , p = 0 . 1 8 )$ ). e Multiplexed CODEX image showing CD68<sup>+</sup> macrophages within the lymph node architecture (blue: DAPI, green: CD68). Zoomed-in region highlights macrophage-rich zones. f Spatial feature plot showing the expression pattern of CD68 in the CODEX dataset. g Comparative visualization of CD14 and CD163 expression in both CODEX (top row, protein) and DBiTplus (bottom row, RNA), showing similar spatial enrichment patterns. h Spatial distribution of macrophages as identified from CODEX-guided DBiTplus cell type deconvolution.

![](images/b6112cd7406144fdbe739d7e2be6ee3d453f05af9ec887aa983718fcfd4bc5e2.jpg)

![](images/c54e79d76e9909771bd971f325ddc4cbbf2cbfb8763dbadc835a6a1f4b971702.jpg)

![](images/025b5b7e63934ad25d8d900f5909a44c0e6d38215612e2a11bc59bb91ecbd1ab.jpg)

![](images/0c4d918f4cc4535c09873c43898945025d0cecfc7c8efa71e67735ee82ca1dcd.jpg)

![](images/20a3a8899d99384cb18d49e8c6d5ff16d98762cfac5c86c0387e35483924cfcb.jpg)  
g

![](images/6f9b789c7cf6c6518cb823d6253e3fd3d90560a1fa570e0f786ead27ff149204.jpg)

![](images/c0808ecd55479713856294643e418744c5639b001efae36497557d7128ddb4a5.jpg)

![](images/caf5695d4a8e02b375f57a41cc65f5c97e19f957be551c54293e607858d9059c.jpg)  
J

![](images/7d715a0130465ea5c313a0b9a44235b63c916a3cecba7c56e8dbd1bda75cbc0d.jpg)  
Extended Data Fig. 7 | See next page for caption.

![](images/0691f5c6672c701ea11465268e8960b519626b5601f3e7b639ab17bd2e06af63.jpg)

Extended Data Fig. 7 | Transcriptional and regulatory landscape of B cell transformation. a Heat map of top differentially expressed genes across annotated cell types from the spatial transcriptomics dataset. b–c, Volcano plots highlighting differentially expressed genes in small B cells (b) and large B cells (c) compared to all other cell types. Differential gene expression computed from two-sided Wilcoxon rank-sum test, adjusted P value on the basis of Bonferroni correction) d, IPA-inferred upstream regulator network predicting TF-driven control over gene expression changes in tumor B cells. e Activation z-scores of top predicted upstream regulators of genes from pathway analysis. f Causal

network diagram centered on MYC, highlighting upstream regulation from SOX4 through the AKT family. g Activation z-scores vs. –log<sub>10</sub>(p-values) from causal network analysis showing predicted activators (red) and inhibitors (blue). z-score ≤ -2 (significantly inhibited) and z-score ≥ 2 (significantly activated). P-values calculated using the right-tailed FET (Fisher’s Exact Test). h Expanded regulatory network involving of SYK, a key upstream regulator of multiple genes in lymphoma transformation. i Monocle3 UMAP embedding showing four key genes. j Pseudotime heat map trajectories of selected genes reveal temporal dynamics of MZL.

a  
![](images/a7e1b83cf5c87458a9a6f4b54cfa3772ad5f664dd9fa29ab204b5e004184edfe.jpg)

![](images/b96c30885489b18ce9d53a8a4822846be4b4eaac2cb8d178e37dc3bee0d33445.jpg)  
C

<table><tr><td>Category</td><td>Markers</td></tr><tr><td>B Cells (CLL &amp; DLBCL)</td><td>CD19, CD20, CD23, CD5, LEF1, CD38, CD138, Ki-67</td></tr><tr><td>T Cells &amp; Immune Checkpoint</td><td>CD3, CD4, CD8, CD45RO, CD45RA, FoxP3, GranzymeB, CD279 (PD1), CD274 (PD-L1), CD45</td></tr><tr><td>Stromal/Endothelial/Myeloid</td><td>CD31, CD34, CD105, Col IV, Podoplanin, CD68, CD163, B-Catenin</td></tr><tr><td>Segmentation</td><td>DNA, ATP1A1, LaminB1, B2M</td></tr></table>

![](images/abed3ffbfbb431e387fd99f02b2510f993a4735d7bdda678cbb237712658a63d.jpg)  
d

![](images/1595315947e7d1127bb667c38dca2535ba184bcdc7e7a1150f0a936e78c985c9.jpg)

e  
![](images/88ba61e64f7e24fdcca41cbb56bdd80e02ee8e0b5ed1dc91011f844d41887df7.jpg)

![](images/ee016e4c221e1af2c13db75f0e044885828359127184fe02388cc537044e2717.jpg)

![](images/53990cfdc87b049641f9a0f00849bba4b28b1914734979cdc02af21b9f9217c1.jpg)

![](images/5182e803e3103cce82d3732e251df954b821e1c99d21ffd7f923279692f8eb8d.jpg)

![](images/50fc0674da47d0015e656f94f9cb423810b0244b05bd573306f443d90807680d.jpg)

![](images/5d93eaed817c1579402f023c07112f9b3c5fbbe91c25231ff535aac4506311a7.jpg)

![](images/686195224032326d42f0cd0073e99cc3bc0c3ca53d37382590a2a55fc63c85dc.jpg)

![](images/cefa088086a07d8d21e5b7f6b72b5ceec80ea392122d88708d819ebe81ba84f5.jpg)

![](images/1f134d7104b662daddb8b80c0eceac62c80a9de91fbaceaf1709ee3bfc7b961f.jpg)

![](images/3f3bc260fa82d6df2f8944bac13edb7a2827afbff96e7ab8da311b263851a7a3.jpg)  
Extended Data Fig. 8 | See next page for caption.

![](images/c172d1be394e645c511ff258f6342be3d38a0c2f80f8f1553eb7f53cdcd1daa7.jpg)

![](images/70ede0b2eaca4f69665719a3d6efd373eee7b4c67a179f4fa208577bb9c38dd8.jpg)

Extended Data Fig. 8 | Spatial proteomic profiling of Richter’s Transformation. a Representative high-resolution images of DLBCL (top) and CLL (bottom) regions showing differences in cell size (n = 1). b Schematic of the DBiTplus workflow using CellScape on an FFPE tissue section. Created with BioRender. com. c Protein marker panel used in CellScape, including immune, stromal, and segmentation markers. d Stacked barplot showing cell type composition in CLL and DLBCL regions. e Boxplot where the central line represents the median, the bottom and upper edges of the box indicate the first and third quartiles, and the whiskers extend to the most extreme data points within 1.5 times the interquartile range (IQR) from the box edge for the quantification of average T cell-tumor cell distances in DLBCL compared to CLL. Computed using a two-tailed Mann-Whitney test (\*\*\*\* represents $> < 0 . 0 0 0 1 , \mathrm { n } _ { \mathrm { c u L } } = 5 , 5 2 5$ and $\mathsf { n } _ { \mathsf { D L B C L } } = 4 , 9 2 4 \rangle$ ). Median distance 7.715 µm and 7.292 µm, respectively for DLBCL and CLL. f Violin plots of the distance of T cell subtypes from tumor cells in DLBCL versus CLL regions. Violin plots show the median (center line), the first and third quartiles (box limits) and 1.5x interquartile range (whiskers). g Boxplot, where the central line represents the median, the bottom and upper edges of the box indicate the first and third quartiles, and the whiskers extend to the most extreme data points within 1.5 times the interquartile range (IQR) from the box edge showing size distribution across all major annotated cell types. h Histogram of cell size distributions comparing large B cells (DLBCL) and small B cells (CLL). Histogram bin width of 0.25 i Spatial maps showing localization of large B cells (red) and small B cells (blue) within the tissue section (left), and CLL cells only (right). j, 2D density scatter plot showing CD20 and Ki67 expression as a function of cell size in large B cells (left) versus other B cells (right). Small B cells < 300 in size and < 0.30 in normalized Ki67 expression were annotated as CLL-like cells. k, Density distribution plots of marker expression (CD23, CD5, LEF1) in small (top) and large B cells (bottom). l Spatial maps showing localization of CLL-like cells.

a  
CD19 Expression Gradient  
![](images/62935b8077abf04efe9d8c5e8a5321f6480a04675995b67d83cdd73f905209d2.jpg)  
FOXP3 Expression Gradient

CD68 Expression Gradient  
![](images/00f9e98b208f0de118980991f5d1cf8572d8f68fd48f2e5a0ab7aa509ed645ec.jpg)  
Ki67 Expression Gradient

CD279 Expression Gradient  
![](images/acee6ba48d5717e1d548809f8c037821b51fc0e99c5c75d4f6bf2baedd5c3ab9.jpg)

![](images/a50e897af6e6922ef50a94cad8ce801df213ce8ff5a1053d2e96e4fe79ad429c.jpg)

GranzymeB Expression Gradient  
![](images/d139d1c659a877edbcaea5fc688ef7510b041992ea4d6b52209214fbd02ee137.jpg)

![](images/be93bf31dd884f610e9ce7cf6da6fa07b18fdf5b56651ed36f71bc6227160160.jpg)

![](images/a4ee6c1a2d1012f9c46105959da9d34c8e66d5f1a5062235eb03fca6b62f15c9.jpg)

d  
![](images/2ab85e874ffa39515184b6fad0f1b983a3edbb075e942f48c8c899d9a375a1b6.jpg)

e  
![](images/66e5f535e448a20829a4d01431ff49b8547ccc9b90303250a790fb2d19f8ed21.jpg)

![](images/d3e9593814c271fae08c5a1e8fe9878630d49461e56e88b1b0dd0efe93991ee4.jpg)  
f  
Extended Data Fig. 9 | See next page for caption.

![](images/e7db70bdaabfb9125102314ccc151662f95895684e3ebd92a6f414efe1e4991f.jpg)

Extended Data Fig. 9 | Spatial gradient expression and molecular features of Richter’s Transformation. a Spatial expression gradients for representative protein markers across the tissue section reveal distinct spatial localization (within CLL or DLBCL regions) patterns of B cells (CD19), macrophages (CD68), immune checkpoints (CD279/PD-1, FOXP3), proliferating cells (Ki67), and cytotoxic activity (GranzymeB). b UMAP plot showing unsupervised clustering of annotated cell type across the lymphoma tissue. c Heat map of top differentially expressed genes across all cell types. d Volcano plot showing DEGs between large B cells (DLBCL) and small B cells (CLL), with key upregulated genes in each population highlighted. Differential gene expression computed from two-sided Wilcoxon rank-sum test, adjusted P value on the basis of Bonferroni correction e Heat map of top 30 DEGs distinguishing large B cells from small B cells. f Ingenuity Pathway enrichment analysis of large B cells.

![](images/dd2a9c2823f71750ee67f449c4f775e24900e6d1222036567aa594fe6d669278.jpg)

![](images/3a9750a2729c084e09499e5b1396e2cf3a15ef23f1f74db3ad4de818cefd2a39.jpg)

![](images/3961d3b33f43b116d346fad9dbb34abe287e3009f17d59898108150aa0f0d979.jpg)

![](images/57e98a7ce7cd81a744e9424abfb16706922d6f49d4c4befd6e4b8b081f866475.jpg)

d  
![](images/ce1f007576310340c8eb1c3b5fab28f14830d420ea00241c1e9fe5df62cda963.jpg)

![](images/73b75e3597f4eb566ecaa054e045438bfe61294f613dd4a94e2ebc66b7f60cba.jpg)

![](images/34dabeb5cbd2e685de1def28460f14acb09f4d2f3fe0f0e4e0aae5239625a3b6.jpg)

![](images/5859ad32d29d6fc993650dccd0bc5875df30d7666f618e20fc97e9d276f2f2e1.jpg)

![](images/ba719c5fe621e2ef5f47fb15062d138e327b1079b5532b9fcd41fd02f9701f57.jpg)

![](images/7b7520857e04b1a0b235c51b11440b29f8ba73b869cbf05f99be4f5b96403845.jpg)

![](images/e4dfae5e0aa917d96fc7edcb7cbee85ac14ed17e97beed98aeb73bafd9950e94.jpg)

![](images/b0809379ad12f8343eac4aa9e7d455a64d0184b3119d629453ad437be9e8fd13.jpg)  
Extended Data Fig. 10 | See next page for caption.

![](images/13c3152ee2054f8dd75a9fd0ef9d854f991c67a7654b99523a5674e39b8cb7fd.jpg)

Extended Data Fig. 10 | Analysis of microRNAs, transcriptional pathways and pathway dynamics in Richter’s Transformation. a Distribution of microRNAs and corresponding UMI counts per spatial pixel. Dashed lines indicate the average number of microRNAs or UMI counts. b Spatial clustering of clusters 0 and 1 whose spatial distributions mirrored CLL and DLBCL regions from histological staining of Richter’s transformation sample. c Differentially expressed microRNAs between clusters 0 and 1. Differential gene expression computed from two-sided Wilcoxon rank-sum test, adjusted P value on the basis of Bonferroni correction) d Spatial mapping of select microRNAs implicated in lymphoid malignancies. e–g, Monocle3 UMAP visualization of large B cells and small B cells e showing distinct partitions in transcriptomic space f Monocle3 UMAP visualization of small B cells g Monocle3 pseudotime UMAP highlighting a dynamic trajectory. h Pseudotime heat map expression dynamics of genes associated with transformation, including anti-apoptotic regulators (BCL2, BIRC3), proliferation (MKI67), and key signaling nodes (ATM, LEF1, TCL1A). i Heat map of pathway-associated gene expression (z-score) across pseudotime reveals coordinated activation of DNA damage response, chromatin modifiers, and NF-κB and MAPK-ERK signaling, consistent with progressive transformation.

# nature portfolio

Corresponding author(s): Rong Fan, Mina Xu, Zongming Ma

Last updated by author(s): Oct 4, 2025

## Reporting Summary

Nature Portfolio wishes to improve the reproducibility of the work that we publish.This form provides structure for consistency and transparency in reporting.For further information on Nature Portfolio policies,see our Editorial Policies and the Editorial Policy Checklist.

## Statistics

Forall statistical analyses,confirm that the following items are present in the figure legend,table legend,main text,or Methods section.

n/a| Confirmed

□区 The exact sample size(n)for each experimental group/condition, given as a discrete number and unit of measurement

□区 A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly

区

□区A description of all ovariates tested

区Adescription of any assumptions or corrections,such as tests of normality and adjustment for multiple comparisons

A

For Bayesian analysis,information on thechoice of priors and Markovchain Monte Carlo settings

For hierarchical andcomplex designs,identificationof the appropriate levelfor tests and fullreporting of outcomes

Estimates of effect sizes (e.g. Cohen's d,Pearson’s ),，indicating how they were calculated

Our web collection on statistics for biologists contains articles on many of the points above.

## Software and code

Policy information about availability of computer code

Data collection Akoya Biosciences PhenoCycler Fusion System,Agilent TapeStation 415O,Ilumina NovaSeq X Plus System,Ilumina NovaSeq 6O00 System, Bruker Spatial Biology CellScape System,M7OOO Imaging EVOS System,Motic EasyScan digital slide scanner

Data analysis

STAR V2.7.8a,ST\_Pipeline V1.8.1, Seurat V4.3.O, Seqkit version 2.3.1,Ingenuity Pathway Analysis (IPA, QlAGEN,Version O1-23-O1),Prism V10, R version 4.2.0, RStudio Server version: v2024.12.1, ASTRO Pipeline(Zhang, D.et al.ASTRO: Automated Spatial Whole-Transcriptome RNA-Expression Workflow (Cold Spring Harbor Laboratory, 2O25).The code for the analyzing the processed multiplexed immunofluorescence imaging datasets and the sequencing datasets are archived at Zenodo (https://zenodo.org/records/16814952)and also available at GitHub (https://github.com/Janezjz/DBiT-plus).

## Data

Policy information about availability of data

All manuscripts must include a data availability statement.This statement should provide the following information, where applicable:

\- Accession codes, unique identifiers,or web links for publicly available datasets

\- A description of any restrictions on data availability

\- For clinical datasets or third party data,please ensure that the statement adheres to our policy

Raw and processed data reported are deposited in the Gene Expression Omnibus (GEO) with accession GSE3o8167. The resulting fastq files were aligned to the mouse reference genome (GRCm39) or human reference genome (GRCh38).Multiplexed immunofluorescence imaging datasets and Histological images are available at https://zenodo.org/records/17153112 and https://zenodo.org/records/17153187.Published data for data comparison are available online at STOmicsDB Mouse Organogenesis Spatiotemporal Transcriptomic Atlas (MOSTA) dataset (E13.5\_E1S2.MOSTA.h5ad). (https://db.cngb.org/stomics/mosta/spatial/) and Allen Mouse Brain Atlas (Developing Mouse Brain -Age: E13.5,Theiler Stage:TS21)at link: https://developingmouse.brain-map.org/).Patho-DBiT reference lymph node data is available on GEO under accession number GSE274641; sample GSM8454083).

## Research involving human participants, their data, or biological material

Policy information about studies with human participants or human data. See also policy information about sex,gender(identity/presentation) and sexual orientation and race, ethnicity and racism

Reporting on sex and gender

Not relevant to this study

Reporting on race,ethnicity,or other socially relevant groupings

Not relevant to this study

Population characteristics

Not relevant to this study

Recruitment

Not relevant to this study

Ethics oversight

De-identified archived formalin-fixed parafin-embedded (FFPE) human reactive lymph node and lymphoma tissue blocks were obtained from Yale Pathology Tissue Services (YPTS).The tissue retrieval and distribution for research was conducted with the approval of the Yale University Institutional Review Board (Approved IRB #14O1013259) and oversight by the Tissue Resource Oversight Committee.Written informed consent for participation in any cases where identification was collected alongside the specimen,was obtained from patients or their guardians,in accordance with the principles of the Declaration of Helsinki. Each sample was handled in strict compliance with HIPAA regulations, University Research Policies, Pathology Department diagnostic requirements,and Hospital by-laws.

## Field-specific reporting

Please select the one below that is the best fit for your research.If you are not sure,read the appropriate sections before making your selection.

区Life sciences

For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf

## Life sciences study design

<table><tr><td>Sample size</td><td>The goal of this study was to develop a new spatial omics technology. Sample size calculation was not performed as samples sizes were chosen primarily based on experiment length, sequencing costs and tissue types. The current manuscript mainly described a new method for the joint profiling of the transcriptome and proteome within the same slide and at single-cell resolution. The number of samples included in the study are sufficient to serve as a proof-of-concept for the new technology.</td></tr><tr><td>Data exclusions</td><td>No data were excluded.</td></tr><tr><td>Replication</td><td>Experiments on the mouse embryo samples were replicated. After demonstrating the reproducibility of the new technology, the subsequent experiments were performed once to serve as a proof-of-concept for the new technology.</td></tr><tr><td>Randomization</td><td>There are no defined sample groups so randomization was not particularly applicable in this study</td></tr><tr><td>Blinding</td><td>There are no defined sample groups so blinding was not particularly applicable in this study</td></tr></table>

Materials & experimental systems

## Reporting for specific materials, systems and methods

<table><tr><td>n/a</td><td>Involved in the study</td><td>n/a</td><td>Involved in the study</td></tr><tr><td>□</td><td>Antibodies</td><td>□</td><td>ChIP-seq</td></tr><tr><td>□</td><td>Eukaryotic cell lines</td><td>□</td><td>Flow cytometry</td></tr><tr><td>□</td><td>Palaeontology and archaeology</td><td>□</td><td>MRI-based neuroimaging</td></tr><tr><td>□</td><td>Animals and other organisms</td><td></td><td></td></tr><tr><td>□</td><td>Clinical data</td><td></td><td></td></tr><tr><td>□</td><td>Dual use research of concern</td><td></td><td></td></tr><tr><td>□</td><td>Plants</td><td></td><td></td></tr></table>

## Antibodies

<table><tr><td>Antibodies used</td><td>Cat No Target Clone Source4250098 Bcl-2 EPR17509 Akoya Biosciences4450040 Beta-actin W16197A Akoya Biosciences4550119 CD3e EP449E Akoya Biosciences4550112 CD4 EPR6855 Akoya Biosciences4250012 CD8 C8/144B Akoya Biosciences4550114 CD11c 118/A5 Akoya Biosciences4450047 CD14 EPR3653 Akoya Biosciences4450018 CD20 L26 Akoya Biosciences4450027 CD21 EP3093 Akoya Biosciences4450017 CD31 EP3095 Akoya Biosciences4550133 CD34 QBEND10 Akoya Biosciences4250057 CD34 QBEND10 Akoya Biosciences4450041 CD44 156-3C11 Akoya Biosciences4250099 CD45 D9M8I Akoya Biosciences4250023 CD45RO UCHL1 Akoya Biosciences4250087 CD56 CAL53 Akoya Biosciences4550113 CD68 KP1 Akoya Biosciences4450078 CD79a D1X5C Akoya Biosciences4550098 CD107a H4A3 Akoya Biosciences4250097 CD141 E7Y9P Akoya Biosciences4250079 CD163 EPR19518 Akoya Biosciences4550122 Collagen IV EPR20966 Akoya Biosciences4250021 E-cadherin 4A2C7 Akoya Biosciences4450088 EpCAM D9S3P Akoya Biosciences4550071 FOXP3 236A/E7 Akoya Biosciences4250055 Granzyme B D6E9W Akoya Biosciences4450046 HLA-A EP1395Y Akoya Biosciences4550118 HLA-DR EPR3692 Akoya Biosciences4250065 HLA-E MEM- E/02 Akoya Biosciences4550117 ICOS D1K2T Akoya Biosciences4550123 IDO1 V1NC3IDO Akoya Biosciences4250062 IFNG EPR21704 Akoya Biosciences4250073 iNOS SP126 Akoya Biosciences4250019 Ki67 B56 Akoya Biosciences4550058 LAG3 EPR20261 Akoya Biosciences4450034 Mac2/Galectin-3 M3/38 Akoya Biosciences4250083 MPO E1E7I Akoya Biosciences4450020 Pan-Cytokeratin AE-1/AE-3 Akoya Biosciences4550124 PCNA PC10 Akoya Biosciences4550038 PD-1 D4W2J Akoya Biosciences4550072 PD-L1 73-10 Akoya Biosciences4250004 Podoplanin NC-08 Akoya Biosciences4250094 Podoplanin NC-08 Akoya Biosciences4450049 SMA 1A4 Akoya Biosciences4250075 SOX2 SP76 Akoya Biosciences4250061 TIGIT BLR047F Akoya Biosciences4250067 TOX E6I3Q Akoya Biosciences4450050 Vimentin 091D3 Akoya Biosciences4250063 VISTA D1L2G Akoya Biosciences</td></tr></table>

<table><tr><td>PA5-28827 CXCL13 - ThermoFisher Scientific552032 CXCR5 RF8B2 BD BiosciencesPA5-14259 BCL6 - ThermoFisher Scientific</td></tr><tr><td>Mouse antibodies (Also from Akoya Biosciences)</td></tr><tr><td>Antibody Clone ReporterCD90 30-H12 RX001-A488CD31 MEC13.3 RX002-ATTO550TCR H57-597 RX003-Cy5Ter119 TER-119 RX004-A488CD44 * IM7 RX005-ATTO550EmptyCD45 30-F11 RX007-A488CD19 6D5 RX020-ATTO550CD169 3D6.112 RX015-Cy5CD45R/B220 RA3-6B2 RX010-A488MHCII M5/114.15 RX014-ATTO550CD3 17A2 RX021-Cy5IgM RMM-1 RX013-A488CD5 53-7.3 RX017-ATTO550Ly6g 1A8 RX024-Cy5CD38 90 RX019-A488CD21/35 7E9 RX023-ATTO550CD71 RI7217 RX027-Cy5IgD 11-26c.2a RX016-A488CD4 RM4-5 RX026-ATTO550CD11c N418 RX030-Cy5CD24 M1/69 RX022-A488CD8a 53-6.7 RX029-ATTO550CD49f GoH3 RX033-Cy5CD11b M1/70 RX025-A488Ki67 * B56 CX047-ATTO550</td></tr><tr><td>CellScape system used the Vistaplex Antibody panel: CD19, CD20, CD23, CD5, LEF1, CD38, CD138, Ki-67CD3, CD4, CD8, CD45RO, CD45RA, FoxP3, GranzymeB, CD279 (PD1), CD274 (PD-L1), CD45CD31, CD34, CD105, Col IV, Podoplanin, CD68, CD163, B-CateninDNA, ATP1A1, LaminB1, B2M. The following were not available used in Bruker&#x27;s Vistaplex Antibody panel and were purchased from a commercial vendor.Antibody Clone VendorCD5 4C7 LeicaCD23 1B12 LeicaLEF1 EPR2029Y Abcam</td></tr><tr><td>Details of antibody dilutions and imaging cycles are included in supplementary file on imaging panel details</td></tr><tr><td>Commercial antibodies were validated for reactivity by the vendors. Antibodies conjugated in-house for use in CODEX were conjugated following Akoya Biosciences&#x27; antibody conjugation protocol (https://www.akoyabio.com/wp-content/uploads/2020/04/Antibody-Screening-and-Custom-Conjugation.pdf and https://www.akoyabio.com/wp-content/uploads/AbConjugation-Kit-for-PhenoCode-Signature-Protocol.pdf)</td></tr></table>

## Animals and other research organisms

Policy information about studies involving animals; ARRIVE guidelines recommended for reporting animal research,and Sexand Gender in Research

<table><tr><td colspan="2">Research</td></tr><tr><td>Laboratory animals</td><td>All mice tissue used were C57BL/6 mice obtained from a commercial vendor, Zyagen (San Diego, CA).</td></tr><tr><td>Wild animals</td><td>No wild animals were included in this study</td></tr><tr><td>Reporting on sex</td><td>Not relevant to this study</td></tr><tr><td>Field-collected samples</td><td>No field-collected samples were included in this study</td></tr><tr><td>Ethics oversight</td><td>The mouse tissue used in this study was obtained from a commercial vendor, Zyagen (San Diego, CA), which procured and handled the animals under their in-house institutional IACUC-approved protocols.</td></tr></table>

## Plants

Seed stocks

No seed stocks were used in this study

Novel plant genotypes

No plants were included in this study

Authentication

Not relevant to study