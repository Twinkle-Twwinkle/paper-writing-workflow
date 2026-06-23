# How to Build the Virtual Cell with Artificial Intelligence: Priorities and Opportunities

## Abstract

The cell is arguably the most fundamental unit of life and is central to understanding biology. Accurate modeling of cells is important for this understanding as well as for determining the root causes of disease. Recent advances in artificial intelligence (AI), combined with the ability to generate large-scale experimental data, present novel opportunities to model cells. Here we propose a vision of leveraging advances in AI to construct virtual cells, high-fidelity simulations of cells and cellular systems under diferent conditions that are directly learned from biological data across measurements and scales. We discuss desired capabilities of such AI Virtual Cells, including generating universal representations of biological entities across scales, and facilitating interpretable in silico experiments to predict and understand their behavior using Virtual Instruments. We further address the challenges, opportunities and requirements to realize this vision including data needs, evaluation strategies, and community standards and engagement to ensure biological accuracy and broad utility. We envision a future where AI Virtual Cells help identify new drug targets, predict cellular responses to perturbations, as well as scale hypothesis exploration. With open science collaborations across the biomedical ecosystem that includes academia, philanthropy, and the biopharma and AI industries, a comprehensive predictive understanding of cell mechanisms and interactions has come into reach.

## Main

The cell, the fundamental unit of life, is a wondrously intricate entity with properties and behaviors that challenge the limits of physical and computational modeling. Every cell is a dynamic and adaptive system in which complex behavior emerges from a myriad of molecular interactions. Some aspects are remarkably robust to perturbations, such as the elimination of genes or their replacement with homologs from diferent species. Other aspects are sensitive to even seemingly minor disruptions, such as a point mutation or an external factor that tip cells into dysfunction and disease.

To understand a cell’s function, scientists have attempted to construct virtual cell models to simulate, predict and steer cell behavior <sup>1,2,3,4,5,6</sup>. Building on this vision, we use the term virtual cell to define a computational model that simulates the biological functions and interactions of a cell. Existing cell models are often rule-based and combine assumptions about the underlying biological mechanisms with parameters fit from observational data. They generally rely on explicitlydefined mathematical or computational approaches, <sup>Molecular</sup> <sup>scale</sup> <sup>Cellul</sup>such as diferential equations <sup>7,8,9,10,11</sup> <sup>ar</sup> <sup>scale</sup> , stochastic sim-<sup>replication</sup><sub>e</sub>l<sup>l</sup> ulations <sup>12,13,14</sup> or agent-based models <sup>15,16</sup>. They vary <sub>a</sub><sup>l</sup> in complexity and cover diferent defined aspects of s<sup>i</sup>cell biology such as transcription <sup>17</sup> and translation <sup>18</sup>, <sup>RNA</sup>P<sup>h</sup>cytoskeletal driven cell behavior<sup>19,20</sup>, biochemical net-<sup>translation cell</sup>molecular <sup>ligand</sup>works <sup>21</sup> or metabolic flux <sup>22,23</sup>. The first whole-cell model was developed in 2012, representing all 482 genes and molecular functions known for an organism; the bac-<sup>b.</sup> <sup>Building</sup> <sup>the</sup> <sup>AI</sup> <sup>Virtual</sup> <sup>Cell</sup> <sup>through</sup> <sup>Universal</sup> <sup>Represent</sup>teria Mycobacterium genitalium <sup>9</sup>. Since this pioneering <sup>Molecular</sup> <sup>scale</sup> <sup>Cellular</sup> <sup>scale</sup> work, genome-wide models have been developed to repnucleus<sub>A</sub> DNA <sup>e.g.,</sup> <sup>phenotypic</sup> <sup>readouts</sup> resent other bacterial organisms, including Escherichia <sup>C</sup> <sup>T</sup> coli <sup>23,9,24,25,26</sup>.

<sub>A</sub> <sub>RNA</sub> <sup>Representatio</sup>RepresentationDespite their widespread use in modeling biologi-U <sub>r</sub>tcal systems, approaches to date fall short of capturing <sup>V</sup>many aspects of the operations of both bacteria and more complex systems, such as human cells: (1) Multi-<sup>EGAYGMVCSAY</sup>DNVNKVRVAIK cellscale modeling: Cells operate on multiple scales across both time and space, from atomic to molecular to cellucell division<sup>tissue</sup> lar and histological, with functional properties emerging <sup>responses</sup> <sup>to</sup> through nonlinear transformation from one scale to an-<sup>&</sup> <sup>intrinsic</sup> other. (2) Diverse processes with massive numbers of interacting components: Cellular function encompasses numerous interacting processes, such as gene regula-<sup>interaction cell</sup> diferentiationtion, metabolic pathways and signal transduction. Each process involves a multitude of biomolecular species, <sup>ions</sup> <sup>… d.</sup> <sup>…</sup> <sup>and</sup> <sup>Virtual</sup> <sup>Instruments.</sup>in diverse and dynamic configurations and states. (3) <sup>Multicellular</sup> <sup>scale e.g.,</sup> <sup>for</sup> <sup>the</sup> <sup>cellular</sup> <sup>scale</sup>Nonlinear dynamics: Most cellular processes are highly nonlinear, such that small changes in inputs can lead to <sup>Virtual</sup> <sup>Instruments</sup>complex changes in outputs. Thus, despite progress in genetic perturbationcell UR modeling specific cellular processes, these factors collectively pose a substantial roadblock to the construction of a virtual cell.

<sup>cell</sup> <sup>UR</sup> <sup>e.g.,</sup> <sup>changes</sup> <sup>in</sup> <sup>Representation</sup>Two exciting revolutions in science and technology— in AI and in ’omics—now enable the construction of cell models learned directly from data. These parallel revolutions provide an unprecedented opportunity for an ambitious vision of an AI Virtual Cell (AIVC), a multi-scale, multi-modal, large neural network-based model that can represent and simulate the behavior of molecules, cells and tissues across diverse states (Fig. 1).

Experimentally, the exponential increase in the throughput of measurement technologies has led to the collection of large and growing reference datasets within and across diferent cell and tissue systems <sup>27,28,29,30</sup>, with data doubling every six months for the past several years <sup>31</sup>, along with the ability to couple these measurements with systematic perturbations <sup>32,33,34,35</sup>.

Computationally, concurrent advances in AI have enhanced our ability to learn patterns and processes directly from data without needing explicit rules or human annotation<sup>36,37,38</sup>. Such modeling paradigms have been used successfully in the biomolecular realm, for example to predict three-dimensional molecular structure from sequence <sup>39,40,41,42</sup> and interactions between diferent molecular components <sup>43,44,45,46,47,48</sup>. Recent modeling methodologies in AI provide representation and inference tools that satisfy the trifecta of being predictive, generative and queryable, which are key utilities for biological research and understanding. By building on these properties, we argue that we now have the methods to develop a fully data-driven neural network-based representation of an AI Virtual Cell that can accelerate research in biomedicine by enabling fast-paced in silico studies, as well as powerful bridges between computational methods and confirmatory wet-lab experimentation (Fig. 1).

The creation of an AIVC will enable a new era of high-fidelity simulation in biology, in which cancer biologists model how specific mutations transition cells from healthy to malignant; developmental biologists forecast how developmental lineages evolve in response to perturbation in specific progenitor cells; microbiologists predict the efects of viral infection on not just the infected cell but also its host organism. AIVCs will empower experimentalists and theorists alike, by transforming the means by which hypotheses are generated and prioritized, and allowing biologists to span a dramatically expanded scope, better fitting the enormous scales of biology. Although the cellular models may not always directly identify mechanistic relationships, they can be viewed as tools for efectively narrowing the search space for mechanistic hypotheses, thereby accelerating the discovery of underlying factors behind cellular function.

This Perspective article is based on extensive community discussions, including a workshop hosted by the Chan Zuckerberg Initiative, and aims to ignite the formation of a collaborative research agenda for a largescale, long-term initiative with a roadmap for developing, implementing, and deploying AI Virtual Cells. We describe a vision catalyzed by emerging advances in

AI in cell biology and their application to constructing virtual representations of cells. We lay out priorities and opportunities across data generation, AI models, benchmarking, interpretation and ensuring biological veracity and safety (Box 1). By encouraging interdisciplinary collaborations in open science—spanning academia, philanthropy, and the biopharma and AI industries—we posit that a comprehensive understanding of cellular mechanisms is within reach. AI Virtual Cells have the potential to revolutionize the scientific process, lead to the understanding of novel biological principles and augment human intelligence to underpin future breakthroughs in programmable biology, drug discovery and personalized medicine (Box 2).

## AI Virtual Cells

Our view of an AI Virtual Cell is a learned simulator of cells and cellular systems under varying conditions and changing contexts, such as diferentiation states, perturbations, disease states, stochastic fluctuations, and environmental conditions (Fig. 1). In this context, a virtual cell should integrate broad knowledge across cell biology. Virtual cells must work across biological scales, over time, and across data modalities, and should help reveal the programming language of cellular systems and provide an interface to use it for engineering purposes.

In particular, an AI Virtual Cell needs to have capabilities that allows researchers to: (1) Create a universal representation of biological states across species, modalities, datasets and contexts, including cell types, developmental stages and external conditions; (2) Predict cellular function, behavior and dynamics, as well as uncovering the underlying mechanisms; (3) Perform in silico experiments to generate and test new scientific hypotheses and guide data collection to eficiently expand the virtual cell’s abilities.

Next, we elaborate on these key capabilities and discuss approaches for how to achieve them.

## Universal representations

An AIVC would map biological data to universal representational spaces (Fig. 1a), facilitating insights into shared states and serving as a comprehensive reference. These universal representations should integrate across three physical scales: molecular, cellular and multicellular, and accommodate contributions from any relevant modality and context (Fig. 1a). This integration will allow researchers to complement new data with existing information within the AIVC, leveraging its extensive biological knowledge to bridge gaps between diferent data. Such a comparison with prior data would provide a comprehensive context for every analysis.

Importantly, the multilevel representation should generalize to new states not present within the data used to train the AIVC. Such an emergent capability would unlock discoveries about biological states that have not been directly observed, or might not even occur in nature. For instance, the AIVC’s exposure to similar instances during training, like inflammatory states in macrophages, might enable it to predict previously unknown inflammatory states in microglia. Additionally, the AIVC should be able to predict novel states resulting from interventions (or, equivalently, interventions needed to achieve a novel specified state) ofering a range of downstream applications in cell engineering and synthetic biology.

## Predicting cell behavior and understanding mechanisms

A defining function of an AIVC will be its ability to model cellular responses and dynamics. By training on a wide range of snapshots, time-resolved, non-interventional and interventional datasets collected across contexts and scales, the AIVC can develop an understanding of the molecular, cellular, and tissue dynamics that occur under natural or engineered signals. These signals include external and internal stresses or other factors like chemical (e.g., small molecules) or genetic (engineered or natural) perturbations and their combinations. An AIVC should be able to predict responses to perturbations that have not been previously tested in the lab, while also accounting for the specific features of the cellular context within which the perturbation is being tested.

The AIVC should also have the capability to simulate the temporal evolution of alterations in cell states in response to both intrinsic or extrinsic factors, along with the resulting multicellular spatial arrangements. By modeling the transient nature of the overall cell state and the continuous flux in cellular conditions, the AIVC could uncover previously unstudied trajectories in diverse dynamic processes like development, maintenance of homeostasis, pathogenesis and disease progression.

Another critical challenge is understanding the molecular mechanisms underpinning observed phenotypes and trajectories. The AIVC could propose potential causal factors behind phenotypes by simulating the efects of diferent interventions. Through its multiscale design, the AIVC should be able to extrapolate the basis of cellular function across scales, and link intracellular processes to phenotypes at the cell and tissue level. Thus, the AIVC opens new avenues for investigating mechanisms linked to diverse phenotypes and behaviors.

Although uncovering a phenotype’s causal factors may not always be feasible through computation alone, the AIVC has the potential to reduce the space of possible hypotheses. Through simulating the efects of diferent interventions, the AIVC could propose potential causal factors behind phenotypes with corresponding degrees of uncertainty, allowing scientists to validate claims experimentally.

## In silico experimentation and guiding data generation

For real world utility, a defining function of an AIVC will be its ability to guide data generation and experiment design. An AIVC should be queryable with computational twins of today’s laboratory experiments, here called Virtual Instuments. Virtual experiments could, for example, simulate experiments in a cell type that is challenging to cultivate in vitro, or simulate expensive readouts from low-cost measurements, such as single cell transcriptomes from label free imaging <sup>49</sup>. Virtual experiments could also be used to screen a vast number of possible perturbagens, at a scale that would be impossible in the lab. Such capabilities are invaluable when considering the exponentially larger search space of combinatorial perturbations involving more than one perturbagen <sup>50,51,52,53,54</sup>

AIVCs will usher in a new paradigm of how computational systems are probed during the design of new biological experiments. In this framework, an AIVC would not only design experiments to validate specific scientific hypotheses, but also to enhance its own capabilities. Equipped with the ability to assign confidence values to its predictions, an AIVC could enable interactive querying to guide experimentalists to the most eficient path for generating additional data for finetuned improvement in low-confidence areas. Extended to an active and iterative lab-in-the-loop process, we envision eficient and focused expansion of the AIVC’s performance. Ultimately, the AIVC might even be able to identify key gaps in its own understanding of biology and propose the most eficient paths to bridge them <sup>55,56,57,58</sup>.

## Building the AIVC

We envision an AI Virtual Cell as a comprehensive AI framework composed of several interconnected foundation models that represent dynamic biological systems at increasingly complex levels of organization—from molecules to cells, tissues, and beyond. Our approach has two main components: (1) a universal multi-modal multi-scale biological state representation and (2) a set of virtual instruments, which are neural networks that manipulate or decode these representations. While there may be other approaches to building an AIVC, we believe this approach would provide a scafold that can be scaled in a collaborative and open way.

We use the term Universal Representation (UR) to refer to an embedding produced by a multi-modal AIVC foundation model. An embedding is a learned numerical representation of data in a continuous vector space. The AIVC transforms high dimensional multiscale multi-modal biological data into embeddings that retain meaningful relationships and patterns.

The AIVC can capture cell biology at three distinct physical scales by representing (1) molecules and their structures found within individual cells, (2) individual cells, as spatial collections of those interacting molecules and structures, and (3) how individual cells interact with one another and the non-cellular environment in a tissue. Each of these scales is represented by a distinct UR, building on abstractions generated by the previous layer, thus linking the diferent scales.

In the context of UR, Virtual Instruments (VIs) are neural networks that take URs as input and produce a desired output. We describe two types of VIs: Decoder Virtual Instruments (or Decoders) that take a UR as an input and produce human-understandable output, for example, a cell type label or a synthetic microscope image; and, Manipulator Virtual Instruments (or Manipulators) which take a UR as an input and produce another UR as an output, for example, that of an altered cell state after perturbation. Since these instruments will operate over the same representations, they can be shared and reused across diferent use cases, experiments and datasets. Thus, we envision that any scientist will be able to build a Virtual Instrument on top of a Universal Representation and share it with the community. The building of VIs that closely resemble real instruments, like a microscope, has the potential to seed the development of instrument specific lab-in-the-loop systems.

## Building universal representation across physical scales

The AIVC would be a multi-scale foundation model that learns distinct representations of biological entities at each physical scale (Fig. 2c). These representations can be aggregated together and transformed to produce representations at the next higher physical scale. This recurring architectural motif can be applied from the level of individual molecules to the scale of entire tissues and organs granting the model consistency across biological scales (Fig. 2a). Each representation applies universally to that specific class of biological entities. This abstraction allows the virtual cell to seamlessly evolve and incorporate new data, from new modalities or from out-of-distribution sources, since it can all integrate within this general framework.

In the following, we discuss design principles and data that could be used to construct each physical scale of the AIVC bottom-up. While many existing machine learning architectures could be applied directly to the task of learning functional representations of cellular components (Box 3), we additionally suggest the incorporation of biological inductive biases into the design of these representations, and further modeling innovations should drive the refinement and success of these models.

Molecular scale. The first layer of the virtual cell represents individual molecular species (Fig. 2a,c). While there are many diferent classes of molecules present in a cell, a starting point for the AIVC will be to model the three types of molecules of the central dogma: DNA, RNA and proteins. These can all be represented as sequences of characters; nucleotides or amino acids <sup>59,60,61,62,63,64,65,66,67</sup>. Such sequence data are particularly well-suited for AI methods originally developed for natural language processing, like large language models (LLMs) (Box 3). Given the high-throughput measurement capabilities for DNA, RNA and protein sequences, there are substantial and growing amounts of training data available. This abundance of data, combined with simple objective functions (such as predicting masked letters in a sequence), provides the key ingredients for efectively training models to generate an initial molecular UR. Furthermore, a biological language model could be trained on all three modalities simultaneously, thus maximizing interoperability and training corpus size. Despite its inherent compatibility with transformers, specific considerations around masking and attention mechanisms must be addressed when applying these models to biological sequence data as opposed to natural language.

While language modeling approaches have been extensively studied for these core molecules and have proven successful for some of their chemical modifications <sup>68</sup> and various other molecules such as glycans, lipids and metabolites <sup>69,70</sup>, they may struggle with other molecular constituents of the cell. Such modeling dificulties might be exacerbated for data that is dificult to fit into a sequence, or very small molecules. Given that the primary building blocks of these entities are atoms, a neural network trained to model molecules at the atomic level<sup>39,71</sup> could be a more general choice for this layer. However, models with atomic resolution introduce a substantial computational burden and might be constrained by limited availability of training data.

Cellular scale. The next level of abstraction models individual cell states (Fig. 2a,c). As cellular function is underpinned by the molecular interactions and signaling networks formed in a cell, a cellular UR can be built using representations of molecular and other (e.g., imaging) features describing the organization and abundance of molecular components. The key step here would be to integrate learned representations of molecules with their quantities, and appropriately abstracted locations and timestamps, to create a unified representation of the cell <sup>72,73,74</sup>.

Data for the cellular UR consist of measurements mapped to a single cell level such as measurements of the transcriptome (scRNA-seq), chromatin accessibility (scATAC-seq), chromatin modification transcription factor binding, and proteome<sup>75</sup>. Imaging technologies measure cell morphology at subcellular resolution, often together with molecular information <sup>76,77,78</sup>. For example, fluorescence confocal microscopy can help resolve the subcellular location of the human proteome <sup>79</sup>. Live-cell imaging<sup>80</sup> enables the study of proteins in living cells using time-lapse microscopy. Cryo-electron microscopy determines biomolecular structures at nearatomic resolution <sup>81,82</sup>. Super-resolution microscopy ofers deeper insights into molecular processes through single-molecule imaging in living systems <sup>83,84,85</sup>. Complementing imaging approaches, mass spectrometry and proximity-dependent labeling can unveil proteinprotein associations and provide deeper insights into cell structure and signaling network rewiring <sup>86,87</sup>

From the model architecture perspective, vision transformers<sup>88</sup> or models leveraging convolutional neural networks (CNNs) <sup>89,90</sup> are widely applicable to biological images to model across multiple imaging channels capturing diferent biological features <sup>91,92,93,94</sup>, while being robust to distribution shift and batch variability <sup>95</sup>. Autoencoders and transformers have been successfully applied for learning representations for sequence-based data <sup>96,97,73,98,99</sup>. Using AI algorithms to integrate different data modalities collected with sequencing and imaging technologies creates a multi-view model of the cell that can be both dynamic and predictive <sup>100,101,102</sup>.

As the AIVC model grows in complexity, it is crucial to also model cellular organelles and membraneless compartments <sup>103</sup> as units that play specific roles within the cell. Robustly capturing the functions of these units is vital to ensure accurate predictions, mechanistic interpretability and model generalizability.

Given their prevalence, the cellular UR will initially rely on transcriptomics measurements, while imaging modalities will be key for continued modeling of cellular spatial organization and dynamics.

Multicellular scale. At the third layer of abstraction, the AIVC models the organization of cells into a multicellular UR (Fig. 2a,c). This layer allows for the exploration of how cell-cell interactions, largely governed by spatial proximity, combine into tissues, organs and, ultimately, whole organisms. Multicellular interactions can be analyzed after tissue dissociation (such as in scRNA-seq) <sup>104</sup> or in situ in a 2D section or 3D volume, where the tissue structure is preserved. Building the AIVC will require integration across available modalities that provide spatial insights, i.e., both spatial molecular profiling as well as non-molecular tissue imaging data.

There are multiple methods to profile the spatial location of RNA <sup>105</sup>, and proteins <sup>106</sup> in cells, along with various imaging methods for select molecular species (e.g., immunohistochemistry), or with stains for tissue strucutre alone (e.g., haematoxylin and eosin (H&E)). Spatial molecular biology is currently a very active area of research and method development. While publicly available data are still limited, we foresee a rapid development in this domain providing multi-omic 2D and

3D datasets. A more generalized data generation efort together with open frameworks for spatial data <sup>107</sup> could greatly accelerate modeling at the multicellular scale.

The relative organization of cells within a 2D tissue section and 3D tissue volume can be represented using a graph or point cloud. The multicellular UR can be derived from such data using graph-learning techniques such as graph neural networks (GNNs) <sup>108</sup> and equivariant neural networks (ENNs)<sup>109</sup>. For image-based data, convolutional neural networks or vision transformers can be applied (Box 3).

## Predicting cell behavior and understanding mechanism

Virtual instruments are the “tools” that operate on UR embeddings and perform various functions and tasks. By altering universal representations of molecules, cells and tissues, Manipulators can abstract complex dynamic processes (Fig. 2b) more simply as transitions between (distributions of) their representations (Fig. 2d). Similarly, Decoders can take an embedding of biological entities and predict one or more concrete properties, for example, physical structure, cell type/state, fitness, expression or drug response.

The design of a wide array of Manipulators provides us with an unprecedented set of tools for modeling cell behavior and dynamics: Generative AI approaches such as difusion models <sup>110</sup> or autoregressive transformers <sup>111</sup>, i.e., model architectures that capture heterogeneity and parameterize continuous time dynamics, can predict a future state or evolution of a cell or molecular state <sup>71,112</sup> (Box 3). Using integrated data from time-lapse imaging <sup>80</sup>, gene expression profiles <sup>104,113,114</sup>, and other modalities, Manipulators can allow inferring the phenotypic progression from stem cell to diferentiated cell, while capturing the influence of both genetic factors and environmental conditions —through learned interpolations and extrapolations between multi-scale URs of diferent cell states. Similarly, they allow predicting the efect of treatments on patients, given a virtual representation of a patient’s molecular profile.

Furthermore, variations in cellular URs can be linked to corresponding changes in molecular states or their spatial localization, influenced by downstream factors like genetic variants or functional changes in proteins that are represented in a lower scale of the AIVC. Leveraging the ability of Manipulators to model temporallyresolved molecular and cellular events, Decoders of the AIVC could potentially identify cellular components, molecular pathways, and their interactions that contribute to each prediction and process. As such, the multi-scale design of the AIVC may unveil mechanistic hypotheses of such processes.

## In silico experimentation and guiding data generation

Manipulator Virtual Instruments operating in the UR space could further enable the exploration of a broad range of hypotheses through in silico experiments that virtually perturb a cell model. This might be achieved by predicting changes in the URs following a perturbation prompt (Fig. 2d) <sup>50,53,54,52</sup>.

The design of Manipulators that predict transitions in the UR upon an in silico input can build on conditional generative models: Deep learning architectures like conditional deep generative models<sup>37</sup> allow generating the desired UR based on the property or context of interest (Box 3). Here, high-throughput perturbation screens —based on RNA-seq <sup>104,32,115,33</sup>, optical pooled screens (OPS) <sup>34,49,116,117</sup>, or other technologies— ofer a rich resource through which the AIVC can be trained to predict these efects. By conditioning on specific perturbations—such as environmental changes, genetic mutations, or chemical treatments—the generative model might produce a new UR reflecting the predicted cellular response. This conditioning could be achieved through learned or pre-computed embeddings of the afected molecular targets. Chemical compounds, small molecules and metabolites could be embedded based on their chemical properties. Additionally, large language models trained on comprehensive scientific literature and biological databases, such as gene ontology or drug banks, could further provide a rich contextual background used for conditioning the generative model, e.g., through considering wide range of interactions and side efects.

Virtual Instruments can be designed so that predictions are accompanied by estimates of model uncertainty <sup>118,119</sup>. Under a Bayesian formulation of its predictive function, the predictions made for cell perturbation outcomes could include an uncertainty score, either implicitly via inference, deep kernels <sup>120,121</sup>, or through explicit estimation of the full posterior over model parameters <sup>122,123</sup>. Some practical approaches utilize model ensembles <sup>124</sup> or conformal predictions <sup>125</sup> By assigning specific confidence levels to its predictions, the AIVC can call methods for computing the expected value of additional data or approximations referred to in machine learning as active learning, to guide experimental data collection <sup>55,56</sup> for expanding its UR. Alternatively, methods for computing the expected value of information could be used to guide data generation with the goal of optimizing a desired biological property <sup>119</sup>. Lastly, through its ability to conduct in silico experiments and suggest additional informative experiments, the AIVC could become an integrative part of lab-in-theloop schemes. This allows not only for a seamless experimental validation of its predictions, but also a sequence of experiments, predictions and generations of hypotheses that gradually improve our systematic understanding of molecular circuits that drive biological functions.

## Data needs and requirements

A key consideration for the AIVC is which datasets and modalities must be collected to enable its efective construction. Unlike traditional experimental design, where data are generated to test specific scientific hypotheses, data collection for training the AIVC should be focused on ensuring the broad applicability and generalizability expected of the AIVC. To meet these ambitions, data would ideally span diferent domains and modalities, capture the heterogeneity and diversity of biological variability, and enable models to distinguish between technical (measurement) noise, stochastic biological variation and physiological diferences.

Data generation will require simultaneous exploration of temporal and physical scales, while allowing for system perturbations. Here, classical imaging technologies <sup>126,127,128</sup>, including live-cell, and newer structural imaging technologies like cryo-electron tomography and soft X-Ray tomography <sup>129,81,130</sup>, as well as novel spatial omics technologies <sup>131,132,133</sup>, ofer opportunities to model biomolecules and functions across scales. Furthermore, biological processes span a vast range of timescales, from the fastest reactions happening in picoseconds, to a cell division happening in a day, tumor development occurring over years, and neurodegeneration over decades. The recent construction of universal cell atlases <sup>134,128</sup> may serve as a powerful resource for modeling cellular behavior over longer time scales, such as tissue formation. New approaches will be needed to build comparable data sets which capture the behavior of cells on shorter times scales, e.g., through methods such as live-cell imaging. Besides molecular measurements, an important aspect of data collection will lie in the measurement of biophysical and biochemical cellular properties to provide boundaries of physical and chemical realism to the AIVC.

Another important driver for the development of AI Virtual Cells will be multi-modal datasets. For example, datasets which bridge molecular and spatial scales, such as single cell transcriptomics data combined with histology to understand how cells interact and what molecular signatures underpin the formation of specialized spatial niches<sup>135</sup>. Further technological development is needed to collect multi-modal data that better captures the relationship between molecular signatures, cell behavior, cellular regulation and organization.

While a core interest of virtual cell modeling will focus on human datasets for the purpose of understanding disease and aiding the development of novel therapeutics, human datasets are limited in our ability to perform controlled experimentation and perturbations in vivo. Here, the field of 3D tissue biology, including culture systems such as organoids, is emerging as a tool to study the complexities of tissue architecture and function <sup>136</sup> in a 3D environment while allowing perturbations of the system. Another critical avenue to surpass this limitation will be to perform diverse, organism-wide profiles of species spanning evolutionary history, across perturbations and under various conditions <sup>137,138,139,140,141</sup>.

Finally, a key aspect of biological data generation will be the exploration of combinatorial spaces: biological spaces are commonly high dimensional, and enumerating their variants is intractable in general, e.g., when considering all possible variants of a genome. Even for combinations of a small number of entities, exemplified in the case of enumerating pairs or sets of perturbations <sup>58,115</sup>, experimental design becomes exceedingly challenging. As combinatorial possibilities quickly expand well beyond what is practical experimentally, or even computationally, new methods for their exploration must be developed.

How much data is needed to build the AI Virtual Cell? The scale of raw biological data is undeniable, but so is the sheer nominal size of even one human cell system, making first principle estimates challenging.

For instance, the Short Read Archive of biological sequence data holds over 14 petabytes of information <sup>142</sup> which is more than one thousand times larger than the dataset used to train ChatGPT <sup>143</sup>. Large parts of this data may be redundant, or have diminishing returns if used for training, and the scaling laws for models’ performances must be investigated thoroughly.

In addition to data size, data diversity is critical to ensure model quality<sup>144</sup>. Data from humans and model organisms like mice and E. coli are unequally represented in sequence and literature databases, which when used for training, encode strong species biases <sup>144</sup>. Other biases, for example towards specific diseases or human ancestral populations could also reduce the impact of AIVC models <sup>145</sup>. As virtual cell eforts mature, the dialogue between the scientists who develop models, those who generate experimental data and funding organizations must be further intensified.

## Model evaluation

A more important question for the development of AI Virtual Cells may not be “How to build them?”, but rather “How to build trust in their competence and fidelity?” To this end, a comprehensive and adaptable benchmarking framework will be needed. Although various frameworks already exist for tackling specific biological questions (for example, protein structure prediction models<sup>112</sup> were developed in the context of the CASP evaluation framework), the AIVC will need to demonstrate generalizability across numerous biological contexts and downstream tasks. It must account for dynamic distributions that evolve due to environmental changes, infections, genetic variants and other such factors causing distribution shifts <sup>146</sup>.

The evaluation of AI Virtual Cells should prioritize both generalizability as well as discovering new biology.

Generalizability measures how well the model performs in unseen contexts such as novel cell types and genetic backgrounds. It can be evaluated through a cross-modal reconstruction task, such as predicting gene expression given the morphology of a previously unseen cell or the next image in a sequence of microscopy images of cell state. Assessing generalizability builds confidence in the AIVC’s ability to capture core biological processes and understand how they vary across diferent contexts. Establishing such cross-modal benchmarks to link scales and modalities in cell biology is of imminent priority to the research community, as these tasks are both biologically useful and well-defined.

Ultimately, AIVC models should be judged on their ability to unlock new ways of understanding biology. Such an evaluation will ensure that model development is aligned with biological relevance. The most useful initial accomplishments will likely be to generate valuable testable hypotheses. For this purpose, validation datasets that are related to phenotypes that are experimentally verifiable may be suitable, such as growth rate of cells, molecular profiles, disrupted protein-protein interactions, or transcription factor binding.

As the capabilities of AI Virtual Cells improve, we must consider whether statistical measures of performance are adequate, or if interpretability and biological causality would be core requirements.

## Interpretability and interaction

One of the hallmarks of scientific discovery in biology has been the creation of mechanistic models of a phenomenon under observation. When creating virtual cells, we may have to forgo our ability to build fully mechanistic models, in favor of learning interactions that will generalize from data and predict beyond the observations. However, it is still desirable to strive towards increased interpretability.

Every AIVC prediction could be substantiated with the corresponding multi-scale interactions that determine resulting states, e.g., understanding how a cellular subsystem or protein complex is disrupted in a diseased tissue can aid development of therapeutic interventions <sup>147,148,149</sup>. The modular structure of the AIVC will enable researchers to pinpoint specific genes, proteins, or molecular processes involved in each predicted behavior. Patterns in the wiring of large models can also be leveraged to uncover combinatorial biological interactions, such as those between proteins, which can be projected to interpretable spaces without restricting the generality of the original model. While many capabilities of the AIVC rely on predictive tasks, generating mechanistic hypotheses could provide experimental routes to understand and explore the AIVC’s predictions further, and will be vital for the adoption and use of AI Virtual Cells.

Ultimately, it will be of key interest to build an interactive layer for the AIVC that enables researchers of varying expertise to grasp and utilize its predictions efectively. AI Agents, built using large language models, could serve as virtual research assistants, providing an intuitive interface for non-experts <sup>150,151,57</sup>. Leveraging their extensive knowledge of scientific literature, these language models can ofer deeper insights into the predictions made by the AIVC.

## An open collaborative approach

Creating an AIVC requires tremendous investment, diverse backgrounds and many iterations, and can only be advanced by a concerted open science efort. As a scientific community, we must strive to ensure that both the development and usage of Virtual Cells are accessible and responsive to the entire scientific community. These eforts would greatly benefit from open data resources and data standards, a collaborative platform for cell modeling, and especially open benchmark datasets and common validation strategies to ensure their biological fidelity and real-world utility. Such a collaborative program could greatly accelerate progress across individual eforts and unify scientific research at a global scale, connecting myriad smaller-scale eforts.

To achieve this, multiple key parameters need to be considered. First, we must ensure that AI Virtual Cells represent and benefit all of humanity, with open data that captures human ancestral and geographic diversity. Ensuring that such datasets reflect human diversity while safeguarding individuals’ privacy is a principal challenge. Second, as the size of AI Virtual Cell models increases, the cost of training, fine-tuning or using them as is will also grow. Investments in infrastructure and a platform for hosting these models will be critical to ensure accessibility and benefit to the broader scientific community. The platform should foster open and collaborative development of AI Virtual Cells, enabling active collaboration between biologists, clinicians and computer scientists. This platform should facilitate swift iterations between the lab and the modeling environment and ofer opportunities to quickly test and benchmark new models. Third, synergistic collaboration amongst stakeholders is needed across the biomedical ecosystem including philanthropy, academia, biopharma and the AI industry. Pre-competitive collaborations can greatly accelerate our collective progress towards creating AI Virtual Cells. Besides the synchronization with data generators and other modeling eforts, collaboration with regulatory authorities and bioethics experts are crucial for benchmarking and establishing new norms that will expedite the deployment of AI Virtual Cells, while complying with legal requirements and setting standards for ethical issues for responsible use of virtual cells.

This article is intended to serve as a primer for the formation of a collaborative research agenda and roadmap for a large-scale, long-term initiative for developing and implementing AI-powered Virtual Cells. If successful, such interactive AI Virtual Cell models, capable of simulating cellular biology, have the potential to fundamentally change how cell biology research is done. We foresee a future where AI Virtual Cell platforms function as open, interconnected hubs for collaborative development and broad deployment of cell models to researchers, but also as education hubs delivering training to researchers, as well as providing engagement activities for educators, patients and the public.

## Outlook and reasons for optimism

The genetics and genomics communities have created large reference datasets, such as the human genome project<sup>28</sup>, HapMap<sup>152</sup>, the Cancer Genome Atlas (TCGA) <sup>153</sup>, ENCODE<sup>154</sup>, the Genotype-Tissue Expression (GTEx) project<sup>155</sup>, the Human Protein Atlas (HPA) <sup>156,79</sup>, the Human Cell Atlas (HCA) <sup>29</sup> and a growing number of deeply phenotyped, population-scale biobank eforts <sup>157</sup>. Thanks to these projects, massive reference data are now available to train machine learning models. While these eforts will continue to grow, they also catalyze a new, parallel efort: creating a virtual simulation of cell biology, a new process for scientific inquiry.

The result, the AI Virtual Cell has the potential to revolutionize the scientific process, leading to fu ture breakthroughs in biomedical research, personalized medicine, drug discovery, cell engineering and programmable biology. Acting as a virtual laboratory, the AIVC could facilitate a seamless interface between data derived from in silico experimentation and results from physical laboratories. As such we expect the AI Virtual Cell to contribute to a more unified view of biological processes, fostering alignment among scientists on how emergent properties in biology arise.

By bridging the worlds of computer systems, modern generative AI and AI agents as well as biology, the AIVC could ultimately enable scientists to understand cells as information processing systems and build virtual depictions of life. As the AI Virtual Cell expands understanding of cellular and molecular systems, it will also increasingly allow us to program them and design novel synthetic ones. AI models have already been used to design new CRISPR enzymes<sup>67</sup>, functional proteins <sup>158</sup>, and even entire prokaryotic genomes <sup>65</sup> The rapid progress in the precision of cell and genome engineering tools will accelerate this shift and diferent instantiations of the AIVC will compete in their ability to engineer new, functional biology capabilities as much as in their ability to represent and simulate biology 159

Finally, we staunchly advocate the role for open science approaches, where the scientific community readily shares data, models, and benchmarks, where findings and insights are contextualized, and where a climate of perpetual improvement is fostered. We welcome and encourage all stakeholders across sectors and domains to engage in this endeavor. With a massive scientific undertaking and shared goals, open sharing of insights and the power of safe, ethical and reliable AI, we believe we are stepping into a new era of scientific exploration and understanding. The confluence of AI and biology, as encapsulated by AI Virtual Cells, signals signals a paradigm shift in biology and shines as a beacon of optimism for unraveling multiple mysteries of the cell.

## References

[1] Slepchenko, B. M., Schaf, J. C., Macara, I. & Loew, L. M. Quantitative cell biology with the Virtual Cell. Trends in Cell Biology 13 (2003).

[2] Johnson, G. T. et al. Building the next generation of virtual cells to understand cellular biology. Biophysical Journal 122 (2023).

[3] Marx, V. How to build a virtual embryo. Nature Methods 20 (2023).

[4] Goldberg, A. P. et al. Emerging whole-cell modeling principles and methods. Current Opinion in Biotechnology 51 (2018).

[5] Georgouli, K., Yeom, J.-S., Blake, R. C. & Navid, A. Multi-scale models of whole cells: progress and challenges. Frontiers in Cell and Developmental Biology 11 (2023).

[6] Marucci, L. et al. Computer-aided whole-cell design: Taking a holistic approach by integrating synthetic with systems biology. Frontiers in bioengineering and biotechnology 8, 942 (2020).

[7] Alon, U. An introduction to systems biology: design principles of biological circuits (Chapman and Hall/CRC, 2019).

[8] Laufenburger, D. A. & Linderman, J. J. Receptors: models for binding, traficking, and signaling (Oxford University Press, USA, 1996).

[9] Karr, J. R. et al. A whole-cell computational model predicts phenotype from genotype. Cell 150 (2012).

[10] Mangan, S. & Alon, U. Structure and function of the feedforward loop network motif. Proceedings of the National Academy of Sciences 100 (2003).

[11] Sachs, K., Perez, O., Pe’er, D., Laufenburger, D. A. & Nolan, G. P. Causal protein-signaling networks derived from multiparameter single-cell data. Science 308 (2005).

[12] Zopf, C., Quinn, K., Zeidman, J. & Maheshri, N. Cellcycle dependence of transcription dominates noise in gene expression. PLoS computational biology 9 (2013).

[13] Eling, N., Morgan, M. D. & Marioni, J. C. Challenges in measuring and understanding biological noise. Nature Reviews Genetics 20 (2019).

[14] To, T.-L. & Maheshri, N. Noise can induce bimodality in positive transcriptional feedback loops without bistability. Science 327 (2010).

[15] Hellweger, F. L., Clegg, R. J., Clark, J. R., Plugge, C. M. & Kreft, J.-U. Advancing microbial sciences by individualbased modelling. Nature Reviews Microbiology 14 (2016).

[16] Gorochowski, T. E. Agent-based modelling in synthetic biology. Essays in biochemistry 60 (2016).

[17] Woodcock, D. J. et al. A hierarchical model of transcriptional dynamics allows robust estimation of transcription rates in populations of single cells with variable gene copy number. Bioinformatics 29, 1519–1525 (2013).

[18] Thiele, I., Jamshidi, N., Fleming, R. & Palsson, B. Genomescale reconstruction of escherichia coli transcriptional and translational machinery: a knowledge base, its mathematical formulation, and its functional characterization. PLoS Comput. Biol 5, 1000312 (2009).

[19] Odell, G. M. & Foe, V. E. An agent-based model contrasts opposite efects of dynamic and stable microtubules on cleavage furrow positioning. The Journal of Cell Biology 183, 471–483 (2008).

[20] Popov, K., Komianos, J. & Papoian, G. A. MEDYAN: mechanochemical simulations of contraction and polarity alignment in actomyosin networks. PLoS Computational Biology 12, e1004877 (2016).

[21] Burke, P. E. P., Campos, C. B. d. L., Costa, L. d. F. & Quiles, M. G. A biochemical network modeling of a whole-cell. Scientific Reports 10, 13303 (2020).

[22] Li, G., Liu, L., Du, W. & Cao, H. Local flux coordination and global gene expression regulation in metabolic modeling. Nature Communications 14, 5700 (2023).

[23] Fang, X., Lloyd, C. J. & Palsson, B. O. Reconstructing organisms in silico: Genome-scale models and their emerging applications. Nature Reviews Microbiology 18, 731–743 (2020).

[24] Stevens, J. A. et al. Molecular dynamics simulation of an entire cell. Frontiers in hemistry 11, 1106495 (2023).

[25] Maritan, M. et al. Building structural models of a whole mycoplasma cell. Journal of Molecular Biology 434, 167351 (2022).

[26] Ahn-Horst, T. A., Mille, L. S., Sun, G., Morrison, J. H. & Covert, M. W. An expanded whole-cell model of e. coli links cellular physiology with mechanisms of growth rate control. NPJ Systems Biology and Applications 8, 30 (2022).

[27] Collins, F. S. et al. New goals for the us human genome project: 1998-2003. Science 282 (1998).

[28] Venter, J. C. et al. The sequence of the human genome. Science 291 (2001).

[29] Regev, A. et al. The Human Cell Atlas. eLife 6 (2017).

[30] Biology, C. S.-C. et al. Cz cellxgene discover: A singlecell data platform for scalable exploration, analysis and modeling of aggregated data. bioRxiv (2023).

[31] Heimberg, G. et al. Scalable querying of human cell atlases via a foundational model reveals commonalities across fibrosis-associated macrophages. bioRxiv (2023).

[32] Dixit, A. et al. Perturb-Seq: dissecting molecular circuits with scalable single-cell RNA profiling of pooled genetic screens. Cell 167 (2016).

[33] Srivatsan, S. R. et al. Massively multiplex chemical transcriptomics at single-cell resolution. Science 367 (2020).

[34] Feldman, D. et al. Pooled genetic perturbation screens with image-based phenotypes. Nature Protocols 17 (2022).

[35] Bock, C. et al. High-content CRISPR screening. Nature Reviews Methods Primers 2 (2022).

[36] Vaswani, A. et al. Attention Is All You Need. In Advances in Neural Information Processing Systems (NeurIPS) (2017).

[37] Rombach, R., Blattmann, A., Lorenz, D., Esser, P. & Ommer, B. High-Resolution Image Synthesis with Latent Difusion Models. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 10684–10695 (2022).

[38] Brown, T. et al. Language Models are Few-Shot Learners. In Advances in Neural Information Processing Systems (NeurIPS) (2020).

[39] Jumper, J. et al. Highly accurate protein structure prediction with AlphaFold. Nature 596 (2021).

[40] Baek, M. et al. Accurate prediction of protein structures and interactions using a three-track neural network. Science 373 (2021).

[41] Lin, Z. et al. Evolutionary-scale prediction of atomic-level protein structure with a language model. Science 379 (2023).

[42] Townshend, R. J. et al. Geometric deep learning of RNA structure. Science 373 (2021).

[43] Gomes, J., Ramsundar, B., Feinberg, E. N. & Pande, V. S. Atomic convolutional networks for predicting protein-ligand binding afinity. arXiv preprint arXiv:1703.10603 (2017).

[44] Alipanahi, B., Delong, A., Weirauch, M. T. & Frey, B. J. Predicting the sequence specificities of DNA-and RNAbinding proteins by deep learning. Nature Biotechnology 33 (2015).

[45] Gainza, P. et al. Deciphering interaction fingerprints from protein molecular surfaces using geometric deep learning. Nature Methods 17 (2020).

[46] Cunningham, J. M., Koytiger, G., Sorger, P. K. & AlQuraishi, M. Biophysical prediction of protein–peptide interactions and signaling networks using machine learning. Nature Methods 17 (2020).

[47] Torng, W. & Altman, R. B. High precision protein functional site detection using 3d convolutional neural networks. Bioinformatics 35 (2019).

[48] Corso, G., Stärk, H., Jing, B., Barzilay, R. & Jaakkola, T. S. DifDock: Difusion Steps, Twists, and Turns for Molecular Docking. In International Conference on Learning Representations (ICLR) (2023).

[49] Kudo, T. et al. Multiplexed, image-based pooled screens in primary cells and tissues with perturbview. Nature Biotechnology 1–10 (2024).

[50] Roohani, Y., Huang, K. & Leskovec, J. Predicting transcriptional outcomes of novel multigene perturbations with GEARS. Nature Biotechnology (2023).

[51] Bunne, C. et al. Learning single-cell perturbation responses using neural optimal transport. Nature Methods 20 (2023).

[52] Lotfollahi, M. et al. Predicting cellular responses to complex perturbations in high-throughput screens. Molecular systems biology 19 (2023).

[53] Bunne, C., Krause, A. & Cuturi, M. Supervised Training of Conditional Monge Maps. In Advances in Neural Information Processing Systems (NeurIPS), vol. 36 (2022).

[54] Bereket, M. & Karaletsos, T. Modelling Cellular Perturbations with the Sparse Additive Mechanism Shift Variational Autoencoder. Advances in Neural Information Processing Systems (NeurIPS) (2023).

[55] Huang, K. et al. Sequential Optimal Experimental Design of Perturbation Screens Guided by Multi-modal Priors. Machine Learning in Computational Biology; Proceedings of Machine Learning Research (2023).

[56] Hie, B., Bryson, B. D. & Berger, B. Leveraging uncertainty in machine learning accelerates biological discovery and design. Cell Systems 11 (2020).

[57] Roohani, Y. H., Vora, J., Huang, Q., Liang, P. & Leskovec, J. Biodiscoveryagent: An ai agent for designing genetic perturbation experiments. In ICLR Workshop on Machine Learning for Genomics Explorations (2024).

[58] Cleary, B. & Regev, A. The necessity and power of random, under-sampled experiments in biology. arXiv preprint arXiv:2012.12961 (2020).

[59] Ji, Y., Zhou, Z., Liu, H. & Davuluri, R. V. DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome. Bioinformatics 37 (2021).

[60] Rives, A. et al. Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences. Proceedings of the National Academy of Sciences 118 (2021).

[61] Brandes, N., Ofer, D., Peleg, Y., Rappoport, N. & Linial, M. ProteinBERT: a universal deep-learning model of protein sequence and function. Bioinformatics 38 (2022).

[62] Celaj, A. et al. An RNA foundation model enables discovery of disease mechanisms and candidate therapeutics. bioRxiv (2023).

[63] Dalla-Torre, H. et al. The nucleotide transformer: building and evaluating robust foundation models for human genomics. bioRxiv (2023).

[64] Nguyen, E. et al. HyenaDNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution. In Advances in Neural Information Processing Systems (NeurIPS) (2024).

[65] Nguyen, E. et al. Sequence modeling and design from molecular to genome scale with Evo. bioRxiv (2024).

[66] Hayes, T. et al. Simulating 500 million years of evolution with a language model. bioRxiv (2024).

[67] Rufolo, J. A. et al. Design of highly functional genome editors by modeling the universe of CRISPR-cas sequences. bioRxiv (2024).

[68] Peng, Z., Schussheim, B. & Chatterjee, P. PTM-Mamba: A PTM-Aware Protein Language Model with Bidirectional Gated Mamba Blocks. bioRxiv (2024).

[69] Dai, B., Mattox, D. E. & Bailey-Kellogg, C. Attention please: modeling global and local context in glycan structure-function relationships. bioRxiv (2021).

[70] Yu, T. et al. LipidBERT: A Lipid Language Model Pretrained on METiS de novo Lipid Library. arXiv preprint arXiv:2408.06150 (2024).

[71] Krishna, R. et al. Generalized biomolecular modeling and design with RoseTTAFold All-Atom. Science 384 (2024).

[72] Rosen, Y. et al. Toward universal cell embeddings: integrating single-cell RNA-seq datasets across species with SATURN. Nature Methods (2024).

[73] Rosen, Y. et al. Universal Cell Embeddings: A Foundation Model for Cell Biology. bioRxiv (2023).

[74] Chen, Y. & Zou, J. GenePT: A Simple But Efective Foundation Model for Genes and Cells Built From ChatGPT. bioRxiv (2024).

[75] Mahdessian, D. et al. Spatiotemporal dissection of the cell cycle with single-cell proteogenomics. Nature 590 (2021).

[76] Chandrasekaran, S. N. et al. Three million images and morphological profiles of cells treated with matched chemical and genetic perturbations. Nature Methods (2024).

[77] Carlson, R. J., Leiken, M. D., Guna, A., Hacohen, N. & Blainey, P. C. A genome-wide optical pooled screen reveals regulators of cellular antiviral responses. Proceedings of the National Academy of Sciences 120 (2023).

[78] Feldman, D. et al. Pooled genetic perturbation screens with image-based phenotypes. Nature Protocols 17, 476–512 (2022).

[79] Thul, P. J. et al. A subcellular map of the human proteome. Science 356 (2017).

[80] McDole, K. et al. In toto imaging and reconstruction of post-implantation mouse development at the single-cell level. Cell 175 (2018).

[81] Nogales, E. & Mahamid, J. Bridging structural and cell biology with cryo-electron microscopy. Nature 628 (2024).

[82] Bauda, E. et al. Ultrastructure of macromolecular assemblies contributing to bacterial spore resistance revealed by in situ cryo-electron tomography. Nature Communications 15 (2024).

[83] Lelek, M. et al. Single-molecule localization microscopy. Nature Reviews Methods Primers 1 (2021).

[84] Möckl, L. & Moerner, W. Super-resolution microscopy with single molecules in biology and beyond–essentials, current trends, and future challenges. Journal of the American Chemical Society 142 (2020).

[85] Deniz, A. A., Mukhopadhyay, S. & Lemke, E. A. Singlemolecule biophysics: at the interface of biology, physics and chemistry. Journal of the Royal Society Interface 5 (2008).

[86] Cesnik, A. et al. Mapping the Multiscale Proteomic Organization of Cellular and Disease Phenotypes. Annual Review of Biomedical Data Science 7 (2024).

[87] Qin, Y. et al. A multi-scale map of cell structure fusing protein images and interactions. Nature 600 (2021).

[88] Dosovitskiy, A. et al. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. arXiv preprint arXiv: 2010.11929 (2020).

[89] Fukushima, K. Neocognitron: a self organizing neural network model for a mechanism of pattern recognition unafected by shift in position. Biological Cybernetics 36 (1980).

[90] LeCun, Y. & Yoshua, B. Convolutional networks for images, speech, and time series. The Handbook of Brain Theory and Neural Networks 3361 (1995).

[91] Moshkov, N. et al. Learning representations for imagebased profiling of perturbations. Nature Communications 15 (2024).

[92] Bao, Y., Sivanandan, S. & Karaletsos, T. Channel vision transformers: An image is worth c x 16 x 16 words. In The Twelfth International Conference on Learning Representations (2024).

[93] Le, T. et al. Analysis of the human protein atlas weakly supervised single-cell classification competition. Nature Methods 19 (2022).

[94] Kraus, O. et al. Masked Autoencoders for Microscopy are Scalable Learners of Cellular Biology. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR) (2024).

[95] Bao, Y. & Karaletsos, T. Contextual vision transformers for robust representation learning. arXiv preprint arXiv:2305.19402 (2023).

[96] Lopez, R., Regier, J., Cole, M. B., Jordan, M. I. & Yosef, N. Deep generative modeling for single-cell transcriptomics. Nature Methods 15 (2018).

[97] Eraslan, G., Avsec, Ž., Gagneur, J. & Theis, F. J. Deep learning: new computational modelling techniques for genomics. Nature Reviews Genetics 20 (2019).

[98] Cui, H. et al. scGPT: toward building a foundation model for single-cell multi-omics using generative AI. Nature Methods (2024).

[99] Theodoris, C. V. et al. Transfer learning enables predictions in network biology. Nature 618, 616–624 (2023).

[100] Comiter, C. et al. Inference of single cell profiles from histology stains with the Single-Cell omics from Histology Analysis Framework (SCHAF). bioRxiv (2023).

[101] Kobayashi-Kirschvink, K. J. et al. Prediction of single-cell RNA expression profiles in live cells by Raman microscopy with Raman2RNA. Nature Biotechnology (2024).

[102] Ryu, J., Lopez, R., Bunne, C. & Regev, A. Cross-modality Matching and Prediction of Perturbation Responses with Labeled Gromov-Wasserstein Optimal Transport. Machine Learning in Computational Biology; Proceedings of Machine Learning Research (2024).

[103] Saar, K. L. et al. Protein Condensate Atlas from predictive models of heteromolecular condensate composition. Nature Communications 15, 5418 (2024).

[104] Macosko, E. Z. et al. Highly parallel genome-wide expression profiling of individual cells using nanoliter droplets. Cell 161 (2015).

[105] Ståhl, P. L. et al. Visualization and analysis of gene expression in tissue sections by spatial transcriptomics. Science 353 (2016).

[106] Lundberg, E. & Borner, G. H. H. Spatial proteomics: a powerful discovery tool for cell biology. Nature Reviews Molecular Cell Biology 20, 285–302 (2019).

[107] Marconato, L. et al. SpatialData: an open and universal data framework for spatial omics. Nature Methods 1–5 (2024).

[108] Scarselli, F., Gori, M., Tsoi, A. C., Hagenbuchner, M. & Monfardini, G. The graph neural network model. IEEE Transactions on Neural Networks 20, 61–80 (2008).

[109] Satorras, V. G., Hoogeboom, E. & Welling, M. E(n) Equivariant Graph Neural Networks. In International Conference on Machine Learning (ICML) (2021).

[110] Somnath, V. R. et al. Aligned Difusion Schrödinger Bridges. In Conference on Uncertainty in Artificial Intelligence (UAI) (2023).

[111] Katharopoulos, A., Vyas, A., Pappas, N. & Fleuret, F. Fast Autoregressive Transformers with Linear Attention. In International Conference on Machine Learning (ICML) (2020).

[112] Abramson, J. et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493–500 (2024).

[113] Klein, A. M. et al. Droplet barcoding for single-cell transcriptomics applied to embryonic stem cells. Cell 161, 1187–1201 (2015).

[114] Qiu, C. et al. A single-cell time-lapse of mouse prenatal development from gastrula to birth. Nature (2024).

[115] Norman, T. M. et al. Exploring genetic interaction manifolds constructed from rich single-cell phenotypes. Science 365 (2019).

[116] Lawson, M. J. et al. In situ genotyping of a pooled strain library after characterizing complex phenotypes. Molecular Systems Biology 13, 947 (2017).

[117] Lawson, M. & Elf, J. Imaging-based screens of poolsynthesized cell libraries. Nature Methods 18, 358–365 (2021).

[118] Mitra, E. D. & Hlavacek, W. S. Parameter estimation and uncertainty quantification for systems biology models. Current Opinion in Systems Biology 18 (2019).

[119] Papamarkou, T. et al. Position: Bayesian Deep Learning is Needed in the Age of Large-Scale AI. In International Conference on Machine Learning (ICML) (2024).

[120] D’Angelo, F., Fortuin, V. & Wenzel, F. On stein variational neural network ensembles. arXiv preprint arXiv:2106.10760 (2021).

[121] Ober, S. W., Rasmussen, C. E. & van der Wilk, M. The promises and pitfalls of deep kernel learning. In Conference on Uncertainty in Artificial Intelligence (UAI), 1206–1216 (2021).

[122] Karaletsos, T. & Bui, T. D. Hierarchical gaussian process priors for bayesian neural network weights. Advances in Neural Information Processing Systems 33 (2020).

[123] Kapoor, S., Maddox, W. J., Izmailov, P. & Wilson, A. G. On uncertainty, tempering, and data augmentation in bayesian classification. Advances in Neural Information Processing Systems 35, 18211–18225 (2022).

[124] Lakshminarayanan, B., Pritzel, A. & Blundell, C. Simple and scalable predictive uncertainty estimation using deep ensembles. Advances in neural information processing systems 30 (2017).

[125] Angelopoulos, A. N. & Bates, S. A gentle introduction to conformal prediction and distribution-free uncertainty quantification. arXiv preprint arXiv:2107.07511 (2021).

[126] Thul, P. J. et al. A subcellular map of the human proteome. Science 356 (2017).

[127] Cho, N. H. et al. OpenCell: Endogenous tagging for the cartography of human cellular organization. Science 375, eabi6983 (2022).

[128] Uhlén, M. Proteomics. Tissue-based map of the human proteome. Science 347, 1260419 (2015).

[129] Berger, C. et al. Cryo-electron tomography on focused ion beam lamellae transforms structural cell biology. Nature Methods 20, 499–511 (2023).

[130] Loconte, V. et al. Soft X-ray tomograms provide a structural basis for whole-cell modeling. The FASEB Journal 37, e22681 (2023).

[131] Mofitt, J. R., Lundberg, E. & Heyn, H. The emerging landscape of spatial profiling technologies. Nature Reviews Genetics 23, 741–759 (2022).

[132] Vandereyken, K., Sifrim, A., Thienpont, B. & Voet, T. Methods and applications for single-cell and spatial multiomics. Nature Reviews Genetics 24, 494–515 (2023).

[133] Palla, G., Fischer, D. S., Regev, A. & Theis, F. J. Spatial components of molecular tissue biology. Nature Biotechnology 40, 308–318 (2022).

[134] Consortium\*, T. S. et al. The tabula sapiens: A multipleorgan, single-cell transcriptomic atlas of humans. Science 376, eabl4896 (2022).

[135] He, B. et al. Integrating spatial gene expression and breast tumour morphology via deep learning. Nature Biomedical Engineering 4, 827–834 (2020).

[136] Bock, C. et al. The Organoid Cell Atlas. Nature Biotechnology 39 (2021).

[137] Schaum, N. et al. Single-cell transcriptomics of 20 mouse organs creates a tabula muris: The tabula muris consortium. Nature 562, 367 (2018).

[138] Consortium, T. T. M. et al. Tabula Microcebus: A transcriptomic cell atlas of mouse lemur, an emerging primate model organism. bioRxiv (2021).

[139] Lu, T.-C. et al. Aging Fly Cell Atlas identifies exhaustive aging features at cellular resolution. Science 380, eadg0934 (2023).

[140] Li, H. et al. Fly Cell Atlas: A single-nucleus transcriptomic atlas of the adult fruit fly. Science 375, eabk2432 (2022).

[141] Lange, M. et al. Zebrahub - Multimodal Zebrafish Developmental Atlas Reveals the State Transition Dynamics of Late Vertebrate Pluripotent Axial Progenitors. bioRxiv (2023).

[142] Katz, K. et al. The Sequence Read Archive: a decade more of explosive growth. Nucleic Acids Research 50, D387–D390 (2022).

[143] Achiam, J. et al. GPT-4 Technical Report. arXiv preprint arXiv:2303.08774 (2023).

[144] Ding, F. & Steinhardt, J. N. Protein language models are biased by unequal sequence sampling across the tree of life. bioRxiv (2024).

[145] Liao, W.-W. et al. A draft human pangenome reference. Nature 617, 312–324 (2023).

[146] Liu, J. et al. Towards out-of-distribution generalization: A survey. arXiv preprint arXiv:2108.13624 (2021).

[147] Zheng, F. et al. Interpretation of cancer mutations using a multiscale map of protein systems. Science 374 (2021).

[148] Ma, J. et al. Using deep learning to model the hierarchical structure and function of a cell. Nature Methods 15, 290–298 (2018).

[149] Yu, M. K. et al. Visible machine learning for biomedicine. Cell 173, 1562–1565 (2018).

[150] Gao, S. et al. Empowering Biomedical Discovery with AI Agents. arXiv preprint arXiv:2404.02831 (2024).

[151] Ouyang, L. et al. Training language models to follow instructions with human feedback. Advances in neural information processing systems 35 (2022).

[152] Gibbs, R. A. et al. The international HapMap project. Nature (2003).

[153] Weinstein, J. N. et al. The cancer genome atlas pan-cancer analysis project. Nature Genetics 45 (2013).

[154] Consortium, E. P. An integrated encyclopedia of DNA elements in the human genome. Nature 489 (2012).

[155] Consortium, G. The Genotype-Tissue Expression (GTEx) project. Nature Genetics 45 (2013).

[156] Pontén, F., Jirström, K. & Uhlen, M. The Human Protein Atlas–a tool for pathology. The Journal of Pathology 216 (2008).

[157] Downey, P. & Peakman, T. C. Design and implementation of a high-throughput biological sample processing facility using modern manufacturing principles. International Journal of Epidemiology 37 Suppl 1 (2008).

[158] Madani, A. et al. Large language models generate functional protein sequences across diverse families. Nature Biotechnology 41 (2023).

[159] Khalil, A. S. & Collins, J. J. Synthetic biology: applications come of age. Nature Reviews Genetics 11 (2010).

[160] Nelson, M. R. et al. The support of human genetic evidence for approved drug indications. Nature genetics 47 (2015).

[161] Mason, C., Brindley, D. A., Culme-Seymour, E. J. & Davie, N. L. Cell therapy industry: billion dollar global business with unlimited potential. Regenerative medicine 6 (2011).

[162] Fischbach, M. A., Bluestone, J. A. & Lim, W. A. Cellbased therapeutics: the next pillar of medicine. Science Translational Medicine 5 (2013).

[163] Bashor, C. J., Hilton, I. B., Bandukwala, H., Smith, D. M. & Veiseh, O. Engineering the next generation of cell-based therapeutics. Nature Reviews Drug Discovery 21 (2022).

[164] Jia, Q., Wang, A., Yuan, Y., Zhu, B. & Long, H. Heterogeneity of the tumor immune microenvironment and its clinical relevance. Experimental Hematology & Oncology 11 (2022).

[165] Melssen, M. M., Sheybani, N. D., Leick, K. M. & Slingluf, C. L. Barriers to immune cell infiltration in tumors. Journal for ImmunoTherapy of Cancer 11 (2023).

[166] Chow, A., Perica, K., Klebanof, C. A. & Wolchok, J. D. Clinical implications of t cell exhaustion for cancer immunotherapy. Nature Reviews Clinical Oncology 19 (2022).

[167] de Visser, K. E. & Joyce, J. A. The evolving tumor microenvironment: From cancer initiation to metastatic outgrowth. Cancer Cell 41 (2023).

[168] Kinker, G. S. et al. Pan-cancer single-cell RNA-seq identifies recurring programs of cellular heterogeneity. Nature Genetics 52 (2020).

[169] Barkley, D. et al. Cancer cell states recur across tumor types and form specific interactions with the tumor microenvironment. Nature Genetics 54 (2022).

[170] Schwartzberg, L., Kim, E. S., Liu, D. & Schrag, D. Precision oncology: who, how, what, when, and when not? In American Society of Clinical Oncology Educational Book. American Society of Clinical Oncology. Annual Meeting, vol. 37, 160–169 (2017).

[171] Aebersold, R. et al. How many human proteoforms are there? Nature Chemical Biology 14 (2018).

[172] Katsoulakis, E. et al. Digital twins for health: a scoping review. NPJ Digital Medicine 7, 77 (2024).

[173] Rajewsky, N. et al. Lifetime and improving european healthcare through cell-based interceptive medicine. Nature 587 (2020).

[174] Alix-Panabières, C. & Pantel, K. Liquid biopsy: from discovery to clinical application. Cancer discovery 11 (2021).

[175] Raue, A. et al. Lessons learned from quantitative dynamical modeling in systems biology. PloS one 8 (2013).

[176] Covert, M. W., Knight, E. M., Reed, J. L., Herrgard, M. J. & Palsson, B. O. Integrating high-throughput and computational data elucidates bacterial networks. Nature 429 (2004).

[177] Vaishnav, E. D. et al. The evolution, evolvability and engineering of gene regulatory DNA. Nature 603 (2022).

[178] Gómez-de Mariscal, E. et al. DeepImageJ: A user-friendly environment to run deep learning models in ImageJ. Nature Methods 18 (2021).

[179] Chen, R. J. et al. Towards a general-purpose foundation model for computational pathology. Nature Medicine 30 (2024).

[180] Moen, E. et al. Deep learning for cellular image analysis. Nature Methods 16 (2019).

[181] Avsec, v. et al. Base-resolution models of transcriptionfactor binding reveal soft motif syntax. Nature Genetics 53 (2021).

[182] Ho, J., Jain, A. & Abbeel, P. Denoising difusion probabilistic models. Advances in Neural Information Processing Systems (2020).

[183] Lipman, Y., Chen, R. T., Ben-Hamu, H., Nickel, M. & Le, M. Flow Matching for Generative Modeling. In International Conference on Learning Representations (ICLR) (2023).

[184] Pariset, M., Hsieh, Y.-P., Bunne, C., Krause, A. & De Bortoli, V. Unbalanced Difusion Schrödinger Bridge. arXiv preprint arXiv:2306.09099 (2023).

[185] Cao, Y. & Shen, Y. Energy-based graph convolutional networks for scoring protein docking models. Proteins (2020).

[186] Brbić, M. et al. Annotation of spatially resolved single-cell data with STELLAR. Nature Methods 19 (2022).

[187] Wu, Z. et al. Graph deep learning for the characterization of tumour microenvironments from spatial protein profiles in tissue specimens. Nature Biomedical Engineering 6 (2022).

[188] Hamilton, W., Ying, Z. & Leskovec, J. Inductive Representation Learning on Large Graphs. Advances in Neural Information Processing Systems (NeurIPS) 30 (2017).

## Acknowledgements

We thank Rok Sosič, Charilaos Kanatsoulis, Lata Nair, Kexin Huang, Hanchen Wang, Minkai Xu, Michael Bereket, Romain Lopez, Takamasa Kudo, Ayush Agrawal, Arnuv Tandon, Mika Jain, Michihiro Yasunaga, Tim Jing, Michael Moor, George Crowley, Maria Brbić, Andrew Tolopko, Ivana Jelic, Ana-Maria Istrate, Sara Simmonds, Maximilian Lombardo, Pablo Garcia-Nieto, Mike Lin, Noorsher Ahmed, Orit Rozenblatt-Rosen, Gita Mahmoudabadi, Zoe Piran, Adam Gayoso and Anshul Kundaje for discussions. J.L. was supported by NSF under Nos. OAC-1835598 (CINES), CCF-1918940 (Expeditions), DMS-2327709 (IHBEM); Stanford Data Applications Initiative, Wu Tsai Neurosciences Institute, Stanford Institute for Human-Centered AI, Chan Zuckerberg Initiative, Amazon, Genentech, GSK, Hitachi, SAP, and UCB. E.L. was supported by Schmidt Futures, the Bridge2AI Program (NIH Common Fund; OT2 OD032742), the Cancer Cell Map Initiative (NCI Center for Cancer Systems Biology; U54 CA274502), the Wallenberg Foundation (2021.0346), Stanford Institute for Human-Centered AI, Chan Zuckerberg Initiative, and Param Hansa Philanthropies.

## Competing interests

C.B. and A. R. are employees of Genentech, a member of the Roche Group. A.R. has equity in Roche. A.R. was a co-founder and equity holder of Celsius Therapeutics, and is an equity holder in Immunitas. Until July 31, 2020 A.R. was an S.A.B. member of ThermoFisher Scientific, Syros Pharmaceuticals, Neogene Therapeutics and Asimov. A.R. is a named inventor on multiple filed patents related to single cell and spatial genomics, including for scRNA-seq, spatial transcriptomics, Perturb-Seq, compressed experiments, and PerturbView. E.L. is an advisor for the Chan-Zuckerberg Initiative Foundation. N.J.S. is an employee of EvolutionaryScale, PBC.

Box 1: Grand challenges for building the AI Virtual Cell.

Outlining capabilities and designing evaluation frameworks. The burgeoning number of foundation models in biology perform a subset of the capabilities of virtual cells outlined in this Perspective. Given the diversity of these approaches, it is important to define what the core capabilities of AIVCs should be and how those capabilities can be evaluated. For every capability, proper metrics must be designed and comprehensive evaluation data be collected. Models’ capabilities should be assessed both on general performance as well as on their ability to answer specific biological questions. It is imperative to continuously improve benchmarking strategies along with AIVC models and ensure that they align with biologically meaningful objectives. As the field develops better alignment on these questions, collaborative opportunities will arise and the speed at which virtual cells can be generated will accelerate.

Establishing self-consistency across varying contexts with diferent architectures. Biology is tremendously complex: it operates across diferent scales, in diferent contexts and is measured with diferent modalities. AIVC models must be self consistent across all of these axes. Models should propagate function across physical scales— interactions between molecules should have consistent efects when measuring binding afinity, gene expression, cell-cell communication or tissue organization. As physical and dynamic scales increase in scope and size, additional context, for example species, cell type, tissue, disease status etc, should fine-tune predictions made at smaller resolutions, while also accounting for stochasticity. Model predictions should also be agnostic to their input and output modalities. The same entity, profiled with diferent technologies, should have the same internal representation in an AIVC. To properly model such complex behaviors, many machine learning approaches should be explored and their merits carefully judged.

Balancing interpretability and biological utility. A consistent trend in the application of deep learning methods to biology, accelerated by the rise of large foundation models, has been the implicit trade-of between models performance gains and their increasingly uninterpretable ’black-box’ natures. AIVC models will ultimately be judged on their ability to expand our understanding of biology, either by providing novel insights to biological processes or by accelerating the scientific process. To achieve this goal, AIVC models must make highly accurate and well-calibrated predictions that simulate biology, and the trade-of between actionabilty and interpretability will have to be balanced. Actionable model outputs are those of high utility to design afordable and eficient validation experiments and are key for initial real-world use. Various approaches exist for explaining model predictions, including causal modeling, sparse featurization and counterfactual reasoning, and this is a highly active research area. Building intuitive interfaces that facilitate the study and interpretation of AIVCs via other models, such as AI research agents will further increase downstream utility.

Constructing a framework for collaborative cell modeling. The successful development of AI Virtual Cells will require collaboration across disciplines. We foresee a future where AI Virtual Cell platforms function as open, interconnected hubs for collaborative development and broad deployment of cell models to researchers, and as education hubs delivering training to researchers, as well as providing engagement activities for educators, patients, and the public. Thus, investments in infrastructure fostering open and collaborative development of AI Virtual Cells should be of high priority.

Ensuring AI Virtual Cells benefit all and promote ethical and responsible use. Generating large open datasets that reflect human diversity—datasets integral for training AIVC models—poses a substantial challenge. Developers will have to use the utmost care to ensure these datasets are used ethically and transparently while building AIVCs and develop strategies to mitigate risks of model contamination with falsified data. Early adopters of AIVCs will have a key role in promoting and demonstrating responsible use of these models. Furthermore, the development of chat-based interfaces could be crucial in democratizing access to AIVCs. Close collaboration with ethics and regulatory experts from the outset is paramount for establishing new norms that will facilitate the responsible use of AI Virtual Cells.

Understanding the value of diferent data types to prioritize large-scale data generation. A fundamental question for the collaborative development of AIVCs is which data and modalities should be collected to enable generalization across biological contexts and scales. These data will need to encompass the breadth of biology in diferent species, domains and modalities, representing the heterogeneity of life, while maintaining depth suficient to distinguish true signals from noise. A key aspect of data generation will be the simultaneous measurement of temporal and physical scales, while also allowing perturbations of the system.

## Cell engineering to enable phenotypic drug discovery and cell-based therapeutics

One challenge in developing successful therapies is the dificulty in incorporating the full underlying genetic, molecular and cellular basis of disease during drug discovery and development <sup>160</sup>. These context-specific underpinnings are not fully specified, and often vary between human patients and model systems used in pre-clinical studies. By integrating biological data from various sources relevant to specific disease contexts, the AIVC could generate an environment for testing diferent therapeutic inter-

ventions in silico, and identify approaches for engineering cells to reverse disease phenotypes, while accounting for the <sup>AI</sup> <sup>Virtual</sup> <sup>Cell</sup>efects of varying both treatments and patient profiles. By representing the overall disease phenotype specific to patient populations (rather than one specific biochemical target at a time), the AIVC can enable virtual phenotypic screens. Even though in silico experiments may not always be fully accurate, by prioritizing virtual hits with higher chances of success, the AIVC can lower experimentation costs and accelerate the process.

spatial The AIVC has potential to push the cell therapy frontier. With growing evidence afirming the eficacy and safety <sup>tumor</sup> <sup>heterogeneity</sup> <sup>and</sup> <sup>microenvironment</sup> <sup>transcriptomics</sup>of cell-based therapies for rare diseases and cancer <sup>161,162,163</sup>, the AIVC can improve systematization and precision to cell engineering. For example, virtual cell-based engineering could enable targeted modifications to pancreatic beta cells to create individualized beta cell replacement therapies for Type 1 diabetes. By simulating the biological phenotype of individual patients, in silico experiments within the AIVC could identify interventions that help drive the diferentiation of beta cells from progenitors, cloak them from the immune system, and maintain their function, with the ultimate goal of digital either transplanting these engineered cells into patients or engineering them in situ.<sup>or AI</sup> <sup>Virtual</sup> <sup>Cell</sup>

## <sup>plasma</sup>Unlocking the power of spatial biology to fight cancer

Spatial structures in cancer, specifically within the tumor mi croenvironment (TME) are critical drivers of cancer progression, and can drive resistance to the immune system and limit drug eficacy <sup>164</sup>. Malignant cells within a tumor can engage in active immune evasion, by either blocking immune infiltration <sup>165</sup>, evadtokenized ing immune recognition, or dampening immune cell function <sup>166</sup>. self-attention Thus, immune resistance must be understood in the spatial con C text of the cellular neighborhood in order to identify the specific A cell states and gene signatures involved. While next-generation

spatial profiling methods enable researchers to experimentally investigate the heterogeneity of the TME <sup>167</sup>, an AIVC<sup>chemical</sup> <sup>drugse.g.,</sup> <sup>transformer</sup> <sup>blocks</sup>could extend these analyses to a universal, pan-cancer framework, which can be personalized to individual patients. Usingor AI Virtual Cell experimentationan AIVC model, cancer researchers should be able to identify TME niches shared across multiple cancer types from <sub>digital</sub> many patients. Identifying pan-cancer markers can drive cancer treatment both by highlighting new targets, but also<sup>genetic</sup> <sup>perturbations</sup> <sup>tissue</sup> <sup>sample twinpatient</sup> AI Virtual Cellby identifying existing treatments that can be applied to new cancer types <sup>168,169</sup>. In this setting, the AIVC would help identify the interactions associated with TME cell states, and would search for similar states from any disease where existing treatments exist.

Finally, the AIVC could greatly advance precision oncology <sup>170</sup>. Given that the AIVC will capture intrinsic variation,<sub>AI</sub> <sub>Virtual</sub> <sub>Cell</sub> the genetic diversity of individual patient’s cancers will be represented in any analyses. While the AIVC would already accurately qualify the change in the expression of genes, tumor sequencing data would allow it to model the change of function of those genes, for example through loss of function, change in post-translational modifications, or rewiring of protein-protein interactions and signaling networks <sup>171</sup>.<sub>spatial</sub>

## Diagnostic virtual cell models for individual patients

<sup>T</sup> <sub>A</sub> The AIVC could introduce a new approach to diagnostics that in-<sup>G</sup> corporates a personalized AI Virtual Cell (or a digital twin <sup>172</sup>) to <sup>…</sup> transformer blockstrack a patient’s health and suggest suitable interventions. The AIVC would create a detailed representation of each patient’s cells by incorporating specific patient data, such as genetic sequences, single-cell profiles from blood, and tissue pathology images, along with additional clinical information from their pathhealth records. Periodic updates to each patient’s AIVC instance enable monitoring of evolving health conditions, prediction of <sub>time</sub>upcoming adverse events and potential therapeutic outcomes.

Through additional updates from less costly assays, this virtual patient model could be progressively refined and made more robust <sup>173</sup>. For example, transcriptomic or genetic liquid biopsies can reveal significant and diverse characteristics of a patient from a single test and could greatly aid in the diagnosis of a broad spectrum of conditions <sup>174</sup>. Throughtissue sample <sup>digital</sup> <sub>twin</sub>patient the virtual cell’s implicit and structured representation of universal cell types and states, one can envision the creation of patient models of inaccessible cell types, such as beta cells in the pancreas or neurons in the brain, generated after<sup>plasma</sup> sampling accessible cell types such as blood or skin.

## A hypothesis-generating framework for scientific research

Traditionally, the biological research community has relied on computational models for analyzing data from past experiments <sup>tokenized</sup> <sub>input</sub>based on an existing hypothesis <sup>175,176</sup>. The virtual cell could <sub>A</sub> switch the paradigm by computationally exploring a vast array of T possible hypotheses through in silico experimentation. It could G identify the most informative experiments for addressing specific <sub>…</sub>biological questions, shifting the role of computational models from merely validating hypotheses or processing observations without a particular goal to generating specific sets of hypotheses to pursue.

This shift could greatly enhance the scientific discovery process: Instead of conducting a single experiment followed by an in-depth analysis, scientists can engage in a dynamic iterative interaction with the virtual cell. With each new piece of data, they can refine their understanding of the biological system and consult the virtual cell to identify what additional experimental data could be valuable. Ultimately, we may be able to perform active learning with biologists in the loop and construct self-driving labs for eficient and unbiased generation of virtual cells.

## Box 3: AI techniques for building the AI Virtual Cell.

The AI Virtual Cell will connect a number of diverse neural network architectures. While these architectures may not have been purpose-built for biological applications, they have each demonstrated success when matched with specific biological modalities and inductive biases. In many cases, these architectures may be exchangeable, and one must weigh their individual trade-ofs in accuracy, speed, and generalizability. Beyond, the community is actively developing AI architectures tailored to the characteristics of (large) biological datasets.

## Transformers

A transformer neural network <sup>36</sup> is comprised of multiple transformer layers, each taking a series of tokens (discrete pieces of information such as words, RNA molecules, or gene representations) as input—initial tokens for the first layer and outputs from the preceding layer for subsequent ones. Within each layer, tokens use self-attention to integrate context from other tokens, enhancing their own representations, which are then processed through a feed forward network. This architecture, which fundamentally requires only a collection of tokens, adapts well across various applications and use cases.

The collection of tokens passed to a transformer does not have any ordering by default. Additionally, the self attention mechanism, the core of the success of the transformer, can be taken as a strong biological inductive bias. For instance, in representing cells through their RNA molecules detected via scRNA-seq, each RNA molecule, represented<sub>G</sub> as a token, interacts with others, modeling gene interactions through self-attention <sup>36</sup>. Customizing input tokens with numerical representations of genes further allows the integration of diverse biological data scales, from individual genes… to whole cells <sup>73,98,74</sup>.

Additionally, introducing positional encodings to tokens enables transformers to process sequences, such as natural language <sup>36</sup> or biological sequences like DNA <sup>59,63,177</sup>, by incorporating sequence-specific dependencies. This approach is crucial in applications like masked language modeling, where the model predicts missing tokens in sequences, enhancing its understanding of contextual relationships within data. Innovations continue to refine transformers, increasing their capacity to handle longer sequences and improving eficiency, with advancements like state-space models enabling the generation of extensive DNA sequences <sup>64,65</sup>.

## Convolutional neural networks

A convolutional neural network is a deep learning model primarily used for analyzing images <sup>89,90</sup>. It consists of multiple layers that automatically and adaptively learn spatial hierarchies of features through backpropagation. This learning is facilitated by convolutional layers that apply filters to local patches of input data, pooling layers that reduce dimensionality, and fully connected layers that interpret the features extracted to make decisions.

In the field of biology, CNNs have proven invaluable for tasks involving image data due to their ability to detect complex patterns and structures, such as microscope images of cells and tissues. Here, CNNs play a critical role in multiplex imaging <sup>178</sup>, where multiple targets within a single sample are labeled and visualized simultaneously. This technique is particularly useful in studying

the complex interactions of diferent molecules or cell types within a heterogeneous tissue environment <sup>93</sup>. Another notable application is in the analysis of H&E stained tissue sections, commonly used in clinical pathology <sup>179</sup>. Lastly, in drift flive-cell imaging, CNNs are employed to track dynamic changes within cells or even single-molecules over time, providing insights into cell migration, responses to treatment or the movement and interaction of individual molecules within cells, revealing crucial biological processes at a molecular level <sup>180</sup>.

difusion Beyond their traditional use in image processing, CNNs can also be applied to model sequence data, such as DNA <sup>path</sup>sequences, where they identify patterns and features that are predictive of biological functions <sup>181</sup>. Despite their extensive utility, CNNs are increasingly being supplemented or replaced by vision transformer models <sup>88</sup>, which leverage self-attention drift fmechanisms to process entire images in parallel. These models can often achieve higher accuracy on tasks where <sup>time</sup>understanding the global context within the image is crucial.

## Difusion models

Difusion models are a class of generative deep learning models that have recently gained attention for their ability to generate high-quality, diverse samples across various domains <sup>182</sup>. They operate by gradually transforming a distribution of random noise into a structured output (e.g., images, text, cellular states, etc.) through a process that mimics a physical difusion process. Building up on difusion model architectures, approaches such as flow matching methods can also model the distributional evolution over time <sup>183</sup>, making them especially powerful in biological applications where dynamic changes and temporal progression are critical. Flow matching methods thus capture and generate sequences of data that reflect continuous transformations, such as the developmental stages of cells over time and space or the response of biological systems to treatments <sup>110,184</sup>. The ability of difusion and flow matching models to learn and replicate complex distributions, combined with the temporal and spatial modeling capabilities of flow matching methods, makes them particularly suited for tasks that involve high-dimensional, intricate data structures typical of biological systems.

## Graph neural networks

Graph neural networks are a set of architectures that can model graphical data <sup>108</sup>. Graphs, sets of nodes connected by edges, are useful representations for many kinds of biological data. When modeling a biological system, a GNN could be a good choice if a graph structure represents some core inductive bias. For example, a protein structure <sup>185</sup> can be thought of as a graph where residues are nodes, and their bonds are edges. Cells in a tissue form a graph: each cell is a node, and the cells it is physically proximal to, are connected by edges <sup>186,187</sup>. In both cases, the graph represents how nodes are physically proximal to each other. For spatially organized cells, the graph represents how they may pass chemical signals between one another.

GNNs can be used to make predictions about individual nodes, edges or the graph as a whole <sup>188</sup>. For simplicity, in the following, we describe a node-based GNN. At each layer, a node updates its representation using a neural network,

which can take in that node’s current representation, in addition to the representations of the node’s neighbors, which are connected by an edge. By stacking GNN layers, a node can receive ’messages‘ from neighboring nodes at increasing distances, ’hops‘, from it. Nodes and edges can both be initialized with diferent features, which control their final representation and what messages they pass to their neighbors. For example, a GNN trained on spatial transcriptomic data could take node features to be the virtual cell representation of each cell’s gene expression. The GNN would then update those representations to include context about each cell’s neighbors, helping to identify spatial interactions and niches <sup>187</sup>.

## Authors

Charlotte Bunne <sup>1,2,3,4,∗</sup>, Yusuf Roohani <sup>1,3,5∗</sup>, Yanay Rosen <sup>1,3,∗</sup>, Ankit Gupta <sup>3,6</sup>, Xikun Zhang <sup>1,3,7</sup>, Marcel Roed <sup>1,3</sup>, Theo Alexandrov<sup>8,9</sup>, Mohammed AlQuraishi<sup>10</sup>, Patricia Brennan<sup>3</sup>, Daniel B. Burkhardt<sup>11</sup>, Andrea Califano<sup>10,12,13</sup>, Jonah Cool<sup>3</sup>, Abby F. Dernburg<sup>14</sup>, Kirsty Ewing<sup>3</sup>, Emily B. Fox<sup>1,15,16</sup>, Matthias Haury<sup>17</sup>, Amy E. Herr<sup>16,18</sup>, Eric Horvitz<sup>19</sup>, Patrick D. Hsu<sup>5,18,20</sup>, Viren Jain<sup>21</sup>, Gregory R. Johnson<sup>22</sup>, Thomas Kalil<sup>23</sup>, David R. Kelley<sup>24</sup>, Shana O. Kelley<sup>25,26</sup>, Anna Kreshuk<sup>27</sup>, Tim Mitchison<sup>28</sup>, Stephani Otte<sup>17</sup>, Jay Shendure<sup>29,30,31,32</sup>, Nicholas J. Sofroniew<sup>33</sup>, Fabian Theis<sup>34,35,36</sup>, Christina V. Theodoris<sup>37,38</sup>, Srigokul Upadhyayula<sup>14,16,39</sup>, Marc Valer<sup>3</sup>, Bo Wang<sup>40,41</sup>, Eric Xing<sup>42,43</sup>, Serena Yeung-Levy<sup>1,44</sup>, Marinka Zitnik<sup>45,46,47</sup>, Theofanis Karaletsos <sup>3,‡</sup>, Aviv Regev <sup>2,‡</sup>, Emma Lundberg <sup>3,6,7,48,‡</sup>, Jure Leskovec <sup>1,3,‡</sup>, Stephen R. Quake <sup>3,7,49,‡</sup>

<sup>∗</sup> These authors contributed equally.

‡ Correspondence to: Theofanis Karaletsos, Aviv Regev, Emma Lundberg, Jure Leskovec, and Stephen R. Quake.

<sup>1</sup> Department of Computer Science, Stanford University, Stanford, CA, USA, <sup>2</sup> Genentech, South San Francisco, CA, USA, <sup>3</sup> Chan Zuckerberg Initiative, Redwood City, CA, USA, <sup>4</sup> School of Computer and Communication Sciences and School of Life Sciences, EPFL, Lausanne, Switzerland, <sup>5</sup> Arc Institute, Palo Alto, CA, USA, <sup>6</sup> KTH Royal Institute of Technology, Science for Life Laboratory, Department of Protein Science, Stockholm, Sweden, <sup>7</sup> Department of Bioengineering, Stanford University, Stanford, CA, USA, <sup>8</sup> Department of Pharmacology, University of California, San Diego, CA, USA, <sup>9</sup> Department of Bioengineering, University of California, San Diego, CA, USA, <sup>10</sup> Department of Systems Biology, Columbia University, New York, NY, USA, <sup>11</sup> Cellarity, Somerville, MA, USA, <sup>12</sup> Vagelos College of Physicians and Surgeons, Columbia University Irving Medical Center, New York, NY, USA, <sup>13</sup> Chan Zuckerberg Biohub New York, NY, USA, <sup>14</sup> Department of Molecular and Cell Biology, University of California, Berkeley, Berkeley, CA, USA, <sup>15</sup> Department of Statistics, Stanford University, Stanford, CA, USA, <sup>16</sup> Chan Zuckerberg Biohub San Francisco, CA, USA, <sup>17</sup> Chan Zuckerberg Institute for Advanced Biological Imaging, Redwood City, CA, USA, <sup>18</sup> Department of Bioengineering, University of California, Berkeley, CA, USA, <sup>19</sup> Microsoft Research, Redmond, WA, USA, <sup>20</sup> Center for Computational Biology, University of California, Berkeley, Berkeley, CA, USA, <sup>21</sup> Google Research, Mountain View, CA, USA, <sup>22</sup> NewLimit, San Francisco, CA, USA, <sup>23</sup> Schmidt Futures, USA, <sup>24</sup> Calico Life Sciences LLC, San Francisco, CA, USA, <sup>25</sup> Chan Zuckerberg Biohub Chicago, IL, USA, <sup>26</sup> Northwestern University, Evanston, IL, USA, <sup>27</sup> Cell Biology and Biophysics Unit, European Molecular Biology Laboratory, Heidelberg, Germany, <sup>28</sup> Department of Systems Biology, Harvard Medical School, Boston, MA, USA, <sup>29</sup> Department of Genome Sciences, University of Washington, Seattle, WA, USA, <sup>30</sup> Brotman Baty Institute for Precision Medicine, Seattle, WA, USA, <sup>31</sup> Seattle Hub for Synthetic Biology, Seattle, WA, USA, <sup>32</sup> Howard Hughes Medical Institute, Seattle, WA, USA, <sup>33</sup> EvolutionaryScale, PBC, USA, <sup>34</sup> Institute of Computational Biology, Helmholtz Center Munich, Munich, Germany, <sup>35</sup> School of Computing, Information and Technology, Technical University of Munich, Munich, Germany, <sup>36</sup> TUM School of Life Sciences Weihenstephan, Technical University of Munich, Munich, Germany, <sup>37</sup> Gladstone Institute of Cardiovascular Disease, Gladstone Institute of Data Science and Biotechnology, San Francisco, CA, USA, <sup>38</sup> Department of Pediatrics, University of California, San Francisco, CA, USA, <sup>39</sup> Molecular Biophysics and Integrated Bioimaging Division, Lawrence Berkeley National Laboratory, Berkeley, CA, USA, <sup>40</sup> Department of Computer Science, University of Toronto, Toronto, Ontario, Canada, <sup>41</sup> Vector Institute, Toronto, Ontario, Canada, <sup>42</sup> Carnegie Mellon University, School of Computer Science, Pittsburgh, PA, USA, <sup>43</sup> Mohamed Bin Zayed University of Artificial Intelligence, Abu Dhabi, United Arab Emirates, <sup>44</sup> Department of Biomedical Data Science, Stanford University, Stanford, CA, USA, <sup>45</sup> Department of Biomedical Informatics, Harvard Medical School, Boston, MA, USA, <sup>46</sup> Kempner Institute for the Study of Natural and Artificial Intelligence, Harvard University, Cambridge, MA, USA, <sup>47</sup> Broad Institute of MIT and Harvard, Cambridge, MA, USA, <sup>48</sup> Department of Pathology, Stanford University, Stanford, CA, USA, <sup>49</sup> Department of Applied Physics, Stanford University, Stanford, CA, USA.

## Figure Descriptions

**Figure 1.** Capabilities of the AI Virtual Cell. a. The AI Virtual Cell provides a Universal Representation of a cell state that can be obtained across species and conditions, and generated from diferent data modalities across scales (molecular, cellular, multicellular). b. The AI Virtual Cell possesses capabilities to represent and predict cell biology. This universality allows the representation to act as a reference that can generalize to previously unobserved cell states, providing guidance for future data generation. Since the representation is shared across modalities, it also remains invariant to the specific data type used to generate it, serving as a virtual representation for unified analysis across modalities. The AI Virtual Cell also allows modeling the dynamics of cells as they transition between diferent states, whether naturally due to processes such as diferentiation or due to genetic variation or artificially through engineered perturbations. Thus, the AI Virtual Cell enables in silico experimentation that would otherwise be cost-prohibitive or impossible in a lab. c. The utility of the AI Virtual Cell depends on its interactions with humans at diferent levels. At the individual scientist level, it must be accessible through open licenses and the democratization of computing resources. Interpretability can be established through intermediary layers such as language models that allow the virtual cell to communicate its results efectively. At the scientific community level, evaluating the AI Virtual Cell should focus on core capabilities that move beyond narrow benchmarks. Community development will be crucial for ongoing improvements to the virtual cell that remain accessible. At the societal level, the AI Virtual Cell must ensure the privacy of its contents to protect sensitive data.

**Figure 2.** Overview of the AI Virtual Cell. a. Similar to biological cells, b. the AI Virtual Cell models cell biology across diferent physical scales, including molecular, cellular, and multicellular. Along the physical dimension, the first scale models the state and interactions of individual molecules, such as those of the central dogma, as well as additional molecules like metabolites. Molecules can be represented as sequences or atomic structures. The next scale represents cells as collections of these molecules. For example, such cells contain a genetic sequence, RNA transcripts and some quantities of proteins. Molecules within cells have specific locations that may be related to their function. The final scale models the interactions between cells, how they communicate and form complex tissues. Each scale relies on Universal Representations that are learned from multi-modal data and are integrating URs from the previous scale. c. To capture the behavior and dynamics of physical cells, its components, or collections, d. the AI Virtual Cell comprises Virtual Instruments. On the cellular scale, for example, Manipulator VIs simulate how cell states change as cells divide, migrate, develop from progenitor states, or respond to perturbations through learned transitions in the URs. Decoder VIs allow to decode the cell UR, e.g., to understand phenotypic properties.