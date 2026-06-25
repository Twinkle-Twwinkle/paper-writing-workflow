# Foundations before models for AI virtual cells

**Article type:** Perspective  
**Target journal:** Nature Biotechnology  
**Running title:** Data standards for AI virtual cells  
**Authors:** [Author names]  
**Affiliations:** [Affiliations]  
**Correspondence:** [Corresponding author email]  
**Display items:** 2 figures and 1 box proposed  

<!-- Submission note: Nature Biotechnology lists Perspective articles as scholarly reviews or arguments up to 3,000 words and up to 50 references. References below use visible Nature-style fields; DOI and source-key audit links are retained in hidden comments. -->

## Abstract

AI virtual cells are usually framed as a modeling frontier: with larger omics corpora, better foundation models and richer biological priors, a predictive cell simulator should emerge. That framing misses a more basic constraint. The dominant measurement paradigm, dissociated single-cell sequencing, removes the very axes that a virtual cell must represent: time, tissue architecture and functional molecular state. Temporal dynamics are inferred from destructive snapshots; spatial context is erased before measurement; and transcriptomes cannot substitute for protein activity, post-translational regulation or metabolic flux. These gaps are not separate inconveniences to be patched downstream, but coupled consequences of how data are generated. We argue that the next milestone for AI virtual cells should be a data standard, not another scale claim: one that records spatial and temporal coordinates, spans non-interchangeable modalities, and makes measurements comparable across laboratories by design.

## Abundance is not enough

The prevailing story about AI virtual cells (AIVCs) is one of abundance. Two revolutions, in artificial intelligence and in omics, are said to enable cell models learned directly from data; measurement throughput has grown rapidly, reference datasets have been doubling on short timescales, and these measurements increasingly come paired with perturbations [1]. A second, more methodological optimism runs alongside the first: compositional architectures and biological priors may stand in for measurements that are sparse, noisy or missing [2]. Together, these views frame the task ahead as one of modeling more cleverly over data that are already arriving at scale.

That conclusion is too easy. Quantity is not the same as usefulness, and the field's own benchmarks show that scaling more of the same data produces diminishing returns. Larger pretraining corpora do not reliably improve single-cell foundation models; even datasets seen during pretraining can still show poor cell-type clustering [3]. Similarly, simply adding cells or perturbations need not improve generalization across evaluation metrics [4]. The optimistic accounts concede the same point from another direction: diversity, not size alone, governs model quality, and unequal representation across species, disease states and human populations encodes biases that training cannot remove [1]. Priors and compositional models can help under sparsity, but without diverse observations even the best models and largest datasets fall short of biological complexity [2].

The bottleneck, then, is not whether models can be made more ingenious. It is that the cells we feed them are incomplete at the source. AIVCs need data that preserve time, tissue position and functional state. The dominant pipeline instead starts by dissociating tissue and ends by destroying the measured cell. These are not three independent defects to be repaired one benchmark at a time. They are three symptoms of a shared measurement choice (Fig. 1).

## Time is the missing coordinate

The deepest gap is temporal, and its cause is physical rather than procedural. Single-cell RNA sequencing destroys the cell it records, so expression in the same cell and its descendants cannot be followed across time [5]. What remains is a static snapshot. To reconstruct dynamics from that snapshot, algorithms must add assumptions that restrict the set of trajectories able to generate the observed distribution [6]. This is not a small inconvenience for biology. It is a fundamental obstacle for time-resolved processes such as embryogenesis, regeneration, immune activation and disease progression [7].

The field has responded with a remarkable set of workarounds: pseudotime, RNA velocity, optimal transport, lineage barcoding and live imaging. Their abundance is itself diagnostic. Pseudotime is useful, but its scale is numerically arbitrary and varies from experiment to experiment [8]. RNA velocity adds directionality, but depends on kinetic assumptions such as constant gene-specific splicing rates that can fail [9]. Optimal-transport inference captures the time-varying component of a distribution, but is blind to systems in dynamic equilibrium. If asynchronously dividing cells change individually while the population distribution stays constant, optimal transport infers stasis [5]. In a review of 62 trajectory approaches, 33 were not applicable to developmental time courses, 25 were applicable but ignored time, and only four used time while still failing to model growth rates [5].

Lineage information helps precisely because it imports what the transcriptomic snapshot lacks. Integrating lineage history with transcriptomic state captures differentiation with higher fidelity than transcriptomes alone [10]. Yet lineage barcoding, the most direct workaround, usually requires genetic engineering and is therefore restricted to model organisms; natural-variant approaches are more applicable to human samples but lack temporal control [10]. Live imaging, the one method that follows the same living cell over time, currently reads morphology such as size and shape rather than the molecular state needed for an AIVC [11]. None of this means that the field has neglected time. It means the opposite: when a quantity can be measured directly, one rarely needs so many incompatible ways to infer it.

## Space cannot be reconstructed after dissociation

The spatial gap is better recognized. Dissociation makes single-cell sequencing possible, but it irreversibly discards tissue architecture and the spatial relationships between cells and their microenvironment [12,13]. That loss is not cosmetic. Cell neighborhoods can have an unexpected and profound effect on the protein receptors displayed by immune cells [14], and tumor immune resistance must be interpreted in the spatial context of the cellular neighborhood [1].

Nor can the gap be closed by collecting more dissociated cells. A foundation model trained on dissociated data alone failed to recover the complexity of spatial microenvironments even when given three times as much spatial data, indicating that dissociated data cannot capture spatial variation by scale alone [15]. This is the encouraging contrast with time: spatial omics offers direct experimental routes to recover what dissociation removes. Space is the better-charted missing axis. But its lesson is general. If the coordinate was erased before measurement, downstream models are left to infer what the experiment chose not to record.

## Modalities are not interchangeable

Even with time and space restored, RNA alone cannot reconstruct a cell. Modalities carry information that is complementary rather than redundant. Surface protein separates CD4+ and CD8+ T cells that the transcriptome partially blends, while RNA resolves other populations that surface protein does not [16]. Phosphorylation state, not total protein or mRNA abundance, tracks transcription-factor activity in relevant contexts [17]. Single-cell metabolomes can classify metabolic phenotypes with near-perfect discriminatory power, information that expression levels alone do not encode [18].

A serious objection is that the mRNA-protein gap largely reflects measurement noise rather than orthogonal biology. That argument should be met directly. Technical ability to quantify mRNA and protein does influence their measured correlation, and noise in protein quantification can explain several-fold more variance in mRNA-protein correlation than some biological factors [19]. But the noise-only account fails where it matters. If discordance were mainly independent measurement error, improvements in transcriptomic and proteomic accuracy should have increased observed correlations; they have not. Instead, transcriptome and proteome regulation are distinct in dynamic settings such as development and disease [20]. A causal genetic design that equalized environmental confounders and most technical bias found that fewer than 20% of loci acted concordantly on mRNA and protein of the same gene, with most influencing protein but not mRNA [21].

The discordance is therefore regulation, not merely artifact. At the same time, the noise objection usefully relocates the problem. Reported mRNA-protein correlations across cancer studies range widely and are not directly comparable because studies use different summary statistics, correlation metrics and protein-inclusion rules [19]. The strongest argument against multimodality becomes an argument for a standard.

## A standard before another scaling race

The temporal, spatial and modal gaps share a fourth consequence: the data that do exist are siloed and difficult to compare. Only about a quarter of public datasets provide the cell-level metadata needed for reuse [22]. A single analysis choice can substantially change a reported result: recomputing one colon-cancer study over all proteins, rather than only the most variable tenth, changed the mRNA-protein correlation from 0.48 to 0.27 [19]. Mass-spectrometry intensity values from different workflows are not directly comparable unless spike-in standards or equivalent calibration strategies are used [20].

The exit is therefore not more models, and not more homogeneous RNA data. It is a data standard for AI virtual cells: a minimal but explicit schema for what a measured cell must carry if it is to train a model of living state. Such a standard should include spatial coordinates and tissue context, temporal information or lineage constraints, perturbation and sampling metadata, and paired functional modalities where they are biologically non-substitutable (Box 1). It should also define calibration and interoperability requirements so that measurements remain comparable across laboratories, platforms and model-building teams.

This goal is not alien to model-first visions of AIVCs. The same entity profiled with different technologies should have the same internal representation in a virtual cell [1]. Minimal schemas can also be practical. CELLxGENE Discover, for example, limits required cell-level metadata fields to a small set considered most valuable for integration and reuse, showing that standards need not become submission barriers [22]. The point is not to demand every modality for every cell. It is to define which coordinates must be present, pairable or explicitly absent, so that the missingness is itself modeled rather than silently inherited.

The standard is buildable rather than aspirational. Spatial proteomics already preserves tissue context while recovering deep molecular information: deep visual proteomics links protein abundance to cellular and subcellular phenotypes while preserving spatial context [23]; spatial single-cell mass spectrometry resolves around 1,700 proteins from a hepatocyte slice, with roughly half the proteome spatially regulated [24]; tissue-scale strategies have mapped more than 9,000 proteins across mouse brain regions [25]; and automated single-cell proteomics can quantify thousands of protein groups per cell without carrier material [26]. These examples show that the data demanded by an AIVC standard can be produced.

Honesty requires the complement to that claim. These methods still largely observe snapshots, and the temporal axis remains open even in advanced spatial proteomics [24]. Proteins are also harder to measure than transcripts because they are abundant, structurally heterogeneous and cannot be amplified [27]. A standard should not pretend that these problems are solved. It should name them precisely enough that methods, benchmarks and model architectures can compete on the same task.

## Outlook

AI virtual cells will not be rescued by scale if scale means more cells stripped of the coordinates that make them biological. The community should therefore define an AIVC-ready data standard before the next generation of models hardens around incompatible assumptions. That standard should specify the required spatial, temporal and modal fields; the acceptable proxies when direct measurement is impossible; the calibration needed for cross-platform comparison; and the open benchmarks required to test whether models preserve biological fidelity rather than only reconstruction loss. Trajectory-inference benchmarks have already called for shared interfaces and consensus around uncertainty and gene importance [28]. AIVCs need the same logic applied upstream to measurement itself: open data resources, data standards, benchmark datasets and common validation strategies [1]. The models will be only as good as the cells we give them. It is time to decide, precisely and collectively, what those cells should contain.

## Figure legends

**Fig. 1 | Measurement losses in the dominant single-cell pipeline.** Dissociation and destructive sequencing generate high-throughput molecular snapshots but remove three axes required for virtual-cell modeling: temporal continuity, tissue architecture and functional molecular state. Downstream inference methods can partially repair each axis, but cannot recover information that was never recorded.

**Fig. 2 | A data standard for AI virtual cells.** A proposed AIVC-ready measurement schema links each profiled cell or spatial unit to coordinates, lineage or sampling-time information, perturbation state, paired modalities, calibration metadata and platform provenance. The aim is not maximal measurement of every sample, but explicit comparability and explicit missingness.

## Box 1 | Minimal fields for an AIVC-ready dataset

1. Biological identity: species, tissue, disease or developmental state, donor and cell annotation provenance.
2. Spatial context: tissue coordinate, neighborhood definition, resolution and whether the sample was dissociated.
3. Temporal context: sampling time, lineage information, live-imaging link, pulse-chase label or explicit indication that time is inferred.
4. Perturbation context: perturbation identity, dose, duration, delivery method and control structure.
5. Modal coverage: RNA, chromatin, protein abundance, protein activity or phosphorylation, metabolome and morphology, with pairing relationships stated.
6. Calibration and comparability: spike-ins, batch controls, normalization strategy, instrument or platform metadata and missing-data semantics.
7. Reuse metadata: cell-level schema fields, licenses, accession identifiers and links to raw and processed data.

## References

1. Bunne, C. et al. How to build the virtual cell with artificial intelligence: priorities and opportunities. Cell 187, 7045-7063 (2024). <!-- source key 01; doi:10.1016/j.cell.2024.11.015 -->
2. Bahrami, M., Richter, T., Schmacke, N. A., Egea Lavandera, A. & Theis, F. J. From modality-specific to compositional foundation models for cell biology. Cell Syst. 17, 101534 (2026). <!-- source key 03; doi:10.1016/j.cels.2026.101534 -->
3. Kedzierska, K. Z., Crawford, L., Amini, A. P. & Lu, A. X. Zero-shot evaluation reveals limitations of single-cell foundation models. Genome Biol. 26, 101 (2025). <!-- source key 04; doi:10.1186/s13059-025-03574-x -->
4. Wei, Z. et al. Benchmarking algorithms for generalizable single-cell perturbation response prediction. Nat. Methods 23, 451-464 (2026). <!-- source key 05; doi:10.1038/s41592-025-02980-0 -->
5. Schiebinger, G. et al. Optimal-transport analysis of single-cell gene expression identifies developmental trajectories in reprogramming. Cell 176, 928-943.e22 (2019). <!-- source key 21; doi:10.1016/j.cell.2019.01.006 -->
6. Bergen, V., Lange, M., Peidli, S., Wolf, F. A. & Theis, F. J. Generalizing RNA velocity to transient cell states through dynamical modeling. Nat. Biotechnol. 38, 1408-1414 (2020). <!-- source key 25; doi:10.1038/s41587-020-0591-3 -->
7. La Manno, G. et al. RNA velocity of single cells. Nature 560, 494-498 (2018). <!-- source key 24; doi:10.1038/s41586-018-0414-6 -->
8. Trapnell, C. et al. The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells. Nat. Biotechnol. 32, 381-386 (2014). <!-- source key 27; doi:10.1038/nbt.2859 -->
9. Chen, C., Liao, Y. & Peng, G. Connecting past and present: single-cell lineage tracing. Protein Cell 13, 790-807 (2022). <!-- source key 23; doi:10.1007/s13238-022-00913-7 -->
10. Kang, Z., Chen, H., Li, S., Wang, S. W. & Zhou, B. Evolving strategies for lineage tracing: genetic markers, synthetic barcodes, and natural variants. Cell Stem Cell (2026). <!-- source key 22; doi:10.1016/j.stem.2026.05.001 -->
11. Zargari, A. et al. DeepSea is an efficient deep-learning model for single-cell segmentation and tracking in time-lapse microscopy. Cell Rep. Methods 3, 100500 (2023). <!-- source key 30; doi:10.1016/j.crmeth.2023.100500 -->
12. Pentimalli, T. M., Karaiskos, N. & Rajewsky, N. Challenges and opportunities in the clinical translation of high-resolution spatial transcriptomics. Annu. Rev. Pathol. 20, 405-432 (2025). <!-- source key 13; doi:10.1146/annurev-pathmechdis-111523-023417 -->
13. Cervilla, S. et al. A technical comparison of spatial transcriptomics platforms across six cancer types. Genome Biol. 27, 22 (2026). <!-- source key 11; doi:10.1186/s13059-026-03937-y -->
14. Goltsev, Y. et al. Deep profiling of mouse splenic architecture with CODEX multiplexed imaging. Cell 174, 968-981.e15 (2018). <!-- source key 14; doi:10.1016/j.cell.2018.07.010 -->
15. Tejada-Lapuerta, A. et al. Nicheformer: a foundation model for single-cell and spatial omics. Nat. Methods 22, 2525-2538 (2025). <!-- source key 07; doi:10.1038/s41592-025-02814-z -->
16. Hao, Y. et al. Integrated analysis of multimodal single-cell data. Cell 184, 3573-3587.e29 (2021). <!-- source key 37; doi:10.1016/j.cell.2021.04.048 -->
17. Blair, J. D. et al. Phospho-seq: integrated, multi-modal profiling of intracellular protein dynamics in single cells. Nat. Commun. 16, 1346 (2025). <!-- source key 35; doi:10.1038/s41467-025-56590-7 -->
18. Wang, Z. et al. Integrative single-cell metabolomics and phenotypic profiling reveals metabolic heterogeneity of cellular oxidation and senescence. Nat. Commun. 16, 2740 (2025). <!-- source key 36; doi:10.1038/s41467-025-57992-3 -->
19. Upadhya, S. R. & Ryan, C. J. Experimental reproducibility limits the correlation between mRNA and protein abundances in tumor proteomic profiles. Cell Rep. Methods 2, 100288 (2022). <!-- source key 34; doi:10.1016/j.crmeth.2022.100288 -->
20. Guo, T., Steen, J. A. & Mann, M. Mass-spectrometry-based proteomics: from single cells to clinical applications. Nature 638, 901-911 (2025). <!-- source key 31; doi:10.1038/s41586-025-08584-0 -->
21. Brion, C., Lutz, S. M. & Albert, F. W. Simultaneous quantification of mRNA and protein in single cells reveals post-transcriptional effects of genetic variation. eLife 9, e60645 (2020). <!-- source key 33; doi:10.7554/eLife.60645 -->
22. CZI Cell Science Program et al. CZ CELLxGENE Discover: a single-cell data platform for scalable exploration, analysis and modeling of aggregated data. Nucleic Acids Res. 53, D886-D900 (2025). <!-- source key 40; doi:10.1093/nar/gkae1142 -->
23. Mund, A. et al. Deep Visual Proteomics defines single-cell identity and heterogeneity. Nat. Biotechnol. 40, 1231-1240 (2022). <!-- source key 17; doi:10.1038/s41587-022-01302-5 -->
24. Rosenberger, F. A. et al. Spatial single-cell mass spectrometry defines zonation of the hepatocyte proteome. Nat. Methods 20, 1530-1536 (2023). <!-- source key 19; doi:10.1038/s41592-023-02007-6 -->
25. Qin, R., Ma, J., He, F. & Qin, W. In-depth and high-throughput spatial proteomics for whole-tissue slice profiling by deep learning-facilitated sparse sampling strategy. Cell Discov. 11, 21 (2025). <!-- source key 18; doi:10.1038/s41421-024-00764-y -->
26. Ctortecka, C. et al. Automated single-cell proteomics providing sufficient proteome depth to study complex biology beyond cell type classifications. Nat. Commun. 15, 5707 (2024). <!-- source key 32; doi:10.1038/s41467-024-49651-w -->
27. Kiessling, P. & Kuppe, C. Spatial multi-omics: novel tools to study the complexity of cardiovascular diseases. Genome Med. 16, 14 (2024). <!-- source key 20; doi:10.1186/s13073-024-01282-y -->
28. Saelens, W., Cannoodt, R., Todorov, H. & Saeys, Y. A comparison of single-cell trajectory inference methods. Nat. Biotechnol. 37, 547-554 (2019). <!-- source key 26; doi:10.1038/s41587-019-0071-9 -->

## Statements

**Acknowledgements:** [To be completed.]  
**Author contributions:** [To be completed.]  
**Competing interests:** [To be completed.]  
**Data availability:** No original data are reported in this Perspective.  
