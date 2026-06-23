REVIEW

Open Access

# Spatial multi-omics: novel tools to study the complexity of cardiovascular diseases

![](images/8abda6b58efb7ba38680bebc4c7f07bfcc088a66dcbb22f51e4b9d35813bd5f9.jpg)

Paul Kiessling<sup>1</sup> and Christoph Kuppe<sup>1</sup> \*

## Abstract

Spatial multi-omic studies have emerged as a promising approach to comprehensively analyze cells in tissues, enabling the joint analysis of multiple data modalities like transcriptome, epigenome, proteome, and metabolome in parallel or even the same tissue section. This review focuses on the recent advancements in spatial multi-omics technologies, including novel data modalities and computational approaches. We discuss the advancements in lowresolution and high-resolution spatial multi-omics methods which can resolve up to 10,000 of individual molecules at subcellular level. By applying and integrating these techniques, researchers have recently gained valuable insights into the molecular circuits and mechanisms which govern cell biology along the cardiovascular disease spectrum. We provide an overview of current data analysis approaches, with a focus on data integration of multi-omic datasets, highlighting strengths and weaknesses of various computational pipelines. These tools play a crucial role in analyzing and interpreting spatial multi-omics datasets, facilitating the discovery of new fndings, and enhancing translational cardiovascular research. Despite nontrivial challenges, such as the need for standardization of experimental setups, data analysis, and improved computational tools, the application of spatial multi-omics holds tremendous potential in revolutionizing our understanding of human disease processes and the identifcation of novel biomarkers and therapeutic targets. Exciting opportunities lie ahead for the spatial multi-omics feld and will likely contribute to the advancement of personalized medicine for cardiovascular diseases.

Keywords Spatial multi-omics, Spatial transcriptomics, In situ sequencing, Multiplex in situ FISH, MALDI, Spatial proteomics, Data integration, Spatial neighborhood analysis

## Background

Organs are built from billions of cells and multiple cell types. Organ function is dependent on tight control of intrinsic and extrinsic stimuli within the tissue microenvironment to control cell fate decisions in development, health, and disease. Te earliest morphometric events of an embryo occur at the 8–16 cell stage when compaction occurs [1]. Further, cell divisions, activation, and inhibition of regulators like transcription factors lead to unique tissue patterns and organ shapes, which support multiple unique organ functions. Cell-cell communication is crucial for maintaining the spatial organization of tissues and organs, ensuring the continuity of their functions across various distances [2]. In the human heart, the proper spatial organization of cells guarantees efcient energy conversion leading to synchronous cardiac muscle contractions, the rhythm of life.

For many years, anatomists and physiologists have focused their studies on cell and tissue morphology using approaches like histological staining techniques and electron microscopy. Tey identifed various spatial features of the heart at macroscopic and at the subcellular level (e.g., distinct cell-cell contacts of cardiomyocytes, intercalated discs (ICD) [3]). While cardiomyocytes make up most of the heart by volume, they are outnumbered by a diverse mix of fbroblasts, immune cells, endothelial cells, and mural cells, which form the organ scafold and vascular compartment [4]. Tis organization is disturbed in disease, often in a similar fashion across cardiovascular diseases, e.g., in the context of fbrosis or tissue infammation. Examples include the zonation of the myocardium into distinct spatial domains of injury after myocardial infarction (ischemic zone, border zone, and remote zone [4]), vascular calcifcation initiated at diferent locations in blood vessels [5, 6] and focal segmental glomerulosclerosis (FSGS), and lesions with distinct spatial organization in fbrotic glomeruli of the kidney caused by hypertension [7–9]. Tus, methods are needed to shed unbiased insights into the spatial molecular changes of these localized processes.

Nature methods selected spatial transcriptomics (ST) as “method of the year 2020” [10], and since then, several studies applied these technologies in cardiovascular research. Single-cell and spatial multi-omics studies of the heart and kidney exemplify the recent development and insights by applying these technologies. While single-cell and single-nuclei studies of the human heart in health [11, 12] and disease [4, 13–15] have led to valuable insights, spatial information was lacking. Spatial biology enables researchers to observe and decode these complex patterns and communications of cells within their native tissue environments. Intrinsically, cells are regulated by a complex interplay of molecular regulators on several levels, which can be measured with high-throughput “omics” technologies. Multiple molecular levels can be measured currently with massive throughputs, including the genome, transcriptome, proteome, and metabolome. In the last few years, several assays have been developed to decode these layers on the single-cell level (e.g., singlecell proteomics, single-cell RNA, or ATAC sequencing). As these technologies became more broadly available to researchers worldwide, they have led to tremendous biological insights into cardiovascular diseases, including atherosclerosis [16, 17], vascular calcifcation [18], kidney [19–21], and heart disease [11–13, 15, 22, 23] and transformed our understanding of cellular heterogeneity, diferentiation trajectories, and plasticity. Te impact of these technologies is highlighted by the initiation of consortium-based research projects like the Human Cell Atlas (HCA) [24, 25] or the Human BioMolecular Atlas Program (HuBMAP) [26], which primarily focus on creating a comprehensive cellular map of the human body detailing the location, function, and characteristics of each cell type in the diferent tissues. However, it has become clear that for a comprehensive understanding of intrinsic and extrinsic factors which control cell fate decisions in tissues, it is crucial to consider and include spatial molecular information. Similarly to the speed of development of single-cell assays (from 1 cell [27] to 100,000 s with ultrahigh throughput [28, 29] within 10 years), the development of spatial technologies has recently gained pace, and various technological breakthroughs have led to the development of innovative approaches to study spatial biology (additionally reviewed here [30–34]). Tis increase in scope has made it possible to assemble spatial multi-omics experiments, opening up new perspectives on cell biology. One of the most pivotal questions is which spatial technologies, or combination thereof, to utilize for a given biological question. Here we give a comprehensive overview of the technological principles of various spatial technologies, their strengths and weaknesses, current and emerging computational strategies to analyze spatial data, challenges, and potential future directions of spatial multi-omics in cardiovascular disease.

## Spatial multi‑omics technologies at cellular resolution

## NGS‑sequencing‑based spatial multi‑omics

Te current rise of ST accelerated after the development of a high-throughput transcriptome-wide assay using arrayed oligo-nucleotide barcoded spots by Ståhl et  al. in 2016 [35, 36], which formed the basis for the commercialized product called Visium by 10× Genomics. While this assay provides high throughput, the resolution is currently limited to 55-μm diameter spots arranged in a hexagonal array with a 100-μm distance between spot centers (see Table 1). Alternative array-based spatial transcriptomic methods have been developed with higher resolution and diferent spot barcoding principles either using beads, like Slide-Seq/Slide-SeqV2 [37, 38] or barcoded wells with 2-μm resolution-like HDST [39]. Tese technologies aim to close the gaps inherent to dissociated single-cell data providing information on the colocalization of cell types and cell states, spatial covariance of gene expression changes, and defning cellular tissue niches and how they change in disease (Fig. 1). Furthermore, this information is used to analyze cell-cell communication and utilized for machine-learning approaches to link the data to the patient’s clinical outcome. In the cardiovascular research space, single-cell and spatial multi-omics studies of the heart and kidney exemplify the recent development and insights by applying these technologies. While single-cell and single-nuclei studies of the human heart in health [11, 12] and disease [4, 13–15] have led to valuable insights, spatial information was lacking.

In our spatial multi-omic study of human myocardial infarction [4], we utilized multi-omic techniques such as single-cell gene expression sequencing, chromatin accessibility sequencing (scATAC-seq), and ST to build a molecular map of cardiac remodeling, including multiple clinical time points. Our study enabled a detailed examination of unique disease markers by analyzing tissue samples collected at various intervals after MI and from distinct areas of the heart. Using this approach, we could resolve several cardiac cell types in their spatial context and the tissue microenvironment. Integrating multimodal data facilitated the identifcation of specifc alterations in the transcriptome and epigenome in response to ischemic damage, repair, and myocardial remodeling and the establishment of gene regulatory networks.

Table 1 Overview of spatial multi-omics methods. Experimental methods, corresponding instruments, analyte principles, modalities, feature scale, and resolution are shown for each category. The cost row ofers an estimation on the price per sample and does not include initial investment into the device

<table><tr><td rowspan="2"></td><td>NGS based multi-omics</td><td colspan="5">Imaging based multi-omics</td><td colspan="2">MS- based multi-omics</td></tr><tr><td>Spatial non-deterministic barcoding</td><td>Spatial deterministic barcoding</td><td>ISS</td><td>Multiplex ISH - diffraction limited</td><td>Multiplex ISH - non diffraction limited</td><td>Cyclic IF</td><td>lon-labelled antibodies</td><td>microdissection</td></tr><tr><td>Method</td><td>Visium35,36, Slide-SeqV237,38, STEREO-Seq101, HDST39</td><td>DBiT-Seq53</td><td>HybISS92, FIS-SEQ,</td><td>MERFISH93, seqFISH94, osmFISH, EEL-FISH,</td><td>FLASH-PAINT103, DNA-PAINT, SUM-PAINT104</td><td>CODEX72, COMET, 4i70, IBEX71, Immuno-SABER73</td><td>IMC68, MIBI69</td><td>Deep Visual Proteomics77,78 (DVP)</td></tr><tr><td>Instrument</td><td>Sequencer (short/long read)</td><td>Sequencer (short/long read)</td><td>microscope (epifluorescence confocal)</td><td>microscope (epifluorescence confocal)</td><td>microscope (confocal, TIRF, STED)</td><td>microscope</td><td>Mass-Spec</td><td>Laser-micro-dissection microscope + Mass-Spec</td></tr><tr><td>Analyte principles</td><td>Barcoded primer</td><td>Barcoded primer</td><td>Padlock probes</td><td>Probe panel</td><td>Oligo-labeled nanobodies</td><td>Oligo or IF labeled antibodies</td><td>lon-labeled antibodies</td><td>Tissues markers and AI software for dissection</td></tr><tr><td>Modalities</td><td>DNA, RNA, protein</td><td>DNA, RNA, protein</td><td>DNA, RNA</td><td>DNA, RNA, protein</td><td>RNA, protein</td><td>protein</td><td>protein</td><td>protein</td></tr><tr><td>Feature scale</td><td>10.000s Protein: 100a</td><td>RNA:10.000s Protein: 100s</td><td>1000s</td><td>cells (1000s) tissues (100s)</td><td>12 (theoretically 10.000s)</td><td>1-200</td><td>1-50</td><td>unlimited</td></tr><tr><td>Resolution</td><td>1-55 μm, Stereo-seq: 200 nm</td><td>10 μm</td><td>Diffraction limited</td><td>Diffraction limited</td><td>Sub-5 nm</td><td>Diffraction limited</td><td>100 nm-1μm</td><td>5-10 μm (cellular level)</td></tr><tr><td>Costs</td><td>+++</td><td>++</td><td>++++</td><td>++++</td><td>+</td><td>+-++</td><td>++</td><td>++</td></tr></table>

ST approaches combined with other technologies have been used by other studies to shed light on tissue remodeling following MI in mice. Using a neonatal mouse model and ST, a recent study [40] focusing on cardiac regeneration found that the transcription factor Nrf1 regulates the oxidative stress response, which protects the neonatal heart from ischemic injury. Another study focused on the border zone (BZ) in mouse models found the gene CSRP3 to be critical for the regulation of remodeling processes after myocardial infarction and identifed distinct mechano-sensing genes in the BZ of the infarct [41]. Boileau et al. introduced scNaST (singlecell nanopore spatial transcriptomics), a method targeted at the identifcation of RNA-isoform switches using longread sequencing of the myocardium following infarction in diferent regions of the myocardium [42].

In a recent seminal study by Kanemaru et  al., the researchers performed spatial multi-omic profling of the human heart, including in a total eight regions [22]. Te authors used single-cell transcriptome and multiome (RNA+ATAC) profling to defne cellular niches and to investigate cell-cell communication, primarily focusing on the cardiac conduction system. In addition, they developed a druggable target prediction tool (drug2cell) revealing the cardiac cellular targets of GLP-1 analogues. Tis spatial atlas will be of tremendous use for future studies involving diseased human heart tissues.

Other studies have utilized spatial transcriptomic approaches to decode the infammatory processes in tissue space, e.g., viral myocarditis [43]. Using ST, the authors decoded the host response in neonatal mice. Tey observed the molecular basis of how endothelial cells mount a potent innate immune response in the heart, which is associated with localized stress response signatures. Spatial resolution was crucial for these fndings, as myocarditis shows distinct zonation and border zones with unique infammatory signatures that could potentially be missed in single-cell RNA sequencing studies of dissociated tissue. Alternative spatial transcriptomic approaches allow the user to assay selected regions of the tissue based on distinct photomasks. UV light is then used to release photoactivated linker molecules, which can be sequenced using NGS. Tis platform is called digital spatial profling (DSP) or GeoMX (from NanoString). Researchers have recently used it to shed light on the human immune landscape in cardiac sarcoidosis, a lethal infammation of the human heart [44]. Te spatial measurement enabled them to fnd a novel marker of multinucleated giant cells and identify patterns in the location of several immune cells throughout the granuloma.

Based on transcriptomic data alone, the diferentiation of naïve or mature immune cells is generally challenging, but additional protein markers such as CD45RO/ CD45RA commonly used in FACS can signifcantly aid the identifcation of the correct immune cell state. Recently, spatial transcriptomics technologies have been developed to include protein information from a panel of selected antibodies similar to CITE-Seq [45] in single-cell RNA sequencing. In SPOTS [46], oligo-labeled antibodies are applied on the tissue section with a unique ID and UMI sequence, allowing for a quantitative assessment of the protein expression in addition to a measurement of the whole transcriptome. SM-Omics [47] is another ST approach which combines the capture of released RNA on an array with an oligo-label antibody staining strategy. Library generation is automated with the help of a pipetting robot, which scales up library generation to nearly 96 libraries in a little over 2 days, albeit at a resolution of only 100 μm.

Similar to spatial protein expression analysis, Llorens-Bobadilla et al. have recently adapted their ST approach to measure open chromatin information using spatial ATAC-Seq [48].

Another interesting development has been the combination of spatial transcriptomics and expansion microscopy called Ex-ST [49]. By embedding the tissue in swellable gel and expanding it up to 2.5-fold, the authors were able to reach a near single-cell resolution and also increased the capture efciency of lowly expressed genes. A key innovation of this protocol is the use of two different poly-T oligos with diferent melting temperatures. In scRNA-seq, technologies, like SMART-Seq total [50] or VASA-Seq [51], extended measurements from just mRNA to all other RNA species like miRNAs, lnc-RNAs, and non-host RNA, like viral transcripts, by enzymatic polyadenylation. Analogous, a spatial total RNA sequencing (STRS) method has been recently developed [52].

While the technologies described above rely on the difusion of reverse-transcribed transcripts onto immobilized oligo-dT-nucleotides barcodes, in DBiT-Seq [53], microfuidic channels in PDMS chips are used to actively fow the barcodes on the tissue (see Table  1). Sequential barcoding in the reverse transcription (barcode A) and ligation step (barcode B) is used to individually and deterministically barcode tissue pixels using

DNA-oligos. Tis method has been recently adapted to measure spatial ATAC-seq profles [54] and co-profling of RNA and ATAC or other epigenetic features like histone modifcations in the same tissue section [55] as well as proteomics [56]  (Fig.  1). In 2022, this technology was highlighted with other spatial multi-omics methods as one of “seven technologies to watch in 2022” [57]. Te resolution of DBiT-Seq is determined by the diameter of the PDMS-chip channels, which range from 10 to 50 μm, thus reaching near single-cell resolution. Te versatility of this approach, especially in regard to multi-omics, is remarkable and could in theory be extended to other modalities like 3D genome organization [58], APEX-seq [59], or higher throughput as demonstrated recently [60].

Kishi et  al. presented another innovative barcoding strategy combining in  situ barcoding and ex situ NGS sequencing called Light-seq [61]. A unique combination of technologies allowed the authors to specifcally target a very rare cell type, dopaminergic amacrine cells (DAC cells) of the mouse retina, which otherwise would be very difcult to capture. Another distinguishing feature, compared to all other spatial methods, is that it leaves the original sample intact, opening several opportunities for further downstream analysis using other omics. Furthermore, this technology might be extended to analyze the proteome or epigenome.

An exciting development for single-cell [62–64] and spatial transcriptomics [65] has been the recent adaptation to formalin-fxed parafn-embedded (FFPE) tissues. Several challenges had to be overcome, including the development of FPPE-specifc nuclei isolation protocols [64] and strategies to handle RNA cross-linking and RNA degradation typical to FPPE tissue stored at room temperature. Te 10× Visium workfow, originally designed for cryo tissue, was adapted to the FFPE tissue workfow by the inclusion of three pairs of probes for each target mRNA. Te assay measures mRNA transcriptome wide and can be refned by the spike-in of custom probes. Since FFPE samples are the gold standard for tissue preservation for pathologists (mostly due to their excellent ability to preserve tissue morphology) and FFPE tissue is widely accessible, the development of these approaches is particularly promising. Clinical data of these samples are usually available, thus enabling the study of larger retrospective cohorts with detailed metadata. A recent study combined the probe panel Visium FFPE workfow with low-quality freshfrozen samples (FF), which led to great improvements in data quality and even made it possible to spatially profle cartilage and bone tissues in mice [66], signifying light at the end of the tunnel for the processing of these challenging samples.

anon-deterministic spatial barcoding (Visium, slide-Seq)

![](images/803487f18534711a0928a16d5d5b9e4909816c7ac3b894fe46d360789d9459fa.jpg)  
Fig. 1 NGS-based spatial multi-omics. a Schematic of nondeterministic barcoding for spatial transcriptomics. Either barcoded spots (e.g., Visium) or beads (Slide-Seq) are used in an array to capture released reverse-transcribed RNA on a glass slide. Spatial multi-omic datasets can be generated using data integration with diferent single-cell methods. b Schematic of deterministic barcoding which utilizes PDMS chips with microchannels to barcode the tissue in two rounds. Several omic layers can be derived from the same tissue section including transcriptomics, proteomics, and epigenomics

## Non‑NGS‑based spatial multi‑omics

While transcriptome information is widely used to model protein expression dynamics, the genome-wide correlation between mRNA and protein is estimated to be only around 40% [60, 61]. Furthermore, the transcriptome alone cannot provide information about processes induced by posttranslational protein modifcations, which can have important efects on cell biology. Compared to the transcripts, resolving the proteome at single-cell resolution or in tissues is much more challenging. Cells typically contain 30,000× more protein molecules than mRNA molecules [67], and proteins are very heterogeneous in size and structure and, unlike nucleic acids, cannot be amplifed. Tis has limited the multiplexing and throughput of spatial proteome measurements. Nevertheless, enormous progress has been made in generating multiplex proteomics datasets from tissues.

Antibody-based multiplexed imaging technologies have been available before NGS-based spatial assays relying on mass cytometry for IMC-Cytof [68] or MIBI-TOF [69] but have only recently increased in throughput (larger feld of view > 1 cm<sup>2</sup>) and complexity (> 10–50 markers) (see Table  1). Te development of fuorescence-based technologies such as 4i [70] and IBEX [71] and DNA-oligo labels in the case of CODEX [72] and Immuno-SABER [73] has made spatial proteomics more approachable, as researchers do not need access to MS instruments.

A major challenge in antibody-based proteomics is validating the antibody specifcity and ensuring that it is not infuenced after the conjugation step with fuorophores or DNA. Another approach to enable unbiased singlecell or spatial proteomics is based on highly sensitive LC-MS-based proteomics (reviewed here [67, 74–76]), which has been adapted to spatial proteomics as deep visual proteomics (DVP) [77, 78]. DVP combines laser-capture microdissection of distinct cell types from tissue and performs MS proteomics of the collected tissues extending bulk proteomics of the human heart [79] with cell type and spatially resolved information in the near future.

Recent developments of transgenic mice have enabled metabolic labeling of proteins using Cre-recombinaseinduced expression of a mutant methionyl-tRNA synthetase [80, 81] from a given cell population. Combined with unbiased MS-proteomic approaches, this might be well suited to resolve the cell secretome or for the discovery of novel biomarkers, which otherwise might be missed in proteomics of isolated cells.

Spatial metabolomics has reached 5–10 μm resolution and has been recently applied to study cell-type-specifc dynamics of metabolism in kidney repair [82]. Every year, 13 million people sufer from AKI and increased cardiovascular risk burden [83]. Te kidney tubules can regenerate following AKI; in most patients, the injury resolves via adaptive regeneration [84]. How this process is molecularly wired is unknown, yet the importance of metabolic factors contributing to this process is widely recognized. MALDI-MSI-based metabolomics combined with 13C-labeled nutrients allowed the authors to study the dynamics of metabolic changes at subcellular resolution. Tey subsequently used multiplexed immunofuorescence microscopy to identify cell types which seemed unnecessary, as cell types could be diferentiated just based on the lipid profles.

One area where spatial metabolomics might ofer great value is research targeting the protective efect of SGLT2 inhibition in renal proximal tubular cells. Inhibition of SGLT2 in the proximal tubule demonstrated a remarkably benefcial efect on survival in patients sufering from cardiovascular disease, including heart and kidney disease [85]. Secondary molecular changes are however not well understood. Spatial metabolomics can elucidate this potent pathway and potentially lead to novel targets.

Additional developments and progress in spatial metabolomics have been recently reviewed here [86, 87]. Te correct metabolite annotation of MS data remains a particular challenge. Resources like www.metaspace2020.eu ofer a powerful platform for annotating and sharing metabolic MS datasets.

A combination of spatial multiplexed IF imaging and spatial metabolomics has recently been established to investigate myeloid cell heterogeneity in atherosclerotic plaques [88], shedding light on plaque myeloid phenotypes.

One recent approach demonstrated the measurement of metabolites or other arbitrary targets based on NGS structure-switching aptamers [89], which are constructed to release barcodes upon contact with the target molecules in single-cell RNA sequencing assays. Follow-up studies on this interesting strategy must be performed to determine how scalable these approaches are. While certainly not on the immediate horizon, single-molecule protein sequencing might be combined with MS and antibody-based multiplex imaging approaches to shed light on the proteome at unprecedented resolution. A recent review [90] is included here for completion.

## Spatial multi‑omics technologies at single‑molecular resolution

Several approaches have been developed which allow in  situ sequencing (ISS) or imaging-based fuorescence in situ hybridization (FISH) of RNA, DNA, or proteins. In ISS, mRNA is labeled with specifc nucleotide sequences called padlock probes [91], which are then sequenced with rolling circle amplifcation to increase the specifcity of fuorophore binding (see Table 1). HybISS [92], or the commercialized version by 10× Genomics (Xenium), enables the detection of 100–1000 targets at subcellular resolution, including the detection of mutations. In general, these approaches have a very high sensitivity allowing them to detect lowly expressed genes.

FISH-based technologies like MERFISH [93] or SeqFISH+ [94] encoding probes are designed based on a binary barcoding scheme, which allows for error correction during the readout of the fuorescent barcode (see Table  1). Tese methods have been recently developed to measure open chromatin [94] and simultaneously 3D genome, proteome, and transcriptome [95]. Te measurement of high-resolution transcriptomics using MERFISH in > 50–100 μm section has recently been proposed [96].

In general, both ISS- and FISH-based methods require the selection of a limited number of targets to form a probe panel a priori. Computational approaches like spapros [97] and others [98, 99] provide a workfow to identify these genes based on reference single-cell RNA sequencing data.

Several other technologies are available: CosMx [100] (NanoString), and Molecular Cartography (Resolve Biosciences). However, an independent benchmark that compares sensitivity, specifcity, and other performance metrics has not been carried out.

Unbiased ST methods at subcellular resolution have been developed recently, such as Stereo-Seq [101] and SeqScope [101]. While these approaches allow subcellular resolution transcriptomics (e.g., 220-nm diameter size for Stereo-Seq), assignment of signals to specifc cells is potentially more challenging, as cell boundary stains are not available and difusion dynamics might afect the measurement. It remains to be seen how accurately these spatial assays perform compared to other in situ approaches.

Tese technologies enable additional insights into subcellular spatial localization of molecules, e.g., between the nucleus or cytoplasm, to gain insights on transcriptional dynamics of cell states. Tey have not been extensively applied in cardiovascular research since they are quite novel and just starting to be accessible to more researchers worldwide.

While these technologies have already reached an astonishing resolution, recent developments of DNA-PAINT approaches like FLASH-PAINT [102] or SUM-PAINT [103] and the development of Ångströmresolution fuorescence microscopy (RESI) [104] might lead to even further increases in multiplexed detection of biomolecules at nanometer ranges. Particularly, the combination of these DNA-imager-based approaches with DNA-based protein-binding aptamers [105] (SOMAmers) might open the possibility to profle 1000 s of proteins in  situ below the difraction limit at single protein resolution in the future.

## Computational approaches for spatial multi‑omics

New experimental designs also require innovative approaches for data analysis. Adding the spatial dimension to multi-omic data sets poses signifcant challenges but empowers existing analysis tools and opens entirely new ways of understanding tissue biology. In this section, we will discuss data analysis strategies and key challenges of working with multi-omic spatial datasets. For a more in-depth technical perspective, readers are directed to additional recent reviews on this topic [106–108] and the community resources at www.sc-best-practices.org and https://lmweber.org/BestPracticesST.

Computational workfows are dependent on the technology that produced the data, but there is signifcant overlap in the processing of the diferent modalities. Te objective of these workfows is similar: to link the signal recorded by the instrument, be that a fuorescent intensity or barcode, the sequence of reverse-transcribed RNA, or the m/z value of an ion back to a spatial location in the tissue. Technologies with cellular resolution are then able to assign signals to individual cells in a process known as cell segmentation.

## Cell segmentation

Cellular segmentation of tissues is often improved by combining the primary readout with additional stains, such as DAPI staining of nuclei and or the cell borders with anti-cadherin antibodies or similar compounds. In imaging-based approaches like FISH, ISS, or multiplexed immunofuorescence, these measurements can be acquired simultaneously with the main measurement, but even measurements that do not require a microscope like NGS-based Stereo-seq [109] or MALDI measurements [110] are often co-registered with separately acquired microscopic images. To assign the measured signal to biological entities like cells or nuclei, the positions of the entities need to be extracted from the image in a process known as instance segmentation of cells. Tis step is critical, as misassignment of the signal can contaminate the measurement with cells which present a mix of signals originating from diferent cell types or can entirely hide difcult-to-segment entitles from downstream processing. Deep-learning-based segmentation algorithms like Cellpose 2.0 [111], Mesmer [112], and Segment Anything [113] have shown superior performance to more traditional algorithms like watershed [114] but are highly sensitive to cell diameter and shape. Tis is problematic, as tissues like the heart are composed of cells with vastly diferent morphology. Human cardiomyocytes are cylindrically shaped with an approximate length and diameter of around 100 μm and 20 μm, respectively [115], which is much larger than interstitial or immune cells for example. Furthermore, they can be multinucleated [116] and vary in shape based on the sectioning of the tissue and disease progression [117]. Tis poses signifcant difculties for deep-learning algorithms, which were not trained on a large corpus of heart data, necessitating fne-tuning. A promising direction for cell segmentation is the probabilistic assignment of signals with tools like Baysor [118], ClusterMap [119], or Sparcle [120], which employ statistical models which judge the likelihood of transcripts originating from the same cell. In technologies where cellular resolution is impossible, the signal is instead assigned to regions of interest or binned into tiles representing the resolution limit (Fig. 2).

Te result of this processing is an entity-by-signalby-position matrix compatible with a variety of downstream analysis workfows. Ecosystems that process spatial multi-omics data in a standardized way are just beginning to emerge. Of note are SpatialData [121], SpatialExperiment [122], GiottoData [123], and SeuratObject [124], which ofer data containers that can store the diverse data generated by spatial-omics experiments. Tis infrastructure is critical to unify the heterogeneous data from diferent technology-specifc vendor formats and the various images, tables, and polygons that a single experiment can generate and makes the development of analysis algorithms that “plug-and-play” possible.

## Integration of multi‑omic datasets

To unlock the synergy of multi-omic measurements, integrating the datasets with each other is necessary. Tis is a nontrivial task as the data generated by diferent modalities exist in entirely diferent feature spaces. When talking about integration, it is important to diferentiate several scenarios. Argelaguet et al. [125] proposed three categories of integration tasks: Horizontal integration is used when the same modality is measured across diferent samples. An example could be the measurement of the spatial transcriptome across multiple myocardial infarction samples. Vertical integration describes the integration of measurements in the same cells, such as co-profling of the epigenome and transcriptome in DBiT-seq. Te most challenging case is diagonal integration. Here, neither the cells nor features are shared across datasets, and integration instead relies on a strong biological signal that can be captured with diferent modalities independently from each other. When applying MALDI and spatial transcriptomics to alternating sections of the heart, neither the features nor, depending on the thickness of the slice, the cells are shared between experiments.

A special case, often referred to as imputation, is the enrichment of targeted spatial transcriptomics with whole transcriptome sc-RNAseq reference data. Tese measurements, which are often restricted to 500 or fewer species of RNA, can thus be virtually extended to cover the whole transcriptome. Tis task is comparatively easier, as the concordance between spatial RNA measurements and single-cell RNA seems to mostly hold across genes [126, 127]. Notable software packages in this domain are Tangram [128], gimVI [129], and ENVI [130].

One approach for horizontal integration is the generation of a common coordinate framework, a shared coordinate system across measurements [131–133]. Based on common landmarks, and distinct morphological features of tissues, slices are morphed and aligned to overlap in space. With enough measurements, this system can then be used to construct entire 3D organs [134, 135].

In vertical and diagonal integration tasks, the collected data needs to be projected into a common latent space to minimize various distance metrics. In general, algorithms developed for single-cell experiments like GLUE [136], Seurat WNN [137], or totalVI [138] could be applied to spatial experiments; however, this would dissociate cells from their spatial context and ignores the cellular neighborhood, which is highly informative for integration tasks. A new class of tools developed specifcally for the integration of spatial experiments has recently come into focus. Moscot [139] formulates integration as an optimal transport problem, encoding the Euclidean distance among spatial locations, MaxFuse [140] applies graphsmoothing to the input data and iteratively matches modalities after co-embedding, while SpatialGlue [141] employs a graph neural network (GNN) and uses an attention aggregation layer to integrate constructed spatial proximity and feature graphs (Fig. 2).

While these tools show promise, it is important to note that as of the time of this article’s publication, several tools have not undergone peer review. An independent benchmark of spatial-omics integration algorithms is urgently needed and would help scientists in their choice of integration strategy and inform their experimental designs.

A well-integrated dataset is very powerful for a lot of common downstream analysis tasks. Cell typing is much improved when information about both transcriptome and proteome is available, as cells like NK-cells, which play a major role in infammatory heart disease [142, 143], are notoriously hard to classify based solely on their low transcript counts. Te combination of epigenome and transcriptome reveals clear links between gene expression and transcription factor binding and enables the construction of gene regulatory networks, e.g. the recently develop SCENIC+ tool [144], across spatial domains like the border zone of myocardial infarction [4] or pacemaker cells [22].

In heart disease, infammatory and fbrotic responses are not randomly located in the tissue but possess specifc motifs or principles. In MI, ANKRD1 and NPPB show a gradient across the border zone of the infarct [4], and the epicardium has been shown to contain distinct niches of plasma B cells [22].

A variety of tools have been tailored to facilitate similar discoveries. Analogous to the conventional processing of single-cell experiments, it is possible to create lower dimensional representations of spatial data to identify trends across cells. MEFISTO [145], SpatialPCA [146], and GraphST [147] allow for the identifcation of clusters of cells not only based on the measured signal but also based on the tissue niche and the surrounding types of cells, leading to a more fne-grained understanding of tissue structure principles. Another branch of tools like SPARK [148], SpaGCN [149], or SpatialDE [149, 150] investigates patterns in feature expression across the region of interest, often with additional functionality like pseudo-time analysis in the case of SpaceFlow [149–151] or the detection of patterns across consecutive slices in STAGATE [152] (Fig. 2).

With the introduction of spatial omics with subcellular resolution, this search for patterns is not limited to a macroscopic view of tissue composition but can also be extended to structures inside cells. Te cellular location of proteins is often disturbed in disease like in familial atrial fbrillation, for example, which is caused by a mutation that impedes HSP70 import [153]. Te role of RNA localization remains poorly understood but has been implicated in developmental processes [154] and diseases like Huntington’s disease [155]. Recently published tools like Bento [156], FishFactor [157], and SPRAWL [158] analyze the position of RNA inside cells and try to identify subcellular compartments and principles of transcripts across the cytoplasm and nucleus (Fig. 2).

Cell morphology is another resource that remains underutilized in the analysis of spatial datasets. Cardiomyocytes and fibroblasts are known to change their cellular phenotype and morphology in response to stress, such as hypertrophy, elongation, or thickening [117]. These features offer valuable insight into cell state that could be integrated with existing omics measurements. Cajal is an algorithm that transfers cell shapes into a latent space that can be integrated with genomic readout [159].

## Cell‑cell interaction in space

Cells in the heart are engaged in intense cross talk with their cellular niche. G-protein-coupled receptors, ion channels, and their paracrine and autocrine signaling are only some examples of critical communication circuits in the development of heart disease [160–162]. Tese processes can be studied on the transcriptional level based on the expression of key receptor and ligand proteins and curated databases that collect matched receptors and ligands. Until recently, programs had to rely on dissociated single-cell data for this task. Tis is however problematic, as most forms of cell-cell communication are short ranged and very much dependent on the spatial tissue organization.

A new generation of algorithms combines receptorligand analysis with the position of molecules to investigate these key processes  (Fig.  2). NCEM [163] and CLARIFY [164] are neural networks which model gene expression as a function of their spatial neighborhood, SpatialDM [165] applies bivariate Moran’s statistics, and COMMOT [166] is based on collective optimal transport. It remains to be seen which approach yields the most biologically relevant information, as no comparative benchmarking has been published so far.

## Design considerations for spatial multi‑omic experiments

Before starting a spatial multi-omic experiment, several key questions have to be addressed by the researcher to inform the choice of technology and the design of the experiment. On the one hand, these are imposed by the research question. Te choice of which modalities to measure and at what resolution cannot be answered by a general guide but must be made on a project-to-project basis. As an example, rare cells, like neuronal cells or pericytes, would best be studied with a high-resolution technique, as detection might not be possible in lower resolution measurements which confate multiple cells into spots. Te analysis of lowly expressed genes like transcription factors is best served by approaches with maximal sensitivity, such as ISS or ISH.

Experiments can in general be divided into exploratory investigations that aim to generate hypotheses and confrmatory experiments that aim to prove a well-designed research question. Generally speaking, methods with a larger feature scale such as NGS-based multi-omics and microdissection MS lend themselves well to an exploratory setting, while more targeted approaches like imaging-based multi-omics and ion-label MS shine in confrming well-defned research questions.

On the other hand, the current technical limitations of the technologies and budgetary considerations must also inform the choice of method. Spatial multi-omics experiments are costly and complex to establish and should only be employed in settings where a clear zonation of the tissue is expected. Almost all technologies require the procurement of additional devices and access to specialized facilities like NGS and mass spectrometry core facilities. Community established technologies such as DBiT-seq and HybISS are generally more afordable than their commercial counterparts, which ofer convenience and a support structure at a surcharge. Comparing the initial investment required, spatial deterministic barcoding ranks at the lower end, as a house vacuum and PDMS chip are easily accessible. Spatial nondeterministic barcoding, ISS, difraction-limited multiplex ISH, and cyclic IF fall in the medium price range, while multiplex ISH beyond the difraction limit and MS-based multi-omics fall into the upper price segment, driven by the high cost of super resolution microscopy and a mass spectrometry + laser-microdissection setup, respectively. Te upkeep costs of the devices and the cost per area of tissue (shown in Table 1) warrant further consideration.

![](images/0224cf99ca71861c5f2d6cc4856393cc09492049e98585f1fcd2817ebcb7f1be.jpg)  
Fig. 2 Overview of key areas of analysis enabled by spatial multi-omics and example software implementations. Gene expression in tissues is not random but forms characteristic spatial patterns. Preserving the spatial context allows for the analysis of cell-cell interaction at diferent length scales. Imaging-based technologies enable the extraction of further features like cell morphology or sub-cellular structures but require well-optimized cell segmentation. A key area of software development is spatial data integration

Te measurement area varies wildly between technologies from a range of mm<sup>2</sup> up to 13.2 cm × 13.2 cm in the case of Stereo-seq. Tis not only limits what kind of samples can be measured but also has a direct efect on analysis. It has been shown, for example, that tumor samples which contain a large number of heterogeneous cell states require a high number of FOV for adequate analysis [167].

Not all technologies are compatible with all samples. While they are more widely available, samples preserved in FFPE can be more challenging to assay as these samples tend to sufer from increased RNA fragmentation and increased modifcations of proteins and metabolites. A further consideration is the species of interest. Spatial multi-omic methods can in principle be applied to any kind tissue, but hybridization-based technologies such as Visium v2 or Xenium rely on the construction of probes, which are only available for human and mouse samples currently.

After a technology has been chosen, it is generally necessary to optimize the processing of samples. Diferent tissues can be more or less challenging and require diferent treatment, owing to factors such as ease of permeabilization, resistance to proteinase, or increased autofuorescence. Tese pilot experiments can then also be used to inform the overall design of a study. In silico tissue generation tools are able to probabilistically create spatial multiomic data based on prior knowledge [167–169]. Tese artifcial datasets can then be used in a power analysis to determine necessary FOV sizes, number of views, and replicates to answer the research question.

## Challenges of spatial multi‑omics Experimental challenges

Many experimental challenges exist for spatial multiomics. As with single-cell RNA sequencing, standardized sample preparation is key for successful experiments and high data quality. Especially for the handling of tissues, standardized protocols need to be followed for tissue sampling, fxation, freezing, and tissue sectioning. Protocols such as FixNCut [170] are based on Lomant’s reagent/DSP or treatments with VivoFix [171] reversible fxate tissues before dissociation, which limits artifacts induced by temperature and enzymatic digestions and preserves RNA integrity. A guide on how diferent tissues should be handled for each spatial multi-omics technology is currently lacking but would greatly increase reproducibility in the feld.

For antibody-based multiplexed imaging methods, the specifcity of a given antibody panel is a potential concern. While established and validated antibody panels are available from commercial vendors (e.g., from Akoya Biosciences for CODEX), they are associated with increased costs. In cases where custom antibodies or antibody combinations are necessary, their validation can be time-consuming, and antibody specifcity can often remain unclear. Community eforts like the recent establishment of organ mapping antibody panels, OMAP [172], are needed to guide antibody selection and ensure high reproducibility.

An open question in the feld of array-based spatial transcriptomics is the efect of difusion artifacts. Especially, high-resolution array-based approaches like Stereo-Seq with 220-nm pixel resolution [109, 173] or Seq-Scope [101] might be afected by difusion artifacts, and it is unclear if this problem might apply for future developments of array-based ST approaches with higher resolution (like Visium-HD). Aided mobilization of the barcoded nucleotides using electrophoresis, like in EEL-FISH [174], might mitigate this problem.

Furthermore, it is unclear how to best select the necessary samples and sample numbers and/or size of the feld of view (FOV) for a cohort or study to accurately capture the targeted biological processes. Several in silico tissue spatial multi-omics generation pipelines have been established [168, 175] to explore this question. However, this might still not lead to the desired result if the tissue does not include the targeted process in the frst place. Another approach could be to use machine learning methods like pathomics [176] on large-scale digital histological data, which highlights areas of interest for a given group of diseases and maximizes the amount of information which can be derived from spatial experiments.

## Computational challenges

Spatial multi-omics data analysis presents various challenges that the feld will need to eventually overcome. Cell segmentation remains challenging for all imagingbased approaches, as discussed above. It is often unclear which algorithm produces the best result, as the generation of ground truth for performance evaluation relies on tedious manual annotation of the target tissue. Furthermore, the performance of segmentation algorithms is highly tissue and disease-state dependent. A pipeline that ranks the performance of several tools compared to prior knowledge of the tissue of interest might help alleviate this key problem.

Data integration is another key area where improvements need to be made. At the moment, the parallel measurement of multiple modalities of the same cells in a “true” multi-omic experiment is very limited, and researchers instead rely on algorithms that diagonally integrate separate measurements or impute missing data. Tis emphasizes the importance of reliable integration. It is necessary to scrutinize integrated datasets for biological plausibility, especially as a recent review of transcriptomics integration methods found that no tool reached a Pearson correlation coefcient of more than 0.5 compared to ground truth [177]. Multi-omic integration is likely even more challenging as the link between datasets is weaker. One possible way forward might be the creation of foundation models for spatial multi-omics, analogues to eforts in natural language processing [178], and single-cell transcriptomics [179–181]. Tese models, trained on a large corpus of spatial and single-cell multiomic datasets, might be able to deconvolute underlying patterns necessary for successful integrations.

Lastly, spatial multi-omics experiments are challenging just based on the amount of data generated. An imaging-based spatial transcriptomics measurement can generate around 5 TB of raw data (e.g., MERFISH, own experience), necessitating a robust data storage strategy to which many academic laboratories might not have access. Research is collaborative, and sharing generated data with publications is a key pillar of reproducible science. In the case of spatial multi-omics, the large data volumes and the diversity of generated data between high-resolution images, sequencing data, and tabular information hinder this. Multiple platforms have been established to facilitate the sharing of data and easy inbrowser viewing of datasets [182–187]. However, these repositories remain underused, with every website only containing a small subset of published data. Ideally, scientifc journals would require sharing of data in a digestible and convenient fashion as ofered by these data stores.

## Future perspectives

In the future, multi-omics technology at spatial single-cell resolution will revolutionize our understanding of cell biology. Anticipated advancements include enhanced throughput, cost reductions, and integration of more modalities per assay with improvements in sensitivity and specifcity. Te construction of 3D tissue maps by predicting molecular features from histopathology may be a powerful approach [188]. Current challenges, such as comprehensive mutation profling at single-cell level and co-detection of epigenomic features, will most likely be overcome soon, as demonstrated in recent publications [189]. Current proteome assays will need to evolve from antibodybased techniques to unbiased, low-input methods, as exemplifed recently in the DVP workfow [77] or based on protein-binding DNA aptamers (SOMAmers, e.g., SOMALogic). Spatial assays that will allow us to decode the cell-cell interactions based on the codetection of ligands and receptors on the protein level will be crucial to enhance the CCC modeling. Enhancing computational accuracy of data extraction from each molecular layer and integrative analyses across modalities will be crucial and will further improve predictive modeling like a weather forecast of biological events in tissues (e.g., acceleration of infammation or fbrotic processes or metastasis in cancer). Additionally, one can predict a rise in the combination of geneediting experiments and spatial multi-omics. Similar to single-cell-based CRISPR screenings, these assays can be implemented in  vivo or in  vitro in organoids or bioprinted constructs and spatial gene or drug perturbations consequences analyzed, thus extending the functional analysis toolbox (Fig. 3).

While several barcoding technologies exist to uncover the hierarchical structure or lineage tree of cellular differentiation on single-cell level, we expect that these technologies will be more employed in tissues like in intMEMOIR [190] to uncover hierarchical tissue maps. Tese might also be applied to human tissue based on somatic mutations or mutational signatures from mitochondria [191] or leveraging clonotype information from, e.g., the TCR of T cells. Furthermore, they may be combined with other digital recording systems for biological events [192, 193], further refning insights for biological time traveling in tissues. While these systems can be genetically introduced in vivo, one can also foresee a combination with in  vitro models in which they can be more easily scaled to larger throughput. For data analysis, we envision that large-scale foundation models, which have been recently employed for the analysis of single-cell RNA sequencing data, will spur advancements in spatial multi-omics data analysis in a diverse range of downstream tasks, including data integration, cell-type annotation spatial gene expression analysis, and perturbation prediction, e.g., from drug and genetic perturbations and gene network inference. Together, these advancements in spatial multi-omics technologies and computational approaches are set to enhance our understanding of biology in health and disease and enhance the identifcation of markers for diagnostic and prognostic evaluation of cardiovascular diseases and novel therapeutic targets for personalized medicine (Fig. 3).

![](images/4a997197c785174e850b532f9c5a94d6f4aaedfbaa84f0383a2de2c536a1be0d.jpg)  
Fig. 3 Future perspectives for spatial multi-omics. We foresee several avenous to be implemented in spatial multi-omic experiments. These include the analysis of gene-edited tissues using CRISPR-Cas or other editing/perturbation approaches. Additionally, gene editing can be used to barcode cells to enable lineage tree reconstruction based on spatial data. Receptor-ligand interactions at high resolution would greatly improve CCC analysis. Pathomics could guide selection of insightful tissue areas which are predictive for a disease outcome. Increased sensitivity and specifcity will also certainly be addressed. Advancements in using machine learning models like foundation models will potentially help to overcome data integration difculties. 3D spatial multi-omics data might be acquired directly or inferred from the registration of measurements in a common coordinate framework

## Abbreviations

ICD Intercalated disc MI Myocardial infarction HCA Human Cell Atlas HuBMAP Human BioMolecular Atlas Program IHD Ischemic heart disease ATAC Assay for transposase-accessible chromatin S Spatial transcriptomics scNaST Single-cell nanopore spatial transcriptomics BZ Border zone PDMS Polydimethylsiloxane MERFISH Multiplex error robust fuorescent in situ hybridization MALDI Matrix-assisted laser desorption/ionization FFPE Formalin-fxed parafn embedded FOV Field of view OMAPs Organ mapping antibody panels CODEX Co-detection by indexing EEL-FISH Enhanced electric fuorescence in situ hybridization FISH Fluorescence in situ hybridization NGS Next-generation sequencing

DBiT Deterministic barcoding in tissues MS Mass spectrometry CCC Cell-cell communication DAPI 4′,6-Diamindino-2-phynylindol ISS In situ sequencing CITE-Seq Cellular indexing of transcriptomes and epitopes by sequencing FFPE Formalin-fxed parafn embedded NK cells Natural killer cells

## Acknowledgements

Servier Medical Art was used to create some parts of the fgures. It falls under Creative Commons Attribution 3.0 Unported License (https://creativeco mmons.org/licenses/by/3.0/).

## Disclosures

C. K. joined the scientifc advisory board of OMAPiX.

## Authors’ contributions

Both authors contributed equally to the manuscript.

## Funding

This work was supported by two grants of the German Research Foundation DFG, CRU-5011-445703531, and Emmy Noether EN-459969915 to C. K. by a grant from the European Research Council (ERC-StG-101040726), a grant from the Else Kroener Fresenius Foundation (EKFS), the Aventis Foundation, and by two BMBF grants Graphs4patients and AgedHeart (both to C. K.).

## Availability of data and materials

Not applicable.

## Declarations

Ethics approval and consent to participate Not applicable.

Consent for publication Not applicable.

## Competing interests

The authors declare that they have no competing interests.

Received: 15 August 2023 Accepted: 2 January 2024 Published online:18 January 2024

## References

1. Firmin J, Ecker N, Danon DR, Lange VB, Turlier H, Patrat C, et al. Mechanics of human embryo compaction. bioRxiv. 2022. Internet, Available from: https://doi.org/10.1101/2022.01.09.475429.

2. Palla G, Fischer DS, Regev A, Theis FJ. Spatial components of molecular tissue biology. Nat Biotechnol. 2022;40:308–18.

3. Forbes MS, Sperelakis N. Intercalated discs of mammalian heart: a review of structure and function. Tissue Cell. 1985;17:605–48.

4. Kuppe C, Ramirez Flores RO, Li Z, Hayat S, Levinson RT, Liao X, et al. Spatial multi-omic map of human myocardial infarction. Nature. 2022;608:766–77.

5. Lanzer P, Hannan FM, Lanzer JD, Janzen J, Raggi P, Furniss D, et al. Medial arterial calcifcation: JACC state-of-the-art review. J Am Coll Cardiol. 2021;78:1145–65.

6. Proudfoot D, Shanahan CM. Biology of calcifcation in vascular cells: intima versus media. Herz. 2001;26:245–51.

7. Kuppe C, Gröne H-J, Ostendorf T, van Kuppevelt TH, Boor P, Floege J, et al. Common histological patterns in glomerular epithelial cells in secondary focal segmental glomerulosclerosis. Kidney Int. 2015;88:990–8.

8. D’Agati VD, Kaskel FJ, Falk RJ. Focal segmental glomerulosclerosis. N Engl J Med. 2011;365:2398–411.

9. Fogo A. Tip lesion variant of FSGS. Am J Kidney Dis. 2001;38:E30.

10. Method of the year. spatially resolved transcriptomics. Nat Methods. 2020;2021(18):1.

11. Litviňuková M, Talavera-López C, Maatz H, Reichart D, Worth CL, Lindberg EL, et al. Cells of the adult human heart. Nature. 2020;588:466–72.

12. Tucker NR, Chafn M, Fleming SJ, Hall AW, Parsons VA, Bedi KC Jr, et al. Transcriptional and cellular diversity of the human heart. Circulation. 2020; Internet, Available from: https://doi.org/10.1161/CIRCULATIO NAHA.119.045401.

13. Chafn M, Papangeli I, Simonson B, Akkad A-D, Hill MC, Arduini A, et al. Single-nucleus profling of human dilated and hypertrophic cardiomyopathy. Nature. 2022;608:174–80.

14. Simonson B, Chafn M, Hill MC, Atwa O, Guedira Y, Bhasin H, et al. Single-nucleus RNA sequencing in ischemic cardiomyopathy reveals common transcriptional profle underlying end-stage heart failure. Cell Rep. 2023;42:112086.

15. Reichart D, Lindberg EL, Maatz H, Miranda AMA, Viveiros A, Shvetsov N, et al. Pathogenic variants damage cell composition and single cell transcription in cardiomyopathies. Science. 2022;377:eabo1984.

16. Fernandez DM, Rahman AH, Fernandez NF, Chudnovskiy A, Amir E-AD, Amadori L, et al. Single-cell immune landscape of human atherosclerotic plaques. Nat Med. 2019;25:1576–88.

17. Wirka RC, Wagh D, Paik DT, Pjanic M, Nguyen T, Miller CL, et al. Atheroprotective roles of smooth muscle cell phenotypic modulation and the TCF21 disease gene as revealed by single-cell analysis. Nat Med. 2019;25:1280–9.

18. Alsaigh T, Evans D, Frankel D, Torkamani A. Decoding the transcriptome of calcifed atherosclerotic plaque at single-cell resolution. Commun Biol. 2022;5:1084.

19. Wilson PC, Wu H, Kirita Y, Uchimura K, Ledru N, Rennke HG, et al. The single-cell transcriptomic landscape of early human diabetic nephropathy. Proc Natl Acad Sci U S A. 2019;116:19619–25.

20. Kuppe C, Ibrahim MM, Kranz J, Zhang X, Ziegler S, Perales-Patón J, et al. Decoding myofbroblast origins in human kidney fbrosis. Nature 2020; Internet, Available from: https://doi.org/10.1038/s41586-020-2941-1.

21. Lake BB, Menon R, Winfree S, Hu Q, Ferreira RM, Kalhor K, et al. An atlas of healthy and injured cell states and niches in the human kidney. Nature. 2023;619:585–94.

22. Kanemaru K, Cranley J, Muraro D, Miranda AMA, Ho SY, Wilbrey-Clark A, et al. Spatially resolved multiomics of human cardiac niches. Nature 2023; Internet, Available from: https://doi.org/10.1038/s41586-023-06311-1.

23. Koenig AL, Shchukina I, Amrute J, Andhey PS, Zaitsev K, Lai L, et al. Single-cell transcriptomics reveals cell-type-specifc diversifcation in human heart failure. Nat Cardiovasc Res. 2022;1:263–80.

24. Lindeboom RGH, Regev A, Teichmann SA. Towards a Human Cell Atlas: taking notes from the past. Trends Genet. 2021;37:625–30.

25. Rozenblatt-Rosen O, Stubbington MJT, Regev A, Teichmann SA. The Human Cell Atlas: from vision to reality. Nature. 2017;550:451–3.

26. Jain S, Pei L, Spraggins JM, Angelo M, Carson JP, Gehlenborg N, et al. Advances and prospects for the Human BioMolecular Atlas Program (HuBMAP). Nat Cell Biol. 2023; Internet, Available from: https://doi.org/ 10.1038/s41556-023-01194-w.

27. Tang F, Barbacioru C, Wang Y, Nordman E, Lee C, Xu N, et al. mRNA-Seq whole-transcriptome analysis of a single cell. Nat Methods. 2009;6:377–82.

28. Datlinger P, Rendeiro AF, Boenke T, Senekowitsch M, Krausgruber T, Barreca D, et al. Ultra-high-throughput single-cell RNA sequencing and perturbation screening with combinatorial fuidic indexing. Nat Methods. 2021;18:635–42.

29. Rosenberg AB, Roco CM, Muscat RA, Kuchina A, Sample P, Yao Z, et al. Single-cell profling of the developing mouse brain and spinal cord with split-pool barcoding. Science. 2018;360:176–82.

30. Moses L, Pachter L. Museum of spatial transcriptomics. Nat Methods. 2022; Internet, Available from: https://doi.org/10.1038/s41592-022-01409-2.

31. Vandereyken K, Sifrim A, Thienpont B, Voet T. Methods and applications for single-cell and spatial multi-omics. Nat Rev Genet. 2023;24:494–515.

32. Walker BL, Cang Z, Ren H, Bourgain-Chang E, Nie Q. Deciphering tissue structure and function using spatial transcriptomics. Commun Biol. 2022;5:220.

33. Crosetto N, Bienko M, van Oudenaarden A. Spatially resolved transcrip tomics and beyond. Nat Rev Genet. 2015;16:57–66.

34. Baysoy A, Bai Z, Satija R, et al. The technological landscape and applications of single-cell multi-omics. Nat Rev Mol Cell Biol. 2023;24:695–713. https://doi.org/10.1038/s41580-023-00615-w.

35. Ståhl PL, Salmén F, Vickovic S, Lundmark A, Navarro JF, Magnusson J, et al. Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. Science. 2016;353:78–82.

36. Salmén F, Ståhl PL, Mollbrink A, Navarro JF, Vickovic S, Frisén J, et al. Barcoded solid-phase RNA capture for spatial transcriptomics profling in mammalian tissue sections. Nat Protoc. 2018;13:2501–34.

37. Rodriques SG, Stickels RR, Goeva A, Martin CA, Murray E, Vanderburg CR, et al. Slide-seq: a scalable technology for measuring genome-wide expression at high spatial resolution. Science. 2019;363:1463–7.

38. Stickels RR, Murray E, Kumar P, Li J, Marshall JL, Di Bella DJ, et al. Highly sensitive spatial transcriptomics at near-cellular resolution with SlideseqV2. Nat Biotechnol. 2021;39:313–9.

39. Vickovic S, Eraslan G, Salmén F, Klughammer J, Stenbeck L, Schapiro D, et al. High-defnition spatial transcriptomics for in situ tissue profling. Nat Methods. 2019;16:987–90.

40. Cui M, Atmanli A, Morales MG, Tan W, Chen K, Xiao X, et al. Nrf1 promotes heart regeneration and repair by regulating proteostasis and redox balance. Nat Commun. 2021;12:5270.

41. Yamada S, Ko T, Hatsuse S, Nomura S, Zhang B, Dai Z, et al. Spatiotemporal transcriptome analysis reveals critical roles for mechano-sensing genes at the border zone in remodeling after myocardial infarction. Nat Cardiovasc Res. 2022;1:1072–83.

42. Boileau E, Li X, Naarmann-de Vries IS, Becker C, Casper R, Altmüller J, et al. Full-length spatial transcriptomics reveals the unexplored isoform diversity of the myocardium post-MI. Front Genet. 2022;13:912572.

43. Mantri M, Hinchman MM, McKellar DW, Wang MFZ, Cross ST, Parker JSL, et al. Spatiotemporal transcriptomics reveals pathogenesis of viral myocarditis. Nat Cardiovasc Res. 2022;1:946–60.

44. Liu J, Ma P, Lai L, Villanueva A, Koenig A, Bean GR, et al. Transcriptional and immune landscape of cardiac sarcoidosis. Circ Res. 2022;131:654–69.

45. Stoeckius M, Hafemeister C, Stephenson W, Houck-Loomis B, Chattopadhyay PK, Swerdlow H, et al. Simultaneous epitope and transcriptome measurement in single cells. Nat Methods. 2017;14:865–8.

46. Ben-Chetrit N, Niu X, Swett AD, Sotelo J, Jiao MS, Stewart CM, et al. Integration of whole transcriptome spatial profling with protein markers. Nat Biotechnol. 2023; Internet, Available from: https://doi.org/10.1038/ s41587-022-01536-3.

47. Vickovic S, Lötstedt B, Klughammer J, Mages S, Segerstolpe Å, Rozenblatt-Rosen O, et al. SM-Omics is an automated platform for high-throughput spatial multi-omics. Nat Commun. 2022;13:795.

48. Llorens-Bobadilla E, Zamboni M, Marklund M, Bhalla N, Chen X, Hartman J, et al. Solid-phase capture and profling of open chromatin by spatial ATAC. Nat Biotechnol. 2023;41:1085–8.

49. Fan Y, Andrusivová Ž, Wu Y, Chai C, Larsson L, He M, et al. Expansion spatial transcriptomics. Nat Methods 2023; Internet, Available from: https://doi.org/10.1038/s41592-023-01911-1.

50. Isakova A, Nef N, Quake SR. Single-cell quantifcation of a broad RNA spectrum reveals unique noncoding patterns associated with cell types and states. Proc Natl Acad Sci U S A. 2021;118:e2113568118.

51. Salmen F, De Jonghe J, Kaminski TS, Alemany A, Parada GE, Verity-Legg J, et al. High-throughput total RNA sequencing in single cells using VASA-seq. Nat Biotechnol. 2022;40:1780–93.

52. McKellar DW, Mantri M, Hinchman MM, Parker JSL, Sethupathy P, Cosgrove BD, et al. Spatial mapping of the total transcriptome by in situ polyadenylation. Nat Biotechnol. 2023;41:513–20.

53. Liu Y, Yang M, Deng Y, Su G, Enninful A, Guo CC, et al. High-spatialresolution multi-omics sequencing via deterministic barcoding in tissue. Cell. 2020;183:1665–81.e18.

54. Deng Y, Bartosovic M, Ma S, Zhang D, Kukanja P, Xiao Y, et al. Spatial profling of chromatin accessibility in mouse and human tissues. Nature. 2022;609:375–83.

55. Zhang D, Deng Y, Kukanja P, Agirre E, Bartosovic M, Dong M, et al. Spatial epigenome-transcriptome co-profling of mammalian tissues. Nature. 2023;616:113–22.

56. Liu Y, DiStasio M, Su G, Asashima H, Enninful A, Qin X, et al. High-plex protein and whole transcriptome co-mapping at cellular resolution with spatial CITE-seq. Nat Biotechnol. 2023; Internet, Available from: https://doi.org/10.1038/s41587-023-01676-0.

57. Eisenstein M. Seven technologies to watch in 2022. Nature. 2022;601:658–61.

58. Arrastia MV, Jachowicz JW, Ollikainen N, Curtis MS, Lai C, Quinodoz SA, et al. Single-cell measurement of higher-order 3D genome organization with scSPRITE. Nat Biotechnol. 2022;40:64–73.

59. Fazal FM, Han S, Parker KR, Kaewsapsak P, Xu J, Boettiger AN, et al. Atlas of subcellular RNA localization revealed by APEX-Seq. Cell. 2019;178:473–90.e26.

60. Wirth J, Huber N, Yin K, Brood S, Chang S, Martinez-Jimenez CP, et al. Spatial transcriptomics using multiplexed deterministic barcoding in tissue. Nat Commun. 2023;14:1523.

61. Kishi JY, Liu N, West ER, Sheng K, Jordanides JJ, Serrata M, et al. Light-Seq: light-directed in situ barcoding of biomolecules in fxed cells and tissues for spatially indexed sequencing. Nat Methods. 2022;19:1393–402.

62. Xu Z, Zhang T, Chen H, Zhu Y, Lv Y, Zhang S, et al. High-throughput single nucleus total RNA sequencing of formalin-fxed parafnembedded tissues by snRandom-seq. Nat Commun. 2023;14:2734.

63. Chung H, Melnikov A, McCabe C, Drokhlyansky E, Van Wittenberghe N, Magee EM, et al. SnFFPE-Seq: towards scalable single nucleus RNA-Seq of formalin-fxed parafn-embedded (FFPE) tissue. bioRxiv. 2022. Internet, Available from: https://doi.org/10.1101/2022.08.25.505257.

64. Vallejo AF, Harvey K, Wang T, Wise K, Butler LM, Polo J, et al. snPATHOseq: unlocking the FFPE archives for single nucleus RNA profling. bioRxiv. 2022. Internet, Available from: https://doi.org/10.1101/2022. 08.23.505054.

65. Liu Y, Enninful A, Deng Y, Fan R. Spatial transcriptome sequencing of FFPE tissues at cellular level. bioRxiv. 2020. p. 2020.10.13.338475. Internet, Available from: http://biorxiv.org/content/early/2020/10/ 19/2020.10.13.338475.abstract.

66. Mirzazadeh R, Andrusivova Z, Larsson L, Newton PT, Galicia LA, Abalo XM, et al. Spatially resolved transcriptomic profling of degraded and challenging fresh frozen samples. Nat Commun. 2023;14:509.

67. MacCoss MJ, Alfaro JA, Faivre DA, Wu CC, Wanunu M, Slavov N. Sampling the proteome by emerging single-molecule and mass spectrometry methods. Nat Methods. 2023;20:339–46.

68. Tracey LJ, An Y, Justice MJ. CyTOF: an emerging technology for single-cell proteomics in the mouse. Curr Protoc. 2021;1:e118.

69. Keren L, Bosse M, Thompson S, Risom T, Vijayaragavan K, McCafrey E, et al. MIBI-TOF: a multiplexed imaging platform relates cellular phenotypes and tissue structure. Sci Adv. 2019;5:eaax5851.

70. Gut G, Herrmann MD, Pelkmans L. Multiplexed protein maps link subcellular organization to cellular states. Science 2018; 361. Internet, Available from: https://doi.org/10.1126/science.aar7042.

71. Radtke AJ, Kandov E, Lowekamp B, Speranza E, Chu CJ, Gola A, et al. IBEX: a versatile multiplex optical imaging approach for deep phenotyping and spatial analysis of cells in complex tissues. Proc Natl Acad Sci U S A. 2020;117:33455–65.

72. Goltsev Y, Samusik N, Kennedy-Darling J, Bhate S, Hale M, Vazquez G, et al. Deep profling of mouse splenic architecture with CODEX multiplexed imaging. Cell. 2018;174:968–81.e15.

73. Saka SK, Wang Y, Kishi JY, Zhu A, Zeng Y, Xie W, et al. Immuno-SABER enables highly multiplexed and amplifed protein imaging in tissues. Nat Biotechnol. 2019;37:1080–90.

74. Paul I, White C, Turcinovic I, Emili A. Imaging the future: the emerging era of single-cell spatial proteomics. FEBS J. 2021;288:6990–7001.

75. Lundberg E, Borner GHH. Spatial proteomics: a powerful discovery tool for cell biology. Nat Rev Mol Cell Biol. 2019;20:285–302.

76. Bennett HM, Stephenson W, Rose CM, Darmanis S. Single-cell proteomics enabled by next-generation sequencing or mass spectrometry. Nat Methods. 2023;20:363–74.

77. Mund A, Coscia F, Kriston A, Hollandi R, Kovács F, Brunner A-D, et al. Deep visual proteomics defnes single-cell identity and heterogeneity. Nat Biotechnol. 2022;40:1231–40.

78. Makhmut A, Qin D, Fritzsche S, Nimo J, König J, Coscia F. A framework for ultra-low input spatial tissue proteomics. Available from: https://doi. org/10.1101/2023.05.13.540426.

79. Doll S, Dreßen M, Geyer PE, Itzhak DN, Braun C, Doppler SA, et al. Region and cell-type resolved quantitative proteomic map of the human heart. Nat Commun. 2017;8:1469.

80. Alvarez-Castelao B, Schanzenbächer CT, Langer JD, Schuman EM. Cell-type-specifc metabolic labeling, detection and identifcation of nascent proteomes in vivo. Nat Protoc. 2019;14:556–75.

81. Alvarez-Castelao B, Schanzenbächer CT, Hanus C, Glock C, Tom Dieck S, Dörrbaum AR, et al. Cell-type-specifc metabolic labeling of nascent proteomes in vivo. Nat Biotechnol. 2017;35:1196–201.

82. Wang G, Heijs B, Kostidis S, Mahfouz A, Rietjens RGJ, Bijkerk R, et al. Analyzing cell-type-specifc dynamics of metabolism in kidney repair. Nat Metab. 2022;4:1109–18.

83. Odutayo A, Wong CX, Farkouh M, Altman DG, Hopewell S, Emdin CA, et al. AKI and long-term risk for cardiovascular events and mortality. J Am Soc Nephrol. 2017;28:377–87.

84. Ferenbach DA, Bonventre JV. Mechanisms of maladaptive repair after AKI leading to accelerated kidney ageing and CKD. Nat Rev Nephrol. 2015;11:264–76.

85. Ingelfnger JR, Rosen CJ. Clinical credence - SGLT2 inhibitors, diabetes, and chronic kidney disease. N Engl J Med, Massachusetts Medical Society. 2019;380:2371–3.

86. Alexandrov T. Spatial metabolomics and imaging mass spectrometry in the age of artifcial intelligence. Annu Rev Biomed Data Sci. 2020;3:61–87.

87. Saunders KDG, Lewis H-M, Beste DJ, Cexus O, Bailey MJ. Spatial single cell metabolomics: current challenges and future developments. Curr Opin Chem Biol. 2023;75:102327.

88. Goossens P, Lu C, Cao J, Gijbels MJ, Karel JMH, Wijnands E, et al. Integrating multiplex immunofuorescent and mass spectrometry imaging to map myeloid heterogeneity in its metabolic and cellular context. Cell Metab. 2022;34:1214–25.e6.

89. Tan JH, Mercado MP, Fraser AG. A novel platform for metabolomics using barcoded structure-switching aptamers. bioRxiv. 2023. Internet, Available from: https://doi.org/10.1101/2023.06.09.544402.

90. Alfaro JA, Bohländer P, Dai M, Filius M, Howard CJ, van Kooten XF, et al. The emerging landscape of single-molecule protein sequencing technologies. Nat Methods. 2021;18:604–17.

91. Nilsson M, Malmgren H, Samiotaki M, Kwiatkowski M, Chowdhary BP, Landegren U. Padlock probes: circularizing oligonucleotides for localized DNA detection. Science. 1994;265:2085–8.

92. Lee H, Marco Salas S, Gyllborg D, Nilsson M. Direct RNA targeted in situ sequencing for transcriptomic profling in tissue. Sci Rep. 2022;12:7976.

93. Chen KH, Boettiger AN, Moftt JR, Wang S, Zhuang X. RNA imaging. Spatially resolved, highly multiplexed RNA profling in single cells. Science. 2015;348:aaa6090.

94. Eng C-HL, Lawson M, Zhu Q, Dries R, Koulena N, Takei Y, et al. Transcriptome-scale super-resolved imaging in tissues by RNA seqFISH. Nature. 2019;568:235–9.

95. Takei Y, Yun J, Zheng S, Ollikainen N, Pierson N, White J, et al. Integrated spatial genomics reveals global architecture of single nuclei. Nature. 2021;590:344–50.

96. Fang R, Halpern AR, Rahman MM, Huang Z, Lei Z, Hell SJ, et al. Three-dimensional single-cell transcriptome imaging of thick tissues. bioRxiv. 2023, p. 2023.07.21.550124. Internet, Cited 2023 Jul 28. Available from: https://doi.org/10.1101/2023.07.21.550124v1.

97. Kuemmerle LB, Luecken MD, Firsova AB, de Andrade e Sousa LB, Straßer L, Heumos L, et al. Probe set selection for targeted spatial transcriptomics. bioRxiv. 2022. p. 2022.08.16.504115. Internet, Cited 2023 Jul 26, Available from: https://doi.org/10.1101/2022.08.16.50411 5v1.abstract.

98. Zhang Y, Petukhov V, Biederstedt E, Que R, Zhang K, Kharchenko PV. Gene panel selection for targeted spatial transcriptomics. bioRxiv. 2023. p. 2023.02.03.527053. Internet, Cited 2023 Jul 26, Available from: https://doi.org/10.1101/2023.02.03.527053v2.abstract.

99. Li X, Korkut A. Recurrent composite markers of cell types and states. bioRxiv. 2023. p. 2023.07.17.549344. Internet, Cited 2023 Jul 26, Available from: https://www.biorxiv.org/content/10.1101/2023.07.17. 549344v1.abstract.

100. He S, Bhatt R, Brown C, Brown EA, Buhr DL, Chantranuvatana K, et al. High-plex imaging of RNA and proteins at subcellular resolution in fxed tissue by spatial molecular imaging. Nat Biotechnol. 2022;40:1794–806.

101. Cho C-S, Xi J, Si Y, Park S-R, Hsu J-E, Kim M, et al. Microscopic examination of spatial transcriptome using Seq-Scope. Cell. 2021;184:3559–72.e22.

102. Schueder F, Rivera-Molina F, Su M, Kidd P, Rothman JE, Toomre D, et al. Unraveling cellular complexity with unlimited multiplexed super-resolution imaging. bioRxiv. 2023. p. 2023.05.17.541061. Internet, Cited 2023 Jul 26, Available from: https://doi.org/10.1101/2023.05.17.541061v1.

103. Unterauer EM, Boushehri SS, Jevdokimenko K, Masullo LA, Ganji M, Sograte-Idrissi S, et al. Spatial proteomics in neurons at single-protein resolution. bioRxiv. 2023. p. 2023.05.17.541210. Internet, Cited 2023 Jul 26, Available from: https://doi.org/10.1101/2023.05.17.541210v1.

104. Reinhardt SCM, Masullo LA, Baudrexel I, Steen PR, Kowalewski R, Eklund AS, et al. Ångström-resolution fuorescence microscopy. Nature. 2023;617:711–6.

105. Kraemer S, Vaught JD, Bock C, Gold L, Katilius E, Keeney TR, et al. From SOMAmer-based biomarker discovery to diagnostic and clinical applications: a SOMAmer-based, streamlined multiplex proteomic assay. PLoS One. 2011;6:e26332.

106. Kleino I, Frolovaitė P, Suomi T, Elo LL. Computational solutions for spatial transcriptomics. Comput Struct Biotechnol J. 2022;20:4870–84.

107. Dries R, Chen J, Del Rossi N, Khan MM, Sistig A, Yuan G-C. Advances in spatial transcriptomic data analysis. Genome Res. 2021;31:1706–18.

108. Wang X, Wu X, Hong N, Jin W. Progress in single-cell multimodal sequencing and multi-omics data integration. Biophys Rev. 2023:1–16.

109. Chen A, Liao S, Cheng M, Ma K, Wu L, Lai Y, et al. Spatiotemporal transcriptomic atlas of mouse organogenesis using DNA nanoballpatterned arrays. Cell. 2022;185:1777–92.e21.

110. Rappez L, Stadler M, Triana S, Gathungu RM, Ovchinnikova K, Phapale P, et al. SpaceM reveals metabolic states of single cells. Nat Methods. 2021;18:799–805.

111. Pachitariu M, Stringer C. Cellpose 2.0: how to train your own model. Nat Methods. 2022;19:1634–41.

112. Greenwald NF, Miller G, Moen E, Kong A, Kagel A, Dougherty T, et al. Whole-cell segmentation of tissue images with human-level performance using large-scale data annotation and deep learning. Nat Biotechnol. 2022;40:555–65.

113. Kirillov A, Mintun E, Ravi N, Mao H, Rolland C, Gustafson L, et al. Segment anything. arXiv [cs.CV]. 2023. Internet, Available from: http://arxiv. org/abs/2304.02643.

114. Beucher S, Lantuejoul C. Use of Watersheds in Contour Detection. International Workshop on Image Processing: Real-Time Edge and Motion Detection/Estimation, Rennes; 1979. https://people.cmm.minesparis. psl.eu/users/beucher/publi/watershed.pdf.

115. Libby P, Bonow RO, Mann DL, Zipes DP. Braunwald’s Heart Disease: A Textbook of Cardiovascular Medicine, 2-Volume Set. Elsevier Health Sciences; 2007.

116. Derks W, Bergmann O. Polyploidy in cardiomyocytes: roadblock to heart regeneration? Circ Res. 2020;126:552–65.

117. Haftbaradaran Esfahani P, ElBeck Z, Sagasser S, Li X, Hossain MB, Talukdar HA, et al. Cell shape determines gene expression: cardiomyocyte morphotypic transcriptomes. Basic Res Cardiol. 2019;115:7.

118. Petukhov V, Xu RJ, Soldatov RA, Cadinu P, Khodosevich K, Moftt JR, et al. Cell segmentation in imaging-based spatial transcriptomics. Nat Biotechnol. 2022;40:345–54.

119. He Y, Tang X, Huang J, Ren J, Zhou H, Chen K, et al. ClusterMap for multi-scale clustering analysis of spatial gene expression. Nat Commun. 2021;12:5909.

120. Prabhakaran S. Sparcle: assigning transcripts to cells in multiplexed images. Bioinform Adv. 2022;2:vbac048.

121. Marconato L, Palla G, Yamauchi KA, Virshup I, Heidari E, Treis T, et al. SpatialData: an open and universal data framework for spatial omics. bioRxiv. 2023. p. 2023.05.05.539647. Internet, Cited 2023 Jul 20, Available from: https://doi.org/10.1101/2023.05.05.539647v1.

122. Righelli D, Weber LM, Crowell HL, Pardo B, Collado-Torres L, Ghazanfar S, et al. SpatialExperiment: infrastructure for spatially-resolved transcriptomics data in R using Bioconductor. Bioinformatics. 2022;38:3128–31.

123. Dries R, Zhu Q, Dong R, Eng C-HL, Li H, Liu K, et al. Giotto: a toolbox for integrative analysis and visualization of spatial expression data. Genome Biol. 2021;22:78.

124. Satija R, Farrell JA, Gennert D, Schier AF, Regev A. Spatial reconstruction of single-cell gene expression data. Nat Biotechnol. 2015;33:495–502.

125. Argelaguet R, Cuomo ASE, Stegle O, Marioni JC. Computational principles and challenges in single-cell data integration. Nat Biotechnol. 2021;39:1202–15.

126. Salas SM, Czarnewski P, Kuemmerle LB, Helgadottir S, Matsson-Langseth C, Tismeyer S, et al. Optimizing xenium in situ data utility by quality assessment and best practice analysis workfows. bioRxiv. 2023. p. 2023.02.13.528102. Internet, Cited 2023 Jul 24, Available from: https:// doi.org/10.1101/2023.02.13.528102v1.full.

127. Liu J, Tran V, Vemuri VNP, Byrne A, Borja M, Kim YJ, et al. Concordance of MERFISH spatial transcriptomics with bulk and single-cell RNA sequencing. Life Sci Alliance 2023;6. Internet, Available from: https:// doi.org/10.26508/lsa.202201701.

128. Biancalani T, Scalia G, Bufoni L, Avasthi R, Lu Z, Sanger A, et al. Deep learning and alignment of spatially resolved single-cell transcriptomes with Tangram. Nat Methods. 2021;18:1352–62.

129. Lopez R, Nazaret A, Langevin M, Samaran J, Regier J, Jordan MI, et al. A joint model of unpaired data from scRNA-seq and spatial transcriptomics for imputing missing gene expression measurements. arXiv [cs.LG]. 2019. Internet, Available from: http://arxiv.org/abs/1905.02269.

130. Haviv D, Gatie M, Hadjantonakis A-K, Nawy T, Pe’er D. The covariance environment defnes cellular niches for spatial inference. bioRxiv. 2023. p. 2023.04.18.537375. Internet, Cited 2023 Jul 24, Available from: https://doi.org/10.1101/2023.04.18.537375v1.full.

131. Andersson A, Andrusivová Ž, Czarnewski P, Li X, Sundström E, Lundeberg J. A landmark-based common coordinate framework for spatial transcriptomics data. bioRxiv. 2021. p. 2021.11.11.468178. Internet, Cited 2023 Jul 24, Available from: https://doi.org/10.1101/2021.11.11.468178v1.full.

132. Liu X, Zeira R, Raphael BJ. PASTE2: partial alignment of multi-slice spatially resolved transcriptomics data. bioRxiv. 2023; Internet, Available from: https://doi.org/10.1101/2023.01.08.523162.

133. Clifton K, Anant M, Aimiuwu OK, Kebschull JM, Miller MI, Tward D, et al. Alignment of spatial transcriptomics data using difeomorphic metric mapping. bioRxiv. 2023; Internet, Available from: https://doi.org/10. 1101/2023.04.11.534630.

134. Zhang M, Pan X, Jung W, Halpern A, Eichhorn SW, Lei Z, et al. A molecularly defned and spatially resolved cell atlas of the whole mouse brain.

bioRxiv. 2023; Internet, Available from: https://doi.org/10.1101/2023.03. 06.531348.

135. Pentimalli TM, Schallenberg S, León-Periñán D, Legnini I, Theurillat I, Thomas G, et al. High-resolution molecular atlas of a lung tumor in 3D. bioRxiv. 2023. p. 2023.05.10.539644. Internet, Cited 2023 Jul 24, Available from: https://doi.org/10.1101/2023.05.10.539644v1.

136. Cao Z-J, Gao G. Multi-omics single-cell data integration and regulatory inference with graph-linked embedding. Nat Biotechnol. 2022;40:1458–66.

137. Hao Y, Hao S, Andersen-Nissen E, Mauck WM 3rd, Zheng S, Butler A, et al. Integrated analysis of multimodal single-cell data. Cell. 2021;184:3573–87.e29.

138. Gayoso A, Steier Z, Lopez R, Regier J, Nazor KL, Streets A, et al. Joint probabilistic modeling of single-cell multi-omic data with totalVI. Nat Methods. 2021;18:272–82.

139. Klein D, Palla G, Lange M, Klein M, Piran Z, Gander M, et al. Mapping cells through time and space with moscot. bioRxiv. 2023. p. 2023.05.11.540374. Internet, Cited 2023 Jul 24, Available from: https:// doi.org/10.1101/2023.05.11.540374v2.full.

140. Chen S, Zhu B, Huang S, Hickey JW, Lin KZ, Snyder M, et al. Integration of spatial and single-cell data across modalities with weak linkage. bioRxiv. 2023. p. 2023.01.12.523851. Internet, Cited 2023 Jul 24, Available from: https://doi.org/10.1101/2023.01.12.523851v2.full.

141. Long Y, Ang KS, Liao S, Sethi R, Heng Y, Zhong C, et al. Integrated analysis of spatial multi-omics with SpatialGlue. bioRxiv. 2023. p. 2023.04.26.538404. Internet, Cited 2023 Jul 24, Available from: https:// doi.org/10.1101/2023.04.26.538404v2.full.

142. Ong S, Rose NR, Cihakova D. Natural killer cells in infammatory heart disease. Clin Immunol. 2017;175:26.

143. Sun K, Li Y-Y, Jin J. A double-edged sword of immuno-microenvironment in cardiac homeostasis and injury repair. Signal Transduct Target Ther. 2021;6:1–16.

144. Bravo González-Blas C, De Winter S, Hulselmans G, Hecker N, Matetovici I, Christiaens V, et al. SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks. Nat Methods. 2023; Internet, Available from: https://doi.org/10.1038/s41592-023-01938-4.

145. Velten B, Braunger JM, Argelaguet R, Arnol D, Wirbel J, Bredikhin D, et al. Identifying temporal and spatial patterns of variation from multimodal data using MEFISTO. Nat Methods. 2022;19:179–86.

146. Shang L, Zhou X. Spatially aware dimension reduction for spatial transcriptomics. Nat Commun. 2022;13:7203.

147. Long Y, Ang KS, Li M, Chong KLK, Sethi R, Zhong C, et al. Spatially informed clustering, integration, and deconvolution of spatial transcriptomics with GraphST. Nat Commun. 2023;14:1155.

148. Sun S, Zhu J, Zhou X. Statistical analysis of spatial expression patterns for spatially resolved transcriptomic studies. Nat Methods. 2020;17:193–200.

149. Hu J, Li X, Coleman K, Schroeder A, Ma N, Irwin DJ, et al. SpaGCN: Integrating gene expression, spatial location and histology to identify spatial domains and spatially variable genes by graph convolutional network. Nat Methods. 2021;18:1342–51.

150. Svensson V, Teichmann SA, Stegle O. SpatialDE: identifcation of spatially variable genes. Nat Methods. 2018;15:343–6.

151. Ren H, Walker BL, Cang Z, Nie Q. Identifying multicellular spatiotemporal organization of cells with SpaceFlow. Nat Commun. 2022;13:4076.

152. Dong K, Zhang S. Deciphering spatial domains from spatially resolved transcriptomics with an adaptive graph attention auto-encoder. Nat Commun. 2022;13:1739.

153. Hung M-C, Link W. Protein localization in disease and therapy. J Cell Sci. 2011;124:3381–92.

154. Lawrence JB, Singer RH. Intracellular localization of messenger RNAs for cytoskeletal proteins. Cell. 1986;45:407–15.

155. Culver BP, DeClercq J, Dolgalev I, Yu MS, Ma B, Heguy A, et al. Huntington’s Disease Protein Huntingtin Associates with its own mRNA. J Huntingtons Dis. 2016;5:39–51.

156. Mah CK, Ahmed N, Lopez N, Lam D, Monell A, Kern C, et al. Bento: a toolkit for subcellular analysis of spatial transcriptomics data. bioRxiv. 2023. p. 2022.06.10.495510. Internet, Cited 2023 Jul 25, Available from: https://doi.org/10.1101/2022.06.10.495510v2.

157. Walter FC, Stegle O, Velten B. FISHFactor: a probabilistic factor model for spatial transcriptomics data with subcellular resolution. Bioinformatics

2023;39. Internet, Available from: https://doi.org/10.1093/bioinforma tics/btad183.

158. Bierman R, Dave JM, Greif DM, Salzman J. Statistical analysis supports pervasive RNA subcellular localization and alternative 3’ UTR regulation. bioRxiv. 2023. p. 2022.10.26.513902. Internet, Cited 2023 Jul 25, Available from: https://doi.org/10.1101/2022.10.26.513902v2.

159. Govek KW, Nicodemus P, Lin Y, Crawford J, Saturnino AB, Cui H, et al. CAJAL enables analysis and integration of single-cell morphological data using metric geometry. Nat Commun. 2023;14:3672.

160. Martins-Marques T, Hausenloy DJ, Sluijter JPG, Leybaert L, Girao H. Intercellular communication in the heart: therapeutic opportunities for cardiac ischemia. Trends Mol Med. 2021;27:248–62.

161. Fountoulaki K, Dagres N, Iliodromitis EK. Cellular communications in the heart. Card Fail Rev. 2015;1:64.

162. Tirziu D, Giordano FJ, Simons M. Cell communications in the heart. Circulation. 2010;122:928–37.

163. Fischer DS, Schaar AC, Theis FJ. Modeling intercellular communication in tissues using spatial graphs of cells. Nat Biotechnol. 2023;41:332–6.

164. Bafna M, Li H, Zhang X. CLARIFY: cell-cell interaction and gene regulatory network refnement from spatially resolved transcriptomics. Bioinformatics. 2023;39:i484–93.

165. Li Z, Wang T, Liu P, Huang Y. SpatialDM: Rapid identifcation of spatially co-expressed ligand-receptor reveals cell-cell communication patterns. bioRxiv. 2023. p. 2022.08.19.504616. Internet, Cited 2023 Jul 25, Available from: https://doi.org/10.1101/2022.08.19.504616v3.

166. Cang Z, Zhao Y, Almet AA, Stabell A, Ramos R, Plikus MV, et al. Screening cell-cell communication in spatial transcriptomics via collective optimal transport. Nat Methods. 2023;20:218–28.

167. Bost P, Schulz D, Engler S, Wasserfall C, Bodenmiller B. Optimizing multiplexed imaging experimental design through tissue spatial segregation estimation. Nat Methods. 2023;20:418–23.

168. Baker EAG, Schapiro D, Dumitrascu B, Vickovic S, Regev A. In silico tissue generation and power analysis for spatial omics. Nat Methods. 2023;20:424–31.

169. Zhu J, Shang L, Zhou X. SRTsim: spatial pattern preserving simulations for spatially resolved transcriptomics. Genome Biol. 2023;24:39.

170. Jiménez-Gracia L, Marchese D, Nieto JC, Caratù G, Melón-Ardanaz E, Gudiño V, et al. FixNCut: single-cell genomics through reversible tissue fxation and dissociation. bioRxiv. 2023. p. 2023.06.16.545221. Internet, Available from: http://biorxiv.org/content/early/2023/06/19/2023.06.16. 545221.abstract.

171. Fortmann SD, Frey BF, Hanumanthu VS, Liu S, Goldsborough A, Kilchrist KV, et al. Fixation before dissociation using a deep eutectic solvent preservesin vivostates and phospho-signaling in single-cell sequencing. bioRxiv. 2023. p. 2023.02.13.528370. Internet, Available from: http:// biorxiv.org/content/early/2023/02/13/2023.02.13.528370.abstract.

172. Quardokus EM, Saunders DC, McDonough E, Hickey JW, Werlein C, Surrette C, et al. Organ mapping antibody panels: a community resource for standardized multiplexed tissue imaging. Nat Methods. 2023; Internet, Available from: https://doi.org/10.1038/s41592-023-01846-7.

173. Wei X, Fu S, Li H, Liu Y, Wang S, Feng W, et al. Single-cell Stereo-seq reveals induced progenitor cells involved in axolotl brain regeneration. Science. 2022;377:eabp9444.

174. Borm LE, Mossi Albiach A, Mannens CCA, Janusauskas J, Özgün C, Fernández-García D, et al. Scalable in situ single-cell profling by electrophoretic capture of mRNA using EEL FISH. Nat Biotechnol. 2023;41:222–31.

175. Song D, Wang Q, Yan G, Liu T, Sun T, Li JJ. scDesign3 generates realistic in silico data for multimodal single-cell and spatial omics. Nat Biotechnol. 2023; Internet, Available from: https://doi.org/10.1038/ s41587-023-01772-1.

176. Gupta R, Kurc T, Sharma A, Almeida JS, Saltz J. The emergence of pathomics. Curr Pathobiol Rep. 2019;7:73–84.

177. Li B, Zhang W, Guo C, Xu H, Li L, Fang M, et al. Benchmarking spatial and single-cell transcriptomics integration methods for transcript distribution prediction and cell type deconvolution. Nat Methods. 2022;19:662–70.

178. Zhou C, Li Q, Li C, Yu J, Liu Y, Wang G, et al. A comprehensive survey on pretrained foundation models: a history from BERT to ChatGPT. arXiv. org. 2023; Internet, Cited 2023 Jul 26, Available from: https://doi.org/10. 48550/ARXIV.2302.09419.

179. Cui H, Wang C, Maan H, Pang K, Luo F, Wang B. scGPT: towards building a foundation model for single-cell multi-omics using generative AI. bioRxiv. 2023. p. 2023.04.30.538439. Internet, Cited 2023 Jul 26, Available from: https://doi.org/10.1101/2023.04.30.538439v2.abstract.

180. Hao M, Gong J, Zeng X, Liu C, Guo Y, Cheng X, et al. Large scale foundation model on single-cell transcriptomics. bioRxiv. 2023. p. 2023.05.29.542705. Internet, Cited 2023 Jul 26, Available from: https:// doi.org/10.1101/2023.05.29.542705v4.abstract.

181. Theodoris CV, Xiao L, Chopra A, Chafn MD, Al Sayed ZR, Hill MC, et al. Transfer learning enables predictions in network biology. Nature. 2023;618:616–24.

182. Chan Zuckerberg CELLxGENE Discover. Cellxgene data portal. Internet, Cited 2023 Jul 26. Available from: https://cellxgene.cziscience.com/.

183. SpatialOmics. Internet, Cited 2023 Jul 26. Available from: https://gene.ai. tencent.com/SpatialOmics/.

184. Website. Internet, Available from: https://www.spatialomics.org/SpatialDB/.

185. WebAtlas pipeline for integrated single cell and spatial transcriptomic data. Human Dev Cell Atlas 2023. Internet, Cited 2023 Jul 26, Available from: https://developmental.cellatlas.io/webatlas.

186. TissUUmaps. TissUUmaps. The TissUUmaps team; Internet, Cited 2023 Jul 26. Available from: https://tissuumaps.github.io/.

187. 李鸿锷杜文斯. Spatial Transcript Omics DataBase - STOMICS DataBase- 空间转录组学数据库. Internet, Cited 2023 Jul 26. Available from:https://db.cngb.org/stomics/.

188. Comiter C, Vaishnav ED, Ciampricotti M, Li B, Yang Y, Rodig SJ, et al. Inference of single cell profles from histology stains with the Single-Cell omics from Histology Analysis Framework (SCHAF). bioRxiv. 2023; Internet, Available from: https://doi.org/10.1101/2023.03.21.533680.

189. Lu T, Ang CE, Zhuang X. Spatially resolved epigenomic profling of single cells in complex tissues. Cell. 2022;185:4448–64.e17.

190. Chow K-HK, Budde MW, Granados AA, Cabrera M, Yoon S, Cho S, et al. Imaging cell lineage with a synthetic digital recording system. Science. 2021;372:eabb3099.

191. Ludwig LS, Lareau CA, Ulirsch JC, Christian E, Muus C, Li LH, et al. Lineage tracing in humans enabled by mitochondrial mutations and single-cell genomics. Cell. 2019;176:1325–39.e22.

192. Bhattarai-Kline S, Lear SK, Fishman CB, Lopez SC, Lockshin ER, Schubert MG, et al. Recording gene expression order in DNA by CRISPR addition of retron barcodes. Nature. 2022;608:217–25.

193. Kaseniit KE, Katz N, Kolber NS, Call CC, Wengier DL, Cody WB, et al. Modular, programmable RNA sensing using ADAR editing in living cells. Nat Biotechnol. 2023;41:482–7.

## Publisher’s Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afliations.