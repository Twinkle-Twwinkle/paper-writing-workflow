# A technical comparison of spatial transcriptomics platforms across six cancer types

## Abstract

Background: Spatial transcriptomics (ST) technologies are reshaping our understanding of tissue organization and cellular context in health and disease. However, technical benchmarking across platforms remains limited, particularly in formalin-fxed, parafnembedded (FFPE) clinical samples, which represent the most common tissue format in oncology.

Results: Here, we systematically benchmark fve commercial ST platforms (Visium v1, Visium v2/CytAssist, Visium HD, Xenium, and CosMx) using matched FFPE human tumor sections from six cancer types. Uniquely, our study includes both sequencingbased and imaging-based platforms profled on the same samples, enabling direct technical comparisons across spatial capture modalities. We evaluate platform performance across multiple dimensions, including transcript and UMI detection, gene–histology concordance, cell type recovery, and integration with a targeted protein panel (Visium v2, 30 proteins), enabling spatial multi-omics. We also quantify the impact of sampling strategies and area coverage on cell type estimation, revealing trade-ofs in spatial resolution versus tissue context. Notably, we present the frst same-sample comparison of Xenium Multi-Tissue (377 genes) and Xenium Prime (5,000 genes), highlighting key diferences in transcript recovery and spatial signal despite shared chemistry and imaging infrastructure. Finally, we integrate Visium targeted protein data with matched RNA profles, uncovering widespread RNA–protein decoupling and spatial heterogeneity in concordance.

Conclusions: Collectively, this work provides a harmonized dataset and technical reference for the spatial transcriptomics community, ofering insight into the relative strengths, limitations, and design considerations associated with high-throughput spatial profling of FFPE tumors.

## Background

Personalized cancer care relies on the molecular and cellular characterization of individual tumors. Over the past decade, large-scale eforts such as Te Cancer Genome Atlas [1], the International Cancer Genome Consortium (ICGC) [2], and the Clinical Proteogenomics Tumor Analysis Consortium [3] have expanded our understanding of oncogenic processes through the analysis of bulk molecular profles. Tese projects have helped identify cancer driver genes [4, 5], map interactions between cancer cells and their surrounding tumor microenvironment through bulk-RNA deconvolution [6, 7], and defne catalogs of clinically actionable mutations [8, 9]. However, by averaging signals across heterogeneous cell populations, bulk profling obscures the cellular diversity and spatial context that shape tumor behavior.

Single-cell omics technologies partially address this limitation by enabling the analysis of molecular profles at single-cell resolution. Tis has uncovered extensive mutational [10], epigenetic [11], and transcriptional [12] heterogeneity in both cancer and immune cells. Yet, these methods require dissociation of the tissue, thereby destroying the spatial relationships between cells and their microenvironment. Tis information is critical the context of most diseases, including solid tumors, where spatial organization infuences cell signaling, immune infltration, and therapeutic response.

Spatial omics technologies bridge this gap by capturing molecular information while preserving spatial architecture [13]. Advances in spatial profling now allow measurement of DNA alterations [14], epigenetic modifcations [15], and, most commonly, RNA [16–23] and protein [24–26] expression, directly within intact tissue sections. Among these, spatial transcriptomics has become one of the most widely used approaches in cancer research, in large part due to the growing availability of commercial platforms. Tese platforms can be classifed into two groups depending on the readout used to quantify gene expression. On the one hand, we have sequencing-based technologies such as VISIUM [16], or SlideSeq [22]. Tese rely on the use of nucleic acid tags to identify the location of the molecule within the slide. On the other hand, other platforms (such as CosMx [20], Xenium [23] or MERFISH [18]) rely on in situ imaging of the RNA molecules, which are identifed with fuorescent probes.

To systematically evaluate the technical performance of current spatial transcriptomics technologies, we profled six FFPE tumor types using fve commercially available platforms: Visium v1, Visium v2 (CytAssist), VisiumHD, Xenium, and CosMx. Our analysis reveals several consistent trends. Visium v2 improves upon its predecessor in gene detection and spatial coherence, refecting the combined efects of updated probe chemistry and analyte transfer. Among imaging-based platforms, Xenium consistently demonstrates lower background noise and stronger spatial signal than CosMx, though both yield comparable cell type classifcations. VisiumHD combines whole-transcriptome coverage with near single-cell resolution, albeit with increased data sparsity and new computational challenges. To assess the impact of panel complexity on performance, we also compared the standard 377-gene Xenium Multi-Tissue panel with the 5,000-gene Xenium Prime panel across matched tumor samples. Tis revealed a clear trade-of between transcript recovery and gene coverage, underscoring the technical consequences of high-plex imaging. Finally, we integrated matched targeted spatial protein measurements to assess concordance between RNA and protein distributions.

Overall, our fndings provide a harmonized technical reference to support the interpretation, comparison, and integration of data across diverse spatial omics platforms.

## Results

## Generation of matching spatial transcriptomics and proteomics data

Te experimental design involved consecutive sectioning of formalin-fxed, parafnembedded (FFPE) tumor samples, followed by spatial transcriptomics profling across multiple platforms and standardized data processing to enable direct comparison (Fig. 1a). To control for confounding variables, tissue sections were registered to a shared spatial coordinate system, allowing analysis of overlapping regions across platforms. Tis strategy ensured consistency in tissue sampling and enabled the systematic evaluation of platform performance. With this framework, we addressed key questions in the feld, including the comparative sensitivity and resolution of new imaging- and sequencingbased technologies, the efects of optical crowding due to gene panel size, and the spatial concordance between transcriptomic and proteomic measurements.

<table><tr><td rowspan="2"></td><td colspan="5">Platform characteristics</td><td colspan="2">Data generated</td></tr><tr><td>Platform</td><td>Gene panel</td><td>Resolution</td><td>Number of features</td><td>Cell segmentation</td><td>Samples</td><td>Section</td></tr><tr><td rowspan="4">Sequencing-based</td><td>VISIUM manual</td><td>v1 WT Panel Gene Expression</td><td>55 μm</td><td>17,943 genes</td><td>None</td><td></td><td>1</td></tr><tr><td rowspan="2">VISIUM CytAssist</td><td>v2 WT Panel Gene Expression</td><td>55 μm</td><td>18,085 genes</td><td>None</td><td></td><td>9</td></tr><tr><td>v2 WT Panel Protein Expression</td><td>55 μm</td><td>35 proteins</td><td>None</td><td></td><td>9</td></tr><tr><td>VISIUM HD</td><td>v2 WT Panel Gene Expression</td><td>2 μm</td><td>18,085 genes</td><td>None</td><td></td><td>16</td></tr><tr><td rowspan="4">Imaging-based</td><td rowspan="3">Xenium</td><td>Human Multi-Tissue and Cancer</td><td>Single-cell</td><td>377 genes</td><td>Nuclear expansion</td><td></td><td>7</td></tr><tr><td>Human Multi-Tissue and Cancer</td><td>Single-cell</td><td>377 genes</td><td>Multi-modal</td><td></td><td>22</td></tr><tr><td>Prime 5K Human</td><td>Single-cell</td><td>5000 genes</td><td>Multi-modal</td><td></td><td>23</td></tr><tr><td>CosMx</td><td>Human Universal Cell Characterization Panel</td><td>Single-cell</td><td>1000 genes</td><td>Multi-modal</td><td></td><td>8</td></tr></table>

We generated spatial transcriptomics data (Visium v1, Visium v2, VisiumHD, Xenium Multi-tissue with and without multi-modal cell segmentation, Xenium Prime, and CosMx Universal Cell Characterization) from six primary untreated tumor samples covering some of the most common cancer types: colorectal (adenocarcinoma), breast (infltrating carcinoma of non-special type), lung (acinar invasive adenocarcinoma), lymphoma (difuse large B-cell lymphoma), ovarian (high-grade serous carcinoma), and bladder (muscle-invasive bladder cancer) (Fig. 1b).

All spatial transcriptomics experiments were successfully completed, with the exception of the Visium v2 breast cancer sample. In that case, the tissue partially detached during the $9 5 ~ ^ { \circ } \mathrm { C }$ decrosslinking step, leading to folding and library failure, likely attributable to its high lipid content [27]. However, we had previously generated high-quality Visium v2 data from the same sample using the larger 11.5 mm capture area, which was used in the analyses presented here. Targeted spatial protein measurements data were also generated using the Visium v2 immuno-oncology panel (n <sub>=</sub> 35 proteins), although the breast sample was excluded from this dataset due to the same technical issue. Overall, after fltering low-quality spots and cells (Methods), we captured 18,672 spots with Visium v1, 33,117 spots with Visium v2, 2,551,540 8 8 µm bins with VisiumHD, 667,916 cells with CosMx, and 5,809,890 cells with Xenium (Additional fle 1: Table S1).

To illustrate how platform iterations difer in performance, we began by comparing Visium v1 and Visium v2, both of which ofer 55 μm resolution with whole transcriptome coverage, and together account for the majority of existing Visium datasets. While both rely on the same spatial barcoding framework, Visium v2 incorporates a revised workfow and a three-probe per gene design, improving compatibility with degraded RNA and enhancing detection sensitivity. In matched FFPE samples, Visium v2 consistently detected more unique genes (\~ 2,000 vs. \~ 200; Fig. 1c), captured more UMIs per spot, and exhibited stronger spatial autocorrelation (Moran’s I), particularly for lowly expressed genes (Additional fle 2: Fig. S1). Tese improvements translated into clearer spatial patterns, exemplifed by ACTA2 expression in colorectal cancer (Fig. 1d). Taken together, these results highlight how even within-platform upgrades can substantially afect data quality and spatial interpretability.

## Technical comparison of imaging‑based platforms: CosMx vs Xenium

An emerging alternative to sequencing-based spatial transcriptomics platforms are those based on in situ transcript quantifcation through imaging. Tese approaches use fuorescent probes and high resolution imaging to localize individual mRNA molecules at subcellular resolution, assigning them to individual cells through image-based segmentation. Among the available platforms, we focused on two widely adopted systems: CosMx (NanoString) and Xenium (10 Genomics).

While both platforms follow similar principles, they difer in gene panel size, imaging approach, and cell segmentation strategies. Importantly, neither currently ofers full transcriptome coverage but instead rely on targeted panels. For Xenium, we generated three datasets: (1) Xenium Multi-Tissue 377-gene panel (XeniumMT) without multi-modal cell segmentation; (2) XeniumMT with cell segmentation, generated using updated software and chemistry; and (3) Xenium Prime, which includes a high-plex 5,000-gene panel (Xenium5K) with multi-modal cell segmentation. Te CosMx dataset was generated using its Universal Cell Characterization 1,000-gene panel. Notably, the CosMx and initial XeniumMT (no segmentation) datasets were generated from serial sections processed together, making them the most directly comparable. Te two additional Xenium datasets were generated months later, once updated reagents and protocols became available, and are thus less directly comparable to the rest of the cohort (Additional fle  2: Fig. S2). Accordingly, in this section, we focus on the comparison between the CosMx and XeniumMT (no segmentation) datasets, while the results of the other Xenium datasets are detailed sections below.

Te platforms, Xenium and CosMx, also difer in acquisition strategy and segmentation methodology. Xenium scans a continuous tissue area up to 1.1 <sub>×</sub> 2.4 cm, whereas CosMx captures discrete, user-defned 0.5 <sub>×</sub> 0.5 mm felds of view (FOVs). In our study, each CosMx sample included an average of 58 FOVs, covering a total of 87.5 mm<sup>2</sup> across all tissues, compared to 394.7 mm<sup>2</sup> imaged with Xenium. Notably, since we scanned a larger area with Xenium than with CosMx, to ensure that the results are comparable we limited our analyses to the shared areas after tissue alignment (Additional fle 2: Fig. S3). Another diference stems from the segmentation in each platform. Tis version of Xenium uses DAPI staining to identify nuclei and computationally expands boundaries to approximate full-cell areas. CosMx, in contrast, incorporates both nuclear (DAPI) and membrane staining, enabling more precise delineation of cell compartments. Although both platforms provide default segmentation methods, external algorithms, such as Baysor [28], can also be applied, making it possible to integrate imaging information and the spatial density of transcripts for more fexible or customized segmentation.

Tese technical diferences were refected in the data. For example, in terms of cell counts, Xenium consistently detected 5% to 30% more cells than CosMx (Fig. 2a), probably refecting the diferences in the segmentation strategy. To ensure fair comparison, we excluded cells located at the edges of CosMx FOVs, as cells at FOVs borders often have transcript counts an order of magnitude lower than those at the center (Fig. 2b). To further test whether diferences in segmentation strategies could explain the discrepancy in cell counts. On average, Xenium-segmented cells were larger than those detected by CosMx across all tumor types except lymphoma (Fig. 2c). Tis size diference was especially pronounced in low-density regions, where Xenium’s nucleus-based segmentation tends to expand cell boundaries in the absence of neighboring cells (Fig.  2d). We also observed occasional extreme outliers (cell area > 1,000  µm<sup>2</sup>), primarily driven by this expansion efect. In contrast, CosMx’s use of membrane staining likely constrains segmentation in these regions. In densely packed areas, Xenium segmentation based on nucleus expansion sometimes failed to cleanly separate adjacent cells, which may further contribute to variability in cell size, even when mean values appear comparable.

We then compared per-cell gene and transcript detection across platforms. Using each platform’s full gene panel, CosMx consistently detected 2 to 3 times more genes and transcripts per cell than Xenium across all tumor types (Fig. 2e, f, “All”), consistent with its larger panel size. To isolate platform-specifc efects from panel content, we repeated the analysis using only the 125 genes shared between both panels. Under this constraint, the number of genes detected per cell was similar between platforms: Xenium detected slightly more genes in lung and ovarian samples, while CosMx had a modest advantage in colorectal sample (Fig. 2e, “Int”). When comparing transcript counts per cell for these shared genes, Xenium consistently outperformed CosMx across all samples (Fig.  2f, “Int”), suggesting higher detection efciency on a per-gene basis.

Next, we assessed assay specifcity across the two technologies by examining the performance of negative control probes, which are designed not to hybridize with any known RNA sequences. Detection of these probes indicates non-specifc binding or background signal. When comparing the proportion of negative control signals relative to gene signals, normalized by the panel size, we found that CosMx exhibited a negative probe signal rate of approximately 10.31%, while Xenium demonstrated a markedly lower rate of 0.06% (Additional fle  3: Table  S2). Consistently, the signal-to-noise ratio (ratio of gene probe counts to negative probe counts) was substantially higher in Xenium. Specifcally, gene probes in CosMx yielded approximately 3 times more counts than negative probes, whereas in Xenium, this ratio was approximately 450 (Additional fle 2: Fig. S4).

To benchmark the in  situ platforms against a sequencing-based reference, we compared gene-level expression profles to those obtained with Visium v2. Using UMI density per gene as the comparison metric, Xenium showed a stronger correlation with Visium v2 (Pearson R <sub>=</sub> 0.93) than CosMx (R <sub>=</sub> 0.86) across all tumor types (Fig.  2g, Additional fle  2: Fig. S5). Tis discrepancy was most pronounced for lowly expressed genes, which in CosMx often had UMI densities indistinguishable from those of negative control probes, suggesting limited reliability for low-abundance transcripts. To assess spatial concordance, we aggregated Xenium and CosMx data into pseudospots matching the resolution of Visium v2 and compared the resulting spatial expression patterns (Additional fle  2: Fig. S6). Tis analysis further supported higher agreement between Xenium and Visium v2, particularly in the distribution of genes with low expression. Tese fndings suggest that Xenium reproduces more similar spatial expression profles captured by sequencing-based approaches.

Diferences in gene expression localization and efciency can be evaluated by examining marker distribution across tissues. For example, ADGRL4 (ELTD1), a gene associated with angiogenesis and tumor-associated endothelial cells [29], exhibited distinct localization patterns between platforms: in Xenium, expression was confned to specifc regions of the colorectal sample, while in CosMx it appeared more dispersed and not aligned with blood vessels (Fig.  2h). Tis observation was consistent with global spatial autocorrelation metrics, where CosMx showed a tendency toward lower Moran’s I values compared to Xenium (Additional fle 2: Fig. S7), indicating weaker spatial clustering overall. However, lower Moran’s I values do not necessarily refect poorer biological fdelity for all genes. For example, ACTG2, which encodes gamma (γ)<sub>−</sub>2 actin, is expected to be predominantly expressed in smooth muscle cells [30]. While CosMx accurately restricted ACTG2 expression to non-epithelial cells, Xenium reported substantial signal within epithelial cells across multiple tumor types. Tis pattern was not supported by Visium v2 data, suggesting that CosMx provided more biologically faithful localization in this instance despite having a lower or similar Moran’s I score (Additional fle 2: Fig. S8).

Finally, we also examined the impact of RNA quality and observed a strong correlation between DV200 and the average number of genes detected per cell in both platforms, emphasizing the importance of RNA integrity for spatial transcriptomics (Fig. 2i).

## Biological concordance and interpretability across in situ platforms

Given the diferences in panel size, sensitivity, background noise, and segmentation strategies, we next asked whether CosMx and Xenium would yield consistent biological insights. As in the previous section, we focused the analysis on CosMx and XeniumMT (no segmentation) to minimize interpretation biases arising from diferences in tissue sections. We annotated all cells from both platforms using SingleR [31], leveraging reference expression profles to assign putative cell identities (Additional fle  2: Figs. S9, S10). To assess whether platform-specifc biases afected downstream interpretation, we re-examined transcriptomic and morphological features stratifed by cell type. Overall, platform diferences mirrored those observed in the global analysis, but with additional nuance. For example, in low-density regions, fbroblasts consistently appeared larger in Xenium due to its nucleus-based segmentation approach (Figs.  3a, S11). By contrast, in the lymphoma sample, T and NK cells showed smaller sizes in Xenium, potentially refecting cell-dense regions where boundary assignment is less accurate. When examining gene and transcript detection for the 125 shared genes, epithelial cancer cells were consistently well-resolved across platforms. In contrast, immune cells, particularly T cells and myeloid populations, showed higher variability between platforms in both transcript counts and detected gene numbers.

We also assessed whether these technical diferences afected estimates of overall cell type composition. Across most tumors, the inferred cell fractions from CosMx and Xenium were broadly similar when restricted to spatially matched tissue regions. Te main exception was the bladder sample, where CosMx reported more epithelial cells and fewer immune and stromal cells than Xenium (Fig. 3b). We also observed systematic differences in the annotation of the myeloid compartment: although the total proportion of monocytes and macrophages was comparable, CosMx consistently assigned fewer cells to the monocyte subset.

Beyond platform-specifc biases, we found that cell composition estimates could also vary substantially depending on the area of tissue analyzed, even when using a single platform. In Xenium, cell type proportions calculated from the full scanned region differed from those in the CosMx-overlapping area in two samples (breast and colorectal), despite being similar in the other four. Tese observations highlight the potential for sampling bias when spatial studies rely on small tissue regions.

We next investigated how well each platform resolved immune cell subtypes and their spatial organization. In the lung and lymphoma samples, both of which contained a high proportion of immune cells, we compared the distributions of B and T cell subtypes inferred from CosMx and Xenium. Subtype frequencies were largely consistent between platforms, with minor discrepancies in the relative abundance of memory versus naive B cells, as well as efector versus regulatory T cells (Fig. 3c, Additional fle 2: Fig. S12).

To determine whether these diferences were extended to spatial organization, we analyzed the spatial distribution of annotated cell types across tissue sections. Te classifcation of epithelial and cancer cells within tumor nest regions at the tumor– stroma interface of the colorectal sample revealed comparable spatial patterns across platforms, closely refecting the underlying tissue architecture (Fig. 3d, left). In contrast, within stromal regions, we observed a higher proportion of fbroblast cells misclassifed as cancer cells in the CosMx dataset (71.6% in CosMx vs. 10.2% in Xenium).

Examination of fner anatomical structures, such as blood vessels, indicated that endothelial cell annotations did not fully delineate the vascular architecture in either platform (Fig.  3d, right). Tis discrepancy was more pronounced in CosMx, where endothelial structures were largely absent (8.51% endothelial cells in CosMx vs. 28.7% in Xenium). Nevertheless, in both datasets, the spatial localization of endothelial cell classifcations corresponded well with the expression of canonical endothelial markers (PECAM1, VWF, CD34) (Additional fle 2: Fig. S13). Together, these fndings suggest that while both platforms capture broad spatial patterns consistently, diferences in gene detection efciency become critical when assessing fner spatial features.

Given the observed sensitivity of cell composition estimates to sampled area, we systematically evaluated how tissue coverage infuences biological interpretation. In many spatial studies, researchers can only analyze small regions, such as tissue microarrays, due to sample availability or cost [32]. To quantify potential biases introduced by sampling such small regions, we used the full Xenium dataset to simulate random sampling of tissue areas equivalent in size to individual CosMx FOVs (0.5 <sub>×</sub> 0.5 mm). We then computed the inferred cell type composition based on increasing numbers of FOVs and compared these estimates to those obtained from the entire scanned region. As expected, compositional accuracy improved with the number of sampled regions. However, sampling only a single FOV yielded highly variable estimates. For example, the inferred proportion of cancer cells ranged from 5 to 55%, whereas the true value for the entire sample was 22% (Fig. 3e, Additional fle 2: Fig. S14). As a control, we did an analogous simulation by randomly selecting an equivalent number of single cells from across the full tissue area, mimicking a single-cell experiment without spatial constraints. In this case, the variability was markedly reduced and consistently closer to the ground truth. Tese results illustrate how spatial constraints, even when total cell numbers are matched, can introduce substantial variability in cell type composition estimates, highlighting the importance of scanned area in the design and interpretation of spatial transcriptomics experiments.

While cell type composition and spatial patterns were broadly comparable across platforms, we identifed important gene-specifc diferences with potential biological and clinical implications. For instance, the MMP7 gene (associated with invasive tumor, distant metastasis [33], and chemotherapy resistance in colorectal cancer [34]) is absent from the Xenium Multi-Tissue panel. In our colorectal tumor sample, CosMx detected strong MMP7 expression in epithelial cells located at the invasive front near stromal boundaries (Fig. 3f ). Tis signal enabled spatial subtyping of cancer cells with potential relevance to tumor progression, an insight that would have been missed using XeniumMT due to its limited panel content.

Together, these analyses reveal that even when imaging-based platforms yield broadly consistent estimates of cell type composition, important diferences remain in how they resolve transcript localization and biological meaning. Xenium demonstrated lower background, stronger spatial coherence, and higher efciency for shared genes, while CosMx provided broader transcriptome coverage and more precise subcellular localization for select markers. Tese diferences were particularly evident in gene-level analyses and in cell types with sparse or context-specifc expression. As spatial transcriptomics is increasingly used to uncover functional heterogeneity and microenvironmental interactions, understanding these trade-ofs is essential. In the following sections, we extend this comparison by analyzing more recent Xenium datasets that incorporate cell segmentation and expanded gene panels.

## Efect of panel size in Xenium results

Imaging-based spatial transcriptomics platforms have historically been limited by modest gene panel sizes. Recent updates have expanded this capacity, with CosMx and Xenium now ofering panels of up to \~ 6,000 and \~ 5,000 genes, respectively. However, larger panels may sufer from reduced sensitivity due to optical crowding, an efect in which high probe density compromises accurate signal resolution [35]. To evaluate this trade-of between panel size and sensitivity, we directly compared two Xenium panels of diferent sizes: the 377-gene Multi-Tissue panel (XeniumMT) and the 5,000-gene Human Prime panel (Xenium5K). We profled consecutive tissue sections from fve tumor types using both panels, applying the same multi-modal segmentation workfow to control for potential confounders.

Both panels yielded comparable numbers of segmented cells within matched tissue regions, with no signifcant diferences in cell size distributions, confrming segmentation consistency across datasets (Additional fle  2: Fig. S15). As expected, the larger Xenium5K panel detected more total genes and transcripts (Fig.  4a, b). However, this increase was not proportional to the \~ 13-fold diference in panel size. When focusing on 225 genes shared between panels, XeniumMT consistently detected more transcripts and genes per cell, indicating higher sensitivity for overlapping targets. Importantly, panel specifcity, measured by signal from negative control probes (20 for XeniumMT, 40 for Xenium5K), was comparable across datasets, with similar negative probe rates and signal-to-noise ratios (Additional fle 3: Table S2, Additional fle 2: Fig. S16).

We next compared UMI densities from both Xenium panels to Visium v2 data from the same colorectal sample. Both XeniumMT and Xenium5K showed high overall correlation with Visium (R <sub>=</sub> 0.92–0.93; Fig. 4c, Additional fle 2: Fig. S17), but Xenium5K produced \~ threefold fewer transcripts per gene, consistent with reduced per-gene sensitivity. Tis reduction in transcript detection was aligned with lower Moran’s I values for Xenium5K (Additional fle 2: Fig. S18), suggesting diminished spatial coherence. For example, MYC expression in the colorectal adenocarcinoma sample retained its overall spatial localization, but was markedly sparser in Xenium5K, leading to diferences in the proportion of cancer cells classifed as MYC-positive: 70% in XeniumMT versus 30% in Xenium5K (Fig. 4d). Tese discrepancies underscore how panel size can infuence downstream biological interpretation.

Despite these sensitivity diferences, broader gene coverage improved certain aspects of cell identity resolution. Cell type annotation with SingleR revealed largely consistent compositions across panels, though epithelial and fbroblast proportions shifted in ovarian and breast tumors (Fig.  4e). In the ovarian sample, epithelial cells at the tumor–stroma interface were often misclassifed as fbroblasts in XeniumMT, where misclassifed epithelial cells represented 12% of cells in this region, compared with < 1% in Xenium5K (Fig.  4f), suggesting that a broader transcriptomic context can enhance classifcation accuracy. Furthermore, Xenium5K enabled deeper subclassifcation of immune cell types, including distinctions among B and T cell subsets (Additional fle 2: Fig. S19), demonstrating the added value of large panels for resolving fne-grained cellular phenotypes, even at the cost of per-gene resolution.

Lastly, we compared all in situ datasets generated across platforms and gene panels. Here it is important to be aware that some diferences may arise from underlying variations in tissue cell composition due to distance between sections in the Z-axis (Fig.  4i). We found that cell sizes derived from CosMx segmentation more closely resembled those estimated by nuclear expansion, whereas Xenium’s multi-modal approach yielded systematically smaller areas. Within the XeniumMT datasets, increasing cell area contributed to a slight rise in the number of genes and transcripts detected. As expected, the number of genes and transcripts increased with broader transcriptome coverage; however, CosMx (1,000-gene panel) and Xenium5K detected a comparable number of transcripts overall. Consistent with our earlier observations, larger panels showed reduced per-gene detection efciency for the 91 shared genes.

In summary, our comparison of the Xenium Multi-Tissue and 5 K panels revealed a clear trade-of between gene coverage and per-gene sensitivity. While the larger panel improved cell type annotation and enabled deeper immune subtyping, it exhibited lower transcript detection efciency and higher sparisity. Tese fndings emphasize the importance of empirically evaluating panel performance within each application context, particularly when panel expansion may impact transcript-level resolution.

## Subcellular resolution and whole‑transcriptome coverage

Te platforms evaluated thus far require a trade-of between spatial resolution and transcriptome breadth: Visium (v1 and v2) provides whole-transcriptome coverage at multicellular resolution, whereas CosMx and Xenium ofer subcellular resolution but are limited to targeted gene panels. VisiumHD represents a new class of technology that may ofer both: single-cell or subcellular resolution with whole-transcriptome coverage.

Like other Visium platforms, VisiumHD is sequencing-based, but its capture array consists of a dense, contiguous grid of 2 <sub>×</sub> 2  µm square bins, each bearing a unique spatial barcode, rather than sparse 55 µm spots. Each capture area spans 6.5 <sub>×</sub> 6.5 mm, yielding \~ 11 million bins at native resolution. While this brings the resolution to a sub-cellular level, it has extraordinary computational costs. To mitigate this, coarser bin aggregations (e.g., 8 µm or 16 µm per side) are typically used, reducing bin counts to \~ 700  K and \~ 160  K, respectively. However, this binning strategy introduces tradeofs: larger bins may include transcripts from multiple cells, while smaller bins may fragment single-cell transcriptomes. To quantify this efect, we overlaid simulated binning grids onto Xenium datasets and calculated two metrics: the fraction of bins containing transcripts from multiple cells, and the number of bins occupied per cell (Fig. 5a).

Tese simulations revealed that bin size signifcantly afects data granularity. At 2 µm resolution, most bins contain transcripts from only one cell; in contrast, 8 µm bins frequently capture transcripts from 2–4 cells, and 16 µm bins from 5–10 cells, with variation across tumor types and cell type specifcity (Additional fle  2: Fig. S20). Similarly, the average number of bins per cell ranges from \~ 10–25 at 2 µm to just \~ 1–5 at 16 µm. Tools such as Bin2Cell [36] attempt to reconstruct single-cell expression profles by aggregating bins using H&E images and transcript data.

We then evaluated the actual VisiumHD data. Transcript distributions correlated well with tissue morphology, and median UMI counts per bin were broadly consistent across samples (\~ 100–300), except for the lung, which showed an order-ofmagnitude lower expression (Additional fle 2: Fig. S21). A notable technical artifact, striping aligned with VisiumHD’s grid structure, was observed, consistent with prior reports, and may afect downstream analyses. At the gene level, VisiumHD correlated strongly with both Visium v2 (R > 0.97) and Xenium (R > 0.85; Fig.  5c), though UMI density was \~ 3 lower than Visium v2 and \~ 15 lower than Xenium. Nevertheless, gene expression patterns in VisiumHD remained spatially aligned with tissue architecture, with increased data sparsity likely attributable to its binning strategy and partial cell capture (Fig. 5d).

We next assessed VisiumHD’s performance in cell type annotation and biological signal recovery. SingleR-based classifcation at the bin level recapitulated gross tissue organization observed in Xenium (Additional fle 2: Fig. S22), but also revealed systematic diferences in cell type proportions. VisiumHD showed a relative overrepresentation of epithelial and stromal cells compared to immune cells (Fig. 5e), a bias that may arise from cell size: larger cells span more bins and are thus overcounted (Fig.  5f ). Despite this, proportions of fner cell types, such as B and T cell subsets, were largely consistent across platforms. Notably, efector T cells were underrepresented in the lymphoma sample in VisiumHD, likely due to incomplete capture of CCR7 (Additional fle 2: Fig. S23, S24). Unsupervised clustering of the whole-transcriptome data uncovered additional subpopulations, including infammatory, SPP1<sub>+</sub>, and SELENOP<sub>+</sub>macrophages in ovarian tumors, subtypes not detected in Xenium (Additional fle 4: Table S3). However, we also observed artifactual clusters in both platforms driven by marker gene contamination from adjacent cells. For instance, EPCAM <sub>+</sub> SOX17 <sub>+</sub> macrophages in Xenium and WFDC2 MUC16 macrophages in VisiumHD were localized near epithelial cells (Fig. 5g, Additional fle 2: Fig. S25), suggesting technical misassignment due to either bin mixing (VisiumHD) or limited transcript coverage (Xenium).

In addition to cell classifcation, spatial transcriptomics is increasingly used to assess the activity of gene programs and pathways that drive tumor behavior. Such analyses provide a more functional view of tissue organization and can reveal gradients or niches not captured by discrete cell type annotations. To illustrate this, we examined hypoxiaassociated gene expression in ovarian tumors, a pathway linked to microenvironmental remodeling, mesenchymal transition, and resistance to therapy. Pathway-level inference is challenging in panel-based platforms due to limited gene coverage, which may compromise scoring accuracy or exclude key regulators. In contrast, VisiumHD’s whole transcriptome resolution enabled robust hypoxia scoring, revealing heterogeneous expression patterns consistent with those observed in Visium v2 (Fig. 5h).

While the overall spatial landscape was concordant between VisiumHD and Visium v2, the higher resolution of VisiumHD allowed for fner mapping of hypoxia gradients and improved association of pathway activity with specifc tissue features. By contrast, the lower resolution of Visium v2 limited the ability to confdently associate pathway scores with individual cell states or microenvironmental neighborhoods. Tese results underscore the potential of VisiumHD to extend spatial transcriptomics beyond descriptive profling and into the domain of functional tissue mapping, provided its known limitations in bin sparsity and technical artifacts are appropriately accounted for.

## Correlation of transcriptomics and proteomics measurements across space

To assess how well spatial transcriptomics recapitulates protein-level abundance, we generated spatial proteomics data using the Visium v2 Immuno-Oncology panel, which targets 35 proteins. Tis assay, integrated into the standard Visium workfow, uses oligotagged antibodies that bind proteins and are co-barcoded with the spatial capture spots, enabling RNA and protein quantifcation from adjacent sections.

Across the fve analyzed tumor samples, we observed weak global correlation between transcript and protein levels. Te average Pearson correlation coefcient across all genes and samples was approximately 0.1 (Fig.  6a), substantially lower than the \~ 0.7 average correlation observed in matched bulk tumor samples from the Clinical Proteomic Tumor Analysis Consortium (CPTAC) across seven cancer types (Fig. 6b). Tis discrepancy underscores the added complexity of spatially resolved RNA–protein relationships, which may refect biological regulation, technical factors, or both.

When examining individual genes, we identifed three distinct RNA–protein concordance patterns. In the frst, we observed positive spatial correlations between RNA and protein for genes with robust transcript detection and coherent spatial structure, such as ITGAX in the lung tumor (Fig. 6c, top). In the second pattern, correlations were near zero, typically involving genes with low transcript abundance despite protein presence, such as KRT5 in the same lung sample (Fig. 6c, bottom). A third, more complex pattern involved partial concordance, where RNA and protein signals overlapped in some regions but diverged in others. For example, CD68 transcript levels were elevated in the upper-left region of the lung tumor, adjacent to adipose tissue, while protein levels were high in both this region and a distinct area in the lower-right (Fig. 6d).

To explore this discrepancy, we performed cross-platform validation using Xenium data from the same tissue block, registering the Xenium and Visium v2 images and generating pseudo-spots for direct comparison. Te RNA expression of CD68 inferred from Xenium largely matched the protein spatial pattern, including the extended signal in the lower-right region (Fig.  6e), suggesting that the divergence may result from platformspecifc technical variability rather than true biological dissociation. When we systematically evaluated this across additional genes, most discordant spatial patterns were rare, with the bladder sample being a notable exception (Fig. 6f).

In summary, spatial co-profling of RNA and protein reveals diverse expression relationships, including cases of high concordance, low transcript capture, and platformspecifc divergence. While bulk data suggests consistent RNA–protein coupling, our spatial analysis demonstrates that these relationships are context-dependent and may vary across regions, cell types, and technologies.

## Discussion

Spatial -omics technologies, particularly spatial transcriptomics, are reshaping our understanding of tissue organization, cell–cell interactions, and disease processes at an unprecedented resolution [37–40]. Among their many applications, cancer research stands to beneft most directly, as spatial profling enables the study of intratumoral heterogeneity, tumor–immune interactions, and microenvironmental remodeling. However, the rapid proliferation of spatial transcriptomics platforms has introduced a new challenge: selecting the most appropriate platform for a given biological question, tissue type, or translational goal.

To help guide researchers facing these decisions, we conducted a systematic comparison of fve spatial transcriptomics platforms across six human tumor types, all derived from FFPE tissue blocks. We focused on FFPE specimens due to their widespread use in both clinical and research settings. Wherever possible, serial sections were processed on the same day to minimize batch efects and ensure comparability of histological features. Tis design enabled us to assess a broad range of technical attributes, including sensitivity, resolution, spatial signal integrity, and RNA–protein concordance.

Our benchmarking aligns with, and extends, recent eforts in the feld. Prior studies have compared in situ platforms across various tissues [41–44], but few have included matched sequencing-based platforms, and none have systematically profled Visium v1, Visium v2, and VisiumHD within the same framework. Consistent with previous reports, we found that Xenium generally exhibited lower background signal and higher gene–histology concordance than CosMx, particularly for low-abundance genes. However, CosMx benefted from membrane staining, resulting in more anatomically plausible cell segmentations. Interestingly, despite these technical diferences, both platforms produced comparable estimates of cell type composition in most tissues, highlighting the relative robustness of coarse cell classifcation to upstream variability.

Our study also provides the frst direct comparison between Visium v1 and Visium v2 using the same tissue samples. Visium v2 signifcantly improved transcript capture and spatial signal, likely due to both probe design (triplicate probes per gene) and enhanced analyte transfer. Tese improvements underscore that even intra-platform upgrades can meaningfully afect data quality and interpretation. Moreover, we quantifed the impact of tissue area selection on cell composition estimates—a critical consideration given the growing use of tissue microarrays and spatially constrained profling to increase cohort size. Our simulations demonstrate that small sampling areas can yield highly variable and potentially biased cell fraction estimates, particularly for heterogeneous tumors.

A unique feature of this study is the within-platform comparison of two gene panels in Xenium: the 377-gene Multi-Tissue panel and the 5,000-gene Prime panel. While Xenium Prime increased gene coverage and enabled fner immune subclassifcation, it also resulted in reduced transcript-level sensitivity and higher sparsity. Tese fndings refect a fundamental trade-of in spatial profling: broader panels may introduce optical crowding and compromise detection fdelity, particularly for low-abundance genes. Researchers should consider whether their study goals prioritize cell state diversity or quantitative accuracy when selecting panel complexity.

We also evaluated VisiumHD, the only platform currently ofering whole-transcriptome coverage at subcellular resolution. Despite its potential, VisiumHD presented challenges, including lower UMI density, incomplete library saturation, and spatial artifacts related to its gridded capture design. Nonetheless, it faithfully recapitulated tissue morphology and enabled the detection of rare or transcriptionally subtle cell populations not captured by in  situ platforms. Tese observations suggest that VisiumHD may be particularly valuable for exploratory or discovery-oriented studies, especially when combined with image-based bin-to-cell assignment tools that mitigate bin mixing.

We further incorporated targeted spatial protein measurements using the Visium FFPE multi-omic assay, enabling side-by-side RNA and protein mapping. While we observed moderate RNA–protein correlation at the cancer type level in bulk data, spatial profles often diverged. Tis suggests that local microenvironmental efects, post-transcriptional regulation, and protein stability contribute to RNA–protein decoupling in situ, fndings that are masked in aggregate measurements but critical for translational insight.

Several limitations should be noted. First, spatial transcriptomics is a fast-moving feld, and our data refect the capabilities of each platform as of mid-2025. For example, CosMx now ofers a whole-transcriptome panel, which was not available at the time of data generation. Second, while we included several major platforms, our study does not cover other important technologies such as MERFISH, Slide-seq, or Stereo-seq. Tird, although we processed serial sections from the same FFPE blocks when possible, some comparisons (particularly those involving newer chemistries like Xenium Prime) used tissue sections generated at later time points, potentially introducing Z-axis variability. Also, this study was designed as a technical comparison rather than a biological discovery exercise, and does not assess how platform choice infuences downstream interpretation of spatial biology in disease contexts. Finally, while this study ofers a detailed technical reference, it is not intended as a platform recommendation or usage guide [27]. Each spatial technology presents strengths and limitations that must be considered in light of specifc biological questions, tissue constraints, and study designs. Instead, our aim is to highlight the consequences of technical diferences (such as bin size, segmentation strategy, sampling area, and gene panel design) for downstream data sparsity, resolution, and interpretability. Tese comparisons may also help guide the development of computational methods that are platform-aware and robust to modality-specifc artifacts.

In summary, this work provides a harmonized technical benchmark of fve commercial ST platforms using matched FFPE cancer tissues. Our results highlight critical tradeofs in spatial resolution, transcript sensitivity, sparsity, and feld-of-view coverage across sequencing-based and imaging-based approaches. By controlling for biological and procedural confounders, we isolate platform-specifc efects and provide a reference dataset for tool developers, methods evaluators, and researchers planning future spatial studies. We anticipate that this resource will inform the design of spatial workfows and the interpretation of spatial features in clinical samples, especially as spatial -omics expands toward routine translational applications.

Looking forward, clinical translation of spatial technologies will require more than technical optimization. Platforms must demonstrate reproducibility, regulatory compliance, and integration with standard pathology workfows, particularly in FFPE tissues. Benchmarking eforts such as ours provide a foundational step in identifying platformspecifc trade-ofs and operational constraints under real-world conditions. As spatial -omics continues to expand into chromatin accessibility, spatial epigenomics, and multimodal proteogenomics, the need for rigorous, same-sample comparisons will only grow. Future atlas-scale initiatives and translational studies should incorporate both technical benchmarking and biological validation to ensure that spatial insights are not only highquality, but also biologically and clinically meaningful.

## Conclusions

Collectively, this work provides a harmonized dataset and technical reference for the spatial transcriptomics community, ofering insight into the relative strengths, limitations, and design considerations associated with high-throughput spatial profling of FFPE tumors.

## Methods

## Sample acquisition

All tumor samples were obtained under the ethics committee approval 2022/78-APA-HUGC.

## Tissue preparation and sequential sectioning

For our benchmarking purpose, we selected six untreated primary tumor samples, covering the most common cancer types: colorectal, breast, lung, lymphoma, ovarian, and bladder. Te H&E staining from each formalin-fxed parafn-embedded (FFPE) blocks, helped us to characterize the tissues and confrmed that each sample had an adequate and good quality representation, not only of tumor tissue but also of the surrounding healthy tissue, to warrant the experiments.

First, the quality of preserved RNA in the FFPE blocks was evaluated based on the percentage of RNA fragments above 200 base pairs (DV200). For each block, we sectioned and collected three consecutive 8  μm sections for RNA extraction using the RNeasy FFPE kit for RNA Purifcation (Qiagen Cat No: 73504). We analyzed the purifed RNA with Agilent tapestation, and chose the samples with values above 34% of DV200. Te dimensions of the tissue in the selected blocks were approximately 7  mm by 7  mm, except in the bladder sample that the block was formed by small pieces of tissue from the same patient.

To facilitate a comprehensive comparison of data from Visium v1, Xenium, CosMx, and Visium v2 platforms, we sectioned the chosen samples as illustrated in Fig. 1b. More in detail, from each of these samples we had collected and processed one 7um section for Visium v1 analysis 6 months ago, and we had stored the blocks at 4 degrees. For the benchmarking study we retrieved the blocks, discarded between 5 to 10—5 μm sections and collected three 7 μm serial sections for Xenium, CosMx, Visium v2 analysis and one extra for H&E staining.

Te sectioning was conducted using a semi-automated microtome (TermoScientifc HM340E), utilizing a fresh blade and ensuring thorough decontamination with RNAse AWAY (TermoFisher Scientifc). We detail the sectioning and subsequent slide preparation methods for Visium v1, Visium v2, Xenium and CosMx in each chapter.

## Visium v1 whole‑transcriptome

FFPE samples were placed in the microtome and sectioned 7  µm thick. After foating on a water bath at 42 °C, sections were placed on Visium Spatial Gene Expression slides (2000233, 10X Genomics). Afterwards, the slides were dried at 42 °C for 3 h. Te slides were then placed inside a slide mailer, sealed with paraflm, and left overnight at Room temperature. Deparafnization was performed by successive immersions in xylene and ethanol followed by H&E staining according to Demonstrated Protocol (CG000409, 10X Genomics).

Brightfeld images were taken using a 10X objective (Plan APO) on a Nikon Eclipse Ti2, images were stitched together using NIS-Elements software (Nikon) and exported as tif fles. After imaging, the glycerol and cover glass were carefully removed from the Visium slides by holding the slides in an 800  ml water beaker and letting the glycerol difuse until the cover glass detached and density changes were no longer visible in the water. Te slides were then dried at 37 °C.

Libraries were prepared according to the Visium Spatial Gene Expression for FFPE User Guide (CG000407, 10X Genomics) and sent for sequencing Using HiseqX 150PE (2 <sub>×</sub> 150 bp) applying 1% Phix. Sequencing was performed using the specifc protocol for Visium v1 FFPE read protocol: read 1: 28 cycles; i7 index read: 10 cycles; i5 index read: 10 cycles; read 2: 50 cycles.

## Visium v2 whole‑transcriptome and protein panel (Cytassist enabled)

Visium v2 with the protein panel provides whole-transcriptome, spatially-barcoded sequence data. Te histology workfow was performed using the Visium v2 Spatial Gene Expression for FFPE (Demonstrated Protocol CG000520, 10 Genomics). Te tissue was sectioned as described in Visium v2 Spatial Gene Expression for FFPE – Tissue Preparation Guide (Demonstrated Protocol CG000518, 10 <sub>×</sub> Genomics). 7 μm sections were cut, foated in an RNAse-free water bath at 42 degrees, and carefully placed on a

Microscope Slide (Epredia, cat # 10149870) the slides were incubated at 42 degrees per 3 h and kept in a sealed bag with desiccators at room temperature overnight.

On the day of the experiment, the Microscope slides containing tissue sections were deparafnized and stained for H&E. Samples were imaged using a Nikon microscope (Nikon Eclipse Ti2), after imaging with brightfeld, the coverslip was removed, followed by hematoxylin destaining and decrosslinking (Demonstrated Protocol CG000520, 10 Genomics). Afterwards, Microscope slides with tissue sections were incubated with whole transcriptome human probes overnight for hybridization, then probe ligation was performed, and probe release was enable using Visium v2 instrument to transfer analytes from tissue to a Visium v2 Spatial Gene Expression slide with 6.5 <sub>×</sub> 6.5 mm capture areas.

Te library construction for gene and protein expression was done following 10 <sub>×</sub> genomics User Guide CG000494. Briefy after probe ligation, samples were incubated with the protein panel, and two libraries were generated per sample.

Gene Expression and Protein Expression Libraries were sequenced with paired-end dual-indexing (28 cycles Read 1, 10 cycles i7, 10 cycles i5, 50 cycles Read 2). Sequencing libraries were demultiplexed with bcl2fastq (Illumina). Te Space Ranger pipeline v2.1 (10 Genomics) and the GRCh38-2020-A reference were used to process FASTQ fles.

## Xenium sample preparation for multi‑tissue panel without cell segmentation

Te Xenium workfow began by sectioning 5  μm FFPE tissue sections onto a Xenium slide, according to the "Xenium In Situ for FFPE- Tissue Preparation Guide" (CG000578 Rev C, 10X Genomics). Briefy, the sections were cut, foated in an RNAse-free water bath at 42 degrees, and carefully placed onto the capture area of a Xenium slide (PN-1000465). We strategically placed three 7 7 mm sections in each slide. After sectioning, the slides were incubated at 42 degrees per 3 h, and kept in a sealed bag with desiccators at 4 degrees overnight. Te next day, the slides were shipped to the Dresden Genome Center Facility, where the experiments were conducted.

At the Dresden Genome Center Facility, the Xenium slides were processed following the "Xenium In  Situ for FFPE- Deparafnization and Decrosslinking" protocol (CG000580 Rev C, 10X Genomics). Te slides were equilibrated to room temperature and the protocol of deparafnization was performed.

Subsequently, the Xenium slides were assembled into Xenium cassettes (PN-1000566, 10X Genomics), which allow for the incubation of slides on the Xenium Termocycler Adapter inside a Termocycler machine with a closed lid for optimal temperature control. Te slides were processed using the "Xenium Slides and Sample Prep Reagents" kit (PN-1000460, 10X Genomics), starting with incubation in a decrosslinking and permeabilization solution at 80 ̊C for 30 min, followed by a wash with PBS-T.

Te Xenium slides were then processed according to the "Xenium In  Situ Gene Expression" user guide (CG000582 Rev D, 10X Genomics). Te slides were incubated at 50 ̊C overnight for aproximately 19 h with the gene expression panel ("Xenium Human Multi-Tissue and Cancer Panel", PN-1000626, 10X Genomics, which targets 377 human genes). Tis was followed by a series of washes and steps, including a post-hybridization wash at 37 ̊C for 30  min, a ligation at 37 ̊C for 2  h, and an amplifcation step at 30 ̊C for 2 h. After additional washing steps, the slides were treated with an autofuorescence quencher and a nuclei staining step.

Finally, at the end of the second day of the protocol, the two slides in the cassettes were loaded into the Xenium Analyzer. Te frst step in the instrument consists in a sample scan, were images of the fuorescent nuclei in each section are given, and these images allow the user to select and determine the regions to be included in the analysis. For the 6 samples, we selected all the tissue to be analyzed.

Te run in the Xenium Analyzer lasted around 50 h. After that, the instrument was emptied of consumables and the Xenium slides carefully removed. PBS-T was added to the slides and a post-run H&E staining was performed.

## Xenium sample preparation for multi‑tissue panel with cell segmentation

For enhanced cell segmentation, we used the 10 <sub>×</sub> Genomics Cell Segmentation Staining Cocktail (PN-1000661) during sample preparation, which provides membrane staining compatible with the Xenium Analyzer.

Te methodology for Xenium Multi-tissue panel adding the cell segmentation cocktail, starts with tissue sectioning according to “Tissue Preparation Guide" (CG000578 Rev C, 10X Genomics), is followed by Demonstrated protocol CG000580 for “Deparafnization and decrosslinking”. After PBS-T washes, the processing must follow User Guide CG000749 “Xenium In Situ Gene Expression with Cell segmentation staining”. Briefy, after amplifcation, a blocking step and an overnight antibody incubation is performed at 4ºC to stain with specifc cell membrane markers. On the next day, Stain Enhancement, autoforescence treatment and nuclei staining are performed and the Xenium slides are load into the Xenium Analyzer.

## Xenium Prime (5000 genes) sample preparation

Te Xenium Prime workfow began by sectioning 5  μm FFPE tissue sections onto a Xenium slide, according to the "Xenium FFPE Tissue Preparation Guide" (CG000578 Rev C, 10X Genomics). Briefy, the sections were cut, foated in an RNAse-free water bath at 42 ̊C, and carefully placed onto the capture area of a Xenium slide (PN- 3000941). After sectioning, the slides were incubated at 42 ̊C per 3 h and kept in a sealed bag with desiccators at room temperature overnight.

Te next day, the slides were incubated at 60 degrees for 30 min and the slides were processed following the "Xenium In Situ for FFPE- Deparafnization and Decrosslinking" protocol (CG000580 Rev D, 10X Genomics). After deparafnization, the Xenium slides were assembled into Xenium cassettes, which allow for the incubation of slides on the Xenium Termocycler Adapter inside a Termocycler machine with a closed lid for optimal temperature control, and Decrosslinking step was performed.

Te slides were then processed using the “Xenium Prime In Situ Gene Expression protocol” (CG000760 Rev A, 10X Genomics) with Cell Segmentation reagents.

Briefy, after Priming hybridization and Rnase treatment, the samples were incubated at 50 ̊C overnight for approximately 19 h with the Xenium Prime Human Panel which targets 5000 human genes. Tis was followed by a series of washing steps, a ligation step, and amplifcation. Afterward, the slides were treated with an autofuorescence quencher and a nuclei staining.

Finally, at the end of the third day of the protocol, the slides were loaded into the Xenium Analyzer. Te frst step in the Xenium instrument consists in a sample scanning, where images of the fuorescent nuclei in each section are given, and these images allow the user to select and determine the regions to be included in the analysis.

After selecting all samples, the run in the Xenium Analyzer lasted 7 days. Te instrument was emptied of consumables, and the Xenium slides carefully removed. PBS-T was added to the slides, and a post-run H&E staining was performed.

## CosMx data generation

Te FFPE blocks from each sample were sectioned as described in CosMx Tissue Preparation Guide (MAN-10184–02, Nanostring). Briefy, 7 μm sections were cut, foated in an RNAse-free water bath at 42 degrees, and carefully placed onto the center of a Microscope Slide (Superfrost Plus, Epredia J1800AMNZ), considering the specifc area the CosMx instrument can analyze. After sectioning, the slides were incubated at 42 degrees per 3 h, and kept in a sealed bag with desiccators overnight. Te slides were shipped to NanoString Seattle for profling as part of their early technology access program (TAP).

Once in Seattle, the slides were processed following Nanostring MAN-10184–02. Briefy, the samples were baked overnight at $6 0 ~ ^ { \circ } C ,$ followed by preparation for in-situ hybridization (ISH) on the Leica Bond RXm system by deparafnization and heatinduced epitope retrieval (HIER) at $1 0 0 ~ ^ { \circ } \mathrm { C }$ for 15 min using ER2 epitope retrieval bufer (Leica Biosystems product, Tris/EDTA-based, pH 9.0). After HIER, tissue sections were digested with 3 μg/ml Proteinase K diluted in ACD Protease Plus at $4 0 ~ ^ { \circ } \mathrm { C }$ for 30 min.

Tissue sections were then washed twice with diethyl pyrocarbonate (DEPC)-treated water (DEPC H2O) and incubated in 0.00075% fducials (Bangs Laboratory) in 2X saline sodium citrate, 0.001% Tween-20 (SSCT solution) for 5 min at room temperature in the dark. Tissue sections were fxed with 10% neutral bufered formalin (NBF) for 5  min at room temperature. Fixed samples were rinsed twice with Tris- glycine bufer (0.1 M glycine, 0.1 M Tris-base in DEPC H2O) and once with 1X PBS for 5 min each before blocking with 100  mM N-succinimidyl (acetylthio) acetate (NHS-acetate, Termo Fisher Scientifc) in NHS-acetate bufer (0.1 M NaP, 0.1% Tween pH 8 in DEPC H2O) for 15 min at room temperature. Te sections were then rinsed with 2X saline sodium citrate (SSC) for 5 min and an Adhesive SecureSeal Hybridization Chamber (Grace Bio-Labs) was placed over the tissue.

NanoString ISH probes were prepared by incubation at $9 5 ~ ^ { \circ } \mathrm { C }$ for 2 min and placed on ice, and the ISH probe mix (1 nM 980 plex ISH probe, 10 nM Attenuation probes, 1 nM SMI-0006 custom, 1X Bufer R, 0.1 U/μL SUPERase•InTM [Termo Fisher Scientifc] in DEPC H2O) was pipetted into the hybridization chamber and hybridization was performed at $3 7 ^ { \circ } \mathrm { C }$ overnight. Tissue sections were washed twice in 50% formamide (VWR) in 2X SSC at $3 7 ^ { \circ } \mathrm { C }$ for 25 min, washed twice with 2X SSC for 2 min at room temperature, and blocked with 100 mM NHS-acetate in the dark for 15 min. In preparation for loading onto the CosMx SMI instrument, a custom-made fow cell was afxed to the slide.

RNA target readout on the CosMx SMI instrument was performed. Briefy, the assembled fow cell was loaded onto the instrument and Reporter Wash Bufer was fowed to remove air bubbles. A preview scan of the entire fow cell was taken, and 40–58 FOVs were placed on the tissue to match regions of interest. RNA readout began by fowing

100 μl of Reporter Pool 1 into the fow cell and incubation for 15 min. Reporter Wash Bufer (1  mL) was fowed to wash unbound reporter probes, and Imaging Bufer was added to the fow cell for imaging. Nine Z-stack images (0.8 μm step size) for each FOV were acquired, and photocleavable linkers on the fuorophores of the reporter probes were released by UV illumination and washed with Strip Wash bufer. Te fuidic and imaging procedure was repeated for the 16 reporter pools, and the 16 rounds of reporter hybridization-imaging were repeated multiple times to increase RNA detection sensitivity.

## VisiumHD data generation

VisiumHD is a single cell scale resolution whole transcriptome probe-based gene expression assay. Te VisiumHD workfow began by sectioning 7 μm FFPE tissue sections onto a Microscope Slide (Epredia, cat # 10,149,870) according to the "VisiumHD FFPE Tissue Preparation Handbook" (CG000684 Rev A, 10X Genomics). Briefy, the sections were cut, foated in an RNAse-free water bath at 42 degrees, and carefully placed onto the center of the superfrost slide. After sectioning, the slides were incubated at 42 degrees per 3 h and kept in a sealed bag with desiccators at room temperature until the day of the experiment.

Te slides were then deparafnized and stained for H&E. Te imaging was done using a Nikon microscope (Nikon Eclipse Ti2), after imaging with brightfeld, the coverslip was removed, followed by hematoxylin destaining and decrosslinking (Demonstrated Protocol CG000520, 10 <sub>×</sub> Genomics). Afterwards, Microscope slides with tissue sections were incubated with whole transcriptome human probes overnight for hybridization, then probe ligation was performed, and probe release was enable using Visium v2 instrument to transfer analytes from tissue to a VisiumHD Spatial Gene Expression slide, with $6 . 5 \times 6 . 5$ mm capture areas according to User Guide “VisiumHD Spatial Gene Expression Reagent $\operatorname { K i t } ^ { n }$ (CG000685 Rev B, 10X Genomics). After probe elution was completed, an amplifcation step was performed and library preparation was fnalized.

After library construction for gene expression was done, libraries were sent for sequencing to Macrogen Korea, and were sequenced with NovaSeq X 10B sequencing (150PE) (43 cycles Read 1, 10 cycles i7, 10 cycles i5, 50 cycles Read 2). Sequenced libraries were demultiplexed with bcl2fastq (Illumina). Te Space Ranger pipeline v3.0 (10 <sub>×</sub> Genomics) and the GRCh38-2020-A reference were used to process FASTQ fles.

## Data preprocessing of sequencing‑based spatial platforms

For Visium v1 and Visium v2, transcript count matrices from SpaceRanger (v2.1) were imported with Seurat [45] (v5). Spots were fltered based on their location since there were spots detected out of the tissue or in folded areas with misleading gene expression. Furthermore, genes with less than fve transcripts in the whole tissue were discarded. Given that for the breast sample we used the 11.5 mm capture area, we subset the tissue for a fairer comparison with the Visium v1. Ten, the gene expression was normalized using the SCTransform function from Seurat. Similar preprocessing was done in VisiumHD using $8 \times 8$ µm bins resolution. In this case, bins were fltered based on their location and low quantity of transcripts captured.

For Visium v2 samples with a protein panel, the protein expression was imported into a new assay independently of the gene expression. No additional spots or proteins were fltered out. Finally, the protein expression was normalized using the centered log ratio (CLR) method implemented in Seurat.

## Data preprocessing of image‑based spatial platforms

Gene expression profles matrices from Xenium Analyzer (v1.5.0.3) of each sample were imported using Seurat (v5). Since the CosMx run aggregated all samples within a single TileDB object, we proceeded to segregate and import each individual sample into a Seurat object based on their respective slide coordinates. During the preprocessing, only cells with no transcripts were fltered. In addition, cells of CosMx that were found in the “Barrel efect” area (see Barrel efect section) were excluded for all comparative experiments. Finally, gene expression was normalized using the SCTransform function from Seurat.

Gene expression profle matrices were processed using Seurat (v5). Data from XeniumMT without cell segmentation were generated using Xenium Analyzer (v1.5.0.3), while both XeniumMT with cell segmentation and Xenium5K used Xenium Analyzer (v3.2.1.2). For the CosMx run, which aggregated all samples into a single TileDB object, individual samples were separated based on their slide coordinates prior to import. During preprocessing, only cells with zero detected transcripts were fltered out. Additionally, CosMx cells located in the region afected by the “Barrel efect” (see Barrel Efect section) were excluded from all comparative experiments. Gene expression data were then normalized using the SCTransform function in Seurat.

## Image registration across platforms

Since we did not have a whole tissue image for CosMx, we could not apply Image Registration techniques to transfer the coordinates of Xenium to the CosMx. Terefore, we aligned the images by frst applying a rotation angle to the Xenium coordinates that was defned by overlaying the distribution of centroids in the space in an image editor software. In the case of the bladder sample, we had to separate the tissue regions as they could difer in orientation and distance. Ten we shifted the x and y coordinates of CosMx (since they covered less tissue area) based on common landmarks defned by tissue morphology. Angles and shifting specifc for each sample can be found in the code. After that, from the Xenium samples were subset by the limits of each FOV in the CosMx as well we discarded CosMx cells that were not found in the Xenium samples.

In the case of the alignment between Visium v2 and Xenium/CosMx, we applied Image Registration using the software Voltron [46] (v0.1) by defning landmarks between Xenium (DAPI) and Visium v2 (H&E) images. Ten the transformation was applied in the Visium v2 spot coordinates to use them in the Xenium space, so we could transfer the FOV limits and subset.

For the XeniumMT and Xenium5K datasets with cell segmentation, spatial alignment was performed using automated image registration via the FLANN method implemented in the Voltron package, using DAPI images. In this process, Xenium5K was mapped to the spatial reference frame of XeniumMT. To ensure consistent spatial overlap across modalities, we frst identifed the smaller tissue sample and defned its outer boundary using the concaveman [47] (v1.1) package, based on the cells from the other modality that were within 20 µm of it. Only the cells from both modalities that fell within this boundary were retained.

## Barrel efect

Cells that sufered from the “Barrel efect” in CosMx are found in 36px (4.33 um) from the edge of the FOV. To compare the gene expression in these cells with the rest of the FOV, we subsetted those cells whose centroid coordinates (x or y) concerning the FOV is smaller than 36 or bigger than 4220. Furthermore, to ensure that the diferences that we found could be related to the subsetting, we selected an area similar to the barrel efect in the middle of the FOV (between 2000 and 2100 px).

## Negative probe rate

To quantify the relative abundance of background signal across in situ spatial transcriptomics platforms, we computed the Negative Probe Rate using the following formula:

$$
\text {NegativeProbeRate} = \left(\frac {\sum_ {c = 1} ^ {C} \text {Control} _ {c}}{\sum_ {c = 1} ^ {C} \text {Control} _ {c} + \sum_ {g = 1} ^ {G} \text {Gene} _ {g}}\right) x \left(\frac {G}{C}\right),
$$

where:

• Control is the expression count from the negative control probe c.

• Gene<sub>g</sub> is the gene expression of gene g.

• C is the total number of negative control probes included in the assay.

• G is the total number of genes in the gene panel.

## Spatial Autocorrelation

To quantify the spatial variation of the normalized transcripts we use global Moran’s I metric. In Visium v1 and Visium v2, we used the function CorSpatialFeature from semla (v1.1.6) package [48] considering the six closest spots as neighbors (default). For imagebased platforms and VisiumHD, the function RunMoransI from the package Voyager [49] (v1.2.7). In this case, the spatial network was built using the fve closest neighbors considering centroid distances.

FindSpatialNeighbors(method <sub>=</sub> "knearneigh", dist\_type <sub>=</sub> "idw", k <sub>=</sub> 5, style <sub>=</sub> "W").

## Cell annotation

To annotate image-based sequencing data without reference data, we use SingleR [31] (v2.4) package to map the annotations of the following cell types: epithelial, endothelial, fbroblast, macrophage, monocyte, dendritic cell, neutrophil, NK cell, B cell, immature B cell, memory B cell, naive B cell, plasma B cell, CD4 T cell, CD8 T cell, efector T cell and Treg. Te “HumanPrimaryCellAtlasData” was used as a reference and the normalized data with SCT was used as input. Cells with labels NA after the pruning were discarded in the comparison of the technologies.

## Cell type co‑localization

To evaluate spatial co-localization patterns of cell types, we applied computed Ripley’s L function with isotropic edge correction was computed for each cell type using the Lcross(correction <sub>=</sub> "isotropic") function from the spatstat [50] (v3) package. Te analysis was performed over radii ranging from 0 to 1000 µm in 5 µm increments.

## FOV sampling experiment

To evaluate the infuence of cell type composition within a selected portion of the tissue, we conducted a sampling experiment. Initially, we treated the CosMx FOV size (0.5  mm <sub>×</sub> 0.5  mm) in the Xenium (shared area) sample as a single unit to facilitate stochastic sampling while adhering spatial constraints. Additionally, we sampled the same number of cells that appear on average in a FOV simulating a single- cell experiment without spatial constraints. Subsequently, we performed 100 iterations of sampling across various quantities of FOVs, including 1, 5, 10, 20, 40, and the maximum number of FOVs possible within the given sample. For each sampling iteration, we calculated the relative abundance of three grouped cell types: cancer (epithelial cells), stroma cells (fbroblasts, smooth muscle and endothelial cells), and immune cells (the remaining cell types).

## Transferring Xenium information to Visium v2 spot resolution

After the image registration between Xenium and Visium v2 samples, we transfer the coordinates of Visium v2 spots to the Xenium space. Ten, for each spot, we assigned the cells within a radius of 27.5 μm to the spot center. Finally, for the deconvolution we computed the relative abundance of each cell type from the assigned cells. For the gene expression, we aggregated the sum of gene transcripts found within each spot and we normalized using SCTransform.

## Unsupervised clustering of macrophages

To fnd macrophages subpopulations in VisiumHD and Xenium, this cell type was subset and renormalized using SCTtransform. Ten, dimensional reduction was applied using PCA on the variable genes. Finally, cell clusters were identifed using FindNeighbors and FindClusters from Seurat using the frst 20 PCA dimensions. Te resolution used in VisumHD was 0.3 and 0.5 for Xenium to obtain a similar number of subclusters.

## Hypoxia pathway scoring

Te transcriptional footprint of the Hypoxia pathway was extracted with PROGENy [51] (v1.17.3) using the top 1,000 genes. Ten, the pathway activity was inferred using a multivariate linear model implemented in decoupleR [52] (v2.8) using the normalized gene expression data from Visium v2 and VisiumHD. For visiualization purposes, q1 and q99 cutofs of the score were used.

## CPTAC protein and RNA analyses

We downloaded the CPTAC protein and RNA expression matrixes from Liang et al [53]. Ten, for each gene included in the 10 <sub>×</sub> Genomics Visium v2 protein panel, we calculated the correlation coefcient between the bulk RNA counts and the massspectrometry protein expression data across all 10 cancer types included in the CPTAC study using a linear model.

## Supplementary Information

The online version contains supplementary material available at https://doi.org/10.1186/s13059-026-03937-y.

Additional fle 1: Table S1. Summary of sample information and QC metrics by sample and technology.

Additional fle 2: Supplementary Figures. Additional fgures to support the analyses in this study.

Additional fle 3: Table S2. Negative probe rates in Xenium, CosMx, XeniumMT and Xenium5K samples.

Additional fle 4: Table S3. Diferentially expressed genes in macrophage subclusters in ovarian tissue.

Additional fle 5. Review history.

## Acknowledgements

We thank the patients who generously donated their samples. We also would like to thank Luciano Martelotto and Nuria Malats for helpful discussions of the results. This work was supported by Nanostring and Longwood Laboratories (who funded the CosMx experiments), 10x Genomics and Bonsai Labs (who funded the Xenium experiments), and Asociación Española Contra el Cáncer (who funded the VISIUM experiments, LABAE20038PORT). S.C is supported by AECC (LABAE-20038PORT). E.P-P is supported by the Spanish Ministry of Science (RYC2019-026415-I), a Fundación FERO fellowship (BFERO2022.6), grant PID2024-159258OB-I00 funded by MICIU/AEI/ 10.13039/501100011033 and Departament de Recerca i Universitats/Generalitat de Catalunya (2021 SGR 01309). S.C. is supported by the FI-STEP predoctoral grants program of the Department of Research and Universities of the Government of Catalonia (Generalitat de Catalunya), and cofnancing by the European Social Fund Plus (2025 STEP 00466) ME is supported by MCIN/AEI/10.13039/501100011033/ and the European Regional Development Fund, ‘A way to make Europe’ ERDF (project PID2021-125282OB-I00); Departament de Recerca i Universitats/Generalitat de Catalunya (2021 SGR 01494), European Union under THRIVE Grant Agreement Nr. 101136622 and Fundación Científca de la Asociación Contra el Cáncer (ASPIRE project, RETOS245779LLOV).

## Peer review information

Claudia Feng was the primary editor of this article and managed its editorial process and peer review in collaboration with the rest of the editorial team. The peer-review history is available in Additional File 5 and in the online version of this article.

## Authors’ contributions

Study conception and design: E.P-P, D.G, M.E; performed experiments and data collection: D.G, E.P., E.M., S.C; computational analyses: S.C, E.P-P; writing, review, and editing: S.C, M.E, E.M., F.X.R., D.G, J.A., E.P-P. All authors read and approved the fnal manuscript.

## Data availability

All data generated in this study are available via Zenodo and are organized into three separate repositories. (i) Visium v1, Visium v2/CytAssist, and Visium HD datasets [54]; (ii) Xenium multi-tissue datasets without cell segmentation together with CosMx datasets [55]; and (iii) Xenium multi-tissue (XeniumMT) and Xenium Prime (Xenium5K) datasets with cell segmentation [56].

The code used to reproduce the results and fgures presented in this study is publicly available on GitHub [57] (https:// github.com/scervilla/SpatialBenchmarking) and on Zenodo [58] (https://doi.org/10.5281/zenodo.1801661), and is distributed under the MIT license.

## Declarations

## Ethics approval and consent to participate

All tumor samples were obtained under the ethics committee approval 2022/78-APA-HUGC.

## Consent for publication

Not applicable.

## Competing interests

The authors declare no competing interests.

Received: 13 October 2025 Accepted: 6 January 2026

Published online: 12 January 2026

## References

1. Ding L, et al. Perspective on oncogenic processes at the end of the beginning of cancer genomics. Cell. 2018;173:305-320.e10.

2. Sabarinathan R, et al. The whole-genome panorama of cancer drivers. Preprint at. 2017. https://doi.org/10.1101/ 190330.

3. Li Y, et al. Pan-cancer proteogenomics connects oncogenic drivers to functional states. Cell. 2023;186:3921-3944. e25.

4. Bailey MH, et al. Comprehensive characterization of cancer driver genes and mutations. Cell. 2018;173:371-385.e18.

5. Muiños F, Martínez-Jiménez F, Pich O, Gonzalez-Perez A, Lopez-Bigas N. In silico saturation mutagenesis of cancer genes. Nature. 2021;596:428–32.

6. Thorsson V, et al. The immune landscape of cancer. Immunity. 2018;48:812-830.e14.

7. Rooney MS, Shukla SA, Wu CJ, Getz G, Hacohen N. Molecular and genetic properties of tumors associated with local immune cytolytic activity. Cell. 2015;160:48–61.

Reardon B, et al. Integrating molecular profles into clinical frameworks through the molecular oncology almanac to prospectively guide precision oncology. Nat Cancer. 2021;2:1102–12.

9. Rubio-Perez C, et al. In silico prescription of anticancer drugs to cohorts of 28 tumor types reveals targeting opportunities. Cancer Cell. 2015;27:382–96.

10. Rodriguez-Meira A, et al. Unravelling intratumoral heterogeneity through high-sensitivity single-cell mutational analysis and parallel RNA sequencing. Mol Cell. 2019;73:1292-1305.e8.

11. Terekhanova NV, et al. Epigenetic regulation during cancer transitions across 11 tumour types. Nature. 2023;623:432–41.

12. Barkley D, et al. Cancer cell states recur across tumor types and form specifc interactions with the tumor microenvironment. Nat Genet. 2022;54:1192–201.

13. Moses L, Pachter L. Museum of spatial transcriptomics. Nat Methods. 2022;19:534–46.

14. Zhao T, et al. Spatial genomics enables multi-modal study of clonal heterogeneity in tissues. Nature. 2022;601:85–91.

15. Zhang D, et al. Spatial epigenome–transcriptome co-profling of mammalian tissues. Nature. 2023;616:113–22.

16. Ståhl PL, et al. Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. Science. 2016;353:78–82.

17. Wang F, et al. RNAscope. J Mol Diagn. 2012;14:22–9.

18. Chen KH, Boettiger AN, Moftt JR, Wang S, Zhuang X. Spatially resolved, highly multiplexed RNA profling in single cells. Science. 2015;348:aaa6090.

19. Lubeck E, Coskun AF, Zhiyentayev T, Ahmad M, Cai L. Single-cell in situ RNA profling by sequential hybridization. Nat Methods. 2014;11:360–1.

20. He S, et al. High-plex imaging of RNA and proteins at subcellular resolution in fxed tissue by spatial molecular imaging. Nat Biotechnol. 2022;40:1794–806.

21. Merritt CR, et al. Multiplex digital spatial profling of proteins and RNA in fxed tissue. Nat Biotechnol. 2020;38:586–99.

22. Rodriques SG, et al. Slide-seq: a scalable technology for measuring genome-wide expression at high spatial resolution. Science. 2019;363:1463–7.

23. Janesick A, et al. High resolution mapping of the tumor microenvironment using integrated single-cell, spatial and in situ analysis. Nat Commun. 2023;14:8353.

24. Keren L, et al. MIBI-TOF: a multiplexed imaging platform relates cellular phenotypes and tissue structure. Sci Adv. 2019;5:eaax5851.

25. Lin J, Fallahi-Sichani M, Chen J, Sorger PK. Cyclic immunofuorescence (CycIF), a highly multiplexed method for single-cell imaging. CP Chem Biol. 2016;8:251–64.

26. Rivest F, et al. Fully automated sequential immunofuorescence (seqIF) for hyperplex spatial proteomics. Sci Rep. 2023;13:16994.

27. Porta-Pardo E, Grases D. A Practical Guide to Spatial Transcriptomics: Lessons from over 1000 Samples. 2025. Preprint at https://doi.org/10.20944/preprints202504.1450.v1.

28. Petukhov V, et al. Cell segmentation in imaging-based spatial transcriptomics. Nat Biotechnol. 2022;40:345–54.

29. Masiero M, et al. A core human primary tumor angiogenesis signature identifes the endothelial orphan receptor ELTD1 as a key regulator of angiogenesis. Cancer Cell. 2013;24:229–41.

30. Edfeldt K, Hellman P, Westin G, Stalberg P. A plausible role for actin gamma smooth muscle 2 (ACTG2) in small intestinal neuroendocrine tumorigenesis. BMC Endocr Disord. 2016;16:19.

31. Aran D, et al. Reference-based analysis of lung single-cell sequencing reveals a transitional profbrotic macrophage. Nat Immunol. 2019;20:163–72.

32. Lin J-R, et al. Multiplexed 3d atlas of state transitions and immune interaction in colorectal cancer. Cell. 2023;186:363-381.e19.

33. Klupp F, et al. Serum MMP7, MMP10 and MMP12 level as negative prognostic markers in colon cancer patients. BMC Cancer. 2016;16:494.

34. Almendro V, et al. The role of MMP7 and its cross-talk with the FAS/FASL system during the acquisition of chemoresistance to oxaliplatin. PLoS One. 2009;4:e4728.

35. Eng C-HL, et al. Transcriptome-scale super-resolved imaging in tissues by RNA seqFISH . Nature. 2019;568:235–9.

36. Polański K, et al. Bin2cell reconstructs cells from high resolution Visium HD data. Bioinformatics. 2024;40:btae546.

37. Williams CG, Lee HJ, Asatsuma T, Vento-Tormo R, Haque A. An introduction to spatial transcriptomics for biomedical research. Genome Med. 2022;14:68.

38. Marx V. Method of the year: spatially resolved transcriptomics. Nat Methods. 2021;18:9–14.

39. Park YM, Lin D-C. Moving closer towards a comprehensive view of tumor biology and microarchitecture using spatial transcriptomics. Nat Commun. 2023;14:7017.

40. Mo C-K, et al. Tumour evolution and microenvironment interactions in 2D and 3D space. Nature. 2024;634:1178–86.

41. Cook DP, et al. A Comparative Analysis of Imaging-Based Spatial Transcriptomics Platforms. Preprint at. 2023. https:// doi.org/10.1101/2023.12.13.571385.

42. Wang H, et al. Systematic benchmarking of imaging spatial transcriptomics platforms in FFPE tissues. Preprint at. 2023. https://doi.org/10.1101/2023.12.07.570603.

43. Hartman A, Satija R. Comparative analysis of multiplexed in situ gene expression profling technologies. Preprint at. 2024. https://doi.org/10.1101/2024.01.11.575135.

44. You Y, et al. Systematic comparison of sequencing-based spatial transcriptomic methods. Nat Methods. 2024;21:1743–54.

45. Hao Y, et al. Dictionary learning for integrative, multimodal and scalable single-cell analysis. Nat Biotechnol. 2024;42:293–304.

46. Manukyan A, et al. VoltRon: A Spatial Omics Analysis Platform for Multi-Resolution and Multi-omics Integration using Image Registration. Preprint at. 2023. https://doi.org/10.1101/2023.12.15.571667.

47. Gombin J, Vaidyanathan R, Agafonkin V. concaveman: A Very Fast 2D Concave Hull Algorithm. 1.1.0 https://doi.org/ 10.32614/CRAN.package.concaveman (2017).

48. Larsson L, Franzén L, Ståhl PL, Lundeberg J. Semla: a versatile toolkit for spatially resolved transcriptomics analysis and visualization. Bioinformatics. 2023;39:btad626.

49. Moses L, et al. Voyager: exploratory single-cell genomics data analysis with geospatial statistics. Preprint at. 2023. https://doi.org/10.1101/2023.07.20.549945.

50. Baddeley A, Rubak E, Turner R. Spatial Point Patterns: Methodology and Applications with R. Chapman and Hall/CRC; 2015. https://doi.org/10.1201/b19708.

51. Schubert M, et al. Perturbation-response genes reveal signaling footprints in cancer gene expression. Nat Commun. 2018;9:20.

52. Badia-i-Mompel P, et al. decoupleR: ensemble of computational methods to infer biological activities from omics data. Bioinform Adv. 2022;2:vbac016.

53. Liang W-W, et al. Integrative multi-omic cancer profling reveals DNA methylation patterns associated with therapeutic vulnerability and cell-of-origin. Cancer Cell. 2023;41:1567-1585.e7.

54. Cervilla S, Grases D, Perez E, Real FX, Musulen E, Aprea J, Esteller M, Porta-Pardo E. A technical comparison of spatial transcriptomics platforms across six cancer types. Zenodo. 2025. https://doi.org/10.5281/zenodo.17999961.

55. Cervilla S, Grases D, Perez E, Real FX, Musulen E, Aprea J, Esteller M, Porta-Pardo E. A technical comparison of spatial transcriptomics platforms across six cancer types. Zenodo. 2025. https://doi.org/10.5281/zenodo.17986017.

56. Cervilla S, Grases D, Perez E, Real FX, Musulen E, Aprea J, Esteller M, Porta-Pardo E. A technical comparison of spatial transcriptomics platforms across six cancer types. Zenodo. 2025. https://doi.org/10.5281/zenodo.18000256.

57. Cervilla S, Grases D, Perez E, Real FX, Musulen E, Aprea J, Esteller M, Porta-Pardo E. A technical comparison of spatial transcriptomics platforms across six cancer types. GitHub. 2025. https://github.com/scervilla/SpatialBenchmarking.

58. Cervilla S, Grases D, Perez E, Real FX, Musulen E, Aprea J, Esteller M, Porta-Pardo E. A technical comparison of spatial transcriptomics platforms across six cancer types. Zenodo. 2025. https://doi.org/10.5281/zenodo.18016691.

## Publisher’s Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afliations.

## Authors

Sergi Cervilla<sup>1†</sup>, Daniela Grases<sup>1†</sup>, Elena Perez<sup>1</sup>, Francisco X. Real<sup>2,3,4</sup>, Eva Musulen<sup>1,5</sup>, Julieta Aprea<sup>6</sup>, Manel Esteller<sup>1,3,7,8</sup> and Eduard Porta-Pardo<sup>1,9\*</sup>

<sup>†</sup>Sergi Cervilla and Daniela Grases contributed equally to this work.

<sup>1</sup> Josep Carreras Leukaemia Research Institute (IJC), Badalona, Spain

<sup>2</sup> Centro Nacional de Investigaciones Oncológicas (CNIO), Madrid, Spain <sup>3</sup> Centro de Investigación Biomedica en Red (CIBERONC), Madrid, Spain

<sup>4</sup> Departament de Medicina I Ciències de La Vida, Universitat Pompeu Fabra, Barcelona, Spain <sup>5</sup> Department of Pathology, Hospital Universitari General de Catalunya, Grupo-QuirónSalud, Sant Cugat del Vallès, Spain <sup>6</sup> DRESDEN-Concept Genome Center, Technology Platform of the TUD Dresden University of Technology, Dresden,

<sup>7</sup> Institució Catalana de Recerca I Estudis Avançats (ICREA), Barcelona, Spain

<sup>8</sup> Physiological Sciences Department, School of Medicine and Health Sciences, University of Barcelona (UB), Barcelona, Spain

<sup>9</sup> Barcelona Supercomputing Center (BSC), Barcelona, Spain

\*Correspondence: eporta@carrerasresearch.org

## Figure Descriptions

**Figure 1.** Experimental design. a Overview of the benchmarked performed on spatial transcriptomics platforms. b Summary table of the spatial datasets, detailing platform characteristics and generated data. c Barplot of the number of detected genes in each sequenced-based platform colored by shared and unique genes. d Gene expression of ACTA2 of the colorectal sample using Visium v1 (left) and Visium v2 (right). Dashed lines indicate the same tissue region

**Figure 2.** Main diferences between in situ platforms. a Barplot of the number of detected cells in each image-based platform (whole scanned area and shared area). b The left plot shows the number of transcripts detected per cell in a small area of the bladder sample in CosMx. The middle plot shows the cells in the bladder sample (CosMx) colored according to their distance to the FOV edge: in red the control (between 2000 and 2100 px), in orange the outer area (36px from the edge), and the remaining cells in yellow. The right boxplot shows the number transcripts detected in each cell and in each CosMx sample. c Boxplot comparing the distribution of the cell area $( \mu \mathsf { m } . ^ { 2 } )$ in CosMx and Xenium. d DAPI images with cell segmentation overlay of CosMx (left) and Xenium (right) in a zoomed area of the breast sample. e Boxplot of the number of unique genes detected per cell (y-axis, in log scale) in CosMx and Xenium considering the whole gene panel (All) and the 125 genes shared between the two gene panels (Int). f Boxplot of the number of transcripts detected per cell (y-axis, in log scale) in CosMx and Xenium considering the whole gene panel (All) and the 125 genes shared between the two gene panels (Int). g Scatterplots showing the correlation between density gene expression in Visium v2 (x-axis) and CosMx (y-axis, left) or Xenium (y-axis, right). The horizontal dashed lines show the average detection rate of the negative probes in Xenium and CosMx. The diagonal dashed line shows the expected perfect correlation $( \mathfrak { i . e . } \times = \mathfrak { y } )$ . The blue line shows the correlation between CosMx/ Xenium and Visium v2. h Zoomed-in region showing H&E staining (left) alongside spatial maps of ADGRL4 expression detected by the CosMx (center) and Xenium (right) platforms. i Correlation between the DV200 of each sample (x-axis) and the mean detected genes per cell (y-axis) in both platforms. Cohen’s d efect sizes are indicated by plus symbols: $( 0 . 2 < d \leq 0 . 5 ,$ small), $+ + ( 0 . 5 < d \leq 0 . 8 ,$ , medium), and $+ + + ( d { > } 0 . 8 ,$ , large)

**Figure 3.** Identifying diferent cell types with each in situ platform. a Diferences by cell type between Xenium and CosMx in cell size (top row), number of genes per cell (middle row), and number of transcripts per cell (bottom row), across all samples. Only the 125 genes shared between the two gene panels were considered. b Barplot showing the cell type relative abundance found in the whole Xenium sample (left), the common area of the Xenium cells (middle) and the common area of the CosMx cells in each tumor sample. c Similar to b) but showing the sub-type relative abundance within B cells (left) and T cells (right) for lung and lymphoma samples. d Representative regions showing H&E staining (left) alongside cell-type maps from CosMx (center) and Xenium (right). The left set depicts the colorectal tumor–stroma interface, and the right set highlights blood vessels in a bladder sample. Barplots (bottom) show the cell composition within each compartment of the corresponding zoomed-in areas. e Boxplot showing the efect of sampling smaller regions to compute relative abundance in the xenium lung sample, of Cancer (epithelial), Stroma cells (fbroblast and endothelial) and Immune (remaining cell types). In the Random category, the subset was determined by randomly sampling across the Xenium (shared area), while in the Spatial category, the sampling was based on FOV as a sampling unit. In each group number of sampled FOV, we used 100 stochastic iterations to compute the abundance of each cell group. Dashed lines represent the relative abundance of the Xenium (shared area) sample. f MMP7 gene expression in the CosMx (left) and Visium v2 (right) samples

**Figure 4.** Diferences in gene panel size in Xenium. a Boxplot of the number of unique genes detected per cell (y-axis, in log scale) in XeniumMT and Xenium5K considering the whole gene panel (All) and the 225 genes shared between the two gene panels (Int). b Boxplot of the number of transcripts detected per cell (y-axis, in log scale) in XeniumMT and Xenium5K considering the whole gene panel (All) and the 225 genes shared between the two gene panels (Int). c Scatterplots showing the correlation between gene expression in Xenium5K (y-axis) and Visium v2 normalized by the area (x-axis, left) or XeniumMT (x-axis, right). The horizontal/vertical dashed lines show the average detection rate of the negative probes in Xenium. The diagonal dashed line shows the expected perfect correlation (i.e. x y). The blue line shows the correlation between Visium v2/XeniumMT and Xenium5K. d MYC gene expression in the XeniumMT (left) and Xenium5K (right) colorectal sample. e Barplot showing the cell type relative abundance found in the XeniumMT (left) and Xenium5K (right) samples. f Cell type annotations overlaid on Xenium multi-modal staining in a zoomed-in region of the ovarian sample, shown for XeniumMT (left) and Xenium5K (right). Barplots (bottom) show the cell composition within cancer compartment of the corresponding zoomed-in areas. g Boxplots representing median measurements evaluating cell area (top), genes detected (middle), and transcripts detected (bottom), considering the whole gene panel (left panels) and restricted to the 81 shared genes (right panels). Individual samples are represented as dots and colored by the corresponding tumor type

**Figure 5.** Comparing VisiumHD against Visium v2 and Xenium. a Left: Small region (32 32 µm) of the ovarian Xenium sample displaying cell boundaries (white lines), bin size overlies (pink squares) and transcript locations for KRT7 (yellow dot). Top Right: Averaged density plot of binning simulation in Xenium samples, showing the number of diferent cells with transcripts in each bin. Bottom Right: Averaged density plot of binning simulation in Xenium samples, showing the number of bins overlapping with transcripts from the same cell. b Transcript count per bin in a small region of the ovarian sample in VisiumHD. c Scatter plots illustrating the correlation between density gene expression in VisiumHD (x-axis) and Visium v2 (y-axis, top) or Xenium (y-axis, bottom. The dashed diagonal line indicates expected perfect correlation (x y). d Spatial distribution of cell types (left), EPCAM (center) and CXCL10 (right) gene expression within Xenium (top) and VisiumHD (bottom) ovarian samples. e Barplot showing the cell type relative abundance found in the whole VisiumHD sample (left) and the cropped Xenium area (right) in each tumor sample. f Barplot displaying the diference in absolute cell type abundance between the full VisiumHD sample and the cropped Xenium area for each tumor sample. Bars are color-coded by cell type, matching the palette used in f ). Positive values indicate higher abundance in VisiumHD, while negative values indicate higher abundance in Xenium. g Cell type characterization of Cancer (epithelial), Stroma cells (fbroblast and endothelial), T cells, Macrophages and Immune (remaining cell types) in the ovarian sample (left). Localization of two macrophage subpopulations with a pair of overexpressed markers on the top (right). h Score of Hypoxia pathway in the ovarian sample using Visium v2 (top) and VisiumHD (bottom)

**Figure 6.** Spatial multi-omics reveals diferences in RNA and protein levels across space. a Boxplots showing the correlation between normalized gene and protein expression in each sample represented by a color. Genes are sorted based on which cell type is expected to be overexpressed and their median correlation. b Boxplot showing the correlation between RNA and protein for the 35 genes included in the Visium v2 protein panel, according to the bulk measurements in 7 CPTAC cancer types. c Normalized gene (left) and protein expression (right) of ITGAX (top) and KRT5 (bottom) in the Lung sample. Correlations between gene and protein expression are shown alongside gene symbols. d Normalized gene (left) and protein expression (right) of CD68 in the Lung sample. Correlation between gene and protein expression are shown alongside gene symbol. e Normalized gene expression of CD68 after transferring Xenium transcripts to Visium spots. f Same as b) but correlations are computed using gene expression from Visium v2 and the pseudo counts from Xenium. In both cases, only genes found in the protein and Xenium panel are considered