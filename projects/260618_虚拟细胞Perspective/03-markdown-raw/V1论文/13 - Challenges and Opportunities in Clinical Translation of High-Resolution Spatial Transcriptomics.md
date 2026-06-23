# Annual Review of Pathology: Mechanisms of Disease Challenges and Opportunities in the Clinical Translation of High-Resolution Spatial Transcriptomics

## REVIEWS CONNECT

![](images/6291bc7e07b3511807d00a51b06fd6012e3c6675750d9bb908591cf40e082b78.jpg)

www.annualreviews.org

·Download figures

·Navigate cited references

· Keyword search

·Explore related articles

· Share via email or social media

Annu. Rev. Pathol. Mech. Dis. 2025. 20:405–32

First published as a Review in Advance on October 30, 2024

The Annual Review of Pathology: Mechanisms of Disease is online at pathol.annualreviews.org

https://doi.org/10.1146/annurev-pathmechdis-111523-023417

Copyright © 2025 by the author(s). This work is licensed under a Creative Commons Attribution 4.0 International License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited. See credit lines of images or other third-party material in this article for license information.

ACCESSBY

Tancredi Massimo Pentimalli,<sup>1,2</sup> Nikos Karaiskos,<sup>1</sup> and Nikolaus Rajewsky<sup>1,2,3,4,5,6</sup>

<sup>1</sup>Laboratory for Systems Biology of Regulatory Elements, Berlin Institute for Medical Systems Biology, Max Delbrück Center for Molecular Medicine in the Helmholtz Association, Berlin, Germany; email: tancredimassimo.pentimalli@mdc-berlin.de, nikolaos.karaiskos@mdc-berlin.de, rajewsky@mdc-berlin.de

<sup>2</sup>Charité – Universitätsmedizin Berlin, Berlin, Germany

<sup>3</sup>German Center for Cardiovascular Research (DZHK), Berlin, Germany

<sup>4</sup>NeuroCure Cluster of Excellence, Berlin, Germany

<sup>5</sup>German Cancer Consortium (DKTK), Berlin, Germany

<sup>6</sup>National Center for Tumor Diseases, Berlin, Germany

## Keywords

spatial transcriptomics, molecular pathology, cell–cell communication, disease mechanism, personalized medicine, artificial intelligence

## Abstract

Pathology has always been fueled by technological advances. Histology powered the study of tissue architecture at single-cell resolution and remains a cornerstone of clinical pathology today. In the last decade, next-generation sequencing has become informative for the targeted treatment of many diseases, demonstrating the importance of genome-scale molecular information for personalized medicine. Today, revolutionary developments in spatial transcriptomics technologies digitalize gene expression at subcellular resolution in intact tissue sections, enabling the computational analysis of cell types, cellular phenotypes, and cell–cell communication in routinely collected and archival clinical samples. Here we review how such molecular microscopes work, highlight their potential to identify disease mechanisms and guide personalized therapies, and provide guidance for clinical study design. Finally, we discuss remaining challenges to the swift translation of high-resolution spatial transcriptomics technologies and how integration of multimodal readouts and deep learning approaches is bringing us closer to a holistic understanding of tissue biology and pathology.

## BACKGROUND

Technological innovation is a driving force of breakthroughs in medicine. For example, microscopy has been one such disruptive technology, enabling the analysis of tissue architecture at single-cell resolution and playing a central role in the development of modern pathology. In the 19th century, early spatial investigations of healthy and diseased tissues by Rudolf Virchow and others revealed how alterations in cellular ecosystems give rise to diseases (1). Today, histology is still at the cornerstone of clinical pathology, underlying the power of tissue morphology in discriminating between different disease entities, predicting patient outcomes, and guiding treatment decisions.

Nevertheless, linking tissue architecture and the underlying (dys)function is far from trivial. In fact, the identification of disease mechanisms and therapeutic targets greatly benefited from molecular readouts about tissue genetic makeup, gene expression, and protein levels. In 2003, the completion of the Human Genome Project (2) represented a turning point in molecular biology, fostering the development of high-throughput assays that can simultaneously assess entire genomes, epigenomes, and transcriptomes. Such next-generation sequencing (NGS) technologies then became the foundation for precision medicine, enabling accurate diagnosis and personalized treatment strategies. Especially in oncology, NGS approaches refined tumor molecular subtyping, improved treatment efficacy, and reduced treatment-related side effects (3). NGS technologies thus represent another prime example of the impact that novel technologies have on clinical care. However, current applications mostly rely on bulk readouts, which average gene expression across millions of cells from different cell types and are unable to distinguish clinically relevant disease heterogeneity.

Next-generation sequencing (NGS): high-throughput DNA sequencing methods for rapid, cost-effective analysis of nucleotide sequences

Omics: large-scale studies of biological molecules or systems, such as genomics, transcriptomics, proteomics, or metabolomics

In the last decade, an ever-growing arsenal of single-cell omics emerged as powerful tools in biomedical research, providing more and more detailed information about cellular molecular biology. Highly parallel, multiomic profiling of cellular genomes, epigenomes, and transcriptomes revolutionized our ability to characterize cellular heterogeneity (4), identifying rare cell types and uncovering a multitude of cellular phenotypic states (5). Single-cell omics enabled the precise reconstruction of cellular trajectories and lineages in development, homeostasis, and disease of tissues and even whole organisms (6). Analyzing experimental models and clinical samples at single-cell resolution revealed the diversity and remodeling of disease-related cell types and molecular states with important implications for patient stratification and personalized therapy. As an example, the LifeTime initiative launched in 2022 aims to leverage single-cell technologies for mapping how cells deviate from their healthy trajectory toward disease states, enabling the early detection and timely interception of complex diseases (7).

Tissue dissociation: process of breaking down tissue into single cells while preserving molecular integrity for analysis

Despite the power of single-cell technologies, the need for tissue dissociation and the lack of standardized protocols for isolating living cells have so far limited their clinical translation on a broader scale (8). With the exception of hematology, where standardized protocols were already introduced in the 1980s for flow cytometry, single-cell applications have so far remained mostly confined to the research space. Furthermore, tissue dissociation can alter both cellular (e.g., depletion of specific cell types) and molecular readouts [e.g., activation of stress responses (9)], hindering the development of robust and reproducible protocols needed for clinical applications. While single-nucleus extraction from fresh-frozen (FF) (10, 11) and, recently, formalin-fixed paraffin-embedded (FFPE) (12) clinical samples represents a promising alternative to living cell isolation, tissue dissociation inevitably leads to the loss of spatial information. However, the spatial organization of cells in complex tissues is central to understanding how molecular phenotypes emerge, are regulated, and affect tissue function (13). While computational tools for the spatial reconstruction of single-cell data with little or no prior knowledge exist (14–16), they rely on the assumption that transcriptomic profiles in neighboring cells are more similar than those that are farther apart, which does not always hold true when tissue organization is disrupted by diseases. Finally, local interactions in cellular neighborhoods drive coordinated cellular processes, and the loss of spatial positions following tissue dissociation prevents their mapping, limiting our mechanistic understanding of disease processes.

In recent years, novel technologies for quantifying RNA and protein abundance in intact tissues emerged, bridging the gap between histology and single-cell omics. Such spatial omics are rapidly expanding and now enable the systematic investigation of the molecular phenotypes of millions of cells in their tissue context (17). In particular, high-resolution spatial transcriptomics (ST) technologies, which profile billions of individual transcripts at subcellular resolution (18), enable the systematic mapping of cell–cell interactions in clinical samples and hold great potential to advance biomedical research and patient care (19).

Given that low-resolution ST approaches, which aggregate transcriptomic readouts across tens of neighboring cells, do not allow single-cell resolved analysis and have been extensively reviewed elsewhere (20, 21), here we focus on high-resolution methods and their clinical usefulness. By charting cell–cell interactions and disease-related molecular phenotypes in clinical samples, these molecular microscopes are bringing us closer to a mechanistic understanding of disease processes. In the same way that hematology was primed for the translation of single-cell omics, we argue that pathology will champion the initial adoption of high-resolution spatial omics, as standardized protocols for tissue collection, processing, and morphological analysis are already in place worldwide. Importantly, the clinical translation of high-resolution ST methods is accelerated by their compatibility with FFPE samples, enabling the retrospective analysis of large archived clinical cohorts and the personalized reconstruction of therapeutic responses from longitudinal samples.

In this review, we present early preclinical studies showcasing the potential of high-resolution ST to inform mechanism-based personalized therapies, identify novel therapeutic targets, and bring us closer to a holistic understanding of tissue biology. As large-scale clinical studies are urgently needed to link spatial biomarkers with patient outcomes, we present key considerations for the design of clinical ST projects and discuss current challenges to the swift clinical translation of these methods. Finally, the digitalization of both cellular transcriptomics and morphologies is generating the matched molecular and histological data needed to train the next generation of predictive deep learning algorithms in pathology, opening up exciting avenues for the prediction of spatial biomarkers from routine hematoxylin and eosin (H&E) images. This will not only increase accessibility of patients worldwide to molecular-directed therapies but also reveal which histological features are predictive of specific gene-expression patterns, shedding light on the intricate relationship between tissue structure and function.

## HIGH-RESOLUTION SPATIAL TRANSCRIPTOMICS TECHNOLOGIES

High-resolution ST technologies aim to localize individual transcripts at subcellular resolution in intact tissues. Existing approaches are classified into imaging-based and sequencing-based methods, relying on either direct imaging or sequencing of spatially barcoded molecules, respectively. As comprehensive comparisons of the different ST technologies have been performed elsewhere

## Cellular

neighborhoods: regions in tissue where cells interact closely, influencing their gene expression profiles and functional properties

High-resolution spatial transcriptomics (ST) technologies: methods that provide readouts at cellular or even subcellular resolution (i.e., at approximately or less than 10 µm)

## Supplemental Material >

(22), here we focus on their functioning principles (Supplemental Figure 1) and usefulness for clinical pathology.

## Quantifying Transcripts in Space at High Resolution

Imaging-based methods operate by probe hybridization. Probe design requires a priori knowledge of target sequences, and, as discussed below, companies typically provide predesigned panels for commercial imaging-based platforms and assist users in their customization. The detection of hybridized probes is then achieved either by in situ hybridization [e.g., seqFISH (23) by the Cai lab, MERFISH (24) by the Zhuang lab (now MERSCOPE by Vizgen), CosMx Spatial Molecular Imager (25) by NanoString Technologies, and Molecular Cartography by Resolve Biosciences] or by in situ sequencing [e.g., CARTANA (26) by the Nilsson lab (now Xenium In-Situ by 10x Genomics) and STARmap (27) by the Wang, Nolan, and Deisseroth labs], as reviewed in Reference 19.

## Computational

On the other hand, sequencing-based ST methods rely on the local capture and spatial barcoding of transcripts followed by NGS approaches to decode both the encoded gene and its spatial position. Examples include high-definition ST (28) developed by the Lundeberg, Ståhl, and Regev labs, DBiT-Seq (29) by the Fan lab, Slide-seq (30) by the Chen and Macosko labs (now Curio Seeker by Curio Bioscience), Stereo-seq (31) by BGI (now STOmics), Visium HD by 10x Genomics, Seq-scope (32) by the Lee lab, and Open-ST (33) by our lab. Sequencing-based methods typically employ an array of spots, each featuring a multitude of molecules with the same barcode and a polyT stretch for mRNA capture. As the tissue section is placed on the array, transcripts are released upon enzymatic permeabilization and locally captured by hybridization of their polyA tails. Regardless of the barcoding strategy, both the transcript (or probe) sequence and the barcode are included in the same molecule during library preparation so that high-throughput NGS can be used to reveal both transcript and barcode identity of billions of transcripts in parallel.

Following data acquisition, computational pipelines enable automated and standardized data preprocessing for the generation of a large transcript-by-position matrix featuring the spatial coordinates of detected transcripts. These include both proprietary software released by companies with their commercial platforms and open-access pipelines developed by the research community that can be tailored to a range of applications, such as Starfish (34) for imaging-based data or Spacemake (35) for sequencing-based data.

While the intrinsic strengths and limitations of imaging- and sequencing-based approaches are discussed further below, it is worth mentioning that sequencing-based methods, capturing potentially all polyadenylated transcripts, are better poised for hypothesis generation, while probebased methods, which feature a higher detection efficiency but are restricted to the targeted genes, are more suitable for hypothesis testing.

## From Transcripts to Cellular Phenotypes

Following their spatial quantifications, transcripts are typically assigned to individual cells. When high-resolution tissue images are available, state-of-the-art deep learning tools for cell segmentation successfully perform this task [e.g., Cellpose (36)]. While nuclei can be already segmented from H&E images, combining nuclear (e.g., DAPI) with cytoplasmic (e.g., rRNA) and membrane (e.g., Na+/K+-ATPase) immunostainings improves the identification of cytoplasmic boundaries. Tissue images then have to be precisely aligned with the detected transcript, which is favored by the microscopy set up in imaging-based methods. On the other hand, images need to be independently acquired before tissue permeabilization and later aligned with the barcoded spots in sequencing-based methods, which may result in imprecise alignments. Alternatively, transcripts can be grouped in cell-sized bins (e.g., 10 µm<sup>2</sup> pseudocells) or segmentation can be performed directly from transcriptomics data using dedicated computational tools [e.g., Baysor (37)].

Following segmentation, low-quality cells are discarded before proceeding with downstream analyses, either setting empirical cutoffs (e.g., on the minimum number of detected genes) or using recent denoising methods that do not require arbitrary thresholds [e.g., STARLING (38)]. Similarly, genes detected in a small fraction of cells can be removed to increase signal-to-noise ratio. Furthermore, the detection of negative probes targeting alien sequences and system controls (i.e., barcodes that are not white listed) can be employed in imaging-based ST to detect nonspecific probe binding and image decoding errors, respectively.

Unbiased clustering of single-cell transcriptomes can then identify distinct molecular phenotypes, which are typically annotated as different cell types and states via the literature-based analysis of their corresponding gene expression markers. These steps, which are shared with singlecell RNA sequencing (scRNA-seq) data analysis, are now streamlined and largely automated following the best practices that have been formulated for the scRNA-seq field (39). Nevertheless, ST datasets carry their intrinsic biases (e.g., due to inaccuracies in cell segmentation or transcript displacement during sectioning or capture) (40), requiring the development of ad hoc computational frameworks to address these challenges [e.g., Voyager (41)].

Following single-cell analysis, preprocessed datasets can be stored, explored, and used for downstream applications based on the spatial coordinates of individual cells. Although infrastructure (e.g., scalable file formats and structures) and ST-specific databases exist [e.g., STOmicsDB (42)], a unified ecosystem and a set of best practices are still lacking. Particular emphasis should be put on developing software for interactive visualization of cellular morphologies, individual transcripts, and cellular annotations, as illustrated in Figure 1, which will be essential for the exploration and validation of ST data by pathologists in clinical applications.

## From Single Cells to Virtual Tissue Blocks

Knowledge of cellular coordinates in high-resolution ST datasets enables ad hoc analyses that have not been possible with scRNA-seq data alone. These include (a) identifying spatial patterns in the distribution of cell types and their molecular states, (b) defining the organization of cell types and molecular states in multicellular niches, and (c) investigating receptor–ligand interactions mediating cell–cell communication in local neighborhoods. While a discussion of specific computational tools is beyond the scope of this review, we would like to point out how best practices still have to be established at this stage. For example, more than 100 different tools exist to map cell–cell interactions (43), and the field still has to converge on standardized approaches, which are urgently needed for clinical applications of ST methods.

While spatial analyses are possible in individual 2D sections, cells live and communicate in 3D. Therefore, reconstructing tissue three dimensionally can improve our understanding of disease mechanisms. As illustrated in Figure 2, it is possible to computationally align the 2D digital imaging and molecular data from consecutive sections using dedicated software [e.g., STIM (44) and PASTE (45)] to create a 3D virtual tissue block. Following alignment, x, y, and z cellular coordinates enable the identification of 3D multicellular niches and the mapping of receptor–ligand interactions in 3D, potentially unveiling aspects that would otherwise be missed when studying only 2D datasets, for instance, gene programs at the tumor boundary (33, 46).

## APPLICATIONS

Despite being in their infancy, high-resolution ST methods have been already successfully employed for building atlases of complex healthy and diseased tissues (Supplemental Table 1).

Clustering: a computational method grouping similar entities based on defined features, commonly used in spatial transcriptomics to identify cell populations

Gene expression marker: a specific gene or set of genes whose expression levels indicate the presence or identity of a particular cell type or cellular state

Spatial patterns: distinct arrangements or distributions of gene expression within tissue regions, revealing spatial organization and functional relationships in spatial transcriptomics

Multicellular niches: groups of cellular neighborhoods sharing a similar cellular composition

Receptor–ligand interactions: molecular binding events between signaling molecules (ligands) and their corresponding receptors, crucial for cell communication and tissue organization

Supplemental Material >

![](images/ff5bf676a65b8660f37731372dc536bca641392186e981abb847d5821d1cf3a7.jpg)  
Figure 1  
Exploring clinical samples with molecular microscopes. (Top row) High-resolution spatial transcriptomics methods work as molecular microscopes, digitalizing gene expression and contextual tissue morphology in intact tissue sections. This enables the interactive exploration of tissue molecular features and their comparison with pathologist annotations. The gray box is the region of interest analyzed; the black square is the inset shown in the bottom row. (Bottom row) Cell segmentation from tissue images is coupled with mapping of millions of transcripts at subcellular resolution (different colors indicate different genes) for the unbiased identification of cell types and states (different colors indicate different transcriptomic clusters). Figure adapted from images created with BioRender.com and from Reference 33 with permission from the authors.

Thanks to the systematic mapping of cell–cell interactions and cellular phenotypes, highresolution ST methods identified coordinated cellular responses driving disease processes and therapeutic responses in situ. High-resolution ST can pinpoint active disease mechanisms in clinical samples, paving the way for mechanism-based personalized therapies (Figure 3). At the same time, high-resolution ST can identify novel disease mechanisms, leading to novel therapeutic targets. Besides mapping gene expression, high-resolution ST can quantify noncoding genes and transcript isoforms, map cellular clones and microorganisms in tissue space, and, combined with additional omics, deepen our understanding of tissue biology. Finally, digitalizing tissue molecular features facilitates the next generation of predictive models in pathology.

## Building Cellular and Molecular Atlases of Complex Tissues

Anatomical and histological atlases have proven essential for modern medicine, serving as references to distinguish physiologic interindividual variations from pathological changes. Atlases also represent shared frameworks that are essential to standardize communication and education in both research and clinical settings. Similarly, spatial molecular atlases will be required to standardize the analysis and guide the interpretation of novel ST data, which are central to advancing our understanding of health and disease. As roughly 37 trillion cells compose the human body, mapping their molecular heterogeneity and spatial relationship represents a formidable challenge that the international research community is starting to tackle thanks to the systematic application of high-throughput single-cell and spatial technologies.

a  
b  
c  
![](images/4608cf5245e16a8c278aff5bcb2378f027a4f55f9c57f7f23c5e294d64620804.jpg)  
Figure 2  
Investigating tissue organization in 2D and 3D virtual tissue blocks. (a,b) High-resolution spatial transcriptomics methods enable the study of tissue organization. Analyzing the composition of cellular neighborhoods reveals how cells live in multicellular niches (different colors indicate different niches) and which receptor–ligand interactions (color gradient indicates interaction strength as a function of receptor-ligand coexpression in neighboring cells) orchestrate communication in situ. (c) The computational alignment of consecutive 2D sections enables the reconstruction and exploration of 3D virtual tissue blocks. Abbreviation: STIM, Spatial Transcriptomics Imaging Framework. Figure adapted from images created with BioRender.com. Panels a and b adapted from Reference 46 with permission from the authors. Panel c adapted from Reference 33 with permission from the authors.

As a prime example of organ complexity, the brain displays an outstanding diversity of cell types with unique molecular features and connectivity. While single-cell technologies reveal the extent of cell types and states across different brain regions (47, 48), they cannot accurately map the spatial organization of neuronal and nonneuronal cells into layers and circuits (49). Moffit and colleagues (50) showcased the power of high-resolution technologies by profiling more than 1 million cells in the mouse brain using their MERFISH platform. Mapping 70 different neuronal populations in the hypothalamic preoptic region and examining the expression of immediate early genes, they revealed the composition of distinct nuclei and their links with parenting, mating, and aggression behaviors. Today, large-scale collaborative efforts, such as the BRAIN Initiative – Cell Census Network (51) and the Allen Brain Cell Atlas (52) combine single-cell technologies, functional assays, and retrograde tracing with high-resolution ST to build a multimodal atlas of the whole brain (53).

At the same time, scientists have been leveraging high-resolution ST to build detailed atlases of major body organs. These efforts range from the 3D reconstruction of the developing heart (54) to the assembly of a stomach encyclopedia (55). Beyond individual efforts, spatial mapping of healthy and diseased cells lies at the core of large consortia, including the Human Cell Atlas (56) and the Human BioMolecular Atlas Program (57), which integrate high-resolution spatial methods with single-cell multiomics to generate a “three-dimensional molecular and cellular atlas of the human body, in health and under various disease conditions” (57, p. 187). The assembly of the human breast cell atlas (58), which “revealed an unexpectedly rich ecosystem of tissue-resident immune cells, as well as distinct molecular differences between ductal and lobular regions,” (58, p. 181) represents a notable early step in this direction. Furthermore, the recent spatial atlases of myocardial infarction (59), metaplastic stomach (55), and injured kidneys (60) highlight their ability to identify cellular neighborhoods related to homeostasis versus injury, pathways linked to successful versus maladaptive repair, and signaling driving recovery versus degenerative states.

![](images/b043515299a4c590b050c1cc92c364e7869778e497349ce009f6afb9d8698095.jpg)  
Clinical applications of high-resolution ST methods. Conceptual diagram depicting a potential workflow for the clinical implementation of high-resolution ST methods, enabling molecularly guided personalized therapies and providing a deeper understanding of disease mechanisms in the future. Abbreviations: AI, artificial intelligence; FF, fresh-frozen; FFPE, formalin-fixed paraffin-embedded; ST, spatial transcriptomics. Figure adapted from images created with BioRender.com.

## Unveiling Coordinated Cellular Responses Driving Disease Processes

High-resolution spatial technologies are already revolutionizing our ability to characterize disease processes at unprecedented resolution, enabling the precise spatiotemporal dissection of disease progression.

By identifying coordinated cellular responses to amyloid plaques in Alzheimer’s disease mouse models and postmortem human samples, Chen and colleagues (61) were among the earliest to showcase the power of spatial omics to interrogate disease processes. To investigate the relationship between amyloid plaques and neurodegeneration, they combined the discovery power of unbiased but low-resolution ST with the high-resolution but low plexy of in situ sequencing. In this way, they identified plaque-induced genes, a set of coexpressed genes upregulated within 100 µm from amyloid plaques, and mapped gene programs to specific cell types. Recently, increasing multiplexing capacity of imaging-based ST technologies and finer resolution of sequencing-based ST provided a more detailed picture of the cellular and molecular characterization of the amyloid plaque niche (62, 63).

Besides neurodegeneration, cellular communication orchestrates a wide variety of tissue processes including inflammation and tissue repair. While low-resolution ST methods enabled the first unbiased analyses of inflammatory processes in intact tissues (64, 65), their lack of single-cell resolution required ad hoc methods to reconstruct cellular networks (66). Today, high-resolution ST technologies enabled the molecular heterogeneity and spatial niches of colitis-associated granulocytes to be resolved (eosinophils in 66, macrophages and neutrophils in 67) and captured the proinflammatory cross talk between keratinocytes and fibroblasts in psoriasis (68). Recently, Cadinu and colleagues (69) reconstructed the remodeling of cellular neighborhoods during injury, inflammation, and repair in a mouse colitis model and revealed how inflammation-associated fibroblasts orchestrate tissue remodeling through receptor–ligand interactions with neighboring epithelial, stromal, and immune cells.

Cellular networks also shape the tumor microenvironment (TME), determining the balance between tumor growth and regression, immune recognition and escape, and tissue invasion or confinement (70). Despite their limitations, early low-resolution ST studies highlighted the spatial heterogeneity of the TME in multifocal prostate cancer (71) and histologically homogeneous regions in melanoma metastases (72). Furthermore, Moncada and colleagues (73) integrated lowresolution ST with matched scRNA-seq data to quantify the abundance of cell types and states in 100-µm ST spots, capturing the colocalization of inflammatory fibroblasts with a transcriptomic subset of cancer cells expressing stress-related genes.

While early ST studies profiled thousands of genes, even large-scale efforts have been typically limited to few patients and relied on matched scRNA-seq data to mitigate their multicellular resolution (74). On the other hand, developments in spatial proteomics methods, such as imaging mass cytometry (75) and multiplexed ion beam imaging (MIBI) (76), enabled the measurement of 30–40 genes at single-cell resolution in large FFPE clinical cohorts. This provided key evidence of TME spatial heterogeneity in breast cancer (77, 78) and the importance of cellular neighborhoods in driving remodeling of the TME in breast and colorectal cancer (79, 80). MIBI was also successfully integrated with low-resolution ST to map a tumor-specific keratinocyte population identified by scRNA-seq to a fibrovascular niche in human squamous cell carcinomas (81). Similarly, Karras and colleagues (82) leveraged low-plex but high-resolution ST to map a population of mesenchymal-like tumor cells identified by scRNA-seq to a perivascular niche in a melanoma mouse model.

While these methods have proven powerful to identify the spatial architecture and heterogeneity of complex tissues, they were limited in either resolution or gene coverage and often required combination with scRNA-seq data (20, 21). Recently, we demonstrated how high-resolution ST instead captures both the precise arrangement of tumor gene expression programs, such as the activation of cholesterol metabolism at the invasion front, and the colocalization of these programs with cell–cell communication hot spots defined by spatially informed receptor–ligand interactions in a metastatic head and neck squamous cell carcinoma (HNSCC) sample (33).

Similarly, Wu and colleagues (83) leveraged Stereo-seq to study tumor phenotypes and intercellular cross talk in 53 primary and metastatic hepatocellular carcinomas (HCCs), revealing the presence of damaged hepatocytes expressing serum amyloid proteins at the invasive margin. Furthermore, a combination of CosMx and in situ sequencing also revealed the preferential colocalization of infiltrating T cells in both high-grade gliomas (84) and high-grade serous tuboovarian carcinomas (85). Finally, Yeh and colleagues (85) leveraged a high-content CRISPR screening (Perturb-seq) to pinpoint the genetic regulators able to upregulate such tumor-intrinsic phenotypes and sensitize ovarian cancer cells to immune-mediated killing in vitro.

## Leveraging Multicellular Niches as Personalized Biomarkers

In the era of personalized medicine, clinicians face the challenge of identifying the most effective drug from among an arsenal of cytotoxic molecules, targeted agents, antibody-based therapeutics, and cellular therapeutics for individual patients. While immunohistochemistry (e.g., to detect hormone receptors) and molecular techniques (e.g., to detect cancer-specific mutations) are able to accurately identify patients presenting specific drug targets, PD-L1 (programmed cell death ligand 1) positivity is not sufficient to predict patient responses to anti-PD-1 agents (86). Anti-tumoral immunity is a highly coordinated response across different components of the TME, which may be only partially captured by the detection of one immune checkpoint molecule. By capturing such multicellular cross talk, high-resolution ST holds great promise for predictive pathology.

Magen and colleagues (87) compared a subset of HCC patients with high intratumoral immune infiltration enrolled in a neoadjuvant anti-PD-1 trial showing variable responses to immunotherapy. Using a combination of MERFISH with scRNA-seq and T cell receptor (TCR) sequencing, they suggest that the local differentiation of $\mathrm { P D - 1 ^ { + } \ T C F { - } 1 ^ { + } \ C D 8 ^ { + } \ T }$ cells occurred only in responders due to their interaction with $\mathrm { C X C L 1 3 ^ { + } ~ T }$ helper cells and dendritic cells in cellular triads. Similarly, Chen and colleagues (88) identified spatially localized immunity hubs to be predictive of immunotherapy benefit in lung cancer. Combining multiplexed immunofluorescence and CosMx, they identify the colocalization of macrophages expressing T cell–recruiting chemokines with $\mathrm { P D - 1 ^ { + } ~ T C F - 7 ^ { + } ~ C D 8 ^ { + } ~ T }$ cells and $\mathrm { C C R 7 ^ { + } \ L A M P 3 ^ { + } }$ dendritic cells in these multicellular niches and quantify their enrichment in preimmunotherapy lung cancers that will benefit from checkpoint blockade.

Besides immune interactions, tumor phenotypes and tumor-stromal cross talk also play critical roles in disease progression and therapeutic responses. Sharma and colleagues (89) previously identified the fetal-like reprogramming of endothelial cells and macrophages in HCC using scRNA-seq. Recently, they leveraged CosMx and Stereo-seq to characterize the cellular cross talk in such oncofetal niches and identified POSTN+ cancer-associated fibroblasts (CAFs) as prominent oncofetal signaling hubs (90). Importantly, they linked the presence of oncofetal niches with relapse and immunotherapy responses in HCC patients, paving the way for the use of oncofetal signatures for therapeutic stratification. High-resolution ST enabled the analysis of cell–cell communication in oncofetal niches, pinpointing which receptor–ligand pairs could potentially drive the expression of the oncofetal program. Inhibiting such interactions (e.g., with blocking antibodies) could represent an effective therapeutic strategy in these patients.

NGS has enabled the coverage of a broad spectrum of actionable mutations, so that a single druggable mutation can be found for an increasing number of patients (91). Similarly, we envision that the spatial mapping of cell types and their transcriptomic phenotypes [e.g., oncofetal programs or cell-type-specific progression biomarkers (92)] together with the expression of drug targets [e.g., hormone receptors (93)] and cell–cell interactions (e.g., cellular triads and immune checkpoint receptor–ligand interactions) will improve patient stratification and guide therapeutic choices in the future.

## Deciphering Novel Disease Mechanisms for Drug Development

Besides being predictive pathology tools, ST technologies are currently being evaluated for applicability in the drug development process, both for identifying novel therapeutic targets (94) and for elucidating mechanisms of drug response and resistance.

Hwang and colleagues (95) profiled 43 pancreatic adenocarcinoma (PDAC) patients who underwent surgical resection either with or without receiving various regimens of adjuvant (chemo)therapy. By combining single-nucleus RNA sequencing (snRNA-seq) with ST (GeoMx), they identified three multicellular communities distinguished by specific malignant and CAF programs, including one composed by neuroendocrine-like malignant and neurotropic CAF programs and infiltrated by $\mathrm { C D 8 ^ { + } ~ T }$ cells. Interestingly, this community was enriched following neoadjuvant treatment, suggesting that the receptor–ligand interactions spatially restricted to this niche could serve as novel therapeutic targets to block the emergence of such aggressive phenotypes. Similarly, Cui Zhou and colleagues (96) combined sc/snRNA-seq and ST to identify the enrichment of inflammatory CAFs expressing metallothioneins in PDAC samples treated with neoadjuvant chemotherapy. As interleukin-1 receptor (IL-1R) blockade has been added to standard chemotherapy to target inflammatory CAFs (iCAFs), metallothioneins could represent an additional therapeutic target for iCAFs in the TME following chemotherapy. On the other hand, Oyoshi and colleagues (97) focused on the microenvironment responses following radiotherapy in esophageal squamous cell carcinoma. Combining scRNA-seq with ST (Visium) and proteomics (CODEX), they uncovered the infiltration of immunosuppressive myeloid cells expressing both PD-L1+ and numerous additional immunomodulatory and tumor-promoting genes, which could constitute targets for combination therapies.

Finally, Derry and colleagues (98) proposed a unique combination of high-resolution ST with trackable intratumor microdosing to evaluate drug responses in situ and in vivo. In this first-of-itskind phase 0 clinical trial, 12 patients with HNSCC received either a SUMOylation inhibitor or a vehicle control through a percutaneous injection 1–4 days before surgery. Local drug responses were then evaluated by combining GeoMx and CosMx, revealing how SUMO pathway inhibition occurred in a spatially graded manner and colocalized with cell cycle arrest restricted to the tumor epithelium. Contextually, SUMO inhibition stimulated interferon responses that shifted the local microenvironment from immunosuppressive to immunopermissive. The localized evaluation of drug responses in arguably the most translationally relevant setting, an in situ human tumor, may revolutionize not only the testing of novel drug agents, as showcased in this study, but also the screening for effective personalized combination therapies (e.g., by implanting devices that simultaneously release multiple drugs).

## Beyond Protein-Coding Genes: Mapping Tumor and Immune Clones, the Full Transcriptome, and Host-Microbial Interactions

Besides mapping gene expression in space, several tools developed for scRNA-seq have been applied to high-resolution ST data. For example, we leveraged the concept of pseudotime to reconstruct tumor transcriptomic evolution in a non–small cell lung cancer (NSCLC) patient (46). Spatial mapping of pseudotime scores revealed a region of the tumor bed where tumor cells acquired proinvasive properties. Analysis of receptor–ligand interactions in this niche revealed the convergent cross talk of $\mathrm { S P P 1 ^ { + } }$ macrophages and myofibroblasts onto tumor integrin receptors, which could drive the induction of tumor invasion in this niche. Furthermore, inferring copy number variants (CNVs) from the simultaneous up- or downregulation of multiple genes located within the same chromosomal region is a popular method to identify and characterize tumor cells in scRNA-seq datasets (99, 100). Transferring the same approach to low-resolution ST data, Erickson and colleagues (101) mapped the phylogenetic hierarchy of histologically benign, preneoplastic, and neoplastic clones in an organ-wide study of a multifocal prostate carcinoma. Similarly, Heiser and colleagues (102) inferred CNVs in space for tumor phylogeographic mapping in 31 colorectal cancer patients. Performing laser capture microdissection and whole-exome sequencing on the different clones identified through spatial CNV analysis, they could then capture the epithelial and microenvironment transcriptomic programs activated during the genetic progression of individual tumors. Furthermore, Chen and colleagues (103) leveraged point mutations captured by sequencing-based methods to visualize allelic imbalance and somatic mutations in cancer samples.

The detection of somatic variants also allows reconstructing the clonal dynamics of T and B cells by analyzing TCR and BCR variable sequences. Single-cell studies demonstrated the power of simultaneously profiling adaptive immune receptors and transcriptional phenotypes to understand immune responses in health and disease (104, 105). As VDJ (variability–diversity–joining) sequences are located within 500 nucleotides away from the 5′ end of the transcript, they are rarely included in short-read sequencing of polyA-captured mRNAs due to their inherent 3′ bias (106). For this reason, either deep sequencing (107) or target enrichment of the VDJ region through polymerase chain reaction (108–110) has been applied to study T cell infiltration in tumors. As full-transcript information is required to resolve different gene isoforms, long-read sequencing has been applied to characterize immunoglobulin isotype switching and chain pairing together with somatic hypermutation and B cell clonal distribution in germinal centers (111). Moreover, Boileau and colleagues (112) leveraged long-read sequencing to spatially map <sub>∼</sub>20,000 isoforms in a mouse model of myocardial infarction. Combining Visium and Nanopore sequencing revealed clinically relevant but yet unexplored modes of transcription, such as higher intron retention, isoform switching in muscle contraction genes, and overall lower transcriptome complexity in the infarct area.

Spatial technologies are also revolutionizing our ability to detect host–pathogen interactions in colonized and infected tissues. Multiple strategies have been adopted to identify and localize pathogens in tissues, including pathognomonic tissue changes [e.g., granulomas in Mycobacterium tuberculosis infection (113)], staining for pathogen-specific proteins (114), or designing pathogenspecific probes (115, 116). As we and others demonstrated in scRNA-seq studies, polyadenylated microbial transcripts are well captured by sequencing-based methods and can be used to profile cellular responses and microbial transcriptomic states [e.g., herpes simplex virus 1 (HSV-1) infection cycle (117, 118)]. Alternatively, metagenomic strategies tailored to the capture of microbial RNA can be integrated in sequencing-based ST methods to identify microbes and contextual host responses. Given the low abundance of microbial transcripts compared with host mRNA, these strategies are preferable to increase assay sensitivity. Recently, Lötstedt and colleagues (119) developed a protocol to capture 16S bacterial sequences and host transcripts to map the cellular composition and commensal geography along the mouse gut. At the same time, Saarenpää and colleagues (120) even included probes for fungal internal transcribed spacers for a richer metagenomic readout.

Finally, in situ polyadenylation strategies are attractive to capture both nonpolyadenylated host and microbial RNA molecules (121). McKellar and colleagues (122) leveraged this approach both to map noncoding transcripts during skeletal muscle regeneration and to profile local host responses around viral mRNAs in a myocarditis mouse model.

Besides expanding the transcriptomic coverage, in situ polyadenylation has also been leveraged to increase the sensitivity of sequenced-based transcriptomic methods when applied to FFPE samples. Although ST successfully identified major cell types when applied to fixed tissues, the data were sparse due to the fragmentation of RNA molecules following formalin fixation (123). Bai and colleagues (124) recently reported high-sensitivity, full-transcriptome profiling of clinical tumor FFPE tissues stored for five years following in situ polyadenylation and polyA-based capture.

## Beyond Gene Expression: Multimodal Spatial Omics

While gene expression is highly informative for identifying cellular types, states, and molecular functions, a holistic understanding of disease processes would benefit from the integrative analysis of cellular genomic, epigenomic, transcriptomic, proteomic, and metabolic layers. Several methods exist for the robust profiling of individual and combined modalities at single-cell (5) and spatial (125) resolution. One approach to multimodal spatial profiling is the independent profiling of consecutive tissue sections with different spatial technologies, followed by computational registration and integration of the resulting high-dimensional images. Androvic and colleagues (126) employed this approach to integrate electron microscopy and MERFISH readouts. Studying transcriptomic and ultrastructural responses in a mouse model of brain injury, they revealed the accumulation of lipid-laden foamy microglia in lesions during remyelination.

As mechanical interactions with the surrounding extracellular matrix (ECM) govern cellular activities in solid tissues, we recently integrated CosMx and second-harmonic imaging readouts to quantify collagen and elastin fiber abundance in cellular neighborhoods (46). Rather than analyzing adjacent cells in consecutive sections, true multimodal profiling of the same cells would be desirable to directly relate features across modalities. For example, ST capture of polyadenylated antibody-derived tags [developed for surface epitope profiling in single cells (127)] has been leveraged for the simultaneous profiling of the whole transcriptome and dozens of proteins in space (128, 129). Similarly, a combination of ST with mass spectrometry–based proteomics and metabolomics (MALDI-MSI) has been applied to correlate neurotransmitter levels with gene expression in Parkinson’s disease (130) and to study tumor metabolic heterogeneity and immunometabolic rewiring at the invasion margin in gastric cancer (131). Finally, paired histological or immunofluorescence images are typically available for more accurate assignment of captured transcripts to single cells, and cellular morphology can be integrated with gene expression to resolve cellular subpopulations missed by either modality alone, as demonstrated by Bao and colleagues (132).

## Toward Affordable Molecular Digital Pathology

In the last decade, technological developments in whole-slide imaging (WSI) scanners enabled the digitization of large numbers of pathology slides at high resolution (133). The growing availability of digitized H&E slides paired with sample-level clinical, histologic, and molecular metadata formed large datasets for the training of predictive deep learning models (134). Today, deep learning approaches can accurately classify different cancer histologies (135), grade prostatic tumors (136), and predict breast cancer hormone receptor status—although with lower accuracy compared with that of immunohistochemistry (137) from H&E images alone. When paired histology and molecular data are available, deep learning approaches can also identify microsatellite instability in colorectal cancer (138) and recurrent mutations in NSCLC frequently mutated genes (139). Pairing H&E images with RNA-seq profiling in large-scale collaborative projects, such as The Cancer Genome Atlas (TCGA) (140), enabled the training of deep learning models that predict gene expression profiles from matching whole-slide images (141). However, the bulk nature of these gene expression measurements, which average across millions of cells in the TME, limited the prediction accuracy of these HE2RNA models. Furthermore, while advances in explainable artificial intelligence (AI) can point to which image regions are relevant for gene expression predictions (e.g., by generating explanatory heat maps) (142), the spatial agnostic nature of bulk RNA-seq limited both the interpretability and the validation of such tools, both of which are central to their clinical application and the advancement of scientific knowledge. In this regard, ST methods provide the missing link between gene expression and H&E morphology and hold great potential for the training of the next generation of deep learning models in pathology.

Deep learning analysis of low-resolution ST and coregistered H&E images already demonstrates the feasibility and power of this approach by successfully predicting local and bulk-like gene expression patterns in breast cancer (143). Models can also be used to impute missing data and artificially increase assay resolution using high-resolution tissue images (144). Furthermore, Zeng and colleagues (145) used ST data to validate the predictions of a deep learning model trained on TCGA data to predict how HCC patients would respond to a combination of immune checkpoint and angiogenesis inhibitors (atezolizumab-bevacizumab). They matched prediction heat maps with ST data to understand whether the morphological structures relevant for model predictions had any biological significance. Interestingly, their research revealed that regions with high prediction scores not only featured higher expression of a gene signature previously linked with atezolizumab-bevacizumab response but also identified the local upregulation of immune effector genes, hinting at an unexpected immune-mediated mechanism as key to drug response.

Today, H&E histology remains at the cornerstone of clinical pathology as a well-established, highly informative, and cost-effective diagnostic tool. While molecular signatures are powerful in guiding patient treatment, the needs for patient material, specialized equipment, costly reagents, and technical expertise represent barriers to their routine application (146). Just as WSI provided the training data for large deep learning models, we envision that high-resolution ST datasets will power the next generation of predictive models in pathology. Importantly, these models could predict the expression of relevant gene/signatures from H&E images alone, enabling widespread access to molecular diagnostics at low cost.

## CONSIDERATIONS FOR THE DESIGN OF HIGH-RESOLUTION SPATIAL TRANSCRIPTOMICS CLINICAL STUDIES

While early studies showcased the potential of high-resolution ST methods to improve clinical care, the translation of these recently developed technologies currently requires clinical studies to link spatial biomarkers with patient outcomes and ultimately demonstrate their usefulness in different therapeutic contexts. As high-resolution ST methods differ significantly in terms of their inherent parameters, we discuss here a number of key considerations that researchers and clinicians should keep in mind to maximize the information obtained and optimize the study outcome.

## Sample Preservation

Given the rapid degradation of RNA molecules at room temperature, sample fixation is required for high-resolution ST analyses. Together with RNA, preserving tissue morphology is also central to downstream analyses, such as integrating high-resolution ST with histologic annotations and improving the accuracy of cell segmentation. Currently, either FFPE or FF samples are compatible with high-resolution ST methods. As tissue preservation limits the choice of applicable downstream ST methods and, in turn, the molecular readouts, it is a key step in experimental design.

In clinical routines, formalin fixation followed by paraffin embedding is by far the most common fixation protocol. Formalin fixation accurately preserves tissue and cellular morphologies, allows sample storage at nonfreezing temperatures, and permits the cutting of 5-µm-thick (and even thinner) sections. Such a thickness mostly spans part of a single cell along the z-axis, thereby limiting the number of misassigned transcripts upon 2D segmentation. As FFPE samples are routinely collected for diagnostics, high-resolution ST profiling can be easily integrated in clinical workflows and matched with H&E histology, immunohistochemistry, and molecular diagnostics. However, cross-linking proteins and nucleic acid results in RNA fragmentation, which prevents the use of ST methods that rely on the capture of polyadenylated transcripts. Until in situ polyadenylation or alternative capture methods become well established, FFPE tissues are best processed with imaging-based methods or sequencing-based methods relying on the capture of hybridized probes (e.g., Visium HD). Alternatively, snap-freezing in liquid nitrogen and embedding in optimal cutting temperature (OCT) medium or alternative cutting media can be used to preserve samples. The integrity of RNA molecules is mostly preserved in such FF samples, enabling the use of sequencing-based methods for the unbiased capture of polyadenylated transcripts.

As for all omic assays, sample quality is of paramount importance. Therefore, screening RNA quality, measuring either the RNA integrity number (RIN) in FF samples or DV200 in FFPE samples, represents a central step in sample selection and guides the optimization of sample fixation and storage protocols. While standardized protocols for collection, preservation, cutting, and storage are well established for FFPE samples in hospitals worldwide, FF tissue preservation is far less common and requires additional biological materials besides those used for diagnostic purposes, which could represent a limit to many applications (e.g., the profiling of diagnostic biopsies). At the same time, FF samples need to be snap-frozen with minimal postmortem/resection time and kept at freezing temperatures during transport, storage, and processing to prevent RNA degradation. In particular, processing requires optimal conditions to avoid tissue melting or cracking during cryosectioning. It is thus essential to establish adequate standard operating procedures to guide FF sample preservation and document time intervals for each specimen to ensure consistency and quality control.

## Method Selection

Besides their compatibility with FFPE and FF samples, imaging- and sequencing-based methods carry their own intrinsic strengths and limitations. Once optimized for FF sample collection and processing, sequencing-based methods are ideal for discovery and hypothesis-generation studies. Not only do they enable the genome-wide investigation of gene expression through the unbiased capture of polyadenylated transcripts but they also retain sequence information, which can be leveraged for the identification of somatic variants, transcript isoforms and noncoding genes, TCR and BCR clones, bacteria, viruses, etc., as discussed above. Furthermore, sequencing-based methods can be combined with single-nucleus extraction protocols to generate single-cell multiomic data from consecutive sections.

Imaging-based methods, on the other hand, are best suited for hypothesis validation and clinical testing. Their discovery potential is indeed limited by the reliance on predesigned probes, which restricts measurements to target genes and determines the loss of sequence information. At the same time, gene panels have several advantages, including higher sensitivity, shorter turnaround times, and improved result interpretability, making them particularly suitable for clinical applications. Furthermore, the nondestructive nature of imaging-based methods facilitates the profiling of the same section with different modalities. This ranges from immunohistochemistry for the diagnostic validation of high-resolution ST results to label-free imaging (e.g., second-harmonic imaging) for the simultaneous profiling of collagen and elastin fibers in the ECM. Even more relevant is the combination of imaging-based ST methods with H&E histology to match highresolution ST results with pathologist annotations and enable the training of the next generation of predictive deep learning models. Furthermore, imaging-based methods by design acquire data at single-molecule resolution, while the resolution of sequencing-based methods is limited by the spot size, which can vary from 0.6 µm in Open-ST to 10 µm in Curio Seeker. On the other hand, imaging-based methods require automated microscopy systems for data acquisition, which can be complex to set up or expensive to purchase, while sequencing-based methods leverage widely available high-throughput sequencers for their readouts. Relying on a microscopy setup also typically limits both the size of the imaged area to a routine glass slide and the number of slides that can imaged simultaneously, while capture areas in sequencing-based methods are limited only to the size of the array used, which can be easily customized in noncommercial solutions, and allow the simultaneous processing of tens of samples.

Table 1 Comparison of commercial high-resolution spatial transcriptomics methods

<table><tr><td>Technology</td><td>Spatial resolution</td><td>Input material</td><td>Gene panel</td><td>Estimated cost/section</td><td>Equipment required</td></tr><tr><td>CosMx Spatial Molecular Imager</td><td>Single molecule</td><td>FFPE</td><td>Yes</td><td> $\$$ </td><td>Proprietary scanner</td></tr><tr><td>Curio Seeker</td><td>10 μm</td><td>FF</td><td>No</td><td> $\$ -$ </td><td> $No^b$ </td></tr><tr><td>MERSCOPE</td><td>500 nm</td><td>FF and FFPE</td><td>Yes</td><td> $\$$ </td><td>Proprietary scanner</td></tr><tr><td>Molecular Cartography</td><td>Single molecule</td><td>FF and FFPE</td><td>Yes</td><td> $\$$ </td><td>Proprietary scanner</td></tr><tr><td>STOmics</td><td>0.5 μm</td><td>FF</td><td>No</td><td> $\$ -$ </td><td> $No^b$ </td></tr><tr><td>Visium HD</td><td>2 μm</td><td>FFPE</td><td> $Yes^a$ </td><td> $\$$ </td><td>Proprietary device</td></tr><tr><td>Xenium In-Situ</td><td>Single molecule</td><td>FF and FFPE</td><td>Yes</td><td> $\$$  - \)</td><td>Proprietary scanner</td></tr></table>

Abbreviations: FF, fresh-frozen; FFPE, formalin-fixed paraffin-embedded.  
<sup>a</sup>Genome-wide (<sub>∼</sub>18,000 genes) but probe-based.  
<sup>b</sup>Sequencer required.

Finally, when choosing a high-resolution ST method, it is worth noting that costs can vary widely. Besides the equipment needed, cost is impacted by the number of targeted genes and the need for panel customization in imaging-based methods and by the size of the capture area and the depth of sequencing in sequencing-based methods. Furthermore, commercial platforms offer a trade-off between higher pricing and easier implementation; however, such costs may become prohibitive when profiling large clinical cohorts.

Ultimately, the local availability of samples annotated with clinically relevant metadata, instrumentations, and trained personnel represents a key limiting factor to the range of methods and experimental designs that can be leveraged. Especially in this early phase, collaborations with core facilities and research labs specializing in spatial technologies would greatly benefit clinical projects.

To help investigators select the most suitable study design, key features of various highresolution ST methods are presented in Table 1 (commercial) and Table 2 (noncommercial),

Table 2 Comparison of noncommercial high-resolution spatial transcriptomics methods

<table><tr><td>Technology</td><td>Spatial resolution</td><td>Input material</td><td>Gene panel</td><td>Estimated cost/section</td><td>Availability</td></tr><tr><td>DBiT-seq</td><td>10, 20, 50 μm</td><td>FF and FFPE</td><td>No</td><td>$</td><td>Methods described in the published paper and in an additional STAR protocol (29)</td></tr><tr><td>HDST</td><td>2 μm</td><td>FF</td><td>No</td><td>NA</td><td>Methods described only in the published paper (28)</td></tr><tr><td>Open-ST</td><td>0.6 μm</td><td>FF</td><td>No</td><td>$</td><td>Continuously updated experimental protocol, open-source software, and discussion board (https://rajewsky-lab.github.io/openst/latest/)</td></tr><tr><td>SeqFISH</td><td>Single molecule</td><td>FF</td><td>Yes</td><td>NA</td><td>Methods described only in the published paper</td></tr><tr><td>Seq-scope</td><td>0.6 μm</td><td>FF</td><td>No</td><td>$</td><td>Methods described in the published paper and in a dedicated protocol (32)</td></tr><tr><td>STARmap</td><td>1 μm</td><td>FF</td><td>Yes</td><td>NA</td><td>Methods described only in the published paper (27)</td></tr></table>

Abbreviations: FF, fresh-frozen; FFPE, formalin-fixed paraffin-embedded; NA, not applicable; STAR, structured, transparent, accessible, reproducible.

## DESIGNING A TARGETED GENE PANEL FOR CLINICAL APPLICATIONS

Probe-based assays restrict measurements to a panel of target genes. Panel design requires both prior knowledge about which sequences to target with gene-specific probes and large-scale unbiased readouts to inform gene selection. For commercial imaging-based platforms, companies offer both fully customized panels and several predesigned panels to which users can add specific genes of interest. Predesigned panels are typically organ-specific (e.g., brain) or application-specific (e.g., immuno-oncology) and feature well-established cell-type markers and receptor–ligand pairs. While probe design is largely based on platform-specific proprietary databases, gene selection and panel evaluation benefit from matched unbiased single-cell or spatial transcriptomics data. With a single-cell reference at hand, several computational tools can identify the smallest number of genes to either capture most transcriptomic variation in the dataset [e.g., geneBasis (154)], or distinguish annotated cell types with high accuracy [e.g., scGeneFit (155) and NS-Forest (156)]. When paired spatial data are available, gpsFISH (157) can account for platform-specific effects in detecting individual genes. gpsFISH can also evaluate the performance of preexisting panels and use a genetic evolution approach to suggest the smallest number of custom genes to be added to better distinguish specific cell types. Finally, probes targeting pathogen-specific sequences, such as bacterial 16S or viral specific sequences, may be added for infectious disease studies.

## SPATIAL POWER ANALYSIS FOR CLINICAL APPLICATIONS

Conducting a power analysis is central to designing clinical studies. Similarly to clinical single-cell studies, a sample’s cellular composition, sensitivity, accuracy, and depth of gene expression profiling are critical to identify statistical differences in cell types (158). In spatial studies, investigators should additionally consider the smallest region of interest (ROI) to be analyzed in each sample. Directly related to the number of cells profiled, ROI size is the most critical factor for detecting cell types and a key determinant of assay cost per patient, thereby determining the total number of patients that can be analyzed. High-resolution ST approaches drastically increase the number of cells profiled from each sample. However, tissue composition is inhomogeneous, and cells are organized in tissue domains and multicellular niches. Therefore, ROI positioning is central to minimizing the ROI area while preserving study power. For sequencing-based methods, ROI selection must be performed upon placing the section on the capture area, while imaging-based methods can distribute fields of view following low-resolution whole-slide imaging before data acquisition. Moreover, FFPE-compatible methods are compatible with tissue microarrays, which enable the parallel analysis of dozens of ROIs from different tissue blocks on the same section. A priori knowledge from pilot studies is beneficial to estimate the impact of tissue architecture on spatial power using dedicated tools for in silico tissue modeling (159). Finally, screening samples with routine histology and immunofluorescence followed by manual annotation, deep learning–aided analysis of WSI images (46), or automated ROI placement with vision transformers (160) can all be used for ROI selection.

and considerations for the design of targeted gene panels and spatial power analysis for clinical applications are discussed in the sidebars titled Designing a Targeted Gene Panel for Clinical Applications and Spatial Power Analysis for Clinical Applications.

## CURRENT CHALLENGES IN THE CLINICAL TRANSLATIONOF HIGH-RESOLUTION SPATIAL TRANSCRIPTOMICS METHODS

As showcased in several preclinical applications, high-resolution ST approaches hold the potential to revolutionize clinical practice. At this early stage, however, high-resolution ST technologies have been mostly limited to the research space. While their compatibility with routinely collected

![](images/ade49e3aa298803f8e033f0df82a1d4cefa7a5335045d6b16fcabc98394e40b1.jpg)  
Figure 4  
Current challenges in the clinical translation of high-resolution spatial transcriptomics methods. Conceptual roadmap of translational <sup>challenges</sup> <sup>categorized</sup> <sup>by</sup> <sup>technique</sup> <sup>(</sup>⃝<sup>1</sup> <sup>),</sup> <sup>actionability/interpretation</sup> <sup>(</sup>⃝<sup>2</sup> <sup>),</sup> <sup>and</sup> <sup>implementation</sup> <sup>(</sup>⃝<sup>3</sup> <sup>).</sup>

FFPE samples and avoidance of tissue dissociation, which still represent major obstacles to the clinical implementation of single-cell approaches today (8), will favor their swift translation, several limitations need to be overcome for their implementation in routine clinical workflows. <sup>These</sup> <sup>can</sup> <sup>be</sup> <sup>classified</sup> <sup>as</sup> <sup>(</sup>⃝<sup>1</sup> <sup>)</sup> <sup>challenges</sup> <sup>inherent</sup> <sup>to</sup> <sup>ST</sup> <sup>methods,</sup> <sup>(</sup>⃝<sup>2</sup> <sup>)</sup> <sup>challenges</sup> <sup>related</sup> <sup>to</sup> <sup>the</sup> <sup>data</sup> <sup>and</sup> <sup>their</sup> <sup>interpretation,</sup> <sup>and</sup> <sup>(</sup>⃝<sup>3</sup> <sup>)</sup> <sup>challenges</sup> <sup>related</sup> <sup>to</sup> <sup>implementation</sup> <sup>in</sup> <sup>clinical</sup> environments (Figure 4).

## Challenges Related to the Methods Themselves

In the last several years, rapid technological advancements have greatly improved the performance of high-resolution ST methods, and further improvements are to be expected. However, several challenges still exist. First, sample preservation strategy imposes a trade-off between sample availability and depth of the molecular readouts: Formalin fixation is well established in routine workflows but inevitably results in RNA fragmentation, while snap-freezing allows the study of intact RNA molecules but requires the implementation of novel sample procedures and prevents the study of archived samples. Second, there is currently a trade-off between the number of genes studied and their detection efficiency. On the one hand, imaging-based approaches feature higher sensitivity but are limited to predefined targeted genes, and detection efficiency decreases with increasing panel size. On the other hand, sequencing-based methods can—in principle—capture the whole polyadenylated transcriptome; however, they are biased toward the detection of highly expressed genes. Furthermore, scalability represents another limit to the implementation of current methods in diagnostic routines. On the one hand, imaging-based methods are largely automated, but they are limited to two to four slides per run and feature long acquisition times, especially when large tissue areas or numerous targets are imaged simultaneously. On the other hand, sequencingbased approaches can process several samples in parallel, but automated workflows are not yet commercially available. Finally, best practices for accurate cell segmentation, data normalization, clustering, and downstream computational data analyses are still areas of active research.

## Challenges Related to Result Interpretation and Actionability

To accurately interpret and generate actionable insights from ST data, large-scale healthy and disease references are required. Investigating disease states will be feasible only after the interindividual variability in healthy states has been clearly described (147). International consortia, such as the Human Cell Atlas (56), have begun undertaking such efforts, and ST studies on specific tissues are being published by individual labs. It is imperative to expand and integrate these studies into a single, unified database, as has been done, for instance, in the Allen Mouse Brain Atlas (148). Naturally, human primary material from healthy individuals is, for several tissues, not as accessible as it is for model systems, but several steps can assist in that direction: (a) commencing with tissues that are more accessible (skin, colon, liver, etc.); (b) acquisition of nondiseased samples from large tissue resections; (c) increasing awareness of organ donors in society; and (d) computational integration of other modalities, such as scRNA-seq datasets.

Apart from the existence of a healthy tissue reference, extracting actionable insights from ST data will require the existence of a large pool of similarly processed datasets for the tissue and disease under study. Amassing data from patient cohorts bears substantial benefits, including (a) more accurate characterization of the disease states and more precise classification of disease subtypes; (b) identification of molecular components responsible for the generation and progression of the disease, when these are present; (c) amelioration of interpatient heterogeneity within the same indication, potentially leading to identification of trends; (d) identification of persistently modified molecular readouts, which could potentially serve as disease biomarkers; (e) identification of persistently active signaling pathways within the disease, paving the way for discovering new drug targets; and ( f ) systematic characterization of molecular readouts across distinct therapies and their correlation with treatment response, leading to better evaluation of survival and prognosis.

Finally, large-scale trials are required to link spatial features to clinical factors and demonstrate the benefit of molecularly guided personalized treatments.

## Challenges Related to Clinical Implementation

Besides solving technical challenges and demonstrating the utility of spatial biomarkers, the recommendation of spatial methods by international guidelines and the accreditation within national regulatory frameworks will ultimately be needed for the routine implementation of high-resolution ST methods in the clinic. This will require standardized operating procedures controlling all steps from tissue extraction inside the operating room to the generation of the ST datasets and subsequent evaluation of the spatial biomarkers to ensure robust and reproducible readouts for clinical decision-making. Furthermore, integration of spatial readouts in actionable clinical reports and in electronic health records will be central to ensuring accessibility to pathologists, clinicians, and researchers.

Overall, the multidisciplinary collaboration between experimental and computational scientists along with clinical researchers, healthcare personnel, and ethical/regulatory bodies will ultimately drive the swift translation of spatial omics for the benefit and safety of patients.

## OUTLOOK

Foundation models: large-scale models pretrained on vast amounts of data, serving as the basis for a wide range of use cases through fine-tuning

While the rapid growth of the ST field is yielding novel and more sophisticated experimental and computational methods every day, the principles discussed here will likely remain valid as will the need for clinical translation of ST technologies to improve patient care. Importantly, clinical trials are urgently needed to demonstrate both the feasibility and the efficacy of ST approaches. In this regard, we outlined a roadmap for the design of clinical projects aimed at linking spatial patterns with patient outcomes. At the same time, international efforts should also be directed toward the benchmarking of different sample collection and preservation protocols, the balancing of molecular readouts with costs, and the identification of personnel and infrastructure required for different experimental methods. Furthermore, the standardization of data analysis and reporting pipelines leveraging publicly available tools and large-scale atlases of healthy and disease samples will be central to the generation of robust clinical reports. Even if the current challenges are overcome, ST methods will still be limited to a single snapshot, highlighting the continued need for experimental models to link clinical trials with perturbation studies to move from hypotheses generated by these high-dimensional assays to mechanistic insights. In this regard, the ability to combine organoids with optogenetic perturbations of tissues in time and space, as recently showcased in human brain organoids (149), represents an attractive avenue to link cause and effect in patient-derived models (150). Ultimately, the integration of ST and proteomic readouts with emerging spatial genomics, epigenomics, and metabolomics technologies will provide a holistic representation of complex tissues in 2D and 3D (151).

Finally, ST methods offer the unique opportunity of digitalizing tissue gene expression and the contextual morphology at high resolution. Recently, the availability of extensive digital imaging and transcriptomic datasets enabled the self-supervised training of large-scale AI models, such as Virchow (152) and RudolfV (153), which were trained on billions of histological images, and scGPT, which was trained on more than 33 million single-cell profiles. Fine-tuning these foundation models for several downstream applications can then improve the robustness and generalizability of deep learning predictions when limited training data are available. This can be especially relevant for ST, as it could provide a unique opportunity to bridge tissue histology and molecular readouts, improving our ability to predict gene expression for routinely collected H&E images and increase access to spatial biomarkers worldwide.

## SUMMARY POINTS

1. High-resolution spatial transcriptomics (ST) methods work as molecular microscopes, profiling gene expression at subcellular resolution in tissue sections.

2. ST technologies can be broadly classified into sequencing-based methods and imagingbased methods, each bearing unique strengths and limitations that must be taken into account during the design of clinical projects.

3. ST methods capture both the heterogeneity of cell types and molecular phenotypes and their spatial organization in multicellular tissue niches.

4. ST methods have been successfully applied to build cellular and molecular atlases and to systematically investigate local cell–cell interactions in healthy and diseased tissues.

5. ST methods have already identified how coordinated cellular processes orchestrate disease progression and therapeutic responses, revealing novel mechanisms across a range of pathologies.

6. Albeit still at an early stage, preclinical studies have started to link spatial biomarkers extracted by ST technologies with patient outcomes in selected oncologic diseases.

7. Digitalizing molecular readouts from patient samples via ST methods holds great potential to revolutionize clinical care, informing mechanism-based, personalized therapies.

8. Computational breakthroughs culminating in explainable artificial intelligence together with the amassing of paired histology images and digital spatial molecular atlases will transform fundamental and clinical research.

## DISCLOSURE STATEMENT

N.K. and N.R. are listed as inventors of a patent application relating to the Open-ST platform. The patent application was submitted through the Technology Transfer Office of the Max-Delbrück Center (MDC), with the MDC being the patent applicant.

## ACKNOWLEDGMENTS

We thank all members of the Rajewsky lab for critical and helpful discussions. We thank Alexandra Tschernycheff, Veronica Jakobi, and Margareta Herzog for supporting the organization of the lab. Special thanks to Marie Schott, Daniel Leon-Perinan, Agnieszka Rybak-Wolf, and Ilan Theurillat for reviewing the manuscript. T.M.P. acknowledges the Berlin School of Integrative Oncology for financial support through the GSSP program of the German Academy of Exchange Service (DAAD) and the Joachim Herz Foundation for financial support through the Add-on Fellowship program. N.R. acknowledges Deutsche Forschungsgemeinschaft (DFG) grant RA 838/5–1, Deutsches Zentrum für Herz-Kreislauf-Forschung (DZHK) grants 81Z0100105 and 81X2100155, and the Chan Zuckerberg Initiative (CZI) Seed Network and NeuroCure Cluster of Excellence in the neurosciences at Charité – Universitätsmedizin Berlin.

## LITERATURE CITED

1. Virchow R. 1858. Die Cellularpathologie in ihrer Begründung auf physiologische und pathologische Gewebelehre. Berlin: Hirschwald. https://www.digitale-sammlungen.de/de/view/bsb10926743?page=5

2. Lander ES, Linton LM, Birren B, Nusbaum C, Zody MC, et al. 2001. Initial sequencing and analysis of the human genome. Nature 409(6822):860–921

3. Brown NA, Elenitoba-Johnson KSJ. 2020. Enabling precision oncology through precision diagnostics. Annu. Rev. Pathol. Mech. Dis. 15:97–121

4. Aizarani N, Saviano A, Sagar, Mailly L, Durand S, et al. 2019. A human liver cell atlas reveals heterogeneity and epithelial progenitors. Nature 572(7768):199–204

5. Baysoy A, Bai Z, Satija R, Fan R. 2023. The technological landscape and applications of single-cell multi-omics. Nat. Rev. Mol. Cell Biol. 24(10):695–713

6. Plass M, Solana J, Wolf FA, Ayoub S, Misios A, et al. 2018. Cell type atlas and lineage tree of a whole complex animal by single-cell transcriptomics. Science 360(6391):eaaq1723

7. Rajewsky N, Almouzni G, Gorski SA, Aerts S, Amit I, et al. 2020. LifeTime and improving European healthcare through cell-based interceptive medicine. Nature 587(7834):377–86

8. Lim J, Chin V, Fairfax K, Moutinho C, Suan D, et al. 2023. Transitioning single-cell genomics into the clinic. Nat. Rev. Genet. 24(8):573–84

9. van den Brink SC, Sage F, Vértesy Á, Spanjaard B, Peterson-Maduro J, et al. 2017. Single-cell sequencing reveals dissociation-induced gene expression in tissue subpopulations. Nat. Methods 14(10):935–36

25. He S, Bhatt R, Brown C, Brown EA, Buhr DL, et al. 2022. High-plex imaging of RNA and proteins at subcellular resolution in fixed tissue by spatial molecular imaging. Nat. Biotechnol. 40(12):1794–806

10. Slyper M, Porter CBM, Ashenberg O, Waldman J, Drokhlyansky E, et al. 2020. A single-cell and singlenucleus RNA-Seq toolbox for fresh and frozen human tumors. Nat. Med. 26(5):792–802

11. Wang Y, Fan JL, Melms JC, Amin AD, Georgis Y, et al. 2023. Multimodal single-cell and whole-genome sequencing of small, frozen clinical specimens. Nat. Genet. 55(1):19–25

12. Vallejo AF, Harvey K, Wang T, Wise K, Butler LM, et al. 2022. snPATHO-seq: unlocking the FFPE archives for single nucleus RNA profiling. bioRxiv 2022.08.23.505054. https://doi.org/10.1101/2022. 08.23.505054

13. Palla G, Fischer DS, Regev A, Theis FJ. 2022. Spatial components of molecular tissue biology. Nat. Biotechnol. 40(3):308–18

14. Satija R, Farrell JA, Gennert D, Schier AF, Regev A. 2015. Spatial reconstruction of single-cell gene expression data. Nat. Biotechnol. 33(5):495–502

15. Karaiskos N, Wahle P, Alles J, Boltengagen A, Ayoub S, et al. 2017. The Drosophila embryo at single-cell transcriptome resolution. Science 358(6360):194–99

16. Nitzan M, Karaiskos N, Friedman N, Rajewsky N. 2019. Gene expression cartography. Nature 576:132– 37

17. Marx V. 2021. Method of the year: spatially resolved transcriptomics. Nat. Methods 18(1):9–14

18. Moses L, Pachter L. 2022. Museum of spatial transcriptomics. Nat. Methods 19(5):534–46

19. Rao A, Barkley D, França GS, Yanai I. 2021. Exploring tissue architecture using spatial transcriptomics. Nature 596(7871):211–20

20. Longo SK, Guo MG, Ji AL, Khavari PA. 2021. Integrating single-cell and spatial transcriptomics to elucidate intercellular tissue dynamics. Nat. Rev. Genet. 22(10):627–44

21. Asp M, Bergenstråhle J, Lundeberg J. 2020. Spatially resolved transcriptomes—next generation tools for tissue exploration. Bioessays 42(10):e1900221

22. Park J, Kim J, Lewy T, Rice CM, Elemento O, et al. 2022. Spatial omics technologies at multimodal and single cell/subcellular level. Genome Biol. 23(1):256

23. Eng C-HL, Lawson M, Zhu Q, Dries R, Koulena N, et al. 2019. Transcriptome-scale super-resolved imaging in tissues by RNA seqFISH. Nature 568(7751):235–39

24. Chen KH, Boettiger AN, Moffitt JR, Wang S, Zhuang X. 2015. Spatially resolved, highly multiplexed RNA profiling in single cells. Science 348(6233):aaa6090

26. Ke R, Mignardi M, Pacureanu A, Svedlund J, Botling J, et al. 2013. In situ sequencing for RNA analysis in preserved tissue and cells. Nat. Methods 10(9):857–60

27. Wang X, Allen WE, Wright MA, Sylwestrak EL, Samusik N, et al. 2018. Three-dimensional intact-tissue sequencing of single-cell transcriptional states. Science 361(6400):eaat5691

28. Vickovic S, Eraslan G, Salmén F, Klughammer J, Stenbeck L, et al. 2019. High-definition spatial transcriptomics for in situ tissue profiling. Nat. Methods 16(10):987–90

29. Liu Y, Yang M, Deng Y, Su G, Enninful A, et al. 2020. High-spatial-resolution multi-omics sequencing via deterministic barcoding in tissue. Cell 183(6):1665–81.e18

30. Rodriques SG, Stickels RR, Goeva A, Martin CA, Murray E, et al. 2019. Slide-seq: a scalable technology for measuring genome-wide expression at high spatial resolution. Science 363(6434):1463–67

31. Chen A, Liao S, Cheng M, Ma K, Wu L, et al. 2022. Spatiotemporal transcriptomic atlas of mouse organogenesis using DNA nanoball-patterned arrays. Cell 185(10):1777–92.e21

32. Cho C-S, Xi J, Si Y, Park S-R, Hsu J-E, et al. 2021. Microscopic examination of spatial transcriptome using Seq-Scope. Cell 184(13):3559–72.e22

33. Schott M, León-Periñán D, Splendiani E, Strenger L, Licha JR, et al. 2024. Open-ST: high-resolution spatial transcriptomics in 3D. Cell 187(15):3953–72.e26

34. Perkel JM. 2019. Starfish enterprise: finding RNA patterns in single cells. Nature 572(7770):549–51

35. Sztanka-Toth TR, Jens M, Karaiskos N, Rajewsky N. 2022. Spacemake: processing and analysis of largescale spatial transcriptomics data. Gigascience 11:giac064

36. Stringer C, Wang T, Michaelos M, Pachitariu M. 2021. Cellpose: a generalist algorithm for cellular segmentation. Nat. Methods 18(1):100–6

37. Petukhov V, Xu RJ, Soldatov RA, Cadinu P, Khodosevich K, et al. 2022. Cell segmentation in imagingbased spatial transcriptomics. Nat. Biotechnol. 40(3):345–54

38. Lee Y, Chen ELY, Chan DCH, Dinesh A, Afiuni-Zadeh S, et al. 2024. Segmentation error aware clustering for highly multiplexed imaging. bioRxiv 2024.02.29.582827. https://doi.org/10.1101/2024.02. 29.582827

39. Luecken MD, Theis FJ. 2019. Current best practices in single-cell RNA-seq analysis: a tutorial. Mol. Syst. Biol. 15(6):e8746

40. Atta L, Clifton K, Anant M, Aihara G, Fan J. 2024. Gene count normalization in single-cell imagingbased spatially resolved transcriptomics. Genome Biol. 25:153

41. Moses L, Einarsson PH, Jackson K, Luebbert L, Booeshaghi AS, et al. 2023. Voyager: exploratory singlecell genomics data analysis with geospatial statistics. bioRxiv 2023.07.20.549945. https://doi.org/10. 1101/2023.07.20.549945

42. Xu Z, Wang W, Yang T, Li L, Ma X, et al. 2024. STOmicsDB: a comprehensive database for spatial transcriptomics data sharing, analysis and visualization. Nucleic Acids Res. 52(D1):D1053–61

43. Armingol E, Baghdassarian HM, Lewis NE. 2024. The diversification of methods for studying cell-cell interactions and communication. Nat. Rev. Genet. 25(6):381–400

44. Preibisch S, Karaiskos N, Rajewsky N. 2021. Image-based representation of massive spatial transcriptomics datasets. bioRxiv 2021.12.07.471629. https://doi.org/10.1101/2021.12.07.471629

45. Zeira R, Land M, Strzalkowski A, Raphael BJ. 2022. Alignment and integration of spatial transcriptomics data. Nat. Methods 19(5):567–75

46. Pentimalli TM, Schallenberg S, León-Periñán D, Legnini I, Theurillat I, et al. 2023. High-resolution molecular atlas of a lung tumor in 3D. bioRxiv 2023.05.10.539644. https://doi.org/10.1101/2023.05. 10.539644

47. Tasic B, Yao Z, Graybuck LT, Smith KA, Nguyen TN, et al. 2018. Shared and distinct transcriptomic cell types across neocortical areas. Nature 563(7729):72–78

48. Hodge RD, Bakken TE, Miller JA, Smith KA, Barkan ER, et al. 2019. Conserved cell types with divergent features in human versus mouse cortex. Nature 573(7772):61–68

49. Piwecka M, Rajewsky N, Rybak-Wolf A. 2023. Single-cell and spatial transcriptomics: deciphering brain complexity in health and disease. Nat. Rev. Neurol. 19(6):346–62

50. Moffitt JR, Bambah-Mukku D, Eichhorn SW, Vaughn E, Shekhar K, et al. 2018. Molecular, spatial, and functional single-cell profiling of the hypothalamic preoptic region. Science 362(6416):eaau5324

51. BRAIN Initiat. Cell Census Netw. (BICCN). 2021. A multimodal cell census and atlas of the mammalian primary motor cortex. Nature 598(7879):86–102

52. Yao Z, van Velthoven CTJ, Kunst M, Zhang M, McMillen D, et al. 2023. A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. Nature 624(7991):317–32

53. Liu H, Zeng Q, Zhou J, Bartlett A, Wang B-A, et al. 2023. Single-cell DNA methylome and 3D multiomic atlas of the adult mouse brain. Nature 624(7991):366–77

54. Asp M, Giacomello S, Larsson L, Wu C, Fürth D, et al. 2019. A spatiotemporal organ-wide gene expression and cell atlas of the developing human heart. Cell 179(7):1647–60.e19

55. Tsubosaka A, Komura D, Kakiuchi M, Katoh H, Onoyama T, et al. 2023. Stomach encyclopedia: Combined single-cell and spatial transcriptomics reveal cell diversity and homeostatic regulation of human stomach. Cell Rep. 42(10):113236

56. Regev A, Teichmann SA, Lander ES, Amit I, Benoist C, et al. 2017. The human cell atlas. eLife 6:e27041

57. Snyder MP, Lin S, Posgai A, Atkinson M, Regev A, et al. (HuBMAP Consort.). 2019. The human body at cellular resolution: the NIH Human Biomolecular Atlas Program. Nature 574(7777):187–92

58. Kumar T, Nee K, Wei R, He S, Nguyen QH, et al. 2023. A spatially resolved single-cell genomic atlas of the adult human breast. Nature 620(7972):181–91

59. Kuppe C, Ramirez Flores RO, Li Z, Hayat S, Levinson RT, et al. 2022. Spatial multi-omic map of human myocardial infarction. Nature 608(7924):766–77

60. Lake BB, Menon R, Winfree S, Hu Q, Melo Ferreira R, et al. 2023. An atlas of healthy and injured cell states and niches in the human kidney. Nature 619(7970):585–94

61. Chen W-T, Lu A, Craessaerts K, Pavie B, Sala Frigerio C, et al. 2020. Spatial transcriptomics and in situ sequencing to study Alzheimer’s disease. Cell 182(4):976–91.e19

62. Mallach A, Zielonka M, van Lieshout V, An Y, Khoo JH, et al. 2024. Microglia-astrocyte crosstalk in the amyloid plaque niche of an Alzheimer’s disease mouse model, as revealed by spatial transcriptomics. Cell Rep. 43(6):114216

63. Zeng H, Huang J, Zhou H, Meilandt WJ, Dejanovic B, et al. 2023. Integrative in situ mapping of single-cell transcriptional states and tissue histopathology in a mouse model of Alzheimer’s disease. Nat. Neurosci. 26(3):430–46

64. Caetano AJ, Redhead Y, Karim F, Dhami P, Kannambath S, et al. 2023. Spatially resolved transcriptomics reveals pro-inflammatory fibroblast involved in lymphocyte recruitment through CXCL8 and CXCL10. eLife 12:e81525

65. Schäbitz A, Hillig C, Mubarak M, Jargosch M, Farnoud A, et al. 2022. Spatial transcriptomics landscape of lesions from non-communicable inflammatory skin diseases. Nat. Commun. 13(1):7729

66. Gurtner A, Borrelli C, Gonzalez-Perez I, Bach K, Acar IE, et al. 2023. Active eosinophils regulate host defence and immune responses in colitis. Nature 615(7950):151–57

67. Garrido-Trigo A, Corraliza AM, Veny M, Dotti I, Melón-Ardanaz E, et al. 2023. Macrophage and neutrophil heterogeneity at single-cell spatial resolution in human inflammatory bowel disease. Nat. Commun. 14(1):4506

68. Ma F, Plazyo O, Billi AC, Tsoi LC, Xing X, et al. 2023. Single cell and spatial sequencing define processes by which keratinocytes and fibroblasts amplify inflammatory responses in psoriasis. Nat. Commun. 14(1):3455

69. Cadinu P, Sivanathan KN, Misra A, Xu RJ, Mangani D, et al. 2024. Charting the cellular biogeography in colitis reveals fibroblast trajectories and coordinated spatial remodeling. Cell 187(8):2010–28.e30

70. Joyce JA. 2005. Therapeutic targeting of the tumor microenvironment. Cancer Cell 7(6):513–20

71. Berglund E, Maaskola J, Schultz N, Friedrich S, Marklund M, et al. 2018. Spatial maps of prostate cancer transcriptomes reveal an unexplored landscape of heterogeneity. Nat. Commun. 9(1):2419

72. Thrane K, Eriksson H, Maaskola J, Hansson J, Lundeberg J. 2018. Spatially resolved transcriptomics enables dissection of genetic heterogeneity in stage III cutaneous malignant melanoma. Cancer Res. 78(20):5970–79

73. Moncada R, Barkley D, Wagner F, Chiodin M, Devlin JC, et al. 2020. Integrating microarraybased spatial transcriptomics and single-cell RNA-seq reveals tissue architecture in pancreatic ductal adenocarcinomas. Nat. Biotechnol. 38(3):333–42

74. Wu SZ, Al-Eryani G, Roden DL, Junankar S, Harvey K, et al. 2021. A single-cell and spatially resolved atlas of human breast cancers. Nat. Genet. 53(9):1334–47

75. Giesen C, Wang HAO, Schapiro D, Zivanovic N, Jacobs A, et al. 2014. Highly multiplexed imaging of tumor tissues with subcellular resolution by mass cytometry. Nat. Methods 11(4):417–22

76. Angelo M, Bendall SC, Finck R, Hale MB, Hitzman C, et al. 2014. Multiplexed ion beam imaging of human breast tumors. Nat. Med. 20(4):436–42

77. Keren L, Bosse M, Marquez D, Angoshtari R, Jain S, et al. 2018. A structured tumor-immune microenvironment in triple negative breast cancer revealed by multiplexed ion beam imaging. Cell 174(6):1373–87.e19

78. Ali HR, Jackson HW, Zanotelli VRT, Danenberg E, Fischer JR, et al. 2020. Imaging mass cytometry and multiplatform genomics define the phenogenomic landscape of breast cancer. Nat. Cancer 1(2):163–75

79. Schürch CM, Bhate SS, Barlow GL, Phillips DJ, Noti L, et al. 2020. Coordinated cellular neighborhoods orchestrate antitumoral immunity at the colorectal cancer invasive front. Cell 182(5):1341–59.e19

80. Jackson HW, Fischer JR, Zanotelli VRT, Ali HR, Mechera R, et al. 2020. The single-cell pathology landscape of breast cancer. Nature 578(7796):615–20

81. Ji AL, Rubin AJ, Thrane K, Jiang S, Reynolds DL, et al. 2020. Multimodal analysis of composition and spatial architecture in human squamous cell carcinoma. Cell 182(2):497–514.e22

82. Karras P, Bordeu I, Pozniak J, Nowosad A, Pazzi C, et al. 2022. A cellular hierarchy in melanoma uncouples growth and metastasis. Nature 610(7930):190–98

83. Wu L, Yan J, Bai Y, Chen F, Zou X, et al. 2023. An invasive zone in human liver cancer identified by Stereo-seq promotes hepatocyte-tumor cell crosstalk, local immunosuppression and tumor progression. Cell Res. 33(8):585–603

84. Moffet JJD, Fatunla OE, Freytag L, Kriel J, Jones JJ, et al. 2023. Spatial architecture of high-grade glioma reveals tumor heterogeneity within distinct domains. Neurooncol. Adv. 5(1):vdad142

85. Yeh CY, Aguirre K, Laveroni O, Kim S, Wang A, et al. 2023. Mapping ovarian cancer spatial organization uncovers immune evasion drivers at the genetic, cellular, and tissue level. bioRxiv 2023.10.16.562592. https://doi.org/10.1101/2023.10.16.562592

86. Robert C. 2020. A decade of immune-checkpoint inhibitors in cancer therapy. Nat. Commun. 11(1):3801

87. Magen A, Hamon P, Fiaschi N, Soong BY, Park MD, et al. 2023. Intratumoral dendritic cell-CD4+ T helper cell niches enable CD8+ T cell differentiation following PD-1 blockade in hepatocellular carcinoma. Nat. Med. 29(6):1389–99

88. Chen JH, Nieman LT, Spurrell M, Jorgji V, Elmelech L, et al. 2024. Human lung cancer harbors spatially organized stem-immunity hubs associated with response to immunotherapy. Nat. Immunol. 25:644–58

89. Sharma A, Seow JJW, Dutertre C-A, Pai R, Blériot C, et al. 2020. Onco-fetal reprogramming of endothelial cells drives immunosuppressive macrophages in hepatocellular carcinoma. Cell 183(2):377–94.e21

90. Li Z, Pai R, Gupta S, Currenti J, Guo W, et al. 2024. Presence of onco-fetal neighborhoods in hepatocellular carcinoma is associated with relapse and response to immunotherapy. Nat. Cancer 5(1):167–86

91. Dietel M, Jöhrens K, Laffert MV, Hummel M, Bläker H, et al. 2015. A 2015 update on predictive molecular pathology and its role in targeted cancer therapy: a review focussing on clinical relevance. Cancer Gene Ther. 22(9):417–30

92. Kiuru M, Kriner MA, Wong S, Zhu G, Terrell JR, et al. 2022. High-plex spatial RNA profiling reveals cell type–specific biomarker expression during melanoma development. J. Investig. Dermatol. 142(5):1401– 12.e20

93. Janesick A, Shelansky R, Gottscho AD, Wagner F, Williams SR, et al. 2023. High resolution mapping of the tumor microenvironment using integrated single-cell, spatial and in situ analysis. Nat. Commun. 14(1):8353

94. Lyubetskaya A, Rabe B, Fisher A, Lewin A, Neuhaus I, et al. 2022. Assessment of spatial transcriptomics for oncology discovery. Cell Rep. Methods 2(11):100340

95. Hwang WL, Jagadeesh KA, Guo JA, Hoffman HI, Yadollahpour P, et al. 2022. Single-nucleus and spatial transcriptome profiling of pancreatic cancer identifies multicellular dynamics associated with neoadjuvant treatment. Nat. Genet. 54(8):1178–91

96. Cui Zhou D, Jayasinghe RG, Chen S, Herndon JM, Iglesia MD, et al. 2022. Spatially restricted drivers and transitional cell populations cooperate with the microenvironment in untreated and chemo-resistant pancreatic cancer. Nat. Genet. 54(9):1390–405

97. Oyoshi H, Du J, Sakai SA, Yamashita R, Okumura M, et al. 2023. Comprehensive single-cell analysis demonstrates radiotherapy-induced infiltration of macrophages expressing immunosuppressive genes into tumor in esophageal squamous cell carcinoma. Sci. Adv. 9(50):eadh9069

98. Derry JMJ, Burns C, Frazier JP, Beirne E, Grenley M, et al. 2023. Trackable intratumor microdosing and spatial profiling provide early insights into activity of investigational agents in the intact tumor microenvironment. Clin. Cancer Res. 29(18):3813–25

99. Patel AP, Tirosh I, Trombetta JJ, Shalek AK, Gillespie SM, et al. 2014. Single-cell RNA-seq highlights intratumoral heterogeneity in primary glioblastoma. Science 344(6190):1396–401

100. Fan J, Lee H-O, Lee S, Ryu D-E, Lee S, et al. 2018. Linking transcriptional and genetic tumor heterogeneity through allele analysis of single-cell RNA-seq data. Genome Res. 28(8):1217–27

101. Erickson A, He M, Berglund E, Marklund M, Mirzazadeh R, et al. 2022. Spatially resolved clonal copy number alterations in benign and malignant tissue. Nature 608(7922):360–67

102. Heiser CN, Simmons AJ, Revetta F, McKinley ET, Ramirez-Solano MA, et al. 2023. Molecular cartography uncovers evolutionary and microenvironmental dynamics in sporadic colorectal tumors. Cell 186(25):5620–37.e16

103. Chen L, Chang D, Tandukar B, Deivendran D, Pozniak J, et al. 2023. STmut: a framework for visualizing somatic alterations in spatial transcriptomics data of cancer. Genome Biol. 24(1):273

104. Azizi E, Carr AJ, Plitas G, Cornish AE, Konopacki C, et al. 2018. Single-cell map of diverse immune phenotypes in the breast tumor microenvironment. Cell 174(5):1293–308.e36

105. Stubbington MJT, Rozenblatt-Rosen O, Regev A, Teichmann SA. 2017. Single-cell transcriptomics to explore the immune system in health and disease. Science 358(6359):58–63

106. Singh M, Al-Eryani G, Carswell S, Ferguson JM, Blackburn J, et al. 2019. High-throughput targeted long-read single cell sequencing reveals the clonal and transcriptional landscape of lymphocytes. Nat. Commun. 10(1):3120

107. Meylan M, Petitprez F, Becht E, Bougoüin A, Pupier G, et al. 2022. Tertiary lymphoid structures generate and propagate anti-tumor antibody-producing plasma cells in renal cell cancer. Immunity 55(3):527–41.e5

108. Hudson WH, Sudmeier LJ. 2022. Localization of T cell clonotypes using the Visium spatial transcriptomics platform. STAR Protoc. 3(2):101391

109. Benotmane JK, Kueckelhaus J, Will P, Zhang J, Ravi VM, et al. 2023. High-sensitive spatially resolved T cell receptor sequencing with SPTCR-seq. Nat. Commun. 14(1):7432

110. Liu S, Iorgulescu JB, Li S, Borji M, Barrera-Lopez IA, et al. 2022. Spatial maps of T cell receptors and transcriptomes reveal distinct immune niches and interactions in the adaptive immune response. Immunity 55(10):1940–52.e5

111. Engblom C, Thrane K, Lin Q, Andersson A, Toosi H, et al. 2023. Spatial transcriptomics of B cell and T cell receptors reveals lymphocyte clonal dynamics. Science 382(6675):eadf8486

112. Boileau E, Li X, Naarmann-de Vries IS, Becker C, Casper R, et al. 2022. Full-length spatial transcriptomics reveals the unexplored isoform diversity of the myocardium post-MI. Front. Genet. 13:912572

113. Carow B, Hauling T, Qian X, Kramnik I, Nilsson M, Rottenberg ME. 2019. Spatial and temporal localization of immune transcripts defines hallmarks and diversity in the tuberculosis granuloma. Nat. Commun. 10(1):1823

114. Mantri M, Hinchman MM, McKellar DW, Wang MFZ, Cross ST, et al. 2022. Spatiotemporal transcriptomics reveals pathogenesis of viral myocarditis. Nat. Cardiovasc. Res. 1(10):946–60

115. Khan M, Yoo S-J, Clijsters M, Backaert W, Vanstapel A, et al. 2021. Visualizing in deceased COVID-19 patients how SARS-CoV-2 attacks the respiratory and olfactory mucosae but spares the olfactory bulb. Cell 184(24):5932–49.e15

116. Mothes R, Pascual-Reguant A, Koehler R, Liebeskind J, Liebheit A, et al. 2023. Distinct tissue niches direct lung immunopathology via CCL18 and CCL21 in severe COVID-19. Nat. Commun. 14(1):791

117. Wyler E, Franke V, Menegatti J, Kocks C, Boltengagen A, et al. 2019. Single-cell RNA-sequencing of herpes simplex virus 1-infected cells connects NRF2 activation to an antiviral program. Nat. Commun. 10(1):4878

118. Rybak-Wolf A, Wyler E, Pentimalli TM, Legnini I, Martinez AO, et al. 2023. Modelling viral encephalitis caused by herpes simplex virus 1 infection in cerebral organoids. Nat. Microbiol. 8:1252–66

119. Lötstedt B, Stražar M, Xavier R, Regev A, Vickovic S. 2024. Spatial host–microbiome sequencing reveals niches in the mouse gut. Nat. Biotechnol. 42:1394–403

120. Saarenpää S, Shalev O, Ashkenazy H, Carlos V, Lundberg DS, et al. 2023. Spatial metatranscriptomics resolves host-bacteria-fungi interactomes. Nat. Biotechnol. https://doi.org/10.1038/s41587- 023-01979-2

121. Salmen F, De Jonghe J, Kaminski TS, Alemany A, Parada GE, et al. 2022. High-throughput total RNA sequencing in single cells using VASA-seq. Nat. Biotechnol. 40(12):1780–93

122. McKellar DW, Mantri M, Hinchman MM, Parker JSL, Sethupathy P, et al. 2023. Spatial mapping of the total transcriptome by in situ polyadenylation. Nat. Biotechnol. 41(4):513–20

123. Gracia Villacampa E, Larsson L, Mirzazadeh R, Kvastad L, Andersson A, et al. 2021. Genome-wide spatial expression profiling in formalin-fixed tissues. Cell Genom. 1(3):100065

124. Bai Z, Zhang D, Gao Y, Tao B, Bao S, et al. 2024. Spatially exploring RNA biology in archival formalin-fixed paraffin-embedded tissues. bioRxiv 2024.02.06.579143. https://doi.org/10.1101/2024. 02.06.579143

125. Vandereyken K, Sifrim A, Thienpont B, Voet T. 2023. Methods and applications for single-cell and spatial multi-omics. Nat. Rev. Genet. 24(8):494–515

126. Androvic P, Schifferer M, Perez Anderson K, Cantuti-Castelvetri L, Jiang H, et al. 2023. Spatial transcriptomics-correlated electron microscopy maps transcriptional and ultrastructural responses to brain injury. Nat. Commun. 14(1):4115

127. Stoeckius M, Hafemeister C, Stephenson W, Houck-Loomis B, Chattopadhyay PK, et al. 2017. Simultaneous epitope and transcriptome measurement in single cells. Nat. Methods 14(9):865–68

128. Ben-Chetrit N, Niu X, Swett AD, Sotelo J, Jiao MS, et al. 2023. Integration of whole transcriptome spatial profiling with protein markers. Nat. Biotechnol. 41(6):788–93

129. Vickovic S, Lötstedt B, Klughammer J, Mages S, Segerstolpe A, et al. 2022. SM-Omics is an automated <sup>˚</sup> platform for high-throughput spatial multi-omics. Nat. Commun. 13(1):795

130. Vicari M, Mirzazadeh R, Nilsson A, Shariatgorji R, Bjärterot P, et al. 2023. Spatial multimodal analysis of transcriptomes and metabolomes in tissues. Nat. Biotechnol. 42:1046–50

131. Sun C, Wang A, Zhou Y, Chen P, Wang X, et al. 2023. Spatially resolved multi-omics highlights cellspecific metabolic remodeling and interactions in gastric cancer. Nat. Commun. 14(1):2692

132. Bao F, Deng Y, Wan S, Shen SQ, Wang B, et al. 2022. Integrative spatial analysis of cell morphologies and transcriptional states with MUSE. Nat. Biotechnol. 40(8):1200–9

133. Ghaznavi F, Evans A, Madabhushi A, Feldman M. 2013. Digital imaging in pathology: whole-slide imaging and beyond. Annu. Rev. Pathol. Mech. Dis. 8:331–59

134. Klauschen F, Dippel J, Keyl P, Jurmeister P, Bockmayr M, et al. 2024. Toward explainable artificial intelligence for precision pathology. Annu. Rev. Pathol. Mech. Dis. 19:541–70

135. Campanella G, Hanna MG, Geneslaw L, Miraflor A, Werneck Krauss Silva V, et al. 2019. Clinicalgrade computational pathology using weakly supervised deep learning on whole slide images. Nat. Med. 25(8):1301–9

136. Bulten W, Pinckaers H, van Boven H, Vink R, de Bel T, et al. 2020. Automated deep-learning system for Gleason grading of prostate cancer using biopsies: a diagnostic study. Lancet Oncol. 21(2):233–41

137. Naik N, Madani A, Esteva A, Keskar NS, Press MF, et al. 2020. Deep learning-enabled breast cancer hormonal receptor status determination from base-level H&E stains. Nat. Commun. 11(1):5727

138. Kather JN, Pearson AT, Halama N, Jäger D, Krause J, et al. 2019. Deep learning can predict microsatellite instability directly from histology in gastrointestinal cancer. Nat. Med. 25(7):1054–56

139. Coudray N, Ocampo PS, Sakellaropoulos T, Narula N, Snuderl M, et al. 2018. Classification and mutation prediction from non-small cell lung cancer histopathology images using deep learning. Nat. Med. 24(10):1559–67

140. Weinstein JN, Collisson EA, Mills GB, Shaw KRM, Ozenberger BA, et al. (Cancer Genome Atlas Res. Netw.). 2013. The Cancer Genome Atlas Pan-Cancer analysis project. Nat. Genet. 45(10):1113–20

141. Binder A, Bockmayr M, Hägele M, Wienert S, Heim D, et al. 2021. Morphological and molecular breast cancer profiling through explainable machine learning. Nat. Mach. Intell. 3:355–66

142. Bach S, Binder A, Montavon G, Klauschen F, Müller K-R, Samek W. 2015. On pixel-wise explanations for non-linear classifier decisions by layer-wise relevance propagation. PLOS ONE 10(7):e0130140

143. He B, Bergenstråhle L, Stenbeck L, Abid A, Andersson A, et al. 2020. Integrating spatial gene expression and breast tumour morphology via deep learning. Nat. Biomed. Eng. 4(8):827–34

144. Hu J, Coleman K, Zhang D, Lee EB, Kadara H, et al. 2023. Deciphering tumor ecosystems at super resolution from spatial transcriptomics with TESLA. Cell Syst. 14(5):404–17.e4

145. Zeng Q, Klein C, Caruso S, Maille P, Allende DS, et al. 2023. Artificial intelligence-based pathology as a biomarker of sensitivity to atezolizumab-bevacizumab in patients with hepatocellular carcinoma: a multicentre retrospective study. Lancet Oncol. 24(12):1411–22

146. Fortina P, Surrey S, Kricka LJ. 2002. Molecular diagnostics: hurdles for clinical implementation. Trends Mol. Med. 8(6):264–66

147. Jones RC, Karkanias J, Krasnow MA, Pisco AO, Quake SR, et al. (Tabula Sapiens Consort.). 2022. The Tabula Sapiens: a multiple-organ, single-cell transcriptomic atlas of humans. Science 376(6594):eabl4896

148. Wang Q, Ding S-L, Li Y, Royall J, Feng D, et al. 2020. The Allen Mouse Brain Common Coordinate Framework: a 3D reference atlas. Cell 181(4):936–53.e20

149. Legnini I, Emmenegger L, Zappulo A, Rybak-Wolf A, Wurmus R, et al. 2023. Spatiotemporal, optogenetic control of gene expression in organoids. Nat. Methods 20(10):1544–52

150. Schutgens F, Clevers H. 2020. Human organoids: tools for understanding biology and treating diseases. Annu. Rev. Pathol. Mech. Dis. 15:211–34

151. Bressan D, Battistoni G, Hannon GJ. 2023. The dawn of spatial omics. Science 381(6657):eabq4964

152. Vorontsov E, Bozkurt A, Casson A, Shaikovski G, Zelechowski M, et al. 2023. Virchow: a million-slide digital pathology foundation model. arXiv:2309.07778 [eess.IV]

153. Dippel J, Feulner B, Winterhoff T, Schallenberg S, Dernbach G, et al. 2024. RudolfV: a foundation model by pathologists for pathologists. arXiv:2401.04079 [eess.IV]

154. Missarova A, Jain J, Butler A, Ghazanfar S, Stuart T, et al. 2021. geneBasis: an iterative approach for unsupervised selection of targeted gene panels from scRNA-seq. Genome Biol. 22(1):333

155. Dumitrascu B, Villar S, Mixon DG, Engelhardt BE. 2021. Optimal marker gene selection for cell type discrimination in single cell analyses. Nat. Commun. 12(1):1186

156. Aevermann B, Zhang Y, Novotny M, Keshk M, Bakken T, et al. 2021. A machine learning method for the discovery of minimum marker gene combinations for cell type identification from single-cell RNA sequencing. Genome Res. 31(10):1767–80

157. Zhang Y, Petukhov V, Biederstedt E, Que R, Zhang K, Kharchenko PV. 2024. Gene panel selection for targeted spatial transcriptomics. Genome Biol. 25:35

158. Schmid KT, Höllbacher B, Cruceanu C, Böttcher A, Lickert H, et al. 2021. scPower accelerates and optimizes the design of multi-sample single cell transcriptomic studies. Nat. Commun. 12(1):6625

159. Baker EAG, Schapiro D, Dumitrascu B, Vickovic S, Regev A. 2023. In silico tissue generation and power analysis for spatial omics. Nat. Methods 20(3):424–31

160. Hossain MS, Shahriar GM, Syeed MMM, Uddin MF, Hasan M, et al. 2023. Region of interest (ROI) selection using vision transformer for automatic analysis using whole slide images. Sci. Rep. 13(1):11314