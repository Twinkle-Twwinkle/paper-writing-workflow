Perspective

# From modality-specific to compositional foundation models for cell biology

Mojtaba Bahrami,<sup>1,2</sup> Till Richter,<sup>1,3</sup> Niklas A. Schmacke,<sup>1,4</sup> Aitana Egea Lavandera,<sup>1</sup> and Fabian J. Theis<sup>1,2,3,</sup>\*

<sup>1</sup>Institute of Computational Biology, Helmholtz Center Munich, Munich, Germany

<sup>2</sup>TUM School of Life Sciences Weihenstephan, Technical University of Munich, Munich, Germany

<sup>3</sup>TUM School of Computation, Information and Technology, Technical University of Munich, Munich, Germany

<sup>4</sup>Gene Center, Department of Biochemistry, Ludwig-Maximilians-Universita¨ t Mu¨ nchen, Munich, Germany

\*Correspondence: fabian.theis@helmholtz-munich.de

https://doi.org/10.1016/j.cels.2026.101534

## SUMMARY

Deriving principles governing cell biology from single-cell measurements across modalities, called multimodal modeling, can advance our understanding of cellular states in health and disease. Realizing the ful potential of multimodal models requires learning generalizable representations across data types, diseases, and biological contexts. This perspective examines the potential of compositional AI as a modular design approach for constructing multimodal foundation models that unify biological modalities—such as chromatin accessibility, protein abundance, spatial transcriptomics, microscopy imaging, and textual annotations— into cohesive representations of cellular behavior. We present key deep learning modeling approaches, along with transformer-based attention strategies to implement them, while addressing challenges posed by limited data availability and structural differences between modality representations. We also discuss how to connect and align partially overlapping multimodal measurements to build a comprehensive representation space. By synthesizing these technical advancements, we chart a path toward agentic virtual cell models, offering insights into opportunities, limitations, and future directions for leveraging multimodal AI to decode the complexity of cellular systems.

## INTRODUCTION

Advances in pre-training natural language models<sup>1–3</sup> have demonstrated remarkable success in leveraging vast amounts of unlabeled data, allowing these models to learn intricate patterns and enabling zero-shot predictions at inference. With the advent of high-throughput cellular measurements, similar methodologies have been explored to pre-train models in single-cell omics, opening new avenues for biological discovery. While single-cell transcriptomics has been a primary driver of this endeavor thanks to substantial efforts in collecting, organizing, and maintaining a wealth of publicly available datasets.<sup>12–17</sup> Gaining a comprehensive understanding of cellular states and dynamics through the development of large, diversely pretrained, and adaptable multimodal single-cell foundation models will require comparable efforts to build and maintain integrated repositories of single-cell multi-omics measurements. Some steps in this direction have already been taken.<sup>12,18,19</sup>

Self-supervised learning (SSL) has emerged as a promising paradigm for training models on vast amounts of data while demonstrating strong generalization capabilities to new tasks during inference.<sup>1,3,20,21</sup> In contrast to supervised learning methods,<sup>22</sup> which rely on externally annotated datasets, SSL leverages data-inherent structure and patterns to generate pseudo-labels, enabling models to learn meaningful representations without human supervision. In high-dimensional settings, SSL is particularly well suited for identifying key signaling sources and targets from millions of features by learning compact, informative representations that emphasize consistent and salient patterns. By reducing noise and redundancy while preserving underlying structure, SSL enables downstream analyses to isolate biologically or mechanistically relevant signals at scale. Furthermore, leveraging the knowledge acquired during the self-supervised training phase enables few-shot and zero-shot predictions at inference, allowing such models to generalize to previously unseen conditions and cellular states with minimum additional fine-tuning.<sup>23</sup> This paradigm serves as a general framework applicable to the training of various deep learning architectures. However, the most successful implementations are built on the transformer architecture,<sup>24</sup> which has demonstrated exceptional performance in capturing complex semantics from large-scale data.<sup>25,26</sup> Transformers excel at modeling long-range dependencies, making them particularly well suited for joint modeling of multiple data modalities.

Integrative and interpretable single-cell analysis is fundamentally driven by biological and functional objectives. Cross-modality integration aims to reconstruct coherent cellular states by jointly modeling complementary molecular layers—such as transcription, chromatin accessibility, protein abundance, and spatial context—that together govern gene regulation, cell identity, and cellular responses to perturbations.<sup>27,28</sup> Functionally, interpretable integration seeks to uncover causal and mechanistic relationships across modalities, enabling the identification of regulatory programs, signaling pathways, and cell-cell communication processes that are not observable from any single modality alone.<sup>29,30</sup> Interpretability is critical not only for hypothesis generation and validation but also for translating learned representations into actionable biological insights, including disease mechanism discovery, target identification, and predictive modeling of cellular perturbations. Consequently, integration in this context is not merely a data-fusion exercise but a principled approach toward building models whose representations align with known biological hierarchies and functional organization.

Numerous efforts have been made to develop deep learning methods capable of learning representations from multiple single-cell modalities. These approaches typically rely on classical supervised or unsupervised learning techniques applied to a limited number of datasets.<sup>31,32</sup> While these methods have demonstrated success in modeling complex biological relationships within specific datasets, they are not designed to generalize knowledge across diverse samples and datasets in the manner of foundation models. Instead, they require training exclusively on the same set of samples that are intended for subsequent analyses, limiting their capacity for broader applicability and cross-sample knowledge transfer. This restriction poses challenges when attempting to leverage information from large-scale, heterogeneous datasets, as each new dataset necessitates independent model training rather than benefiting from a pre-trained, adaptable representation. This is partly caused by the model architecture and training objectives of such models, which mostly depend on an information bottleneck through a neural network (as in variational autoencoders). These information bottleneck designs implicitly prevent model scaling and learning high-dimensional representations.<sup>25</sup>

Going beyond transcriptomic profiles alone, recent studies have begun to take initial steps toward constructing large pretrained single-cell models that integrate multiple modalities. One approach has focused on learning unified representations of single-cell RNA sequencing (scRNA-seq) and chromatin accessibility profiles.<sup>33,34</sup> Other efforts<sup>35,36</sup> have explored the use of large transformer-based models to predict protein abundance from transcriptomic readouts, demonstrating generalizability across unseen datasets. Additionally, there has been growing interest in incorporating spatial information to enhance pre-trained cellular representations. For instance, recent works<sup>6,37,38</sup> have leveraged spatial transcriptomic data to develop context-aware models capable of capturing cell-cell interactions within tissue environments. These studies highlight the effectiveness of transformer attention mechanisms in modeling spatial dependencies inherent in modern spatial transcriptomics assays.

Inspired by the success of large language models (LLMs) in other biomedical applications,<sup>39,40</sup> a new line of research has emerged, aiming to adapt LLMs for single-cell analysis. These approaches<sup>41–48</sup> treat biological measurements as sequences of words and tokens, similar to natural language processing tasks. Encoding biological readouts in a unified manner facilitates seamless integration of diverse data modalities, though it may come at the cost of losing fine-grained biological detail. Nevertheless, this notion holds promise for unifying heterogeneous single-cell datasets and may thereby advance the field toward more comprehensive multimodal models.

A number of recent review articles have articulated visions for constructing virtual cells and multimodal single-cell foundation models.<sup>49–51</sup> While these works primarily focus on the promise of multimodality and the integration of diverse biological data, our perspective emphasizes a compositional design approach that explicitly leverages modularity and the integration of modality-specific components as first-class architectural principles. Rather than treating multimodality as a monolithic challenge, we explore how compositional AI can structure and scale single-cell foundation models through reusable, interoperable modules. We broadly discuss and compare the potential existing deep learning architectures and mechanisms for modular composition, highlighting key technical choices, and discuss practical considerations for implementation. In addition, we curate and briefly review early efforts toward building such multimodal models, positioning them within the introduced architectural frameworks.

## MULTI-MODALITY AND COMPOSITIONAL AI

Efforts for building single-cell foundation models (FMs) can be categorized along three main directions, as in Figure 1A. Modeling: how to adopt, modify, or develop architectures and learning paradigms for building foundation models on multimodal data is still an ongoing research question. Importantly, the choice of modeling architecture has direct implications for how effectively different modalities can be integrated and how interpretable the learned representations are for downstream biological analysis. For instance, while a modular approach may limit the interactions of low-level features across different modalities, it enables an easier interpretation of different modules. The unique characteristics of cellular measurements, compared with other types of data such as natural images or language, require specific architectural and inductive bias considerations to develop native foundation models that support both robust multimodal integration and biologically meaningful interpretation. Scale: scaling laws observed in language foundation models<sup>3,25</sup> show a power-law relation between model size, amount of training data, and performance. A recent work investigates the scaling laws for native multimodal models.<sup>52</sup> Recent efforts have scaled to tens of millions of cells and large model sizes, and the continued collection of data will drive further growth in the future. Observation: the number and type of modalities included in the training data. Without diverse observations, even the most effective models and largest datasets will fall short of capturing the true complexity of the underlying biology. The overall progress in multimodal single-cell foundation models will depend on jointly advancing modeling strategies, scaling principles, and the diversity of observed modalities to ensure that increased capacity translates into deeper and more faithful representations of cellular biology.

Cells contain diverse molecular entities such as genetic material, transcripts, proteins, and metabolites that interact to carry out biological functions. Multi-modal experiments aim to capture various aspects and properties of these cellular components and their relations. Each of these measurement modalities provides a unique perspective on cellular function and regulation, and together they offer a more comprehensive view of cellular states and processes than individual measurements. We differentiate

![](images/0c3fd82f46115997b68e50aec2804214857a4a853f2e677b92af3ecc2bfdf2b8.jpg)  
Figure 1. Development of multimodal compositional foundation models

(A) Three major axes underlie the development of multimodal single-cell foundation models: scale, referring to the use of larger datasets and model sizes; modeling, encompassing advances in architecture and learning paradigms; and observation, focusing on the integration of multimodal and multiscale cellular measurements.

(B) Cellular measurements capture diverse biological entities (e.g., RNA and proteins) across various modalities. These measurements can be encoded as different data types—tabular (e.g., gene/protein matrices), imaging, sequential (e.g., nucleotide sequences), or relational (e.g., interaction networks)—which serve as inputs to a multimodal foundation model. Each modality can optionally be encoded with pre-trained unimodal models, taking advantage of a compositional design. Such models enable multiple downstream applications, including learning a shared embedding space, cross-modality prediction, biological mechanism inference, and generative modeling of cellular data.

between employing a multimodal or a multi-view approach, with a multi-view approach involving different representations or encodings of the same modality. For example, spatial transcriptomics data could be structured as a cell-by-gene expression matrix, visualized as an image, or embedded as a graph of cell-cell interactions. While these are distinct views of the same underlying data, they do not form a multimodal readout.

The ability to build multimodal foundation models has been extensively demonstrated in the fields of computer vision and natural language processing, which benefit from internet-scale corpora containing billions of naturally occurring examples. In these domains, high-quality paired datasets enable the joint optimization of encoders, often under the assumption that the modalities are redundant. The availability of large corpora of paired natural images and text has enabled a range of architectural choices, from modality-specific encoders,<sup>21,53</sup> to projection-based strategies,<sup>54,55</sup> and ultimately to unified models<sup>56–60</sup> learning over raw multi-modal input space. However, in cell biology, training a unified non-compositional model is significantly more difficult because paired multimodal measurements are rare relative to the vast amount of available unimodal data. Unlike vision and language, biological modalities are fragmented and may encode useful complementary information, and no single technology currently captures all these distinct aspects simultaneously. Furthermore, the scarcity of biological samples relative to the immense complexity and dimensionality of cellular systems makes it challenging for monolithic architectures to learn robust, generalized representations without the modular flexibility offered by a compositional approach.

We define compositional foundation models through the lens of compositional AI, which we view as a modular design paradigm that emphasizes the principled integration of specialized, modality-specific expert modules at the architectural level. Rather than adopting a monolithic paradigm where a single model is trained on all data types simultaneously, a compositional foundation model involves the modular assembly of independently pre-trained foundation models, such as those for RNA-seq, microscopy imaging, or molecular graphs, into a unified framework (Figure 1B). While the term ‘‘compositionality’’ carries distinct theoretical weight in visual reasoning, cognitive science, and linguistics, its application here is primarily an engineering and architectural solution aimed at scaling models through reusable, interoperable modules that can be updated as new biological data become available. Compositional AI is particularly valuable in scenarios where paired multimodal measurements are scarce or incomplete, a common challenge in single-cell biology. By leveraging independently trained, modalityspecific models, compositional modeling enables meaningful integration and cross-modal inference even when only singlemodality data is available for most samples. For example, a model trained on RNA-seq data can be composed with a pathology model to infer tissue-level features without requiring every sample to have matched imaging data. This reduces the dependency on costly or technically challenging multi-omic experiments while still allowing the model to learn rich, multi-faceted representations of cellular states. As such, compositional AI maximizes the utility of fragmented datasets and enhances model generalization across diverse biological contexts. This modularity also accelerates development, improves interpretability, and supports continual updates as new data types become available.

The attention mechanism, a fundamental component of modern transformer architectures,<sup>24</sup> plays a crucial role in building compositional models. It facilitates flexible information exchange between modality-specific expert modules through the powerful query-key-value framework, enabling alignment of corresponding elements across different modalities and the extraction of novel multimodal insights. While within-modality attention captures and processes modality-specific representations and readouts, cross-modality attention enables the integration of information across modalities, as illustrated in Figure 2. We discuss the attention building blocks for multimodal learning further below.

## Multi-modal measurements

Advances in single-cell technologies have enabled high-resolution profiling of a wide range of cellular modalities. scRNA-seq reveals transcriptional heterogeneity at the single-cell level,<sup>6</sup> while single-cell assay for transposase-accessible chromatin using sequencing (scATAC-seq) identifies regulatory elements through chromatin accessibility.<sup>62</sup> Chromatin modifications and transcription factor binding, measured by chromatin immunoprecipitation sequencing (ChIP-seq), 63 cleavage under targets and release using nuclease (CUT&RUN), 64 and cleavage under targets and tagmentation (CUT&Tag),<sup>65</sup> provide epigenetic insights.<sup>66</sup> Single-cell proteomics quantifies protein levels and modifications,<sup>67</sup> offering a functional perspective on cellular states. Imaging techniques offer spatial and temporal context, capturing subcellular structures and live dynamics. Highthroughput capabilities enable datasets covering millions of cells,<sup>18,19</sup> with some technologies capturing genetic perturbations and images<sup>68–71</sup> or full modalities in spatial omics,<sup>72–77</sup> revealing cellular neighborhoods in tissues. The spatial nature of image data requires adapted model architectures to extract descriptive features.<sup>78</sup> Currently, the two predominant architectures are convolutional neural networks (CNNs) and transformers adapted for image inputs, called vision transformers.<sup>79</sup> Multiple unimodal models for cellular representation learning based on images have been proposed.<sup>80,81</sup> Interestingly, recent advances in computer vision research have shown that image-based representation learning can be improved by multimodal training on image-text pairs.<sup>21,53,82</sup> While not always straightforward due to the lack of text annotations, these findings are beginning to be transferred to biological images, for example, by using transcriptome information instead of text descriptions.<sup>83</sup>

The abundance of these measurements has thus far enabled the development of modality-specific single-cell foundation models. However, constructing a model that spans multiple modalities requires the integration and alignment of data across modalities, facilitated by paired or co-assayed multimodal measurements, as illustrated in Figure 2. A compositional approach leverages the wealth of unimodal measurements to train modality-specific expert modules capable of accurately interpreting and representing each modality. At the same time, it requires a degree of cross-modality supervision to align these expert modules, enabling a coherent multimodal understanding that extends beyond the capabilities of any individual module.

Such cross-modality supervision could be acquired through technologies that allow simultaneous profiling of multiple molecular modalities within a single cell,<sup>84</sup> providing deeper insights into gene regulatory mechanisms.<sup>85,86</sup> For example, co-assays such as SNARE-seq,<sup>87</sup> SHARE-seq,<sup>86</sup> sci-CAR,<sup>85</sup> and scCATseq<sup>88</sup> enable joint measurement of transcriptome and chromatin accessibility, while scM&T-seq<sup>89</sup> and snmCT-seq<sup>90</sup> combine RNA profiling with DNA methylation. Similarly, G&T-seq<sup>91</sup> and DR-seq<sup>92</sup> facilitate the simultaneous capture of genomic DNA and transcriptomes, allowing insights into genotype-phenotype relationships at single-cell resolution. Technologies such as

![](images/72af4fe17a588a09ec24bf44e618a861ffd9ebbecbced681fc6aa61b64df9ca1.jpg)  
Figure 2. Modality availability and anchoring mechanism  
Abundant unimodal datasets enable within-modality learning, while scarce multimodal assays provide critical links between modalities. Anchor modalities, such as transcriptomics, help bridge different data types (e.g., chromatin and protein) using co-assayed measurements like Multiome and CITE-seq. This anchoring enables integration into a unified multimodal foundation space through both within- and cross-modality attention.

CITE-seq,<sup>93</sup> REAP-seq,<sup>94</sup> ASAP-seq,<sup>95</sup> and DOGMA-seq<sup>96</sup> integrate transcriptomics with protein quantification (cell surface or intracellular), bridging the gap between gene expression and functional protein measurements. Trimodal assays, such as TEA-seq,<sup>97</sup> allow simultaneous measurement of RNA, chromatin accessibility, and proteins.

In addition to spatial omics,<sup>73,98–100</sup> spatial multiomics technologies, including DBiT-seq,<sup>101</sup> spatial CITE-seq,<sup>102</sup> SPOTS,<sup>103</sup> SM-OMICS,<sup>104</sup> Stereo-seq-based multiomics,<sup>105,106</sup> SlideseqV2 extensions,<sup>74</sup> and spatial ATAC-RNA co-profiling methods (e.g., spatial-ATAC-seq and spatial CUT&Tag RNAseq<sup>75</sup>) enable joint modality measurements, providing spatial organization of cells and subcellular structure. However, since no single technology currently captures all modalities simultaneously, an anchoring strategy is required to align and integrate different modalities into a shared space as illustrated in Figure 2. For instance, transcriptomics can serve as an anchor modality (a modality shared between different multimodal assays) to integrate Multiome and CITE-seq datasets, connecting chromatin accessibility and protein abundance.

A biological study may involve either paired or unpaired multimodal measurements. Paired measurements capture multiple modalities from the same cell simultaneously. For example, CITE-seq quantifies both transcript and protein abundance, and SHARE-seq<sup>86</sup> measures RNA expression along with the identification of accessible chromatin regions within a single cell. By contrast, unpaired multimodal assays measure different modalities from different biological samples. For instance, scRNA-seq and spatial transcriptomics performed on similar or replicate samples still measure different cells. Several methods have been developed to model paired single-cell multi-omics data .<sup>28,31,107–112</sup> However, the restricted amount of paired multimodal measurements limits their capabilities for learning from independent modalities. Composing a foundation model from a smaller model approach is a promising way to take advantage of the large amount of existing unpaired measurements of distinct modalities by learning the connections between different modalities with minimum direct supervision.

The relative abundance of unpaired measurements motivates the use of distribution alignment strategies, such as optimal transport-based methods,<sup>113–116</sup> which align feature distributions across modalities without requiring direct cell-tocell correspondence. Recently, continuous-time generative modeling approaches based on flow matching have emerged as a principled alternative for learning mappings between complex high-dimensional distributions .<sup>117</sup> Flow matching learns a time-dependent vector field whose induced probability flow transforms a simple reference distribution into a target data distribution, avoiding explicit likelihood computation and adversarial training. Importantly, conditional and optimal-transportinspired variants of flow matching enable learning stochastic couplings between distributions without requiring paired samples.<sup>118,119</sup> In the context of multimodal single-cell data, such methods provide a natural framework for modeling modalityto-modality translations by defining conditional flows that transport cells from one modality’s feature space to another while preserving global distributional structure. Compared with static alignment approaches, flow-matching-based models offer continuous, invertible transformations and scale favorably to high-dimensional settings, making them particularly appealing for compositional foundation models that must integrate large collections of unpaired measurements across diverse experimental modalities. 113,120

## Challenges in modeling across modalities

Different biological measurements are naturally represented by different data structures (Figure 1B). Gene expression data, for instance, is a sparse and highly dispersed count vector for each cell. Therefore, it is typically stored as a cell-bygene matrix in a tabular format requiring consistent gene ordering for machine learning modeling. Similarly, DNA sequences are typically represented as strings of nucleotides, while imaging data captures spatial information in pixel arrays. These underlying data structures each present unique modeling challenges: tabular data require handling high dimensionality and sparsity, sequences need to capture long-range dependencies, and images must process spatial hierarchies while maintaining translational invariance. Multimodal modeling requires handling multiple data structures, while adding challenges, for instance, pooling gene expression data to match a paired image patch.

Beyond these technical challenges, modeling biomedical data with multimodal foundation models requires dealing with the scarcity of data relative to its complexity. Language and vision foundation models benefit from training data that densely sample their underlying distributions—for instance, internetscale corpora that approximate the diversity of human language through billions of naturally occurring examples. By contrast, recent large-scale single-cell studies only capture a tiny fraction of possible cellular states and conditions given the complexity of biological systems. This scarcity of samples, combined with the high dimensionality and heterogeneity of biological data, makes it challenging to learn robust representations that generalize across different biological contexts and experimental conditions while enabling the inference of biological mechanisms.

A fundamental distinction between biological multimodal learning and web-scale multimodal representation learning lies in both data availability and assumptions about cross-modal information content. In vision-language models, modalities are typically designed to be redundant, and large, high-quality paired datasets enable joint optimization of modality-specific encoders using alignment-based objectives. By contrast, biological modalities often encode complementary information, while paired multimodal measurements are rare compared with unimodal data. In addition, cross-modal pairing is often imperfect due to technical effects or biological heterogeneity. These constraints motivate compositional multimodal architectures that reuse pretrained unimodal models and restrict cross-modal learning to lightweight interfaces. However, commonly used contrastive objectives such as InfoNCE implicitly assume semantic overlap by maximizing representation agreement across modalities. While effective for retrieval or matching tasks, such objectives are poorly suited for settings in which modalities must be integrated to recover information absent from any single view. From a methodological perspective, this suggests a need to move beyond alignment-centric interfaces toward integration mechanisms that explicitly model how complementary biological signals interact under limited and noisy pairing.

Recent work has explored increasing the effective availability of paired multimodal data by inferring or synthesizing crossmodal correspondences from large collections of unimodal measurements. For example, scPairing constructs a shared latent space across modalities using pretrained unimodal encoders and contrastive objectives and subsequently generates artificial multimodal profiles via bridge integration.<sup>122</sup> Such approaches can be useful for data augmentation and for enabling training or evaluation in settings with limited experimentally paired data. At the same time, they depend on the structure of the underlying unimodal representations and introduce additional modeling assumptions, suggesting that inferred pairing is best viewed as a complementary tool rather than a general substitute for architectural choices that explicitly account for sparse and imperfect cross-modal coupling.

## INTEGRATING DIFFERENT MODALITIES

A key technical challenge in developing multimodal compositional foundation models for single-cell biology lies in effectively integrating diverse modalities while preserving their biological relationships. Several architectures and approaches have emerged, especially from natural language processing and multimodal machine learning,<sup>123</sup> which show promise for biological applications. Here, we discuss transformers and their attention building blocks, followed by high-level architectural designs for modality integration in compositional models.

## Attention building blocks for multimodal learning

Transformers have become a foundational component of stateof-the-art models in both the language and the vision domain, owing to their remarkable scalability with respect to available training data and computational resources.<sup>25,26</sup> A central element contributing to their strong performance is the attention mechanism, which facilitates data-driven interactions among all input elements. While numerous variants have been proposed to enhance the original transformer architecture,<sup>124–128</sup> its core building blocks—particularly self-attention—have remained largely unchanged. Moreover, the transformer framework, along with its attention mechanism, has been widely adopted for learning from multimodal inputs, especially when combining vision and language modalities.<sup>129–134</sup> Inspired by the different approaches of combining multiple modalities, we outline the four main self-attention building blocks in Box 1 that could be incorporated into any multimodal transformer architecture to integrate different modalities Figures 3A–3D. While ‘‘all-to-all self-attention’’ and ‘‘within-modality self-attention’’ are applied in cross-encoder and bi-encoder architectures, as described in the infobox, ‘‘fused self-attention’’ and ‘‘cross-modality attention’’ remain to be applied to multimodal single-cell foundation models.

## Architectural designs for multimodal learning

Multimodal learning architectures are central to integrating diverse biological data types into unified analytical frameworks. These architectures differ in how they encode, process, align, and interpret information across modalities, with each design offering unique trade-offs between interpretability, performance, reusability, and computational efficiency. In the context of

## Box 1. Attention building blocks

Fused self-attention: fusion is a straightforward and widely used method for integrating related pieces of information through a simple addition operation of different but related pieces of information in the high-dimensional vector space, as illustrated in Figure 3A within the transformer architecture. It was already employed in the original transformer model<sup>24</sup> through the use of positional embeddings, which introduce ordinal information into the sequence of tokens. Due to its simplicity and effectiveness, fusion has since been applied to integrate other types of related data, including multimodal inputs. A similar strategy can be adopted for integrating related single-cell modalities, which aim to capture different aspects of the same biological process. For instance, transcriptomic and proteomic count data reflect the abundance of distinct molecular entities associated with the same underlying gene. Thus, fusion offers a promising approach for combining token embeddings from two or more modalities. All-to-all self-attention: another unit for integrating information while preserving modality-specific identities is the all-to-all attention mechanism (Figure 3B). In this configuration, embeddings from all modalities are concatenated into a single sequence, allowing each token to attend to every other token, regardless of its original modality. This approach is particularly well-suited for leveraging shared and complementary information across modalities. The all-to-all self-attention unit is a fundamental component for constructing cross-encoding architectures with transformers, as it enables comprehensive interaction without discarding modality-specific characteristics. Unlike the fusion mechanism, this mechanism allows for the integration of two or more modalities even when their token semantics are not aligned. Within-modality self-attention: even when constructing a multimodal foundation model, it is often necessary to process each modality individually prior to their full or partial integration. Within-modality self-attention utilizes separate attention heads to handle each modality in isolation (Figure 3C). This component is particularly useful for preprocessing modalities that differ significantly and are therefore unsuitable for early fusion within the network. Such modalities typically require preliminary adaptation and feature extraction before effective integration. For instance, applying several layers of within-modality attention can facilitate the integration of chromatin accessibility data and fluorescence microscopy images, as each encodes distinct biological information. Cross-modality attention: cross-attention was first introduced in the original transformer architecture<sup>24</sup> as a key component for addressing machine translation tasks. In this mechanism, the target language sequence attends to the encoded representations of the source language. Specifically, the queries are derived from the outputs of the preceding decoder layer, while the keys and values originate from the encoder outputs of the source language. In Figure 3D we outline a cross-modality attention building block in which the queries of a single modality are used to pull required information from the keys and values of another modality. This strategy facilitates explicit information exchange between different modalities while effectively reducing the interference of intra-modality noise.

single-cell biology, choosing the right architectural strategy is essential for uncovering meaningful biological relationships across data types. Below, we outline three prominent approaches—cross-encoders, bi-encoders, and language encoding—highlighting their principles and applications. These architectural choices could be either adopted for implementing individual expert modules or the compositional framework in general, as in Figure 1. Table 1 compares the key characteristics of bi-encoders, cross-encoders, and language encoding approaches for integrating different modalities in single-cel biology. The comparison highlights the trade-offs between accuracy, efficiency, and scalability for each paradigm.

## Cross-encoder

Cross-encoders process multiple modalities jointly through a single encoder, allowing direct modeling of interactions between different data types.<sup>135,136</sup> In the context of single-cell biology, this approach enables the model to capture complex relationships between modalities. For example, when integrating gene expression with corresponding proteomics data, a crossencoder can learn the gene-protein dependencies.<sup>31</sup> This joint processing allows the model to understand the fine-grained contextual relationships that might be missed by processing each modality independently. While cross-encoders often achieve superior performance in capturing inter-modality relationships,<sup>137</sup> they come with computational limitations due to their need to process each pair of inputs jointly, leading to slower inference and scalability issues for large-scale retrieval.<sup>138</sup> Their utility is limited in scenarios where only one modality is available at inference time. Moreover, this approach makes it challenging to reuse or fine-tune existing pre-trained unimodal models, a promising strategy for training multimodal models, when only a limited amount of paired data is available. From an implementation perspective, in the case of adopting a transformer architecture, all-to-all self-attention could be the main unit for building cross-encoder models.

## Bi-encoder

Bi-encoders, also referred to as dual encoders, by contrast, employ separate encoders for each modality before integrating their representations in a shared latent space.<sup>139,140</sup> While these individual encoders can sometimes share weights, forming what is known as a Siamese network,<sup>141,142</sup> their primary function remains the independent transformation of their respective input modalities. The key characteristic of the bi-encoder is that the interaction between the modalities primarily occurs after the initial encoding stage. Once each modality’s embedding is generated, a similarity metric, such as cosine similarity or dot product, is applied to quantify their relationship. This architecture offers greater flexibility and computational efficiency, as each modality can be processed independently. In singlecell applications, bi-encoders are particularly valuable when (C) Within-modality self-attention for parallel processing of different modalities in order to induce a hierarchical structure for learning.

A  
![](images/e0577d2cf1951cf28c47504acbba6fce8168e7375d1e1adde01e4eb48bef6655.jpg)

![](images/8b92ec6f109631c3fdd4be2500e1802d6b590227eda9a8e0fe3340eb7f71e350.jpg)

![](images/4fa4cc4b8fbd148bc39cfdf9ce8c52435770be4ba8b05db5cd029eb912fc8d45.jpg)

![](images/44ee635eb96c8ecb2be12e8fc71f29e50d10626e6e6e8c36a8b16f5027d7ffc7.jpg)

Integration architectures  
![](images/2f4ea174f1727fe9709beebfd60eef61ec93d5002a3b00a2016be9eab9cea6f3.jpg)  
Figure 3. Transformer self-attention building blocks and model architectures for multimodal learning  
(A) Fused self-attention through an additive block as a simple yet effective way of merging two related modalities.  
(B) All-to-all self-attention for processing all information from all modalities together.

(D) Cross-modality attention for explicit exchange of information between different modalities while keeping the hierarchical processing of each. Three paradigms for integrating biological modalities are shown.

(E) Cross-encoder models jointly process inputs from multiple modalities to learn rich inter-modality interactions, though at a higher computational cost.

(F) Bi-encoder models use separate encoders for each modality and align their embeddings in a shared space, enabling efficient and scalable training, especiall for unpaired data.

(G) Language-encoding models represent biological data as text sequences, allowing the use of LLMs to unify diverse modalities through languagemodeling tasks.

working with unpaired measurements or when fast inference is needed.<sup>33,41,43,143</sup> For instance, a bi-encoder can align chromatin accessibility (ATAC) information with gene expression information by contrastive learning, using CLIP training with an InfoNCE loss.<sup>33</sup> The bi-encoder strategy also allows for the reuse of pre-trained models designed for individual modalities. This approach is particularly advantageous in scenarios where paired modality measurements are scarce. The main trade-off with biencoders is their reduced ability to model fine-grained interactions between modalities, as they rely on the alignment of independently computed representations.<sup>144</sup> However, their scalability and flexibility often make them a practical choice for large-scale biological applications. In order to implement them, within-modality self-attention can be used for building transformer-based bi-encoders by keeping the modality processing independent, at least for the very first layers.

<table><tr><td colspan="3">Table 1. Comparison of bi-encoder, cross-encoder, and language encoding approaches</td></tr><tr><td colspan="3"></td></tr><tr><td>Feature</td><td>Bi-encoder Cross-encoder</td><td>Language encoding leveraging LLM architectures</td></tr><tr><td>Architecture Processing</td><td>twin tower independent encoding of</td><td>single encoder joint encoding</td></tr><tr><td>each modality</td><td>of combined modalities occurs during encoding (attention</td><td>encoding biological data as text</td></tr><tr><td>Interaction Output</td><td>occurs after encoding (similarity metric) mechanisms)</td><td>implicit through LLM pre-training and text input</td></tr><tr><td>for each modality</td><td>separate embedding vectors single score representing the relationship</td><td>textual representation r mbeddings derived from text</td></tr><tr><td>Accuracy</td><td>lower for fine-grained understanding</td><td>higher for fine-grained understanding depends on the quality of text encoding and LLM</td></tr><tr><td>Efficiency tasks</td><td>high, epecially foal low, requires processing each pair individually</td><td>can be efficient depending on the LLMused</td></tr><tr><td>Scalability high, embeddings</td><td>low, computational cost increases with can be pre-computed data size</td><td>depends on the LLM&#x27;s scalability</td></tr><tr><td>Typical use cases</td><td>large-scale retrieval, QA, ranking, precise similarity tasks unpaired data analysis</td><td>integrating prior knowledge, multimodal data fusion, leveraging LLMs</td></tr></table>

## Language encoding

Recent advances in LLMs have inspired a novel approach to multimodal integration in single-cell biology: encoding biological measurements as text.<sup>50,145</sup> This paradigm treats various biological measurements—including gene expression values, chromatin accessibility scores, or protein abundances—as ‘‘words’’ in a biological vocabulary. By converting different modalities into a common text-based format, these models can leverage the powerful architectures and pre-training strategies developed for language models. For example, gene expression profiles can be represented as a sequence of gene names ordered by their expression levels, effectively creating a ‘‘cell sentence.’’ Similarly, metadata annotations or experimental conditions can be directly incorporated as textual information.<sup>146</sup> Language encoding offers several advantages for biological applications. It provides a natural way to incorporate prior biological knowledge through text descriptions and annotations. It also enables seamless integration of qualitative and quantitative data types. For example, cell-type annotations, pathway descriptions, and numerical measurements can all be processed within the same framework. Furthermore, it introduces new avenues for modeling interactions using human-readable prompts and commands, enabling the interactive generation of novel biological hypotheses. However, care must be taken to ensure that important biological information is not lost in the text encoding process. The granularity of the textual representation and the choice of vocabulary are critical factors that can influence the model’s ability to capture the nuances of biological data. Additionally, the performance of these models heavily relies on the quality and relevance of the textual information used for encoding. Recent research has also demonstrated the potential of repurposing pre-trained LLMs, originally trained on natural language corpora, for biomedical applications.<sup>44</sup> Depending on the implementation preferences, both all-to-all self-attention and within-modality self-attention can be used for language encoding models.

## Current approaches

There is a rich literature on modality-specific single-cell models and analysis tools taking into account the nuances and unique signal characteristics of each modality. Building on top of them, several foundation model approaches have been proposed, trying to learn a specific modality at scale. Many examples have been developed from single-cell genomics<sup>147,148</sup> (such as DNABERT<sup>149</sup> and EVO<sup>150</sup>) to transcriptomics<sup>151</sup> (such as Geneformer<sup>4</sup> and scGPT<sup>5</sup>) and digital histopathology 52 (such as UNI<sup>153</sup> and GigaPath<sup>154</sup>), each focusing on a single data modality. Several models have been proposed in recent years to develop large-scale models that go beyond a single modality. Bi-encoder models such as scCLIP,<sup>33</sup> SCARF,<sup>34</sup> and CAPTAIN<sup>155</sup> emphasize modularity by learning modality-specific representations that are aligned through contrastive or attention-based mechanisms, which can offer flexibility and scalability across heterogeneous data types. By contrast, cross-encoder approaches, including Nicheformer,<sup>6</sup> CellPLM,<sup>156</sup> scGPT-spatial, 37 and STPath,<sup>157</sup> jointly model multiple modalities within a shared representation space, enabling explicit cross-modal interactions that are well suited to tightly coupled data such as spatial transcriptomics and imaging. Orthogonal to this architectural distinction, several methods—such as GenePT,<sup>146</sup> Cell2Sentence, 158 CellHermes,<sup>159</sup> OKR-Cell,<sup>160</sup> and CellWhisperer<sup>43</sup>—reformulate biological measurements and prior knowledge as natural language, leveraging LLMs for representation learning, annotation, and reasoning. Hybrid frameworks such as Precious3GPT<sup>41</sup> and spEMO<sup>160</sup> further illustrate how different unimodal foundation models can be combined in a compositional manner to balance expressive multimodal interaction with computational efficiency. Table 2 provides an overview of the existing methods for multimodal integration in singlecell biology. The table includes the model name, its underlying architecture, the omic modalities it supports, and its key characteristics. The architectural assignment of each model is not always straightforward, as custom modifications and hybrid approaches often blur the boundaries between standard model categories.

<table><tr><td colspan="4">Table 2. Comparison of multimodal omics models and their architectures, modalities, and key characteristics</td></tr><tr><td>Model ScCLIP33</td><td>Architecture bi-encoder</td><td>Modalities scRNA-seq, scATAC</td><td>Key characteristics separate transformers for RNA and ATAC modalities;</td></tr><tr><td></td><td></td><td></td><td>contrastive alignment of multimodal embeddings (CLIP-style)</td></tr><tr><td>SCARF34</td><td>bi-encoder</td><td>scRNA-seq, scATAC</td><td>separat nsformers r NA nATACodalies; combined contrastive alignment of multimodal embeddings and reconstruction of each modality</td></tr><tr><td>Nicheformer</td><td>cross-encoder</td><td>scRNA-seq, spatial transcriptomics</td><td>modality-specific tokens; within-modality mask language modeling; shared weights across modalities</td></tr><tr><td>CelIPLM156</td><td>cross-encoder</td><td>scRNA-seq, spatial transcriptomics</td><td>genes from neighboring cells can help predict the masked genes of other cells; encodes spatial coordinates using 2D positional encodings</td></tr><tr><td>ScGPT-spatial37</td><td>cross-encoder</td><td>scRNA-seq, spatial transcriptomics</td><td>spatially sampled input tokens; mask language modeling with mixture-of-expert decoders</td></tr><tr><td>CellWhisperer43</td><td>bi-encoder</td><td>bulk RNA, scRNA-seq</td><td>transcriptome data paired with natural language annotations; multimodal contrastive training and instruction tuning of LLMs modalities in cross-encoder, text embeddings in bi-</td></tr><tr><td>Precious3GPT41</td><td>cross-encoder</td><td>transcriptomics, epigenetics, proteomics, knowledge graphs</td><td>encoder; combines cross-encoder for multimodal interaction and bi-encoder for efficiency whole slide images (WSls) paired with spatial</td></tr><tr><td>STPath 157</td><td></td><td>image, spatial transcriptomics</td><td>transcriptomics; represent each spot within a WSI by fusing information foifferet dalites; usn alred eisti pathology foundation model (Gigapath)</td></tr><tr><td>GenePT146</td><td>language encoding</td><td>scRNA-seq, text</td><td>gene names ordered by expression or LLM embeddings; ChatGPT embeddings of gene descriptions used to generate cell embeddings</td></tr><tr><td>Cell2Sentence158</td><td>language encoding</td><td>scRNA-seq, text</td><td>expression profiles transformed into cell sentences; fine-tunes LLMs on synthetic sentences for generation and annotation tasks</td></tr><tr><td>LangCell161</td><td>bi-encoder</td><td>scRNA-seq, text</td><td>uinified representation of cells and language; pre-trains on paired scRNA and text; zero-shot celltype annotation</td></tr><tr><td>scChat162</td><td>language encoding</td><td>scRNA-seq, text</td><td>uses GPT-4o for annotation; hypothesis generation, experiment design</td></tr><tr><td>CELLama 163</td><td>language encoding</td><td>scRNA-seq, spatial transcriptomics, text</td><td>gene expression and metadata as ranked gene lists; encodes all data as text and embeds via sentence transformers</td></tr><tr><td>scELMo164</td><td>language encoding</td><td>scRNA-seq, CITE-seq, text</td><td>weighted NLP embeddings of features and metadata; creates metadata-aware embeddings via LLMs and integrates them with raw data</td></tr><tr><td>spEMO160</td><td>bi-encoder</td><td>spatial transcriptomics, spatial multi-omics, text, histopathology images</td><td>unifies pathology FMs and LLMs for spatial analysis; enables spatial domain identification, disease prediction, and automated medical report generation</td></tr><tr><td>OKR-Cell10</td><td>bi-encoder</td><td>scRNA-seq, text</td><td>scGPT for the cellular branch and Clinical-LongFormer for the textual branch; cross-modal robust alignment (CRA) with curriculum learning to handle noisy data</td></tr><tr><td>CellHermes 159</td><td>language encoding</td><td>scRNA-seq, PPI networks, text</td><td>unifying tabular (scRNA-seq) and graph (PPI) by reformulating them into natural language question-answer pairs; multi-task prediction by instruction fine-tuning;</td></tr><tr><td>CAPTAIN155</td><td>bi-encoder</td><td>scRNA-seq, proteomics</td><td>functioning as an encoder, a predictor, and an explainer dual-encoder architecture with cross-modal attention fusion; incorporating prior knowledge (GRNs, promoters)</td></tr></table>

## TOWARD MULTIMODAL SINGLE-CELL FOUNDATIONMODELS

Multimodal single-cell foundation models have the potential to advance our understanding of cellular states by integrating diverse molecular and spatial data. These models promise to advance therapeutic discoveries, personalized medicine, and fundamental biological understanding through data-driven discovery processes that complement traditional hypothesis-driven research. How can we achieve that vision, and what are the challenges to consider?

## Integrating prior knowledge

Incorporating biological prior knowledge into multimodal singlecell foundation models can improve learning efficiency, model robustness, and interpretability—particularly in settings where purely data-driven approaches fall short due to data sparsity, noise, or limited coverage across biological contexts.<sup>46,165–167</sup> Such priors embed well-established biological principles that help constrain model behavior, guide representation learning, and enhance generalization across data modalities and experimental systems.

Several forms of biological knowledge are especially valuable for this purpose. Ontologies such as the Gene Ontology (GO) and Cell Ontology (CL) capture structured, hierarchical relationships between genes and cell types, respectively, and provide curated functional annotations that reflect consensus biological understanding .<sup>168,169</sup> SCimilarity<sup>170</sup> is a recent foundational approach that incorporates cell ontology structures into its training objective. Gene regulatory networks (GRNs) offer another critical form of prior knowledge, as they encode directed relationships between transcription factors and their target genes. These networks, often constructed from ChIP-seq, CUT&RUN, and CUT&- Tag experiments,<sup>63–65</sup> perturbation assays, or literature mining, represent mechanistic underpinnings of transcriptional regulation. In contrast to co-expression patterns learned from data, GRNs introduce causality and control into the modeling process, enabling biologically grounded inference of transcriptional regulation over time. <sup>171</sup> Curated databases such as KEGG, Reactome, and MSigDB provide pathway-level annotations that define canonical signaling cascades, metabolic routes, and gene sets representing conserved biological processes. 172–174 These modules can also be used to organize latent spaces, enforce coherence in prediction tasks, and offer interpretable biological structure to model outputs. Likewise, protein-protein interaction (PPI) networks capture functional or physical associations between proteins, reflecting post-transcriptional regulation and co-regulated modules that extend beyond transcriptional readouts.

In addition to molecular-level priors, models can also benefit from spatial and temporal information. Spatial transcriptomics and time-series single-cell data provide insights into the organization of cells within tissues and their progression over time during development, differentiation, or disease. Part of such knowledge is already captured in a data-driven approach in recent technological advancements such as spatial omics; however, established anatomical and histological knowledge accumulated over decades remains invaluable for interpreting and constraining spatial patterns. Likewise, longstanding insights from developmental biology and time-resolved lineage tracing studies have immense potential to provide critical context for modeling dynamic cellular processes.

From a methodological perspective, these diverse types of prior knowledge can be integrated using several strategies. Graph neural networks (GNNs)<sup>175,176</sup> are naturally suited for handling structured data such as ontologies and PPI networks, enabling the propagation of information along known biological interactions. Alternatively, attention-based architectures such as transformers<sup>24</sup> and graph attention networks can incorporate less structured descriptions of biological knowledge, merging both quantitative measurements and qualitative domain expertise. In practice, many of these priors are most effectively incorporated through compositional or modular model designs. For example, distinct GNN or transformer modules can be assigned to different knowledge graphs—such as GRNs, PPIs, or ontologies—and their outputs integrated with modality-specific encoders via cross-attention, allowing each prior to influence learning at an appropriate resolution. Such modularization supports interpretability and extensibility, as individual components can be updated as biological knowledge evolves without retraining the entire model.

Moreover, regularization techniques and multi-task learning frameworks can be designed to enforce biological constraints (for example, local continuity in spatial transcriptomics data or temporal smoothness in time-course experiments) during mode training.<sup>178,179</sup> A key design choice concerns the balance between hard constraints and soft regularization: hard constraints (e.g., masking edges to known GRNs or enforcing pathway-level latent dimensions) can improve biological plausibility but risk limiting model flexibility when priors are incomplete or contextdependent, whereas soft constraints implemented through regularization terms, auxiliary losses, or Bayesian priors allow models to deviate from canonical knowledge when supported by data. Hybrid strategies that combine weakly enforced priors with data-driven adaptation are likely to be particularly effective for single-cell settings, where both noise and biological heterogeneity are pervasive.

Language modeling offers a promising avenue for systematically integrating this wealth of prior clinical and biological knowledge into multimodal single-cell models. By encoding and retrieving structured information from unstructured biomedical literature, clinical guidelines, and ontologies, language models can serve as dynamic knowledge interfaces bridging textual and experimental domains to inform representation learning and downstream biological inference.

## Multiscale

Biological systems operate across scales, from molecular mechanisms to ecosystems-level phenomena. While most foundation models focus on individual scales, for example a molecular readout, pioneering works envision how to bridge scales.<sup>49,180</sup> Recent bi-encoder architectures demonstrate promise, particularly in combining subcellular features with tissue-level context.<sup>181</sup> Patient representation learning further shows how single-cell analyses can inform organism-scale understanding.<sup>182</sup> Extending uni-scale foundation models to integrate both across modalities and across biological scales will be crucial for the vision of a virtual cell.<sup>49</sup> Transitions between successive scales are well suited to compositional AI because the underlying task is structurally similar regardless of which specific scales are being connected. Indeed, a compositional model using cross-attention in combination with cross-scale fine-tuning has recently been proposed to derive a common representation from existing foundation models at different scales. 183 Given its comparatively low cost per cell and its ability to use different magnifications seamlessly, microscopy imaging is particularly well suited to connect biology across scales. Hence, while rare for other modalities, computational models integrating different image scales have been developed, most prominently for cell segmentation.<sup>184–187</sup>

## Multimodal data management

High-throughput technologies have enabled unprecedented data generation, but a significant imbalance persists between unimodal and paired multimodal measurements. While multimodal measurements naturally include diverse information, unimodal readouts are often cheaper, and one modality may be more economic than another. The availability of large pretraining datasets raises the question of how relevant a given modality is compared with more data of another modality. Therefore, it is important to determine optimal strategies for balancing data quantity, modality diversity, and measurement depth while developing robust methods for integrating these diverse data types. Initial research suggests that the creation of diverse training datasets is crucial 188 and that foundation models trained on abundant unimodal data can be effectively fine-tuned for multimodal tasks, potentially offering a practical path forward.<sup>189</sup> However, data from separate modalities are often available in different amounts, and adding more modalities is usually associated with different costs. Images, for example, are often cheap to acquire and comparatively simple to add as an additional modality, as demonstrated in spatial transcriptomics and -proteomics techniques.<sup>77,190</sup> However, imaging data, due to the absence of rich spatial labels by default, are usually harder to interpret than, for example, transcriptomics data. In contrast to imaging, profiling the transcriptome jointly with molecular modalities such as chromatin accessibility<sup>62</sup> or protein abundance<sup>93</sup> is more limited in depth and throughput.

## Evaluation

Quantitative metrics like zero-shot cell-type classification accuracy provide essential benchmarks for systematic model evaluation and method development. However, although high performance on classification tasks demonstrates a model’s ability to learn meaningful cellular representations, it may not directly translate to improvements in downstream applications such as drug discovery or disease modeling. Therefore, biological foundation models require additional evaluation strategies that capture their broader scientific utility. For multimodal models, evaluation becomes particularly challenging due to the need to assess cross-modal predictions and the quality of integrated representations.<sup>29</sup> A key limitation is that most metrics used to evaluate multimodal models are inherited from unimodal settings and primarily quantify downstream performance, without indicating whether improvements arise from true cross-modal integration or from aggregating redundant information already present in a dominant modality. This obscures whether a model actually exploits complementary signals across modalities. Addressing this gap will require evaluation criteria and benchmark tasks that are explicitly sensitive to cross-modal complementarity, rather than accuracy alone, particularly in settings where relevant information is distributed across modalities.

An example is cross-modality prediction, which evaluates a model’s ability to predict one modality from another, for example predicting protein abundance from transcriptomics data.<sup>23,191</sup> This task can provide a metric for mutual information across different modalities while also evaluating a multi-modal foundation model’s capability to recover the underlying mutual dependency. Moreover, shifting from the evaluation tasks based on expert annotations (e.g., cell-type or nichetype annotation<sup>6</sup>) to intrinsic, expert-agnostic benchmarks such as cross-modality prediction and perturbation prediction will enable unbiased and data-driven assessments of model performance that are less dependent on subjective labeling choices, easily scalable across datasets and experimental conditions, and more directly reflective of whether the learned representations capture biologically meaningful relationships between modalities. We have compiled a broad list of evaluation tasks based on both categories in Box 2. A multi-faceted evaluation approach will ensure that technical improvements translate to meaningful biological insights. Community-driven challenges focused on specific biological questions could also complement existing metrics and drive innovation in both model development and evaluation methodologies.<sup>191,192</sup>

## CONCLUSIONS

Compositional foundation models hold significant promise for advancing our understanding of cellular states in health and disease by unifying heterogeneous molecular and spatial data across different modalities. Integrating diverse single-cell measurements—including transcriptomic, chromatin accessibility, protein abundance, spatial organization, microscopy imaging, and textual descriptions—into cohesive representations is key to unlocking their full potential for therapeutic discovery. We explored the technical foundations necessary for this vision, including the use of compositional AI for modular design, deep learning approaches including transformer architectures with various attention mechanisms, and distinct architectural designs. Despite significant progress, challenges remain, particularly concerning the structural differences of modality representations, data availability, and the scarcity of biological samples relative to the complexity of cellular systems. Addressing these technical hurdles is crucial for charting a path toward comprehensive virtual cell models.

Looking ahead, the development of multimodal cellular foundation models requires continued effort along several key axes. A central direction involves enhancing integration and alignment across diverse modalities, moving beyond reliance on scarce paired measurements toward strategies that integrate unimodal foundation models. Crucially, incorporating various forms of biological prior knowledge will be essential to improve model robustness, interpretability, and generalization, especially in data-sparse settings. Furthermore, future models must aspire to integrate information not only across modalities but also across biological scales, connecting subcellular features with tissue-level context to move closer to the vision of a virtua cell. Strategic management of increasingly large and diverse multimodal datasets, considering the balance between data quantity, modality diversity, and measurement cost, is paramount. Compositional foundation models offer a distinctive opportunity for integration with autonomous AI agents,<sup>193–198</sup> enabling the automation of the complex and demanding process of therapeutic target discovery and thereby accelerating progress in biomedical research. Finally, alongside technical advancements, the development of rigorous and biologically relevant evaluation strategies is necessary to ensure that improvements in model performance translate into meaningful scientific utility for downstream applications like drug discovery and disease understanding. By synthesizing these technical advancements and addressing these future challenges, multimodal AI can truly begin to decode the complexity of cellular systems.

<table><tr><td>Box 2. Evaluations</td></tr><tr><td>EXPERT ANNOTATION-BASED</td></tr><tr><td>Sublurniynctionpredictionspreiciheeistubcellulrechaniowleas. gene/prot/p function and regulatory network interactions).</td></tr><tr><td>Cell type and state annotation: predicting expert-annotated cell identities and cellular states (e.g., activation states or differentiation stages), often across datasets or technologies, to assess biological coherence and transferability.</td></tr><tr><td>Tisse, nihe or spatial domainannotation: assigning cel oexpert-define spatial niches ortissueregions in spalr multimodal datasets.</td></tr><tr><td>Disease stateor condition classification:predictingdisease labels, clinical phenotypes,rexperimentalconditions .., treated vs. control).</td></tr><tr><td>Trajectory orineage stage labeling:apping cel to annotated developmental stages orpseudotime bins derivedfrom curated references.</td></tr><tr><td>INTRINSIC (EXPERT-AGNOSTIC)</td></tr><tr><td>Masked feature reconstruction and/or denoising: reconstructing held-out genes, peaks, or proteins within or across mo- dalities.</td></tr><tr><td>Cross-modality prediction and/or modality matching: predicting one modality from another (e.g., protein abundance from transcriptomics) or matching profiles originating from the same cell, probing learned cross-modal dependencies and</td></tr><tr><td>complementarity.</td></tr><tr><td>Perurbation response prediction: predicting transcriptional ormultimodal responses to genetic, chemical, or environmental perturbations. Joint embedding of modalities: learning a shared low-dimensional representation that captures biological signals while</td></tr></table>

## ACKNOWLEDGMENTS

M.B. and T.R. are supported by the Helmholtz Association under the joint research school ‘‘Munich School For Data Science.’’ N.A.S. is supported by the Add-On Fellowship of the Joachim Herz Foundation. F.J.T. acknowledges support by the European Union (ERC, DeepCell—101054957). Views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council. Neithe the European Union nor the granting authority can be held responsible for them. Figures are partly created with https://BioRender.com.

## DECLARATION OF INTERESTS

N.A.S. consulted for Lamin Labs GmbH. F.J.T. consults for Immunai, CytoReason, Cellarity, and Omniscope and has an ownership interest in Dermagnostix GmbH and Cellarity.

## DECLARATION OF GENERATIVE AI AND AI-ASSISTED TECHNOLOGIES IN THE WRITING PROCESS

During the preparation of this work, the authors used ChatGPT by OpenAI and Grammarly by Grammarly Inc. in order to refine the language. After using these tools or services, the authors reviewed and edited the content as needed and take full responsibility for the content of the publication.

## REFERENCES

1. Devlin, J., Chang, M.-W., Lee, K., and Toutanova, K. (2019). BERT: Pretraining of Deep Bidirectional Transformers for Language Understanding. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, 1, J. Burstein, C. Doran, and T. Solorio, eds. (Association for Computational Linguistics), pp. 4171–4186. https://doi.org/10.18653/ v1/N19-1423.

2. Radford, A., Narasimhan, K., Salimans, T., and Sutskever, I. (2018). Improving Language Understanding by Generative Pre-training. https:// cdn.openai.com/research-covers/language-unsupervised/language\_ understanding\_paper.pdf.

3. Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I. (2019). Language Models are Unsupervised Multitask Learners. https:// www.semanticscholar.org/paper/Language-Models-are-Unsupervised-Multitask-Learners-Radford-Wu/9405cc0d6169988371b2755e573cc 28650d14dfe.

4. Theodoris, C.V., Xiao, L., Chopra, A., Chaffin, M.D., Al Sayed, Z.R., Hill, M.C., Mantineo, H., Brydon, E.M., Zeng, Z., Liu, X.S., et al. (2023). Transfer learning enables predictions in network biology. Nature 618, 616–624. https://doi.org/10.1038/s41586-023-06139-9.

5. Cui, H., Wang, C., Maan, H., Pang, K., Luo, F., Duan, N., and Wang, B. (2024). scGPT: toward building a foundation model for single-cell multiomics using generative AI. Nat. Methods 21, 1470–1480. https://doi. org/10.1038/s41592-024-02201-0.

6. Schaar, A.C., Tejada-Lapuerta, A., Palla, G., Gutgesell, R., Minaeva, M., Vornholz, L., Dony, L., Drummer, F., and Theis, F.J. (2024). Nicheformer: a Foundation Model for Single-Cell and Spatial Omics. Nat. Methods 22, 2525–2538.

7. Rosen, Y., Roohani, Y., Agrawal, A., Samotorcan, L., Consortium, T.S., Quake, S.R., and Leskovec, J. (2023). Universal Cell Embeddings: A Foundation Model for Cell Biology. Preprint at bioRxiv. https://doi.org/ 10.1101/2023.11.28.568918.

8. Bahrami, M., Tejada-Lapuerta, A., Becker, S., F.S.H., G., and Theis, F.J. (2025). scConcept: Contrastive pretraining for technology-agnostic single-cell representations beyond reconstruction. Preprint at bioRxiv. https://doi.org/10.1101/2025.10.14.682419.

9. Shen, H., Liu, J., Hu, J., Shen, X., Zhang, C., Wu, D., Feng, M., Yang, M., Li, Y., Yang, Y., et al. (2023). Generative pretraining from large-scale transcriptomes for single-cell deciphering. iScience 26, 106536. https://doi. org/10.1016/j.isci.2023.106536.

10. Yang, F., Wang, W., Wang, F., Fang, Y., Tang, D., Huang, J., Lu, H., and Yao, J. (2022). scBERT as a large-scale pretrained deep language model for cell type annotation of single-cell RNA-seq data. Nat. Mach. Intell. 4, 852–866. https://doi.org/10.1038/s42256-022-00534-z.

11. Hao, M., Gong, J., Zeng, X., Liu, C., Guo, Y., Cheng, X., Wang, T., Ma, J., Zhang, X., and Song, L. (2024). Large-scale foundation model on singlecell transcriptomics. Nat. Methods 21, 1481–1491. https://doi.org/10. 1038/s41592-024-02305-7.

12. Regev, A., Teichmann, S.A., Lander, E.S., Amit, I., Benoist, C., Birney, E., Bodenmiller, B., Campbell, P., Carninci, P., Clatworthy, M., et al. (2017). The Human Cell Atlas. eLife 6, e27041. https://doi.org/10.7554/eLife.27041.

13. Tarhan, L., Bistline, J., Chang, J., Galloway, B., Hanna, E., and Weitz, E. (2023). Single Cell Portal: an interactive home for single-cell genomics data. Preprint at bioRxiv. https://doi.org/10.1101/2023.07.13.548886.

14. Schaum, N., Karkanias, J., Neff, N.F., May, A.P., Quake, S.R., Wyss-Coray, T., Darmanis, S., Batson, J., Botvinnik, O., and Chen, M.B. (2018). Singlecell transcriptomics of 20 mouse organs creates a Tabula Muris. Nature 562, 367–372. https://doi.org/10.1038/s41586-018-0590-4.

15. The Tabula; Sapiens Consortium, Jones, R.C., Karkanias, J., Krasnow, M.A., Pisco, A.O., Quake, S.R., Salzman, J., Yosef, N., Bulthaup, B., Brown, P., and et al.. (2022). The Tabula Sapiens: A multiple-organ, single-cell transcriptomic atlas of humans. Science 376, eabl4896. https:// doi.org/10.1126/science.abl4896.

16. CZI; Cell Science Program, Abdulla, S., Aevermann, B., Assis, P., Badajoz, S., Bell, S.M., Bezzi, E., Cakir, B., Chaffer, J., Chambers, S., and et al.. (2025). CZ CELLxGENE Discover: a single-cell data platform for scalable exploration, analysis and modeling of aggregated data. Nucleic Acids Res. 53, D886–D900. https://doi.org/10.1093/nar/gkae1142.

17. Edgar, R., Domrachev, M., and Lash, A.E. (2002). Gene Expression Omnibus: NCBI gene expression and hybridization array data repository. Nucleic Acids Res. 30, 207–210. https://doi.org/10.1093/nar/30.1.207.

18. Chandrasekaran, S.N., Ackerman, J., Alix, E., Ando, D.M., Arevalo, J., Bennion, M., Boisseau, N., Borowa, A., Boyd, J.D., Brino, L., et al. (2023). JUMP Cell Painting dataset: morphological impact of 136,000 chemical and genetic perturbations. Preprint at bioRxiv. https://doi. org/10.1101/2023.03.23.534023.

19. Uhle´ n, M., Fagerberg, L., Hallstro¨ m, B.M., Lindskog, C., Oksvold, P., Mardinoglu, A., Sivertsson, A<sup>˚</sup> ., Kampf, C., Sjo¨ stedt, E., Asplund, A., et al. (2015). Proteomics. Tissue-based map of the human proteome. Science 347, 1260419. https://doi.org/10.1126/science.1260419.

20. Chen, T., Kornblith, S., Norouzi, M., and Hinton, G. (2020). A simple framework for contrastive learning of visual representations. Proceedings of the 37th International Conference on Machine Learning Volume 119 of ICML’20. https://dl.acm.org/doi/10.5555/3524938.3525087.

21. Radford, A., Kim, J.W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., et al. (2021). Learning Transferable Visual Models From Natural Language Supervision. Preprint at ar-Xiv. https://doi.org/10.48550/arXiv.2103.00020.

22. Ji, Y., Tejada-Lapuerta, A., Schmacke, N.A., Zheng, Z., Zhang, X., Khan, S., Rothenaigner, I., Tschuck, J., Hadian, K., Theis, F.J., et al. (2024). Scalable and universal prediction of cellular phenotypes enables in silico experiments. Preprint at bioRxiv. https://doi.org/10.1101/2024. 08.12.607533.

23. Richter, T., Bahrami, M., Xia, Y., Fischer, D.S., and Theis, F.J. (2024). Delineating the effective use of self-supervised learning in single-cell genomics. Nat. Mach. Intell. 7, 68–78. https://doi.org/10.1038/s42256-024- 00934-3.

24. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., and Kaiser, L. (2017). Polosukhin I. Attention is All you Need. Advances in Neural Information Processing Systems 30. Curran Associates, Inc. https://proceedings.neurips.cc/paper\_files/paper/2017/file/ 3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf.

25. Kaplan, J., McCandlish, S., Henighan, T., Brown, T.B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., and Amodei, D. (2020). Scaling Laws for Neural Language Models. Preprint at arXiv. https://doi.org/10.48550/ar-Xiv.2001.08361.

26. Zhai, X., Kolesnikov, A., Houlsby, N., and Beyer, L. (2022). Scaling Vision Transformers. Preprint at arXiv. https://doi.org/10.48550/arXiv. 2106.04560.

27. Argelaguet, R., Velten, B., Arnol, D., Dietrich, S., Zenz, T., Marioni, J.C., Buettner, F., Huber, W., and Stegle, O. (2018). Multi-omics factor analysis—a framework for unsupervised integration of multi-omics data sets. Mol. Syst. Biol. 14, e8124. https://doi.org/10.15252/msb. 20178124.

28. Stuart, T., Butler, A., Hoffman, P., Hafemeister, C., Papalexi, E., Mauck, W.M., Hao, Y., Stoeckius, M., Smibert, P., and Satija, R. (2019). Comprehensive integration of single-cell data. Cell 177, 1888–1902.e21. https:// doi.org/10.1016/j.cell.2019.05.031.

29. Luecken, M.D., Bu¨ ttner, M., Chaichoompu, K., Danese, A., Interlandi, M., Mueller, M.F., Strobl, D.C., Zappia, L., Dugas, M., Colome´ -Tatche´ , M., et al. (2022). Benchmarking atlas-level data integration in single-cell genomics. Nat. Methods 19, 41–50. https://doi.org/10.1038/s41592-021- 01336-8.

30. Lotfollahi, M., Hao, Y., Theis, F.J., and Satija, R. (2024). The future of rapid and automated single-cell data analysis using reference mapping. Cell 187, 2343–2358. https://doi.org/10.1016/j.cell.2024.03.009.

31. Gayoso, A., Steier, Z., Lopez, R., Regier, J., Nazor, K.L., Streets, A., and Yosef, N. (2021). Joint probabilistic modeling of single-cell multi-omic data with totalVI. Nat. Methods 18, 272–282. https://doi.org/10.1038/ s41592-020-01050-x.

32. Fischer, D.S., Schaar, A.C., and Theis, F.J. (2023). Modeling intercellular communication in tissues using spatial graphs of cells. Nat. Biotechnol. 41, 332–336. https://doi.org/10.1038/s41587-022-01467-z.

33. Xiong, L., Chen, T., and Kellis, M. (2023). scCLIP: Multi-modal Single-cell Contrastive Learning Integration Pre-training. https://xiong-lei.com/ assets/pdf/scclip.pdf.

34. Liu, G., Zhao, Y., Zhao, Y., Wang, T., Cai, Q., Wang, X., Wen, Z., Lin, L., Yang, G., and Chen, J. (2025). SCARF: Single Cell ATAC-seq and RNAseq Foundation model. Preprint at bioRxiv. https://doi.org/10.1101/ 2025.04.07.647689.

35. Liu, L., Li, W., Wong, K.-C., Yang, F., and Yao, J. (2023). A pre-trained large generative model for translating single-cell transcriptome to proteome. Preprint at bioRxiv. https://doi.org/10.1101/2023.07.04.547619.

36. Tang, W., Wen, H., Liu, R., Ding, J., Jin, W., Xie, Y., Liu, H., and Tang, J. (2023). Single-Cell Multimodal Prediction via Transformers. Preprint at arXiv. https://doi.org/10.1145/3583780.3615061.

37. Wang, C., Cui, H., Zhang, A., Xie, R., Goodarzi, H., and Wang, B. (2025). sC + spatial. Preprint at bioRxiv. https://doi.org/10.1101/2025.02.05. 636714.

38. Wen, H., Tang, W., Dai, X., Ding, J., Jin, W., Xie, Y., and Tang, J. (2023). CellPLM: Pre-training of Cell Language Model Beyond Single Cells. https://openreview.net/forum?id=BKXvPDekud.

39. Luo, R., Sun, L., Xia, Y., Qin, T., Zhang, S., Poon, H., and Liu, T.-Y. (2022). BioGPT: Generative Pre-trained Transformer for Biomedical Text

## Cell Systems Perspective

Generation and Mining. Brief. Bioinform. 23, bbac409. https://doi.org/10. 1093/bib/bbac409.

40. Ankit Pal, M.S. (2024). Openbiollms: Advancing open-source large language models for healthcare and life sciences. https://huggingface.co/ aaditya/OpenBioLLM-Llama3-70B.

41. Galkin, F., Naumov, V., Pushkov, S., Sidorenko, D., Urban, A., Zagirova, D., Alawi, K.M., Aliper, A., Gumerov, R., Kalashnikov, A., et al. (2024). Precious3GPT: Multimodal Multi-Species Multi-Omics Multi-Tissue Transformer for Aging Research and Drug Discovery. Preprint at bioRxiv. https://doi.org/10.1101/2024.07.25.605062.

42. Zhao, S., Zhang, J., Wu, Y., Luo, Y., and Nie, Z. (2024). LangCell: Language-Cell Pre-training for Cell Identity Understanding. Preprint at arXiv. https://doi.org/10.48550/arXiv.2405.06708.

43. Schaefer, M., Peneder, P., Malzl, D., Peycheva, M., Burton, J., Hakobyan, A., Sharma, V., Krausgruber, T., Menche, J., Tomazou, E.M., et al. (2024). Multimodal learning of transcriptomes and text enables interactive single-cell RNA-seq data exploration with natural-language chats. Preprint at bioRxiv. https://doi.org/10.1101/2024.10.15.618501.

44. Lu, Y.-C., Varghese, A., Nahar, R., Chen, H., Shao, K., Bao, X., and Li, C. (2024). scChat: A Large Language Model-Powered Co-Pilot for Contextualized Single-Cell RNA Sequencing Analysis. Preprint at bioRxiv. https://doi.org/10.1101/2024.10.01.616063.

45. Choi, H., Park, J., Kim, S., Kim, J., Lee, D., Bae, S., Shin, H., and Lee, D. (2024). CELLama: Foundation Model for Single Cell and Spatial Transcriptomics by Cell Embedding Leveraging Language Model Abilities. Preprint at bioRxiv. https://doi.org/10.1101/2024.05.08.593094.

46. Guo, Z.-H., Wu, Y., Wang, S., Zhang, Q., Shi, J.-M., Wang, Y.-B., and Chen, Z.-H. (2023). scInterpreter: a knowledge-regularized generative model for interpretably integrating scRNA-seq data. BMC Bioinform. 24, 481. https://doi.org/10.1186/s12859-023-05579-4.

47. Cheng, P., Peng, Y., Zhang, X.-L., Chen, S., Fang, B.-B., Li, Y.-Z., and Sun, Y.-M. (2024). A natural language processing system for the efficient extraction of cell markers. Sci. Rep. 14, 21183. https://doi.org/10.1038/ s41598-024-72204-6.

48. Liu, T., Chen, T., Zheng, W., Luo, X., and Zhao, H. (2025). scELMo: Embeddings from Language Models are Good Learners for Single-cell Data Analysis. Preprint at bioRxiv. https://doi.org/10.1101/2023.12.07. 569910.

49. Bunne, C., Roohani, Y., Rosen, Y., Gupta, A., Zhang, X., Roed, M., Alexandrov, T., AlQuraishi, M., Brennan, P., Burkhardt, D.B., et al. (2024). How to build the virtual cell with artificial intelligence: Priorities and opportunities. Cell 187, 7045–7063. https://doi.org/10.1016/j.cell.2024. 11.015.

50. Szałata, A., Hrovatin, K., Becker, S., Tejada-Lapuerta, A., Cui, H., Wang, B., and Theis, F.J. (2024). Transformers in single-cell omics: a review and new perspectives. Nat. Methods 21, 1430–1443. https://doi.org/ 10.1038/s41592-024-02353-z.

51. Cui, H., Tejada-Lapuerta, A., Brbic, � M., Saez-Rodriguez, J., Cristea, S., Goodarzi, H., Lotfollahi, M., Theis, F.J., and Wang, B. (2025). Towards multimodal foundation models in molecular cell biology. Nature 640, 623–633. https://doi.org/10.1038/s41586-025-08710-y.

52. Shukor, M., Fini, E., da Costa, V.G.T., Cord, M., Susskind, J., and El-Nouby, A. (2025). Scaling Laws for Native Multimodal Models. https:// openaccess.thecvf.com/content/ICCV2025/html/Shukor\_Scaling\_Laws\_ for\_Native\_Multimodal\_Models\_ICCV\_2025\_paper.html.

53. Jia, C., Yang, Y., Xia, Y., Chen, Y.-T., Parekh, Z., Pham, H., Le, Q., Sung, Y.-H., Li, Z., and Duerig, T. (2021). Scaling up visual and vision-language representation learning with noisy text supervision. International conference on machine learning. https://proceedings.mlr.press/v139/jia21b/ jia21b.pdf.

54. Bai, J., Bai, S., Yang, S., Wang, S., Tan, S., Wang, P., Lin, J., Zhou, C., and Zhou, J. (2023). Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond. Preprint at arXiv. https://doi.org/10.48550/arXiv.2308.12966.

55. Li, J., Li, D., Savarese, S., and Hoi, S. (2023). Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large

language models. Preprint at arXiv. https://doi.org/10.48550/arXiv. 2301.12597.

56. Team, G., Anil, R., Borgeaud, S., Alayrac, J.-B., Yu, J., Soricut, R., Schalkwyk, J., Dai, A.M., Hauth, A., Millican, K., et al. (2023). Gemini: a Family of Highly Capable Multimodal Models. Preprint at arXiv. https:// doi.org/10.48550/arXiv.2312.11805.

57. Alayrac, J.-B., Donahue, J., Luc, P., Miech, A., Barr, I., Hasson, Y., Lenc, K., Mensch, A., Millican, K., Reynolds, M., et al. (2022). Flamingo: a visual language model for few-shot learning. Preprint at arXiv. https://doi.org/ 10.48550/arXiv.2204.14198.

58. Driess, D., Xia, F., Sajjadi, M.S.M., Lynch, C., Chowdhery, A., Ichter, B., Wahid, A., Tompson, J., Vuong, Q., Yu, T., et al. (2023). Palm-e: An embodied multimodal language model. Preprint at arXiv. https://doi. org/10.48550/arXiv.2303.03378.

59. Reed, S., Zolna, K., Parisotto, E., Colmenarejo, S.G., Novikov, A., Barth-Maron, G., Gimenez, M., Sulsky, Y., Kay, J., Springenberg, J.T., et al. (2022). A generalist agent. Preprint at arXiv. https://doi.org/10.48550/ar-Xiv.2205.06175.

60. Yu, J., Xu, Y., Koh, J.Y., Luong, T., Baid, G., Wang, Z., Vasudevan, V., Ku, A., Yang, Y., Ayan, B.K., et al. (2022). Scaling autoregressive models for content-rich text-to-image generation. Preprint at arXiv. https://doi.org/ 10.48550/arXiv.2206.10789.

61. Tang, F., Barbacioru, C., Wang, Y., Nordman, E., Lee, C., Xu, N., Wang, X., Bodeau, J., Tuch, B.B., Siddiqui, A., et al. (2009). mRNA-Seq wholetranscriptome analysis of a single cell. Nat. Methods 6, 377–382. https:// doi.org/10.1038/nmeth.1315.

62. Buenrostro, J.D., Wu, B., Litzenburger, U.M., Ruff, D., Gonzales, M.L., Snyder, M.P., Chang, H.Y., and Greenleaf, W.J. (2015). Single-cell chromatin accessibility reveals principles of regulatory variation. Nature 523, 486–490. https://doi.org/10.1038/nature14590.

63. Johnson, D.S., Mortazavi, A., Myers, R.M., and Wold, B. (2007). Genome-Wide Mapping of in Vivo Protein-DNA Interactions. Science 316, 1497–1502. https://doi.org/10.1126/science.1141319.

64. Skene, P.J., and Henikoff, S. (2017). An efficient targeted nuclease strategy for high-resolution mapping of DNA binding sites. eLife 6, e21856. https://doi.org/10.7554/eLife.21856.

65. Kaya-Okur, H.S., Wu, S.J., Codomo, C.A., Pledger, E.S., Bryson, T.D., Henikoff, J.G., Ahmad, K., and Henikoff, S. (2019). CUT&Tag for efficient epigenomic profiling of small samples and single cells. Nat. Commun. 10, 1930. https://doi.org/10.1038/s41467-019-09982-5.

66. Barski, A., Cuddapah, S., Cui, K., Roh, T.-Y., Schones, D.E., Wang, Z., Wei, G., Chepelev, I., and Zhao, K. (2007). High-Resolution Profiling of Histone Methylations in the Human Genome. Cell 129, 823–837. https://doi.org/10.1016/j.cell.2007.05.009.

67. Guo, T., Steen, J.A., and Mann, M. (2025). Mass-spectrometry-based proteomics: from single cells to clinical applications. Nature 638, 901–911. https://doi.org/10.1038/s41586-025-08584-0.

68. Schmacke, N.A., Ma¨ dler, S.C., Wallmann, G., Metousis, A., Be´ routi, M., Harz, H., Leonhardt, H., Mann, M., and Hornung, V. (2023). Sparcs, a platform for genome-scale crispr screening for spatial cellular phenotypes. Preprint at bioRxiv. https://doi.org/10.1101/2023.06.01.542416.

69. Fandrey, C.I., Jentzsch, M., Konopka, P., Hoch, A., Blumenstock, K., Zackria, A., Maasewerd, S., Lovotti, M., Lapp, D.J., Gohr, F.N., et al. (2024). Nis-seq enables cell-type-agnostic optical perturbation screening. Nat. Biotechnol. 43, 1337–1347. https://doi.org/10.1038/ s41587-024-02516-5.

70. Kudo, T., Meireles, A.M., Moncada, R., Chen, Y., Wu, P., Gould, J., Hu, X., Kornfeld, O., Jesudason, R., Foo, C., et al. (2024). Multiplexed, image-based pooled screens in primary cells and tissues with perturbview. Nat. Biotechnol. 43, 1091–1100. https://doi.org/10.1038/s41587-024- 02391-0.

71. Bock, C., Datlinger, P., Chardon, F., Coelho, M.A., Dong, M.B., Lawson, K.A., Lu, T., Maroc, L., Norman, T.M., Song, B., et al. (2022). High-content CRISPR screening. Nat. Rev. Methods Prim. 2, 8. https://doi.org/ 10.1038/s43586-021-00093-4.

72. Sta˚ hl, P.L., Salme´ n, F., Vickovic, S., Lundmark, A., Navarro, J.F., Magnusson, J., Giacomello, S., Asp, M., Westholm, J.O., Huss, M., et al. (2016). Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. Science 353, 78–82. https://doi.org/10. 1126/science.aaf2403.

73. Chen, K.H., Boettiger, A.N., Moffitt, J.R., Wang, S., and Zhuang, X. (2015). RNA imaging. Spatially resolved, highly multiplexed RNA profiling in single cells. Science 348, aaa6090. https://doi.org/10.1126/science. aaa6090.

74. Rodriques, S.G., Stickels, R.R., Goeva, A., Martin, C.A., Murray, E., Vanderburg, C.R., Welch, J., Chen, L.M., Chen, F., and Macosko, E.Z. (2019). Slide-seq: A scalable technology for measuring genome-wide expression at high spatial resolution. Science 363, 1463–1467. https://doi.org/ 10.1126/science.aaw1219.

75. Zhang, D., Deng, Y., Kukanja, P., Agirre, E., Bartosovic, M., Dong, M., Ma, C., Ma, S., Su, G., Bao, S., et al. (2023). Spatial epigenome– transcriptome co-profiling of mammalian tissues. Nature 616, 113–122. https://doi.org/10.1038/s41586-023-05795-1.

76. Deng, Y., Bartosovic, M., Ma, S., Zhang, D., Kukanja, P., Xiao, Y., Su, G., Liu, Y., Qin, X., Rosoklija, G.B., et al. (2022). Spatial profiling of chromatin accessibility in mouse and human tissues. Nature 609, 375–383. https:// doi.org/10.1038/s41586-022-05094-1.

77. Rosenberger, F.A., Ma¨ dler, S.C., Thorhauge, K.H., Steigerwald, S., Fromme, M., Lebedev, M., Weiss, C.A.M., Oeller, M., Wahle, M., Metousis, A., et al. (2025). Deep Visual Proteomics maps proteotoxicity in a genetic liver disease. Nature 642, 484–491. https://doi.org/10.1038/ s41586-025-08885-4.

78. Ma¨ dler, S.C., Schmacke, N.A., Palma, A., Namsaraeva, A., Can, A.O., Varlamova, V., Heumos, L., Arunkumar, M., Wallmann, G., Hornung, V., et al. (2025). scPortrait integrates single-cell images into multimodal modeling. Preprint at bioRxiv. https://doi.org/10.1101/2025.09.22. 677590.

79. Dosovitskiy, A., Beyer, L., Kolesnikov, A., Weissenborn, D., Zhai, X., Unterthiner, T., Dehghani, M., Minderer, M., Heigold, G., Gelly, S., et al. (2020). An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. https://openreview.net/forum?id=YicbFdNTTy.

80. Gupta, A., Wefers, Z., Kahnert, K., Hansen, J.N., Leineweber, W., Cesnik, A., Lu, D., Axelsson, U., Ballllosera Navarro, F., Karaletsos, T., et al. (2024). Subcell: Vision foundation models for microscopy capture single-cell biology. Preprint at bioRxiv. https://doi.org/10.1101/2024.12. 06.627299.

81. Kraus, O., Kenyon-Dean, K., Saberian, S., Fallah, M., McLean, P., Leung, J., Sharma, V., Khan, A., Balakrishnan, J., Celik, S., et al. (2024). Masked autoencoders for microscopy are scalable learners of cellular biology. https://openaccess.thecvf.com/content/CVPR2024/papers/Kraus\_Masked Autoencoders\_for\_Microscopy\_are\_Scalable\_Learners\_of\_Cellular\_Biology\_ CVPR\_2024\_paper.pdf.

82. Zhai, X., Mustafa, B., Kolesnikov, A., and Beyer, L. (2023). Sigmoid loss for language image pre-training. Proceedings of the IEEE/CVF International Conference on Computer Vision, 11975–11986. https:// openaccess.thecvf.com/content/ICCV2023/papers/Zhai\_Sigmoid\_Loss\_ for\_Language\_Image\_Pre-Training\_ICCV\_2023\_paper.pdf.

83. Lee, Y., Liu, X., Hao, M., Liu, T., and Regev, A. (2024). Pathomclip: Connecting tumor histology with spatial gene expression via locally enhanced contrastive learning of pathology and single-cell foundation model. Preprint at bioRxiv. https://doi.org/10.1101/2024.12.10.627865.

84. Zhu, C., Preissl, S., and Ren, B. (2020). Single-cell multimodal omics: the power of many. Nat. Methods 17, 11–14. https://doi.org/10.1038/ s41592-019-0691-5.

85. Cao, J., Cusanovich, D.A., Ramani, V., Aghamirzaie, D., Pliner, H.A., Hill, A.J., Daza, R.M., McFaline-Figueroa, J.L., Packer, J.S., Christiansen, L., et al. (2018). Joint profiling of chromatin accessibility and gene expression in thousands of single cells. Science 361, 1380–1385. https://doi. org/10.1126/science.aau0730.

86. Ma, S., Zhang, B., LaFave, L.M., Earl, A.S., Chiang, Z., Hu, Y., Ding, J., Brack, A., Kartha, V.K., Tay, T., et al. (2020). Chromatin Potential Identified by Shared Single-Cell Profiling of RNA and Chromatin. Cell 183, 1103–1116.e20. https://doi.org/10.1016/j.cell.2020.09.056.

87. Chen, S., Lake, B.B., and Zhang, K. (2019). High-throughput sequencing of the transcriptome and chromatin accessibility in the same cell. Nat. Biotechnol. 37, 1452–1457. https://doi.org/10.1038/s41587-019- 0290-0.

88. Liu, L., Liu, C., Quintero, A., Wu, L., Yuan, Y., Wang, M., Cheng, M., Leng, L., Xu, L., Dong, G., et al. (2019). Deconvolution of single-cell multi-omics layers reveals regulatory heterogeneity. Nat. Commun. 10, 470. https:// doi.org/10.1038/s41467-018-08205-7.

89. Angermueller, C., Clark, S.J., Lee, H.J., Macaulay, I.C., Teng, M.J., Hu, T.X., Krueger, F., Smallwood, S.A., Ponting, C.P., Voet, T., et al. (2016). Parallel single-cell sequencing links transcriptional and epigenetic heterogeneity. Nat. Methods 13, 229–232. https://doi.org/10.1038/ nmeth.3728.

90. Clark, S.J., Argelaguet, R., Kapourani, C.-A., Stubbs, T.M., Lee, H.J., Alda-Catalinas, C., Krueger, F., Sanguinetti, G., Kelsey, G., Marioni, J.C., et al. (2018). scNMT-seq enables joint profiling of chromatin accessibility DNA methylation and transcription in single cells. Nat. Commun. 9, 781. https://doi.org/10.1038/s41467-018-03149-4.

91. Macaulay, I.C., Haerty, W., Kumar, P., Li, Y.I., Hu, T.X., Teng, M.J., Goolam, M., Saurat, N., Coupland, P., Shirley, L.M., et al. (2015). G&T-seq: parallel sequencing of single-cell genomes and transcriptomes. Nat. Methods 12, 519–522. https://doi.org/10.1038/nmeth.3370.

92. Dey, S.S., Kester, L., Spanjaard, B., Bienko, M., and van Oudenaarden, A. (2015). Integrated genome and transcriptome sequencing of the same cell. Nat. Biotechnol. 33, 285–289. https://doi.org/10.1038/ nbt.3129.

93. Stoeckius, M., Hafemeister, C., Stephenson, W., Houck-Loomis, B., Chattopadhyay, P.K., Swerdlow, H., Satija, R., and Smibert, P. (2017). Simultaneous epitope and transcriptome measurement in single cells. Nat. Methods 14, 865–868. https://doi.org/10.1038/nmeth.4380.

94. Peterson, V.M., Zhang, K.X., Kumar, N., Wong, J., Li, L., Wilson, D.C., Moore, R., McClanahan, T.K., Sadekova, S., and Klappenbach, J.A. (2017). Multiplexed quantification of proteins and transcripts in single cells. Nat. Biotechnol. 35, 936–939. https://doi.org/10.1038/nbt.3973.

95. Mimitou, E.P., Lareau, C.A., Chen, K.Y., Zorzetto-Fernandes, A.L., Hao, Y., Takeshima, Y., Luo, W., Huang, T.-S., Yeung, B.Z., Papalexi, E., et al. (2021). Scalable, multimodal profiling of chromatin accessibility, gene expression and protein levels in single cells. Nat. Biotechnol. 39, 1246– 1258. https://doi.org/10.1038/s41587-021-00927-2.

96. Kim, J., Schanzer, N., Singh, R.S., Zaman, M.I., Garcia-Medina, J.S., Proszynski, J., Ganesan, S., Dan Landau, P., C.Y., Melnick, A.M., et al. (2025). Chapter three – dogma-seq and multimodal, single-cell analysis in acute myeloid leukemia. In Epigenetic Regulation of Cancer – Part D vol. 390 of International Review of Cell and Molecular Biology, L. Galluzzi and S. Spada, eds. (Academic Press), pp. 67–108. https://doi.org/10. 1016/bs.ircmb.2024.08.001.

97. Swanson, E., Lord, C., Reading, J., Heubeck, A.T., Genge, P.C., Thomson, Z., Weiss, M.D., Li, X.-J., Savage, A.K., Green, R.R., et al. (2021). Simultaneous trimodal single-cell measurement of transcripts, epitopes, and chromatin accessibility using TEA-seq. eLife 10, e63632. https://doi. org/10.7554/eLife.63632.

98. Eng, C.L., Lawson, M., Zhu, Q., Dries, R., Koulena, N., Takei, Y., Yun, J., Cronin, C., Karp, C., Yuan, G.-C., et al. (2019). Transcriptome-scale super-resolved imaging in tissues by RNA seqFISH. Nature 568, 235–239. https://doi.org/10.1038/s41586-019-1049-y.

99. Goltsev, Y., Samusik, N., Kennedy-Darling, J., Bhate, S., Hale, M., Vazquez, G., Black, S., and Nolan, G.P. (2018). Deep Profiling of Mouse Splenic Architecture with CODEX Multiplexed Imaging. Cell 174, 968– 981.e15. https://doi.org/10.1016/j.cell.2018.07.010.

100. Keren, L., Bosse, M., Thompson, S., Risom, T., Vijayaragavan, K., McCaffrey, E., Marquez, D., Angoshtari, R., Greenwald, N.F., Fienberg, H., et al. (2019). MIBI-TOF: A multiplexed imaging platform relates cellular phenotypes and tissue structure. Sci. Adv. 5, eaax5851. https://doi.org/ 10.1126/sciadv.aax5851.

101. Liu, Y., Yang, M., Deng, Y., Su, G., Enninful, A., Guo, C.C., Tebaldi, T., Zhang, D., Kim, D., Bai, Z., et al. (2020). High-Spatial-Resolution Multiomics Sequencing via Deterministic Barcoding in Tissue. Cell 183, 1665–1681.e18. https://doi.org/10.1016/j.cell.2020.10.026.

## Cell Systems Perspective

102. Liu, Y., DiStasio, M., Su, G., Asashima, H., Enninful, A., Qin, X., Deng, Y., Nam, J., Gao, F., Bordignon, P., et al. (2023). High-plex protein and whole transcriptome co-mapping at cellular resolution with spatial CITE-seq. Nat. Biotechnol. 41, 1405–1409. https://doi.org/10.1038/s41587-023- 01676-0.

103. Ben-Chetrit, N., Niu, X., Swett, A.D., Sotelo, J., Jiao, M.S., Stewart, C.M., Potenski, C., Mielinis, P., Roelli, P., Stoeckius, M., et al. (2023). Integration of whole transcriptome spatial profiling with protein markers. Nat. Biotechnol. 41, 788–793. https://doi.org/10.1038/s41587-022-01536-3.

104. Vickovic, S., Lo¨ tstedt, B., Klughammer, J., Mages, S., Segerstolpe, A<sup>˚</sup> ., Rozenblatt-Rosen, O., and Regev, A. (2022). SM-Omics is an automated platform for high-throughput spatial multi-omics. Nat. Commun. 13, 795. https://doi.org/10.1038/s41467-022-28445-y.

105. Chen, A., Liao, S., Cheng, M., Ma, K., Wu, L., Lai, Y., Qiu, X., Yang, J., Xu, J., Hao, S., et al. (2022). Spatiotemporal transcriptomic atlas of mouse organogenesis using DNA nanoball-patterned arrays. Cell 185, 1777– 1792.e21. https://doi.org/10.1016/j.cell.2022.04.003.

106. Liao, S., Heng, Y., Liu, W., Xiang, J., Ma, Y., Chen, L., Feng, X., Jia, D., Liang, D., Huang, C., et al. (2023). Integrated Spatial Transcriptomic and Proteomic Analysis of Fresh Frozen Tissue Based on Stereo-seq. Preprint at bioRxiv. https://doi.org/10.1101/2023.04.28.538364.

107. Ashuach, T., Gabitto, M.I., Koodli, R.V., Saldi, G.-A., Jordan, M.I., and Yosef, N. (2023). MultiVI: deep generative model for the integration of multimodal data. Nat. Methods 20, 1222–1231. https://doi.org/10. 1038/s41592-023-01909-9.

108. Argelaguet, R., Arnol, D., Bredikhin, D., Deloro, Y., Velten, B., Marioni, J.C., and Stegle, O. (2020). MOFA+: A statistical framework for comprehensive integration of multi-modal single-cell data. Genome Biol. 21, 111. https://doi.org/10.1186/s13059-020-02015-1.

109. Zuo, C., and Chen, L. (2021). Deep-joint-learning analysis model of single cell transcriptome and open chromatin accessibility data. Brief. Bioinform. 22, bbaa287. https://doi.org/10.1093/bib/bbaa287.

110. Cao, Z.-J., and Gao, G. (2022). Multi-omics single-cell data integration and regulatory inference with graph-linked embedding. Nat. Biotechnol. 40, 1458–1466. https://doi.org/10.1038/s41587-022-01284-4.

111. Korsunsky, I., Millard, N., Fan, J., Slowikowski, K., Zhang, F., Wei, K., Baglaenko, Y., Brenner, M., Loh, P.-R., and Raychaudhuri, S. (2019). Fast, sensitive and accurate integration of single-cell data with Harmony. Nat. Methods 16, 1289–1296. https://doi.org/10.1038/s41592-019-0619-0.

112. Welch, J.D., Kozareva, V., Ferreira, A., Vanderburg, C., Martin, C., and Macosko, E.Z. (2019). Single-Cell Multi-omic Integration Compares and Contrasts Features of Brain Cell Identity. Cell 177, 1873–1887.e17. https://doi.org/10.1016/j.cell.2019.05.006.

113. Klein, D., Palla, G., Lange, M., Klein, M., Piran, Z., Gander, M., Meng-Papaxanthos, L., Sterr, M., Saber, L., Jing, C., et al. (2025). Mapping cells through time and space with moscot. Preprint at bioRxiv. https://doi. org/10.1038/s41586-024-08453-2.

114. Schiebinger, G., Shu, J., Tabaka, M., Cleary, B., Subramanian, V., Solomon, A., Gould, J., Liu, S., Lin, S., Berube, P., et al. (2019). Optimal-transport analysis of single-cell gene expression identifies developmental trajectories in reprogramming. Cell 176, 928–943.e22. https://doi.org/10. 1016/j.cell.2019.01.006.

115. Demetci, P., Santorella, R., Sandstede, B., Noble, W.S., and Singh, R. (2022). Scot: single-cell multi-omics alignment with optimal transport. J. Comput. Biol. 29, 3–18. https://doi.org/10.1089/cmb.2021.0446.

116. Cao, K., Hong, Y., and Wan, L. (2021). Manifold alignment for heterogeneous single-cell multi-omics data integration using pamona. Bioinformatics 38, 211–219. https://doi.org/10.1093/bioinformatics/btab594.

117. Lipman, Y., Chen, R.T.Q., Ben-Hamu, H., Nickel, M., and Le, M. (2022). Flow Matching for Generative Modeling. Preprint at arXiv. https://doi. org/10.48550/arXiv.2210.02747.

118. Tong, A., Fatras, K., Malkin, N., Huguet, G., Zhang, Y., Rector-Brooks, J., Wolf, G., and Bengio, Y. (2024). Improving and generalizing flow-based generative models with minibatch optimal transport. Preprint at arXiv. https://doi.org/10.48550/arXiv.2302.00482.

119. Albergo, M.S., and Vanden-Eijnden, E. (2023). Building normalizing flows with stochastic interpolants. Preprint at arXiv. https://doi.org/10.48550/ arXiv.2209.15571.

120. Klein, D., Fleck, J.S., Bobrovskiy, D., Zimmermann, L., Becker, S., Palma, A., Dony, L., Tejada-Lapuerta, A., Huguet, G., Lin, H.-C., et al. (2025). CellFlow enables generative single-cell phenotype modeling with flow matching. Preprint at bioRxiv. https://doi.org/10.1101/2025.04.11. 648220.

121. Oord, A.v. d., Li, Y., and Vinyals, O. (2018). Representation Learning with Contrastive Predictive Coding. Preprint at arXiv. https://doi.org/10. 48550/arXiv.1807.03748.

122. Niu, J., Vasquez-Rios, C., and Ding, J. (2025). Single-cell multiomics data integration and generation with scpairing. Cell Rep. Methods 5, 101211. https://doi.org/10.1016/j.crmeth.2025.101211.

123. Humeau, S., Shuster, K., Lachaux, M.-A., and Weston, J. (2020). Poly-encoders: Architectures and pre-training strategies for fast and accurate multi-sentence scoring. International Conference on Learning Representations. https://openreview.net/forum?id=SkxgnnNFvH.

124. Choromanski, K., Likhosherstov, V., Dohan, D., Song, X., Gane, A., Sarlos, T., Hawkins, P., Davis, J., Mohiuddin, A., Kaiser, L., et al. (2020). Rethinking Attention with Performers. Preprint at arXiv. https://doi.org/ 10.48550/arXiv.2009.14794.

125. Tay, Y., Dehghani, M., Bahri, D., and Metzler, D. (2022). Efficient transformers: A survey. ACM Comput. Surv. 55, 1–28. https://doi.org/10. 1145/3530811.

126. Kitaev, N., Kaiser, Ł., and Levskaya, A. (2020). Reformer: the Efficient Transformer. Preprint at arXiv. https://doi.org/10.48550/arXiv.2001.04451.

127. Wang, S., Li, B.Z., Khabsa, M., Fang, H., and Ma, H. (2020). Linformer: Self-Attention with Linear Complexity. Preprint at arXiv. https://doi.org/ 10.48550/arXiv.2006.04768.

128. Beltagy, I., Peters, M.E., and Cohan, A. (2020). Longformer: the Long-Document Transformer. Preprint at arXiv. https://doi.org/10.48550/ar-Xiv.2004.05150.

129. Xu, P., Zhu, X., and Clifton, D.A. (2023). Multimodal Learning With Transformers: A Survey. IEEE Trans. Pattern Anal. Mach. Intell. 45, 12113– 12132. https://doi.org/10.1109/TPAMI.2023.3275156.

130. Wang, Z., Yu, J., Yu, A.W., Dai, Z., Tsvetkov, Y., and Cao, Y. (2021). Simvlm: Simple Visual Language Model Pretraining with Weak Supervision. Preprint at arXiv. https://doi.org/10.48550/arXiv.2108.10904.

131. Zhang, P., Li, X., Hu, X., Yang, J., Zhang, L., Wang, L., Choi, Y., and Gao, J. (2021). Vinvl: Revisiting visual representations in vision-language models. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 5579–5588. https://openaccess.thecvf.com/content/ CVPR2021/html/Zhang\_VinVL\_Revisiting\_Visual\_Representations\_in\_ Vision-Language\_Models\_CVPR\_2021\_paper.html.

132. Kim, W., Son, B., and Kim, I. (2021). Vilt: Vision-and-language transformer without convolution or region supervision. International conference on machine learning, pp. 5583–5594. https://proceedings.mlr. press/v139/kim21k/kim21k.pdf.

133. Xu, H., Yan, M., Li, C., Bi, B., Huang, S., Xiao, W., and Huang, F. (2021). E2e-vlp: End-to-End Vision-Language Pre-training Enhanced by Visual Learning. Preprint at arXiv. https://doi.org/10.48550/arXiv.2106.01804.

134. Huang, Z., Zeng, Z., Huang, Y., Liu, B., Fu, D., and Fu, J. (2021). Seeing out of the box: End-to-end pre-training for vision-language representation learning. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 12976–12985. https://openaccess. thecvf.com/content/CVPR2021/papers/Huang\_Seeing\_Out\_of\_the\_Box\_ End-to-End\_Pre-Training\_for\_Vision-Language\_Representation\_CVPR\_ 2021\_paper.pdf.

135. Wolf, T., Sanh, V., Chaumond, J., and Delangue, C. (2019). Transfertransfo: A Transfer Learning Approach for Neural Network Based Conversational Agents. Preprint at arXiv. https://doi.org/10.48550/ar-Xiv.1901.08149.

136. Vig, J., and Ramea, K. (2019). Comparison of transfer-learning approaches for response selection in multi-turn conversations. Workshop on DSTC7 10. https://www.researchgate.net/publication/330554970\_

Comparison\_of\_Transfer-Learning\_Approaches\_for\_Response\_Selection\_in\_ Multi-Turn\_Conversations.

137. Zhang, W., Tan, Q., Li, P., Zhang, Q., and Wang, R. (2023). Cross-modal transformer with language query for referring image segmentation. Neurocomputing 536, 191–205. https://doi.org/10.1016/j.neucom.2023. 03.011.

138. Yadav, N., Monath, N., Angell, R., Zaheer, M., and McCallum, A. (2022). Efficient nearest neighbor search for cross-encoder models using matrix factorization. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, Y. Goldberg, Z. Kozareva, and Y. Zhang, eds. (Association for Computational Linguistics), pp. 2171–2194. https://doi.org/10.18653/v1/2022.emnlp-main.140.

139. Mazare´ , P.-E., Humeau, S., Raison, M., and Bordes, A. (2018). Training Millions of Personalized Dialogue Agents. Preprint at arXiv. https://doi. org/10.48550/arXiv.1809.01984.

140. Dinan, E., Roller, S., Shuster, K., Fan, A., Auli, M., and Weston, J. (2019). Wizard of wikipedia: Knowledge-powered conversational agents. International Conference on Learning Representations. https:// openreview.net/forum?id=r1l73iRqKm.

141. Chen, X., and He, K. (2021). Exploring simple siamese representation learning. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 15750–15758. https://openaccess.thecvf. com/content/CVPR2021/papers/Chen\_Exploring\_Simple\_Siamese\_ Representation\_Learning\_CVPR\_2021\_paper.pdf.

142. Bromley, J., Guyon, I., LeCun, Y., Sa¨ ckinger, E., and Shah, R. (1993). Signature verification using a ‘‘siamese’’ time delay neural network. Advances in Neural Information Processing Systems, 6. https://papers. neurips.cc/paper\_files/paper/1993/file/288cc0ff022877bd3df94bc9360b 9c5d-Paper.pdf.

143. Liu, T., Wang, Y., Ying, R., and Zhao, H. (2023). Muse-gnn: Learning unified gene representation from multimodal biological graph data. In Advances in Neural Information Processing Systems 36, 24661–24677.

144. Chen, Y., Ma, Z., Zhang, Z., Qi, Z., Yuan, C., Li, B., Pu, J., Shan, Y., Qi, X., and Hu, W. (2024). How to make cross encoder a good teacher for efficient image-text retrieval? Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 26994–27003. https:// openaccess.thecvf.com/content/CVPR2024/papers/Chen\_How\_to\_Make Cross\_Encoder\_a\_Good\_Teacher\_for\_Efficient\_CVPR\_2024\_paper.pdf.

145. Consens, M.E., Dufault, C., Wainberg, M., Forster, D., Karimzadeh, M., Goodarzi, H., Theis, F.J., Moses, A., and Wang, B. (2025). Transformers and genome language models. Nat. Mach. Intell. 7, 346–362. https://doi. org/10.1038/s42256-025-01007-9.

146. Chen, Y., and Zou, J. (2024). Genept: a simple but effective foundation model for genes and cells built from chatgpt. Preprint at bioRxiv. https://doi.org/10.1101/2023.10.16.562533.

147. Feng, H., Wu, L., Zhao, B., Huff, C., Zhang, J., Wu, J., Lin, L., Wei, P., and Wu, C. (2025). Benchmarking DNA foundation models for genomic and genetic tasks. Nat. Commun. 16, 10780. https://doi.org/10.1038/ s41467-025-65823-8.

148. Benegas, G., Ye, C., Albors, C., Li, J.C., and Song, Y.S. (2025). Genomic language models: opportunities and challenges. Trends Genet. 41, 286–302. https://doi.org/10.1016/j.tig.2024.11.013.

149. Ji, Y., Zhou, Z., Liu, H., and Davuluri, R.V. (2021). DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome. Bioinformatics 37, 2112–2120. https://doi. org/10.1093/bioinformatics/btab083.

150. Nguyen, E., Poli, M., Durrant, M.G., Kang, B., Katrekar, D., Li, D.B., Bartie, L.J., Thomas, A.W., King, S.H., Brixi, G., et al. (2024). Sequence modeling and design from molecular to genome scale with Evo. Science 386, eado9336. https://doi.org/10.1126/science.ado9336.

151. Baek, S., Song, K., and Lee, I. (2025). Single-cell foundation models: bringing artificial intelligence into cell biology. Exp. Mol. Med. 57, 2169–2181. https://doi.org/10.1038/s12276-025-01547-5.

152. Bilal, M., Aadam, X., Raza, M., Altherwy, Y., Alsuhaibani, A., Abduljabbar, A., Almarshad, F., Golding, P., and Rajpoot, N. (2025). Foundation models in computational pathology: A review of challenges, opportu-

nities, and impact. Preprint at arXiv. https://doi.org/10.48550/arXiv. 2502.08333.

153. Chen, R.J., Ding, T., Lu, M.Y., Williamson, D.F.K., Jaume, G., Song, A.H., Chen, B., Zhang, A., Shao, D., Shaban, M., et al. (2024). Towards a general-purpose foundation model for computational pathology. Nat. Med. 30, 850–862. https://doi.org/10.1038/s41591-024-02857-3.

154. Xu, H., Usuyama, N., Bagga, J., Zhang, S., Rao, R., Naumann, T., Wong, C., Gero, Z., Gonza´ lez, J., Gu, Y., et al. (2024). A whole-slide foundation model for digital pathology from real-world data. Nature 630, 181–188. https://doi.org/10.1038/s41586-024-07441-w.

155. Ji, B., Hu, T., Wang, J., Liu, M., Xu, L., Zhang, Q., Zhong, S., Qiao, L., Zhang, Y., Peng, S., et al. (2025). Captain: A multimodal foundation model pretrained on co-assayed single-cell RNA and protein. Preprint at bioRxiv. https://doi.org/10.1101/2025.07.07.663366.

156. Wen, H., Tang, W., Dai, X., Ding, J., Jin, W., Xie, Y., and Tang, J. (2024). CellPLM: Pre-training of cell language model beyond single cells. In The Twelfth International Conference on Learning Representations. https:// openreview.net/forum?id=BKXvPDekud.

157. Huang, T., Liu, T., Babadi, M., Ying, R., and Jin, W. (2025). Stpath: A generative foundation model for integrating spatial transcriptomics and whole slide images. Preprint at bioRxiv. https://doi.org/10.1101/2025. 04.19.649665.

158. Levine, D., Rizvi, S.A., Le´ vy, S., Pallikkavaliyaveetil, N., Zhang, D., Chen, X., Ghadermarzi, S., Wu, R., Zheng, Z., Vrkic, I., et al. (2024). Cell2sentence: teaching large language models the language of biology. Preprint at bioRxiv. https://doi.org/10.1101/2023.09.11.557287.

159. Gao, Y., Wang, W., Zhao, Y., Dong, K., Shan, C., Zheng, W., Richter, T., Li, Z., Chen, S., Theis, F.J., et al. (2025). Language may be all omics needs: Harmonizing multimodal data for omics understanding with Cell-Hermes. Preprint at bioRxiv. https://doi.org/10.1101/2025.11.07. 687322.

160. Liu, T., Huang, T., Ding, T., Wu, H., Humphrey, P., Perincheri, S., Schalper, K., Ying, R., Xu, H., Zou, J., et al. (2025). spEMO: Leveraging Multi-Modal Foundation Models for Analyzing Spatial Multi-Omic and Histopathology Data. Preprint at bioRxiv. https://doi.org/10.1101/2025. 01.13.632818.

161. Zhao, S., Zhang, J., Wu, Y., Luo, Y., and Nie, Z. (2024). Langcell: Language-Cell Pre-training for Cell Identity Understanding. Preprint at ar-Xiv. https://doi.org/10.48550/arXiv.2405.06708.

162. Lu, Y.-C., Varghese, A., Nahar, R., Chen, H., Shao, K., Bao, X., and Li, C. (2024). scchat: A large language model-powered co-pilot for contextualized single-cell rna sequencing analysis. Preprint at bioRxiv. https://doi. org/10.1101/2024.10.01.616063.

163. Choi, H., Park, J., Kim, S., Kim, J., Lee, D., Bae, S., Shin, H., and Lee, D. (2024). Cellama: Foundation model for single cell and spatial transcriptomics by cell embedding leveraging language model abilities. Preprint at bioRxiv. https://doi.org/10.1101/2024.05.08.593094.

164. Liu, T., Chen, T., Zheng, W., Luo, X., and Zhao, H. (2023). scelmo: Embeddings from language models are good learners for single-cell data analysis. Preprint at bioRxiv. https://doi.org/10.1101/2023.12.07. 569910.

165. Wysocka, M., Wysocki, O., Zufferey, M., Landers, D., and Freitas, A. (2023). A systematic review of biologically-informed deep learning models for cancer: fundamental trends for encoding and interpreting oncology data. BMC Bioinform. 24, 198. https://doi.org/10.1186/ s12859-023-05262-8.

166. Fortelny, N., and Bock, C. (2020). Knowledge-primed neural networks enable biologically interpretable deep learning on single-cell sequencing data. Genome Biol. 21, 190. https://doi.org/10.1186/s13059-020- 02100-5.

167. Stock, M., Losert, C., Zambon, M., Popp, N., Lubatti, G., Ho¨ rmanseder, E., Heinig, M., and Scialdone, A. (2025). Leveraging prior knowledge to infer gene regulatory networks from single-cell RNA-sequencing data. Mol. Syst. Biol. 21, 214–230. https://doi.org/10.1038/s44320-025- 00088-3.

## Cell Systems Perspective

168. Ashburner, M., Ball, C.A., Blake, J.A., Botstein, D., Butler, H., Cherry, J.M., Davis, A.P., Dolinski, K., Dwight, S.S., Eppig, J.T., et al. (2000). Gene Ontology: tool for the unification of biology. The Gene Ontology Consortium. Nat. Genet. 25, 25–29. https://doi.org/10.1038/75556.

169. Diehl, A.D., Meehan, T.F., Bradford, Y.M., Brush, M.H., Dahdul, W.M., Dougall, D.S., He, Y., Osumi-Sutherland, D., Ruttenberg, A., Sarntivijai, S., et al. (2016). The cell ontology 2016: Enhanced content, modularization, and ontology interoperability. J. Biomed. Semant. 7, 44. https://doi. org/10.1186/s13326-016-0088-7.

170. Heimberg, G., Kuo, T., DePianto, D.J., Salem, O., Heigl, T., Diamant, N., Scalia, G., Biancalani, T., Turley, S.J., Rock, J.R., et al. (2025). A cell atlas foundation model for scalable search of similar human cells. Nature 638, 1085–1094. https://doi.org/10.1038/s41586-024-08411-y.

171. Wang, W., Hu, Z., Weiler, P., Mayes, S., Lange, M., Wang, J., Xue, Z., Sauka-Spengler, T., and Theis, F.J. (2024). Regvelo: gene-regulatoryinformed dynamics of single cells. Preprint at bioRxiv. https://doi.org/ 10.1101/2024.12.11.627935.

172. Kanehisa, M., Furumichi, M., Sato, Y., Ishiguro-Watanabe, M., and Tanabe, M. (2021). KEGG: integrating viruses and cellular organisms. Nucleic Acids Res. 49, D545–D551. https://doi.org/10.1093/nar/gkaa970.

173. Gillespie, M., Jassal, B., Stephan, R., Milacic, M., Rothfels, K., Senff-Ribeiro, A., Griss, J., Sevilla, C., Matthews, L., Gong, C., et al. (2022). The reactome pathway knowledgebase 2022. Nucleic Acids Res. 50, D687– D692. https://doi.org/10.1093/nar/gkab1028.

174. Liberzon, A., Birger, C., Thorvaldsdo´ ttir, H., Ghandi, M., Mesirov, J.P., and Tamayo, P. (2015). The Molecular Signatures Database Hallmark Gene Set Collection. Cell Syst. 1, 417–425. https://doi.org/10.1016/j. cels.2015.12.004.

175. Kipf, T.N., and Welling, M. (2017). Semi-Supervised Classification with Graph Convolutional Networks. Preprint at arXiv. https://doi.org/10. 48550/arXiv.1609.02907.

176. Scarselli, F., Gori, M., Tsoi, A.C., Hagenbuchner, M., and Monfardini, G. (2009). The Graph Neural Network Model. IEEE Trans. Neural Netw. 20, 61–80. https://doi.org/10.1109/TNN.2008.2005605.

177. Velickovi� c,� P., Cucurull, G., Casanova, A., Romero, A., Lio\` , P., and Bengio, Y. (2018). Graph Attention Networks. Preprint at arXiv. https://doi. org/10.48550/arXiv.1710.10903.

178. Caruana, R. (1997). Multitask learning. Mach. Learn. 28, 41–75. https:// doi.org/10.1023/A:1007379606734.

179. Ruder, S. (2017). An Overview of Multi-task Learning in Deep Neural Networks. Preprint at arXiv. https://doi.org/10.48550/arXiv.1706.05098.

180. Song, L., Segal, E., and Xing, E. (2024). Toward Ai-Driven Digital Organism: Multiscale Foundation Models for Predicting, Simulating and Programming Biology at All Levels. Preprint at arXiv. https://doi.org/10. 48550/arXiv.2412.06993.

181. Xiang, J., Wang, X., Zhang, X., Xi, Y., Eweje, F., Chen, Y., Li, Y., Bergstrom, C., Gopaulchan, M., Kim, T., et al. (2025). A vision–language foundation model for precision oncology. Nature 638, 769–778. https://doi. org/10.1038/s41586-024-08378-w.

182. Litinetskaya, A., Shulman, M., Hediyeh-Zadeh, S., Moinfar, A.A., Curion, F., Szałata, A., Omidi, A., Lotfollahi, M., and Theis, F.J. (2024). Multimodal weakly supervised learning to identify disease-specific changes in single-cell atlases. Preprint at bioRxiv. https://doi.org/10.1101/2024.07. 29.605625.

183. Kalfon, J., Cantini, L., and Peyre, G. (2025). Towards foundation models that learn across biological scales. Preprint at bioRxiv. https://doi.org/10. 1101/2025.05.16.653447.

184. Stringer, C., Wang, T., Michaelos, M., and Pachitariu, M. (2021). Cellpose: a generalist algorithm for cellular segmentation. Nat. Methods 18, 100–106. https://doi.org/10.1038/s41592-020-01018-x.

185. Van Rijthoven, M., Balkenhol, M., Silin‚ a, K., Van Der Laak, J., and Ciompi, F. (2021). Hooknet: Multi-resolution convolutional neural networks for semantic segmentation in histopathology whole-slide images. Med. Image Anal. 68, 101890. https://doi.org/10.1016/j.media.2020.101890.

186. Wang, F., and Wei, L. (2022). Multi-scale deep learning for the imbalanced multi-label protein subcellular localization prediction based on immunohistochemistry images. Bioinformatics 38, 2602–2611. https:/ doi.org/10.1093/bioinformatics/btac123.

187. Marks, M., Israel, U., Dilip, R., Li, Q., Yu, C., Laubscher, E., Iqbal, A., Pradhan, E., Ates, A., Abt, M., et al. (2025). CellSAM: a foundation model for cell segmentation. Nat. Methods 22, 2585–2593. https://doi.org/10. 1038/s41592-025-02879-w.

188. Nadig, A., Thoutam, A., Hughes, M., Gupta, A., Navia, A.W., Fusi, N., Raghavan, S., Winter, P.S., Amini, A.P., and Crawford, L. (2025). Consequences of training data composition for deep learning models in single-cell biology. Preprint at bioRxiv. https://doi.org/10.1101/2025.02. 19.639127.

189. Fan, D., Tong, S., Zhu, J., Sinha, K., Liu, Z., Chen, X., Rabbat, M., Ballas, N., LeCun, Y., Bar, A., et al. (2025). Scaling Language-Free Visual Representation Learning. Preprint at arXiv. https://doi.org/10.48550/arXiv. 2504.01017.

190. Moffitt, J.R., Lundberg, E., and Heyn, H. (2022). The emerging landscape of spatial profiling technologies. Nat. Rev. Genet. 23, 741–759. https:// doi.org/10.1038/s41576-022-00515-3.

191. Luecken, M.D., Gigante, S., Burkhardt, D.B., Cannoodt, R., Strobl, D.C., Markov, N.S., Zappia, L., Palla, G., Lewis, W., Dimitrov, D., et al. (2025). Defining and benchmarking open problems in single-cell analysis. Nat. Biotechnol. 43, 1035–1040. https://doi.org/10.1038/s41587-025- 02694-w.

192. Lance, C., Luecken, M.D., Burkhardt, D.B., Cannoodt, R., Rautenstrauch, P., Laddach, A., Ubingazhibov, A., Cao, Z.-J., Deng, K., Khan, S., et al. (2022). Multimodal single cell data integration challenge: Results and lessons learned. In In Proceedings of the NeurIPS 2021 Competitions and Demonstrations Track vol. 176 of Proceedings of Machine Learning Research, pp. 162–176. https://proceedings.mlr.press/ v176/lance22a.html.

193. Liu, W., Li, J., Tang, Y., Zhao, Y., Liu, C., Song, M., Ju, Z., Kumar, S.V., Lu, Y., and Akbani, R. (2025). DrBioRight 2.0: an LLM-powered bioinformatics chatbot for large-scale cancer functional proteomics analysis. Nat. Commun. 16, 2256.

194. Ghareeb, A.E., Chang, B., Mitchener, L., Yiu, A., Szostkiewicz, C.J., Laurent, J.M., Razzak, M.T., White, A.D., Hinks, M.M., and Rodriques, S.G.R. (2025). A multi-agent system for automating scientific discovery. Preprint at arXiv. https://doi.org/10.48550/arXiv.2505.13400.

195. Huang, K., Zhang, S., Wang, H., Qu, Y., Lu, Y., Roohani, Y., Li, R., Qiu, L., Li, G., Zhang, J., et al. (2025). Biomni: A General-Purpose Biomedical AI Agent. Preprint at bioRxiv. https://doi.org/10.1101/2025.05.30.656746.

196. Zhang, Z., Qiu, Z., Wu, Y., Li, S., Wang, D., Zhou, Z., An, D., Chen, Y., Li, Y., Wang, Y., et al. (2025). OriGene: A Self-Evolving Virtual Disease Biologist Automating Therapeutic Target Discovery. Preprint at bioRxiv. https://doi.org/10.1101/2025.06.03.657658.

197. Gao, S., Zhu, R., Kong, Z., Noori, A., Su, X., Ginder, C., Tsiligkaridis, T., and Zitnik, M. (2025). TxAgent: An AI Agent for Therapeutic Reasoning Across a Universe of Tools. Preprint at arXiv. https://doi.org/10.48550/ arXiv.2503.10970.

198. Ferber, D., El Nahhas, O.S.M., Wo¨ lflein, G., Wiest, I.C., Clusmann, J., Leßmann, M.-E., Foersch, S., Lammert, J., Tschochohei, M., Ja¨ ger, D., et al. (2025). Development and validation of an autonomous artificial intelligence agent for clinical decision-making in oncology. Nat. Cancer 6, 1–13. https://doi.org/10.1038/s43018-025-00991-6.