## Contents

1 Computational Methods 1   
1.1 Whole-Cell Simulation Algorithm 1   
1.2 Cellular Processes 1   
1.3 Cellular Process Integration 2   
1.4 Initial Conditions . . 3   
1.5 Reconstruction 4   
1.6 Experimental Validation . 6   
1.7 Computational Implementation 7   
1.8 Computational Simulation & Analysis 7   
2 Cellular State Methods 8   
2.1 Chromosome 9   
2.2 FtsZ Ring 11   
2.3 Geometry 12   
2.4 Host . 15   
2.5 Mass . 15   
2.6 Metabolic Reaction . 17   
2.7 Metabolite . . 17   
2.8 Polypeptide . 19   
2.9 Protein Complex 20   
2.10 Protein Monomer 20   
2.11 Ribosome 22   
2.12 RNA . 24   
2.13 RNA Polymerase 25   
2.14 Stimulus . 27   
2.15 Time . 27   
2.16 Transcript 28   
3 Cellular Process Methods 29   
3.1 Chromosome Condensation 32   
3.2 Chromosome Segregation 34   
3.3 Cytokinesis 35   
3.4 DNA Damage . 39   
3.5 DNA Repair . 40   
3.6 DNA Supercoiling 43   
3.7 FtsZ Polymerization 49   
3.8 Host Interaction 51   
3.9 Macromolecular Complexation 52   
3.10 Metabolism 53   
3.11 Protein Activation 58   
3.12 Protein Decay . . 59   
3.13 Protein Folding . 63   
3.14 Protein Modification 65   
3.15 Protein Processing I 67   
3.16 Protein Processing II 69   
3.17 Protein Translocation 71   
3.18 Replication 73   
3.19 Replication Initiation 78   
3.20 Ribosome Assembly 83   
3.21 RNA Decay . . 85   
3.22 RNA Modification 86   
3.23 RNA Processing 88   
3.24 Terminal Organelle Assembly 91   
3.25 Transcription 93   
3.26 Transcriptional Regulation . 98   
3.27 Translation 100   
3.28 tRNA Aminoacylation 103   
4 Experimental Procedures 106   
4.1 Media Composition . 106   
4.2 Frozen Stocks . 106   
4.3 Colorimetric Growth Assay Serial Dilutions 106   
4.4 Colorimetric Growth Assay Calculations 106   
4.5 Quantitative PCR to Measure Cell Growth 108   
A Computational Implementation 109   
A.1 Whole-Cell Model Architecture 109   
A.2 Test-Driven Development 110   
A.3 Distributed Simulation . 111   
A.4 Computational Analysis 111   
A.5 Knowledge Base 111   
A.6 Source Code Organization 111   
A.7 Key Classes & Functions . 112   
A.8 Third-Party Software . 118   
B List of Abbreviations 120

## Chapter 1

# Computational Methods

The goal of this study was to predict the complex phenotypes of individual cells in terms individual molecules and their interactions. The primary challenges to building a unified whole-cell model of a single cell are threefold: (1) complexity, processes relevant to cellular behavior are diverse and span a wide range of length and time scales, (2) heterogeneity, cellular networks have heterogeneous mathematical structures and are typically investigated using heterogeneous experimental methods, and (3) sparsity, little quantitative data rigorously describing single cell physiology is available. We felt that the flexibility of a hybrid model allowed us to best meet our goal while navigating these challenges. This chapter discusses the mathematical foundation and construction of the M. genitalium whole-cell model, as well as model fitting and validation. Appendix A provides further discussion of the implementation, execution, and testing of the whole-cell model.

## 1.1 Whole-Cell Simulation Algorithm

Overall, the whole-cell model is similar to a system of ordinary diferential equations (ODEs) where the 16 cellular states are analogous to the state variables and the 28 cellular processes are analogous to the diferential equations. Therefore, the whole-cell model is simulated using an algorithm comparable to those used to numerically integrate ODEs, such as the Runge-Kutta 4<sup>th</sup> order method<sup>928</sup>. Algorithm S1 summarizes the whole-cell simulation algorithm. First, the cell state variables are initialized. Second, the temporal evolution of the cell state is calculated on a 1 s time scale by repeatedly allocating the cell state variables among the processes, executing each of the cellular process sub-models, and updating the values of the cell states. Finally, the simulation terminates when either the cell divides, or the time reaches a predefined maximum value. The principal diferences between the whole-cell model algorithm and numerical ODE integration methods are (1) the whole-cell model “equations” are grouped into 28 processes, (2) the wholecell model “variables” are grouped into 16 cellular states, and (3) the state variables must be allocated among the processes at each time step to satisfy the sub-model independence assumption.

## 1.2 Cellular Processes

Because biological systems are modular, cells can be modeled by (1) dividing cells into functional processes, (2) independently modeling each process on a short time scale, and (3) integrating process sub-models at longer time scales. We divided M. genitalium into the 28 functional processes illustrated in Figure 1 of the accompanying manuscript, and modeled each process independently on a 1 s time scale using diferent mathematics and diferent experimental data. The sub-models spanned six areas of cell biology: (1) transport and metabolism, (2) DNA replication and maintenance, (3) RNA synthesis and maturation, (4) protein synthesis and maturation, (5) cytokinesis, and (6) host interaction. Sub-models were implemented as separate classes. See Chapter 3 for further discussion of each sub-model.

Algorithm S1 | Whole-cell dynamic simulation algorithm. Algc  
Construct whole-cell simulation objects using the KnowledgeBase classes   
Computationally align processes and fit parameters   
Identify initial conditions variance control parameters using Algorithm S2   
Initialize cell state using Algorithm S3 and the fit values of the cell state variance control parameters   
repeat   
Increment the time by 1 s   
Set the external conditions based on Table S3F and Table S3H   
Allocate shared resources:   
foreach metabolite i in compartment $j$ do   
foreach process k do Calculate the demand, $d _ { i j k }$ , of process k for metabolite i in compartment j   
Divide the total count, $m _ { i j }$ , of metabolite i in compartment $j$ into temporary dedicated pools, $m _ { i j k }$ , for each   
process proportional to demand, $m _ { i j k } \gets m _ { i j } \frac { d _ { i j k } } { \sum _ { k } d _ { i j k } }$   
Compute temporal evolution:   
foreach process i do   
Retrieve the current values of cell state variables and the counts of metabolites allocated to process i   
Compute the contribution of process i to the temporal evolution of the cell state   
Update the values of the cell state variables   
until cell divided or time > 1.5× average mass doubling time

## 1.3 Cellular Process Integration

## Cell States

We integrated the sub-models in three steps. First, we structurally integrated the process sub-models by linking their common inputs and outputs. However, rather than directly linking these inputs and outputs, we mapped the inputs and outputs of each sub-model onto 16 state variables which together represent the complete configuration of the modeled cell: (1) metabolite, RNA, and protein copy numbers, (2) metabolic reaction fluxes, (3) nascent DNA, RNA, and protein polymers, (4) molecular machines, (5) cell mass, volume, and shape, (6) the external environment including the host urogenital epithelium, and (7) time. Each cellular state variable was implemented as a separate class. See Chapter 2 for further discussion of the mathematics and computational implementation of each state variable.

## Shared Resource Allocation

Second, to satisfy our sub-model independence assumption, at each time step we computationally allocated common sub-model inputs. At each simulation time step, prior to the evaluation of the sub-models, we estimated the metabolite resources required by each process and divided the total pool of each metabolite among the processes proportional to demand. Resource requirements were estimated by calculating the expected metabolite consumption of each process conditioned on the current cell configuration and an infinite metabo lite supply. Algorithm S1 outlines the shared metabolite allocation algorithm. Because macromolecules and enzymatic capacity are less heavily shared by the cellular processes, we chose not to implement similar procedures for these sub-model inputs.

## Process Alignment & Parameter Fitting

Third, because the 28 cellular processes were trained using diferent experimental data obtained by diferent investigators under diferent conditions using diferent techniques and diferent model organisms, we refined the values of the sub-model parameters to make the processes mutually consistent. This was necessary for example, because amino acid production by the Metabolism process, which was trained using the observed amino acid composition of M. gallisepticum reported by Morowitz et al.<sup>870</sup>, conflicted with the amino acid requirements of the Translation process, which was trained using the observed Mycoplasma genetic code<sup>53,168,607</sup>, the reported M. pneumoniae mRNA expression<sup>569</sup>, and the N-end rule<sup>586</sup>. Specifically, Morowitz et al. reported that cysteine was only present in trace amounts, whereas the combination of the genetic code and observed mRNA expression is consistent with low, but not insignificant cysteine incorporation.

First, we manually identified constraints among groups of parameters spread across multiple processes. Among these constraints, we identified equality constraints between the cell chemical composition used to train the flux-balance analysis (FBA) metabolic objective and the expected metabolite requirements of the cellular processes. We also identified inequality constraints among the kinetic rate, expression, and required enzymatic capacity of each enzyme which describe the minimum expression of each gene consistent with all 28 sub-models.

Second, we computationally identified a set of parameter values which (1) satisfy all of these constraints and (2) deviate minimally from their experimentally observed values. Initially, we attempted to rigorously formulate this problem as a non-linear constrained optimization problem, and identify the parameter values which minimize the sum of squared diferences between the adjusted and observed parameter values among all sets of parameters which satisfy the constraints. However, we were unable to find a feasible solution, much less the globally optimal solution, to this optimization problem. Instead, we focused on identifying a mutually consistent set of parameter values, and developed a heuristic procedure that uses the constraints to calculate a consistent set of parameter values from a subset of the parameters. This procedure primarily adjusted the gene expression. The adjusted gene expression correlated highly with that observed by Weiner et $a l . ^ { 5 6 9 } ~ ( R ^ { 2 } = 0 . 6 8$ , see Figure S1A). Section A.7.8 and the FitConstants class provide further discussion of the implementation of the parameter refinement procedure.

## 1.4 Initial Conditions

Cell theory<sup>919</sup> states that all cells are created from old cells, or, more mathematically, that on the time scale of a single-generation, mother and daughter cells are statistically identical. This principle relates the initial and final cell state distributions of the whole-cell model, providing a rigorous way to define the initial cell state distribution in terms of the dynamic model.

We applied this principle in seven steps (see Algorithm S2). First, we developed a method that calculates the expectation value of each cell state variable. Second, we approximated the distribution of each cell state variable by a standard, well-behaved statistical distribution, and set the mean of each distribution to its calculated value. For example, we assumed that the copy number of each RNA and protein species is multinomially distributed, and that the total cell mass is normally distributed. Third, we parameterized the variance of the distribution of each cell state variable and initially set the variance of each distribution to zero. Fourth, we developed the procedure outlined in Algorithm S3 to sample these distributions and set the initial value of each state variable. Fifth, we simulated a population of wild type cells using this cell state initialization procedure and calculated the variance of the final distribution of each cell state variable. Sixth, we set the initial variance of each state variable to its calculated final variance. Finally, we repeated steps five and six until convergence.

<table><tr><td>Algorithm S2 | Initial conditions identification algorithm.</td></tr><tr><td>Initialize the initial cell state variance control parameters:  $\sigma _ { m } \gets 0 , \eta _ { r } \gets 0 , \eta _ { p } \gets 0$ </td></tr><tr><td>repeat Simulate the life cycle of a population of wild type cells using Algorithm S3 to initialize the value of each cell state</td></tr><tr><td>variable</td></tr><tr><td>Randomly segregate the cellular content into two daughter cells</td></tr><tr><td>Calculate the variances of the total cell mass, RNA copy number, and protein copy number states</td></tr><tr><td>Set the values of the initial distribution control parameters of each state equal to that of the final distribution</td></tr><tr><td> $\sigma _ { m } \gets$  standard deviation of the final cell mass distribution  $\sigma _ { r } ^ { 2 }$ </td></tr><tr><td> $\eta _ { r }  \sigma _ { r } ^ { 2 } / N _ { r }$  , where  $N _ { r }$  and are the mean and variance of the final RNA copy number distribution  $\eta _ { p }  \sigma _ { p } ^ { 2 } / N _ { p }$  , where  $N _ { p }$  and  $\sigma _ { p } ^ { 2 }$  are the mean and variance of the final RNA copy number distribution</td></tr></table>

Algorithm S3 | Cell state initialization procedure.

Input: $\sigma _ { m }$ ← standard deviation of the initial total cell mass distribution   
Input: η<sub>r</sub>, η<sub>p</sub> ← RNA and protein copy number distribution initial variance control parameters   
Input: f<sub>r</sub>, f<sub>p</sub> ← reconstructed fractional cell RNA and protein composition   
Input: $e _ { r } , e _ { p } \gets$ expected relative expression of each RNA and protein species   
Input: $w _ { r } , w _ { p }$ ← molecular weight of each RNA and protein species   
Input: $N _ { i } \left( f _ { i } , e _ { i } , w _ { i } \right) \gets f _ { i } m / \left( e _ { i } ^ { \prime } * w _ { i } \right)$ total initial RNA (i =r) and protein (i =p) copy number functions   
Set time ← 0 s   
Set values of external stimuli and metabolites according to Table S3F and S3H   
Set total cell mass, m $ \sim N ( \mu , \sigma _ { m } )$ , and calculate cell volume and shape   
Set the metabolite counts according to the total cell mass and reconstructed cell composition (see Table S3I)   
Initialize the Chromosome state with one methylated chromosome; decrement dNMP counts to maintain cell mass   
Set mature RNA copy numbers according to multinomialRand $( \eta _ { r } N _ { r } , e _ { r } ) / \eta _ { r } ;$ decrement NMP counts   
Set mature protein monomer copy numbers according to multinomialRand $( \eta _ { p } N _ { p } , e _ { p } ) / \eta _ { p } ;$ decrement amino acids   
Form macromolecules by calculating the steady-state of the Macromolecular Complexation process   
Set the RNA Polymerase and Transcript states to a steady-state of the Transcription sub-model   
Set the Ribosome and Polypeptide states to a steady-state of the Translation sub-model   
Set the FtsZ state to a steady-state of the FtsZ Polymerization sub-model with no septal rings   
Set the growth rate and metabolic reaction fluxes to a steady-state of the Metabolism sub-mode   
Set the Host state to a steady-state of the Host Interaction sub-model   
Set the chromosome protein occupancy to a steady-state the chromosome-interacting sub-models

## 1.5 Reconstruction

The M. genitalium whole-cell model was based on a detailed reconstruction of M. genitalium physiology developed from over 900 primary sources, reviews, books, and databases. First, we reconstructed the organi zation of the M. genitalium chromosome including the locations of each gene, transcription unit, promoter, and protein binding site primarily based on studies by Weiner et al.<sup>411</sup>, Güell et al.<sup>418</sup>, and the CMR genome annotation<sup>168</sup>. We also reconstructed the afinity of RNA polymerase for each promoter based on the reported expression<sup>569</sup> and half-life<sup>602</sup> of each RNA species.

Second, we functionally annotated each gene beginning with the CMR<sup>168</sup> annotation. We annotated genes with additional information from the BioCyc<sup>6</sup>, KEGG<sup>113</sup>, NCBI<sup>61</sup>, and UniProt<sup>96</sup> genome annotations. To fill gaps in the reconstructed organism, such as observed reactions without reported enzyme catalysts, and to maximize the scope of the model, we also expanded and refined each gene’s annotation using primary research articles and reviews identified by systematically searching PubMed and Google Scholar for each gene and homologs of each gene. Table S3J lists all functional annotations assigned beyond the CMR annotation. Additionally, we curated the reported essentiality<sup>193</sup> of each gene product.

Next, we curated the structure of each gene product, including the sequence of each protein, the posttranscriptional and post-translational processing and modification of RNA and protein, the signal sequence and localization of each protein, the DNA footprint of each DNA-binding protein, the chaperones and prosthetic groups required to fold each protein, the subunit composition of each protein and ribonucleoprotein complex, and the disulfide bonds of each protein and complex.

After annotating each gene, we categorized the genes into 28 cellular processes. We curated the chemical reactions of each cellular process with particular emphasis on reactions needed to interface the processes. For example, we added several metabolic reactions to provide the metabolites required for RNA modification. We also added metabolic reactions to catabolize modified nucleotides produced by the degradation of modified RNA. We reconstructed the stoichiometry and catalysis of each chemical reaction based on the databases BioCyc<sup>6</sup> and $\mathrm { K E G G ^ { 1 1 3 } }$ , a M. genitalium FBA metabolic developed by Suthers et al.<sup>610</sup>, and hundreds of additional primary research articles. We reconstructed the kinetics of each reaction primarily based on the databases BRENDA<sup>570</sup> and SABIO-RK<sup>100</sup>.

We reconstructed the M. genitalium metabolome based on the substrates and products of the reconstructed chemical reactions, the observed chemical compositions of M. gallisepticum<sup>870</sup> and E. coli<sup>393</sup>, and the reported chemical composition of SP-4 Mycoplasma growth medium<sup>754–759</sup>. We reconstructed the structure of each metabolite based on several metabolomic databases including PubChem<sup>587</sup>. We reconstructed the protein regulatory properties of each metabolite primarily based on DrugBank<sup>847</sup>.

Finally, we calculated the empirical formula, molecular weight, and several other physical properties of each metabolite, RNA, protein, and macromolecular complex using the KnowledgeBase classes, ChemAxon Marvin<sup>594</sup>, and ExPASy ProtParam<sup>585</sup>.

Because M. genitalium is not well-studied, the M. genitalium reconstruction was primarily based on studie of M. genitalium homologs identified by bi-directional best BLAST. Where possible, the M. genitalium reconstruction was based on closely related organisms.

Table S3A-S3S define the reconstructed M. genitalium organism including the structure of every metabolite; the sequence of every RNA and protein; and the stoichiometry, kinetics, and catalysis of every reaction. Table S3T-S3BK describe the how the reconstructed organism was developed, including detailed notes on how the value of each reconstructed property was derived by consensus of all available experimental observations and computational predictions. List S1 lists the principal sources of the M. genitalium reconstruction; Table S3S provides a complete list of all the sources of the reconstruction. Table S2B-S2C list the computationally refined values of the reconstructed cellular composition and gene expression. See Chapter 2 for further discussion of the reconstruction of each cell variable. See Chapter 3 for further discussion of the reconstruction of each cellular process sub-model. See Section 1.3 for further discussion of modeling fitting and computational refinement of the reconstruction.

List S1. Primary sources of the M. genitalium reconstruction.
<table><tr><td>Data source</td><td>Content</td></tr><tr><td>Bernstein et al., 2002602</td><td>mRNA half-lives</td></tr><tr><td>BCyc}</td><td>Genome annotation, metabolic reactions</td></tr><tr><td>BRENDA 570</td><td>Reaction kinetics</td></tr><tr><td>CMR168</td><td>Genome annotation</td></tr><tr><td>Deuerling et al., 200388</td><td>Chaperone substrates</td></tr><tr><td>DrugBank847</td><td>Antibiotics</td></tr><tr><td>Eisen et al., 1999891</td><td>DNA repair</td></tr><tr><td>Endo et al., 2007391</td><td>Chaperone substrates</td></tr><tr><td>Feist et al., 2007558</td><td>Metabolic reactions</td></tr><tr><td>Glass et al., 2006193</td><td>Gene essentiality</td></tr><tr><td>Güell et al., 2009418</td><td>Transcription unit structure</td></tr><tr><td>Gupta et al., 2007280</td><td>N-terminal methionine cleavage</td></tr><tr><td>KEGG113</td><td>Genome annotation, orthology</td></tr><tr><td>Kerner et al., 2005389</td><td>Chaperone substrates</td></tr><tr><td>Krause et al., 2004409</td><td>Terminal organelle assembly</td></tr><tr><td>Lindahl et al., 2000462</td><td>DNA damage</td></tr><tr><td>Morowitz et al., 1962870</td><td>Cell chemical composition</td></tr><tr><td>NCBI Gene61,777</td><td>Genome annotation</td></tr><tr><td>Neidhardt et al., 1990393</td><td>Cell chemical composition</td></tr><tr><td>Peil, 2009105</td><td>RNA modification</td></tr><tr><td>PubChem 587</td><td>Metabolite structures</td></tr><tr><td>SABIO-RK100</td><td>Reaction kinetics</td></tr><tr><td>Solabia754-759</td><td>Media chemical composition</td></tr><tr><td>Suthers et al., 2009610</td><td>Metabolic reactions</td></tr><tr><td>UniProt6</td><td>Genome annotation</td></tr><tr><td>Weiner et al., 2000411</td><td>Promoters</td></tr><tr><td>Weiner et al., 2003569</td><td>mRNA expression</td></tr></table>

## 1.6 Experimental Validation

The M. genitalium whole-cell model was validated by comparing the model’s predictions to three experimental datasets: (1) the essentiality of each M. genitalium gene reported by Glass et al.<sup>193</sup>, (2) the measured growth rates of 12 non-essential M. genitalium single-gene disruption strains, and (3) the cytosolic concentrations of 39 E. coli metabolites reported by Bennett et $a l . ^ { 3 9 2 }$ and curated by Sundararaj et al.<sup>394</sup>. The M. genitalium whole-cell model also reproduces several experimental measurements which were used to train the model including the published cellular composition of M. gallisepticum<sup>870</sup>, the measured RNA composition of E. coli<sup>393</sup>, the reported M. pneumoniae mRNA expression<sup>569</sup>, the observed E. coli mRNA half-lives<sup>602</sup>, and the measured growth rate of wild type M. genitalium.

To validate the model against the observed gene essentiality and the observed disruption strain growth rates, we first simulated the individual disruption of each gene. We ran 5 simulations of each single-gene disruption strain by (1) randomly initializing the cell state using Algorithm S3, (2) deleting the in silico gene, and (3) calculating the temporal evolution of the cell state for the first generation post-disruption. Gene disruption was implemented in two steps: (1) we modeled insertion of a transposon of length zero which reduces the stability of the terminal products of the deleted gene, and set the half-life of the RNA and protein products of the deleted gene to zero; and (2) to more quickly highlight altered phenotypes, we deleted all RNA and protein products of the deleted gene. Next, we calculated the mean predicted mass doubling time, cell cycle length, terminal organelle protein mass, and damaged protein copy number of each disruption strain.

Third, we calculated the mean growth rate of each single-gene disruption strain at successive generations postdisruption. Rather than simulating the complete dynamics of successive generations, which was infeasible due to the significant computational cost of each simulation, we predicted only the growth rate of each disruption strain at successive generations post-disruption by initializing simulations using a modified version of the method described above. (1) We initialized cells using the wild type cell initialization method. (2) We deleted the in silico gene as previously described. (3) To simulate the long-term efects of the gene disruption and dilution resulting from cellular growth and division, we reduced the copy numbers of macromolecules which are normally synthesized by the deleted gene product. (4) We calculated the growth rate using the Metabolism process.

Fourth, we classified each in silico single-gene disruption strain as (quasi-)essential if the predicted first generation cell cycle length was significantly $( P \leq 0 . 0 1 )$ less than that of wild type in silico M. genitalium, if the terminal organelle was protein mass was significantly $( P \leq 0 . 0 1 )$ less than that of wild type in silico M. genitalium, if the predicted damaged protein copy number was significantly $( P \leq 0 . 0 1 )$ greater than that of wild type in silico M. genitalium, or if the growth rate declined over successive generations. We found that the model reproduces the observed gene essentiality with 79% accuracy. Figure 6B of the accompanying manuscript illustrates these distinct disruption strain phenotypes. Figure S2 illustrates the distribution of growth rates among wild type M. genitalium and the quasi-essential and essential single-gene disruption strains. Table S2G lists the predicted growth rate of each disruption strain.

Fifth, we compared the experimentally observed and predicted growth rates of 12 non-essential single-gene disruption strains (see Figure 7A of the accompanying manuscript and Table S1), and found that the model correctly predicts the measured growth rates of 67% of the disruption strains.

To validate the model against the Bennett et al.<sup>392</sup> and Sundararaj et al.<sup>394</sup> datasets, we calculated the mean concentration of each cytosolic metabolite in a population of 128 wild type cells. Figure 2E of the accompanying manuscript and Table S2E compare the predicted and measured concentrations of 39 cytosolic metabolites, illustrating that 70% of the model’s predictions are statistically consistent with the Sundararaj et al. dataset. The model doesn’t reproduce the Bennett et al. dataset, and interestingly, there is significant disagreement between the Bennett et al. and Sundararaj et al. datasets.

## 1.7 Computational Implementation

The whole-cell model was implemented in MATLAB, and consisted primarily of the main Simulation class and one class for each cellular state and process. The computational correctness of the whole-cell model algorithm was validated using unit testing. The M. genitalium reconstruction was stored using a modified version of the BioWarehouse schema<sup>918</sup> in a MySQL relational database. The knowledge base was viewed and edited using a web-interface implemented in PHP. Several KnowledgeBase classes represented the knowledge base in MATLAB. Appendix A provides further discussion of the whole-cell model architecture and it’s computational validation.

## 1.8 Computational Simulation & Analysis

We used the whole-cell model to simulate 192 wild type cells and 3,011 single-gene deletants. All simulations were performed with MATLAB R2010b on a 128 core Linux cluster. The predicted dynamics of each cell was logged at each time point and subsequently analyzed using MATLAB. Appendix A provides further discussion of the execution, logging, and analysis of the whole-cell model.

## Chapter 2

# Cellular State Methods

The whole-cell model used 16 state variables to represent the instantaneous configuration of M. genitalium and integrate the 28 modeled cellular processes. The 16 state variables represented seven areas of cellular physiology: (1) copy numbers of metabolites, RNA and proteins, (2) metabolic reaction fluxes, (3) nascent DNA, RNA, and protein polymers, (4) molecular machines, (5) cell-level properties, including mass, volume and shape, (6) nascent polymers of DNA, RNA and protein, and (7) time. This chapter provides detailed discussions of the mathematics and computational implementation of each state variable.

The Metabolite, Rna, Protein Monomer, and Protein Complex states represented the copy number of each metabolite, RNA, protein monomer, and macromolecular complex. The complement of metabolite species was indirectly reconstructed by reconstructing the chemical reactions of each cellular process. The RNA complement was primarily reconstructed from the M. genitalium genomic annotation<sup>168</sup>, the experimentally defined operon structure of M. pneumoniae<sup>418</sup>, and the reported complement of E. coli RNA polycistronic cleavages and non-coding RNA modifications. The protein complement was primarily reconstructed from the predicted localization and signal sequence of each protein gene product (see Table S3AM-S3AO), the observed chaperone interactions of E. coli<sup>388,389</sup> and B. subtilis<sup>391</sup>, the observed complement of M. genitalium and M. pneumoniae protein modifications<sup>94,277,282,283,672</sup>, the reported N-terminal methionine cleavage of Shewanella oneidensis MR-1<sup>280</sup>, and the inferred subunit composition of each macromolecular complex (see Table S3AS).

The Metabolic Reaction state recorded the predicted flux of each metabolic reaction. The M. genitalium metabolic network was reconstructed as described in Section 3.10.

The Chromosome, Transcript, Polypeptide, and FtsZ Ring states represented the configurations of the chromosome, nascent RNA and protein polymers, and FtsZ septal ring. The Chromosome state represented the polymerization, protein occupancy, and modification status of the chromosomes. The M. genitalium chromosome was sequenced by Fraser et al.<sup>57</sup>. Protein binding sites and DNA footprints were reconstructed from the primary literature and several databases (see Table S3M and S3N). DNA modification sites were predicted based on the reported DNA motif of the MunI methylase<sup>96</sup>. The Transcript and Polypeptide states represented the sequence of each nascent RNA transcript and polypeptide. The sequence of each RNA and protein species was reconstructed as described in Chapter 3. The FtsZ Ring state represented the configuration of the FtsZ septal ring. The structure of the FtsZ septal ring was reconstructed based on the Li et al. iterative pinching model<sup>611</sup>.

The RNA Polymerase and Ribosome states represented the detailed configuration of each RNA polymerase and ribosome. The RNA Polymerase state represented the status – free, non-promoter bound, promoterbound, or actively transcribing – of each RNA polymerase molecule, and the chromosomal location and direction of each DNA-bound RNA polymerase. The afinity of RNA polymerase for each promoter was primarily reconstructed from the observed expression of each RNA gene product<sup>569</sup> and the observed halflife of each E. coli mRNA<sup>602</sup>. The genetic code was reconstructed based on that of M. pneumoniae<sup>53</sup>.

The Mass state represented the total cell mass. The Geometry state represented the cell shape and volume. The average cell size, density, and mass were reconstructed from studies by Baldwin et $a l . ^ { 5 5 { \bar { 3 } } }$ , Bray<sup>554</sup>, and Zhao et al.<sup>555</sup>.

The Metabolite, Stimulus, Host, and Geometry states represented the configuration of the external environment, including the extracellular copy number of each metabolite which was reconstructed as described in Section 3.10. The Stimulus state represented the temperature, the fluxes of six types of radiation, and the status of three common experimental stress conditions. Table S3F describes the reconstruction of the Stimulus state. The Host state represented four properties of the host human urogenital epithelium: (1) M. genitalium adherence, (2) activation of Toll-like receptors 1, 2, and 6, (3) activation of the host transcriptional regulator NF-κB, and (4) activation of the host inflammatory response. The Geometry state represented the volume of the extracellular environment.

Finally, the Time state represented the time elapsed from the beginning of the simulation.

## 2.1 Chromosome

## Biology

Chromosomes encode the structure and function of every RNA and protein, and thereby control cellular behavior. Due to their critical function and large size, cells dedicate considerable resources to chromosome replication, maintenance, and compaction. This state represents the polymerization, winding, modification, protein occupancy, and (de)catenation status of the chromosome(s).

## Reconstruction

## Structure and Organization

The reconstructed M. genitalium chromosome contains 525 genes based on the Comprehensive Microbial Re source (CMR) genomic annotation<sup>168</sup> (see Table S3J) organized into 335 transcription units based on the M. pneumoniae operon organization experimentally defined by Güell et al.<sup>418</sup> and the M. genitalium promoters computationally predicted by Weiner et al.<sup>411</sup> (see Table S3U). The reconstructed genome also contains 17 transcriptional regulatory elements based on 15 studies and databases<sup>96,110,112,186,196,418–420,433–438,505</sup> (see Table S3P), 2,283 DnaA binding sites computationally identified based on the consensus binding motif reported by Grimwade et al.<sup>744</sup> and Speck et al.<sup>745</sup> (see Table S3L), 760 MunI restriction/modification (R/M) sites computationally identified based on the reported MunI binding motif<sup>96</sup> (see DNA Repair process), and 19 short tandem repeats identified by Ma et al.<sup>183</sup> and Washio et $\bar { a } l . ^ { 1 8 4 }$ (see Table S3V). Additionally, the location of the replication origin was reconstructed based on studies by Lobry<sup>880</sup>, Jensen et al.<sup>517</sup>, and others<sup>521,848</sup>, and the predicted DnaA box sites. Finally, the reconstructed steady-state superhelicity is based on the observed equilibrium helical repeat length of plasmid DNA<sup>879</sup> and the observed superhelicity of E. coli DNA<sup>749</sup>.

## Protein Binding

The binding motif and footprint of each DNA-binding protein was reconstructed from several experimental studies<sup>85,461,517,521,709,710,712,717,719–726,728,735–737,743,748</sup> and the databases 3D-Footprint<sup>696</sup>, NDB<sup>697</sup>, and ProNIT<sup>703</sup>. DNA-bound protein displacement reactions were assembled describing which proteins each protein species is able to displace from the chromosome (see Table S3O). Functionally, displacement of DNA-bound proteins enables proteins to access the chromosome and fulfill their chromosomal replication or maintenance role. The afinity of RNA polymerase for each promoter was first reconstructed from the observed RNA composition of E. coli<sup>393</sup> (see Table S3U), the expression of each M. genitalium mRNA reported by Weiner et $a l . ^ { 5 6 9 }$ (see Table S3W), the half-life of each E. coli mRNA reported by Bernstein et al.<sup>602</sup> (see S3Y, the observed amino acid composition of M. gallisepticum<sup>870</sup>, and the Mycoplasma genetic code<sup>53,168,607</sup> (see Table S3X). Subsequently, the afinity of RNA polymerase for each promoter was fit to match the additional data used to train the 28 modeled cellular processes (see Section 1.3).

## Computational Representation

This state represents the polymerization, winding, modification, and protein occupancy of each nucleotide of each strand of each copy of the M. genitalium chromosome, and the (de)catenation status of the two sister chromosomes following replication. List S2 summarizes the mathematical representation of the M. genitalium chromosome(s) including the size and type of each variable.

Mathematically, each quantity except winding, base and sugar-phosphate modification, protein occupancy and catenation, is represented as a 3-dimensional Boolean tensor. Winding is represented as a 3-dimensional real tensor which indicates the linking number density of each nucleotide. Base and sugar modification are represented as 4-dimensional tensors which indicate the chemical identity $l = \{ 1 . . M \}$ of each nucleotide, where $M = 7 2 2$ is the number of distinct metabolite species represented by the Metabolite state. Protein monomer and complex occupancy are represented as 4-dimensional tensors which indicate the identity, $l = \{ 1 . . B ^ { m } \}$ and $l = \{ 1 . . B ^ { c } \}$ respectively, of the protein bound at each nucleotide, where $B ^ { m } = 4 8 2$ and $B ^ { c } = 2 0 1$ are the numbers of distinct protein monomer and complex species represented by the Protein Monomer and Protein Complex states. (De)catenation is represented as a Boolean scalar.

List S2. Mathematical representation of nucleotide $i = \{ 1 . . L \}$ of strand $j = \{ 1 . . 2 \}$ of chromosome copy $k = \{ 1 . . 2 \}$
<table><tr><td>Physical Property</td><td>Symbol</td><td>Size</td><td>Type</td><td></td></tr><tr><td>Polymerization</td><td> $p _ { i j k }$ </td><td> $\overline { { L \times 2 \times 2 } }$ </td><td>Boolean</td><td></td></tr><tr><td>Winding</td><td> $w _ { i j k }$ </td><td> $L \times 2 \times 2$ </td><td>Real</td><td></td></tr><tr><td>Modification</td><td></td><td></td><td></td><td></td></tr><tr><td>Gap site</td><td> $m _ { i j k } ^ { g }$ </td><td> $L \times 2 \times 2$ </td><td>Boolean</td><td></td></tr><tr><td>Abasic site</td><td> $m _ { i j k } ^ { a }$ </td><td> $L \times 2 \times 2$ </td><td>Boolean</td><td></td></tr><tr><td>Sugar-phosphate</td><td> $m _ { i j k l } ^ { p }$ </td><td> $L \times 2 \times 2 \times M$ </td><td>Boolean</td><td></td></tr><tr><td>Base</td><td> $m _ { i j k l } ^ { \upsilon }$ </td><td> $L \times 2 \times 2 \times M$ </td><td>Boolean</td><td></td></tr><tr><td>Intrastrand cross link</td><td> $m _ { i j k } ^ { c }$ </td><td> $L \times 2 \times 2$ </td><td>Boolean</td><td></td></tr><tr><td>Strand break</td><td> $m _ { i j k } ^ { s }$ </td><td> $L \times 2 \times 2$ </td><td>Boolean</td><td></td></tr><tr><td>Holliday junction</td><td> $m _ { i j k } ^ { n }$ </td><td> $L \times 2 \times 2$ </td><td>Boolean</td><td></td></tr><tr><td>Protein occupancy</td><td></td><td></td><td></td><td></td></tr><tr><td>Monomer</td><td> $b _ { i j k l } ^ { m }$ </td><td> $L \times 2 \times 2 \times B ^ { m }$ </td><td>Boolean</td><td></td></tr><tr><td>Complex</td><td> $b _ { i j k l } ^ { c }$ </td><td> $L \times 2 \times 2 \times B ^ { c }$ </td><td>Boolean</td><td></td></tr><tr><td>Catenation</td><td>S</td><td> $1 \times 1$ </td><td>Boolean</td><td></td></tr></table>

## Integration

The Metabolite state describes the identity of each modified base and sugar-phosphate. The Protein Monomer and Protein Complex states represent the total DNA-bound copy number of each protein monomer and macromolecular complex. For computational eficiency, the RNA Polymerase state redundantly represents the chromosomal location of each bound RNA polymerase. The mass of the chromosome(s), including all modifications and all DNA-bound proteins, is included in the cell mass calculated by the Mass state.

Ten processes access and modify the Chromosome state. The Replication Initiation process models DnaA DNA-binding and formation of the oriC DnaA complex which promotes replication initiation. The Replication process models bidirectional DNA polymerization from the oriC, continuously on the leading strand and discontinuously on the lagging strand, and Okazaki fragment ligation. The Chromosome Segregation process models sister chromosome decatenation following successful chromosome replication. The Cytokinesis process models cell division following successful decatenation. The Chromosome Condensation and DNA Supercoiling processes model SMC- and supercoiling-mediated chromosome compaction. The DNA Damage process models stochastic and radiation- and chemically-induced DNA damage. The DNA Repair process models three DNA repair pathways – base excision repair, nucleotide excision repair, and homologous recombination. The DNA Repair process also models methylation and restriction of MunI (MG184) restriction/modification sites. Finally, the Transcriptional Regulation and Transcription processes model the binding of transcription factors and RNA polymerases to promoters and the synthesis of RNA.

## Initial Conditions

First, the Chromosome state is initialized with one supercoiled and fully methylated chromosome,

$$
\begin{array} { r l } & { P _ { \mathrm { e f f } } ^ { \mathrm { e f f } } = 1 \sqrt { 1 - \xi } , } \\ & { R _ { \mathrm { e f f } } = 0 \ : \forall i , j } \\ & { \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : \times _ { \mathrm { e f f } } = \ : \forall i , j \ : \ : \ : \forall \ : \ : \ : } \\ & { \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \times _ { \mathrm { e f f } } = \ : \forall \ : i , j \ : \ : } \\ & { \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : \times _ { \mathrm { e f f } } = \ : \forall i , j \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : \times _ { \mathrm { e f f } } = \ : \ : \forall i , j \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : \ : \times _ { \mathrm { e f f } } = \ : \ : \forall \ : \ : \ : \mathrm { h e f } \ : \ : \ : \ : \ : \mathrm { s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e ~ s i m e } } \\ & { \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : \ : \times _ { \mathrm { e f f } } = \ : \ : \forall \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : \ : } \\ & { \ : \ : \ : \ : \ : \ : \ : } \\ &  \ : \ : \ : \ : \ : \ : \times _ { \mathrm { e f f } } = \ : \forall \ : \ : \ : \end{array}
$$

where $L = 5 8 0 0 7 6 \mathrm { n t }$ is the length of the M. genitalium chromosome, $\sigma _ { s s } = - 0 . 0 6$ is the observed bacterial steady-state superhelicity<sup>749</sup>, and $h = 1 0 . 5 ~ \mathrm { n t l k ^ { - 1 } }$ is the observed equilibrium helical repeat length<sup>879</sup>.

Second, the Protein Monomer and Protein Complex states initialize the total copy number of each protein species. Finally, the Chromosome Condensation, DNA Supercoiling, Replication Initiation, Transcriptional Regulation, and Transcription processes initialize the protein occupancy of the chromosome.

## Fitting

The chemical composition of M. genitalium and the objective of the flux-balance analysis metabolic model were fit to match the mass and dNMP composition of the M. genitalium chromosome (see Section 1.3 and 2.5). The afinity of RNA polymerase for each promoter was fit to provide the gene products required by the 28 modeled processes to reproduce the observed 9 h M. genitalium mass doubling time (see Section 1.3). The oriC DnaA DNA-binding cooperativity was fit to match our intuition for the duration of the replication initiation cell cycle phase (see Section 3.19). The expression and activity of DNA gyrase and topoisomerse I were balanced to match the observed steady state superhelical density (see Section 3.6).

## 2.2 FtsZ Ring

## Biology

Cytokinesis is the division of a cell into two daughter cells. M. genitalium contains a protein called FtsZ that assembles into long filaments that are implicated in cell pinching. These filaments bind to the membrane at the midline of the cell<sup>217</sup>. FtsZ is a GTPase, and when the GTPs bound in a membrane-bound FtsZ filament hydrolyze to GDP, the filaments bend constricting the membrane<sup>421</sup>. We use a geometric model of iterative filament bending modified from a model proposed by Li et $a l . ^ { 6 1 1 }$ . See the Cytokinesis process and Schematic S6, for more details about this model. In summary, the FtsZ ring at the midline of the cell can exist in many states of various numbers of filaments in the bent and straight configurations. The purpose of this state class is to keep track of the state of the FtsZ ring across timesteps.

## Reconstruction

In our model, the FtsZ ring is represented as a polygon of FtsZ filaments. As the circumference of the midline of the cell (C) decreases with time, the number of edges in the inscribed FtsZ polygon decreases. The FtsZ filaments are of a fixed length (l) of 40 nm<sup>217</sup>.

## Computational Representation

The number of edges in the polygon (E) is determined by the maximum number of edges of length l that can be inscribed in the given cell circumference. (The use of a fixed filament length is a simplification. See the Cytokinesis and FtsZ Polymerization processes for more details about the assumptions used.) This state class computes the number of edges in the FtsZ polygon using the inscribed polygon formula and the current cell midline diameter (d):

$$
E = \frac { \pi } { \arcsin ( \frac { l } { d } ) }\tag{S1}
$$

The filaments may not perfectly inscribe the cell circumference, and so we round down, such that E only accounts for full filaments in the FtsZ ring.

The Cytokinesis process determines how many straight and/or bent filaments reside at each edge of the FtsZ polygon. At each edge, any of the following occupancies are possible:

• 1 straight filament

• 2 straight filaments

• 1 bent filament

• 2 bent filaments

• 1 bent filament and 1 straight filament

• 1 bent filament and 2 straight filaments

The FtsZ Ring state class keeps track of the filament occupancy of each edge. As the filament occupancy in a timestep is highly dependent on the occupancy at the previous timestep, the tracking of the state of the FtsZ ring is extremely important in the time evolution of Cytokinesis.

## Integration

The FtsZ Ring state class reads the diameter of the cell’s midline (d) from the Geometry state class.

The Cytokinesis process class reads the number of FtsZ ring edges (E) and the filament occupancy at each edge from the FtsZ Ring state class. The Cytokinesis process class updates the filament occupancy at each edge, and this is stored in the FtsZ Ring state class.

## Initial Conditions

An FtsZ ring is not assembled at the beginning of the simulation. Therefore, no initialization steps are required for this state class.

## 2.3 Geometry

## Biology

While M. genitalium divides by binary fission similarly to other bacterial species, its non-uniform shape, lack of cell wall, and lack of complete division machinery make its growth and division distinctive from most other bacteria. M. genitalium has a flask/pear-like shape, with a protruding adhesion structure called the terminal organelle. This flask-like shape is rather fluid due to the lack of a cell wall<sup>872</sup>.

## Reconstruction

Since the growth and division of M. genitalium are not well understood, we chose to model the cell as varying from a spherical to short rod shape. The cell is modeled as a cylinder with two hemispherical caps, and growth is modeled in the cylinder length. Once cell pinching commences at the midline of the cell, the shape and size of a “septum region” is also modeled. The Geometry state class calculates and keeps track of the physical shape of the cell including its width, length, volume, and surface area. This state also keeps track of the progress of cytokinesis, and the completion of cytokinesis is the trigger to end the entire simulation.

## Computational Representation

The Geometry state uses a set of geometric equations to calculate the shape of the cell, given the width (w), density (ρ), and cytokinesis progress of the cell. The state houses the calculations of cell length (l), volume (V ), surface area (SA), and progress of cell pinching. The geometric representation requires us to assume that the cell density and cell width are constant across the cell cycle. Various sources have indicated that the volumetric density of a cell remains constant overtime<sup>874,875</sup>. The cell density used is that of E. coli, which has been estimated as $1 1 0 0 \mathrm { g / L ^ { 5 5 3 } }$ . Several sources have described the width of a rod-shaped bacterial cell as remaining approximately constant across the cell cycle and across cell divisions<sup>873</sup>. The cell width is calculated based on the initial cell mass (m<sub>0</sub>) and density and the assumption that the cell is a sphere. The initial cell mass was fit to result in the measured M. genitalium cell width of 200 nm<sup>225</sup>. The general geometric equations to represent the shape of a cell are inspired by Domach et al.<sup>305</sup>. These geometric equations use the fixed width and fixed cell density assumptions to calculate all the other aspects of the cell geometry.

## Cell Geometry Calculations

The mass (m) and density (ρ) enable calculation of the volume at all time points:

$$
V = { \frac { m } { \rho } }\tag{S2}
$$

Before cell pinching starts

The cell is modeled as a cylinder (length: ${ { l } _ { c } } ,$ diameter: w) with two hemispherical caps (diameter: w). We use the cell volume to calculate the cell length and surface area:

$$
\begin{array} { r l r l } { { 2 } { \mathrm { ~ h e m i s p h e r e s ~ } } } & { { } } & { { \mathrm { c y l i n d e r } } } \end{array}
$$

$$
\begin{array} { r l } { V = } & { { } \stackrel { \displaystyle \overbrace { \frac { 1 } { 6 } \pi w ^ { 3 } } } { \overbrace { 6 } } + \frac { 1 } { 4 } \pi w ^ { 2 } l _ { c } } \end{array}\tag{S3}
$$

$$
\mathrm { 2 \ h e m i s p h e r e s ~ } \quad \mathrm { c y l i n d e r }
$$

$$
l = \ \overbrace { w } ^ { \mathrm { ~ \tiny ~ { ~ m e r } ~ } } + \overbrace { l _ { c } } ^ { \mathrm { ~ \tiny ~ { ~ \chi ~ } ~ } }\tag{S4}
$$

$$
= w + { \frac { 4 } { \pi w ^ { 2 } } } \left( V - { \frac { 1 } { 6 } } \pi w ^ { 3 } \right)\tag{S5}
$$

$$
\begin{array} { r l r } { { 2 } { \mathrm { ~ h e m i s p h e r e s ~ } } } & { { } { \mathrm { c y l i n d e r } } } \end{array}
$$

$$
\begin{array} { r l r } { S A = } & { { } \widehat { \pi w ^ { 2 } } } & { + \widehat { \pi w l _ { c } } } \end{array}\tag{S6}
$$

## After cell pinching starts

Once cell pinching commences at the midline of the cell, there is a “septum region” as well (Schematic S1). Here the cylinder length (l<sub>c</sub>), is the combined length of the two cylinders. The septum length (s) is the length from the cell midpoint to the edge of the septum region. This septum length is calculated from the “pinched diameter” property that is calculated in the Cytokinesis Process. Each half of the septum volume is calculated as the area of two quarter circles (radius: s) and one rectangle (width: s, height: w − 2s), integrated around the midline cylindrically (see Schematic S2). We use the cell volume to calculate the cell length and surface area:

$$
\begin{array} { r l } { V = { } } & { { } { \displaystyle \overbrace { { \frac { 1 } { 6 } } \pi w ^ { 3 } } ^ { \mathrm { ~ } } } + { \displaystyle \overbrace { { \frac { 1 } { 4 } } \pi w ^ { 2 } l _ { c } } ^ { \mathrm { ~ } } } + { \displaystyle \overbrace { { \frac { s \pi } { 2 } } \left( \left( 8 s ^ { 2 } - 4 s w + w ^ { 2 } \right) + s \pi \left( w - 2 s \right) - { \frac { 4 } { 3 } } s ^ { 2 } \right) } ^ { \mathrm { ~ } } } } \end{array}\tag{S7}
$$

2 cylinders septum region

$$
l = \widehat { \textbf { \textit { w } } } + \widehat { \textbf { \textit { l } } _ { c } } + \widehat { \textbf { \textit { 2 s } } }\tag{S8}
$$

$$
= w + \frac { 4 } { \pi w ^ { 2 } } \left( V - \frac { 1 } { 6 } \pi w ^ { 3 } - \left( \frac { s \pi } { 2 } \left( \left( 8 s ^ { 2 } - 4 s w + w ^ { 2 } \right) + s \pi \left( w - 2 s \right) - \frac { 4 } { 3 } s ^ { 2 } \right) \right) \right) + 2 s\tag{S9}
$$

$$
S A = \overbrace { \pi w ^ { 2 } } ^ { 2 { \mathrm { ~ h e m i s p h e r e s } } } + \overbrace { \pi w l _ { c } } ^ { 2 { \mathrm { ~ c y l i n d e r s } } } + \overbrace { 4 \pi s \left( w - s \right) } ^ { \mathrm { s e p t u m \ r e g i o n } }\tag{S10}
$$

Once the pinched diameter is zero, this state records that the cell has divided, and this determines the end point of the simulation.

![](images/bec6463472d80a7c6dec105f36debc92d581a897912b20432999f380061374d4.jpg)  
Schematic S1. Model representation of cell geometry.

![](images/d14723319d81e00d79e032bafb9cc95171f14f2c630fa8966648ceb6fc6bfc2c.jpg)  
Schematic S2. Representation of volume of septum region.

## Integration

The Geometry state class obtains the initial mass of the cell (to determine the cell width) from the Mass state class. It also obtains the mass of the cell from the Mass state class at all time points to determine the cell volume.

The Metabolism, Protein Activation, Replication Initiation, and FtsZ Polymerization process classes all obtain the cell volume from the Geometry state class. The Cytokinesis process class reads the pinched diameter from the Geometry state class, and sends back the updated pinched diameter.

## Initial Conditions

The initial cell volume is calculated based on the initial cell mass (m<sub>0</sub>) and density (ρ). The initial cell width is calculated from the volume and the assumption that the cell is a sphere. All of the other parameters describing cell geometry are evaluated from the mass, volume, density, and width.

## 2.4 Host

## Biology

As discussed in Section 3.8, the M. genitalium terminal organelle is believed to mediate attachment to the human urogenital epithelium and enable its parasitic lifestyle. Upon attachment, lipoproteins are believed to activate host Toll-like receptors (TLRs) 1, 2, and 6, the host transcriptional regulator NF-κB, and ultimately the host inflammatory response. This state represents the instantaneous configuration of the human host. The Host Interaction process describes the host response to M. genitalium.

## Reconstruction

Section 3.8 describes the reconstruction of the interaction of M. genitalium with its human host.

## Computational Representation

This state uses six Boolean variables to represent the instantaneous configuration of the human host:

• Adherent – true if M. genitalium is attached to its human host and false otherwise.

• TLR 1 activation – true if TLR receptor 1 is active and false otherwise.

• TLR 2 activation – true if TLR receptor 2 is active and false otherwise.

• TLR 6 activation – true if TLR receptor 6 is active and false otherwise.

• NF-κB activation – true if NF-κB is active and false otherwise.

• Inflammatory response activation – true if the host inflammatory response is active and false otherwise.

## Integration

None of the other 15 states directly interact with the Host state. The Host Interaction process completely determines the initial conditions and temporal dynamics of all six Boolean variables represented by this state.

## Initial Conditions

As discussed in Section 3.8, this state is initialized to the steady-state of the host-interaction dynamic model.

## 2.5 Mass

## Biology

Cells are composed primarily of water, DNA, RNA, and protein enclosed in a bilipid membrane. The Metabolite, Chromosome, Rna, Protein Monomer, and Protein Complex states represent the detailed molecular composition of M. genitalium. The Mass state calculates the total cell mass from those states. The total cell mass is used as a proxy for membrane surface area in several processes which are based on mathematical models originally developed outside our integrated whole-cell modeling framework without calculations of the membrane surface area.

## Reconstruction

The mass and chemical composition of M. genitalium were reconstructed based on an extensive review of the primary literature (see Table S3I, S3AR-S3BE) and fit to match the 28 modeled cellular processes. First, the average initial M. genitalium cell mass (13.1 fg) and dry mass (3.93 fg) were self-consistently calculated assuming a spherical geometry with 200 nm diameter<sup>555</sup>, 1.1 g ml<sup>−1</sup> density<sup>553</sup>, and 70% water composition by mass<sup>554</sup>. Note this is comparable to the 18.9 fg M. genitalium cell mass reported by Morowitz<sup>869</sup>. Second, the molecular composition of the dry mass was hierarchically reconstructed:

1. The M. genitalium dry mass was divided into eight classes – DNA/dNMPs, RNA/NMPs, protein/amino acids, lipids, carbohydrates, polyamines, vitamins & cofactors, and ions.

2. The fractional mass (see Table S3AS) and molecular composition (see Table S3AU-S3BE) of each class was reconstructed from the literature.

3. The complete molecular composition of M. genitalium was assembled (see Table S3I and S3AT).

4. The dry mass composition was fit to match the 28 modeled cellular processes as described below and in Section 1.3.

## Computational Representation

This state calculates the total cell mass. The total cell mass is equal to the sum of that represented by the Chromosome, Rna, Protein Monomer, Protein Complex, Transcript, Polypeptide, and Metabolite states.

## Integration

This state interacts with the Geometry state which calculates the cell shape, surface area, and volume from the calculated cell mass and observed density. None of the processes directly modify the Mass state. The Metabolism process uses the cell mass to bound the rates of exchange reactions. The Replication Initiation process models DnaA-ADP reactivation to DnaA-ATP as a function of membrane lipid mass. The Metabolism and Replication Initiation processes use the cell mass rather than the cell volume because these processes are based on mathematical models that were originally developed outside our whole-cell modeling framework without more detailed calculations of the membrane surface area.

## Initial Conditions

The cell mass is hierarchically initialized. First, the total cell mass is initialized according to a normal distribution with mean 13.1 fg and standard deviation 0.66 fg. The mean initial cell mass was set to the reconstructed value. The variance was fit to match that of the predicted final cell mass following cell division. Second, the total cell mass is divided among individual metabolites according to the reconstructed chemical composition (see Section 2.7). Third, the Chromosome, Rna, Protein Monomer, Protein Complex, Transcript, and Polypeptide states are initialized as functions of the metabolite copy numbers, and the metabolite copy numbers are decremented to maintain the initial cell mass.

## Fitting

The mean initial cell mass was fit to the reconstructed value. The variance was fit to match that of the predicted final cell mass following cell division.

Cellular composition is the balance of the production and usage of molecules by cellular processes. Consequently, it was necessary to reconcile the reconstructed cellular composition with that predicted by the 28 modeled cellular processes. See Section 1.3 for further discussion. First, the DNA dry mass fraction, including both chromosomal DNA and free dNTP, was increased 322% to be consistent with the predicted mass of the chromosome and the free dNTP pool. The predicted chromosome mass accounted for the observed chromosome sequence<sup>182</sup>, predicted modifications (see DNA Repair process), and predicted time-average copy number (see Replication, Replication Initiation, and Metabolism processes). The predicted free dNTP pool accounted for the free dNTPs needed support the observed 9 h M. genitalium mass doubling time. Second, the RNA dry mass fraction, including both RNA and free NTPs, was increased 39% to be consistent with the amounts of m-, r-, s-, and tRNA needed to support the observed 9 h mass doubling time. The NMP composition of the RNA fraction was set equal to that predicted by the expression, sequence, and modification of each RNA species (see Transcription, RNA Processing, and RNA Modification processes). Third, the vitamin & cofactor and ion dry mass fractions were increased to match the amounts of vitamins, cofactors, and ions needed for protein folding and catalysis (see Protein Folding process). Finally, the protein dry mass fraction, including both proteins and free amino acids, was decreased 23% to ofset the increased DNA and RNA mass fractions. The amino acid composition of the protein fraction was set equal to that predicted by the expression, sequence, and modification of each protein species (see Translation, Protein Processing I, Protein Processing II, and Protein Modification processes).

## 2.6 Metabolic Reaction

## Biology

Cells grow by importing nutrients from the external environment and using those nutrients to construct macromolecules. The Metabolism process models the dynamics of the 645 transport and chemical reactions which provide the metabolic building blocks required for macromolecular synthesis and drive cellular growth. Table S3O lists the reconstructed transport and chemical reactions.

## Reconstruction

The M. genitalium metabolic network was reconstructed based on extensive review of the primary literature, several databases, and the metabolic demands of all of the processes. See Section 3.10 for further discussion.

## Computational Representation

This state records the instantaneous flux of each metabolic reaction in reactions per second as a floating point vector. This state also records the instantaneous cellular growth rate predicted by the Metabolism process in cells per second as a floating point scalar.

## Integration

None of the other 15 states directly interact with the Metabolic Reaction state. The Metabolism process calculates the flux of each metabolic reaction and the total cellular growth rate using flux-balance analysis (FBA). The Metabolism process uses the predicted fluxes to update the copy number of each metabolite.

## Initial Conditions

The Metabolism process initializes the flux of each metabolic reaction and the total cellular growth rate to a steady-state of the FBA model.

## Fitting

The FBA objective was set to the reconstructed M. genitalium chemical composition (see Mass and Metabolite states and Metabolism process). The cellular growth rate was fit to match the observed 9 h M. genitalium mass doubling time using a modified version of minimization of metabolic adjustment (MOMA)<sup>876</sup> (see Section 1.3 and Metabolism process)

## 2.7 Metabolite

## Biology

The M. genitalium model accounts for the dynamics of 722 distinct metabolites (see Table S3G) which serve many important functions in over 1,100 chemical reactions across three compartments – cytosol, membrane, and extracellular space. First, cells use nucleic and amino acids to synthesize DNA, RNA, and protein. Cells also use ions and other prosthetic groups to stabilize macromolecules. Second, cells use small molecule bonds and gradients to store energy and drive cellular processes. In particular, cells drive many energetically unfavorable reactions through hydrolysis of the high energy intermediates ATP and GTP. Third, cells use coenzyme functional moieties to facilitate chemical catalysis. Additionally, cells use small molecules such as Ca<sup>2+</sup>, ATP, and (p)ppGpp for communication and regulation. Finally, cells use small molecule antibiotics to defend against predators and attack prey.

## Reconstruction

The M. genitalium metabolite complement was indirectly reconstructed by reconstructing the chemical reactions of each of the 28 modeled cellular processes. Table S3G lists the 722 reconstructed metabolites.

## Metabolite Physical Properties

The empirical formula and structure of each metabolite was curated based on an extensive review of the primary literature including two genome-scale metabolic models of M. genitalium<sup>610</sup> and E. coli<sup>558</sup>, and the databases BioCyc<sup>6</sup>, ChEBI<sup>593</sup>, Delta Mass<sup>589</sup>, FindMod<sup>590</sup>, KEGG<sup>113</sup>, LIPID MAPS<sup>588</sup>, Modomics<sup>267</sup>, PubChem<sup>587</sup>, RESID<sup>592</sup>, and UniMod<sup>591</sup>. The molecular weight, van der Waals volume, pI, logP, and logD of each metabolite was computed using ChemAxon Marvin<sup>594</sup>. Table S3G lists the physical properties of each metabolite.

## Metabolite Regulatory Properties

The regulatory properties of several antibiotics were reconstructed from the primary literature and the database DrugBank<sup>847</sup>. See Protein Activation process for further discussion.

## Cellular Chemical Composition

The molecular composition of M. genitalium was reconstructed based on an extensive review of the primary literature. See Section 2.5 for further discussion.

## Extracellular Medium Chemical Composition

M. genitalium was cultured in complex Spiroplasma medium #4 (SP-4 medium)<sup>878</sup> for all experiments presented in this study. Accordingly, the chemical composition of the in silico external environment modeled that of SP-4 medium. Because the chemical composition of SP-4 medium is undefined, the composition of in silico medium was reconstructed based on the characterized composition of each SP-4 medium component<sup>754–762</sup> (see Table S3BJ), and supplemented with additional metabolites to support in silico growth. Addition of supplemental metabolites was guided by the Metabolism process and by the M. pneumoniae minimal medium defined by Yus et al.<sup>614</sup>. Table S3BI lists the composition of the in silico medium.

## Computational Representation

This state represents the copy number of each metabolite in each of 3 compartments – cytosol, membrane, and extracellular space – as an integer matrix.

## Integration

At each time step of the simulation, the Simulation object simulates an M. genitalium cell culture incubator which maintains the extracellular partial pressures of carbon dioxide and oxygen by setting the dissolved extracellular copy numbers of these gases. Table S3BI lists the simulated partial pressures of carbon dioxide and oxygen. To satisfy the assumption that each process is independent on the time scale of the 1 s simulation time step, and because many metabolite species participate in multiple processes, the Simulation object also allocates shared metabolites among processes at each time step. See Section 1.3 for further discussion.

Cytosolic- and membrane-localized metabolites are included in the cell mass calculated by the Mass state. The Metabolism process models the import of extracellular nutrients into the cytosol and membrane, the conversion of those metabolites into the precursors of DNA, RNA, protein, and lipids, and the export of byproducts into the extracellular space. The exchange rate of each metabolite of the flux-balance analysis metabolic model is limited by its extracellular copy number. 23 additional processes access and modify the Metabolite state, primarily drawing cytosolic metabolites to support macromolecule synthesis. Four processes do not directly interact with the Metabolite state: Host Interaction, Macromolecular Complexation, Terminal Organelle Assembly, and Transcriptional Regulation.

## Initial Conditions

After the Mass state initializes the total cell mass, the Metabolite state initializes the total cytosolic and membrane copy numbers of each metabolite according to the calculated chemical composition of M. genitalium (see Section 2.7 and 2.7 and Table S3I). Additionally, after the Geometry state initializes the volume of the extracellular compartment, the Metabolite state initializes the extracellular copy number of each metabolite according to the reconstructed medium composition (see Section 2.7 and 2.7 and Table S3H). Following Metabolite state initialization, the Chromosome, Rna, Protein Monomer, Protein Complex, Transcript, and Polypeptide states initialize the copy number of each macromolecule species, and decrement the metabolite copy numbers to maintain the initial cell mass.

## Fitting

The chemical compositions of M. genitalium and the extracellular medium were initially reconstructed based on the experimentally characterized compositions of M. genitalium and SP-4 medium. The cell and medium composition were both supplemented to support the metabolic demands of the 28 modeled cellular processes. See Section 1.3, 2.5, and 2.7 for further discussion.

## 2.8 Polypeptide

## Biology

The Polypeptide state class keeps track of the progress of translation. In our model, binding of free ribosomes to mature mRNAs is determined by mRNA availability. Once bound, a polypeptide is sythesized at a rate of up to 16 amino acids per second<sup>564</sup>. Therefore, polypeptides may take multiple 1 second timesteps to be completed. The Polypeptide state class holds information about which mRNAs are ribosome bound, as well as ribosomal progress of translating a transcript across timesteps.

For reasons such as limited resources, a ribosome may stall resulting in an incomplete polypeptide. In such cases, a proteolysis tag (a short peptide added to the end of a nascent polypeptide) may be synthesized to mark the ribosome for release and the aborted polypeptide for degradation. This state also houses the progress of proteolysis tag synthesis and the amino acid sequences of the incomplete polypeptides that are to be degraded.

## Reconstruction

The Polypeptide state class serves as a “support system” for translation, providing it with infomation that is required to translate polypeptides.

The state holds fixed information such as the length, tRNA sequence, and amino acid sequence of every M. genitalium monomer and the length, molecular weight, tRNA sequence, and amino acid sequence of every possible M. genitalium proteolysis tag.

## Computational Representation

As the simulation progresses, this state class holds transient information such as the ribosome-bound mRNAs, the lengths of polypeptides that are being translated, and the sequences of aborted polypeptides.

The state can calculate information from the transient properties such as the counts of each amino acid in each polypeptide and the length of aborted sequences. Lastly, this state is able to calculate the weight of all nascent polypeptides as the sum of the weights of the amino acid components.

## Integration

The Translation process class reads all of the fixed parameters describing polypeptides and proteolysis tags. It both reads and updates the time evolving parameters describing polypeptides and proteolysis tags. The Protein Decay process class reads the sequence and length of each aborted polypeptide.

## Initial Conditions

The simulation begins in a state in which ribosomes are already bound to mRNAs and in the process of elongating. Each growing polypeptide is accounted for in the Polypeptide state class. No proteolysis tags exist at the start of the simulation.

## 2.9 Protein Complex

## Biology

Protein complexes are used by almost all of the process classes in the system to perform their respective functions. A protein complex could be as small as transketolase, a dimer, or as large as pyruvate dehydrogenase that has 192 monomeric subunits. A complex may contain a mixture of protein and RNA subunits (e.g. ribosome), metabolites (e.g. DnaA protein bound to ATP), or ions (e.g. oxidized form of the protein thioredoxin). A complex can also exist in various locations within a cell including in the cytoplasm, membrane, terminal organelle, and bound to the chromosome. The Protein Complex state class holds information about complex composition, as well as the counts of each complex in the cell.

## Reconstruction

The Protein Complex state class holds fixed parameters including the complex subunit composition, molecular weights, amino acid composition, half-lives, and localization. Some essential functions require a certain threshold abundance of particular protein complexes, and so this state class also holds the minimum expression of each complex.

## Computational Representation

As complexes are produced by the Macromolecular Complexation process and other processes in the model, their counts are stored in this state. This state can also compute the dry weight of each protein complex in the cell.

## Integration

List S3. Connections between the Protein Complex state class and other processes in the cell.
<table><tr><td>Connected Processes</td><td>Read from Protein Complex</td><td>Written to Protein Complex</td></tr><tr><td>Macromolecular Complexation</td><td>Counts of protein complexes Complex subunit composition</td><td>Updated counts of protein complexes</td></tr><tr><td>Ribosome Assembly</td><td>Counts of ribosomes</td><td>Updated counts of ribosomes</td></tr><tr><td>Replication</td><td>Counts of replication complexes</td><td>Updated counts of replication complexes</td></tr><tr><td>Replication Initiation</td><td>Counts of DnaA complexes</td><td>Updated counts of DnaA complexes</td></tr><tr><td>Protein Decay</td><td>Counts of protein complexes</td><td>Updated counts of protein complexes</td></tr><tr><td></td><td>Complex half lives Complex amino acid composition</td><td></td></tr><tr><td>Transcription</td><td>Minimum average expression</td><td></td></tr><tr><td>Various other processes</td><td>Protein complex counts to</td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td>determine maximal enzyme activity</td><td></td></tr></table>

## Initial Conditions

The system is initialized with a set of proteins. The determination of which proteins are expressed and at what quantities is determined randomly based on expected protein expression and expected total protein mass fraction.

## 2.10 Protein Monomer

## Biology

Protein Monomers are the direct result of successful translation events. Upon Translation, a monomer undergoes various steps towards maturation including deformylation, translocation, folding, and phosphorylation. As a result, a monomer can exist in many forms (nascent, processed (I), translocated, processed (II), folded, and mature) as it moves through the maturation pipeline (See Schematic S3).

![](images/f8b6797abac096f62780bf5c4b880c56e865828ed54a35c4f140b2e1aa9f5b69.jpg)  
Schematic S3. Protein monomer forms diagrammed in the context of the maturity pipeline.

In addition to maturation, various processes can render a monomer non-functional, resulting in the misfolded, inactive, or damaged forms. Further, a mature monomer may be freely floating in the cytoplasm or bound to another molecule in the cell. For example, a translation factor may be bound to a mRNA, or a topoisomerase may be bound to a chromosome. The quantities of monomers in each of the maturation phases, functional forms, and non-functional forms are stored in this state class. Note that some functional enzymes are a complex of monomers, and these complexes are stored in a separate state class called Protein Complex.

## Reconstruction

The main purpose of the Protein Monomer state class is to hold the counts and attributes of the monomeric species in the system.

This state class holds important information describing protein monomers such as their molecular weights, amino acids composition, length (in amino acids), and half-lives. A subset of monomers are translocated to diferent compartments in our model such as the membrane or terminal organelle. The Protein Monomer state class contains information about where each monomer localizes.

The Protein Monomer state class also houses information that is important for the fitting and initialization of the model. Some essential functions require a certain abundance of particular proteins. For example, the Cell Division process may require at least some threshold abundance of the division protein FtsZ for cell division to ever be possible. The sytem is then fit such that in an unperturbed state, at least this threshold amount of FtsZ is produced. This state stores the minimum expression of each monomer.

The current version of this model involves a stochastic generation of the initial protein abundances in the cell. The initial abundance of certain monomers is more rigid than others for the maintainace of a stable system that can grow and divide. The Protein Monomer state class stores the degree of variation we allow in the initial abundances of each monomer.

## Computational Representation

The Protein Monomer state class holds the counts of the monomeric species in each of the forms shown in blue in Schematic S3.

## Integration

List S4. Connections between the ProteinMonomer state class and other processes in the cell.
<table><tr><td>Connected Processes</td><td>Read from Protein Monomer</td><td>Written to Protein Monomer</td></tr><tr><td>Translation</td><td>Counts of nascent monomers</td><td>Updated counts of nascent monomers</td></tr><tr><td>Protein Processing I</td><td>Counts of nascent and processed (I) monomers</td><td>Updated counts of nascent and processed () monomers</td></tr><tr><td>Protein Translocation</td><td>Counts of processed (I) and translocated monomers</td><td>Updated counts of processed (I) and</td></tr><tr><td>Protein Processing II</td><td>Counts of translocated and processed  Updated counts of translocated and (II) monomers and signal sequences</td><td>translocated monomers processed (II) monomers and signal</td></tr><tr><td>Protein Folding</td><td>Counts of processed (II) and folded monomers</td><td>sequences Updated counts of processed (II) and folded monomers</td></tr><tr><td>Protein Modification</td><td>Counts of folded and mature monomers</td><td>Updated counts of folded and mature monomers</td></tr><tr><td>Macromolecular Complexation • Counts of mature monomers</td><td></td><td>Updated counts of mature monomers</td></tr><tr><td>Protein Decay</td><td>Counts of monomers Monomer half lives</td><td>Updated counts of monomers Assignment of damaged monomers</td></tr><tr><td>Protein Activation</td><td>Monomer amino acid composition Counts of mature and inactivated</td><td>Assignment of misfolded monomers Updated counts of mature and</td></tr><tr><td>Various other processes Protein monomer counts to determine</td><td>monomers Counts of mature and bound monomers</td><td>inactivated monomers Updated counts of mature and bound monomers</td></tr></table>

## Initial Conditions

The system is initialized with a set of proteins. The determination of which proteins are expressed and at what quantities is determined randomly based on expected protein expression and expected total protein mass fraction.

## 2.11 Ribosome

## Biology

## Composition

Ribosomes are large ribonucleoproteins which synthesize polypeptides. The M. genitalium 70S ribosome is composed of two subunits – the 30S and 50S ribosomal subunits – which assemble on mRNA with assistance from initiation factors 1-3 (MG173, MG142, MG196). The 30S subunit is composed of 1 RNA and 20 protein monomer subunits. The 50S subunit is composed of 2 RNA and 32 protein monomer subunits. The 30S and 50S ribosomal subunits are believed to assemble in stereotyped patterns<sup>660,661</sup>, and six GTPases – EngA (MG329), EngB (MG335), Era (MG387), Obg (MG384), RbfA (MG143), and RbgA (MG442) – have been associated with ribosomal subunit assembly<sup>58,102,104,105,182,222,223</sup>. The exact functions of the six GTPases are unknown.

## Translation

Following 70S ribosome assembly, ribosomes synthesize amino acid polymers according to nucleic acid templates specified by mRNA and decoded by tRNA. Upon reaching the stop codon UAG, ribosome release factor (MG258) binds to the 70S ribosome, recognizes the stop codon, hydrolyzes the peptidyl-tRNA bond, and releases the terminal tRNA. Finally, elongation factor G (MG089) and initiation factor 3 dissociate the 30S and 50S ribosomal subunits, the mRNA, and the ribosome release factor. See Section 3.27 for further discussion of translation.

## Stalled Ribosome Response

Upon prolonged translational stalling, tmRNA can displace both ribosome-bound tRNA and mRNA, leading to the generation of chimeric polypeptides containing an N-terminal mRNA-coded domain and a C-terminal tmRNA-coded degradation domain, or SsrA tag. Following translation termination, the protein degradation machinery recognizes the SsrA tag and degrades the chimeric polypeptide. See Section 3.27 and 3.12 for further discussion.

## Computational Representation

The Ribosome state represents (1) the status – actively translating or stalled – of each 70S ribosome, (2) the mRNA, or tmRNA in the case of stalled ribosomes, species each 70S ribosome is bound to and translating, and (3) the position, in codons, of each 70S ribosome from the start codon. The status, bound (t)mRNA, and (t)mRNA position of each ribosome are implemented as scalar integer variables.

## Integration

The Polypeptide state represents the sequence of each nascent polypeptide. The Protein Complex state represents the copy numbers of free 30S and 50S ribosomal subunits, and of mRNA-bound 70S ribosomes. The Rna state represents the copy number of each mRNA species and of tmRNA.

Three processes – Translation, RNA Decay, and Protein Decay – access and modify the Ribosome state. The Translation process models the formation of 70S ribosomes on mRNA, polypeptide synthesis catalyzed by 70S ribosomes, and 70S ribosome disassembly following translation termination. The Translation process also models ribosome stalling, tmRNA substitution, and SsrA degradation tag synthesis. Computationally, the Translation process predicts the state of each 70S ribosome, the mRNA or tmRNA species each 70S ribosome is bound to, and the elongation rate of each nascent polypeptide.

mRNA and tmRNA degradation events modeled by the RNA Decay process trigger early 70S ribosome disassembly resulting in incomplete polypeptides. Similarly, 70S ribosome degradation events modeled by the Protein Decay process result in incomplete polypeptides. Both processes decrement the copy number of mRNA-bound 70S ribosomes represented by the Protein Complex and Ribosome states.

The Ribosome Assembly process models the assembly of 30S and 50S ribosomal subunits from rRNA and ribosomal protein monomers. The Protein Activation process models the efect of antibiotics on the catalytic activity of 30S and 50S ribosomal particles.

## Initial Conditions

After the Rna and Protein Monomer states initialize the total copy number of each RNA and protein monomer species and the Ribosome Assembly process initializes the total copy numbers of the 30S and 50S ribosomal subunits, the Translation process initializes the Ribosome and Polypeptide states. As described in Algorithm S4, the Translation process forms 70S ribosomes equal to the minimum of the 30S and 50S subunit copy numbers, and randomly positions each 70S ribosome on mRNA weighted by the copy number of each mRNA.

Algorithm S4 | Ribosome and Polypeptide state initialization.  
Free 70S ribosomes ← min(free 30S, 50S ribosomal particles)   
Decrement the copy numbers of free 30S and 50S ribosomal particles   
foreach 70S ribosome i do   
Select the mRNA of 70S ribosome i weighted by the product of mRNA copy number and length   
Set the bound mRNA species of 70S ribosome i   
Select the position of 70S ribosome i along the bound mRNA with uniform probability   
Set the status of 70S ribosome i to actively translating   
Decrement the copy number of free 70S ribosomes   
Increment the copy number of bound 70S ribosomes   
Set the sequence of the nascent polypeptide corresponding to 70S ribosome i

## 2.12 RNA

## Biology

Transcription leads to the production of nascent RNA that, once mature, may be used in various cell functions. mRNAs serve as a template for protein synthesis, rRNAs are a part of the ribosome structure, tRNAs carry amino acids to growing polypeptides, and sRNAs act as regulators. tmRNAs come into action when ribosomes stall on an mRNA during translation, helping recycle the stalled ribosome and adding a proteolysis tag to the incomplete polypeptide.

Diferent nascent RNAs undergo various steps towards maturation, including cleavage from polycistronic (transcription unit) to single RNA form, methylation, and thiolation (see Schematic S4). Maturation is carried out by the RNA Processing and RNA Modification process classes. There is an additional step for tRNAs which are coupled with amino acids by the tRNA Aminoacylation process.

In addition to the various forms an RNA can take in the maturation pathway, an RNA can also transition between various non-functional and functional forms. RNAs may exist with proteins in a macromolecular complex, and when the complex is marked for decay by the Protein Decay process class, its RNA subunits are marked as damaged in the Protein Monomer state class. Damaged RNAs are degraded by the RNA Decay process class. Further, a mature RNA may be freely floating in the cytoplasm or bound to another molecule in the cell. For example, an mRNA may be bound to a ribosome. This is accounted for in the the Bound RNA form. The quantities of RNA in each of these immature/mature and functional/non-functional forms is stored in this state class (see Schematic S4).

## Reconstruction

This state class holds information about RNAs such as their weights, compositions, lengths, and localizations. It also holds important parameters for the maturation pathway of RNA, such as a number of matrices that map one form of RNA to another, and the gene composition of transcription units. Other parameters such as expected RNA half-lives and RNA weight fractions are included in this class, and are used to determine the RNA Polymerase-DNA binding parameters associated with gene expression.

## Computational Representation

The Protein Monomer state class contains the number of each RNA species in each RNA form.

Other properties are calculated by this state class. The RNA decay rates are calculated from the experimentally measured half lives. The actual decay rates and RNA expression values used in the model are fit from the experimentally measure values such that the cell will double its mass and successfully divide by the end of the cell cycle.

![](images/2e3d7eec2338b27a13a046d9e07f040c87336c1c842f3c901340b325b6ae85ba.jpg)  
Schematic S4. RNA forms diagrammed in the context of RNA maturation.

## Integration

List S5. Connections between ProteinMonomer state and other processes in the cell.
<table><tr><td>Connected Processes</td><td>Read from Rna</td><td>Written to Rna</td></tr><tr><td>Transcription</td><td>Counts of nascent RNAs</td><td>Updated counts of nascent RNAs</td></tr><tr><td>RNA Processing</td><td>Counts of nascent, processed, and intergenic RNAs</td><td>Updated counts of nascent, processed, and intergenic RNAs</td></tr><tr><td>RNA Modification</td><td>Counts of processed and mature RNA</td><td>Updated counts of processed and mature RNA</td></tr><tr><td>tRNA Aminoacylation</td><td>Counts of mature and aminoacylated tRNA</td><td>Updated counts of mature and aminoacylated tRNA</td></tr><tr><td>RNA Decay</td><td>Counts of mature, misfolded, and damaged RNA</td><td>Updated counts of mature, misfolded, and damaged RNA</td></tr><tr><td>Various Processes</td><td>Counts of mature and bound RNAs</td><td>Updated counts of mature and bound RNAs</td></tr></table>

## Initial Conditions

The system is initialized with a set of RNAs. The determination of which RNAs are expressed and at what quantities is determined randomly based on expected RNA expression and expected total RNA mass fraction.

## 2.13 RNA Polymerase

## Biology

RNA polymerases are protein complexes that bind to gene promoters on the chromosomes and mediate the synthesis of RNA transcripts. This state class helps keep track of the conditions and chromosomal locations of RNA polymerases in the cell.

## Reconstruction

An RNA polymerase in our model can exist in one of four conditions:

1. Free (not bound to DNA)

2. Non-specifically bound (bound to the DNA, but not to a specific gene promoter and not transcribing)

3. Specifically bound (bound to a specific gene promoter)

4. Actively transcribing (moving along a gene to produce an RNA)

This state class stores properties relating to RNA polymerases such as the expected probabilities of a polymerase being in the above 4 conditions.

## Computational Representation

As the simulation progresses, this state class stores the condition of each RNA polymerase in the simulated cell. Transition between the conditions may involve RNA polymerase association and dissociation from the cell’s chromosome(s). This state class holds the precise positions on the chromosome(s) where polymerases are bound. The RNA Polymerase state class also handles basic accounting. For example, upon an RNA polymerase decay event, a free polymerase is decremented. Further, this class records the premature release of RNA polymerases from the chromosome(s) and passes information about the aborted transcript to the Transcript state class.

Further, the Transcription process class requires the RNA Polymerase-promoter binding probability for each transcription unit. These probabilities may vary during the cell cycle due to the efects of other processes in the system, such as Transcriptional Regulation or DNA supercoiling. The fold changes to the base binding probabilities incurred by these other processes is stored in the RNA Polymerase state class.

This state class can also calculate the total number of RNA polymerases in each condition.

## Integration

The Chromosome state class updates the chromosomal positions of RNA polymerases in the RNA Polymerase state class. The Transcript state class reads the aborted RNA sequences from and writes the updated aborted sequences to the RNA Polymerase state class.

The Transcription process class reads the RNA polymerase conditions and progress from and updates the RNA polymerase conditions and progress to the RNA Polymerase state class. The Transcription process class also reads the RNA polymerase condition transition probabilities and RNA polymerase binding probabilities from the RNA Polymerase state class. The Transcriptional Regulation and DNA Supercoiling process classes record the fold change in RNA polymerase binding probabilities to the RNA Polymerase state class.

## Initial Conditions

NA polymerases are initialized as follows:

1. Each RNA polymerase is randomly assigned (with replacement) to one of the actively transcribing, specif ically bound, non-specifically bound, or free states weighted by the expected occupancy of each state

2. Actively transcribing and specifically bound polymerases are randomly assigned to transcription unit weighted by the transcription unit binding probabilities $\left( P _ { t u } \right)$

3. Actively transcribing polymerases are randomly assigned to positions within the assigned segment of their assigned transcription unit (positions near the segment border are not allowed to prevent polymerases from being too close to each other) with uniform probability.

4. Non-specifically bound polymerases are randomly assigned to an accessible region on the chromosome.

## 2.14 Stimulus

## Biology

Cells live in complex environments where they are exposed to physical and chemical stresses including antibiotics, radiation, heat and cold. Furthermore, manipulation of the external environment is a powerful tool for discovering new biology. This state represents the status of 10 properties of the external environment.

## Reconstruction

Table S3F describes the reconstruction of the values of these 10 properties of the external environment.

## Computational Representation

Specifically, this state represents the temperature in °C, six types of radiation in $\mathrm { W } \mathrm { m } ^ { - 2 } , ~ \mathrm { G y } \mathrm { s } ^ { - 1 }$ or $\mathrm { m ^ { - 2 } s ^ { - 1 } s r ^ { - 1 } }$ , and three Boolean-valued stress conditions. Computationally, each property is implemented as a floating point scalar. Table S3F lists the values of these 10 properties used throughout each simulation.

## Integration

This state does not directly interact with any of the other 15 states. The Geometry, Metabolite, Protein Monomer, Protein Complex, and Host states represent additional properties of the extracellular environment. The Geometry state represents the volume of the external environment. The Metabolite state represents the copy numbers of extracellular metabolites including antibiotics. The Protein Monomer and Protein Complex states represent the copy numbers of extracellularly localized proteins. The Host state represents six properties of the host urogenital epithelium.

Three processes – Protein Activation, DNA Damage, and Metabolism – access the Stimulus state. The Protein Activation process regulates the activity of four transcription factors as functions of temperature and three stress conditions (see Table S3Q). The DNA Damage process models the rates of several types of DNA damage as functions of radiation (see Table S3O). The Metabolism process models the generation of hydroxyl radicals from water and γ-radiation (see Table S3O). None of the processes modify the 10 properties of the external environment.

## Initial Conditions

For this study the 10 properties of the external environment were initialized to the values listed in Table S3F, and were not modified during the simulation.

## 2.15 Time

## Biology

The physical, chemical, and biological processes relevant to cell physiology span a wide range of time scales. To limit the scope of this study, we modeled M. genitalium on a 1 s time scale and averaged out the efects of faster processes. M. genitalium can be approximated as a well-mixed system at this time scale.

## Computational Representation

This state represents the time elapsed from the start of the simulation in seconds as a single integer variable.

## Integration

The Time state directly interacts with only three parts of the simulation:

• The Simulation linearly advances time in 1 s increments (See Section 1.1).

• If the cell has not yet divided, each simulation terminates at a predetermined maximum time of 50,000 s, approximately equal to 150% of the observed mean M. genitalium mass doubling time (See Section 1.1).

• The concentrations of extracellular metabolites and the values of extracellular stimuli depend on time (see Section 2.7 and 2.14).

None of the processes or other states depend directly on the Time state.

## Initial Conditions

The Time state is initialized to zero and the other 15 states are initialized to the beginning of the cell cycle.   
Consequently, the Time state also represents the time elapsed from the beginning of the cell cycle.

## 2.16 Transcript

## Biology

During Transcription, an RNA polymerase binds to a gene promoter and facilitates the synthesis of an RNA transcript. This state stores all of the information that pertains to nascent RNA transcripts and aids in the time evolution of Transcription.

## Reconstruction

There are multiple fixed properties relating to the gene templates of transcripts that are essential for transcription and stored in the Transcript state. For each transcription unit, we store the 5’ coordinate of the gene on the genome. This is the template for the 1st nucleotide in a growing transcript. In addition to this, we store the direction in which the template is read, towards or away from the origin. We also store the sequence and length of each transcription unit.

## Computational Representation

Transcription proceeds at a maximal rate of 50 nucleotides per second<sup>562,563</sup>. Therefore, it may take several timesteps to synthesize a transcript, and the progress of the RNA polymerase along the transcription unit must be stored. This state stores the transcription unit to which each RNA polymerase is bound, including which chromosome it is bound to and the progress of the RNA polymerase along the transcription unit.

An RNA polymerase may stall in the Transcription process or be knocked of of a gene by another protein. In these cases, an incomplete transcript may result, and will be targeted for degradation by the RNA Decay process. This state holds the sequence of each aborted transcript, such that the nucleotides can correctly be accounted for upon degradation.

Multiple RNA polymerases may be bound to a given transcription unit, and this state can calculate the total number of polymerases on each unit. Finally, the Transcript state also calculates the dry weight of the nascent transcripts.

## Integration

The Transcript state class reads about the existence of an aborted sequence from the RNA Polymerase state class. Upon RNA polymerase displacement, the Transcript state class updates the Transcript state in the Chromosome state class. It also records the start sites and directions of transcription units in the Chromosome state class.

The Transcription process class uses all of the fixed properties and time evolving properties housed in the Transcript state class.

## Initial Conditions

An RNA polymerase may be initialized in the actively transcribing state. For all such polymerases, the growing transcript is accounted for in the Transcript state class.

## Chapter 3

# Cellular Process Methods

The whole-cell model is composed of 28 sub-models which span six major areas of cellular physiology: (1) transport and metabolism, (2) DNA replication and maintenance, (3) RNA synthesis and maturation, (4) protein synthesis and maturation, (5) cytokinesis, and (6) host interaction. The sub-models were modeled using diferent mathematics and trained using diferent experimental data. Each of the 28 functional processes, or cellular processes, represents a group of chemical reactions which transform chemical substrates into products using enzyme catalysts. Computationally, the inputs and outputs of each sub-model are the copy numbers of metabolites and macromolecules; the configurations of RNA, protein and DNA polymers; and the catalytic capacity and configurations of the enzymes which participate in each sub-model. This chapter provides detailed discussions of the mathematics and computational implementation of each cellular process.

## Metabolism

The Metabolism process modeled the import of nutrients from the external environment and their conversion primarily into the metabolic building blocks required by the 27 other processes for macromolecule synthesis. Therefore, the Metabolism process served as the primary interface between the external environment and the 27 other processes, providing the nutrients required for each of the other processes and recycling and/or exporting the metabolic byproducts of the other processes. The Metabolism process was reconstructed primarily based on DNA sequence homology of M. genitalium to E. coli and a comprehensive metabolic model of E. coli<sup>558</sup>. The Metabolism process was modeled using FBA and trained using the observed growth rate of M. genitalium and the observed chemical compositions of M. gallisepticum<sup>870</sup> and E. coli<sup>393</sup>. The composition of the in silico growth medium was reconstructed based on the reported chemical composition of the individual components of Mycoplasma SP-4 medium, with additional metabolites added to support sustained in silico growth.

## RNA Synthesis & Degradation

RNA synthesis and maturation was modeled by four processes: Transcription, RNA Processing, RNA Modification, and tRNA Aminoacylation. Transcription modeled the state – free, non-promoter bound, promoter-bound, or actively transcribing – of each RNA polymerase, transcription initiation at specific promoters, transcription elongation and NTP allocation among nascent transcripts, and transcription termination. The state of each RNA polymerase was modeled as a Markov chain and trained with the observed occupancies of each of the four modeled states<sup>775</sup>. Transcription initiation was modeled as a stochastic process and trained using the reconstructed expression and decay rates of each transcription unit<sup>569,602</sup>. The transcription unit organization of the chromosome was reconstructed from the observed operon organization of M. pneumoniae<sup>418</sup>. Because transcription termination is not well-characterized, termination was modeled as a deterministic process which proceeds to completion within the 1 s simulation time step if there is least one copy of each of the characterized transcription termination factors.

Transcriptional Regulation modeled the fold change efects of transcriptional regulators on the afinity of RNA polymerase for specific promoters. The Transcriptional Regulation sub-model was reconstructed using the database DBTBS<sup>419</sup>. Transcriptional Regulation was modeled as a stochastic process and trained using reported fold change efects.

Following transcription, non-coding transcripts are cleaved, modified, and aminoacylated. The RNA Processing sub-model modeled the cleavage of polycistronic non-coding RNA into individual non-coding RNA gene products. The RNA Processing sub-model was reconstructed primarily based on reported E. coli RNA cleavages<sup>39,105,649</sup> and the complement of RNA processing enzymes contained in the M. genitalium genome. The RNA Modification process modeled the modification of specific bases of specific non-coding RNAs and was reconstructed based on the observed complement of E. coli RNA modifica tions<sup>45,47,55,56,64,65,105,560,651,885</sup>. The tRNA Aminoacylation sub-model modeled the aminoacylation of tR-NAs according to the observed Mycoplasma genetic code<sup>53,168,607</sup>. RNA Processing, RNA Modification, and tRNA Aminoacylation were modeled motivated by mass-action kinetics and parameterized using the observed kinetics of the RNA cleavage and modification enzymes.

RNA transcripts are hydrolytically cleaved into 10-30 nucleotide fragments by ribonuclease R, which in turn are further degraded into individual NMPs. The RNA Decay sub-model modeled the decay of each RNA species as a first-order Poisson process with rate parameters equal to the observed decay rates of E. coli RNA<sup>602</sup>.

## Protein Synthesis & Degradation

Protein synthesis and maturation was modeled by nine processes: Translation, Protein Processing I, Protein Translocation, Protein Processing II, Protein Folding, Protein Modification, Macromolecular Complexation, Ribosome Assembly, and Terminal Organelle Assembly. Translation modeled the assembly of 70S ribosomes on mRNA Shine-Dalgarno sequences, the polymerization of amino acids into polypeptides, and the allocation of aminoacylated tRNAs among the multiple active ribosomes. The Translation sub-model also modeled the role of tmRNA in the termination of stalled ribosomes as a rare stochastic event.

Following translation, polypeptides are deformylated, cleaved, translocated, folded, and modified before forming macromolecular complexes. Protein Processing I modeled the first steps in protein maturation: polypeptide deformylation and N-terminal methionine cleavage. Protein Translocation modeled integral membrane, lipoprotein, and secreted protein translocation into the membrane by the SecA translocase. Protein Processing II modeled lipoprotein diacylglyceryl transfer, and lipoprotein and secreted protein signal sequence cleavage. Protein Folding modeled the folding of polypeptides into compact three-dimensional structures. Protein Modification modeled the covalent modification of specific amino acids. Macromolecular Complexation modeled the formation of protein and ribonucleoprotein complexes. Ribosome Assembly modeled the role of several GTPases in the assembly of 30S and 50S ribosomal particles. Terminal Organelle Assembly modeled the observed hierarchical assembly of the protein content of the M. genitalium terminal attachment organelle.

The eight post-translational processing sub-models were reconstructed based on specific N-terminal methionine cleavages observed in Shewanella oneidensis MR-1<sup>280</sup>, the predicted localization and signal sequence of each protein monomer (see Table S3AM-S3AO), the observed chaperone interactions of E. coli<sup>388,389</sup> and B. subtilis<sup>391</sup>, the observed complement of M. genitalium and M. pneumoniae protein modifications<sup>94,277,282,283,672</sup>, and the inferred subunit composition of each macromolecular complex (see Table S3AS). The eight posttranslational processing sub-models were modeled motivated by mass-action kinetics and were parameterized using the reported kinetics of the post-translational processing enzymes.

The Protein Decay sub-model modeled the hydrolytic cleavage of proteins into 10-20 amino-acid-long fragments by protease La, as well as the cleavage of aborted polypeptides by protease FtsH. Similar to RNA Decay, Protein Decay was modeled as a first-order Poisson process. The half-life of each protein was predicted using the N-end rule<sup>586</sup>. Additionally, the Protein Decay sub-model modeled protein misfolding and ClpB chaperone-mediated refolding. Protein misfolding was modeled as a stochastic process. Protein refolding was modeled as a deterministic process governed by a single Boolean rule.

The Protein Activation process modeled the chemical regulation of protein activity. The Protein Activation process was reconstructed primarily based on the database DrugBank<sup>847</sup>. Because the exact mechanisms of protein chemical regulation are poorly characterized, Protein Activation was modeled as a Boolean network.

## Chromosomal Replication & Maintenance

Seven processes modeled chromosomal replication, damage, and maintenance: Replication Initiation, Replication, Chromosome Segregation, Chromosome Condensation, DNA Supercoiling, DNA Damage, and DNA Repair. The Replication Initiation process modeled the recruitment of DNA polymerase to the oriC by the formation of a large DnaA complex at the R1-5 functional oriC DnaA boxes. Replication Initiation was reconstructed using the reported DnaA DNA-binding motif, and implemented similar to the E. coli replication initiation model developed by Messer<sup>924</sup>.

The Replication process modeled bidirectional DNA replication, dissolution of the oriC DnaA complex, single stranded binding protein (SSB) binding to exposed single-stranded DNA, and Okazaki fragment ligation. Allocation of dNTPs among elongating DNA polymerases was modeled similarly to Transcription and Translation.

The Chromosome Segregation process modeled daughter chromosome segregation following chromosomal replication. Because Chromosome Segregation is poorly characterized, Chromosome Segregation was modeled as a single event governed by a simple Boolean rule.

Chromosome Condensation and DNA Supercoiling modeled DNA compaction mediated by structural main tenance of chromosome (SMC) proteins and topoisomerases. Chromosome Condensation was reconstructed based on the reported DNA density of SMC proteins<sup>517</sup> and SMC DNA-binding was modeled as a stochastic process. DNA Supercoiling was modeled as the balance of the competing winding and unwinding efects of topoisomerase I and DNA gyrase, and parameterized by the observed kinetics of topoisomerase I and DNA gyrase<sup>502,750,922</sup>.

DNA Damage modeled spontaneous and chemically- and radiation-induced DNA damage as a stochastic process parameterized by the reported eficiencies of DNA damage. DNA Repair modeled four modes of DNA repair – direct damage repair (DDR), base excision repair (BER), nucleotide excision repair (NER), and homologous recombination double strand break repair (HR-DSBR) – as well as the M. genitalium MunI restriction/methylation (R/M) system. DDR, BER, NER, and HR-DSBR were modeled as stochastic processes parameterized by their observed kinetic rates. R/M was reconstructed based on the reported MunI DNA-binding motif and modeled as a stochastic process.

## Cytokinesis

Following chromosomal replication and segregation, M. genitalium divides by binary fission. According to the Li et al. hypothesis<sup>611</sup>, M. genitalium divides by iteratively pinching its the septal membrane using the filamentous protein FtsZ. The FtsZ Polymerization process modeled the formation of septal FtsZ rings. FtsZ Polymerization is implemented using the ordinary diferential equations described by Surovtsev et al.<sup>164</sup>. The Cytokinesis process modeled the iterative contraction of successively smaller FtsZ septal rings. The Cytokinesis sub-model was parameterized using the observed rate of FtsZ-GTP hydrolysis<sup>421</sup>.

## Cell Cycle

Three M. genitalium cell cycle phases were modeled: (1) pre-replication, or replication initiation, (2) replication, and (3) cytokinesis. All simulations reported in this study were initialized to the beginning of the replication initiation phase. Starting at the beginning on each simulation, the Replication Initiation process modeled the formation of the oriC DnaA complex, ultimately resulting in the recruitment of DNA polymerase to the replication origin and the start of DNA replication. Following DNA polymerase recruitment to the replication origin, the Replication process modeled DNA replication. After chromosomal replication the Chromosome Segregation process modeled daughter chromosomal segregation. Finally, the FtsZ Polymerization and Cytokinesis processes modeled the formation and contraction of FtsZ septal rings, ultimately resulting in cell division.

## Host Interaction

The Host Interaction process modeled the interaction of M. genitalium with its host human urogenital epithelium. The Host Interaction process was reconstructed based on the observed composition of the protein content of the M. genitalium terminal organelle<sup>408,409</sup> and the reported M. genitalium-host interactions<sup>88,176,194,313,842,844</sup>. Because the interaction of M. genitalium with its human host is poorly characterized, Host Interaction was implemented as a Boolean model.

## 3.1 Chromosome Condensation

## Biology

Bacterial chromosomes are compacted 10<sup>4</sup>-fold in volume in order to physically fit inside of a cell<sup>921</sup>. Compaction is also necessary to support various cellular processes including chromosome replication, cell division, and chromosome segregation to opposing poles of the cell<sup>921</sup>. Bacteria employ several mechanisms to compact DNA including ”clamping” of the DNA by structural maintenance of chromosome (SMC) proteins, DNA supercoiling, macromolecular crowding, and charge neutralization<sup>921</sup>. M. genitalium has the machinery to perform all of these levels of DNA compaction, and we explicitly model DNA Supercoiling in a separate process class and DNA clamping by SMC complexes here in the Chromosome Condensation process class.

## Reconstruction

SMC complexes consist of an SMC core protein (Smc: MG298) and segregation and condensation proteins A and B (ScpA: MG213, ScpB: MG214). Together, the SMC complex is a “V” shaped structure (with a head and two legs) that induces positive supercoils in double stranded DNA<sup>848</sup>. The complexes are believed to work with a lock and key mechanism in which first DNA is looped around the legs of the SMC complex, and then an ATP is bound between the two tails to lock the SMC complex in place. The complexes bind and clamp the DNA causing many loops in the DNA and DNA compaction. The loops around each leg occupy 90bp. A loop of about 450bp forms between the two SMC complex legs<sup>517,521</sup>. Further, it has been inferred that there is about one SMC complex bound for every 7130bp of DNA (See Schematic S5)<sup>517</sup>. All of the parameters used in the Chromosome Condensation process class are described in List S6.

![](images/2b3ee7fd8094dc87ed9a8dcd45ac6ea5e4bd1e321ba707b7f8e6abc71c8e9f0e.jpg)  
Schematic S5. SMC complex occupation of the DNA.

List S6. Fixed parameters used in the Chromosome Condensation process class.
<table><tr><td>Parameters</td><td>Value</td><td>Symbol</td><td>Source</td></tr><tr><td>Average separation of SMC complexes on the chromosome(s)</td><td>7130 nt</td><td>s</td><td>[517]</td></tr><tr><td>SMC complex threshold spacing</td><td>2800 nt</td><td>l</td><td>Fit</td></tr><tr><td>SMC DNA footprint</td><td>630 nt</td><td></td><td>[517]</td></tr><tr><td>SMC arm DNA footprint</td><td>90 nt</td><td></td><td>[517]</td></tr><tr><td>SMC inter-arm loop length</td><td>450 nt</td><td></td><td>[517]</td></tr></table>

## Parameter Assignment

Given that the DNA footprint of an SMC complex is much less than its average spacing, if we simply applied a 1/s probability of each base being bound at each timestep, over time given an SMC abundance we would see SMCs bound at intervals much less than s. the SMC complex threshold spacing parameter (l) prevents this phenomenon by inhibiting SMC complex binding where the gap between existing SMC complexes on the DNA is already much less than the desired spacing. Biologically, this parameter represents the notion that SMC complex binding is not only determined by SMC complex abundance, but also the writhe and physical properties of the DNA that prevent SMC complex to bind too close to each other. This parameter was fit such that the average SMC complex spacing in the model is 7130 nt. The fit of this parameter was assessed by various tests to assure an average SMC spacing of 7130 nt.

## Computational Representation

This module models the contribution of SMC proteins to chromosome condensation. SMC-related DNA condensing could be considered along with the efects of topoisomerases, but we model the efect of the topoisomerases by tracking the efect of each topoisomerase activity on the DNA linking number (in the DNA supercoiling process). Since SMCs do not act by strand-passing events (the causing of a nick in the DNA, enabling two double stranded DNA regions to pass through each other, and the re-ligation of the DNA), and since we do not know the exact efect of SMC complex activity on the DNA linking number, we consider SMC condensation as compacting the DNA at a diferent level and model it independently of the DNA linking number calculations in the DNA Supercoiling process. Macromolecular crowding and charge neutralization are not presently modeled.

SMCs are bound at an average spacing (s) of 7130 bases<sup>517</sup>. Since it is unknown whether SMC complexes bind to specific DNA motifs, at each timestep, we bind SMC complexes to random positions on the chromosomes. The binding is weighed by calculated probabilities (P ) of a free SMC complex binding to each accessible double-stranded DNA base. The probability distribution is calculated as a step function: bases within a threshold distance (l) from another SMC complex have a zero probability of being bound, and bases beyond a threshold distance, l, from other SMC complexes bind at a probability of 1/s. SMC complex disassociation from the DNA occurs upon interaction with other DNA binding proteins and is handled by the Chromosome state class.

## Integration

The Chromosome Condensation process class reads from and writes to the Chromosome state class. It reads in the regions of DNA that SMC complexes can bind to, and writes back the positions of SMC complexes on the chromosome(s).

## Initial Conditions

Before the start of the simulation, we iteratively run the SMC complex binding calculations described above, to bind SMC complexes to the first chromosome until a steady state is reached, that is no more SMC complexes can be bound.

## Dynamic Computation

At each timestep, we perform the following algorithm:

1. Calculate the maximum number of SMC complexes that can bind in the given timestep.

SMCBindingLimit = min (Number of free SMC complexes, Number of availableATPmolecules)

## 2. Bind SMCs

(a) Query the Chromosome state to determine the free bases where SMC complexes can bind. Accessible bases are > l bases away from any DNA bound SMC complexes.

(b) Given that the probability of binding each accessible base is,

$$
P _ { \mathrm { B i n d i n g ~ A c c e s s i b l e ~ B a s e } } = { \frac { 1 } { s - 2 l } }
$$

randomly choose sites to bind based on this probability up to the SMCBindingLimit

(c) Form an SMC-ATP complex, and hydrolyze the ATP to ADP.

i. Decrement a free SMC

ii. Increment and decrement free metabolites for ATP hydrolysis

(d) Bind the SMC-ADP complex to chromosome (facilitated by the Chromosome state)

## 3.2 Chromosome Segregation

## Biology

DNA replication produces two chromosomes that are catenated, or connected like links of a chain. Before cell division can take place, these chromosomes need to migrate to opposing sides of the cell and be decatenated. Chromosome segregation in M. genitalium is not well understood, but is believed to result from both entropic factors and enzymatic activity<sup>849,850</sup>.

## Reconstruction

The Chromosome Segregation process class assumes that the chromosomes entropically segregate during replication as described in Bloom et al. and Jun et al.<sup>849,850</sup>. That is, it is unfavorable for the two copies of replicated DNA to exist too close to each other, thus as the replication fork moves, the replicated DNA starts to migrate towards the poles. Enzymatic segregation activity is also modeled. The five chromosome segregation proteins are a nucleotide binding domain (CobQ/CobB/MinD/ParA: MG470), an MraZ protein (MraZ: MG221), a GTP binding protein (Era: MG387), a GTPase (Obg: MG384), and topoisomerase IV (ParE: MG203, ParC: MG204). The other segregation protein, FtsZ is accounted for in the Cytokinesis process class. These proteins assist in the chromosomal migration towards the cell poles and decatenate the chromosomes following the completion of replication. However, there is no detailed understanding of the function of these proteins, and much fewer proteins are present in M. genitalium than that required for the detailed mechanisms for segregation described for other bacterial species. Further, the specific kinetics, and metabolic costs of these proteins are not known.

Note that topoisomerase IV is also used in the DNA Supercoiling process class, as it is known to relieve coils that form just downstream of the replication loops. Here it performs a decatenation function, the unlinking of the two chromosomes.

All of the parameters used in the Chromosome Segregation process class are described in List S7.

List S7. Fixed parameters used in the Chromosome Segregation process class.
<table><tr><td>Parameter</td><td>Value</td><td>Symbol</td><td>Source</td></tr><tr><td>GTP cost of chromosome segregation</td><td>1 GTP</td><td> $E _ { s e g }$ </td><td>Value unknown</td></tr><tr><td>Superhelical density tolerance</td><td>± 0.1</td><td> $\sigma _ { \mathrm { t o l } }$ </td><td>Value unknown</td></tr><tr><td>Equilibrium superhelical density</td><td>-0.06</td><td>σ</td><td>[922]</td></tr></table>

## Parameter Assignment

The energetic cost of segregation has not been experimentally characterized. The energetic cost is set to a nominal value of 1 GTP per segregation event. The superhelical density tolerance is also unknown, so the

allowed range of DNA superhelical density was set to be quite wide.

## Computational Representation

This process models enzymatically catalyzed sister chromosome separation and decatenation. Entropically driven sister chromosome separation is not well understood and is not presently modeled.

Because the molecular biology of chromosome segregation is not well understood, we have chosen to imple ment this process as a simple Boolean process: the chromosomes are regarded as segregated immediately after the following four conditions are met:

• The chromosome is replicated

• The chromosomes are properly supercoiled within a given tolerance of superhelical density

• There is at least one free and functional molecule of each of the five segregation proteins, and

• There are enough available GTP molecules

Note that Glass et al. gene essentiality study suggests that the cobQ/cobB/minD/parA gene is non-essential, but we model this gene as essential because we don’t know its specific function and how the other segregation proteins compensate in its absence.

## Integration

List S8. State classes connected to the Chromosome Segregation process class.
<table><tr><td>Connected States</td><td>Read from state</td><td>Written to state Chromosomes are segregated</td></tr><tr><td rowspan="3">Chromosome</td><td>Is chromosome replicated?</td></tr><tr><td>Are chromosome superhelical densities within tolerance?</td></tr><tr><td>Are chromosomes segregated?</td></tr></table>

## Initial Conditions

The chromosome state is initialized with 1 chromosome with superhelical density within the acceptable tolerance.

## Dynamic Computation

At each timestep, the following conditional statement is performed: If

• The chromosome is replicated

• The superhelical density is in the range: $\sigma \pm \sigma _ { \mathrm { t o l } }$

• There is at least one free and functional molecule of each of the 5 segregation proteins

• Available $\mathrm { G T P } \geq E _ { s e g }$

Then, mark the chromosome as segregated.

## 3.3 Cytokinesis

## Biology

Cytokinesis, the division of the cell into two separate daughter cells, is the final step in the cell cycle. The major step of cytokinesis is the pinching of the cell membrane in a certain location (typically the midline of the cell) until the membrane is separated and division is complete. Typically, a membrane-bound ring of a tubulin homologue forms at the cell membrane around the pinching site, and the localization and assembly of this ring requires a set of accessory proteins<sup>217</sup>. Both contractile forces of the ring filaments, and external forces by the accessory proteins contribute to the pinching of the cell membrane<sup>217</sup>.

## Reconstruction

M. genitalium has the tubulin homologue, FtsZ (MG224), but does not contain the accessory proteins required for cell division in other bacterial species. Therefore, cytokinesis in M. genitalium is not fully understood. However, Li et al. propose an “iterative pinching” model by which a cell can divide using only $\mathrm { F t s Z ^ { 6 1 1 } }$ Their proposed mechanism invokes the formation of a contractile Z ring along the interior surface of the midline of the cell membrane. The ring is comprised of GTP-activated FtsZ polymer filaments that bend when their GTP is hydrolyzed. The bending draws the membrane-bound ends of the filaments together, thereby constricting the cell membrane. Many such pinching events result in a complete constriction of the cell. M. genitalium cytokinesis is thus a cycle of filament binding, bending, and dissociation.

Lluch-Senar et al. suggest that M. genitalium cell division can occur in the absence of FtsZ through motil $\mathrm { i t y ^ { 7 9 6 } }$ We chose to use the Li et al. model because we do not have a descriptive model of M. genitalium motility and FtsZ is known to be an essential gene in M. genitalium.

All of the parameters used in the Cytokinesis process class are described in List S9.

List S9. Fixed parameters used in the Cytokinesis process class.
<table><tr><td>Parameters</td><td>Value</td><td>Symbol</td><td>Source</td></tr><tr><td>Length of an FtsZ filament</td><td>40 nm</td><td>L</td><td>[217]</td></tr><tr><td>Number of FtsZ subunits in an FtsZ filament</td><td>9 subunits</td><td>S</td><td>[217]</td></tr><tr><td>Rate of FtsZ-GTP hydrolyzing to FtsZ-GDP</td><td> $0 . 1 5 { \mathsf { s } } ^ { - 1 }$ </td><td> $k _ { \mathrm { h y d } }$ </td><td>[421]</td></tr><tr><td>Rate of FtsZ polymers binding to the membrane</td><td> $0 . 7 { \mathsf { s } } ^ { - 1 }$ </td><td> $k _ { \mathrm { b i n d } }$ </td><td>Fit</td></tr><tr><td>Rate of FtsZ polymers dissociating from the membrane</td><td> $0 . 7 { \mathsf { s } } ^ { - 1 }$ </td><td> $k _ { \mathrm { u n b i n d } }$ </td><td>Fit</td></tr></table>

## Parameter Assignment

The kinetic rates of FtsZ filaments binding and dissociating from the membrane, $k _ { \mathrm { b i n d } }$ and $k _ { \mathrm { u n b i n d } }$ , were uncharacterized. Therefore, the rates were set to be rapid such that their values under typical protein expression do not significantly limit the progression of cytokinesis.

## Computational Representation

We represent cytokinesis using a modified version of the Li et al. model<sup>611</sup>. There are four main steps to our iterative pinching model, as seen in Schematic S6. First straight FtsZ-GTP filaments bind inside the cell membrane, such that they form an inscribed polygon (Schematic S6A). Next the GTP molecules in these filaments hydrolyze to GDP, causing the filaments to bend. Since the filaments are cell membrane bound, this bending pinches the membrane inwards. The filaments bend just enough to approximately form a new circle. The new circumference of the pinched region is now smaller, and equal to the perimeter of the inscribed polygon (Schematic S6C). The precise timing of the binding, hydrolysis, and dissociation of the contractile rings allows us to maintain the contraction progress across iterative pinching steps. After hydrolysis, one of the two bent filament rings is dissociated. The other remains, to maintain the progress of cell pinching (Schematic S6D). Now a new set of straight filaments can bind and form a new polygon that will be smaller than the previous (Schematic S6A). Upon binding, the residual ring of bent filaments can dissociate (Schematic S6B). The cycle repeats, resulting in smaller and smaller pinched circumferences, until the cell has divided.

We adapted the Li et al. model into our model framework as follows. First, we implemented cytokinesis as a process that is only initiated upon chromosomal segregation. Next, the Li et al. model only explicitly involves a single set of filaments binding at each edge during the binding stage. We have modified this such that two sets of filaments bind (Schematic S6A). Multiple filament sets are required to maintain the progress of membrane constriction. Indeed, Li et al. propose that the FtsZ filaments are more abundant and that a new ring of filaments attaches to stabilize the membrane and maintain progress before the depolymerization event. Osawa et al. also report that the FtsZ ring is 3-9 filaments thick depending on the bacterial strain<sup>455</sup>. Using the lower bound, since M. genitalium is a very small bacterium, we assume that the FtsZ maintains a thickness of up to 3 filaments. Our modified version of the Li et al. model requires two sets of straight FtsZ filaments to inscribe the diameter of the cell. Then up to one set of filaments can depolymerize while two new sets of straight filaments bind the diameter of the cell. Only once the two new sets of straight filaments have bound, can the second bent set of filaments depolymerize.

![](images/48e9a14a8d7af8d18dd9867d0a55248e3a728ed3fb964fd72c37112d0d49f7c0.jpg)  
Schematic S6. Algorithm to bind, bend, and dissociate FtsZ filaments to pinch cell.

The output of this process is an indication of the profess of cell pinching, including the determination of when the cell has successfully split into two daughter cells. Complete cell division is also the trigger to end the entire simulation.

## Integration

List S10. State classes connected to the Cytokinesis process class.
<table><tr><td>Connected State</td><td>Read from state</td><td>Written to state</td></tr><tr><td>FtsZ Ring</td><td>Number of filaments bound to each edge, and whether they are bent or straight Calculation of number of polygon edges in current cell diameter</td><td>Updated number of filaments bound to each edge, and whether they are bent or straight</td></tr><tr><td>Geometry</td><td>Pinched diameter of the cell Filament length parameters (L, S)</td><td>Updated pinched diameter of the cell</td></tr><tr><td>Chromosome</td><td></td><td></td></tr><tr><td></td><td>Has chromosome segregated?</td><td></td></tr></table>

## Initial Conditions

Initialization steps are not required for this process, as Cytokinesis does not take place until late in the cell cycle. Initialization of FtsZ polymers is handled by the FtsZ Polymerization process class.

## Dynamic Computation

At each timestep we perform our modified version of the Li. et al. algorithm<sup>611</sup>. This involves binding a pair of full length (9mer) FtsZ polymers along the circumference of the midplane of the cell. When these filaments hydrolyze and bend we use circle and arc formulas to calculate the new smaller circumference of the cell. Depending on the state of the FtsZ ring, one or more of the following five steps is performed.

1. Straight filament binding (Schematic S6A): If cytokinesis has just initiated (triggered by Chromosome Segregation) or if the previous FtsZ ring has hydrolyzed and undergone dissociation I, attempt to bind two straight filaments at each polygon edge, forming a regular polygon that inscribes the pinched cell circumference:

(a) Determine the number of filaments to bind, based on the number of edges on the polygon that inscribes the pinched cell circumference. The number of edges (numEdges) is determined using the pinched diameter of the cell calculated in the previous timestep $( D _ { \mathrm { p r e v } } )$ , and the length of the FtsZ filament (L):

$$
{ \mathrm { n u m E d g e s } } = \left\lfloor \left( { \frac { \pi } { \sin ^ { - 1 } \left( { \frac { L } { D _ { \mathrm { p r e v } } } } \right) } } \right) \right.
$$

(b) Bind straight filaments such that each edge has a random chance of being bound and the probability of binding each of two filaments is equal to $k _ { \mathrm { b i n d } }$

(c) Upon each binding event, update the state of the FtsZ ring

2. Bent filament dissociation II (Schematic S6B): If there was a previous cycle and at least one straigh filament has bound each polygon edge, then dissociate the bent filament from each edge.

(a) Randomly dissociate bent FtsZ-GDP filaments such that the probability of dissociating each filament is equal to $k _ { \mathrm { u n b i n d } }$

(b) Dissociate unbound FtsZ-GDP filaments into FtsZ-GDP monomers.

(c) Upon each dissociation event, update the state of the FtsZ ring.

3. Filament bending (Schematic S6C): If all polygon edges have two filaments bound and all residual bent filaments have dissociated, bend the edges of the newly completed polygon. When the filaments bend, their length does not change, and the amount of bending is only suficient to form a new circle. The new circumference is therefore equal to the old polygon’s perimeter. Each fragment is now an arc. For simplicity, all of the GTP molecules in the pair of filaments at a particular edge hydrolyze at the same time. In this version of the model, all filaments are of a fixed length. When they are joined end-to-end to form a regular polygon, the polygon may not fully inscribe the entire circumference. This remaining portion of the circumference does not bend when the polygon does. It is preserved and accounted for in the next iteration.

(a) Randomly determine whether to bend the filaments, such that the probability of bending each edge is $k _ { \mathrm { h y d } }$ Bending at an edge can only take place if there are suficient water molecules available to hydrolyze all of the GTP molecules in the two filaments.

(b) Update the state of the the FtsZ ring and change the bent filament from FtsZ-GTP to FtsZ-GDP.

(c) If all the edges have been bent, calculate the new pinched diameter of the cell:

$$
{ \begin{array} { r } { { \mathrm { D i a m e t e r } } _ { \mathrm { A f t e r H y d r o l y s i s } } = { \frac { \mathrm { c i r c u m f e r e n c e } } { \pi } } } \\ { = { \frac { \mathrm { n u m E d g e s } \times L } { \pi } } } \end{array} }
$$

Adjust this diameter to account for the polygon not perfectly inscribing the cell circumference by adding back the length of the old perimeter not accounted for by the inscribed polygon.

4. Bent filament dissociation I (Schematic S6D): If all the filaments have been bent, dissociate one bent filament from each polygon edge. The other ring must remain to preserve pinching progress by maintaining the new smaller circumference.

(a) Randomly dissociate bent FtsZ-GDP filaments such that the probability of dissociating each filament is equal to $k _ { \mathrm { u n b i n d } }$

(b) Dissociate unbound FtsZ-GDP filaments into FtsZ-GDP monomers.

(c) Upon each dissociation event, update the state of the FtsZ ring.

5. Termination: If the pinched diameter is smaller than the length of one filament, conclude cytokinesis.

## 3.4 DNA Damage

## Biology

DNA is not absolutely stable. Rather, DNA is susceptible to spontaneous modification including base loss and deamination. DNA is also susceptible to modification by many exotic agents including UV-A and UV-B radiation, α-, β-, and γ-radiation, oxygen, hydroxyl, carbon, and nitrogen radicals, and alkylating agents. These diverse DNA modification modes generate equally diverse DNA structures including missing and modified sugar-phosphates, missing and modified nucleobases, intra- and inter-strand cross links, and strand breaks. Table S3O lists the modeled causes and types of DNA damage.

DNA damage is an evolutionarily important source of genetic variation. However, damaged DNA has also been shown to deleterious to many processes including transcription and replication<sup>780–783</sup>. Consequently, cells employ dedicated DNA repair machinery. See Section 3.5 for further discussion. The exact efect of DNA damage on physiology is not well characterized. Tornaletti and Hanawalt have extensively reviewed the efects of several specific DNA modifications on transcription<sup>781–783</sup>.

## Reconstruction

DNA damage modes were reconstructed based on a review by Lindahl and Barnes<sup>462</sup> and the primary literresultant base configuration, metabolite stoichiometry, and kinetic rate of each DNA damage reaction.

## Computational Representation

## Mathematical Model

Because DNA damage is rare, this process models each DNA damage reaction as an independent Poisson process. The rate, $r _ { i } ,$ of each spontaneous DNA damage reaction i is given by the observed specific rate $k _ { i } .$ The rate, $r _ { i } ,$ of each DNA damage reaction i caused by radiation $j$ is given by the product of the experimentally observed specific rate, $k _ { i } .$ , and the radiation flux, $s _ { j }$

$$
r _ { i } = k _ { i } s _ { j } .\tag{S11}
$$

Chemically-induced damage reactions were reconstructed, but not modeled because M. genitalium is not typically cultured with DNA damaging agents.

## Integration

The Chromosome state represents the copy number, modification status, and protein occupancy of each chromosome. The Metabolite state represents the copy number of each metabolite. The Stimulus state represents the fluxes of six types of radiation: α-, $\beta -$ , and γ-particles, electrons, protons, and UV-A and UV-B.

The Metabolism process models the generation of hydroxyl radicals. The DNA Repair process models four DNA repair pathways: direct damage reversal, base excision repair, nucleotide excision repair, and homologous recombination. The DNA Repair process also models DNA methylation at restriction/modification (R/M) sites. All DNA modifications except methylations of R/M sites are assumed to impede protein DNA-binding.

## Initial Conditions

The Chromosome state initializes one chromosome, fully methylated at R/M sites and otherwise unmodified.   
Several other processes including Transcription initialize the protein occupancy of the chromosome.

## Dynamic Computation

Algorithm S5 outlines the implementation of the DNA damage model.

Algorithm S5 | DNA damage simulation. See the Mathematical Model section above and List S2 for definition of the   
mathematical notation.   
Input: $m _ { i }$ copy number of metabolite i   
Input: $M _ { i j }$ stoichiometry of metabolite i in reaction j   
Input: $z _ { i } ^ { g } , z _ { i } ^ { a } , Z _ { \bullet i } ^ { p } , Z _ { \bullet i } ^ { b } , z _ { i } ^ { c }$ , and $z _ { i } ^ { s } \colon$ final base configuration resulting from reaction i   
foreach DNA modification reaction i do   
Calculate base modification rate   
switch trigger of reaction i do   
case spontaneous   
$\lfloor \ r _ { i } \gets k _ { i }$   
case radiation   
$j \gets$ index of radiation trigger   
$\boldsymbol { r } _ { i } \gets k _ { i } \boldsymbol { s } _ { j }$   
foreach base $j$ in strand k of chromosome l susceptible to reaction i in a random order do   
if insuficient metabolic resources to support reaction $i \ ( \exists \ j \ s . t . \ m _ { j } \ < \ - M _ { j i } )$ then   
break   
if poissonRand $( r _ { i } ) \geq 1$ then   
Update the configuration of base $j$ of strand k of chromosome k   
$m _ { j k l } ^ { g }  z _ { i } ^ { g }$   
$m _ { j k l } ^ { a }  z _ { i } ^ { a }$   
$m _ { j k l \bullet } ^ { \check { p } }  Z _ { \bullet i } ^ { p }$   
$m _ { j k l \bullet } ^ { b }  Z _ { \bullet i } ^ { b }$   
$m _ { j k l } ^ { c }  z _ { i } ^ { c }$   
$m _ { j k l } ^ { s }  z _ { i } ^ { s }$   
Update metabolite copy numbers: $m \gets m + M _ { \bullet i }$

## 3.5 DNA Repair

## Biology

DNA is susceptible to several intrinsic and extrinsic modes of damage (see Section 3.4). Because damaged DNA is deleterious to many processes including transcription and replication<sup>780–783</sup>, organisms have evolved specialized machinery to detect and repair damaged DNA. Eisen and Hanawalt have shown that the M. genitalium genome contains the DNA damage sensor DisA and four DNA repair pathways: direct damage reversal (DDR), base excision repair (BER), global genomic nucleotide excision repair (GG-NER), and homologous recombination double strand break repair (HR-DSBR)<sup>891</sup>. In addition, M. genitalium employs the type II restriction/modification $( \mathrm { R } / \mathrm { M } )$ system MunI to selectively degrade foreign DNA.

## Reconstruction

## Damage Recognition

M. genitalium employs only one dedicated machine – DisA (MG105) – to recognize DNA damage. Bejerano-Sagie et al. have shown that B. subtilis DisA recognizes strand breaks, base damage, and cross links<sup>513</sup>. The mechanism of DisA damage recognition is not well understood. DisA is believed to signal DNA damage through the absence of the second messenger cyclic-di-AMP. In the absence of DNA damage, DisA cyclizes ATP to cyclic-di-AMP. In the presence of DNA damage, DisA is believed to bind DNA, adopt a catalytically inactive conformation, and via an unknown mechanism possibly involving cyclic-di-AMP and the transcrip tional regulator Spo0A, delay sporulation. M. genitalium, however, does not have most of the downstream signaling machinery associated with B. subtilis DisA-dependent sporulation delay.

## Direct Damage Reversal

DNA ligation is the only DDR pathway employed by M. genitalium<sup>891</sup>. DNA ligation is catalyzed by DNA ligase LigA (MG254) by a NAD-dependent mechanism. DNA ligase repairs single strand breaks as well as ligates DNA synthesized during replication, BER, NER, and HR.

## Base Excision Repair

The primary role of BER is to repair small patches of oxidized nucleobases<sup>487,488,718</sup>. M. genitalium BER repairs single damaged nucleobases. M. genitalium does not undergo long patch BER because M. genitalium does not have a flap endonuclease.

M. genitalium BER repairs DNA via a four step mechanism. First, glycosylase Fpg (MG498) or Ung (MG097) hydrolytically cleaves the glycosidic bond between the damaged nucleobase and the DNA backbone, creating an abasic site. Second, two parallel subpathways cleave the phosphodiester bonds 3’ and 5’ to the abasic site, introducing a gap site. The first subpathway begins with cleavage of the 3’ phosphodiester bond site by AP lyase Fpg and ends with cleavage of the 5’ phosphodiester bond by 5’-deoxyribosephosphodiesterase Nfo. The second subpathway begins with cleavage of the 5’ phosphodiester bond by 5’-AP endonuclease Nfo (MG235) and ends with cleavage of the 3’ phosphodiester bond by 3’-(deoxyribose-5’-phosphate) lyase DnaN (MG001). Third, DNA polymerase DnaN restores the missing base using the template provided by the opposite strand. Finally, DNA ligase ligates the inserted base.

## Nucleotide Excision Repair

The primary role of NER is to repair bulky distortions in the shape of the DNA helix of up to 12-13 bases in length caused by UV radiation and nitric oxide. M. genitalium NER provides global protection against small DNA lesions. M. genitalium does not undergo transcription-coupled NER because M. genitalium does have the transcription-repair coupling factor mfd. Compared to BER, NER employs less specific endonucleases and consequently has broader repair capacity.

M. genitalium NER repairs DNA via a four step mechanism. First, UvrABC (MG421, MG073, MG206) identifies a DNA lesion and cleaves the phosphodiester bonds 6-7 bases 3’ and 5’ to the lesion. Second, helicase PrcA excises the cleaved DNA. Third, DNA polymerase DnaN (MG001) restores the missing bases using the template provided by the opposite strand. Finally, DNA ligase ligates the inserted base.

## Homologous Recombination Double Strand Break Repair

HR repairs double strand breaks caused by ionizing radiation and stalled replication forks. HR also repairs strand gaps generated by the interaction of replication forks with unrepaired lesions<sup>797</sup>. M. genitalium has a very reduced complement of recombination repair proteins. Recombination repair is modeled as an eight step process:

1. Initiation: 5’-3’ exonuclease removes dNMPs from the 5’ ends of the strand break, leaving 3’ overhangs of at least 8 bases<sup>526</sup>. No traditional initiation gene has been identified in M. genitalium. We assumed that polI-like 5’-3’ exonuclease (PolA, MG262) is the M. genitalium HR initiator.

2. Strand exchange: RecA (MG339) catalyzes the formation of a Holliday junction between one of the damaged 3’ overhands and the undamaged homologous chromosome.

3. Polymerization: DnaN (MG001) polymerizes DNA guided by the undamaged chromosome template.

4. Ligation: LigA (MG254) ligates the newly produced DNA.

5. Second strand exchange: RecA catalyzes the formation of a second Holliday junction.

6. Holliday junction migration: RuvA and RuvB widen the distance between the two strand cross over points by moving the Holliday junctions to the preferred sequence 5’-[AT]TTN[GC]-3’<sup>532</sup>.

7. Resolution: RecU nicks the DNA at the cross over points, creating four single strand breaks.

8. Ligation: LigA ligates the four strand breaks.

Additionally, HR is believed to be critical for M. genitalium antigenic variation<sup>797</sup>.

## Restriction/Modification

Organisms employ R/M systems to distinguish foreign from self DNA. These systems maintain self DNA in a fully methylated configuration by methylating self DNA during chromosomal replication and cleaving unmethylated foreign DNA which has not been exposed to self DNA methylases. M. genitalium contains a reduced R/M system consisting of the type I DNA recognition subunit EcoD (MG438) and the type II methylase MunI (MG184). EcoD is the DNA binding domain of a type I multimeric methylation and restriction complex which recognizes the sequence $5 ^ { 3 } - \mathrm { T C A R T T C - 3 ^ { 3 } }$ Because M. genitalium contains only the DNA recognition subunit and not the methylation and restriction subunits, we do not model type I R/M. MunI methylates the third base of both strands of the palindromic sequence 5’-CAATTG-3’, producing N<sup>6</sup>- methyladenine. Because M. genitalium does not contain a separate type II endonuclease and because type II R/M systems are often monomeric, we assumed MunI also has restriction activity.

## Metabolism of Damaged Nucleo-bases, -sides, and -tides

The metabolic byproducts of DNA repair are salvaged by oligonucleases. However, the mechanism of M. genitalium oligonucleotide salvage is not well understood. No gene has been identified which cleaves DNA oligonucleotides. Candidate oligonucleotide salvage genes include pcrA (MG244), mgpA (MG190), and polA (MG262). Of these genes, we assumed that mgpA is responsible oligonucleotide salvage. Individual damaged nucleotides are further metabolized and exported. See Section 3.10 for further discussion.

## Reaction Stoichiometry & Kinetics

The DNA specificity and geometry, stoichiometry, and kinetics of each DNA repair reaction were reconstructed based on an extensive review of the primary literature<sup>72,82,84,96,195,487,488,511–516,525,526,532,538,542,652,</sup> <sup>653,707,708,714,718,719,733,742,743,780</sup>. Table S3O lists the reconstructed stoichiometry and kinetics of each reaction. Table S3D lists the reconstructed DNA specificity and geometry of each DNA repair reaction.

## Computational Representation

## Mathematical Model

This process models four DNA repair pathways and methylation and restriction of MunI R/M sites. Because DNA repair is not well understood on the genomic level, this process makes several simplifying assumptions. First, this process represents each step in DNA repair, methylation, and restriction as a separate reaction, and assumes that each reaction is independent. Consequently, the rate of each reaction is determined only by the configuration of the DNA. Second, this process assumes that the mean arrive rate, $v _ { i } ,$ of each reaction i is independently limited by (1) the copy numbers of intracellular metabolites, $m _ { j } ,$ and (2) the DNA repair enzyme copy numbers, $e _ { j }$ . Based on these assumptions, the function form of $v _ { i }$ is given by

$$
v _ { i } = \operatorname* { m i n } \left( \left| \begin{array} { c } { { \overbrace { \overbrace { m _ { j } } } } } \\ { { \overbrace { M _ { j i } ^ { s } } } } \\ { { j } } \end{array} \right| , \ \left| \overbrace { \mathrm { p o i s s o n R a n d } \left( \underbrace { e _ { j } } _ { K _ { j i } } \Delta t \right) } ^ { \mathrm { e n z y m e s } } \right| \right) ,\tag{S12}
$$

where $M _ { j i }$ is the stoichiometry of metabolite $j$ in reaction i, $M ^ { s } = \operatorname* { m a x } { ( 0 , - M ) }$ is the negative part of $M .$ $K _ { j i }$ is the experimentally observed catalytic rate of enzyme $j$ in reaction i, and $\Delta t = 1 \mathrm { s }$ is the simulation time step.

This process also stochastically models the binding of free DisA to DNA lesions.

## Integration

The Chromosome state represents the copy number, modification status, and protein occupancy of each chromosome. The Protein Monomer and Protein Complex states represent the free and DNA-bound copy numbers of each protein species. The Metabolite state represents the copy number of each metabolite.

The DNA Damage process models spontaneous and chemical- and radiation-induced DNA modification. The Metabolism process models DisA diadenylate cyclase activity and modified nucleotide catabolism.

## Initial Conditions

The Chromosome state initializes one chromosome, modified only at R/M sites. Several other processes including Transcription initialize the protein occupancy of the chromosome.

## Dynamic Computation

Algorithm S6 outlines the implementation of the DNA repair model.

Algorithm S6 | DNA repair simulation.   
Repair, methylate, and restrict DNA   
foreach reaction i in a random order do   
foreach base j of strand k of chromosome l susceptible to reaction i in a random order do   
if suficient enzymatic and metabolic resources to support reaction i then   
Execute reaction i   
Update DNA configuration   
Update metabolite copy numbers   
Decrement enzymatic capacity   
Bind DisA to damaged DNA   
while there is free DisA and at least 1 DisA-accessible DNA lesion do   
Let i, j, k ← represent the base, strand, and chromosome of a DisA-accessible DNA lesion   
Bind DisA to base i of strand j of chromosome k

## 3.6 DNA Supercoiling

## Biology

DNA naturally exists at a certain level of helicity, and this level of helical density is important for the DNA’s stability, its ability to fit in the cell, and its ability to bind proteins<sup>693</sup>. DNA supercoiling can also have an efect on RNA transcription rates as the helicity of the DNA may make given genes more or less accessible<sup>920</sup>.

## Reconstruction

M. genitalium has three topoisomerase proteins: DNA gyrase, topoisomerase I, and topoisomerase IV. These proteins transiently break a DNA strand to wind (topoisomerase I) or unwind (topoisomerase IV, gyrase) the DNA. The opposing actions of the topoisomerase enzymes help maintain a stable level of DNA helicity<sup>694</sup>. This is especially important during replication because while the replication loops progress along the chromosome unwinding the DNA, the coils that previously existed in the DNA persist and accumulate downstream of the replication loop. This over-coilied region is relieved by the actions of topoisomerases<sup>923</sup>.

All of the enzymes and parameters used in the DNA Supercoiling process class are described in List S11 and List S12.

List S11. Enzymes and complexes used in the DNA Supercoiling process class.
<table><tr><td>Enzyme/Complex</td><td>Composition</td><td>Gene Name(s)</td><td>DNA Footprint (nt)</td></tr><tr><td>DNA gyrase</td><td>) MG003, (2) MG004</td><td>gyrB, gyrA</td><td>140</td></tr><tr><td>Topoisomerase IV</td><td>) MG203, (2) MG204</td><td>parE, parC</td><td>34</td></tr><tr><td>Topoisomerase I</td><td>(1) MG122</td><td>topA</td><td>19</td></tr></table>

List S12. Fixed parameters used in the DNA Supercoiling process class.
<table><tr><td>Parameter</td><td>Value</td><td>Symbol</td><td>Source</td></tr><tr><td>Supercoiling</td><td></td><td></td><td></td></tr><tr><td>Bases per turn in relaxed DNA</td><td>10.5</td><td></td><td></td></tr><tr><td>Equilibrium superhelical density</td><td>-0.06</td><td> $\sigma _ { 0 }$ </td><td></td></tr><tr><td>Supercoils introduced by 1 gyrase strand passing event</td><td>-2</td><td> $\delta _ { \mathtt { g y r } }$ </td><td>[695]</td></tr><tr><td>Supercoils introduced by 1 topoisomerase I strand passing event</td><td>1</td><td> $\delta _ { \mathsf { t o p l } }$ </td><td>[502]</td></tr><tr><td>Supercoils introduced by 1 topoisomerase IV strand passing event</td><td>-2</td><td> $\delta _ { \sf t o p I V }$ </td><td>[922]</td></tr><tr><td>Strand passing events rate per gyrase</td><td> $1 . 2 { \mathsf { s } } ^ { - 1 }$ </td><td> $k _ { \mathrm { g y r } }$ </td><td>[922]</td></tr><tr><td>Strand passing events rate per topoisomerase I</td><td> ${ { 1 \varsigma } ^ { - 1 } }$ </td><td> $k _ { \tt t o p l }$ </td><td>[502]</td></tr><tr><td>Strand passing events rate per topoisomerase IV</td><td> $2 . 5 \mathsf { s } ^ { - 1 }$ </td><td> $k _ { \tt t o p I V }$ </td><td>[750]</td></tr><tr><td>ATP hydrolyzed per gyrase-catalyzed strand passing event</td><td>2</td><td> $E _ { \mathrm { g y r } }$ </td><td>[751]</td></tr><tr><td>ATP hydrolyzed per topoisomerase I-catalyzed strand passing event</td><td>0</td><td> $E _ { \mathsf { t o p l } }$ </td><td>[922]</td></tr><tr><td>ATP hydrolyzed per topoisomerase IV-catalyzed strand passing event</td><td>2</td><td> $E _ { \mathrm { t o p l V } }$ </td><td>[922]</td></tr><tr><td>Superhelical denisty above which gyrase acts</td><td>-0.1</td><td> $T _ { \mathrm { g y r } }$ </td><td>[922]</td></tr><tr><td>Superhelical denisty above which topoisomerase I acts</td><td>0</td><td> $T _ { \mathrm { t o p l } }$ </td><td>[502]</td></tr><tr><td>Superhelical density below which topoisomerase II acts</td><td>0</td><td> $T _ { \mathrm { t o p I V } }$ </td><td>[922]</td></tr><tr><td>Gyrase logistic function steapness parameter</td><td>100</td><td> $L _ { \mathrm { g y r } }$ </td><td>Fit</td></tr><tr><td>Topoisomerase I losgistic function steapness parameter</td><td>-100</td><td> $L _ { \mathsf { t o p l } }$ </td><td>Fit</td></tr><tr><td>Number of bases in the chromosome</td><td>580076</td><td></td><td></td></tr><tr><td>Enzyme DNA footprints Processivity</td><td>See List S11</td><td></td><td>[693695]</td></tr><tr><td>Mean time gyrase stays bound to the DNA</td><td></td><td></td><td></td></tr><tr><td>Supercoiling&#x27;s Effect on Gene Expression</td><td>45 s</td><td></td><td>[922]</td></tr><tr><td>Slopes of linear fit of gyrase σ-gene expression data</td><td>42.8</td><td></td><td>[920]</td></tr><tr><td>Slopes of linear fit of topoisomerase I σ-gene expression data</td><td>-7.4</td><td></td><td></td></tr><tr><td>Slopes of linear fit of topoisomerase IV σ-gene expression data</td><td>1.1</td><td></td><td>[920] [920]</td></tr><tr><td>y-intercepts of linear fit of gyrase σ-gene expression data</td><td>3.57</td><td></td><td></td></tr><tr><td>y-intercepts of linear fit of topoisomerase I σ-gene expression data</td><td>0.56</td><td></td><td>[920]</td></tr><tr><td>y-intercepts of linear fit of topoisomerase IV σ-gene expression data</td><td></td><td></td><td>[920</td></tr><tr><td>σ bounds for applying linear fit of gene expression data</td><td>1.07 -0.08, 0.07</td><td>σlower, σupper</td><td>[920] Fit</td></tr></table>

## Parameter Assignment

The logistic function parameters $( L _ { \mathrm { g y r } } , \ L _ { \mathrm { t o p I } } )$ were fit such that the equilibrium superhelical density, $\sigma _ { 0 } ,$ could be maintained while still allowing both gyrase and topoisomerase I to act at the equilibrium $\sigma _ { 0 } .$ Linear fits were approximated for gene expression data experimentally measured at varying σ. The upper and lower bounds of σ for applying the linear fit of the σ-gene expression data $( \sigma _ { l o w e r } , \sigma _ { u p p e r } )$ were set in there range where a linear fit was appropriate for the data.

## Computational Representation

The supercoiling of the DNA is quanitfied using a metric known as the DNA linking number, LK. The $L K _ { \mathrm { r e l a x e d } }$ is defined as (# of base pairs)/10.5, where 10.5 is the number of bases per turn in a relaxed double helix. The $L K _ { \mathrm { c u r r e n t } }$ may deviate from the $L K _ { \mathrm { r e l a x e d } }$ due to the actions of topoisomerases and the progression of replication. The ∆LK is defined as the diference between the current level of DNA supercoiling and the relaxed level of DNA supercoiling. DNA gyrase and topoisomerase IV each require 2 ATP to induce 2 negative supercoils each time they act<sup>236</sup>. Topoisomerase IV induces positive supercoils relatively rarely and its positive coiling activity is therefore not considered in our model<sup>236</sup>. Topoisomerase I acts to induce positive supercoils<sup>502</sup>. Gyrase, topoisomerase IV, and topoisomerase I act at rates of 1.2, 2.5, and 1 strand passing events per second respectively<sup>502,750,922</sup>.

The helicity of diferent regions on the DNA are modeled separately. Before replication, the entire chromosome is represented as one region. During replication, two additional regions are defined and accounted for: the replicated DNA upstream of the replication loops on each of the two chromosomes (see Schematic S7). During replication, the unreplicated region of DNA (region downstream of the two replication loops) is shrinking in terms of number of bases (see Schematic S7), and as a result, the $L K _ { \mathrm { r e l a x e d } }$ decreases. However, as the DNA replicative helicases unwind the DNA they push the existing coils into this region, and there are more coils for fewer bases. This over-coiled region has a $L K _ { \mathrm { c u r r e n t } }$ that is too high, and must be brought down towards the $L K _ { \mathrm { r e l a x e d } }$ . Gyrases and topoisomerases help bring the DNA back to the relaxed state by inducing negative supercoils. It is assumed that the newly replicated DNA is made in the relaxed state: $L K _ { \mathrm { c u r r e n t } } = L K _ { \mathrm { r e l a x e d } }$ , but the supercoiling enzymes act in this region as well, helping maintain equilibrium helicity. It is essential that the $\Delta L K$ in the region downstream of the replication loops be brought down to 0 by the end of replication. After replication is complete, only the two replicated regions exist (2 separate chromosomes). While in general, DNA supercoiling involves the regions described above, DNA damage and other processes can cause gaps in the DNA that result in additional regions.

![](images/2d65836d0a3d4ac35810de151ccaab162a4492feccaa1551d2e2326994bc936f.jpg)  
Schematic S7. Regions of varying superhelical density on the replicating chromosome.

The superhelical density of a DNA region, $\sigma ,$ is defined as the $( L K _ { \mathrm { c u r r e n t } } - L K _ { \mathrm { r e l a x e d } } ) / L K _ { \mathrm { r e l a x e d } }$ . Experimentally it has been shown that the steady state superhelical density, $\sigma _ { 0 } .$ is $- 0 . 0 6 ^ { 9 2 3 }$ The activity of topoisomerases depends on the $\sigma$ of the $\mathrm { D N A } ^ { 9 2 2 }$ Although there is likely a more complex relationship between the DNA supercoiling and enzyme activity, enzyme activity is modeled as a set of step functions and logistic functions (see Schematic S8). It is known that the topoisomerases are unable to act beyond certain σ thersholds (gyrase can only act above $T _ { \mathrm { g y r } }$ , topoisomerase IV can only act above $T _ { \mathrm { t o p I V } }$ , and topoisomerase I can only act below $T _ { \mathrm { t o p I } } )$ , so the activities of the topoisomerases outside of the thresholds are set to $\mathrm { z e r o } ^ { 9 2 2 }$ However, the exact enzyme activity profiles within these bounds is unknown. Fitting a logistic function within the thresholds of gyrase and topoisomerase I allows the maintainance of $\sigma$ approximately near $\sigma _ { 0 }$ Topoisomerase IV is not active near $\sigma _ { 0 }$ and therefore acts more rarely than the other topoisomerases. As a result, there was no need to assume a logistic profile for its activity. The proportion of full activity for each topoisomerase was obtained from the profiles. This proportion was multiplied by the maximal activity to determine the number of strand passing events for each topoisomerase for a given timestep.

Data from Peter <sup>et</sup> <sup>al.</sup> 2004 Fold change profile used in model

![](images/d10a669094ead4b865cc0f2e6d38f308379921c6ce25a8cb52d9049e3672d4c8.jpg)  
Schematic S8. Enzyme activity profiles.

Further, the model keeps track of enzyme processivity, or how long an enzyme can remain bound to the DNA and continue to act. Topoisomerase IV and DNA gyrase are highly processive and may perform several strand-passing events before falling of of the DNA. Topoisomerase I is not highly processive, it acts on the DNA and falls back of right away.

Finally, it has been shown that there is an efect of supercoiling on transcription rates, and experimental data in E. coli compares superhelical density to fold change of gene expression<sup>920</sup>. While expression fold changes at diferent superhelical densities have been calculated for many E. coli genes, none have been measured for M. genitalium, and therefore only the efects of supercoiling on the expression of the 5 supercoiling genes gyrB, gyrA, parC, parE, and topA, are included. These genes exist in 3 transcription units. Peter et al. have E. coli data for the fold change of expression (microarray data) of each of these genes at various values of σ (ranging from σ -0.06 to 0.02) at various experimental conditions<sup>920</sup>. Despite the large variation of data in a narrow σ range, we have decided to use linear fits of the data, as they fit the general trends in the data: increased helicity leads to decreased or increased gene expression. The linear fits are constrained such that the fold change is 1, at equilibrium σ, -0.06. The linear fits are extrapolated between the σ range of -0.08 to 0.07, where all the fold changes remain above 0. Outside of this range, a constant fold change of expression is estimated. While there is a separate set of data for each of the 5 genes, the Transcription process class requires a single probability of transcription for each transcription unit. The data for the first gene in each transcription unit is used (gyrB and parE). topA is transcribed with genes that are not supercoiling related. The expression of those genes (MG119, MG120, MG121) is also afected by supercoiling. The general trend is that gyrase and topoisomerase IV will have an increased expression when σ is higher than the equilibrium, and that topoisomerase I will have a higher expression when σ is lower than the equilibrium. The profiles of fold change in promoter binding probabilities for varying σ can be seen in Schematic S9.

![](images/2b0784ed99260f73d068a17241212ac08754b048af28c489939b6ef8d5cc4e44.jpg)

![](images/1b6da09b1017e3fe78ea3a340021cea4d15b96751c46c48987b074984d07f1c0.jpg)

![](images/99c997044eb481410c6a941b18b509203ace2b9221a3366a6336af70ef1fd7db.jpg)  
Schematic S9. Fold change in the probability of RNA polymerase-gene promoter binding for three transcription units.

List S13. State classes connected to the DNA Supercoiling process class.
<table><tr><td>Connected State</td><td>Read from state</td><td>Written to state</td></tr><tr><td rowspan="3">Chromosome</td><td>Accessible positions on the DNA for topoisomerases to bind</td><td>Positions where topoisomerases are bound</td></tr><tr><td>Start positions of transcription units affected by supercoiling Linking number, length, and start sites of</td><td>Fold change of transcription unit-RNA polymerase binding probabilities</td></tr><tr><td>regions of DNA (considered independently in terms of superhelical density)</td><td>Updated linking number of regions of DNA</td></tr></table>

## Initial Conditions

At the start of the simulation, the entire chromosome exists in a single double stranded region. The linking number of this region is set such that the superhelical density is at equilibrium, -0.06. All of the existing gyrase are bound to randomly designated positions around the chromosome. The transcription probabilities of the afected transcription units are adjusted according to the superhelical density.

## Dynamic Computation

The activities of DNA gyrase, topoisomerase I, and topoisomerase IV, and the progress of replication loops can all afect the linking number (and superhelical density) of the DNA. The DNA Supercoiling process class, evaluates the efects of all the free topoisomerases in random order, determines what regions they can bind in, and randomly binds them to large enough open positions on the DNA. The linking number is then adjusted based on the actions of all the bound enzymes, and the usage of ATP is determined. The processivity of gyrase and topoisomerase IV are also tracked so that they can be unbound from the DNA when appropriate.

## Algorithm

## 1. Determine regions of DNA

The superhelicity of the chromosome is tracked separately for diferent each double stranded region. The exact base positions and length in base pairs, l, of each region is determined based on the progress of replication and positions of breaks in the DNA. If there are no breaks in the DNA, the following DNA regions exist:

Before Replication:

• Region 1: Unreplicated DNA

## During Replication:

• Region 1: Replicated DNA, Chromosome 1 (upstream of replication loops, increasing in length over time)

• Region 2: Replicated DNA, Chromosome 2 (upstream of replication loops, increasing in length over time)

• Region 3: Unreplicated DNA (downstream of replication loops, decreasing in length over time)

## After Replication:

• Region 1: Replicated DNA, Chromosome 1

• Region 2: Replicated DNA, Chromosome 2

## 2. Calculate σ at each DNA region

The enzymes may act on the chromosome afecting the $L K _ { \mathrm { c u r r e n t } }$ , and experimentally it has been shown that the enzymes would obtain an $L K _ { \mathrm { c u r r e n t } }$ such that the steady state $\sigma = - 0 . 0 6 ^ { 9 2 3 }$ . For each region of DNA, the $L K _ { \mathrm { c u r r e n t } }$ is stored across timesteps. The superhelical density, $\sigma ,$ of each region is calculated using the $L K _ { \mathrm { c u r r e n t } } { \mathrm { a s } }$ follows:

$$
\begin{array} { r } { L K _ { \mathrm { r e l a x e d } } = \cfrac { l } { 1 0 . 5 } \qquad } \\ { \sigma = \cfrac { L K _ { \mathrm { c u r r e n t } } - L K _ { \mathrm { r e l a x e d } } } { L K _ { \mathrm { r e l a x e d } } } } \end{array}
$$

## 3. Determine which topoisomerases can act in which DNA regions

Gyrase, topoisomerase I, and topoisomerase IV can only act on the DNA if the superhelical density (σ) is within a certain range. A combination of step functions and logistic functions were used to determine the activity of the enzymes for a given σ. The activity profiles can be seen in Schematic S8. An enzyme can act in a DNA region if its activity profile is greater than zero at the current σ.

## 4. Unbind Processive Enzymes

Topoisomerase IV and DNA gyrase are processive enzymes meaning that they may perform several strandpassing events before falling of of the DNA. Topoisomerase I is not highly processive, it acts on the DNA and immediately dissociates<sup>922</sup>.

Topoisomerase IV is highly processive and will stay bound to the DNA as long as $\sigma$ is greater than zero.

• For each region, if $\sigma \leq 0 .$

• unbind all Topoisomerase IVs

Gyrase will stay bound to the DNA for about 30-60 s. Gyrase processivity is modeled as a Poisson distribution with $\lambda = 4 5 \mathrm { s }$

• For each bound gyrase,

• if rand < 1/λ, unbind gyrase.

## 5. Bind Enzymes to Each Region

Topoisomerases may bind to the DNA without acting on the DNA. Therefore, binding is only limited by the availability of free topoisomerases and space on the DNA.

• Randomize the order of binding each of the three topoisomerases, to fairly allocate space on the chromosome

• For each of the three topoisomerases i,

• For each region j where the σ permits topoisomerase i binding,

• Stochastically bind topoisomerases i in region j, up to:

<sup>(</sup>Available positions in DNA region<sub>j</sub> of length > footprint<sub>i</sub>

Number of free topoisomerase<sub>i</sub>

## 6. Calculate new Linking Numbers and Perform Metabolite Accounting

The DNA linking number is afected by the bound topoisomerases, up to the limits of available resources and kinetic rates.

## • For each DNA region j,

• For each of the three topoisomerases i that is able to bind region j given $\sigma ,$

• Count the number of topoisomerase i bound in region $j ~ ( C _ { i j } )$

• Use the logistic/step functions (See Schematic S8) to determine the Probability $( P _ { i j } )$ of topoisomerase i acting in region j at the current σ

• Determine the number of strand passing events $( S _ { i j } )$ for enzyme i in region j, given the kinetic rate of topoisomerasei $( k _ { i } )$ and the energy requirement per strand passing event for topoisomerase i $( E _ { i } )$ :

$$
S _ { i j } = m i n \left\{ { \begin{array} { l l } { r o u n d ( C _ { i j } k _ { i } P _ { i j } ) } \\ { { \frac { \mathrm { a v a i l a b l e \ A T P } } { E _ { i } } } } \\ { { \frac { \mathrm { a v a i l a b l e \ H _ { 2 } O } } { E _ { i } } } } \end{array} } \right.
$$

• Calculate the new linking number $\left( L K _ { \mathrm { c u r r e n t } } \right)$ for region j, given topoisomerase i’s efect on the linking number (δ<sub>i</sub>):

$$
L K _ { \mathrm { c u r r e n t } } = L K _ { \mathrm { c u r r e n t } } + \delta _ { i } S _ { i j }
$$

• Account for used metabolites, ATP and $\mathrm { H _ { 2 } O } .$ , and produced metabolites, ADP, Pi, and $\mathrm { H ^ { + } }$

• Unbind all topoisomerase I, a non-processive enzyme

## 7. Determine the efects of supercoiling on transcription

Supercoiling efects the expression of the genes: gyrB, gyrA, parC, parE, and topA, which lie in three transcription units. The DNA Supercoiling process calculates the fold change in the probability of an RNA polymerase binding to the promoters of these transcription units.

• For each topoisomerase transcription unit i,

• Find the double stranded region where transcription unit i lies and the σ of this region

• Use the fold change profiles (See Schematic S9) to determine the fold change in probability of polymerase binding to transcription unit i

## 3.7 FtsZ Polymerization

## Biology

Cell division in many bacterial species requires the assembly of an FtsZ ring at the cell membrane around the midplane of the cell<sup>217</sup>. FtsZ is a homologue of eukaryotic tubulin that assembles into long polymers. These polymers are typically localized to the center of the cell, forming a membrane-bound ring<sup>217</sup>. FtsZ is a GTPase, and GTP hydrolysis to GDP causes the FtsZ filaments to bend. This bending serves as one of the forces enabling cell division<sup>611</sup>. (For more information about cell division, see the Cytokinesis process class.) GTP only hydrolyzes to GDP at an active site formed at the interface of two FtsZ molecules, meaning that FtsZ polymerization is required for GTPase activity<sup>611</sup>. This process addresses the assembly FtsZ monomers into long polymers.

## Reconstruction

This process addresses the assembly FtsZ (MG224) monomers into long polymers.

All of the parameters used in the FtsZ Polymerization process class are described in List S14.

List S14. Fixed parameters used in the FtsZPolymerization process class.
<table><tr><td>Parameter</td><td>Value</td><td>Symbol</td><td>Source</td></tr><tr><td>Maximum length of an FtsZ filament</td><td>9 subunits</td><td>n</td><td>[611]</td></tr><tr><td>Rate of forward activation of FtsZ by GTP</td><td> $1 . 1 { \mathsf { s } } ^ { - 1 }$ </td><td> $k _ { \mathrm { a c t 1 } }$ </td><td>[200]</td></tr><tr><td>Rate of reverse activation of FtsZ by GTP</td><td> $0 . 0 1 { \mathsf { s } } ^ { - 1 }$ </td><td> $k _ { \mathrm { a c t } 2 }$ </td><td>[200]</td></tr><tr><td>Rate of forward exchange of FtsZ-GTP from FtsZ-GDP</td><td> $1 \times 1 0 ^ { 4 } \mathsf { M } ^ { - 1 } \mathsf { s } ^ { - 1 }$ </td><td> $k _ { \mathrm { e x 1 } }$ </td><td>[164]</td></tr><tr><td>Rate of reverse exchange of FtsZ-GTP to FtsZ-GDP</td><td> $5 \times 1 0 ^ { 3 } \mathsf { M } ^ { - 1 } \mathsf { s } ^ { - 1 }$ </td><td> $k _ { \mathrm { e x } 2 }$ </td><td>[164]</td></tr><tr><td>Rate of forward nucleation of FtsZ-GTP to form a dimer</td><td> $4 . 2 \times 1 0 ^ { 6 } \mathsf { M } ^ { - 1 } \mathsf { s } ^ { - 1 }$ </td><td> $k _ { \mathrm { { n u c 1 } } }$ </td><td>[164, 200]</td></tr><tr><td>Rate of reverse nucleation of FtsZ-GTP to dissociate a dimer</td><td> $4 0 { \mathsf { s } } ^ { - 1 }$ </td><td> $k _ { \mathrm { n u c } 2 }$ </td><td>[164, 200]</td></tr><tr><td>Rates of forward elongation of FtsZ-GTP into polymers of length 3 to 9</td><td> $5 . 1 \times 1 0 ^ { 6 } \mathsf { M } ^ { - 1 } \mathsf { s } ^ { - 1 }$ </td><td> $k _ { \mathrm { e l 1 } }$ </td><td>[164]</td></tr><tr><td>Rates of reverse elongation of FtsZ-GTP from polymers of length 3 to 9</td><td> $2 . 9 \mathsf { s } ^ { - 1 }$ </td><td> $k _ { \mathrm { e } | 2 }$ </td><td>[164]</td></tr></table>

## Computational Representation

Typically, FtsZ polymers of variable length are able to bind the cell membrane to form contractile rings. The mean filament length in E. coli has been measured to be 100 nm (23 FtsZ monomers)<sup>217</sup>. The minimum fragment length observed in C. crescentus is 40 nm (9 FtsZ monomers)<sup>611</sup>. Being such a small organism, we hypothesize that M.genitalium would have filaments on the lower end of what is suficient for contractile force generation. For simplicity of calculating the Cytokinesis progress, we use polymers of a fixed length, 9 subunits<sup>611</sup>.

This process class simulates polymerization of FtsZ-GTP monomers to 9mers. We use a diferential equation model developed by Surovtsev et al. to assemble the polymers<sup>164</sup>. During polymerization, FtsZ-GTP can exist in any intermediate state: 1mer, 2mer, ... 8mer, 9mer. The set of diferential equations models the following reactions:

Activation of FtsZ monomers (F ) to $\mathrm { F t s Z – G T P } \left( F _ { T } \right)$

Deactivation of FtsZ-GTP $\left( F _ { T } \right)$ to FtsZ $( F )$

Exchange of FtsZ-GDP $\left( F _ { D } \right)$ to FtsZ-GTP $\left( F _ { T } \right)$

Reverse exchange of FtsZ-GTP $\left( F _ { T } \right)$ to FtsZ-GDP $\left( F _ { D } \right)$

Nucleation of two FtsZ-GTP molecules $\left( F _ { T } \right)$ to form a dimer $\left( F _ { T 2 } \right)$

Reverse nucleation of a dimer $\left( F _ { T 2 } \right)$ into two $\mathrm { F t s Z – G T P s } \left( F _ { T } \right)$

Polymer elongation adding an FtsZ-GTP $\left( F _ { T } \right)$ to an existing polymer of length 2-8 subunits $\left( F _ { T 2 ^ { - } } F _ { T 8 } \right)$ Reverse elongation removing an FtsZ-GTP $\left( F _ { T } \right)$ from an existing polymer of length 3-9 subunits $( F _ { T 3 } -$ $F _ { T 9 } )$

## Integration

The count full-length activated FtsZ (9mer) filaments is used by the Cytokinesis process class for cell pinching.

## Initial Conditions

The FtsZ polymerization diferential equations are run a number of times (up to 50 iterations) before the simulation starts, to ensure starting at a steady state distribution of polymer lengths. Iterations are run until the change in the solution across consecutive iterations is less than a set tolerance (0.2% of the enzymatic counts).

## Dynamic Computation

FtsZ can exist in one of multiple states: inactivated monomer, activated monomer (GTP bound), nucleated (dimer of two activated FtsZ molecules), elongated polymer of three or more GTP bound FtsZ molecules. The hydrolyzed FtsZ polymers are only considered during cell membrane pinching in the Cytokinesis process class. The FtsZ molecules can move to states of higher and lower polymerization at rates obtained from Chen et al. and Surovtsev et al.<sup>164,200</sup>.

FtsZ polymerization is modeled using a set of diferential equations modified from that described in Surovtsev et al., involving the activation, nucleation, and elongation of FtsZ polymers<sup>164</sup>. The main modifications were that the equations were simplified to not include annealing and cyclization of FtsZ polymers.

The following diferential equation model is evaluated at each timestep:

$$
\begin{array} { l } { { \displaystyle \frac { d F } { d t } = k _ { \mathrm { a c } 2 } P r - k _ { \mathrm { s a t } 1 } P } } \\ { { \displaystyle \frac { d P _ { T } } { d t } = k _ { \mathrm { a c } 2 } k _ { T } \left[ \mathrm { G D P } \right] - k _ { \mathrm { c a t } 1 } k _ { P } \left[ \mathrm { G T P } \right] } } \\ { { \displaystyle \frac { d F _ { T } } { d t } = k _ { \mathrm { a c } 1 } k _ { T } - k _ { \mathrm { s a t } 2 } P r + k _ { \mathrm { c a t } 1 } P _ { T } \left[ \mathrm { G T P } \right] - k _ { \mathrm { s a t } 2 } P r _ { T } \left[ \mathrm { G D P } \right] - 2 k _ { \mathrm { a m i } } P _ { T } ^ { 2 } + \cdots } } \\ { { \displaystyle + \ldots 2 k _ { \mathrm { m a x } 2 } P r _ { T } - k _ { \mathrm { c a t } 1 } T _ { T } \left( \displaystyle \sum _ { i = 2 } ^ { 8 } P r _ { T } \right) + k _ { \mathrm { a t } 2 } \left( \displaystyle \sum _ { i = 3 } ^ { 8 } P r _ { T } \right) } } \\ { { \displaystyle \frac { d F _ { T } } { d t } = k _ { \mathrm { a c } 1 } P _ { T } ^ { 2 } - k _ { \mathrm { a m g } 2 } P r _ { T } - k _ { \mathrm { d i } } P _ { T } \cdot P r _ { 2 } + k _ { \mathrm { a b } 2 } P r _ { T } } } \\ { { \displaystyle \frac { d F _ { T } } { d t } = k _ { \mathrm { a c } 1 } P _ { T } P r _ { T - 1 } - k _ { \mathrm { b i f } } P r _ { T } - k _ { \mathrm { a i l } } P _ { T } P r _ { T } + k _ { \mathrm { c a f } 2 } P r _ { T + 1 } , \mathrm { f o r ~ } i \mathrm { ~ c a s } } } \\ { { \displaystyle \frac { d F _ { T } } { d t } = k _ { \mathrm { a c } 1 } P r _ { T } P r _ { T - 1 } - k _ { \mathrm { a b } 2 } P r _ { T } \cdot P r _ { 1 } - k _ { \mathrm { c a t } } P r _ { T } . } } \end{array}
$$

Solving these equations results in a real-value distribution of monomers and filament lengths at each timestep. The model framework requires the storage of the count of each molecular entity rather than the concentration. This process class discretizes the distribution at each time step for compatibility with the rest of the simulation.

## 3.8 Host Interaction

## Biology

M. genitalium is a common extracellular urogenital epithelial parasite. Although M. genitalium is estimated to colonize the urogenital tract of 3% of all women, most infections are asymptomatic, and most researchers regard M. genitalium as an “ideal parasite” which lives in harmony with its human host<sup>313</sup>. Only a small fraction of M. genitalium infections manifest clinically as urethritis, cervicitis, or pelvic inflammatory disease.

## Reconstruction

Although M. genitalium is a common urogenital pathogen, the pathophysiology of M. genitalium is only beginning to be elucidated. Razin and colleagues have studied the Mycoplasma terminal organelle, and have shown that several lipoproteins (MG191, MG192, MG217, MG318, and MG386) are involved in host adhesion and activation of the host immune response<sup>88,313</sup>. Shimizu et al. and McGown et al. have identified 3 additional lipoproteins – MG149, MG309, and MG412 – which activate the host immune response by stimulating Toll-like (TLR) receptors 1, 2, and 6, which in turn activate the host transcriptional regulator NF-κB<sup>194,842,844</sup>. Additionally, Dufy et al. have reported that MG075 is immunoreactive<sup>176</sup>. Razin and colleagues have suggested that Mycoplasma also stimulates the host immune response by secreting hydrogen peroxide and superoxide radicals which cause membrane oxidative damage and trigger inflammation<sup>313</sup>.

## Computational Representation

## Mathematical Model

Because the interaction between M. genitalium and its human host is not well understood, this process implements a Boolean model of the efect of the M. genitalium terminal organelle and accessory lipoproteins on six properties of the host human urogenital epithelium:

• Adherence – Mycoplasma adheres to its host if its terminal organelle is properly formed and all of its adhesion proteins are expressed.

TLR 1, 2, and 6 activation – Host TLR 1 is activated if the bacterium is adherent and MG149 or MG412 is expressed. TLR 2 is activated if the bacterium is adherent and MG149, MG309, or MG412 is expressed. TLR 6 is activated if the bacterium is adherent and MG309 is expressed.

• NF-κB activation – NF-κB is activated if TLRs 2 and 1 or 6 are active.

• Inflammatory response activation – The host inflammatory response is activated if either NF-κB is active or the bacterium is adherent and at least one of the MG075, MG149, MG309, or MG412 antigens is expressed.

## Integration

The Host state uses six Boolean variables to represent the status of the human urogenital epithelium. The Protein Monomer state represents the copy number of each terminal organelle and accessory lipoprotein synthesized and matured by the protein maturation pathway (see Section 2.10) and translocated into the terminal organelle (see Terminal Organelle Assembly process).

## Initial Conditions

After the Protein Monomer and Terminal Organelle Assembly states initialize the copy number of each protein, the Host state is initialized to the steady-state of the Host Interaction Boolean model. Because the Boolean model is acyclic, the model converges in one iteration.

## Dynamic Computation

At each time step, this process evaluates the six Boolean rules outlined in Algorithm $\mathrm { S 7 }$ until convergence.   
Because the Boolean rules are acyclic, the model converges in one iteration.

Algorithm S7 | Host-parasite interaction simulation.  
adherent ← organelle proteins MG191, MG192, MG217, MG218, MG312, MG317, MG318, and MG386 expressed   
tlr1 ← adherent AND (lipoproteins MG149 and MG412 expressed)   
tlr2 ← adherent AND (lipoproteins MG309 expressed)   
tlr6 ← adherent AND (lipoproteins MG149, MG309, and MG412 expressed)   
nf kb ← tlr2 AND (tlr1 OR tlr6)   
inf lammation ← nf kb OR (adherent AND MG075, MG149, MG309, or MG412 antigen expressed)

## 3.9 Macromolecular Complexation

## Biology

Many enzymes are functional as multimeric proteins or ribonucleoproteins. Macromolecular complexes are believed to form quickly $( k _ { o n } \approx 1 0 ^ { 3 } - 1 0 ^ { 6 } \mathrm { M } ^ { - 1 } \mathrm { s } ^ { - 1 } )$ ), energetically favorably $( \Delta G \approx - 1 2 \mathrm { k c a l m o l ^ { - 1 } } )$ , and stably $( K _ { D } \approx 1 0 ^ { - 4 } - 1 0 ^ { - 1 0 } \mathrm { M } )$ . This process models the formation of all macromolecular complexes except the 30S and 50S ribosomal particles, the 70S ribosome, the FtsZ ring, and the oriC DnaA complex. The Ribosome Assembly, Translation, FtsZ Polymerization, and Replication Initiation processes model the more complex and better characterized formation of these complexes.

## Reconstruction

An extensive review of the primary literature and several databases (see Table S3AI) suggested that M. genitalium forms 201 distinct macromolecular complexes containing 269 protein and 5 RNA gene products<sup>6,96,386,570</sup>. Table S3N lists the reconstructed composition of each M. genitalium macromolecular complex.

## Computational Representation

## Mathematical Model

This process models the formation of macromolecular complexes as a stochastic process. Because macromolecular complexation is poorly understood, this process makes several simplifying assumptions. First, this process assumes that macromolecular complexes form spontaneously, uncoupled to other chemical reactions and without assistance from chaperones or other proteins. The contribution of chaperones to the three dimensional folding of individual protein monomers is modeled by the Protein Folding process. Second, this process assumes that macromolecular complexation is fast and proceeds to completion within the 1 s time step of the simulation. Third, this process makes the simplifying assumption that each macromolecule complex forms with the same specific rate. Fourth, this process assumes that complexes form by simultaneous collision of each subunit. Together these assumptions imply that the relative formation rate, $r _ { i }$ of each complex, i, is described by mass-action kinetics,

$$
r _ { i } = \prod _ { j } \left( \frac { m _ { j } } { V } \right) ^ { S _ { i j } } ,\tag{S13}
$$

where $m _ { j }$ is the copy number of gene product j, V is the cell volume, and $S _ { i j }$ is the stoichiometry of subuni $j$ in complex i. This process models complex formation by (1) calculating the relative formation rate of each complex, $r _ { i } , \ ( 2 )$ randomly forming one complex according to a multinomial distribution defined by the relative formation rates, (3) updating the copy numbers of RNA and protein subunits and complexes, and (4) repeating until insuficient protein and RNA subunits are available to form additional complexes. Importantly, this algorithm resolves the order of macromolecular complex formation before several subunits participate in multiple complexes.

## Integration

The Rna and Protein Monomer states represent the copy number of each RNA and protein subunit synthesized by the RNA and protein synthesis pathways (see Section 2.12 and 2.10). The Protein Complex state represents the copy number of each complex, c<sub>i</sub>. The Geometry state represents the cell volume.

## Initial Conditions

After the cell volume and the total copy number of each RNA and protein gene product are initialized (see Geometry, Rna, and Protein Monomer states), the copy number of each macromolecular complex is initialized by iteratively evaluating the dynamic model until convergence, or more specifically until insuficient subunits are available to form additional complexes.

## Dynamic Computation

Algorithm S8 outlines the implementation of the macromolecular complexation model.

Algorithm S8 | Macromolecular complexation simulation. See Mathematical Model above for mathematical notation.  
repeat   
foreach protein complex i do   
Calculate relative formation rate, $\begin{array} { r } { r _ { i } \gets \prod _ { j } \left( \frac { m _ { j } } { V } \right) ^ { S _ { i j } } } \end{array}$   
Select a complex k to form according to multinomialRand(1, $r _ { i } / \sum _ { i } r _ { i } )$   
Increment copy number of complex $k , c _ { k } \gets c _ { k } + 1$   
Decrement copy numbers of complex k subunits, $m _ { j }  m _ { j } - S _ { k , j }$   
until Insuficient subunits to form additional complexes

## 3.10 Metabolism

## Biology

To grow and replicate cells transform external nutrients into cellular mass. The first step in this process is to import nutrients from the external environment and metabolize those nutrients primarily into macromolecule building blocks. Furthermore, cells must recycle and/or export byproducts. This process models the import of extracellular nutrients and their conversion into macromolecule building blocks.

M. genitalium is believed to have adapted to the rich environment provided by its host human urogenital epithelium by massive degenerative evolution from low G+C content Gram positive bacteria, eliminating non-essential genes involved in oxidative phosphorylation, ATP synthesis via the pentose phosphate pathway, and amino acid, nucleotide, lipid, and cofactor biosynthesis<sup>57,881,883</sup>. Several studies have also shown that M. genitalium has evolved metabolic enzymes with relaxed substrate specificity<sup>444,596,798,882</sup>. M. genitalium is generally cultured on SP-4 medium, a complex and undefined medium based on CMRL-1066<sup>565</sup>.

## Reconstruction

## Extracellular Medium

The in silico medium was based on SP-4 medium with supplementary metabolites added to facilitate in silico growth (see Table S3BI). First, the chemical composition of SP-4 medium was estimated from the characterized composition of each medium component (see Section 2.7 and Table S3BI). Second, additional metabolites were added until the flux-balance analysis (FBA) metabolic model predicted non-zero growth. Finally, the concentrations of several metabolites were increased to support sustained cell growth.

## Cellular Composition

The in silico chemical composition of M. genitalium was based on its reconstructed cellular mass composition (see Table S3AR-S3BG), and fit to match the 27 other modeled cellular processes (see Section 2.5 and 1.3).

## Energy

In addition to metabolic building blocks such as nucleic and amino acids, cellular growth and maintenance requires energy. The in silico M. genitalium growth-associated maintenance energy (GAM) was based on the characterized energetic requirements of E. coli<sup>558</sup>.

## Reactions

The M. genitalium metabolic network illustrated in Figure S1B was reconstructed as previously described<sup>884</sup> with guidance from the M. genitalium FBA metabolic model recently reported by Suthers et al.<sup>610</sup>. Briefly, the metabolic network was reconstructed based on homology to previously modeled organisms<sup>558</sup> and an extensive review of the primary literature. In particular, the metabolic network was reconstructed to support the metabolic demands of all 27 other modeled cellular processes. Table S3O lists the reconstructed metabolic reactions.

## Kinetics

Reaction kinetics were curated primarily from the proteomic databases SABIO-RK<sup>100</sup>, BRENDA<sup>570</sup>, and ${ \mathrm { B i o C y c } } ^ { 6 }$ (see Table S3AL). The maximum exchange rates of carbon- and non-carbon-containing metabolites were set to 12 and 20 mmol $\mathrm { _ { g D C W } ^ { - 1 } h ^ { - 1 } }$ , comparable to recent FBA models of M. genitalium<sup>610</sup> and E. $c o l i ^ { 5 5 8 }$ metabolism.

## Computational Representation

## Mathematical Model

This process models several critical cellular functions including (1) the uptake of external nutrients, (2) the synthesis of the metabolic building blocks and intermediate energy carriers, (3) lipid assembly, membrane insertion, and maturation, and (4) the recycling and export of the metabolic byproducts of other cellular processes. This process makes two key assumptions and uses $\mathrm { F B A ^ { 6 8 6 , 6 8 7 } }$ to model M. genitalium metabolism. In particular, this process calculates the flux, v, of each metabolic reaction. First, this process assumes that the internal dynamics of the metabolome are fast compared to the 1 s time step of the M. genitalium simulation, or equivalently, that the metabolic network can be considered to be at steady-state on the 1 s simulation time scale. Second, this process assumes that the M. genitalium metabolic network maximizes cellular metabolite production given the available extracellular nutrients and metabolic enzymes. See Orth et $a l . ^ { 6 8 7 }$ for further discussion of the assumptions and mathematical formalism of FBA.

To be compatible with the 27 other modeled cellular processes, the metabolic sub-model has four key diferences from most FBA metabolic models. First, the metabolic network, S, and the cellular mass production pseudoreaction are expanded to produce all of the metabolites required by the 27 other processes, where $S _ { i j }$ is the stoichiometry of metabolite i in reaction j and $S _ { i b }$ is the stoichiometry of metabolite i in the cellular mass production pseudoreaction, b. Second, internal exchange reactions are added to recycle the metabolic byproducts of the other processes (e.g. recycle ADP and Pi to ATP), that is to exchange metabolites between the cytosol and the metabolic network. Third, the optimization objective, $^ { g , }$ is expanded to include the construction of new cell mass as well as the recycling and export of the metabolic byproducts of the 27 other processes. g represents the relative fitness gains of intracellular metabolite recycling and novel cell mass production, that is g represents how heavily the metabolic network favors novel cell mass production over metabolite recycling. g was set assuming that the production/exchange of each molecule contributes equally to cellular fitness. Specifically g was set such that the production/exchange of each individual molecule is weighted equally. Fourth, the flux bounds, v<sub>l</sub> are $v _ { u } ,$ are functions of the cell dry mass, m, the copy number and maximum exchange rate of each extracellular metabolite, $n _ { m }$ and $k _ { \pm e x } .$ , the thermodynamics, $\Delta E .$ , of each reaction, and the copy number and maximum catalytic rate of each metabolic enzyme, $n _ { e }$ and $k _ { \pm c a t }$ . Specifically, external exchange flux bounds are functions of the cell dry mass and the extracellular copy numbers and maximum exchange rates of the exchanged metabolites; internal exchange flux bounds are functions of the intracellular copy numbers of the exchanged metabolites; transport and chemical reaction flux bounds are functions of the copy numbers and kinetics of the enzymes and the reaction thermodynamics. Fifth, because the average energy used by the 27 other cellular processes is significantly less than the observed GAM, this process also represents the turnover of the otherwise unmodeled energy consumption.

![](images/8b094595a9ba23aa17dc590ef8dbe22ed14e35206565e402ded1cdcc0b1fc42f.jpg)

![](images/7866f3117817ad340378a0c78d19725a2d5fc7ccabb7da89e85619990038b01f.jpg)  
Schematic S10. Metabolite perspective of the flux-balance analysis (FBA) metabolic model. a, Conventional FBA metabolic model. b, Integrated FBA metabolic model.

$$
v ^ { * } = \underset { v } { \mathrm { a r g m a x } } \ g ^ { \mathsf { T } } v \ \mathrm { s u b j e c t \ t o }\tag{S14}
$$

Sv = 0 and

v<sub>l</sub> $\leq v \leq v _ { u }$ where

$$
g _ { i } = { \left\{ \begin{array} { l l } { - 1 } & { \qquad { \mathrm { r e a c t i o n ~ } } i { \mathrm { ~ r e p r e s e n t s ~ a n ~ i n t e r n a l ~ e x c h a n g e } } } \\ { 0 } & { \qquad { \mathrm { o t h e r w i s e } } } \end{array} \right. }
$$

$$
v _ { l } = f _ { l } \left( m , n _ { m } , k _ { - e x } , - \Delta E , n _ { e } , k _ { - c a t } \right)
$$

$$
v _ { u } = f _ { u } \left( m , n _ { m } , k _ { - e x } , \Delta E , n _ { e } , k _ { - c a t } \right)
$$

Algorithm S9 describes the functional forms of $f _ { l }$ and $f _ { u }$ in detail.

## Integration

The Metabolism process imports extracellular nutrients and converts them into the building blocks of macromolecular synthesis. The Metabolite state represents both the extracellular and cellular copy numbers of each metabolite. The rates of extracellular nutrient exchange are functions of the total cell mass represented by the Mass state and the extracellular metabolite copy numbers. Cytosolic and membrane metabolite copy numbers limit the rates of internal exchange/recycling. The rates of chemical and transport reactions are limited by the copy numbers and kinetics of metabolic enzymes synthesized by the protein synthesis and maturation pathway (see Section 2.10) and represented by the Protein Monomer and Protein Complex states. The Metabolic Reaction state records the calculated flux of each metabolic reaction. The Simulation object allocates metabolites produced by the Metabolism process to the other 27 cellular processes to support several functions including DNA, RNA, and protein synthesis and maturation. Additionally, the other 27 processes generate byproducts which the Metabolism process either recycles or exports from the cell.

## Initial Conditions

The Metabolite state initializes the copy number of each metabolite. The Protein Monomer state initializes the total copy number of each protein monomer. The Macromolecular Complexation process initializes the

copy number of each macromolecular complex. This process initializes the cellular growth rate and reaction fluxes to the steady-state of the metabolic network using the same FBA simulation used at each time step.

## Dynamic Computation

Algorithm S9 outlines the implementation of the FBA metabolic model.

## Fitting

The metabolic model was fit to match the observed M. genitalium mass doubling time, $\tau = 9 \mathrm { h }$ . Specifically, metabolic enzyme expression was fit using a modified version of minimization of metabolic adjustment (MOMA)<sup>876</sup>. Let $\mu _ { o } , \ v _ { o }$ be the FBA solution. Let $\mu ^ { * } = \ln 2 / \tau$ be the target growth rate. First, find a neighboring flux distribution consistent with the target growth rate. If $\mu ^ { * } > \mu _ { o }$ find a neighboring flux distribution within the current flux bounds v and $v _ { u }$

$$
\begin{array} { l } { { \displaystyle v ^ { * } = \mathrm { a r g m a x } \left| \frac { v - v _ { o } } { v _ { o } } \right| \mathrm { ~ s u b j e c t ~ t o ~ } } } \\ { { \displaystyle S v = 0 } } \\ { { \displaystyle v _ { l } \leq v \leq v _ { u } } } \\ { { \displaystyle v _ { b } = \mu ^ { * } } . } \end{array}\tag{S15}
$$

If $\mu ^ { * } < \mu _ { o }$ find a neighboring flux distribution by relaxing the flux bounds by $\mu ^ { * } / \mu _ { o }$

$$
\begin{array} { c } { { v ^ { * } = \displaystyle \operatorname * { a r g m a x } _ { v } \left| \frac { v - v _ { o } } { v _ { o } } \right| \mathrm { ~ s u b j e c t ~ t o ~ } } } \\ { { S v = 0 } } \\ { { \displaystyle v _ { l } \frac { \mu ^ { * } } { \mu _ { o } } \leq v \leq v _ { u } \frac { \mu ^ { * } } { \mu _ { o } } } } \\ { { v _ { b } = \mu ^ { * } . } } \end{array}\tag{S16}
$$

Second, invert $f _ { l }$ and $f _ { u }$ to calculate a set of enzyme expression consistent with $v ^ { * }$

$$
n _ { m } = \operatorname* { m a x } \left( f _ { l } ^ { - 1 } \left( v ^ { * } \right) , f _ { u } ^ { - 1 } \left( v ^ { * } \right) \right) .\tag{S17}
$$

The upper and lower bound of the expression of each enzyme consistent with the target growth rate was calculated using a similar procedure.

```latex
Algorithm S9 | Metabolism FBA simulation. See Mathematical Model section above for definition of the mathematical
notation.
Calculate flux bounds
begin
Initialize bounds: $v _ { l , i } \gets - \operatorname* { i n f } , v _ { u , i } \gets +$ inf
foreach thermodynamically irreversible reaction i do
Constrain reverse flux to zero: $v _ { l , i } \gets 0$
foreach chemically catalyzed reaction i do
$j \gets$ index of enzyme which catalyzes reaction i
if $k _ { - , i }$ is known then
bound flux by enzyme kinetics and expression: $v _ { l , i } \gets \operatorname* { m a x } \left( v _ { l _ { i } } , k _ { - c a t , i } n _ { e , j } \right)$
else bound flux by enzyme expression: $v _ { l , i }  v _ { l , i } \cdot ( n _ { e , j } > 0 )$
if $k _ { + , i }$ is known then
bound flux by enzyme kinetics and expression: $v _ { u , i } $ min $( v _ { u _ { i } } , k _ { + c a t , i } n _ { e , j } )$
else bound flux by enzyme expression: $v _ { u , i }  v _ { u , i } \cdot ( n _ { e , j } > 0 )$
foreach chemical reaction i do
foreach protein substrate j of reaction i do
if protein substrate j is not expressed then constrain flux to zero: ${ v _ { l , i } } \gets 0 , { v _ { u , i } } \gets 0$
foreach internal exchange reaction i do
j ← index of metabolite exchanged by reaction i
Bound internal metabolite exchange by copy number: $v _ { l , i } \gets$ max $( v _ { l _ { i } } , - n _ { m , j } )$
foreach external exchange reaction i do
j ← index of metabolite exchanged by reaction i
Bound external metabolite exchange by copy number and maximum exchange rate: $v _ { l , i } \gets \operatorname* { m a x } \left( v _ { l _ { i } } , m k _ { - e x , i } \right)$
$v _ { u , i } \gets \operatorname* { m i n } \left( v _ { u _ { i } } , m k _ { + e x , i } , n _ { m , j } \right)$
Calculate the growth rate and flux of each reaction
begin
v<sup>∗</sup> ← argmax $\mu = v _ { b }$ subject to $S v = 0$ and ${ v } _ { l } { < } v { \le } v _ { u }$
v
$\mu ^ { * }  v _ { b } ^ { * }$
Update the copy number of each metabolite species
begin
foreach extracellular metabolite i do
$j \gets$ index of reaction which exchanges metabolite i
$n _ { m , i }  n _ { m , i } + v _ { j } ^ { * }$
foreach intracellular metabolite i do
$j \gets$ index of reaction which exchanges/recycle metabolite i
$n _ { m , i }  n _ { m , i } + v _ { j } ^ { * }$
foreach metabolic objective component i do
$n _ { m , i } \gets n _ { m , i } - S _ { i , b } \mu ^ { * }$
Turnover extra energy produced beyond the demands of the 27 other modeled cellular processes,
$\Delta G A M = G A M -$ used energy
$n _ { m , A T P } \gets n _ { m , A T P } - \Delta G A M \mu ^ { * }$
$n _ { m , A D P } \gets n _ { m , A D P } + \Delta G A M \mu ^ { * }$
$n _ { m , P i } \gets n _ { m , P i } + \Delta G A M \mu ^ { * }$
$n _ { m , H _ { 2 } O } \gets n _ { m , H _ { 2 } 0 } - \Delta G A M \mu ^ { * }$
$n _ { m , H ^ { + } } \gets n _ { m , H ^ { + } } + \Delta G A M \mu ^ { * }$
```

## 3.11 Protein Activation

## Biology

The activity of mature protein monomers and complexes is not fixed, but rather can be modulated by smal molecules, DNA, RNA, and other proteins, as well as by temperature and pH. Furthermore, cells often purposefully modulate protein activity to respond to external signals and maintain homeostasis.

## Reconstruction

Protein chemical regulation was reconstructed based on extensive review of the primary literature and several databases, with particular emphasis on antibiotics (see Table S3Q and S3AQ). The reconstructed protein chemical regulation network contains 16 metabolites, three Boolean-valued pseudometabolites or stimuli, and temperature which regulate 10 proteins including four transcription factors, topoisomerases II and IV, the 30S and 50S ribosomal particles. The 10 putative chemically regulated proteins are critical for transcription, supercoiling, and translation. The efects of physical properties such as temperature and pH on protein activity were curated from BRENDA<sup>570</sup>, BioCyc<sup>6</sup>, and UniProt<sup>96</sup> (see Table S3AO and S3AP). The prosthetic groups and coenzymes required for maturation and catalysis were also curated (see Table S3AM).

## Computational Representation

## Mathematical Model

Because the exact efects of small molecules, temperature, and pH on the functional activity of proteins are not well characterized, this process implements a Boolean model of their efects on the functional state

enzymatically competent or incompetent – of mature proteins. Less well characterized efects of other physical properties such as pH are not modeled. The functional state, $I _ { i } ,$ of every copy of protein species i is governed by a single independent Boolean function, $f _ { i }$ (see Table S3Q),

$$
I _ { i } = f _ { i } \left( { \frac { \vec { m } } { V } } , \vec { s } , T \right) ,\tag{S18}
$$

where $m _ { j }$ is the concentration of metabolite j, $s _ { j }$ is the value of stimulus $j ,$ and $T$ is the temperature.   
Proteins with no known chemical regulation were assumed to be constitutively competent.

The Protein Folding process separately models the role of chaperones in protein folding and accounts for the small molecule prosthetic groups required for protein folding. Several processes including Metabolism model the coenzymes required for catalytic activity.

## Integration

The Stimulus state represents the value of each pseudometabolite and temperature. The Metabolite state represents the copy number of each metabolite. The Geometry state represents the cell volume. The Protein Monomer and Protein Complex states represent the competent and incompetent copy numbers of each protein species. Proteins regulated by this process are synthesized and matured by several processes (see Section 2.10).

## Initial Conditions

After the temperature, cell volume, pseudometabolite values, and metabolite and total protein copy numbers are initialized, the competency state of each of the regulated proteins is initialized to the steady state of the regulatory network. Because the regulatory network is acyclic, the network converges in one iteration.

## Dynamic Computation

Algorithm S10 outlines the implementation of the protein activation model.

Input: $p _ { i } ^ { c }$ competent copy number of protein i   
Input: $p _ { i } ^ { i }$ incompetent copy number of protein i   
foreach regulated protein i do   
if regulatory rule f ( \~m/V, \~s, T ) then   
Mark all copies of protein i competent   
$p _ { i } ^ { c } = p _ { i } ^ { c } + p _ { i } ^ { i }$   
$p _ { i } ^ { i } = 0$   
else   
Mark all copies of protein i incompetent   
$p _ { i } ^ { i } = p _ { i } ^ { i } + p _ { i } ^ { c }$   
p<sup>c</sup><sub>i</sub> = 0

## 3.12 Protein Decay

## Biology

Protein degradation serves two critically important functions. First, protein degradation eliminates abnormal and potentially toxic proteins including prematurely aborted polypeptides tagged with SsrA degradation signals, and salvages their valuable metabolic resources to support protein synthesis. Second, degradation controls protein expression, enabling cells to direct valuable amino acids away from inefective or even harmful proteins toward productive proteins, regulate protein activity, and respond to external signals. Tobias et al. have shown that the degradation rates of E. coli proteins are correlated with their N-terminal residue, suggesting that cells target proteins for degradation by manipulating their N-termini<sup>586</sup>. This relationship is known as the N-end rule.

Protein refolding is an eficient mechanism for eliminating abnormally folded proteins, requiring less energy than protein degradation and avoiding the large cost of resynthesis. The M. genitalium chromosome contains one protein chaperone – the cytosol-localized and ATP-dependent protease ClpB (MG355) – dedicated to protein refolding<sup>14,182</sup>. The kinetics and energetics of protein refolding are not well characterized.

This process models the degradation of protein monomers, macromolecular complexes, cleaved signal sequences, and prematurely aborted polypeptides as well as the misfolding and refolding of protein monomers and complexes.

## Reconstruction

## Protein Half-Lives

The half-life of each protein monomer was predicted using the N-end rule reported by Tobias et al.<sup>586</sup>. The half-life of each macromolecular complex was set equal to the weighted mean half-life of its RNA and protein subunits. The half-lives of the damaged and misfolded configurations of each protein species, cleaved signal sequences, and prematurely aborted polypeptides were set to zero to reflect their rapid degradation. Section 2.12 and Table S3Y describe how RNA half-lives were reconstructed.

## Proteolytic Machinery

The M. genitalium genome contains homologs of proteases FtsH (MG457) and La (MG239) and six peptidases: aminopeptidase (MG324), cytosol aminopeptidase (MG391), glycoprotease (MG208), metalloendopeptidase (MG046), oligoendopeptidase F (MG183), and proline iminopeptidase (MG020)<sup>182,634</sup>. The membrane-localized protease FtsH is believed to cleave prematurely aborted polypeptides tagged with an N-terminal SsrA tag into approximately 15 amino long fragments by an ATP-dependent mechanism<sup>30,634</sup>. Bruckner et al. reported the kinetics and energetics of FtsH proteolysis<sup>31</sup>. The cytosol-localized protease La is believed to processively cleave most other proteins into fragments 10-20 amino acids in length by an ATP-dependent mechanism<sup>29</sup>. Lee and Suzuki reported the kinetics and energetics of La proteolysis<sup>29</sup>. Peptidases are believed to hydrolytically degrade the polypeptide fragments produced by peptidases FtsH and La. The specific function of each of the six M. genitalium peptidases is unknown.

## Computational Representation

## Mathematical Model

Under conditions of excess proteases, peptidases, and ATP, this process models the configuration of each protein as a five-state system – aborted, nascent, mature, misfolded, and damaged – and models the degradation of protein i as Poisson process with rate parameter $k _ { d , i } = \ln 2 / \tau _ { 1 / 2 , i }$ where $\tau _ { 1 / 2 , i } = 2 0 \mathrm { h }$ for the nascent and mature states and zero for the aborted, misfolded, and damaged states. Under conditions of limited proteases, peptidases, or ATP the model stochastically degrades proteins as a function of the copy number and catalytic rate of each enzyme and the number of cytosolic ATP molecules. This models assumes (1) cytosol-localized nascent, mature, misfolded, and damaged proteins are degraded by protease La and six peptideases, (2) membrane and extracellular-localized proteins are not vulnerable to degradation by the cytosol localized protease La, (3) aborted polypeptides are degraded by protease FtsH and six peptidases, (4) protein degradation is kinetically fast and therefore this model doesn’t represent intermediate degradation states, and (5) aborted, misfolded, and damaged proteins are immediately degraded if proteases are expressed and energy is available. Algorithm S11 outlines the implementation of the protein degradation model.

This process models protein unfolding as a Poisson process with rate parameter $k _ { u }$ set to the nominal rate $1 0 ^ { - 6 } \mathrm { { s } ^ { - 1 } }$ molecule<sup>−1</sup>. Cytosol-localized protein refolding is modeled as a single chemical event catalyzed by the cytosol-localized chaperone ClpB and driven by the hydrolysis of a single ATP molecule. Because protein refolding is not well characterized, this process assumes that if ClpB is expressed and excess ATP is available, protein refolding proceeds to completion within the 1 s simulation time step. If ClpB is expressed, but ATP is not present in excess, the model stochastically refolds proteins equal to the intracellular copy number of ATP.

This model makes several simplifying assumptions. First, the model assumes that all protein species misfold and refold at the same rate. Second, the model assumes that the kinetics of protein misfolding and refolding are fast and therefore intermediate misfolded states can be ignored.

## Integration

The Protein Monomer and Protein Complex states represent the copy number of each protein monomer and macromolecular complex including the signal sequence, misfolded, and damaged copy numbers of each protein species and the copy number of each proteolytic enzyme in each of five compartments: cytosol, membrane, terminal organelle cytosol, terminal organelle membrane, and extracellular space. The Polypeptide state represents the amino acid sequence of each prematurely aborted polypeptide. The Chromosome, FtsZ Ring, Ribosome, and RNA Polymerase states represents the detailed configurations of DNA-bound proteins, the FtsZ septal ring, RNA polymerases, and ribosomes. These detailed configurations are updated when DNA-bound proteins, FtsZ, RNA polymerase, or 70S ribosomes are degraded to reflect decreased enzyme copy numbers. The Transcript and Polypeptide states are also updated upon RNA polymerase or 70S ribosome degradation to reflect transcript and polypeptide abortion. The Rna state represents the damaged copy number of each RNA species. See below for further discussion. The Metabolite state represents the copy number of each intracellular metabolite.

This process marks RNA subunits of degraded macromolecules as “damaged” for immediate degradation by the RNA Decay process.

## Initial Conditions

The misfolded and damaged configurations of each RNA and protein species are initialized with zero copy number because the typical occupancies these configurations are small compared to that of the mature configuration. Similarly, the cell is initialized with no prematurely aborted polypeptides. The Rna, Protein Monomer, and Protein Complex states initialize the total copy numbers of each RNA and protein species.

Dynamic Computation Algorithm S11 outlines the implementation of the protein decay model.

## Algorithm S11 | Protein decay simulation.

<table><tr><td>Input:  $k _ { u } = 1 0 ^ { - 6 } \mathsf { s }$ </td><td>protein unfolding rate</td></tr><tr><td>Input:</td><td> $k _ { d , i } ^ { p } = \ln 2 / \tau _ { 1 / 2 , i }$  degradation rate of protein monomer species i</td></tr><tr><td>Input:</td><td> $k _ { d , i } ^ { c ^ { \prime } } = \ln 2 / \tau _ { 1 / 2 , i }$  degradation rate of macromolecular complex species i</td></tr><tr><td>Input:</td><td> $k _ { \mathsf { L o n } } ,$  kFtsH protease kinetic rates in amino acids per second</td></tr><tr><td>Input:</td><td>copy number of metabolite i</td></tr><tr><td>Input:</td><td>damaged copy number of RNA species  $_ { i }$ </td></tr><tr><td>Input:</td><td> $r _ { i } ^ { d }$   $p _ { i } ^ { a } , p _ { i } ^ { u } , \bar { p _ { i } ^ { d } }$  mature, unfolded, and damaged copy numbers of protein monomer species i</td></tr><tr><td>Input:</td><td> $c _ { i } ^ { a } , c _ { i } ^ { u } , c _ { i } ^ { d }$  mature, unfolded, and damaged copy numbers of macromolecular complex species i</td></tr><tr><td>Input:</td><td> $p \gets \{ p _ { i } ^ { a } , p _ { i } ^ { u } , p _ { i } ^ { d } \}$  copy number of all forms of protein monomer species i</td></tr><tr><td>Input:</td><td> $c \gets \{ c _ { i } ^ { a } , c _ { i } ^ { u } , c _ { i } ^ { d } \}$  copy number of all forms of macromolecular complex species i</td></tr><tr><td>Input:</td><td> ${ \mathrm { e } } _ { \mathsf { L o n } } ,$  EFtsH copy numbers of proteases La and FtsH</td></tr><tr><td>Input:</td><td>sequence of prematurely aborted polypeptide i</td></tr><tr><td>Input:  $l _ { i } ^ { p }$ </td><td> $s _ { i }$  length of protein monomer species i</td></tr><tr><td>Input:</td><td>length of prematurely aborted polypeptide i</td></tr><tr><td>Input:  $P _ { i j } ^ { m }$ </td><td>reaction stoichiometry of metabolite i in the degradation of protein monomer  $j$  including ATP hydrolysis</td></tr><tr><td>Input:</td><td>stoichiometry of metabolite species i in macromolecular complex  $j$ </td></tr><tr><td>Input:</td><td>subunit stoichiometry of mature RNA species i in macromolecular complex  $j$ </td></tr><tr><td>Input:</td><td>subunit stoichiometry of mature protein monomer i in macromolecular complex  $j$ </td></tr><tr><td>Input:</td><td> $C _ { i j } ^ { p }$  reaction stoichiometry of metabolite i in the degradation of polypeptide j including ATP hydrolysis</td></tr><tr><td> $S _ { i j } ^ { m }$  Input:  $\Delta \dot { t } = 1$ </td><td>s is the simulation time step</td></tr><tr><td colspan="2">Misfold proteins (see Algorithm S13)</td></tr><tr><td colspan="2">Refold proteins (see Algorithm S12)</td></tr><tr><td colspan="2"></td></tr><tr><td colspan="2">Degrade macromolecular complexes (see Algorithm S14)</td></tr><tr><td colspan="2">Degrade prematurely aborted polypeptides (see Algorithm S15)</td></tr><tr><td colspan="2">Degrade protein monomers (see Algorithm S16)</td></tr></table>

## Fitting

The expression of the proteases and peptidases was fit to provide suficient enzymes to quickly degrade damaged proteins, or more specifically to prevent sustained accumulation of damaged proteins. See Section 1.3 for further discussion.

```latex
Algorithm S12 | Protein refolding simulation. See Algorithm S11 for mathematical notation.
if ClpB chaperone is expressed $( e _ { C I p B } > 0 )$ then
repeat
Select protein species $i \sim$ multinomialRand(1, $\{ p ^ { u } , c ^ { u } \} / \left( \sum _ { j } p _ { j } ^ { u } + \sum _ { j } c _ { j } ^ { u } \right) )$
Update protein copy numbers
if species i is a protein monomer then $p _ { i } ^ { u }  p _ { i } ^ { u } - 1 , p _ { i } ^ { a }  p _ { i } ^ { a } + 1$
else $c _ { i } ^ { u }  c _ { i } ^ { u } - 1 , c _ { i } ^ { a }  c _ { i } ^ { a } + 1$
Hydrolyze ATP
$m _ { \mathsf { A T P } } \gets m _ { \mathsf { A T P } } - 1$
$m _ { \mathsf { A D P } } \gets m _ { \mathsf { A D P } } + 1$
$m _ { \mathsf { P i } } \gets m _ { \mathsf { P i } } + 1$
$m _ { \mathsf { H } _ { 2 } 0 } \gets m _ { \mathsf { H } _ { 2 } 0 } - 1$
$m _ { \mathsf H ^ { + } } \gets m _ { \mathsf H ^ { + } } + 1$
until $( p _ { i } ^ { u } = 0 \ \forall \ i a n d c _ { i } ^ { u } = 0 \ \forall \ i )$ orm $\iota _ { A T P } = 0$
```

Algorithm S13 | Protein unfolding simulation. See Algorithm S11 for mathematical notation.   
foreach protein monomer i do   
Calculate protein unfolding extent: $\Delta p _ { i } ^ { u } \gets \mathtt { p o i }$ issonRand $( k _ { u } p _ { i } ^ { a } )$   
Update protein copy numbers: $p _ { i } ^ { a }  p _ { i } ^ { a } - \bar { \Delta } p _ { i } ^ { u } , p _ { i } ^ { u }  p _ { i } ^ { u } + \Delta p _ { i } ^ { u }$   
foreach macromolecular complex i do   
Calculate protein unfolding extent: $\Delta c _ { i } ^ { u }  \mathtt { p o }$ issonRand $( k _ { u } c _ { i } ^ { a } )$   
Update protein copy numbers: $c _ { i } ^ { a }  c _ { i } ^ { a } - \bar { \Delta } c _ { i } ^ { u } , c _ { i } ^ { u }  c _ { i } ^ { u } + \Delta c _ { i } ^ { u }$

```perl
Algorithm S14 | Macromolecular complex degradation simulation. See Algorithm S11 for mathematical notation.
Calculate rates of protein degradation
foreach macromolecular complex i do
∆c<sub>i</sub> ← poissonRand $( k _ { d , i } ^ { c } c _ { i } )$
Degrade specific complexes
repeat
Select protein species $i \sim$ multinomialRand $( \Delta c _ { i } / \sum _ { j } \Delta c _ { j } )$
if suficient metabolic resources available $( m _ { j } \ge - C _ { j i } ^ { m } \forall j )$ then
Breakdown complex into metabolites and damaged RNA and protein subunits
$\Delta c _ { i } \gets \Delta c _ { i } - 1$
$c _ { i } \gets c _ { i } - 1$
$p ^ { d }  p _ { i } ^ { d } + C _ { \bullet i } ^ { p }$
$r ^ { d }  r _ { i } ^ { d } + C _ { \bullet i } ^ { r }$
$m  m C _ { \bullet i } ^ { m }$
else
$\Delta c _ { i } \gets 0$
until $\Delta c _ { i } = 0 \ \forall \ i$
```

Algorithm S15 | Aborted polypeptide degradation simulation. See Algorithm S11 for mathematical notation.   
Let $z \gets$ poissonRand $( e _ { F t s H } / k _ { F t s H } \Delta t )$ be the FtsH enzymatic capacity   
while all peptidases expressed $( e _ { i } \ \forall$ peptidasesi) do   
Select an aborted polypeptides i ∼ multinomialRand $( \boldsymbol { \mathit { 1 } } , \boldsymbol { \mathit { 1 } } / n _ { p e p } )$   
if insuficient resources to degrade polypeptide $( \exists j s . t - S _ { j i } ^ { m } > m _ { j }$ and $z \geq ]$ length $( l _ { i } ^ { s } ) \geq 1 )$ then   
break   
Degrade polypeptide: $s _ { i } \gets \emptyset , m \gets m + S _ { \bullet i } ^ { m } , z \gets z \mathrm { - } 1 \mathtt { e n g t h } ( l _ { i } ^ { s } )$

Algorithm S16 | Protein monomer degradation simulation. See Algorithm S11 for mathematical notation.   
if all peptidases expressed (e<sub>i</sub> ∀ peptidasesi) then   
Let z ←poissonRand $( e _ { L o n } / k _ { L o n } \Delta t )$ be the Lon enzymatic capacity   
Calculate rates of protein degradation   
foreach protein monomer i do   
$\Delta p _ { i } \gets$ poissonRand $( k _ { d , i } ^ { p } { p } _ { i } )$   
  
Degrade specific monomers   
repeat   
Select protein species $i \sim$ multinomialRand $( \Delta p _ { i } / \sum _ { j } \Delta p _ { j } )$   
if suficient metabolic resources available $( m _ { j } \geq - P _ { j i } ^ { m } \forall j$ and $z \geq l _ { i } ^ { p } \geq 1 )$ then   
Breakdown protein into metabolites   
$\Delta p _ { i } \gets \Delta p _ { i } - 1$   
$p _ { i } \gets p _ { i } - 1$   
$m \gets m P _ { \bullet i } ^ { m }$   
$z  z - l _ { i } ^ { p }$   
else   
$\ L \Delta p _ { i } \gets 0$   
until $\Delta p _ { i } = 0 \ \forall \ i$

## 3.13 Protein Folding

## Biology

Proteins are synthesized as long, catalytically inactive linear chains of amino acids (see Translation). Subsequently, proteins fold into energetically favorable, compact, and enzymatically competent three-dimensional structures. While some protein species are believed to fold spontaneously, other proteins are believed to require helper chaperone proteins to properly fold<sup>17,718</sup>. In addition, some protein species require metal ions and other small molecule prosthetic groups to fold. This process models chaperone-mediated protein folding.

M. genitalium is believed to employ three chaperones to assist protein folding. First, trigger factor (Tig, MG238) co-translationally binds all nascent polypeptides at the ribosome exit site (L23) and assists in early protein folding<sup>5,9,14,17,388,644,718</sup>.

Second, chaperones GroEL (MG392) and DnaK (MG305) and their co-chaperones are believed to assist in late folding. GroEL and DnaK are believed to fold 10-15% and 5-18% of all proteins, respectively. GroEL and its co-chaperone GroES (MG393) are believed to help fold intermediate sized proteins (20-60 kDa)<sup>14,644</sup>. GroEL is believed to bind each protein for 30 s to 10 min, and to couple folding to ATP hydrolysis<sup>14,644</sup>.

DnaK and its co-chaperones DnaJ (MG019) and GrpE (MG201) are believed to help fold large proteins $( > \mathrm { 3 0 k D a } ) ^ { \mathrm { 1 4 , 6 4 4 } }$ . DnaK is a monomeric protein which transiently (< 2 min) binds to the backbones of short, linear, unfolded peptide segments. GrpE is believed to couple peptide release to ATP hydrolysis. DnaJ is believed to regulate the activity of DnaK, as well bind the side chains of hydrophobic and aromatic residues and directly assist protein folding.

Finally, FtsH and the lipids phosphatidyl ethanolamine and phosphatidyl glycerol have been suggested to assist membrane protein folding<sup>14</sup>. However, the role of FtsH as a molecular chaperone is not well established, and FtsH has been associated with several additional functions. Consequently, we chose not to model FtsH as a chaperone. The contributions of phosphatidyl ethanolamine and phosphatidyl glycerol to protein folding are also poorly understood, and are not modeled.

## Reconstruction

M. genitalium GroEL substrates were reconstructed based on two proteome-scale studies of E. coli and B. subtilis (see Table S3AG)<sup>389,391</sup>. M. genitalium DnaK substrates were reconstructed based on a proteomescale study of $E .$ coli (see Table $\mathrm { S 3 A G ) ^ { 3 8 8 } }$ The prosthetic group requirements for protein folding were reconstructed based on an extensive review of the literature and several databases (see Table S3AM). Table S3M lists the chaperones required to fold each protein monomer and the prosthetic group stoichiometry of each protein monomer.

## Computational Representation

## Mathematical Model

This process implements a model of the chaperone-mediated folding of processed, translocated polypeptides. Because the kinetics and energetics of protein folding are not well understood, this process represents the three-dimensional configuration of each protein as a two-state – folded, unfolded – Boolean variable. Furthermore, this process makes the simplifying assumption that the folding rate, $r _ { i } ,$ of protein species i is a Boolean function of the copy numbers of metabolites and chaperones,

$$
r _ { i } = \operatorname* { m i n } \left( \overbrace { \int _ { i } ^ { u } \mathbf { \Phi } _ { j } } ^ { \mathrm { m e t e i n } } , \overbrace { \left[ \operatorname* { m i n } _ { j } \frac { m _ { j } } { M _ { j i } } \right] } ^ { \mathrm { m e t a b o l i t e s } } , \overbrace { \operatorname* { m i n } _ { j } \frac { e _ { j } } { C _ { j i } } } ^ { \mathrm { e n z y m e s } } \right) ,\tag{S19}
$$

where $p _ { i } ^ { u }$ is the unfolded copy number of protein species $i , m _ { i }$ is the copy number of metabolite $i , e _ { i }$ is the copy number of chaperone $i , M _ { j i }$ is the stoichiometry of prosthetic group $j$ in protein $i ,$ and $C _ { j i }$ is true if protein species i requires chaperone $j$ to fold. $p _ { i } ^ { f }$ is the folded copy number of protein species i.

## Integration

The Metabolite state represents the copy number of each metabolite species. The Protein Monomer and Protein Complex states represent the copy numbers of unfolded and folded proteins. Protein folding is one of the last steps in protein maturation following protein processing and translocation (see Protein Processing I and Protein Translocation processes) and preceding protein modification (see Protein Modification process). See Section 2.10 for further discussion.

## Initial Conditions

The Protein Monomer and Protein Complex states initialize the total copy number of each protein species, and set all protein monomers and complexes to their mature – folded and modified – configuration.

## Dynamic Computation

Algorithm S17 outlines the implementation of the protein folding model.

## Algorithm S17 | Protein folding simulation.

repeat   
foreach protein species i do   
Calculate the relative Boolean-valued folding rate, $\boldsymbol { r } _ { i } ,$ of each protein species   
$r _ { i } \gets \operatorname* { m i n } \left\{ p _ { i } ^ { u } , m _ { j } / M _ { i j } , c _ { k } \geq C _ { i k } \right\}$   
Select a protein species i to fold according to multinomialRand $( \lambda , \vec { r } )$   
Increment the folded copy number of protein species i, $p _ { i } ^ { f } \gets p _ { i } ^ { f } + 1$   
Decrement the unfolded copy number of protein species i $, p _ { i } ^ { u } \gets p _ { i } ^ { u } - 1$   
Decrement the copy numbers of the prosthetic groups of protein species $i , m _ { j } \gets m _ { j } - M _ { i j }$   
until no additional proteins can fold $( \vec { r } = 0 )$

## Dynamic Computation

Chaperone expression was fit to provide suficient enzymes to quickly fold all newly synthesized proteins, or more precisely, to prevent accumulation of unfolded proteins. See Section 1.3 for further discussion.

## 3.14 Protein Modification

## Biology

Post-translational protein modification serves several important functions<sup>281,890</sup>. First, post-translation modification can increase the structural and chemical diversity of the proteome by stabilizing alternative conformations and providing catalytic cofactors. Second, post-translational modification, and in particular phosphorylation, provides a mechanism to regulate protein activity. Third, post-translational modification can be used to regulate protein expression through proteasome recruitment. This process models protein covalent modification including phosphorylation, lipoyl transfer, and α-glutamate ligation.

## Reconstruction

The M. genitalium protein modification complement was reconstructed in three steps. First, protein modifications that have been observed in M. genitalium<sup>94</sup>, M. pneumoniae<sup>94,277,282,283,672</sup>, or other related bacteria<sup>96,105,276,280,673</sup> or which have been computationally predicted<sup>268,278,575</sup> were curated. Second, curated protein modifications were mapped to M. genitalium homologs using sequence alignment. Third, based on the genome annotation<sup>182</sup>, M. genitalium was determined to have three protein modification pathways: (1) phosphorylation catalyzed by serine/threonine kinase PrkC (MG109), (2) lipoyl transfer to lysine catalyzed by LplA (MG270), and (3) C-terminal α-glutamate ligation catalyzed by RimK (MG012). Fourth, modifications were rejected which do not belong to one of these three pathways, or for which a specific locus was not reported. Table S3AH outlines the reconstruction process and lists the reconstructed protein modifications. The reconstructed protein modification network contains one kinase that modifies 16 proteins, one lipoyl transferase that modifies the E2 subunit of pyruvate dehydrogenase (PdhC, MG272), providing an important organosulfur cofactor which contains a catalytic disulfide bond, and one α-glutamate ligase that modifies 50S ribosomal protein L6 (RplF, MG166). The stoichiometry and kinetics of all three modeled protein modification reactions were based on a review of the primary literature<sup>110,288–290,294</sup> (see Table S3O). Catalytic disulfide bonds were separately reconstructed and are modeled by several chemical reactions in the Metabolism process (see Table S3O).

## Computational Representation

## Mathematical Model

This process models protein covalent modification, the fifth step of post-translational processing. In particular, this process models protein phosphorylation, lipoyl transfer, and α-glutamate ligation. Because the mechanisms of protein modification are not well characterized on the genomic scale, this process make several simplifying assumptions. First, this process assumes that each protein is fully modified in a single time step, collapses the modification of each protein into a single reaction, and only represents unmodified and fully modified proteins. Intermediate protein configurations are not represented. Second, this process assumes that the mean arrival rate, $v _ { i }$ of modification events of each protein species i is independently limited by (1) the copy number of unmodified protein, $p _ { i } ^ { u }$ , (2) the copy numbers of intracellular metabolites, $m _ { j }$ , and (3) the copy numbers of the protein modification enzymes, $e _ { j }$ . Based on these assumptions, the functional form of $v _ { i }$ is given by

$$
v _ { i } = \operatorname* { m i n } \left( \overbrace { \int _ { p _ { i } ^ { u } } ^ { u } \ , \ \sqrt { \left. \left[ \operatorname* { m i n } _ { j } \frac { m _ { j } } { M _ { j i } ^ { s } } \right] \right]}  , \overbrace { \mathrm { p o i s s o n R a n d } \left( \operatorname* { m i n } _ { j } \frac { e _ { j } } { K _ { j i } } \Delta t \right) } ^ { \mathrm { m e t a b o l i t e s } } } \right) ,\tag{S20}
$$

where $M _ { j i }$ is the stoichiometry of metabolite $j$ in the modification of protein species $i , M ^ { s } = \operatorname* { m a x } { ( 0 , - M ) }$ is the negative part of M , $K _ { j i }$ is the experimentally observed catalytic rate of enzyme j in the modification of protein species $i ,$ and $\Delta t = 1 \mathrm { s }$ s is the simulation time step.

This process implements a stochastic model of the arrival of protein monomer and macromolecular complex modification events with relative rates $v _ { i }$ . Until protein, metabolic, and/or enzymatic resources are exhausted, the model iteratively (1) computes the arrival rate, $v _ { i } ,$ of each modification event, (2) selects a single modification event to execute according to a multinomial distribution parameterized by v<sub>i</sub>, and (3) executes the selected modification reaction, updating the copy numbers of proteins and metabolites and decrementing the available enzymatic capacity. Algorithm S18 outlines the implementation of the protein modification model.

## Integration

The Protein Monomer and Protein Complex states represent the copy number of each protein modification enzyme. The Protein Monomer state also represents the unmodified and modified copy numbers of each protein monomers species. The Metabolite state represents the copy number of each intracellular metabolite.

Protein are synthesized and matured in six steps (see Section 2.10). This process models the fifth step in protein synthesis following protein folding (see Protein Folding process) and preceding macromolecule assembly (see Macromolecular Complexation, Ribosome Assembly, Protein Folding, and Protein Modification processes).

## Initial Conditions

Section 1.4 outlines the cell state initialization algorithm. Briefly, after the Mass state initializes the tota cell mass, the Protein Monomer state initializes the total copy number of each protein monomer species and initializes all monomers to their mature – processed, folded, modified, and localized – configuration. Second, the Macromolecular Complexation and Ribosome Assembly processes initialize the copy number of each ribonucleoprotein complex, and set all initialized complexes to their mature – folded and modified configuration. Finally, several processes including Transcription and Translation initialize the detailed configurations of RNA polymerases, 70S ribosomes, DNA-binding proteins, and FtsZ.

The unmodified configurations of each protein monomer species is initialized with zero copy number because the typical occupancy this configuration is small compared to that of the modified/mature configuration.

## Dynamic Computation

Algorithm S18 outlines the implementation of the protein modification model.

Algorithm S18 | Protein modification simulation. See Mathematical Model section above for definition of the mathe  
matical notation.   
Input: $p _ { i } ^ { m }$ copy number of modified protein species i   
Let $k _ { i } \gets e _ { i } \Delta t$ be the capacity of enzyme i for protein modification   
repeat   
Calculate modification rates   
foreach protein species i do   
Calculate v<sub>i</sub> according to Eq. S20   
Select protein species i ∼ multinomialRand(1, $v _ { i } / \sum _ { j } v _ { j } )$   
Update protein copy numbers: $p _ { i } ^ { u } \gets p _ { i } ^ { u } - 1 , p _ { i } ^ { m } \gets p _ { i } ^ { m } + 1$   
Update metabolites: m $ m - M _ { \bullet i }$   
Update enzyme catalytic capacity: $k  k - K _ { \bullet i }$   
until no further modification possible $( v _ { i } = 0 ~ \forall ~ i )$

## Fitting

The expression of the protein modification enzymes was fit to provide suficient enzymes to quickly modify newly synthesized proteins, or more specifically to prevent sustained accumulation of unmodified proteins. See Section 1.3 for further discussion.

## 3.15 Protein Processing I

## Biology

Bacterial translation is initiated by the formation of the 70S ribosome and the recruitment of the initiator tRNA<sup>fMet</sup> to the ribosomal P site. This process models N-terminal formylmethionine deformylation and N-terminal methionine cleavage, the first steps in post-translational processing.

The exact function of the initiator $\mathrm { \ t R N A ^ { \mathrm { f M e t } } }$ is unknown. Several authors suggest that bacteria employ a separate tRNA for translation initiation in order to control the rate of protein synthesis through the expression of initiator tRNA<sup>887,889</sup>. Others believe that cells use a separate initiator tRNA to diferentiate between initiation factor 2-dependent recruitment of the first tRNA to the ribosomal P site and EF-Tudependent recruitment of subsequent tRNA to the A site<sup>887,888</sup>. The unique formyl group of $\mathrm { \ t R N A ^ { \mathrm { f M e t } } }$ has been suggested to enable initiation factor 2 to discriminate between initiator and other tRNA<sup>887</sup>. The role of formylmethionine as the starting amino acid is also not well understood<sup>886,888</sup>. Some authors believe that bacteria employ methionine as the first amino acid because it is the most expensive to synthesize and therefore couples translation to general cell health<sup>886</sup>. Furthermore, neither the formyl group of tRNA<sup>fMet</sup> nor methionine is essential for translation initiation<sup>886,888</sup>. S everal studies have shown that other amino acids are able to support translation initiation<sup>886,888</sup>.

Following translation, bacteria deformylate the N-terminal methionine of most proteins and cleave the Nterminal methionine of approximately 7% of proteins. The function of peptide deformylation and methionine cleavage is not well understood. Some authors believe that bacteria employ these reactions to recycle formylmethionine which is a metabolically expensive amino acid<sup>886</sup>. Other authors, citing the N-end rule<sup>586</sup>, believe that bacteria cleave the N-terminal methionine of specific proteins in order to regulate protein halflives by exposing the second-most N-terminal amino acid<sup>886</sup>.

## Reconstruction

M. genitalium peptide deformylase (MG106) was assumed to deformylate all protein monomers. The protein substrates of M. genitalium methionine aminopeptidase (MG172) where reconstructed based on specific Nterminal methionine cleavages of M. genitalium homologs observed in Shewanella oneidensis MR-1<sup>280</sup>. The kinetics of peptide deformylation and N-terminal methionine cleavage were reconstructed from the primary literature<sup>21,26</sup>. Table S3O lists the stoichiometry and kinetics of the deformylation and cleavage reactions.

## Computational Representation

## Mathematical Model

This process models N-terminal formylmethionine deformylation and N-terminal methionine cleavage, the first step of post-translational processing. Because the mechanisms of early protein processing are not well characterized on the genomic scale, this process make several simplifying assumptions. First, this process assumes that each protein is both deformylated and cleaved in a single time step. Consequently, this process collapses the processing of each protein into a single reaction, and only represents nascent and fully processed proteins. Intermediate protein configurations are not represented. Second, this process assumes that the mean arrival rate, $v _ { i }$ of processing events of each protein species i is independently limited by (1) the copy number of unprocessed protein, $p _ { i } ^ { u }$ , (2) the copy numbers of intracellular metabolites, $m _ { j }$ , and (3) the copy numbers of processing enzymes, $e _ { j }$ . Based on these assumptions, the functional form of $v _ { i }$ is given by

$$
v _ { i } = \operatorname* { m i n } \left( \overbrace { \int _ { p _ { i } ^ { u } } ^ { u } \ , \ \sqrt { \left. \left[ \operatorname* { m i n } _ { j } \frac { m _ { j } } { M _ { j i } ^ { s } } \right] \right]}  } ^ { \mathrm { { m e t a b o l i t e s } } } , \overbrace { \mathrm { { p o i s s o n R a n d } } \left( \operatorname* { m i n } _ { j } \frac { e _ { j } } { K _ { j i } } \Delta t \right) } ^ { \mathrm { e n z y m e s } } \right) ,\tag{S21}
$$

where $M _ { j i }$ is the stoichiometry of metabolite $j$ in the processing of protein species i, $M ^ { s } = \operatorname* { m a x } { ( 0 , - M ) }$ is the negative part of M, $K _ { j i }$ is the experimentally observed catalytic rate of enzyme j in the processing of protein species $i ,$ and $\Delta t = 1$ s is the simulation time step.

The Protein Processing I process implements a stochastic model of the arrival of early protein monomer processing events with relative rates $v _ { i }$ . Until protein, metabolic, and/or enzymatic resources are exhausted, the model iteratively (1) computes the arrival rate, $v _ { i } .$ , of each processing event, (2) selects a single processing event to execute according to a multinomial distribution parameterized by $v _ { i } ,$ and (3) executes the selected processing reaction, updating the copy numbers of protein monomers and metabolites and decrementing the available enzymatic capacity. Algorithm S19 outlines the implementation of the early protein processing model.

## Integration

The Protein Monomer and Protein Complex states represent the copy number of each protein processing enzyme. The Protein Monomer state also represents the nascent and processed copy numbers of each protein monomers species. The Metabolite state represents the copy number of each intracellular metabolite. Proteins are synthesized and matured in six steps (see Section 2.10). This process models the first step in post-translational processing following translation (see Translation process) and preceding membrane and extracellular protein translocation and cytosolic protein folding (see Protein Translocation and Protein Folding processes).

## Initial Conditions

Section 1.4 outlines the cell state initialization algorithm. Briefly, after the Mass state initializes the tota cell mass, the Protein Monomer state initializes the total copy number of each protein monomer species and initializes all monomers to their mature – processed, folded, modified, and localized – configuration. Second, the Macromolecular Complexation and Ribosome Assembly processes initialize the copy number of each ribonucleoprotein complex and set all initialized complexes to their mature – folded and modified – configuration. Finally, several processes including Transcription and Translation initialize the detailed configurations of RNA polymerases, 70S ribosomes, DNA-binding proteins, and FtsZ.

The nascent and processed configurations of each protein monomer species are initialized with zero copy number because the typical occupancy these configurations is small compared to that of the mature config uration.

## Dynamic Computation

Algorithm S19 outlines the implementation of the protein processing (I) model.

Algorithm S19 | Protein processing (I) simulation. See Mathematical Model section above for definition of the mathe  
matical notation.   
Input: $p _ { i } ^ { p }$ copy number of processing protein monomer species i   
Let $k _ { i } \gets e _ { i } \Delta t$ be the capacity of enzyme i for protein processing   
repeat   
Calculate processing rates   
foreach protein monomer species i do   
Calculate $v _ { i }$ according to Eq. S21   
Select protein monomer species i ∼ multinomialRand $( 1 , v _ { i } / \sum _ { j } v _ { j } )$   
Update protein monomer copy numbers: $p _ { i } ^ { u }  p _ { i } ^ { u } - 1 , p _ { i } ^ { p }  p _ { i } ^ { p } + 1$   
Update metabolites: $m \gets m - M _ { \bullet i }$   
Update enzyme catalytic capacity: $k  k - K .$   
until no further processing possible $( v _ { i } = 0 ~ \forall ~ i )$

## Fitting

The expression of the protein processing enzymes was fit to provide suficient enzymes to quickly process proteins, or more specifically to prevent sustained accumulation of unprocessed proteins. See Section 1.3 for further discussion.

## 3.16 Protein Processing II

## Biology

This process models the third step of post-translational processing: lipoprotein diacylglyceryl adduction and lipoprotein and secreted protein signal peptide cleavage.

## Lipoproteins

As discussed in Section 3.17, M. genitalium lipoproteins are translated in the cytosol and subsequently tar geted to the plasma membrane by type II N-terminal signal sequences. Following membrane insertion, M. genitalium lipoproteins are first anchored to the outer leaflet of the plasma membrane. This is achieved via covalent adduction of diacylglyceryl to the sulfhydryl group of the lipobox cysteine by diacylglyceryl transferase (MG086)<sup>266,629,654</sup>. Many bacteria further anchor lipoproteins through phospholipidation. However, M. genitalium does not have an apolipoprotein transacylase, and is not believed to phospholipidate lipoproteins<sup>655–657</sup>. Second, lipoprotein N-terminal signal sequences are cleaved immediately C-terminal to the lipobox cysteine by type II signal peptidase (MG210)<sup>654</sup>. See Section 3.17 for further discussion of the structure of type II signal sequences.

## Secreted Proteins

Extracellular M. genitalium proteins are transcribed in the cytosol and targeted to the plasma membrane by type II signal sequences. In contrast to lipoproteins, extracellular proteins do not undergo diacylglyceryl transfer, and instead are cleaved immediately C-terminal to the cysteines of their lipoboxes by type II signal peptidase, releasing the resultant protein and signal peptide into the extracellular space.

## Integral Membrane Proteins

M. genitalium does not have a type I signal sequence protease<sup>634</sup> and does not cleave the signal sequences of integral membrane proteins. Integral membrane protein signal peptides are believed to help anchor proteins to the membrane<sup>3</sup>.

## Reconstruction

The localization and N-terminal signal sequence length of each protein monomer was reconstructed based on an extensive review of the primary literature, several proteomic database, and several computational predictions. See Section 3.17 for further discussion. The stoichiometry and kinetics of each protein processing reaction was reconstructed from the primary literature<sup>8,158,167,266,654</sup>. Table S3O lists the reconstructed stoichiometry and kinetics of each reaction.

## Computational Representation

## Mathematical Model

This process models lipoprotein diacylglyceryl adduction and lipoprotein and secreted protein signal peptide cleavage, the third step of post-translational processing. Because the mechanisms of protein processing are not well characterized on the genomic scale, this process make several simplifying assumptions. First, this process assumes that each protein is both covalently modified and cleaved in a single time step. Consequently, this process collapses the processing of each protein into a single reaction and only represents unprocessed and fully processed proteins. Intermediate protein configurations are not represented. Second, this process assumes that the mean arrival rate, v<sub>i</sub> of processing events of each protein species i is independently limited by (1) the copy number of unprocessed protein, p<sup>u</sup><sub>i</sub> , (2) the copy numbers of intracellular metabolites, m<sub>j</sub> , and (3) the copy numbers of processing enzymes, e<sub>j</sub>. Based on these assumptions, the functional form of v<sub>i</sub>

is given by

$$
v _ { i } = \operatorname* { m i n } \left( \overbrace { \int _ { p _ { i } ^ { u } } ^ { u } \ , \ \sqrt { \left. \left[ \operatorname* { m i n } _ { j } \frac { m _ { j } } { M _ { j i } ^ { s } } \right] \right]}  } ^ { \mathrm { { m e t a b o l i t e s } } } , \overbrace { \mathrm { { p o i s s o n R a n d } } \left( \operatorname* { m i n } _ { j } \frac { e _ { j } } { K _ { j i } } \Delta t \right) } ^ { \mathrm { e n z y m e s } } \right) ,\tag{S22}
$$

where $M _ { j i }$ is the stoichiometry of metabolite $j$ in the processing of protein species i, $M ^ { s } = \operatorname* { m a x } { ( 0 , - M ) }$ is the negative part of $M , K _ { j i }$ is the experimentally observed catalytic rate of enzyme j in the processing of protein species $i ,$ and $\Delta t = 1$ s is the simulation time step.

This process implements a stochastic model of the arrival of protein monomer processing events with relative rates $v _ { i } .$ Until protein, metabolic, and/or enzymatic resources are exhausted, the model iteratively (1) computes the arrival rate, $v _ { i } ,$ of each processing event, (2) selects a single processing event to execute according to a multinomial distribution parameterized by $v _ { i } ,$ and (3) executes the selected processing reaction, updating the copy numbers of protein monomers and metabolites and decrementing the available enzymatic capacity. Algorithm S20 outlines the implementation of the protein processing model.

## Integration

The Protein Monomer and Protein Complex states represent the copy number of each protein processing enzyme. The Protein Monomer state also represents the unprocessed and processed copy numbers of each protein monomers species. The Metabolite state represents the copy number of each intracellular metabolite.

Protein are synthesized and matured in six steps (see Section 2.10). This process models lipoprotein diacylglyceryl transfer and lipoprotein and secreted protein signal sequence cleavage following translocation (see Protein Translocation process) and preceding folding and modification (see Protein Folding and Protein Modification processes).

## Initial Conditions

Section 1.4 outlines the cell state initialization algorithm. Briefly, after the Mass state initializes the tota cell mass, the Protein Monomer state initializes the total copy number of each protein monomer species and initializes all monomers to their mature – processed, folded, modified, and localized – configuration. Second, the Macromolecular Complexation and Ribosome Assembly processes initialize the copy number of each ribonucleoprotein complex, and set all initialized complexes to their mature – folded and modified configuration. Finally, several processes including Transcription and Translation initialize the detailed configurations of RNA polymerases, 70S ribosomes, DNA-binding proteins, and FtsZ.

The unprocessed and processed configurations of each protein monomer species are initialized with zero copy number because the typical occupancy these configurations is small compared to that of the mature configuration.

## Dynamic Computation

Algorithm S20 outlines the implementation of the protein processing (II) model.

## Fitting

The expression of the protein processing enzymes was fit to provide suficient enzymes to quickly process proteins, or more specifically to prevent sustained accumulation of unprocessed proteins. See Section 1.3 for further discussion.

Algorithm S20 | Protein processing (II) simulation. See Mathematical Model section above for definition of the   
mathematical notation.   
Input: $p _ { i } ^ { p }$ copy number of processed protein monomer species i   
Input: p<sup>s</sup> copy number of cleaved signal sequence of protein monomer species i   
Let $k _ { i } \gets e _ { i } \Delta t$ be the capacity of enzyme i for protein processing   
repeat   
Calculate processing rates   
foreach protein monomer species i do   
Calculate $v _ { i }$ according to Eq. S22   
Select protein monomer species i ∼ multinomialRand(1, $v _ { i } / \sum _ { j } v _ { j } )$   
Update protein monomer copy numbers: $p _ { i } ^ { u }  p _ { i } ^ { u } - 1 , p _ { i } ^ { p }  p _ { i } ^ { p } + 1 , p _ { i } ^ { s }  p _ { i } ^ { s } + 1$   
Update metabolites: $m \gets m - M _ { \bullet i }$   
Update enzyme catalytic capacity: $k  k - K _ { \bullet i }$   
until no further processing possible $( v _ { i } = 0 ~ \forall ~ i )$

## 3.17 Protein Translocation

## Biology

Bacterial proteins are translated in the cytosol. However, many functionally important proteins including nutrient transporters, ATP synthase, metabolic enzymes, adhesins, receptors, transducers, virulence factors, and the protein translocation machinery itself must be embedded in the cell membrane or secreted in order to properly function<sup>658</sup>. Cells employ short N-terminal and C-terminal signal sequences to selectively translocate proteins. This process models membrane and extracellular protein localization, the second step in post-translational processing.

## Reconstruction

The subcellular localization – cytosol, integral membrane, lipoprotein, terminal organelle cytosol, terminal organelle lipoprotein, or extracellular space – of each protein monomer and the N-terminal signal sequence of each lipoprotein and secreted protein was reconstructed based on an extensive review of the primary literature<sup>88,89,91–93,284,303,406–409</sup>, several proteomic databases<sup>96,253,386,570,572–574</sup>, and several computational reconstructed localization and signal sequence of each protein monomer.

M. genitalium employs two convergent SecA-dependent pathways – co-translational and post-translational to translocate approximately 35-45% of all protein monomers into the plasma membrane<sup>3</sup>. M. genitalium does not contain a type I Tat transporter or sortase<sup>631</sup>. The co-translational SecA pathway translocates integral membrane proteins into the cell membrane. First, GTP-dependent signal recognition particles (SRP; MG0001, MG048) and molecular chaperones co-translationally recognize the type I signal sequence of nascent integral membrane proteins<sup>3</sup>. Second, SRPs deliver nascent proteins to their cognate receptor FtsY (MG297) which is associated with the SecA type II preprotein translocon<sup>3</sup>. Finally, the preprotein translocase SecA (MG072) iteratively pushes nascent proteins through the SecYEG (MG170, MG055, MG476) translocase pore by an ATP-dependent, step-wise mechanism<sup>3</sup>. Several studies have shown that SecDF (MG277)<sup>6</sup> and YidC (MG464)<sup>57,328</sup> also participate in the translocase pore. SecDF and YidC are believed to increase the eficiency of protein translocation<sup>3</sup>. The exact functions of SecDF and YidC are not known.

The M. genitalium post-translational SecA pathway translocates lipoproteins and secreted proteins. First, nascent proteins complete translation. Second, SecA translocons directly recognize the type II signal sequence of nascent proteins. Type II signal sequences are short, positively charged N-terminal sequences<sup>3</sup>. Type II signal sequences are composed of three regions – n, h, and c. The n region is composed of 1-5 positively charged amino acids. The h region is composed of 7-15 hydrophobic amino acids and forms an α-helix. The c region is composed of 3-7 polar amino acids and forms a $\beta \mathrm { . }$ -strand. Signal peptidase II cleaves type II signal sequences at lipoboxes distinguished by the sequence L[ASI][GA]C inside the c region. Finally, similar to the co-translational pathway, SecA iteratively translocates nascent proteins into the plasma membrane.

Following translocation M. genitalium anchors lipoproteins to the outer leaflet through the covalent ligation of diacylglyceryl by diacylglyceryl transferase and extracellularly cleaves the type II signal sequence of each lipoprotein and secreted protein at conserved lipoboxes (see Protein Processing II). M. genitalium does not have a I signal sequence protease<sup>634</sup> and does not cleave the signal sequences of integral membrane proteins. Integral membrane protein signal peptides are believed to help anchor proteins to the membrane<sup>3</sup>.

Following insertion into the plasma membrane and signal peptide cleavage, terminal organelle-localized lipoproteins are recruited into the terminal organelle. See the Terminal Organelle Assembly process for further discussion.

The stoichiometry, energetics, and kinetics of each protein translocation reaction were reconstructed from the primary literature<sup>1,2,10</sup> (see Table S3D and S3O). Tomkiewicz et al. reported that SecA translocates 270 pmol amino acid min<sup>−11</sup>. Doyle et al. reported that SecA translocates 20-30 amino acids per $\mathrm { A T P ^ { 2 } }$

## Computational Representation

## Mathematical Model

This process models integral membrane, lipoprotein, and secreted protein translocation into the cell membrane by the SecA preprotein translocase, the second step of post-translational processing. Because the mechanisms of protein translocation are not well characterized on the genomic scale, this process make several simplifying assumptions. First, this process decouples translation, N-terminal formylmethionine processing, and translocation by assuming that translocation does not begin until after translation termination and N-terminal formylmethionine processing. Second, this process assumes that each protein is fully translocated in a single time step. Consequently, this process collapses the translocation of each protein into a single reaction, and only represents untranslocated and fully translocated proteins. Intermediate protein localizations are not represented. Third, this process assumes that the mean arrival rate, v<sub>i</sub> of translocation events of each protein species i is independently limited by (1) the copy number of untranslocated protein, $p _ { i } ^ { u }$ , (2) the copy numbers of intracellular metabolites, $m _ { j }$ m , and (3) the copy numbers of the translocation enzymes, $e _ { j }$ . Based on these assumptions, the functional form of $v _ { i }$ is given by

$$
v _ { i } = \operatorname* { m i n } \left( \overbrace { \int _ { p _ { i } ^ { u } } ^ { u } \ , \ \sqrt { \left. \left[ \operatorname* { m i n } _ { j } \frac { m _ { j } } { M _ { j i } ^ { s } } \right] \right]}  , \overbrace { \mathrm { p o i s s o n R a n d } \left( \operatorname* { m i n } _ { j } \frac { e _ { j } } { K _ { j i } } \Delta t \right) } ^ { \mathrm { m e t a b o l i t e s } } } \right) ,\tag{S23}
$$

where $M _ { j i }$ is the stoichiometry of metabolite $j$ in the translocation of protein species i including ATP and GTP hydrolysis, $M ^ { s } = \operatorname* { m a x } { ( 0 , - M ) }$ is the negative part of M , $K _ { j i }$ is the experimentally observed catalytic rate of enzyme $j$ in the translocation of protein species i, and $i ,$ $\Delta t = 1 \mathrm { s }$ is the simulation time step.

This process implements a stochastic model of the arrival of protein monomer translocation events with relative rates $v _ { i } .$ Until protein, metabolic, and/or enzymatic resources are exhausted, the model iteratively (1) computes the arrival rate, $v _ { i } ,$ , of each translocation event, (2) selects a single translocation event to execute according to a multinomial distribution parameterized by $v _ { i } ,$ and (3) executes the selected translocation reaction, updating the copy numbers of protein monomers and metabolites and decrementing the available enzymatic capacity. Algorithm S21 outlines the implementation of the protein translocation model.

## Integration

The Protein Monomer and Protein Complex states represent the copy number of each protein translocation enzyme. The Protein Monomer state also represents the cytosolic- and membrane-localized copy numbers of each protein monomers species. The Metabolite state represents the copy number of each intracellular metabolite.

Protein are synthesized and matured in six steps (see Section 2.10). This process models protein translocation following deformylation and N-terminal methionine cleavage (see Protein Processing I process) and preceding lipoprotein diacylglyceryl transfer and lipoprotein and secreted protein signal sequence cleavage (see Protein Processing II process).

## Initial Conditions

Section 1.4 outlines the cell state initialization algorithm. Briefly, after the Mass state initializes the tota cell mass, the Protein Monomer state initializes the total copy number of each protein monomer species and initializes all monomers to their mature – processed, folded, modified, and localized – configuration. Second, the Macromolecular Complexation and Ribosome Assembly processes initialize the copy number of each ribonucleoprotein complex, and set all initialized complexes to their mature – folded and modified configuration. Finally, several processes including Transcription and Translation initialize the detailed configurations of RNA polymerases, 70S ribosomes, DNA-binding proteins, and FtsZ.

The untranslocated and translocated configurations of each protein monomer species are initialized with zero copy number because the typical occupancy these configurations is small compared to that of the mature configuration.

## Dynamic Computation

Algorithm S21 outlines the implementation of the protein translocation model.

Algorithm S21 | Protein translocation simulation. See Mathematical Model section above for definition of the mathe   
matical notation.   
Input: $p _ { i } ^ { t }$ copy number of translocated (membrane- or extracellular-localized) protein monomer species i   
Let $k _ { i } \gets e _ { i } \Delta t$ be the capacity of enzyme i for protein translocation   
repeat   
Calculate translocation rates   
foreach protein monomer species i do   
Calculate v according to $\mathsf { E q . }$ S23   
Select protein monomer species i ∼ multinomialRand(1, $v _ { i } / \sum _ { j } v _ { j } )$   
Update protein monomer copy numbers: $p _ { i } ^ { u } \gets p _ { i } ^ { u } - 1 , p _ { i } ^ { t } \gets p _ { i } ^ { t } + 1$   
Update metabolites: $m \gets m - M _ { \bullet i }$   
Update enzyme catalytic capacity: $k  k - K _ { \bullet i }$   
until no further translocation possible $( v _ { i } = 0 ~ \forall ~ i )$

## Fitting

The expression of the protein translocation enzymes was fit to provide suficient enzymes to quickly translo cate proteins, or more specifically to prevent sustained accumulation of untranslocated proteins. See Section 1.3 for further discussion.

## 3.18 Replication

## Biology

DNA replication is an integral part of the cell cycle which produces a complete chromosome for each daughter cell. DNA replication is initiated by the formation of a large multimeric DnaA complex at the origin of replication (oriC), which enables the recruiting of the DNA replication machinery to the oriC. Replication proceeds bidirectionally from the oriC to the terminus (terC), half way around the circular chromosome. The chromosome has two strands of base pairing DNA called the leading and lagging strands. Replication of the leading strand proceeds continuously the $5 '$ to $3 ^ { \prime }$ direction. Replication of the lagging strand occurs in short Okazaki fragments, also in the $5 '$ to $3 ^ { \prime }$ direction<sup>927</sup>.

## Reconstruction

The DNA replication machinery consists of multiple proteins (See Schematic S11), and there is one set of machinery for each of the two replication bubbles (on each side of the oriC). The replicative DNA helicase serves to unwind the coiled DNA<sup>628</sup>. The DNA primase makes short primers that help initiate the polymerization of a long stretch of DNA. Primers are made once at the origin for the replication of the leading strand, and one primer is made to start each Okazaki fragment<sup>606</sup>. DNA polymerization is carried out by DNA polymerase III molecules, consisting of two core subunits, a gamma complex, and beta-clamps<sup>739</sup>. One core resides on each of the leading and lagging strands, and is made up of two alpha subunits. The two cores are held together by a gamma complex, consisting of delta, delta prime, gamma, and tau subunits. The core is also bound to a sliding beta-clamp which helps anchor the polymerase to the DNA and maintain processivity. On the lagging strand, beta-clamps are swapped out each time a new DNA loop is created to make a new Okazaki fragment (See Schematic S11). A “back-up” beta-clamp binds downstream of the lagging DNA loop to facilitate this switch and formation of the next loop<sup>739</sup>. (The lagging stand polymerization requires the formation of DNA loops, so that the DNA can be polymerized in the opposite, 5’ to 3’, direction.) DNA ligases connect the separate polymerized Okazaki fragments together<sup>733</sup>. Finally, single-stranded binding proteins (SSBs) stabilize and protect single-stranded DNA, which is created as the DNA is unwound to make room for the DNA machinery<sup>637,857</sup>. For example, the lagging stand DNA loop often has long stretches of unwound DNA waiting to be polymerized. All of the replication proteins are described in List S15, and all of the parameters used in replication are described in List S16.

List S15. Enzymes and complexes used in the Replication process class.
<table><tr><td>Enzymes/Complexes</td><td>Composition</td><td>Gene Name(s)</td><td>DNA Footprints (nt)</td></tr><tr><td>DNA helicase</td><td>(6) MG094</td><td>dnaB</td><td>20</td></tr><tr><td>DNA primase</td><td>(1) MG250</td><td>dnaG</td><td>14</td></tr><tr><td>β-clamp</td><td> MG001</td><td>dnaN</td><td>25</td></tr><tr><td>DNA polymerase core</td><td>(1) MG031, (1) MG261</td><td>polC, polC-2</td><td>24</td></tr><tr><td>γ-complex</td><td>(1) MG007, (1) MG351, (4) MG419</td><td>holB, holA, dnaX</td><td>26</td></tr><tr><td>DNA ligase</td><td>(1) MG254</td><td>ligA</td><td>19</td></tr><tr><td>Single stranded binding protein (SSB) 8mer</td><td>(8) MG091</td><td>ssb</td><td>145</td></tr></table>

![](images/0edc4e2b4f9347c38e069e54925f905eafac1a79eea4ce255dc9c67e28bb976b.jpg)  
Schematic S11. Schematic of DNA replication.

## Computational Representation

Upon replication initiation (the binding of 29 DnaA-ATP molecules near the oriC by the Replication Initiation process class), the Replication process class tracks the progression of the replication proteins on the known chromosome sequences. Some bacterial species are known to have multiple replication initiation events during their life cycles. This has never been demonstrated in M. genitalium and we model up to 1 chromosome duplication event per cell cycle. Further, the exact mechanism of replication initiation in M. genitalium is unknown. M. genitalium does not include a DnaC homolog, which in other species is an essential cue for the binding of the replication machinery to the oriC. Here, the binding of 29 DnaA-ATP molecules to the oriC is the cue for replication initiation.

List S16. Fixed parameters used in the Replication process class.
<table><tr><td>Parameter</td><td>Value</td><td>Symbol</td><td>Source</td></tr><tr><td>OriC position</td><td>Base: 1</td><td> $\overline { { \mathsf { o r i C } } }$ </td><td>[182]</td></tr><tr><td>TerC position</td><td>Base: 290038</td><td> $\mathsf { t e r } \mathsf { C }$ </td><td>[182]</td></tr><tr><td>Primer length</td><td>11 nt</td><td> $l _ { \mathsf { p r i m } }$ </td><td>[606]</td></tr><tr><td>DNA polymerase elongation rate</td><td> $1 0 0 \mathsf { n t s } ^ { - 1 }$ </td><td> $k _ { \mathrm { e l } }$ </td><td>[851]</td></tr><tr><td>SSB complex spacing</td><td>30 nt</td><td> $s _ { \mathsf { S S b } }$ </td><td>[637]</td></tr><tr><td>Okazaki fragment mean length</td><td>1500 nt</td><td> $l _ { \mathsf { O F } }$ </td><td>[623, 926, 927]</td></tr><tr><td>Ligase kinetic rate</td><td> $0 . 0 4 \mathsf { s } ^ { - 1 }$ </td><td> $k _ { \mathrm { I i g } }$ </td><td>8]</td></tr><tr><td>Current Okazaki fragment length before &quot;back-up&quot; beta-clamp can bind</td><td>750 nucleotide</td><td> $l _ { \mathrm { b e t a } }$ </td><td>Set as half loF</td></tr><tr><td>Length of lagging strand loop at the start of Okazaki fragment 50 nt polymerization</td><td></td><td> $l _ { 1 \mathrm { o o p } }$ </td><td>Set to be larger than polymerase</td></tr><tr><td>DNA polymerase stall time upon anti-direction collision with RNA polymerase</td><td>1.7s</td><td> $t _ { \mathsf { s t a l l } }$ </td><td>footprint [799]</td></tr><tr><td>SSB dissociation rate</td><td> $0 . 3 { \mathsf { s } } ^ { - 1 }$ </td><td> $k _ { \mathrm { d s s b } }$ </td><td>[857]</td></tr><tr><td>Chromosome length</td><td>580076</td><td></td><td>[182]</td></tr><tr><td>Chromosome sequence</td><td>See [182]</td><td></td><td>[182]</td></tr><tr><td>DNA footprints of Proteins</td><td>See &#x27;Enzymes/</td><td></td><td>[628, 733, 739,</td></tr><tr><td>ATP cost of beta-clamp binding</td><td>Complexes&#x27; 1 ATP molecule</td><td></td><td>743]</td></tr><tr><td>ATP cost  1 base pairunwiding</td><td>1 ATP molecule</td><td> $e _ { \mathrm { b e t a } }$   $e _ { \mathsf { h e l } }$ </td><td>[628] [739]</td></tr><tr><td>NAD requirement per ligation event</td><td>1 NAD molecule</td><td> $e _ { \mathrm { l i g } }$ </td><td>[733]</td></tr></table>

To duplicate the chromosome, the exact position of each replisome protein is tracked over time on both the leading and lagging strands. The polymerization of Okazaki fragments is explicitly modeled. Since the exact primer binding sites for M. genitalium Okazaki fragments are uncharacterized, the Okazaki fragment lengths are randomly determined based on a Poisson distribution centered around the mean fragment length $\left( l _ { \mathrm { O F } } \right)$ Polymerization of both the leading and lagging strands is limited by the average rate of polymerization $\left( k _ { \mathrm { e l } } \right)$ in Mycoplasmas<sup>851</sup>, the availability of nucleotides and energy, and the available protein binding sites on the chromosome. Further, polymerization of the leading strand is prevented if additional unwinding will lead to too many unprotected single-stranded bases on the lagging stand, or if the leading polymerase will progress over two Okazaki fragment length distances beyond the lagging strand polymerase. Leading strands are not polymerized past the terC, and the lagging strands are not polymerized past the ends of Okazaki fragments.

This process outputs the progress of replication, which has a big impact on many other processes in the system. For example, the copy number of each gene plays a role in RNA polymerase binding in the Transcription process, and afects the cell’s gene expression. The duplicated regions of the chromosome have to be wound appropriately by the DNA supercoiling process, and the completion of replication triggers other cell cycle events such as the decatenation of the chromosomes by the Chromosome Segregation process.

Collisions of the replication machinery with the transcription machinery (as determined by the Chromosome state class) are also handled by the Replication process class. A helicase may collide with a RNA polymerase in two ways, head-on (RNA polymerase is traveling in a direction opposite to the helicase) or co-directionally (RNA polymerase is traveling in the same direction as the helicase)<sup>638</sup>. There is some debate in the literature regarding the pausing of the replication loop upon collisions and whether RNA polymerases are displaced upon collisions<sup>638,659,711,852,853</sup>. Based on these studies as well as modeling considerations, we assume that the RNA polymerase is always displaced upon collisions, and the replication loop is only stalled upon a head-on collision. If the helicase hits an RNA polymerase, polymerization pauses, the RNA polymerase falls of, and its transcript is degraded. If it is a head-on collision (the helicase and RNA polymerase were traveling in opposite directions on the DNA), the impact will stall progression of the replication bubble for some amount of time $( t _ { \mathrm { s t a l l } } )$ . If it is a codirectional collision, polymerization will continue at full speed the

## Integration

List S17 outlines the states integrated with the Replication process class.

List S17. State classes connected to the Replication process class.
<table><tr><td>Connected States Chromosome</td><td>Read from state</td><td>Written to state</td></tr><tr><td rowspan="7"></td><td>Whether a DnaA complex has formed at oriC</td><td>Polymerized regions of DNA</td></tr><tr><td>DNA-bound protein locations Superhelicity</td><td>DNA-bound protein locations</td></tr><tr><td>DNA strand breaks to be ligated</td><td>Unwound bases (Effect on superhelicity)</td></tr><tr><td>DNA sequence</td><td>DNA strand breaks to be ligated</td></tr><tr><td>DNA footprints of proteins</td><td></td></tr><tr><td>Chromosome regions accessible for protein</td><td></td></tr><tr><td>binding</td><td></td></tr><tr><td></td><td>Damaged DNA bases</td><td></td></tr><tr><td></td><td>OriC position</td><td></td></tr><tr><td></td><td>TerC position</td><td></td></tr><tr><td></td><td>Sequence Length</td><td></td></tr></table>

## Initial Conditions

At the beginning of the simulation, we choose Okazaki fragment lengths randomly based on a Poisson distribution around the mean length of 1500 nucleotides (l<sub>OF</sub>). From this we obtain the start position of each Okazaki fragment, to be used to determine primer, beta-clamp, and polymerase core binding during the simulation.

## Dynamic Computation

The Replication process class is built up of 8 subfunctions which move the replication proteins along the chromosomes, and evolve the DNA copy number of the cell from 1 to 2. These subfunctions are evaluated in random order, such that shared resources across subfunctions, such as energy, are allocated fairly.

## 1. Initiate Replication

• If a 29-mer DnaA-ATP complex exists at the oriC,

• If suficient proteins and metabolites exist to make 2 replisomes,

• Unwind enough DNA bases $\left( b _ { \mathrm { u n w o u n d } } \right)$ to bind 2 sets of replication machinery. One set binds on either side of the oriC. All proteins are bound to the leading strand of DNA. Each set includes:

• 1 helicase

• 1 primase

• 2 polymerase cores

• 1 gamma complex

• 1 beta-clamp

• Account for total ATP usage (as well as $_ \mathrm { H _ { 2 } O }$ usage, and ADP, Pi, and $\mathrm { H ^ { + } }$ production):

$$
\mathrm { A T P \ u s a g e } = 2 e _ { \mathrm { b e t a } } + e _ { \mathrm { h e l } } b _ { \mathrm { u n w o u n d } }
$$

• Note: following the initiation of replication, the dissociation of the DnaA complex is handled by the Chromosome state class.

## 2. Advance replisomes

• If an Okazaki fragment is starting at the current timestep,

• Bind a primase and a polymerase core to the lagging strand

• Model the unwinding and polymerizing of the DNA. The leading and lagging polymerases and helicases are advanced only so far as the following conditions are met:

Let N = the number of polymerized/unwound bases on a given strand in the given timestep.

Let P be the last polymerized position. P varies from 0 (at the oriC) to 290038 (at the terC).

$N \leq l _ { \mathrm { p r i m } }$ if a primer is being synthesized

$N \leq k _ { \mathrm { e l } }$

• Available $\mathrm { d N T P s } \leq d N T P$ requirements

• Available $\mathrm { A T P } \le N e _ { \mathrm { h e l } }$

• # Bound SSBs = Length of lagging single strand region

• Upstream DNA regions accessible to replisome proteins (no DNA damage, non-displacable proteins)

• Leading strand $P \leq t e r C$ , Lagging strand P ≤ Okazakifragmentlength

• Leading strand $P \leq 2 L _ { \mathrm { O F } } + \mathrm { l a g g i n g ~ s t r a n d } ~ P$

• $P \leq$ position of colliding RNA polymerase

## 3. Bind and Unbind SSBs

SSBs nucleate as a tetramer, binding single-stranded DNA around them. These tetramers generally bind in sets of two.

• For all single-stranded stretches of DNA,

• Randomly bind SSBs (as 8mers) to deterministically selected position (with fixed spacing: $s _ { \mathrm { s s b } } )$

• Randomly release SSB 8mers according to the dissociation rate $\left( k _ { \mathrm { d s s b } } \right)$

• Dissociate all free 8mer SSBs into two tetramer SSBs

## 4. Bind “Back-up” Beta-Clamp

The formation of a new Okazaki fragment requires the formation of a new lagging strand DNA loop. To prepare for this event, while the current Okazaki fragment is being polymerized, a “back-up” beta-clamp is bound just downstream of the start position of the next Okazaki fragment. The beta-clamp assembles as a dimer on the chromosome, and the binding event requires hydrolysis of one ATP molecule to $\mathrm { A D P } \left( e _ { \mathrm { b e t a } } \right)$

\# available beta-clamp monomers> 2

\# available $A T P { > } e _ { \mathrm { b e t a } }$

• If

Position on the DNA is accessible

Helicase has passed beta-clamp binding site

Okazaki fragment length $> l _ { \mathrm { b e t a } }$

• Bind “back-up” beta-clamp

• Decrement $\mathrm { A T P , H _ { 2 } O }$ , and increment ADP, Pi, and $\mathrm { H ^ { + } }$

## 5. Terminate Okazaki fragments

When an Okazaki fragment has been completely polymerized, its beta-clamp is released, and the end of the Okazaki fragment is marked as having a single-strand break to be ligated by DNA ligase. The lagging strand primase and polymerase associate with the “back-up” beta clamp that was previous bound. This forms a new lagging strand DNA loop.

<sup></sup>Okazaki fragment has been completely polymerized

Number of bound SSBs = <sup>Length</sup> <sup>of</sup> <sup>lagging</sup> <sup>single</sup> <sup>strand</sup> <sup>region</sup> SSB 8mer footprint×s<sub>ssb</sub>

A "back-up" clamp has been bound on the lagging strand

The replication machinery on the leading strand has advanced beyond the Okazaki start site

• Release beta-clamp

• Mark Okazaki fragment as having a single-strand break to be ligated by DNA ligase

• Associate lagging strand primase and polymerase with the “back-up” beta clamp that was previously bound (This forms a new lagging strand DNA loop.)

## 6. Ligate DNA

• If single-strand breaks exist (usually between polymerized Okazaki fragments),

• Ligate these breaks in random order up to the limits of:

• DNA ligase availability

• Ligase kinetics $\left( k _ { \mathrm { l i g } } \right)$

• NAD availability

• Decrement NAD, and increment AMP, NMM, and $\mathrm { H ^ { + } }$

## 7. Terminate Replication

• If leading and lagging strands to both sides of the terC have been completely polymerized,

• Release all replication machinery from the chromosome

• Mark terC as having a single-strand break to be ligated by DNA ligase

## Representation of Replication Machinery on the Chromosome

The Replication process class involves keeping track of the specific positions of the replication proteins on the chromosome. We define where on the chromosome the proteins bind based on the following rules:

1. The Helicase is centered on the boundary between double stranded DNA (wound) and single-stranded DNA (unwound). The position over which it is centered is the next position to be unwound.

2. There is no gap between the helicase and leading strand DNA polymerase core or between the leading strand polymerase core and the leading strand beta-clamp. Therefore, movement of the helicase control the movement of the leading strand polymerase core.

3. There is no gap between the lagging strand DNA polymerase core and the beta-clamp on the current Okazaki fragment.

4. The positions over which the polymerase cores are centered are the next position to be polymerized.

5. “Back-up” beta-clamps bind slightly upstream of the start site of the next Okazaki fragment to be polymerized such that when the next Okazaki fragment starts polymerizing, there will be no gap between the polymerase and beta-clamp, and the polymerase core will be centered on the Okazaki fragment start site.

6. At replication initiation, the mother strands are separated such that the leading polymerase cores are centered at oriC ±1 base and the helicases are 11 nucleotides $\left( \mathrm { l } _ { \mathrm { p r i m } } \right)$ ahead

7. During replication initiation (and the final step of replication after the last Okazaki fragment has completed), the lagging polymerase, beta-clamp, and primase are accounted for as part of a complex on the leading strand (containing also the helicase, leading polymerase, gamma complex, and leading betaclamp). At all other times, the lagging polymerase, lagging beta-clamp, and primase are accounted for as a complex on a diferent strand. This allows for separate tracking of the leading and lagging polymerase positions.

8. SSBs are bound at a fixed spacing $\left( \mathrm { s } _ { \mathrm { s s b } } \right)$ in the single-stranded regions of DNA.

## 3.19 Replication Initiation

## Biology

The Replication Initiation process determines when during the cell cycle chromosome duplication begins. This replication initiation time is therefore very important in determining the cell’s division time.

## Reconstruction

The mechanism of replication initiation used here is modeled after that described for E. coli by Messer involving the protein DnaA (MG469)<sup>924</sup>. Chromosome Replication begins when a complex of 29 DnaA-ATP molecules assembles near the replication origin, OriC, at specific DNA motifs called R1-R5. The assembly of this complex is rare because the DnaA molecules are titrated out by approximately 2000 additional binding sites, or ”DnaA boxes” that exist all around the chromosome<sup>925</sup>. DnaA needs to be bound to ATP or ADP to bind to these sites, and binds on and of these sites throughout the cell cycle. Binding of the DnaA-ATP at the R1-R5 sites is cooperative, enabling the large complex to form at this specific location on the chromosome.

All of the parameters used in the Replication Initiation process class are described in List S18.

List S18. Fixed parameters used in the Replication Initiation process class.
<table><tr><td>Parameter</td><td>Value</td><td>Symbol</td><td>Source</td></tr><tr><td>Positions of all the DnaA binding sites on the chromo- some(s)</td><td>(see Table S3L)</td><td></td><td>Calculated from motif in [819]</td></tr><tr><td>Factor by which DnaA-ATP to oriC site binding probabil-g ity increases when other sites are bound</td><td>85.6909</td><td> $C _ { \mathsf { s i t e } }$ </td><td>See Parameter Fitting</td></tr><tr><td>Factor by which DnaA-ATP to oriC site binding probabil- 1 ity increases when x*4 sized DnaA complex has formed at oriC</td><td></td><td> $C _ { s t a t e }$ </td><td>See Parameter</td></tr><tr><td>Rate for DnaA-ATP binding high affinity DnaA boxes</td><td> $2 5 \mathsf { n M } ^ { - 1 } \mathsf { h } ^ { - 1 }$ </td><td>kb1ATP</td><td>Fitting [448]</td></tr><tr><td>Rate for DnaA-ATP binding medium affinity DnaA boxes Rate for DnaA-ATP dissociating from the DNA</td><td> $0 . 6 \mathsf { n M } ^ { - 1 } \mathsf { h } ^ { - 1 }$ </td><td>kb2ATP</td><td>[448]</td></tr><tr><td></td><td> $2 0 \mathsf { h } ^ { - 1 }$ </td><td>kd1ATP</td><td>[448]</td></tr><tr><td>Rate for DnaA-ADP binding high affinity DnaA boxes</td><td> $2 . 5 \mathsf { n M } ^ { - 1 } \mathsf { h } ^ { - 1 }$ </td><td>kb1ADP</td><td>[448]</td></tr><tr><td>Rate for DnaA-ADP binding medium affinity DnaA boxes</td><td> $0 . 6 1 \mathsf { n } \mathsf { M } ^ { - 1 } \mathsf { h } ^ { - 1 }$ </td><td>kb2ADP</td><td>[448]</td></tr><tr><td>Rate for DnaA-ADP dissociating from the DNA</td><td> $2 0 \mathsf { h } ^ { - 1 }$ </td><td>kd1ADP</td><td>[448]</td></tr><tr><td>Rate for DnaA-ADP to DnaA-ATP regeneration</td><td> $2 . 3 \mathsf { h } ^ { - 1 }$ </td><td>k_Regen</td><td>[447]</td></tr><tr><td>Rate for DnaA-ADP to DnaA-ATP regeneration catalyzed by membrane lipids</td><td> $0 . 0 1 8 { \mathrm { g } } { \mathrm { L } } ^ { - 1 }$ </td><td>K_Regen_P4</td><td>[447]</td></tr></table>

## Parameter Assignment

All of the rate constants used in this process class were obtained from previous models of replication initiation<sup>447,448</sup>. The site and state cooperativity constants were fit according to the cell cycle length. The site and state cooperativity constants directly afect the time required for replication initiation. The total cell cycle length has been experimentally measured, and the time required for Cytokinesis and Chromosome Replication can be estimated from their process classes. Thus:

$$
{ \mathrm { t i m e } } _ { \mathrm { R e p l i c a t i o n I n i t i a t i o n } } = { \mathrm { t i m e } } _ { \mathrm { C e l l C y c l e } } - { \mathrm { t i m e } } _ { \mathrm { C y t o k n e s i s } } - { \mathrm { t i m e } } _ { \mathrm { R e p l i c a t i o n } }\tag{S24}
$$

The site and state cooperativity constants were fit such that on average the simulated cell divides in the experimentally measured amount of time.

## Computational Representation

The methods we use to model replication initiation are based on existing models by Atlas et al. and Browning et $a l . ^ { 4 4 7 , 4 4 8 }$ First, DnaA rapidly associates with ATP, and in some cases DnaA-ATP can be converted to DnaA-ADP. DnaA-ATP and DnaA-ADP molecules bind to and release from the binding sites on the chromosome. The number of binding/unbinding events that occur in a given period of time is determined by the number of available DnaA-ATP and DnaA-ADP molecules and binding/unbinding rates calculated as in Browning et $a l . ^ { 4 4 8 }$

## Binding Sites

In addition to the R1-R5 sites at the origin, there 2227 DnaA binding sites around the chromosome. All of the DnaA binding sites are based on theM. genitalium motifs described by Cordova et $a l . ^ { 8 1 9 }$ . The motifs are 9 bases long. A high afinity site is defined as one that exactly matches the motif or its reverse complement (148 sites). A medium afinity motif is defined as one that matches 8 of the 9 bases in the motif or its reverse complement (2079 sites), and a low afinity site is one that only matches 7 of 9 bases. Our model allows binding to all of the high and medium afinity sites outside of the oriC region.

We recognize 5 DnaA binding sites in the OriC region: one high afinity (R4), three medium afinity (R1-R3), and one low afinity (R5), to mimic E. coli’s 5 R-sites<sup>854</sup> and the 5 R-sites predicted for M. genitalium<sup>819</sup>. These sites reside between the genes MG469 and MG470 (bases: 578581-579224). There are 9 high and medium afinity motifs in this region, but we only recognize 4 to match the E. coli pattern, and therefore ignore the sites at genome positions 578837, 578855, 578881, 578966, and 579139. R5 matches 7 of 9 bases of the motif, so it is a very weak binder of DnaA. Since we do not know its exact mechanism/purpose we bind this site after a 28-mer DnaA-ATP initiator complex at R1-R4 is formed, and the R5 binding triggers initiation. This is the only low afinity binding site included in our model.

## 7 States

The 28-mer initiator complex consists of 7 DnaA-ATP molecules bound to each of the R1-R4 sites<sup>854</sup>. This binding is split up into 7 serial states, and in each state one additional DnaA-ATP molecule binds to each of the R1-R4 sites. All four sites must be bound before transition to the next state.

## Cooperative Binding

DnaA-ATP binding at the origin is cooperative. There are two forms of cooperativity in our model of repli cation initiation. The first type of cooperativity is state cooperativity, which helps increase the probability of transitioning into higher states. Once the binding within a state is completed, the cooperativity to transition into the next state is calculated as:

$$
\mathrm { S t a t e ~ C o o p e r a t i v i t y ~ F a c t o r } = C _ { \mathrm { { s t a t e } } } ( \mathrm { S t a t e } - 1 )\tag{S25}
$$

where $C _ { \mathrm { s t a t e } }$ is a fixed cooperativity constant. This calculation is described in Schematic S12.

The second type of cooperativity is site cooperativity, which describes the efects of the binding of one or more of the R1-R4 sites, on the probability of binding the other sites. The site cooperativity factor of a given site is 1 unless certain other R-sites are already bound, in which case the cooperativity factor changes to $C _ { \mathrm { s i t e } }$ R4 is a high afinity site, so it generally is the first to bind and has the highest cooperative efect on the other sites. The site cooperativity rules can be seen in Schematic S13).

R5 is also bound by cooperativity, given the presence of a complete 28-mer DnaA-ATP initiator complex at the R1-R4 sites. The resulting DnaA-ATP 29-mer is the trigger to begin the Replication of the chromosome.

## Post-Replication Initiation

Following initiation, the DnaA-ATP complex at the origin dissociates and hydrolyzes. DnaA molecules can continue to bind around the chromosome. The formation of a second complete initiation complex is rare because the time left in the cell cycle is generally less than that needed for an initiation event and because DnaA molecules are further titrated with a $2 ^ { n d }$ set of binding sites on the $2 ^ { n d }$ chromosome. For simplicity, we do not model a second DNA replication event.

![](images/67338dbfe0d2d6ae4d71936f316cfe652e3d34d7fc07bd61eee969e68d1c3247.jpg)  
Schematic S12. Calculation of the state cooperativity factor for DnaA-ATP binding at the origin of replication.

![](images/d4c531d3343d83d8aa4928a239e042753e7c1f8eb867b2b27dcae2e3893336dc.jpg)  
Schematic S13. Calculation of the total cooperativity factor for DnaA-ATP binding at the origin of replication.

## Integration

List S19. State classes connected to the Replication Initiation process class.
<table><tr><td>Connected States</td><td>Read from State</td><td>Written to State</td></tr><tr><td rowspan="3">Chromosome</td><td>Positions on chromosome(s) where DnaA</td><td>Updated positions on chromosome(s) where DnaA molecules are bound</td></tr><tr><td>molecules are bound Accessible DnaA binding sites</td><td></td></tr><tr><td>Copy numbers of DnaA binding sites</td><td></td></tr><tr><td rowspan="3">Mass</td><td></td><td></td></tr><tr><td>Membrane mass (used to calculate membrane</td><td></td></tr><tr><td>concentration)</td><td></td></tr><tr><td rowspan="2">Geometry</td><td>Cell volume (used to calculate membrane</td><td></td></tr><tr><td>concentration)</td><td></td></tr></table>

## Initial Conditions

This process is initialized to a steady state. The steady state amounts of free, medium afinity site bound, and high afinity site bound DnaA-ATPs and DnaA-ADPs are found using non-linear constrained optimization where we try to identify a state which is a stable point and which maximizes the amount of high afinity site bound DnaA-ATP. All DnaA proteins are either ADP or ATP bound at the initial timestep. There are also no DnaA polymers at the R1-R4 sites at the start of the simulation.

## Dynamic Computation

At each timestep, we perform the following algorithm:

## 1. DnaA activation

• Deterministically form DnaA-ATP complexes up to the limit of available DnaA and ATP. The kinetics of DnaA activation are not known, and are not modeled.

$$
{ \mathrm { N u m b e r ~ o f ~ a c t i v a t i o n ~ e v e n t s } } = \operatorname* { m i n } { \left\{ \begin{array} { l l } { { \mathrm { N u m b e r ~ o f ~ a v a i l a b l e ~ A T P ~ m o l e c u l e s } } } \\ { { \mathrm { N u m b e r ~ o f ~ f r e e ~ D n a A ~ m o l e c u l e s } } } \end{array} \right. }
$$

• Update the counts of free DnaA, DnaA-ATP, and ATP

2. DnaA-ATP complex dissociation

A complex of multiple bound DnaA-ATPs is only found near the oriC. This complex can be released from the chromosome by the DNA polymerase at the start of DNA replication. The resulting DnaA-ADP molecules are able to re-bind to the chromosome or reactivate to DnaA-ATP.

• If 29-mer DnaA-ATP complex is disrupted by the replisome machinery,

• Dissociate the complex to individual DnaA-ATP molecules

• Hydrolyze the ATP to form free DnaA-ADP molecules

• Decrement the counts of DnaA-ATP complexes and $_ \mathrm { H _ { 2 } O }$ molecules

• Increment the counts of free DnaA-ADP, $\mathrm { H ^ { + } }$ , and Pi

## 3. Binding DnaA-ATP and DnaA-ADP

Up to 7 DnaA-ATPs can polymerize at each of the origin sites and only one DnaA-ATP can bind at each site outside of the origin. Only one DnaA-ADP can bind at each site.

• If the chromosomes are suficiently supercoiled,

• Stochastically select both high and low afinity sites at the origin and around the chromosome to bind DnaA-ATP and DnaA-ADP molecules. Binding proceeds such that the rate of binding each site is as follows (where the cooperativity factor, depends on the polymerization status of the R1-R4 boxes):

$$
 \begin{array} { r l } { { \mathrm { r a t e ~ o f ~ D n a A - A T P ~ b i n d i n g ~ R 4 ~ ( h i g h ~ a f f u n i t y ) } } = { \frac { { \mathrm { k b } } { \mathrm { 1 } } { \mathrm { A T P } } \times { \mathrm { n u m e r r e e l D n a A A A T P } } } { { \mathrm { c e l l ~ v o l u m e } } \times { \mathrm { c o o p e r a t i v i t y ~ f a c t o r } } } } } \\ { { \mathrm { r a t e ~ o f ~ D n a A - A T P ~ b i n d i n g ~ R 1 - R 3 ~ ( m e d u m ~ a f f u n i t y ) } } = { \frac { { \mathrm { k b } } { \mathrm { 2 } } { \mathrm { A T P } } \times { \mathrm { n u m e r } } { \mathrm { F r e e l D n a A A A T P } } } { { \mathrm { c e l l ~ v o l u m e } } \times { \mathrm { c o o p e r a t i v i t y ~ f a c t o r } } } } } \\  { \mathrm { r a t e ~ o f ~ D n a A - A T P ~ b i n d i n g ~ n o n - o r i g i n ~ h i g h ~ a f h ~ a f h n i t y ~ s i t e s } = { \frac { { \mathrm { k b } } { \mathrm { 1 } } { \mathrm { A T P } } \times { \mathrm { n u m e r } } { \mathrm { F r e l D n a A A A T P } } } { { \mathrm { c e l l ~ v o l u m e } } } } } \\ { { \mathrm { r a t e ~ o f ~ D n a A - A T P ~ b i n d i n g ~ n o n - o r i g i n ~ m e d i u m ~ a f f n i t y ~ s i t e s } = { \frac { { \mathrm { k b } } { \mathrm { 2 } } { \mathrm { A T P } } \times { \mathrm { n u m e r } } { \mathrm { F r e l D n a A A A T P } } } { { \mathrm { c e l l ~ v o l u m e } } } } } \end{array} }
$$

The rate equations for DnaA-ADP binding are the same as above, except that the rate constants are kb1ADP and kb2ADP.

## 4. Cooperativity

The binding of DnaA-ATP to the R1-R4 sites is cooperative at two levels. Site cooperativity increases the probability of binding successive sites within a state. State cooperativity increases the probability of entering successive states. The cooperativity factors for sites R1-R4 are calculated as follows:

• Calculate the State Cooperativity Factor as described in Schematic S12:

$$
\mathrm { S t a t e ~ C o o p e r a t i v i t y ~ F a c t o r } = C _ { \mathrm { { s t a t e } } } ( \mathrm { S t a t e } - 1 )
$$

• Calculate the Site Cooperativity as described in Schematic S13. The Site Cooperativity Factor for a given site is 1 or $C _ { \mathrm { s i t e } }$ depending on the occupancy of the other R-sites

• Assign the total Cooperativity Factor for sites R1, R2, and R3 as their respective Site Cooperativity Factors

• Assign the total Cooperativity Factor for R4 as its Site Cooperativity Factor+State Cooperativity Factor

The cooperativity factors calculated here will be used in the rate calculation in Step 3.

5. Displacing DnaA-ATP and DnaA-ADP

We model the release of DnaA-ATP and DnaA-ADP molecules from their binding sites throughout the cell cycle at the following rates:

• Stochastically select DnaA-ATP and DnaA-ADP molecules to unbind from both high and low afinity sites at the origin and around the chromosome, such that the number of unbinding events is in agreement with the following rates:

6. Reactivation of DnaA-ADP to DnaA-ATP

The rejuvenation of DnaA-ADP to DnaA-ATP is incorporated similarly to that described by Atlas et al.<sup>447</sup>.   
This reaction is promoted by the acidic phospholipids cardiolipin and phosphatidylglycerol.

• Deterministically reactivate free DnaA-ADP at a rate of:

$$
\mathrm { r a t e ~ o f ~ r e a c t i v a t i o n } = \mathrm { n u m F r e e D n a A A D P } \frac { \mathrm { k \_ R e g e n ~ m e m b r a n e C o n c e n t r a t i o n } } { \mathrm { K \_ R e g e n \_ P 4 + m e m b r a n e C o n c e n t r a t i o n } }
$$

where the membrane concentration is the grams of membrane in the cell divided by the volume of the cell. These values are read from the Mass and Geometry state classes.

## 7. Replication-dependent bound DnaA-ATP release

Atlas et al. included a global term for the efect of active beta-clamps (a part of the DNA polymerase machinery) on bound DnaA-ATP inactivation<sup>447</sup>. Our model predicts the exact position of the active betaclamps on the chromosome. Therefore, we do not need to use a global term, and instead can model the release of a DnaA-ATP molecule exactly when the beta-clamp encounters it on the DNA. We however cannot distinguish between free DnaA-ATP in the cytosol and DnaA-ATP that has been recently released by a betaclamp. Therefore, we model the release in the form of DnaA-ATP and not the hydrolysis to DnaA-ADP. This beta-clamp-dependent release is handled by the DNA Replication process class and Chromosome state class.

## 3.20 Ribosome Assembly

## Biology

Ribosomes are large ribonucleoproteins which synthesize polypeptides. The M. genitalium 70S ribosome is composed of two subunits – the 30S and 50S ribosomal particles – which assemble at the mRNA Shine-Dalgarno sequence with assistance from initiation factors 1-3<sup>393,660</sup>. This process models the enzymecatalyzed formation of 30S and 50S ribosomal particles.

## Reconstruction

Table S3N lists the observed subunit composition of the 30S and 50S particles<sup>6</sup>. The 30S particle is composed of 1 RNA and 20 protein monomer subunits. The 50S particle is composed of 2 RNA and 32 protein monomer subunits. The 30S and 50S particles have both been shown to assemble in stereotyped patterns with assistance from several GTPases<sup>58,102,104,105,222,223,660,661</sup>. Era (MG387) and RbfA (MG143) have been associated with 30S particle formation<sup>104,105</sup>. EngA (MG329), EngB (MG335), Obg (MG384), and RbgA (MG442) have been associated with 50S particle formation<sup>104,105,222,223</sup>. The exact functions, kinetics, and energetics of the six GTPases are unknown.

## Computational Representation

## Mathematical Model

Because 30S and 50S ribosomal assembly are not well characterized, this process makes several simplifying assumptions to model ribosomal particle assembly. First, the process only represents individual rRNA transcripts and protein monomers and fully formed ribosomal particles. Intermediate states of ribosomal particle formation are not represented. Second, this process assumes that ribosomal particle formation is kinetically fast and energetically favorable such that ribosomal particle formation proceeds to completion within the 1 s simulation time step. Finally, the process assumes that each GTPase hydrolyzes 1 GTP molecule per ribosomal particle. With these assumptions, the rate of formation of ribosomal particle i is given by

$$
\Delta c _ { i } = \left\{ \begin{array} { l l } { \operatorname* { m i n } \left( \overbrace { \operatorname* { m i n } \frac { r _ { j } } { R _ { j i } } } ^ { \mathrm { { r R N A } } } , \overbrace { \operatorname* { m i n } \frac { p _ { j } } { P _ { j i } } } ^ { \mathrm { { p r o t e i n } } } , \overbrace { \frac { m _ { G T P } } { \eta _ { i } } } ^ { \mathrm { { G T P } } } \right) \qquad \overbrace { \left( \operatorname* { m i n } \frac { e _ { j } } { j } \right) > 0 } ^ { \mathrm { { G T P } } \mathrm { { a s e s } } } } \\ { 0 } & { \mathrm { o t h e r w i s e } } \end{array} \right.\tag{S26}
$$

where $m , r , p , c ,$ and e represent the copy number of each metabolite, rRNA transcript, protein monomer, ribosomal particle, and GTPase, $R _ { i j }$ and $P _ { i j }$ represent the stoichiometry of rRNA transcript or protein monomer i in ribosomal particle $j , E _ { i j }$ is true if ribosomal particle j formation requires GTPase i and false otherwise, and $\begin{array} { r } { \eta _ { i } = \sum _ { j } E _ { i j } } \end{array}$ is the GTP cost of forming ribosomal particle i.

This process implements a stochastic model of the arrival of ribosomal particle assembly events with relative rates $\Delta { c } _ { i }$ Until RNA, protein, metabolic, and/or enzymatic resources are exhausted, the model iteratively (1) computes the arrival rate, $\Delta { c } _ { i }$ , of each assembly event, (2) selects an event to execute according to a binomial distribution parameterized by $\Delta { c } _ { i }$ , and (3) executes the selected assembly reaction, updating the copy numbers of RNA, protein, and metabolites and decrementing the available enzymatic capacity. Algorithm S22 outlines the implementation of the Boolean ribosomal particle assembly model.

## Integration

The Rna and Protein Monomer states represents the free copy numbers of each RNA and protein monomer species. The Protein Complex state represents the copy numbers of 30S and 50S ribosomal particles and the 70S ribosome. The Ribosome state represents the (t)mRNA location of each 70S ribosome.

Several processes including Transcription and Translation model the synthesis and maturation of rRNA transcripts and protein monomers (see Section 2.12 and 2.10). The Translation process models (1) translation initiation: 70S ribosome formation at mRNA Shine-Dalgarno sequences, (2) translation elongation: 70S ribosome-catalyzed polypeptide synthesis, and (3) translation termination: mRNA release and 70S ribosome disassembly. The Translation process also models ribosome stalling whereby the mRNA template is replaced by a tmRNA and the 70S ribosome synthesizes a SsrA degradation tag at the polypeptide C-terminus, marking the nascent polypeptide for degradation. The Protein Activation process models the efect of antibiotics on the catalytic activity of 30S and 50S ribosomal particles.

## Initial Conditions

After the Mass state initializes the total cell mass, the Rna and Protein Monomer states initialize the total copy number of each rRNA and protein monomer species. Next, the Ribosome Assembly process initializes the total copy numbers of 30S and 50S ribosomal particles to a steady-state of the ribosome assembly model by evaluating Algorithm S22 with excess GTP. Finally, the Translation process initializes the copy number of 70S ribosomes, and randomly positions each 70S ribosome on mRNA weighted by the expressed copy number of each codon (see Algorithm S4).

## Dynamic Computation

Algorithm S22 outlines the implementation of the Boolean ribosomal particle assembly simulation.

## Fitting

The expression of each ribosomal RNA and protein monomer was fit to provide suficient ribosomes for translation and prevent sustained amino acid accumulation. See Section 1.3 for further discussion.

Algorithm S22 | Ribosome assembly simulation. See Mathematical Model section above for definition of the mathematical notation. matical notation.

```powershell
foreach ribosomal particle i in random order do
Calculate the extent of ribosomal particle formation, $\Delta c _ { i } ,$ , using Eq. S26
Form ribosomal subunits and decrement the copy numbers of rRNA transcripts and protein monomers.
$r \gets r - R _ { \bullet i } \Delta c _ { i }$
$p \gets p - P _ { \bullet i } \Delta c _ { i }$
$c _ { i } \gets c _ { i } + \Delta c _ { i }$
Hydrolyze GTP
$m _ { G T P } \gets m _ { G T P } - \eta _ { i } \Delta c _ { i }$
$m _ { G D P } \gets m _ { G D P } - \eta _ { i } \Delta c _ { i }$
$m _ { P i } \gets m _ { P i } - \eta _ { i } \Delta c _ { i }$
$m _ { H _ { 2 } O } \gets m _ { H _ { 2 } O } - \eta _ { i } \Delta c _ { i }$
$m _ { H ^ { + } } \gets m _ { H ^ { + } } - \eta _ { i } \Delta c _ { i }$
```

## 3.21 RNA Decay

## Biology

In presence of ribonucleases such as ribonuclease R, RNAs have relatively short half-lives compared to that of other macromolecules (eg. protein, DNA) and the M. genitalium doubling time. The relatively short halflives of RNAs enables the small M. genitalium with its very small pool of RNAs and particularly mRNAs to sample a broader range of configurations of the RNA pool over a shorter period that would be possible with longer half-lives. This helps the cell more finely tune the expression of proteins, more eficiently execute cell-cycle dependent events, and respond to the external environment. However, this enhanced fitness due to short RNA half-lives comes at a large energetic cost. In addition to ribonucleases, aminoacylated RNAs require peptidyl tRNA hydrolase to release their conjugated amino acids. This process decays all species of RNA, and at all maturation states including aminoacylated states.

## Reconstruction

RNA decay is modeled as requiring ribonuclease R (MG104). The decay of tRNAs also requires peptidyl tRNA hydrolase (Pth: MG083). Given the availability of the necessary decay enzymes, RNAs are randomly selected for degradation by a Poisson probability distribution based on the RNA half lives. All of the parameters used in the Replication Initiation process class are described in List S20.

List S20. Fixed parameters used in the RNA Decay process class.
<table><tr><td>Parameter</td><td>Value</td><td>Symbol</td><td>Source</td></tr><tr><td>Rate of peptidyl tRNA hydrolase activity</td><td> $\overline { { 0 . 7 \ { \mathsf { s } } ^ { - 1 } } }$ </td><td> $k _ { \mathrm { h y d } }$ </td><td>[26]</td></tr><tr><td>Half lives of all RNA species</td><td>See Table S3Y</td><td> $t _ { 1 / 2 i }$ </td><td>[602]</td></tr><tr><td>Decay rates of all RNA species</td><td></td><td> $k _ { \mathrm { d e c a y } \ i }$ </td><td>Derived from RNA half lives. See Transcription Process Class.</td></tr><tr><td>Reactants and products of decay reactions of all RNAs</td><td></td><td> $M _ { \tt d e c a y }$ </td><td>Computed from RNA sequences</td></tr></table>

## Computational Representation

Half-lives of all the RNA species are largely based on experimental measurements of homologous E. coli genes. The E. coli genes are mapped to the M. genitalium genes by homology. (Refer to the Transcription Process Class for additional details regarding the determination of RNA half-lives.) RNA species are randomly selected to decay from a Poisson distribution based on the half-life of each RNA species. This process class contains no intermediate representation of RNA degradation. RNA degradation is treated as an all-or-nothing event that proceeds to completion in a single timestep. Upon degradation, water is used to break the nucleotide-nucleotide bonds and the nucleotides are recycled. All aborted transcripts (due to stalled RNA polymerases or RNA polymerases that have been knock of of the DNA) are also degraded by this process.

## Integration

List S21. State classes connected to the RNA Decay process class.
<table><tr><td>Connected State</td><td>Read from state</td><td>Written to state</td></tr><tr><td rowspan="2">Rna</td><td>Count of each RNA species Updated count of each RNA species Decay Rates of all RNAs</td></tr><tr><td></td></tr><tr><td></td><td></td></tr><tr><td>Transcript</td><td>Aborted transcript sequences</td></tr></table>

## Initial Conditions

No initialization steps are required for this process.

## Dynamic Computation

1. Determine the counts of free ribonuclease R $( N _ { R } )$ and peptidyl tRNA hydrolase $( N _ { T } )$ from the Protein Monomer State Class

2. Determine the limits on the number of RNA decay events, $D _ { R } { \mathrm { : } }$

(The number of tRNA decay events is designated $D _ { T } )$

(a) If $N _ { R } = 0$ , then $D _ { R } = 0$

(All RNAs require ribonuclease R in order to decay, but ribonuclease R has a high rate of activity, so as long as $N _ { R } > 0$ , RNA decay can occur)

(b) $D _ { T } = N _ { T } k _ { \mathrm { h y d } }$

(The tRNA decay limit is dependent on the peptidyl tRNA hydrolase availability and kinetic rate)

3. Considering each RNA independently, decide whether to decay an RNA by random number selection from a Poisson distribution with a rate parameter, λcalculated as:

$$
\lambda = R N A _ { i } k _ { \mathrm { d e c a y } ~ i }\tag{S27}
$$

where $R N A _ { i }$ is the count of a given RNA species i

4. If aborted transcripts exist in the cell due to RNA polymerase stalling or RNA polymerase displacement on the DNA, decay all aborted sequences

5. Calculate the total number of metabolites used and produced from the decay of the given RNA species, using the matrix $M _ { \mathrm { d e c a y } }$ , update the counts of existing RNAs and metabolites.

## 3.22 RNA Modification

## Biology

Bacteria employ post-transcriptional base modification in order to degenerately encode approximately 61 triplet codes using far fewer tRNA species than possible using only Watson-Crick base pairing<sup>885</sup>. Modification of wobble position 34 is believed to be most important for improving codon recognition<sup>885</sup>. Bacteria modify several positions in addition to position $3 4 ^ { 8 8 5 }$ Modifications distant from the anticodon are believed to help tRNAs properly fold and stabilize their catalytically active structures<sup>885</sup>. Bacteria also posttranscriptionally modify rRNA<sup>105</sup>. rRNA modifications are believed to help stabilize rRNA, participate in protein synthesis, and confer resistance to ribosomal inhibitors<sup>105</sup>. The exact role of rRNA modification is unknown<sup>105</sup>. This process models tRNA and rRNA modification.

## Reconstruction

The M. genitalium tRNA modification complement was reconstructed based on the observed complement of E. coli modifications. Table S3AA describes the reconstruction process in detail. First, the E. coli modification complement was reconstructed<sup>45,47,55,56,64,65,560,651</sup>. Second, modifications situated in conserved

motifs were transferred to M. genitalium. The M. genitalium rRNA modification complement was similarly reconstructed (see Table S3Z). The stoichiometry and kinetics of each RNA modification reaction were reconstructed based on an extensive review of the literature (see Table S3O, S3Z, and S3AB).

## Computational Representation

## Mathematical Model

This process models non-coding RNA modification. Because the kinetics of RNA modification are not well characterized, this process make several simplifying assumptions. First, this process assumes that each RNA is fully modified in a single time step. Consequently, this process collapses the modification of each RNA into a single reaction, and only represents unmodified and fully modified RNA. Intermediate modification configurations are not represented. Second, this process assumes that the mean arrival rate, $v _ { i }$ of modification events of each RNA species i is independently limited by (1) the copy number of unmodified RNA, $r _ { i } ^ { u }$ , (2) the copy numbers of intracellular metabolites, $m _ { j }$ , and (3) the copy numbers of RNA modification enzymes, $e _ { j }$ . Based on these assumptions, the functional form of $v _ { i }$ is given by

$$
v _ { i } = \operatorname* { m i n } \left( \overbrace { r _ { i } ^ { u } } ^ { \mathrm { R N A } } , \ \overbrace { \left[ \operatorname* { m i n } _ { j } \frac { m _ { j } } { M _ { j i } ^ { s } } \right] } ^ { \mathrm { m e t a b o l i t e s } } , \ \overbrace { \mathrm { p o i s s o n R a n d } \left( \operatorname* { m i n } _ { j } \frac { e _ { j } } { K _ { j i } } \Delta t \right) } ^ { \mathrm { e n z y m e s } } \right) ,\tag{S28}
$$

where $M _ { j i }$ is the stoichiometry of metabolite $j$ in the modification of RNA species $i ,$ $M ^ { s } = \operatorname* { m a x } { ( 0 , - M ) }$ is the negative part of M, $K _ { j i }$ is the experimentally observed catalytic rate of enzyme j in the modification of RNA species $i ,$ and $\Delta t = 1$ s is the simulation time step.

This process implements a stochastic model of the arrival of RNA modification events with relative rates $v _ { i }$ Until RNA, metabolic, and/or enzymatic resources are exhausted, the model iteratively (1) computes the arrival rate, $v _ { i }$ , of each modification event, (2) selects a single modification to execute according to a multinomial distribution parameterized by $v _ { i } .$ , and (3) executes the selected modification reaction, updating the copy numbers of RNA and metabolites and decrementing the available enzymatic capacity. Algorithm S23 outlines the implementation of the RNA modification model.

## Integration

The Rna state represents the unmodified and modified copy numbers of each RNA species. The Metabolite state represents the copy number of each intracellular metabolite. The Protein Monomer and Protein Complex states represent the copy number of each RNA modification enzyme.

RNA are synthesized and matured in four steps (see Section 2.12). This process models the modification of individual non-coding RNA following RNA processing (see RNA Processing process). The Macromolecular Complexation and Ribosome Assembly processes model the formation of macromolecular complexes, including the 30S and 50S ribosomal particles. The Translation process models the function of m-, r-, s-, and tRNA in translation.

## Initial Conditions

Section 1.4 outlines the cell state initialization algorithm. Briefly, after the Mass state initializes the total cell mass, the Rna state initializes the total copy number of each RNA species and initializes all RNA to their mature – processed and modified – configuration. Second, the tRNA Aminoacylation process initializes tRNA to the aminoacylated configuration. Next, the Macromolecular Complexation and Ribosome Assembly processes initialize the copy number of each ribonucleoprotein complex. Finally, the Translation process initializes the mRNA location of each 70S ribosome.

## Dynamic Computation

Algorithm S23 outlines the implementation of the RNA modification model.

Algorithm S23 | RNA modification simulation. See Mathematical Model section above for definition of the mathematical   
notation.   
Input: $r _ { i } ^ { p }$ copy number of modified RNA species i   
Let $k _ { i } \gets e _ { i } \Delta t$ be the capacity of enzyme i for RNA modification   
repeat   
Calculate modification rates   
foreach non-coding RNA species i do   
Calculate $v _ { i }$ according to Eq. S28   
Select non-coding RNA species i ∼ multinomialRand(1, $v _ { i } / \sum _ { j } v _ { j } )$   
Update RNA copy numbers: $r _ { i } ^ { u } \gets r _ { i } ^ { u } - 1 , r _ { i } ^ { m } \gets r _ { i } ^ { m } + 1$   
Update metabolites: $m \gets m - M _ { \bullet i }$   
Update enzyme catalytic capacity: $k  k - K _ { \bullet i }$   
until no further modification possible $( v _ { i } = 0 ~ \forall ~ i )$

## Fitting

The expression of the RNA modification enzymes was fit to provide suficient enzymes to quickly modify RNA, or more specifically to prevent sustained accumulation of unmodified RNA. See Section 1.3 for further discussion.

## 3.23 RNA Processing

## Biology

Bacteria transcribe genes both individually as well in groups referred to as transcription units or operons. Operonic transcription has several advantages compared to single-gene transcription. First, operonic transcription allows cells to minimize the number of transcriptional regulators required to control gene expression. Second, operonic transcription increases the likelihood that groups of gene products have similar stoichiometry. At the same time, operonic transcription carries the costs of synthesizing intercistronic RNA and cleaving operonic non-coding transcripts into individual RNAs. Additionally, operonic transcription doesn’t provide separate control of the expression of each gene. This process models operonic RNA cleavage into individual RNA gene products.

## Reconstruction

## Transcription Unit Structure

The transcription unit organization of the M. genitalium chromosome was reconstructed by mapping the “suboperon” structure of M. pneumoniae chromosome defined by Güell et al.<sup>418</sup> on to that of M. genitalium (see Table S3U) with two modifications. First, non-coding RNA were organized into transcription units according to their “reference operons”<sup>418</sup>. Second, all mRNAs either not associated with suboperons, without M. pneumoniae homologs, or which have been rearranged since divergence from M. pneumoniae, were assigned to their own transcription units. The in silico M. genitalium chromosome is organized into 335 transcription units containing 525 genes.

## Leader Sequences

Bacteria also transcribe $3 ^ { \prime }$ and $5 '$ leader sequences before and after each non-coding RNA gene. These leader sequences must be cleaved to produce functional non-coding RNA.

## mRNA Cleavage

M. genitalium mRNA cleavage is not well described and is not modeled. The model assumes M. genitalium polycistronic mRNA are not cleaved.

## rRNA Cleavage

E. coli rRNA have been shown to be transcribed as a single 30S transcript which is cleaved into individual 5S, 16S, and 23S rRNA transcripts by the action of several ribonucleases<sup>105</sup>. The E. coli rRNA cleavage scheme was adapted and simplified for the reduced ribonuclease complement of M. genitalium by removing cleavage reactions catalyzed by non-homologous enzymes. Schematic S14 illustrates the reconstructed M. genitalium rRNA cleavage scheme. First, ribonuclease III (MG367) hydrolytically cleaves the 30S rRNA into 5S, 16S, and 23S rRNA precursors. Second, hydrolytic ribonuclease J (MG139) and phosphorolytic ribonucleases RsgA (MG110) and DeaD (MG425) cleave the 3’ and 5’ ends of the 5S and 16S rRNA precursors. M. genitalium doesn’t contain a homolog of the E. coli 9S RNA cleavage enzyme ribonuclease E. The mechanisms of 3’ and 5’ cleavage of the M. genitalium 5S rRNA precursor are unknown. 3’ and 5’ cleavage of the 5S rRNA precursor are modeled as a spontaneous process.

## sRNA Cleavage

The reconstructed M. genitalium small non-coding RNA (sRNA) precursor cleavage scheme illustrated in Schematic S14 was based on that of E. coli<sup>39,649</sup>. fs (MG0001) is cleaved at both its 3’ and 5’ ends by ribonuclease III. ribonuclease P cleaves the 5’ end of rpnB (MG0003) and ssrA (MG0004).

## tRNA Cleavage

The reconstructed M. genitalium tRNA precursor cleavage scheme illustrated in Schematic S14 was based on that of E. coli<sup>39,649</sup>. Ribonucleases III (MG367) and P (MG0003, MG465) hydrolytically cleave the 3’ and 5’ ends of each pre-tRNA, removing the 3’ and 5’ leader regions and intercistronic regions to produce individual tRNA.

![](images/c078546aa14b8ffeb16898a0831961f3df049d2b4abb2267ab309b11f9fcc6e0.jpg)  
Schematic S14. Non-coding RNA cleavage.

## Cleavage Reactions

The stoichiometry, kinetics, and energetics of each non-coding RNA cleavage reaction were reconstructed based on extensive review of the primary literature (see Table S3D and S3O).

## Computational Representation

## Mathematical Model

This process models the cleavage of operonic non-coding RNA into individual gene products and intercistronic RNA fragments. Because the kinetics of RNA cleavage are not well characterized, this process makes several simplifying assumptions. First, this process assumes that each RNA is fully cleaved in a single time step. Consequently, this process collapses the cleavage of each RNA into a single reaction, and only represents uncleaved and fully cleaved RNA. Intermediate cleavage configurations are not represented. Second, this process assumes that the mean cleavage rate, $v _ { i }$ of each RNA species i is independently limited by (1) the copy number of unprocessed RNA, r<sup>u</sup><sub>i</sub> , (2) the copy numbers of intracellular metabolites, $m _ { j } ,$ and (3) the copy numbers of RNA processing enzymes, e<sub>j</sub>. Based on these assumptions, the functional form of $v _ { i }$ is

given by

$$
v _ { i } = \operatorname* { m i n } \left( \overbrace { r _ { i } ^ { u } } ^ { \mathrm { R N A } } , \ \overbrace { \left[ \operatorname* { m i n } _ { j } \frac { m _ { j } } { M _ { j i } ^ { s } } \right] } ^ { \mathrm { m e t a b o l i t e s } } , \ \overbrace { \mathrm { p o i s s o n R a n d } \left( \operatorname* { m i n } _ { j } \frac { e _ { j } } { K _ { j i } } \Delta t \right) } ^ { \mathrm { e n z y m e s } } \right) ,\tag{S29}
$$

where $M _ { j i }$ is the stoichiometry of metabolite $j$ in the processing of RNA species i including NTP hydrolysis coupled to phosphorolytic cleavage, $M ^ { s } = \operatorname* { m a x } { ( 0 , - M ) }$ is the negative part of M , $K _ { j i }$ is the experimentally observed catalytic rate of enzyme $j$ in the processing of RNA species $i ,$ and $\Delta t = 1$ s is the simulation time step.

This process implements a stochastic model of the arrival of RNA processing events with relative rates $v _ { i } .$ Until RNA, metabolic, and/or enzymatic resources are exhausted, the model iteratively (1) computes the arrival rate, $v _ { i } ,$ of each processing event, (2) selects a single processing event to execute according to a multinomial distribution parameterized by $v _ { i }$ , and (3) executes the selected processing reaction, updating the copy numbers of RNA and metabolites and decrementing the available enzymatic capacity. Algorithm S24 outlines the implementation of the RNA processing model.

## Integration

The Rna state represents the copy numbers of unprocessed, processed, and intercistronic RNA. The Metabolite state represents the copy number of each intracellular metabolite. The Protein Monomer and Protein Complex states represent the copy number of each RNA processing enzyme.

RNA are synthesized and matured in four steps (see Section 2.12). This process models the cleavage of RNA transcripts produced by the Transcription process. The RNA Modification process models the modification of transcripts cleaved by this process. The Macromolecular Complexation and Ribosome Assembly processes model the formation of macromolecular complexes, including the 30S and 50S ribosomal particles. The Translation process models the function of m-, r-, s-, and tRNA in translation. The RNA Decay process models the degradation of cleaved intercistronic RNA fragments.

## Initial Conditions

Section 1.4 outlines the cell state initialization algorithm. Briefly, after the Mass state initializes the total cell mass, the Rna state initializes the total copy number of each RNA species and initializes all RNA to their mature – processed and modified – configuration. Second, the tRNA Aminoacylation process initializes tRNA to the aminoacylated configuration. Next, the Macromolecular Complexation and Ribosome Assembly processes initialize the copy number of each ribonucleoprotein complex. Finally, the Translation process initializes the mRNA codon location of each 70S ribosome.

## Dynamic Computation

Algorithm S24 outlines the implementation of the RNA processing model.

## Fitting

The expression of the RNA processing enzymes was fit to provide suficient enzymes to quickly process RNA, or more specifically to prevent sustained accumulation of unprocessed RNA. See Section 1.3 for further discussion.

Algorithm S24 | RNA processing simulation. See Mathematical Model section above for definition of the mathematical   
notation.   
Input: $\overline { { r _ { i } ^ { p } } }$ copy number of processed RNA species i   
Input: $r _ { i } ^ { i }$ copy number of intercistronic fragment i   
Input: $R _ { j i } ^ { g }$ is one if operonic RNA i contains gene $j ,$ and zero otherwise   
Input: $R _ { j i } ^ { \bar { i } }$ is one if operonic RNA i contains intercistronic fragment j, and zero otherwise   
Let $k _ { i } \gets e _ { i } \Delta t$ be the capacity of enzyme i for RNA processing   
repeat   
Calculate cleavage rates   
foreach operonic non-coding RNA species i do   
Calculate v<sub>i</sub> according to Eq. S29   
Select operonic non-coding RNA species i ∼ multinomialRand(1, $v _ { i } / \sum _ { j } v _ { j } )$   
Update RNA copy numbers: $r _ { i } ^ { u }  r _ { i } ^ { u } - 1 , r ^ { p }  r ^ { p } + R _ { \bullet i } ^ { g } , r ^ { i }  r ^ { i } + R _ { \bullet i } ^ { i }$   
Update metabolites: $m \gets m - M _ { \bullet i }$   
Update enzyme catalytic capacity: $k  k - K _ { \bullet i }$   
until no further cleavage possible $( v _ { i } = 0 ~ \forall ~ i )$

## 3.24 Terminal Organelle Assembly

## Biology

Balish and Krause have shown that M. genitalium maintains a flask shape with a single $3 0 0 \times 8 0$ nm membrane-bound bleb or terminal attachment organelle throughout most of its life $\mathrm { c y c l e ^ { 9 1 } }$ Krause and Balish have also shown that the M. genitalium terminal organelle divides during cell division, producing a daughter organelle which subsequently migrates to the opposite pole<sup>409</sup>. The M. genitalium terminal organelle been associated with several cellular processes including motility, adhesion, replication, and cytokinesis<sup>88,91,406–409,794,803,813</sup>. This process models the assembly of the protein content of the terminal organelle.

## Reconstruction

Krause and Balish have shown that the terminal organelle is composed of eight proteins – high molecular weight cytadherence accessory proteins (HMW) 1-3 (MG312, MG218, MG317), adhesins MgPa (MG191), P32 (MG318) and P65 (MG217), and proteins P110 (MG192) and P200 (MG386)<sup>406–409</sup>. The terminal organelle protein content is believed to assemble in the stereotyped hierarchical pattern illustrated in Schematic S15<sup>408,409</sup>. First, HMW1 and HMW2 mutually recruit each other into the terminal organelle. Second, HMW1 recruits MgPa, HMW3, and P200 into the terminal organelle. Third, HMW3 recruits P32 which in turn recruits P65. P110 independently localizes to the terminal organelle. The kinetics of terminal organelle assembly are unknown.

![](images/bbcc85ca61f647628816a349336b08729b943ceb70cfd97877aa955b20954215.jpg)  
Schematic S15. Hierarchical assembly of the M. genitalium terminal organelle.

## Computational Representation

## Mathematical Model

This process implements a Boolean model of the observed hierarchical assembly of the protein content of the M. genitalium terminal organelle. Schematic S15 outlines the Boolean assembly model. Algorithm S25 describes the model implementation in detail.

## Integration

The Protein Monomer state represents the copy number of each protein species in each of four compart ments: cytosol (c), membrane (m), and terminal organelle cytosol (tc) and membrane (tm). The Host state represents the status of the host urogenital epithelium to which the M. genitalium terminal organelle attaches.

Several processes including Translation model the synthesis and maturation of protein monomers (see Section 2.10). The Host Interaction process models the role of the terminal organelle in host attachment and immune activation.

## Initial Conditions

After the total cell mass is initialized, the Protein Monomer state initializes the terminal organelle copy number of each terminal organelle protein.

## Dynamic Computation

Algorithm S25 outlines the implementation of the Boolean terminal organelle assembly model.

## Algorithm S25 | Terminal organelle assembly simulation. Algorithm S25 | Terminal organelle assembly simulation.

if HMW1 and HMW2 expressed $( H M W 1 _ { c } + H M W 1 _ { t c } > 0$ and $H M W 2 _ { c } + H M W 1 _ { t c } > 0 )$ then   
Localize HMW1 and HMW2 to the terminal organelle   
$H M W 1 _ { t c } \gets H M W 1 _ { t c } + H M W 1 _ { c }$   
$H M W 2 _ { t c } \gets H M W 2 _ { t c } + H M W 2 _ { c }$   
$H M W 1 _ { c } \gets 0$   
$H M W 2 _ { c } \gets 0$   
if HMW1 localized to terminal organelle $( H M W 1 _ { t c } > 0 )$ then   
Localize ${ \mathsf { H M W 3 } } , { \mathsf { M g P a } } ,$ , P200 to terminal organelle   
$H M W 3 _ { t c } \gets H M W 3 _ { t c } + H M W 3 _ { c }$   
$M g P a _ { t m } \gets M g P a _ { t m } + M g P a _ { m }$   
$P 2 0 0 _ { t c } \gets P 2 0 0 _ { t c } + P 2 0 0 _ { c }$   
$H M W 3 _ { c } \gets 0$   
$M g P a _ { m } \gets 0$   
$P 2 0 0 _ { c } \gets 0$   
if HMW3 localized to terminal organelle $( H M W 3 _ { t c } > 0 )$ then   
Localize P32 to terminal organelle   
$P 3 2 _ { t m } \gets P 3 2 _ { t m } + P 3 2 _ { m }$   
$P 3 2 _ { m } \gets 0$   
if P32 localized to terminal organelle $( P 3 2 _ { t m } > 0 )$ then   
Localize P65 to terminal organelle   
$P 6 5 _ { t c } \gets P 6 5 _ { t c } + P 6 5 _ { c }$   
$P 6 5 _ { c }  0$   
Localize P110 to terminal organelle   
$P 1 1 0 _ { t m } \gets P 1 1 0 _ { t m } + P 1 1 0 _ { m }$   
$P 1 1 0 _ { m } \gets 0$

## 3.25 Transcription

## Biology

Transcription is the first step in the synthesis of functional gene products where RNA polymerase and several accessory enzymes translate transcription units (regions of the DNA containing 1 or more genes) into RNA molecules. An RNA polymerase can bind on and of of the DNA either specifically to a gene promoter or non-specifically to a non-promoter site<sup>775</sup>. Transcription begins with the recruitment of RNA polymerase to a gene promoter with the help of a sigma initiation factor and possibly transcription factors. Next elongation factors are recruited, RNA begins to be polymerized, and the sigma factor is released. In this stage, the RNA polymerase is said to be in the actively transcribing state. Finally the RNA polymerase reaches a terminator at the end of the transcription unit, and with the help of termination factors releases the polymerized RNA and dissociates from the DNA.

Termination of transcription in some bacteria can require the hexameric ATP-dependent helicase Rho<sup>233</sup>. However, Rho is not essential in B. subtilis (gram positive) or M. genitalium<sup>234</sup>, and therefore we chose to only include Rho-independent termination in our model. Rho-independent termination occurs via the intrinsic properties of RNA which disrupt RNA polymerase-DNA binding.

As soon as the RNA begins to polymerize, even prior to termination, the mRNA transcripts may be bound by ribosomes and translated to polypeptides. For simplicity, our model doesn’t represent this phenomenon, allowing translation only of completed mRNAs.

## Reconstruction

## Enzymes

All of the enzymes required for transcription are detailed in List S22.

List S22. Enzymes and complexes used in the Transcription process class.
<table><tr><td>Enzymes/Complexes</td><td>Composition</td><td>Gene Name(s)</td><td>DNA (bases)</td><td>Footprint</td></tr><tr><td>RNA polymerase sigma factor</td><td>(1) MG249</td><td>rpoD</td><td>58</td><td></td></tr><tr><td>Transcription elongation factor</td><td>(1) MG282</td><td>greA</td><td></td><td></td></tr><tr><td>Transcription termination factor</td><td>(1) MG141</td><td>nusA</td><td></td><td></td></tr><tr><td>Transcription termination/antitermination protein</td><td>(1) MG027</td><td>nusB</td><td></td><td></td></tr><tr><td>DNA-directed RNA Polymerase</td><td>(1) MG022, (2) MG177, (1) MG340, (1) MG341</td><td>rpoE, rpoA, rpoC, rpoB</td><td>75</td><td></td></tr></table>

## Parameters

The parameters required for transcription were derived from multiples sources including mircoarray gene expression data and RNA half life data. The data used and calculations performed pre-fitting, are described below:

## mRNA Gene expression data

Gene expression data for M. genitalium was unavailable, so we used data (measured at 37°C) from Mycoplasma pneumonie, the closest phylogenetic relative of M. genitalium<sup>569</sup>. The microarray data by Weiner III et al. was presented in normalized log form. Since the exact method of normalization was unknown to us, to re-derive expression levels we simply calculated 2^(presented value). The M. genitalium genome is contained in the larger M. pneumonie genome and we were able to map a M. pneumonia gene to all but 6 M. genitalium genes<sup>576</sup>. The genes were mapped based on matching gene names, matching gene descriptions, and Bio-cyc’s Align Multi-Genome Browser<sup>6</sup>.

## tRNA expression data

We also require tRNA expression estimates analogous to the mRNA microarray data. Since no microarray data is available, we use cell composition data to approximate tRNA expression<sup>870</sup>. We approximate the total tRNA expression as the total mRNA expression multiplied by the ratio of the tRNA to mRNA weight fractions of the cell. Next we need to approximate the expression of each individual tRNA. We use measurements of the relative abundances of each amino acid in the cell. A tRNA’s expression is the total tRNA expression multiplied by the fraction of the total amino acid weight represented by its amino acid<sup>53,182</sup>. For example, alanine accounts for about 8% of the total amino acid mass. Then the expression of tRNA for alanine, MG471, is 8% of the total tRNA expression. In cases of degeneracy, where multiple tRNAs bind to the same amino acid, the amino acid weight fractions is split evenly between the tRNAs.

## rRNA and sRNA expression data

Similar to the tRNA expression calculations, the total rRNA expression is calculated as the total mRNA expression multiplied by the ratio of the rRNA to mRNA weight fractions of the cell. This total rRNA expression is split between the three rRNA species (23S, 16S, 5S) based on their relative abundances in the cell. sRNA expression is also calculated in the same way, such that expression is proportional to RNA abundance in the cell.

## Half-life data

We obtained mRNA half-lives from measurements in E. coli performed at $3 0 ^ { \circ } \mathrm { C }$ in M9 minimal media<sup>602</sup>. Additional sets of E. coli half-life data are available, but we chose the set with the most comprehensive list of genes mapping to homologous M. genitalium genes, and the set whose average half-life was closest to the reported bulk E. coli mRNA half-life<sup>601,603</sup>. The gene mapping between E. coli and M. genitalium was based on common gene names and annotations, Bio-Cyc’s Align Multi-Genome Browser, and UniProt<sup>6,96,182</sup>. This have us a half-life estimate for 274 M. genitalium genes. For the remaining genes, we assigned the average half-life, 4.425 minutes. We used separate sources to acquire the half-lives of tRNAs (45 minutes), rRNAs (150 minutes), and sRNAs (89 minutes)<sup>604,608</sup>.

## Gene assignment to transcription units

The transcription unit structure (sets of genes that are transcribed together following a single promoter binding event) was compiled from several sources including primary reports<sup>176,186,188,244,247–249,411</sup> and databases<sup>182,250</sup> of cotranscribed genes, and a computational model<sup>251</sup>that predicts promoter and transcription unit start sites. We also predicted transcription units using information on the conservation of gene order across multiple species, the related functions of adjacent genes, the similar expression levels of adjacent genes as measured by microarrays, and the strandedness (transcription direction) of adjacent genes<sup>569</sup>. We transcribe the 525 M. genitalium genes in 355 transcription units. 294 genes fall in transcription units of more than one gene. The longest transcription unit contains 4 genes.

## Rate at which each transcript is produced

The rate of change of the concentration of an $R N A _ { i } ,$ is its synthesis net its degradation:

$$
\frac { d [ R N A _ { i } ] } { d t } = \underbrace { k _ { s y n t h , i } } _ { \mathrm { s y n t h e s i s } } - \underbrace { k _ { d e g , i } [ R N A _ { i } ] } _ { \mathrm { d e g r a d a t i o n } } ,\tag{S30}
$$

where $k _ { s y n t h , i }$ is the rate of synthesis and $k _ { d e g , i }$ is the rate of degradation of $R N A _ { i }$

The degradation rate is described by the first-order degradation constant of RNA<sub>i</sub> with half-life, $h _ { i }$ (obtained as described above).

$$
k _ { d e g , i } = \frac { \ln ( 2 ) } { h _ { i } }\tag{S31}
$$

At steady state RNA concentration, $\begin{array} { r } { { \frac { d [ R N A ] } { d t } } = 0 } \end{array}$

$$
k _ { s y n t h , i } = \frac { \ln ( 2 ) } { h _ { i } } \left[ R N A _ { i } \right] _ { S S }\tag{S32}
$$

The relative expression, $E _ { i } ,$ as described above, was obtained from microarray and cell composition data.

Substituting $[ R N A _ { i } ] _ { S S }$ with $E _ { i } [ R N A ]$ , where the relative expression, $E _ { i }$ , as described above, was obtained from microarray and cell composition data, and [RNA] is the total RNA concentration in the cell, we get the synthesis rate of $R N A _ { i }$ :

$$
k _ { s y n t h , i } = \frac { \ln ( 2 ) } { h _ { i } } E _ { i } \left[ R N A \right]\tag{S33}
$$

Rate at which each transcript is produced (assuming exponential growth)

We adjust the above derivation for growth and dilution. Assuming exponential growth of the cell:

$$
k _ { s y n t h , i } = k _ { s y n t h , i i n i t } e ^ { \ln ( 2 ) \frac { t } { \tau } }\tag{S34}
$$

$$
[ R N A _ { i } ] = [ R N A _ { i } ] _ { i n i t } e ^ { \ln ( 2 ) \frac { t } { \tau } }\tag{S35}
$$

where $\tau$ is the cell cycle length,

$$
\frac { d [ R N A _ { i } ] } { d t } = \underbrace { k _ { s y n t h , i i n i t } e ^ { \ln ( 2 ) \frac { t } { \tau } } } _ { \mathrm { d e g r a d a t i o n } } - \underbrace { k _ { d e g , i } [ R N A _ { i } ] _ { i n i t } e ^ { \ln ( 2 ) \frac { t } { \tau } } } _ { \mathrm { d e g r a d a t i o n } }\tag{S36}
$$

Assuming that mother and daughter cells are identically distributed:

$$
[ R N A _ { i } ] _ { t = \tau } = 2 [ R N A _ { i } ] _ { i n i t }
$$

$$
[ R N A _ { i } ] _ { i n i t } = \int \sp { \tau } { \frac { d [ R N A _ { i } ] } { d t } }\tag{S37}
$$

(S38)

$$
= \left( k _ { s y n t h , i i n i t } - k _ { d e g , i } [ R N A _ { i } ] _ { i n i t } \right) \frac { \ln ( 2 ) } { \tau }\tag{S39}
$$

$$
k _ { s y n t h , i i n i t } = [ R N A _ { i } ] _ { i n i t } \left( \frac { \tau } { \ln ( 2 ) } + k _ { d e g , i } \right)\tag{S40}
$$

Again substituting [RN A<sub>i</sub>] with $E _ { i } [ R N A ]$

$$
k _ { s y n t h , i i n i t } = E _ { i } [ R N A ] _ { i n i t } \left( \frac { \tau } { \ln ( 2 ) } + k _ { d e g , i } \right)\tag{S41}
$$

Synthesis Rate Adjustment for Transcription Units

Genes that are transcribed together in a transcription unit must have the same synthesis rate. This is because we do not model incomplete transcription of a transcription unit, where the RNA polymerase can fall of the unit, after transcribing a subset of its genes. For half-lives that have not been measured in $E .$ coli and were set to an average 4.425 minutes, we adjusted the half-lives to even out the synthesis rates within a transcription unit. For the other cases, we set the synthesis rate of the transcription unit to be the average of the rates within the transcription unit.

Determining the probabilities of making transcripts

The probability of an RNA polymerase binding a given transcription unit, i, is based on the synthesis rate of transcription unit i relative to the synthesis rate of all the other transcription units:

$$
\mathrm { P r o b a b i l i t y } ( \mathrm { t r a n s c r i b i n g ~ } i ) = P _ { t u , i }
$$

$$
= \frac { k _ { s y n t h , i } } { \sum _ { j = 1 : 3 3 5 } k _ { s y n t h , i j } }\tag{S42}
$$

(S43)

Substituting in the synthesis rate from above:

$$
\begin{array} { c } { { P _ { t u , i } = \frac { E _ { i } \left[ R N A \right] _ { i n i t } \left( \frac { \tau } { l n ( 2 ) } + k _ { d e g , i } \right) } { \sum _ { j = 1 : 3 3 5 } E _ { i } \left[ R N A \right] _ { i n i t } \left( \frac { \tau } { \ln ( 2 ) } + k _ { d e g , i } \right) } } } \\ { { = \frac { E _ { i } \left( \frac { \tau } { l n ( 2 ) } + k _ { d e g , i } \right) } { \sum _ { j = 1 : 3 3 5 } E _ { i } \left( \frac { \tau } { \ln ( 2 ) } + k _ { d e g , i } \right) } } } \end{array}\tag{S44}
$$

(S45)

## Parameter Fitting

After and all of the raw data has been transformed according to the calculations described above, and fit to assure growth of a wildtype cell that will accommodate doubling in 9hours, we reach the parameters described in List S23.

List S23. Fixed parameters used in the Transcription process class.
<table><tr><td>Parameters</td><td>Value</td><td>Symbol</td><td>Source</td></tr><tr><td>RNA polymerase elongation rate</td><td> $\overline { { 5 0 \mathsf { n t s } ^ { - 1 } } }$ </td><td> $k _ { e I }$ </td><td>[562, 563] See &#x27;Data and</td></tr><tr><td>Transcription unit binding probabilities</td><td></td><td> $P _ { t u }$ </td><td>Calculations&#x27;</td></tr><tr><td>RNA polymerase state transition probabilities</td><td></td><td> $P _ { t r a n s }$ </td><td>[775]</td></tr><tr><td>Enzyme DNA footprints</td><td>See</td><td></td><td>[747, 748]</td></tr><tr><td>Transcription unit sequences</td><td>&#x27;Enzymes/complexes&#x27;</td><td></td><td></td></tr><tr><td>Transcription unit directions</td><td>See Table S3K, [182]</td><td></td><td>[182] [182]</td></tr><tr><td>Transcription unit lengths</td><td>See Table S3K</td><td></td><td></td></tr><tr><td>Transcription unit 5&#x27; coordinates</td><td>See Table S3K</td><td></td><td>[182]</td></tr><tr><td>Cell Cycle Length</td><td>See Table S3K</td><td></td><td>[182]</td></tr><tr><td></td><td>8.9 h</td><td>τ</td><td>Experimentally</td></tr><tr><td></td><td></td><td></td><td>measured. See</td></tr><tr><td></td><td></td><td></td><td>Experimental</td></tr><tr><td></td><td></td><td></td><td>Methods.</td></tr></table>

## Computational Representation

We use a Markov model to determine the state of each RNA polymerase. An RNA polymerase may exist in any of the four following states:

1. Free (not bound to a chromosome) (FS)

2. Non-specifically bound somewhere on a chromosome (NSB)

3. Specifically bound to the promoter of a transcription unit (SB)

4. Actively transcribing a transcription unit (AT)

Transition probabilities between these states are designed to maintain the occupancy of each state within a narrow window around their expected values<sup>775</sup>. The transition probabilities $\left( P _ { t r a n s } \right)$ are determined by four logistic control functions, tuned by the RNA polymerase state expectations.

## Free State

All newly created or released RNA polymerases are in the free state. From the free state, a polymerase can transition to the non-specifically bound state, transition to the specifically bound state, or remain in the free state.

## Non-specifically bound state

From the non-specifically bound state, a polymerase can transition to the free state, transition to the specifically bound state, or remain in the non-specifically bound state. A random position on a chromosome for the non-specifically bound polymerase is selected from the polymerase accessible sites as determined by the Chromosome state.

## Specifically bound state

From the specifically bound state, a polymerase can transition to the free state, non-specifically bound state, or actively transcribing state, or remain in the specifically bound state. A polymerase can only transition into the specifically bound state if a free sigma factor is available. Upon transition a polymerase into this state, we randomly pick a transcription unit to bind to. The probability of binding each transcription unit is based on experimentally measured gene expression and half life data, as detailed below.

## Actively transcribing state

Once in the actively transcribing state, a polymerase will remain in the actively transcribing state until transcription is terminated, the RNA polymerase is displaced by another protein, or the RNA polymerase falls of due to a stall. In all these cases, the RNA polymerase falls of into the free state. For a polymerase in the actively transcribing state, we release any bound sigma factors and elongate the transcript according to nucleic acid limits (given the transcript sequence) and the elongation rate $k _ { e l }$ . The transcript and polymerase are released if transcription is complete and the necessary termination factors are available.

## Integration

List S24. State classes connected to the Transcription process class.
<table><tr><td>Connected States</td><td>Read from state</td><td>Written to state</td></tr><tr><td rowspan="2">Chromosome</td><td>Regions accessible for transcription machinery to bind</td><td>Positions and strands on the DNA where transcription machinery is bound</td></tr><tr><td>Polymerized regions of DNA</td><td></td></tr><tr><td>Rna RNA Polymerase</td><td>Counts of RNA species</td><td>Updated couents of RNA species Updated states of RNA polymerases</td></tr><tr><td rowspan="2"></td><td>RNA polymerase states (FS, NSB, SB, AT) DNA positions and strands of DNA bound RNA polymerases</td><td>Updated positions and strands of DNA boune RNA polymerases</td></tr><tr><td>Expectations of RNA polymerases in FS, NSB, SB, and AT states (used to derive transition</td><td></td></tr><tr><td rowspan="4">Transcript</td><td>Probabilities Ptrans) Transcription unit indexes of bound RNA</td><td>Updated transcription unit indexes of bound</td></tr><tr><td>polymerases RNA polymerase position within transcript</td><td>RNA polymerases Updated RNA polymerase position</td></tr><tr><td>Chromosome on which RNA polymerase resides (1 or 2)</td><td></td></tr><tr><td>Transcription unit sequences, directions, lengths, and 5&#x27; start coordinates</td><td></td></tr></table>

## Initial Conditions

All RNAs are initialized to the mature state. RNA polymerases are initialized as follows:

1. Each RNA polymerase is randomly assigned (with replacement) to one of the actively transcribing, specif ically bound, non-specifically bound, or free states weighted by the expected occupancy of each state

2. Actively transcribing and specifically bound polymerases are randomly assigned to transcription units weighted by the transcription unit binding probabilities $\left( P _ { t u } \right)$

3. Each transcription unit to which one or more actively transcribing polymerases have been assigned is divided into 1 segment for each polymerase

4. Actively transcribing polymerases are randomly assigned to positions within the assigned segment of their assigned transcription unit (positions near the segment border are not allowed to prevent polymerases from being too close to each other) with uniform probability.

5. Non-specifically bound polymerases are randomly assigned to an accessible region on the chromosome.

## Dynamic Computation

At each timestep, we follow the following algorithm:

1. Assign all newly synthesized RNA polymerases to the free state

2. Use the Markov model to randomly transition RNA polymerases among the FS, NSB, SB, and AT states, weighted by the state transition probabilities $P _ { t r a n s }$

3. Randomly assign RNA polymerases entering the NSB state to an accessible position on the Chromosome (performed by Chromosome state).

4. Randomly assign RNA polymerases entering the SB state to specific transcription units weighted by the product of the transcription unit binding probabilities $\left( P _ { t u } \right)$ and the binding probability fold changes. (Fold changes arise from other cellular processes and are described in the Transcriptional Regulation and DNA Supercoiling process classes.) We determine whether the selected promoter site is accessible and bind the polymerase to a chromosome using the Chromosome state class. RNA polymerase specific binding can only occur if there is an available sigma factor, and a sigma factor is accordingly decremented.

5. Simulate RNA polymerization by actively transcribing RNA polymerases with the aid of elongation factors.

(a) Release the sigma factor if this is the first second of elongation, and increment the free sigma factor count

(b) If all of the necessary elongation factors are available, elongate the transcript according to nucleic acid limits (given the transcript sequence) and the elongation rate $k _ { \mathrm { e l } }$ . We allocate available nucleic acids among the actively polymerizing RNA polymerases, by adding a base to each elongating transcript before moving to the next base of a given transcript. Polymerization can also be limited if the new site at which the polymerase will land is not accessible (for example, if another RNA polymerase lies in its way)

6. If transcription is complete and the necessary termination factors are available,

(a) Release the completed transcript

(b) Transition the RNA polymerase to the free state

(c) Increment the RNA count

## 3.26 Transcriptional Regulation

## Biology

Transcription factors are one of many mechanisms cells employ to respond to external signals and maintain homeostasis. Transcription factors regulate the synthesis rates of RNA by modulating the afinity of RNA polymerase for promoters. Transcriptional enhancers stabilize RNA polymerase-promoter complexes by contributing negative free energy to the complex, for example by providing additional surfaces for RNA polymerase binding. Transcriptional repressors destabilize RNA polymerase-promoter complexes, for example by sterically blocking promoters. This process models the binding of transcriptional regulators to promoters and the fold-change efect of transcriptional regulators on the afinity of RNA polymerase for individual promoters.

## Reconstruction

The M. genitalium transcriptional regulatory network was reconstructed based on an extensive review of the ium has few homologs to reported transcription factors. The reconstructed network contains five regulators which regulate 54 genes through 29 regulatory interactions, including one regulator (Spx, MG127) which interacts directly with RNA polymerase. Table S3P lists the five reconstructed transcriptional regulators and the binding site, motif, and afinity, and fold-change efect of each regulatory interaction.

## Computational Representation

## Mathematical Model

This process models the binding of transcriptional regulators to promoters and the fold-change efect of transcriptional regulators on RNA polymerase-promoter binding. Because M. genitalium transcriptional regulation is not well characterized, this process makes several simplifying assumptions. First, this process assumes that transcriptional regulator-DNA binding is kinetically fast and energetically favorable, and there fore proceeds to completion within the 1 s simulation time step. Second, because transcriptional regulatorpromoter afinities have not been systematically characterized, this process assumes that transcriptional regulators bind promoters with afinity proportional to their fold change efect. Third, this process assumes that only one copy of each transcriptional regulator can bind at each promoter. Fourth, this process assumes that transcriptional regulators stably bind DNA. Consequently, transcriptional regulator dissociation is ignored except displacement by other DNA-binding proteins which is modeled by the Transcription and Replication processes. Finally, this process assumes that transcriptional regulators independently affect RNA polymerase, and thus their fold change efects add multiplicatively. Algorithm S26 outlines the implementation of the transcriptional regulation model.

## Integration

The Protein Monomer and Protein Complex states represent the free and DNA-bound copy numbers of each transcriptional regulator. The Chromosome state represents the exact chromosomal location of each DNA-bound transcriptional regulator. The RNA Polymerase state represents the fold change efect of transcriptional regulation on the afinity of RNA polymerase for each promoter.

Several processes including Translation model protein synthesis (see Section 2.10). The Transcription process models (1) transcription initiation: RNA polymerase-promoter binding including the fold-change efects of transcriptional regulation, (2) transcript elongation, and 3) transcription termination.

## Initial Conditions

Section 1.4 outlines the cell state initialization algorithm. Briefly, after the Protein Monomer and Protein Complex states initialize the total copy number of each transcriptional regulator, the Transcriptional Regulation process initializes the status – free or DNA-bound – and chromosomal location of the transcriptional regulators to a steady-state of the transcriptional regulatory network by iteratively evaluating Algorithm S26 until convergence. Because the transcriptional regulatory model assumes that transcriptional regulatorpromoter binding proceeds to completion within the 1 s simulation time step and is stable, Algorithm S26 converges in one iteration.

## Dynamic Computation

Algorithm S26 outlines the implementation of the Transcriptional Regulation model.

```latex
Algorithm S26 | Transcriptional regulation simulation.
Input: $n _ { i k }$ is true if promoter i is expressed in chromosome k
Input: $p _ { c , i }$ free cytosolic copy number of transcriptional regulator $i$
Input: $p _ { b , i }$ DNA-bound copy number of transcriptional regulator i
Input: $\boldsymbol { x } _ { i j }$ Binding site of transcriptional regulator i at promoter $j$
Input: $F _ { i j }$ fold-change efect of transcriptional regulator i on promoter $j$
Input: $b _ { i j k l } ^ { m } , \ b _ { i j k l } ^ { c }$ chromosomal protein occupancy as defined in List $\mathsf { S 2 }$
Output: f<sub>i</sub> fold-change efect of transcriptional regulation on RNA polymerase afinity for promoter $i$
Calculate the relative rate, $r _ { i j k }$ , transcriptional regulator i binds promoter $j$ of chromosome $k \colon$
foreach DNA-binding transcriptional regulator i in promoter j of chromosome $k = \{ 1 . . 2 \}$ do
$\begin{array} { r } { \underline { \mathbf { \Lambda } } _ { r { i j k } } \gets n _ { j k } p _ { c , i } F _ { i j } } \end{array}$
Bind transcriptional regulators to the chromosome:
repeat
Select regulator $i ,$ promoter $j ,$ and chromosome $k \sim$ multinomialRand(1, $r _ { i j k } / \sum _ { i j k } r _ { i j k } )$
if regulator i expressed $( p _ { c , i } > 0 )$ and isRegionAccessible(promoter j of chromosome k to regulator i) then
Bind protein to chromosome: $b _ { y \bullet k i } ^ { z } = 1 \forall y \in \{ x _ { i j } . . x _ { i j } + l _ { i } - 1 \}$ , where $z = m$ for monomers and c for complexes
Update free and bound copy numbers: $p _ { c , i } \gets p _ { c , i } - 1 , p _ { b , i } \gets p _ { b , i } + 1$
Update binding rate: $r _ { i j k } \gets 0$
until no additional transcriptional regulator can bind DNA $( r _ { i j } = 0 \ \forall \ : i , \ j )$
Calculate the fold-change efect of transcriptional regulators on the afinity of RNA polymerase for each promoter
Initialize fold-change efects: $f _ { i } \gets 1 \ \forall \ i$
foreach promoter $j$ of chromosome $k = \{ 1 . . 2 \}$ bound by DNA-binding transcriptional regulator i do
Add fold-change efects multiplicatively: $f _ { j } \gets f _ { j } F _ { i j }$
foreach promoter $j$ regulated by an expressed non-DNA-binding transcriptional regulator i $( p _ { c , i } > 0 )$ do
$\underline { \mathbf { \Omega } } _ { - } \mathbf { \Omega } f _ { j } \gets f _ { j } F _ { i j }$
```

## 3.27 Translation

## Biology

Translation is the process whereby the ribosome, accessory enzymes, and tRNAs transcode mRNAs and produce amino acid polymers. Translation begins with the recruitment of the 30S and 50S ribosomal particles and initiation factor 3 (IF3) to an mRNA molecule. Next, the ribosomal particles assemble into a 70S ribosome on the mRNA molecule with the help of initiation factors. Third, the ribosome polymerizes amino acids presented by aminoacylated tRNAs with the help of elongation factors. Finally, a release factor recognizes the stop codon UAG or UAA, hydrolyzes the peptidyl tRNA bond, and dissociates. A ribosome recycling factor dissociates the E-site tRNA, an elongation factor G releases the release factor and 50S ribosome, and an initiation factor 3 dissociates the 30S ribosome, P-site tRNA, and mRNA<sup>393</sup>.

A ribosome may stall for various reasons including collisions with other proteins and limited resources required of translation. When a ribosome stalls, its last tRNA is expelled and replaced by the tRNA-like domain of a tmRNA molecule. Next, the mRNA-like domain of the tmRNA expels the bound mRNA. Third, the ribosome resumes polymerization, now using the tmRNA’s mRNA-like domain as its template. This results in the production of an amino acid polymer containing a C-terminal proteolysis tag. Finally, the proteolysis tag will be recognized by the protein degradation machinery, and the amino acid polymer will be degraded into its individual component amino acids<sup>226</sup>.

## Reconstruction

All of the enzymes required for translation are detailed in List S25, and all of the parameters are detailed in List S26.

List S25. Enzymes and complexes used in the Translation process class.
<table><tr><td>Enzymes/Complexes</td><td>Composition</td><td>Gene Name(s)</td></tr><tr><td>Initiation factor IF-1</td><td>(1) MG173 (1) MG142</td><td>infA</td></tr><tr><td>Initiation factor IF-2 Initiation factor IF-3</td><td>(1) MG196</td><td>infB infC</td></tr><tr><td>Elongation factor G</td><td>(MG089</td><td>fusA</td></tr><tr><td>Elongation factor P</td><td>(1) MG026</td><td>efp</td></tr><tr><td>Elongation factor Tu Elongation factor Ts</td><td> MG451</td><td>tuf</td></tr><tr><td>Peptide chain release factor 1 Ribosome recycling factor</td><td>MG433 (1) MG258</td><td>tsf prfA</td></tr><tr><td>30S ribosomal subunit</td><td>(1) MG435 (1 each) MGrrna16S, MG070, MG087, MG088, MG090, MG092,</td><td>frr 16S rRNA, rpsB, rpsL, rpsG, -, rpsR, rpsJ,</td></tr><tr><td></td><td>MG150, MG155, MG157, MG160, MG164, MG165, MG168, MG175, MG176, MG311, MG417, MG424, MG446, MG481, MG522</td><td>rpsS, rpsC, rpsQ, rpsN, rpsH, rpsE, rpsM, rpsK, rpsD,, rpsl, , rpsO, , rpsP, -, -</td></tr><tr><td>30S ribosomal subunit - initiation factor IF-3 complex 50S ribosomal subunit</td><td>(1) Ribosome_30S, (1) MG196 (1 each) MGrrna23S, MGrrna5S, MG081, MG082, MG093, MG151,</td><td>30S ribosomal subunit, infC 23S rRNA, 5S rRNA, rpIK, rplA, -, rpIC, rpID,</td></tr><tr><td></td><td>MG152, MG153, MG154, MG156, MG158, MG159, MG161, MG162, MG163, MG166, MG1676, MG169, MG174, MG178, MG197, MG198, MG257, MG325,MG361, MG362,</td><td>rpIW, rplB, rpIV, rplP, rpIC, rpIN, rpIX, rplE, rpIF, rplR, rpIO, rpmJ,, rplQ, rpml, rplT, rpmE, rpmG, -, rplL, rpmF,</td></tr><tr><td>70S ribosome</td><td>MG363, MG418, MG426, MG444, MG466, MG473</td><td>rpIM, rpmB, rplS, rpL34, rpmG-2</td></tr><tr><td></td><td>(1) Ribosome_50S, (1) Ribosome_30S</td><td>50S ribosomal subunit,</td></tr><tr><td>tmRNA, MCS6 (10sa RNA)</td><td></td><td>30S ribosomal subunit</td></tr><tr><td></td><td></td><td></td></tr><tr><td>SsrA binding protein peptidyl-tRNA hydrolase</td><td>(1) MG0004 (1) MG059 smpB</td><td>ssrA</td></tr></table>

List S26. Fixed parameters used in the Translation process class.
<table><tr><td>Parameter</td><td>Value</td><td>Symbol</td><td>Source</td></tr><tr><td>Ribosome elongation rate acids/second</td><td>(amino 16</td><td> $k _ { \mathrm { e l o n g } }$ </td><td>[564]</td></tr><tr><td>Probability that stationary ribosome is moved to a stalled state (mRNA re- placed by tmRNA)</td><td> $1 \times 1 0 ^ { - 6 }$ </td><td> $P _ { s t a l l e d }$ </td><td>See &quot;Parameter Fitting&quot;</td></tr><tr><td rowspan="2">tRNA sequences of the protein monomers tRNA sequences of the proteolysis tags</td><td></td><td></td><td>Determined from genome sequence, tRNA code [247]</td></tr><tr><td></td><td></td><td>Determined from genome sequence, tRNA code [247]</td></tr></table>

## Parameter Assignment

Most of the parameters required for this process class were obtained from the literature or derived from the M. genitalium genome sequence. The probability that a ribosome stalled is an uncharacterized value, and therefore we set this probability to be very low, such that ribosome stalling is a rare event which does not typically limit the simulation.

## Computational Representation

This process simulates protein translation by ribosomes and accessory initiation, elongation, and termination factors. Ribosomes transition from a free to active state if the necessary factors are present, and bind to an mRNA. The selection of a specific mRNA to bind to a ribosome is random and weighted by mRNA abundances. As the sequence of each gene is known, the codons presented by the mRNAs are translated using aminoacylated tRNAs and elongation factors at a rate of up to 16 amino acids per second (measured by radioactive labeling in E. coli)<sup>564</sup>. Once a stop codon has been reached, translation is terminated and the polypeptide will undergo further modifications by other processes in our simulation. The process class also simulates the identification of stalled ribosomes by the tmRNA, the replacement of the tRNA and mRNA with the tmRNA, and the synthesis of the proteolysis tag encoded by the tmRNA’s mRNA-like domain.

## Integration

List S27. State classes connected to the Translation process class.
<table><tr><td>Connected State</td><td>Read from state</td><td>Written to state</td></tr><tr><td rowspan="3">Polypeptide</td><td>List of ribosome-bound mRNAs Lengths of nascent polypeptides (proteolysis</td><td rowspan="3">Updated list of ribosome-bound mRNAs Updated lengths of nascent polypeptides (proteolysis tags)</td></tr><tr><td>tags</td></tr><tr><td>tRNA sequences of protein monomers and proteolysis tags</td></tr><tr><td rowspan="3">Ribosome</td><td>List of ribosome-bound mRNAs</td><td>Updated list of ribosome-bound mRNAs</td></tr><tr><td>Lengths of nascent polypeptides (proteolysis tags</td><td>Updated lengths of nascent polypeptides (proteolysis tags)</td></tr><tr><td>State of each ribosome: free, actively translating, or stalled</td><td>Updated state of each ribosome: free, activel translating, or stalled</td></tr><tr><td>Rna</td><td>Counts of mRNA, aminoacylated tRNA, and aminoacylated tmRNA species</td><td>Updated counts of aminoacylated tRNA and aminoacylated tmRNA species</td></tr></table>

## Initial Conditions

The simulation begins in a state in which ribosomes are already bound to mRNAs and in the process of elongating. Each ribosome is randomly assigned (without replacement) to an mRNA species, weighted by the current expression of the mRNAs. Then, each ribosome is assigned to positions within the assigned mRNA with uniform probability. No ribosomes are initialized to the stalled state, since the expected probability of stalling is negligible. No tmRNAs are initiated to the bound state.

## Dynamic Computation

Initiation

Each ribosome exists in one of two states, free or actively transcribing. Ribosomes are created in the free state and may transition to the actively transcribing state as follows:

• If ribosome factor A is present, initiation factors (IF-1, IF-2, and IF-3) are present, and one unit of energy (GTP) is available

• Randomly select free ribosomes to initiate up to the limits of ribosome factor A, initiation factors, and GTP

• Randomly select mRNA species for each initiating ribosome to bind to, weighted by the counts of each mRNA species

• Update the state of each ribosome and mRNA, and the amount of available substrates

## Elongation

Next, we elongate polypeptides. We assume that one of each elongation factor (EF-tu, TS, and G) is suficient for each ribosome, but require a separate set of factors for each ribosome. Elongation proceeds as follows:

• If elongation factors (EF-tu, TS, and G), aminoacylated tRNAs, and energy (GTP) are available,

• Randomly select actively transcribing ribosomes to elongate up to the limits of elongation factors. Available amino acids and energy are allocated among actively translating ribosomes.

• If the ribosome is newly initiated,

• Release the initiation factors

• Associate a tRNA for f-methionine to bind the first amino acid, and release a free tRNA

• Else,

• Derive the amino acid sequence of the translating gene by converting the genome sequence into a tRNA sequence using the amino acid code

• Associate aminoacylated tRNAs to bind amino acids to the growing polypeptide up to the aminoacylated tRNA limit, energy limit, and elongation limit, $k _ { \mathrm { e l o n g } }$ . Release free tRNAs

• Update the state of each ribosome, the progress of all actively translating ribosomes, and the amount of available substrates

Note, for cases in which translation of a peptide finishes partway through the time step, the elongation factors are released, but only available at the timestep. For simplicity, we do not explicitly model the transition between P an E sites.

## Termination

Once all amino acids of a protein have been translated, one release factor, one recycling factor, one elongation factor G, and one GTP molecule are suficient to terminate the polypeptide, as follows:

• If at release factors, recycling factors, elongation factors G, and energy (GTP) are available,

• Randomly select completed polypeptide-mRNA-ribosome complexes to dissociate

• Update the state of each ribosome and mRNA, monomer counts, and the amount of available substrates. The ribosome will be available to bind mRNA at the following iteration

## Translation Stalling

The stalling of ribosomes is dealt with as follows:

• If in a timestep an elongating ribosome hasn’t advanced,

• Then with a small probability, $P _ { s t a l l e d } ,$

• Transition the ribosome to the stalled state

• Expel the mRNA and replace it with a tmRNA

• Encode a proteolysis tag and mark the amino acid chain for degradation by the Protein Decay process class.

## 3.28 tRNA Aminoacylation

## Biology

The tRNA Aminoacylation process class simulates the conjugation of amino acids to the tRNAs. tRNAs serve as mediators between the ribosome and the amino acids which form polypeptides. tRNAs are composed of short RNA sequences which recognize specific codons (triplets of bases) on mRNAs. Each tRNA binds to a specific amino acid, and then interacts with a ribosome to deliver this amino acid to an elongating polypeptide chain, according to the mRNA code.

tmRNAs are short RNA structures that add a proteolysis tag to the end of incomplete polypeptides upon ribosomal stalling, signaling the polypeptides for degradation. The tRNA Aminoacylation process class also simulates the aminoacylation of the tmRNA which delivers the amino acid alanine to stalled ribosomes.

## Reconstruction

These aminoacylation reactions are both enzyme and energy dependent. M.genitalium is believed to have 36 tRNA aminoacylation reactions and 1 tmRNA aminoacylation reaction, and all of the reactions require 1 $\mathrm { A T P ^ { 5 3 , 1 0 0 } }$ There are also two tRNA modification reactions that must occur. Since there is no glutaminyltRNA synthetase (to add a glutamine to a tRNA), glutamyl-tRNA synthetase first adds a glutamate to tRNA MG502, and then Glu-tRNA Gln amidotransferase converts the glutamate into a glutamine. Also, a methionylformyltransferase is used to add the formyl group onto the methionine on tRNA MG488 (formylmethionine is used as the start codon).

All of the enzymes required for tRNA aminoacylation are detailed in List S28, and all of the parameters are detailed in List S29.

List S28. Enzymes and complexes used in the tRNA Aminoacylation process class.
<table><tr><td>Enzymes/Complexes</td><td>Composition</td><td>Gene Name(s)</td></tr><tr><td>Alanyl-tRNA synthetase</td><td>(4) MG292</td><td>alaS</td></tr><tr><td>Arginyl-tRNA synthetase</td><td>(1) MG378</td><td>argS</td></tr><tr><td>Aspartyl-tRNA synthetase</td><td>(2) MG036</td><td>aspS</td></tr><tr><td>Asparaginyl-tRNA synthetase</td><td>(2) MG113</td><td>asnS</td></tr><tr><td>Cysteinyl-tRNA synthetase</td><td>(1) MG253</td><td>cysS</td></tr><tr><td>Glutamyl-tRNA synthetase</td><td>(1) MG462</td><td>gltX</td></tr><tr><td>Glycyl-tRNA synthetase</td><td>(2) MG251</td><td>glyS</td></tr><tr><td>Histidyl-tRNA synthetase</td><td>(2) MG035</td><td>hisS</td></tr><tr><td>Isoleucyl-tRNA synthetase</td><td>(1) MG345</td><td>ileS</td></tr><tr><td>Leucyl-tRNA synthetase</td><td>(1) MG266</td><td>leuS</td></tr><tr><td>Lysyl-tRNA synthetase</td><td>(2) MG136</td><td>lysS</td></tr><tr><td>Methionyl-tRNA synthetase</td><td>(2) MG021</td><td>metG</td></tr><tr><td>Phenylalanyl-tRNA synthetase</td><td>(2) MG194, ( MG195</td><td>pheS, -</td></tr><tr><td>Prolyl-tRNA synthetase</td><td>(2) MG283</td><td>proS</td></tr><tr><td>Seryl-tRNA synthetase</td><td>(2) MG005</td><td>serS</td></tr><tr><td>Threonyl-tRNA synthetase</td><td>(2) MG375</td><td>thrS</td></tr><tr><td>Tryptophanyl-tRNA synthetase</td><td>(2) MG126</td><td>trpS</td></tr><tr><td>Tyrosyl-tRNA synthetase</td><td>(2) MG455</td><td>tyrS</td></tr><tr><td>Valyl-tRNA synthetase</td><td>(1) MG334</td><td>valS</td></tr><tr><td>Glutamyl-tRNA(GIn) amidotransferase</td><td>(1) MG098, (1) MG099, (1) MG100</td><td>-, -, gatB</td></tr><tr><td>Methionyl-tRNA formyltransferase</td><td>(1) MG365</td><td></td></tr></table>

List S29. Fixed parameters used in the tRNA Aminoacylation process class.
<table><tr><td>Parameters</td><td>Source</td></tr><tr><td>Free metabolites required for each reaction</td><td>[53, 100]</td></tr><tr><td>tRNA aminoacylated by each reaction</td><td>3, 100</td></tr><tr><td>Enzymes required to aminoacylate each tRNA</td><td>[100]</td></tr><tr><td> $k _ { c a t }$  of the catalyzing enzyme of each aminoacylation reaction  $\left( \mathsf { \mathsf { s } } ^ { - 1 } \right)$ </td><td>[100]</td></tr></table>

## Computational Representation

The tRNA Aminoacylation process maximizes the number of aminoacylation reactions (tRNA aminoacylations, tmRNA aminoacylations, and tRNA modifications) up to the limits of available RNAs, enzymes, and metabolites. The enzymatic bounds are calculated from the catalytic turnover constant $\left( k _ { c a t } \right)$ of each enzyme. The required metabolites include, among others, amino acids and ATP. Since multiple reactions require the same metabolites and enzymes, reactions to occur within a given timestep are randomly selected using a probability distribution that is weighted by the abundances of the reaction requirements. That is, the limits of each reaction are calculated assuming that all of the available required resources would be allocated to the given reaction. The probability distribution for selecting given reactions is weighted by these calculated limits. Reactions are performed one by one until insuficient resources exist to perform any additional reactions. Intermediate steps in the aminoacylation of tRNAs are not represented.

## Integration

The tRNA Aminoacylation process class reads from and writes to the Rna state class. It reads in the counts of free and aminoacylated tRNAs and tmRNA, and writes back the updated counts.

## Initial Conditions

All of the tRNAs are initialized to an aminoacylated state.

## Dynamic Computation

At each timestep,

1. For each of the 39 possible reactions (36 tRNA aminoacylations, 1 tmRNA aminoacylation, 1 Glu-Gln

amidotransfer, 1 methionylformyltransfer), i, calculate the maximum number of reactions that can occur:

<sup></sup>Number of available required metabolites (amino acid, $\mathrm { A T P , \Omega . . . ) }$ Reaction Limit i = min <sup></sup>Number of available required enzyme × $k _ { c a t }$ Number of free tRNA or tmRNA

2. The available ATP, amino acids, and enzyme activities used in the limits calculation in Step 1, may be double counted as multiple reactions may require the same metabolites or enzymes. Therefore, the selection of which reactions occur, within the calculated limits, is randomly determined. While resources are available:

(a) Randomly select a reaction to perform, weighing the probability of selecting a given reaction by its calculated reaction limit

(b) Decrement the used metabolites, enzyme activities, free tRNAs, free tmRNAs

(c) Increment the produced metabolites, and modified RNA

(d) Recalculate the reaction limits as in Step 1, based on the new availabilities

# Chapter 4

# Experimental Procedures

## 4.1 Media Composition

Each liter of SP-4 is comprised of broth base 600 ml (Mycoplasma Broth Base 3.5 g (BD 211458), Bacto Tryptone 10 g (BD 211705), Bacto Peptone 5.3 g (BD 211677), distilled water 598 ml, pH 7.5 by KOH and autoclaved), 20% glucose 25 ml (CalBioChem 346351), CMRL 1066 10X 50 ml (ATCC20-2207), 7.5% sodium bicarbonate 5 ml (EMDSX-0320-1), 200 mM L-glutamine 5 ml, 2% yeast extract solution 35 ml (BD 210933), 2% autoclaved TC Yeastolate 100 ml (BD 255772), fetal bovine serum albumin (heat inactivated at 55°C for 2 hours) 170 ml (Gibco 26140-079), penicillin G (100,000 U ml<sup>−1</sup>) 2.5 ml (Sigma P7794), and 0.5% phenol red 4 ml (Sigma P0290).

## 4.2 Frozen Stocks

Cells were harvested for storage as a frozen stock when the media in the 10 cm petri dish cultures was yellow (pH 6.3-6.7). The media from the 10 cm plate cultures was aspirated. Cells were collected by scraping the bottom of the plates, resuspended in 3 ml of FBS, and serial filtered through 1.2, 0.8, 0.45, and 0.2 µm polyethersulfone filters to sterilize and de-clump the cells. Stocks were stored at -80°C.

## 4.3 Colorimetric Growth Assay Serial Dilutions

Cells were harvested for serial dilutions when the media in the 10 cm petri dish culture was yellow (pH 6.3-6.7), and were harvested as described above for frozen stocks. The filtered suspension was used to make a serial dilution plate. The initial solution in the serial dilution plate is comprised of 50 ul of culture in 450 ul of SP-4. (For strains that were especially dificult to culture, 100 ul culture was added to 400 ul SP-4.) From this concentration we made three 5-fold serial dilutions. Dilutions were performed in triplicate for each culture, and 200 ul of each diluted sample was plated in a 96-well plate. The 96-well plates were stored at 37°C and 5% CO<sub>2</sub>. Optical density readings were taken at 550 nm twice a day and used to make growth curves.

## 4.4 Colorimetric Growth Assay Calculations

The growth rate constant and doubling time for each strain was calculated using the growth curves of serially diluted bacterial cultures measured by the colorimetric assay and the serial dilution factor.

Assuming exponential growth, the cell concentration (C) in dilution1 can be defined as:

![](images/23443e183b3ece3989d044996bb952fd6ded21a3fc9c990fde3e6882e6a02c28.jpg)  
Schematic S16. Comparison of consecutive dilutions.

$$
C _ { \mathrm { d i l u t i o n 1 , t i m e } _ { x } } = C _ { \mathrm { d i l u t i o n 1 , t i m e _ { 0 } } } \mathrm { e x p ( g r o w t h \ r a t e \times t i m e } _ { x } )\tag{S46}
$$

And the concentration of dilution2 as:

$$
C _ { \mathrm { d i l u t i o n 2 , t i m e } _ { y } } = C _ { \mathrm { d i l u t i o n 2 , t i m e } _ { 0 } } \mathrm { e x p ( g r o w t h \ r a t e \times t i m e } _ { y } )\tag{S47}
$$

Because the concentration of a dilution at the start of the experiment is five times less than that of the previous dilution:

$$
C _ { \mathrm { d i l u t i o n 1 , t i m e _ { 0 } } } = 5 C _ { \mathrm { d i l u t i o n 2 , t i m e _ { 0 } } }\tag{S48}
$$

Furthermore, the two dilutions reach a given OD550 at diferent times x and y (see horizontal arrows in Schematic S16):

$$
C _ { \mathrm { d i l u t i o n 1 , t i m e } _ { x } } = C _ { \mathrm { d i l u t i o n 2 , t i m e } _ { y } }\tag{S49}
$$

(This calculation was done at 5 OD550 values:0.26, 0.27, 0.28, 0.29, and 0.30)

By substitution, the relation for growth rate constant (for a specific pair of cultures and OD500) and is defined:

$$
{ \mathrm { g r o w t h ~ r a t e ~ c o n s t a n t } } = { \frac { \ln ( 5 ) } { \mathrm { t i m e } _ { y } - \mathrm { t i m e } _ { x } } }\tag{S50}
$$

The doubling time is then calculated as:

$$
\mathrm { d o u b l i n g ~ t i m e = \frac { l n ( 2 ) } { g r o w t h ~ r a t e ~ c o n s t a n t } }\tag{S51}
$$

## 4.5 Quantitative PCR to Measure Cell Growth

Some strains grew so slowly that the colorimetric assay was inadequate to determine a growth rate. In these cases, a DNA quantitfication method was used to estimate the growth rate. This method calculates the number of chromosomes in a sample, and assumes that changes in chromosome count is correlated with changes in the M. genitalium cell count. The strains were cultured in 4 mL SP-4 and incubated at 37°C with 5% CO<sub>2</sub>. Three replicate cultures were made for each of 14 days of harvest, resulting in 42 cultures per strain. Each day, cells were harvested by scraping the bottom of the plate, spun down at 4575 xg for 15 minutes, and resuspended in 20-400 µl of TE with 1% SDS. Samples were run on a 0.8% electrophoresis gel, and the DNA band was quantified using a Typhoon scanner and ImageQuant. The slope of the exponential region of the resulting growth curves was used to calculate a growth rate constant and doubling time (see Table S1). Comparing the relative growth of wild-type and the tkt gene deletion strain, we see that the results of the PCR method match those of the colorimetric assay.

# Computational Implementation

## A.1 Whole-Cell Model Architecture

This chapter outlines the computational implementation of the whole-cell model and briefly summarizes the most important whole-cell model classes and functions. All of the source code for the whole-cell model, as well as comprehensive documentation of each class and function is freely available at SimTK: http: //www.simtk.org/home/wholecell.

As illustrated in Schematic S17, the Simulation class coordinates the entire whole-cell model and is the primary class users interact with to execute the whole-cell model.

![](images/b77fd6ddf101b0f0c5849e74e70d607bb2b76a179b17ecbba360fa39bda05a4e.jpg)  
Schematic S17. Whole-cell model architecture.

The Simulation class performs several functions to coordinate the whole-cell model. First, the Simulation class instantiates all of the states and processes. Second, the Simulation class constructs an object graph of the states and processes. Specifically, the Simulation class triggers the states and process to store references to the other states and processes with which they will interact during the simulation. Third, the Simulation class initializes the structural and quantitative parameters of each state and process. Specifically, the Simulation class passes the KnowledgeBase to the states and processes and triggers the states and process to retrieve data from the knowledge base. Fourth, the Simulation class manages the calculation of the initial cell state by triggering initialization methods of the states and processes. Fifth, the Simulation class oversees the simulation time line. Sixth, at each time step of the simulation the Simulation class orchestrates the calculation of the temporal evolution of the cell state by allocating shared resources among the processes and triggering the temporal evolution method of each of the processes. Finally, at each time step of the simulation the Simulation class triggers loggers to store the predicted values of the states.

The role of cell state allocation is most clearly illustrated by counterexample. If processes were executed serially and each process was passed the total count of each metabolite at the beginning of the time step, then there would be no constraint which prevents the processes from together using more than the total amount of a metabolite, resulting in a negative and unphysical metabolite count. If alternatively the processes were executed serially in the same order at each time step and each process updated the cell state following its execution, then there would be no constraint which prevents the earliest executed processes from using all of the copies of a metabolite needed by a later executed process. If processes were executed as in the previous example, except that processes were executed in a random order at each time step, then early processes could outcompete later processes as before, resulting in high frequency artifacts where processes randomly oscillate between metabolically on and of states on the same time scale as the simulation time step. In summary, input allocation has the benefit of reducing the process evaluation order dependence of the model without introducing high frequency artifacts.

The KnowledgeBase class represents the reconstructed M. genitalium knowledge base and provides this data to the states and processes. The KnowledgeBase is constructed outside the Simulation class, and is passed to the Simulation class to set the values of the parameters of the states and processes. The M. genitalium knowledge base was implemented in MySQL. The knowledge base web-interface was implemented in PHP.

Each cellular process sub-model is implemented as a subclass of Process and each cellular state is imple mented as a subclass of CellState. This standardizes the implementation of the processes and states, and in particular, ensures that each process and state exposes a common interface. Specifically, each state class (1) implements a common method to retrieve structural and quantitative data from the KnowledgeBase, (2) implements a common method to initialize its value at the beginning of each simulation, (3) implements a common method to calculate its contribution to the total cell mass, and (4) sets the value of a common property which tells the loggers which properties to store at each time step.

Each process class implements common methods that (1) retrieve structural and quantitative data from the KnowledgeBase, (2) model each process’ contribution to the initialization and temporal evolution of the cell state, and (3) calculate the instantaneous and total life cycle metabolic and enzymatic requirements of each process. In addition to implementing the Process interface, each process satisfied a contract with the cell state classes to conserve mass and synchronize the redundantly represented parts of the cell state. For example, the process classes maintained synchrony between the DNA-bound copy number of each protein complex represented by the Protein Complex state and the location of each DNA-bound protein complex represented by the Chromosome state. Unit testing was used to verify that this contract between the states and processes was upheld.

The role of the FitConstants class is to fit the whole-cell model predictions to match the experimentally observed properties of M. genitalium including the mass doubling time, chemical composition, and RNA decay and expression. The FitConstants class implements an algorithm which computationally refines the values of the parameters of the states and processes. See Section 1.3 for further discussion of the simulation fitting algorithm.

The role of the Logger classes is to store the simulated dynamics represented by the cell states, and to later retrieve this information for computational analysis. Logged dynamics are plotted and analyzed by the several classes in the analysis package, including the PaperFigures class which produces Figure 2-6 of the accompanying manuscript.

## A.2 Test-Driven Development

The whole-cell model was extensively tested throughout the development process to ensure correctness. Using the MATLAB xUnit framework<sup>894</sup>, we developed 1,058 tests of the whole-cell model MATLAB code, including 100% of all state and process class methods and 92% of all state and process class lines. First, we developed 791 tests of each individual state and process class. For example, we developed several tests of the Metabolism process which check that the predicted and observed growth rates are approximately equal, that the predicted growth rate responds correctly to the external environment and enzyme copy numbers, and that the Metabolism process conserves mass. Second, we developed 41 tests of collections of related processes and states. For example, we developed several tests of the process classes responsible for modeling translation and protein maturation. These tests check that these processes receive adequate amino acids from the Metabolism process, translate mRNA, and produce mature proteins. Third, we developed five tests of the entire simulation which check that the model predicts exponential growth with growth rates approximately equal to the experimentally observed rate, that all of the mass fractions – DNA, RNA, protein, metabolite, etc. – of the cell are approximately equal to their experimentally observed sizes, that the simulated and observed gene expression are approximately equal, and that the simulation obeys mass conservation. Stochastic functions were tested by checking the mean of their outputs. Additionally, we developed tests of the KnowledgeBase, analysis, and utility classes.

The whole-cell model code was maintained using Subversion<sup>896</sup>. All tests were run at each code revision using the freely available Hudson continuous integration server<sup>895</sup>, providing rapid feedback throughout the development process.

Separately, the model was experimentally validated as discussed in the accompanying manuscript and Section 1.6.

## A.3 Distributed Simulation

The whole-cell model was implemented in object-oriented MATLAB (R2010b) and simulated on a 128 core Rocks (v5.4)<sup>897</sup> Linux cluster. Simulation code was compiled using the MATLAB compiler<sup>900</sup> and executed on the cluster nodes using the freely distributable MATLAB component runtime<sup>900</sup>. The open-source resource manager Torque<sup>899</sup> and cluster scheduler Maui<sup>898</sup> were used to distribute simulation jobs among the cluster nodes.

## A.4 Computational Analysis

The whole-cell model simulations were analyzed using the MATLAB code in the edu.stanford.covert.cell.   
sim.analysis package.

## A.5 Knowledge Base

The M. genitalium knowledge base was stored using a modified version of the BioWarehouse schema<sup>918</sup> in a MySQL relational database. Several tables and columns were added to the BioWarehouse schema primarily to represent additional functional genomic data. The knowledge base was viewed and edited using a web-interface implemented in PHP. The KnowledgeBase classes represented the knowledge base MySQL relational database in MATLAB.

## A.6 Source Code Organization

The whole-cell model source code is available at SimTK, http://www.simtk.org/home/wholecell. The model source code is contained in the simulation/src directory and organized into several packages using the Java package naming convention:

• edu.stanford.covert.cell.sim: Simulation class and cellular process and state superclasses

• edu.stanford.covert.cell.sim.analysis: simulation analysis code

• edu.stanford.covert.cell.sim.constant: classes which represent constants such gene names

• edu.stanford.covert.cell.sim.process: implementations of all cellular processes

• edu.stanford.covert.cell.sim.state: implementations of all cell states

• edu.stanford.covert.cell.sim.util: utility classes for fitting, logging, plotting, printing, and more

• edu.stanford.covert.cell.kb: classes which represent the M. genitalium knowledge base

• edu.stanford.covert.db: classes for interacting with MySQL relational databases

• edu.stanford.covert.io: classes for reading and writing MAT- and JSON-formatted data

• edu.stanford.covert.test: classes for unit test logging, assessing code coverage, and mocking

• edu.stanford.covert.util: various utility functions

The simulation directory contains several unpackaged MATLAB, Perl, PHP, and Shell scripts for running simulations and unit tests on individual machines and compute clusters. The whole-cell model test code is similarly organized to the source code in the simulation/src\_test directory. The knowledge base source code is located in the knowledgebase directory.

## A.7 Key Classes & Functions

## A.7.1 CellState

edu.stanford.covert.cell.sim.CellState is the base class from which all cell state classes are derived. CellState defines the interface each state exposes to Simulation. This interface enables Simulation to construct each state using data from the knowledge base, initialize the value of each state, account for the contribution of each state to the total cell mass, and log the dynamics of each state to disk. Molecule-CountState extends CellState by defining properties which represent the identity and copy numbers of molecules, and by providing a function which calculates the state’s contribution to the total cell mass.

## A.7.2 Chromosome

edu.stanford.covert.cell.sim.state.Chromosome implements the Chromosome state and provides an API which cellular process classes use to modify the chromosome object. To eficiently represent chromosomes, each property of the Chromosome class, except catenation, is implemented as an instance of the CircularSparseMat class of size L × 4 where the first two columns represent the base-paired strands of the first chromosome and the second two columns represent the second chromosome. List S31 summarizes the properties of the Chromosome class. polymerizedRegions(i, j) sparsely represents the length in nt of a contiguous DNA strand starting at nucleotide i of strand/chromosome $j .$ linkingNumbers $( i , j )$ sparsely represents the linking number of a contiguous double-stranded DNA region starting at nucleotide i of strand/chromosome $j .$ gapSites(i, j) is true if the sugar-phosphate of nucleotide i of strand/chromosome $j$ is absent, and false otherwise. abasicSites(i, j) is true if the base of nucleotide i of strand/chromosome $j$ is absent, and false otherwise. damagedBases(i, j) and damagedSugarPhosphates $( i , j )$ are enumerations indicating the Metabolite identity of the base and sugar-phosphate of nucleotide i of strand/chromosome $j .$ intrastrandCrossLinks(i, j) is true if nucleotide i of strand/chromosome $j$ is cross linked to nucleotide i + 1 of the same strand and chromosome, and false otherwise. strandBreaks $( i , j )$ is true if the phosphodiester bond between nucleotides i and i + 1 of strand/chromosome $j$ is broken, and false otherwise. hollidayJunctions $( i , j )$ is true if nucleotide i of strand/chromosome $j$ forms a Holliday junction with the opposite strand, and false otherwise. monomerBoundSites $( i , j )$ and complexBoundSites(i, j) are enumerations indicating the Protein Monomer or Protein Complex identity of the protein bound starting at nucleotide i of strand/chromosome j.

Due its complexity, the Chromosome class provides an API which process classes use to access and modify its properties. First, the API allows the Chromosome class to prevent processes from specifying invalid configurations of the chromosome state such as single-stranded binding proteins binding to double-stranded DNA or multiple proteins occupying the same nucleotide. Second, the API ensures that the Chromosome properties remains synchronized with the rest of the cell state. In particular, the API ensures that the monomerBoundSites and complexBoundSites properties remain synchronized with the copy numbers of DNA-bound proteins stored in the Protein Monomer and Protein Complex classes. Third, the API provides an abstraction layer over the chromosome representation, allowing process classes to focus on modeling biology. In particular, the API provides process classes methods for calculating the chromosomal regions accessible to each protein species and binding and releasing proteins to and from the chromosome. Furthermore, the API centralizes the modeled interactions among DNA-binding proteins, and specifically the reconstructed rules which describe the bound proteins each protein species is able to displace from the chro mosome (see Table S3O). Fourth, the API eliminates the need to redundantly implement similar codes in each of the chromosome-interacting process classes. Finally, the API allows the Chromosome class to implement caching and other strategies to optimize simulation run-time performance. List S30 summarizes the public methods of the Chromosome class.

Each chromosome-interacting process class inherits from ChromosomeProcessAspect. This class provides several additional methods to help process classes interact with the Chromosome class. See Section A.7.3 for further discussion of the implementation of ChromosomeProcessAspect.

List S30. Chromosome class public methods.
<table><tr><td>Function</td><td>Description</td></tr><tr><td>Accessors</td><td></td></tr><tr><td>isRegionSingleStranded</td><td>Checks if region is single-stranded.</td></tr><tr><td>isRegionDoubleStranded</td><td>Checks if region is double-stranded.</td></tr><tr><td>isRegionPolymerized</td><td>Checks if region is polymerized.</td></tr><tr><td>isRegionNotPolymerized</td><td>Checks if region is not polymerized.</td></tr><tr><td>isRegionProteinFree</td><td>Checks if region is not occupied by proteins.</td></tr><tr><td>isRegionUndamaged isRegionAccessible</td><td>Checks if region is unmodified (except methylated Munl R/M sites). Checks if a protein species can bind a region. Checks if region is polymer-</td></tr><tr><td>getAccessibleRegions</td><td>ized, protein free or the query protein is capable of displacing all bound proteins, and undamaged.</td></tr><tr><td>sampleAccessibleSites</td><td>Returns all regions accessible (polymerized, protein free or the query pro- tein is capable of displacing all bound proteins, and undamaged) to a protein species. Efficiently returns a short list of regions accessible (polymerized, protein</td></tr><tr><td>sampleAccessibleRegions</td><td>free or the query protein is capable of displacing all bound proteins, and undamaged) to a protein species. Efficiently returns a short list of sites vulnerable to a specific type of DNA</td></tr><tr><td>Modifiers</td><td>damage.</td></tr><tr><td>setRegionPolymerized</td><td></td></tr><tr><td>setRegionUnwound</td><td>Marks a region polymerized.</td></tr><tr><td></td><td>Moves a region of strand 2 of chromosome 1 to strand 2 of chromosome 2. Conserves the linking number of chromosome 1 by increasing the super-</td></tr><tr><td>setSiteProteinBound</td><td>helical density of the downstream double-stranded region of chromosome 1. If the region is accessible to the query protein, binds query protein to</td></tr><tr><td>setRegionProteinUnbound</td><td>region. Displaces any previously bound proteins. Updates Protein Mon- omer and Protein Complex states. Releases all proteins bound to a region. Updates Protein Monomer and</td></tr><tr><td>setSiteDamaged</td><td>Protein Complex states. Introduces a gap site, abasic site, modified base or sugar phosphate, cross</td></tr><tr><td>stochasticallySetProteinUnbound</td><td>link, strand break, or Holliday junction at the query nucleotide.</td></tr><tr><td>modifyBoundProtein</td><td>Stochastically releases all copies of a protein species at a specified prob- ability. Updates Protein Monomer and Protein Complex states. If the query protein and previous bound protein have the same footprint,</td></tr></table>

## A.7.3 ChromosomeProcessAspect

edu.stanford.covert.cell.sim.ChromosomeProcessAspect provides several convenience methods which cellular process classes use to access and modify the properties of the Chromosome class. S32 summarizes the public methods of the ChromosomeProcessAspect class.

List S31. Computational representation of the Chromosome class.
<table><tr><td>Physical Property</td><td>Name</td><td>Size</td><td>Type</td></tr><tr><td>Polymerization</td><td>polymerizedRegions</td><td> $\overline { { L \times 4 } }$ </td><td>CircularSparseMat&lt;int&gt;</td></tr><tr><td>Winding</td><td>linkingNumbers</td><td> $L \times 4$ </td><td>CircularSparseMat&lt;double&gt;</td></tr><tr><td>Modification</td><td></td><td></td><td></td></tr><tr><td>Gap site</td><td>gapSites</td><td> $L \times 4$ </td><td>CircularSparseMat&lt;logical&gt;</td></tr><tr><td>Abasic site</td><td>abasicSites</td><td> $L \times 4$ </td><td>CircularSparseMat&lt;logical&gt;</td></tr><tr><td>Sugar-phosphate</td><td>damagedSugarPhosphates</td><td> $L \times 4$ </td><td>CircularSparseMat&lt;int&gt;</td></tr><tr><td>Base</td><td>damagedBases</td><td> $L \times 4$ </td><td>CircularSparseMat&lt;int&gt;</td></tr><tr><td>Intrastrand cross link</td><td>intrastrandCrossLinks</td><td> $L \times 4$ </td><td>CircularSparseMat&lt;logical&gt;</td></tr><tr><td>Strand break</td><td>strandBreaks</td><td> $L \times 4$ </td><td>CircularSparseMat&lt;logical&gt;</td></tr><tr><td>Holliday junction</td><td>hollidayJunctions</td><td> $L \times 4$ </td><td>CircularSparseMat&lt;logical&gt;</td></tr><tr><td>Protein occupancy</td><td></td><td></td><td></td></tr><tr><td>Monomer</td><td>monomerBoundSites</td><td> $L \times 4$ </td><td>CircularSparseMat&lt;int&gt;</td></tr><tr><td>Complex</td><td>complexBoundSites</td><td> $L \times 4$ </td><td>CircularSparseMat&lt;int&gt;</td></tr><tr><td>Catenation</td><td>segregated</td><td> $1 \times 1$ </td><td>logical</td></tr></table>

List S32. ChromosomeProcessAspect class public methods.
<table><tr><td>Function</td><td>Description</td></tr><tr><td>Accessors</td><td></td></tr><tr><td>isDnaBound</td><td>Checks if a site is bound by a specified protein species.</td></tr><tr><td>findProteinInRegion</td><td>Returns positions of a protein species within a specified region.</td></tr><tr><td>Modifiers bindProteinToChromosome</td><td></td></tr><tr><td></td><td>Convenience function for setSiteProteinBound. Updates local enzyme state and global Protein Monomer and Protein Complex states.</td></tr><tr><td>bindProteinToChromosomeStochastically</td><td>Binds multiple copies of a protein species to specified positions each with a specified probability. Updates local enzyme state and global Protein Monomer and Protein Complex states.</td></tr><tr><td>modifyProteinOnChromosome</td><td>Convenience function for modifyBoundProtein. Updates local en- zyme state and global Protein Monomer and Protein Complex states.</td></tr><tr><td>releaseProteinFromChromosome</td><td>Convenience function for stochasticallySetProteinUnbound. Updates local enzyme state and global Protein Monomer and Pro- tein Complex states.</td></tr><tr><td>releaseProteinFromSites</td><td>Convenience function for setRegionProteinUnbound. Updates lo- cal enzyme state and global Protein Monomer and Protein Com-</td></tr></table>

## A.7.4 CircularSparseMat

edu.stanford.covert.util.CircularSparseMat eficiently represents sparse, circular, multidimensional matrices. CircularSparseMat inherits from SparseMat, adding support for circular matrix reference and assignment. Several properties of the Chromosome class are implemented as instances of CircularSparse-Mat.

## A.7.5 Compartment

edu.stanford.covert.cell.sim.constant.Compartment defines the identifier and name of each of the six modeled compartments: cytosol, extracellular space, membrane, nucleoid, terminal organelle cytosol, and terminal organelle membrane. State classes which derive from MoleculeCountState represent the copy number of each molecule in each of these six compartments.

## A.7.6 DatabaseLogger

edu.stanford.covert.cell.sim.util.DatabaseLogger provides methods to store and retrieve simulated single cell dynamics and simulation meta data to/from a relational database. DatabaseLogger implements the logger interface defined by Logger.

## A.7.7 DiskLogger

edu.stanford.covert.cell.sim.util.DiskLogger was the primary logger used to store the simulated single cell dynamics. DiskLogger provides methods to store and retrieve the simulated dynamics of individual cells and simulation meta data to/from disk. DiskLogger implements the logger interface defined by Logger. SimulationEnsemble provides methods to retrieve simulated data stored by DiskLogger for multiple cells. SimulationDiskUtil provides methods to retrieve and search simulation meta data.

## A.7.8 FitConstants

edu.stanford.covert.cell.sim.util.FitConstants provides several methods for fitting the simulated dynamics of cellular populations to experimental observations as well as computationally aligning the quantitative parameters of the cellular process sub-models such that the sub-models are mutually consistent. See Section 1.3 for further discussion of simulation fitting.

## A.7.9 Gene

edu.stanford.covert.cell.sim.constant.Gene defines the identifier, name, type (m-, r-, s-, or t-RNA), location, length, and directionality of each gene.

## A.7.10 Logger

DatabaseLogger, DiskLogger, and SummaryLogger define three ways of storing simulated single cell dynam ics. DatabaseLogger provides methods to store and retrieve simulated data to/from a relational database. DiskLogger provides methods to store and retrieve simulated data directly to/from disk. SummaryLogger provides methods to store a small amount of key simulated data to/from disk. DatabaseLogger, DiskLogg er, and SummaryLogger derive from edu.stanford.covert.cell.sim.util.Logger. Logger defines the common interface which Simulation uses to initialize, append, and finalize each simulation log.

## A.7.11 KnowledgeBase

The primary function of edu.stanford.covert.cell.kb.KnowledgeBase is to represent the curated knowl edge base of M. genitalium physiology, and to provide this information to the states and processes. In this way, KnowledgeBase serves as an abstraction layer between the knowledge base relational database and the whole-cell MATLAB model. Specifically, the knowledge base represents several reconstructed properties of M. genitalium including the genomic sequence; the location, length, and direction and observed expression of half-life of each gene; the transcription unit organization of the chromosome; the subunit composition of each macromolecular complex; the chemical composition of M. genitalium and its typical external environment; and the stoichiometry, kinetics, energetics, and catalysis of each chemical reaction.

## A.7.12 KnowledgeBaseObject

edu.stanford.covert.cell.kb.KnowledgeBaseObject is the base class from which all MATLAB classes which represent objects contained the M. genitalium knowledge base are derived, including KnowledgeBase. See Section A.7.11 for further discussion of the role of the M. genitalium knowledge base.

## A.7.13 MoleculeCountState

edu.stanford.covert.cell.sim.MoleculeCountState is the superclass for all cell state classes which represent the copy numbers of individual molecules including the Metabolite, Rna, Protein Monomer, and Protein Complex classes. MoleculeCountState extends CellState by defining properties which represent the identifier, name, and molecular weight of each molecular species and the copy number of each species in each of the six compartments defined by Compartment.

## A.7.14 PaperFigures

The run method of edu.stanford.covert.cell.sim.analysis.PaperFigures produces Figure 2-6 presented in the accompanying manuscript.

## A.7.15 polymerize

edu.stanford.covert.cell.sim.util.polymerize implements a model of nutrient and energy allocation among nascent polymers. The Replication, Transcription, and Translation processes use polymerize to model the allocation of dNTPs, NTPs, and amino acids among active DNA polymerases, RNA polymerases, and ribosomes. See Section 3.18, 3.25, or 3.27 for further discussion of the mathematical model implemented by the polymerize function.

## A.7.16 Process

edu.stanford.covert.cell.sim.Process is the base class from which all process sub-model classes are derived. Process defines the public interface that each process exposes to Simulation. This interface enables Simulation to construct each sub-model using data from the knowledge base, evaluate each process’ contributions to the initialization and temporal evolution of the cell’s state, determine the parts of the cell state accessed and modified by each sub-model, and to calculate the life cycle and instantaneous metabolic demands of each process. ReactionProcess extends Process by adding several properties which represent the structure of the modeled biological network as well as one method which initializes the values of those properties using the knowledge base.

## A.7.17 RandStream

The MATLAB built in RandStream class provides four low-level methods – rand, randi, randn, and randperm for generating random numbers from a specific random stream. edu.stanford.covert.util.RandStream extends the functionality of the built in RandStream class by (1) providing methods to execute four statistics toolbox functions – multinomially-distributed random number generation (mnrnd), Poisson-distributed random number generation (poissrnd), a wrapper over several random number generation methods (random), and multinomially-distributed random number generation with and without replacement (randsample) – on a specific random stream, and (2) adding four methods randCounts, stochasticRound, randomlySelect-Rows, and randomlySelectNRows. randCounts returns the number of times each of N objects with counts $m _ { i }$ for $i = 1 . . N$ is selected without replacement. stochasticRound stochastically rounds elements of a matrix M . With probability $M _ { i j }$ mod 1 stochasticRound replaces $M _ { i j }$ with is ceiling, and otherwise replaces $M _ { i j }$ with its floor. randomlySelectRows randomly returns each row of a matrix with a specified probability. randomlySelectNRows randomly returns N rows of a matrix, each with equal probability.

## A.7.18 ReactionProcess

edu.stanford.covert.cell.sim.ReactionProcess is the base class from which several process classes representing large network models including Metabolism are derived. ReactionProcess extends Process by defining several properties which represent the structure of the modeled biological network and by providing one method which initializes the values of those properties using the knowledge base.

## A.7.19 SparseMat

edu.stanford.covert.util.SparseMat eficiently represents sparse multidimensional matrices. Externally, SparseMat behaves similarly to matrices created using the built in MATLAB sparse function with two exceptions: (1) SparseMat supports multidimensional matrices, whereas the built in sparse function supports only one- and two-dimensional matrices, and (2) SparseMat redefines linear indexing in reference and assignment operations as syntactic sugar for the composition of linear indexing with sub2ind. SparseMat supports many common matrix operations including addition, subtraction, multiplication, and division. Internally, SparseMat represents an N-dimensional matrix containing n non-zero elements as an $n \times ( N + 1 )$ two-dimensional matrix containing the indices and values of each non-zero element. CircularSparseMat extends SparseMat by enabling circular matrix reference and assignment. Several properties of the Chromosome class are implemented as instances of CircularSparseMat.

## A.7.20 Simulation

edu.stanford.covert.cell.sim.Simulation is the primary class users interact with to run and analyze whole-cell model simulations. The primary functions of Simulation are several-fold: (1) initializeConstants constructs the states and processes using data contained in the knowledge base, (2) initialize-State randomly initializes the cell state, (3) evolveState sequentially executes the process sub-models in a random order, (4) applyOptions, applyParameters, applyPerturbations override the default values of each option and parameter, for example to simulate gene disruption, (5) run executes a complete simulation by initializing the cell state, iteratively executing evolveState, and optionally triggering loggers to store the predicted single cell dynamics.

## A.7.21 SimulationEnsemble

edu.stanford.covert.cell.sim.util.SimulationEnsemble provides methods for retrieving simulated sin gle cell dynamics stored by DiskLogger and SummaryLogger for multiple cells. DiskLogger and Summary-Logger provide methods for retrieving the simulated dynamics of individual cells.

## A.7.22 SimulationDiskUtil

edu.stanford.covert.cell.sim.util.SimulationDiskUtil provides methods to retrieve and search simulation meta data generated by DiskLogger.

## A.7.23 SimulationStateSideEffect

edu.stanford.covert.cell.sim.SimulationStateSideEffect and edu.stanford.covert.cell.sim.SimulationStateSideEffectItem represent the side efects of one process on parts of the cell state outside the direct focus of that process. For example, when a sub-model binds one protein to the chromosome, displacing another protein from the chromosome modeled by a diferent cellular process, these classes represent the side efect of displacing that second protein on the DNA-bound copy number of that second protein redundantly represented by the Protein Monomer state. During the execution of each cellular process sub-model, cellular states use SimulationStateSideEffect to keep track of their side efects on other parts of the cell state primarily modeled by other sub-models. After the completion of the execution of each sub-model, the Simulation class processes the accumulated side efects and updates the afected states. The principal advantages of this approach are two-fold. First, this approach minimizes direct communication among the cellular states which reduces complexity and run time. Second, this approach outlines the side efects of processes on parts of the cell state outside their direct purview.

Each atomic, mass-balanced modification of a distant part of the cell’s state is represented by an instance of the SimulationStateSideEffect class of size 1 × 1 whose children of type SimulationStateSideEffect-Item represent the specific efect of the modification on the other parts of the cell state. For example, each event where a process displaces a foreign protein from the chromosome is represented by an instance of the SimulationStateSideEffect class which has two children each of type SimulationStateSideEffectItem, one of which represents the decrement of the DNA-bound copy number of the displaced protein and a second which represents the increment of the free copy number of the displaced protein.

## A.7.24 SimulationStateSideEffectItem

See Section A.7.23 for discussion of the SimulationStateSideEffectItem class.

## A.7.25 SummaryLogger

edu.stanford.covert.cell.sim.util.SummaryLogger provides methods to store a key subset of simulated single cell dynamics to disk. SummaryLogger implements the common logger interface defined by Logger. SimulationEnsemble provides methods to retrieve results logged by SummaryLogger.

## A.8 Third-Party Software

The M. genitalium whole-cell model and knowledge base were developed using the software libraries and applications listed below.

Knowledge Base

• BioWarehouse biowarehouse.ai.sri.com

• Excel ofice.microsoft.com/en-us/excel

• GeSHi qbnz.com/highlighter

• Marvin chemaxon.com/products/marvin

• MySQL mysql.com

• MySQL connector J mysql.com/products/connector

• Pear pear.php.net

• PHP php.net

• PHPExcel phpexcel.codeplex.com

Modeling

GLPKmex glpkmex.sourceforge.net

• MATLAB mathworks.com/products/matlab

• multiprod mathworks.com/matlabcentral/fileexchange/8773

Simulation

CentOS centos.org

• JSON Marshaller code.google.com/p/jsonmarshaller

• MATLAB Compiler mathworks.com/products/compiler

• Maui clusterresources.com/products/maui

Torque adaptivecomputing.com/products/torque.php

• Perl perl.org

• Rocks www.rocksclusters.org

## Analysis & Visualization

• Apache apache.org

• boundedline mathworks.com/matlabcentral/fileexchange/27485

• Bullseye mathworks.com/matlabcentral/fileexchange/16458

• DHTML Window dynamicdrive.com/dynamicindex8

• fmpeg fmpeg.org

• flowplayer flowplayer.org

• Funct\_Bezier mathworks.com/matlabcentral/fileexchange/6661

• Illustrator www.adobe.com/products/illustrator.html

• Inkscape inkscape.org

• LAT X www.latex-project.org

• jqGrid trirand.com/blog

• pdftk pdflabs.com/tools/pdftk-the-pdf-toolkit

• PHP php.net

• propertygrid mathworks.com/matlabcentral/fileexchange/28732

• rude mathworks.com/matlabcentral/fileexchange/6436   
• Silk • Silk

famfamfam.com/lab/icons/silk

• spanFigure mathworks.com/matlabcentral/fileexchange/31604

• swtest mathworks.com/matlabcentral/fileexchange/13964

• tick2text mathworks.com/matlabcentral/fileexchange/16003

• Uniform uniformjs.com

• uitabpanel mathworks.com/matlabcentral/fileexchange/11546

## Interactive Visualization

• alivepdf alivepdf.bytearray.org

• amfphp silexlabs.org/amfphp

• as3gif code.google.com/p/as3gif

• AS3FlexDB code.google.com/p/as3flexdb

• degrafa degrafa.org

• Flash adobe.com/products/flashplayer.html

• Flex adobe.com/products/flex.html

• flexlib code.google.com/p/flexlib

• Flex Menu Accelerators rphelan.com/2008/03/17/flex-menu-accelerators

• Flex Multiline Button forestandthetrees.com/flex-multiline-button

• MS Visual C# microsoft.com/visualstudio

• Premier adobe.com/products/premiere.html

• print-as3 code.google.com/p/printf-as3

• Screen2Video viscomsoft.com/products/screen2video

Tooltip Speech Bubbleblog.flexmp.com/2008/09/10

• tweener code.google.com/p/tweener

## Testing & Development

• absolutepath mathworks.com/matlabcentral/fileexchange/3857

• Doxygen www.stack.nl/ dimitri/doxygen

• Hudson hudson-ci.org

• MATLAB xUnit framework mathworks.com/matlabcentral/fileexchange/22846

• m2cpp mathworks.com/matlabcentral/fileexchange/25925

• m2html artefact.tk/software/matlab/m2html

• Subversion subversion.apache.org

## Appendix B

## List of Abbreviations

<table><tr><td>API</td><td>Application programming interface</td><td>ODE</td><td>Ordinary differential equation</td></tr><tr><td>BER</td><td>Base excision repair</td><td>R/M</td><td>Restriction/modification</td></tr><tr><td>DDR</td><td>Direct damage reversal</td><td>rRNA</td><td>Ribosomal RNA</td></tr><tr><td>DSBR FBA</td><td>Double-strand break repair</td><td>SMC</td><td>Structural maintenance of</td></tr><tr><td>GAM</td><td>Flux-balance analysis Growth-associated maintenance</td><td></td><td>chromosome protein</td></tr><tr><td></td><td>energy</td><td>SP-4</td><td>Spiroplasma medium #4</td></tr><tr><td>GG</td><td>Global genomic</td><td>sRNA</td><td>Small non-coding RNA</td></tr><tr><td>HR</td><td>Homologous recombination</td><td>SRP</td><td>signal recognition particle</td></tr><tr><td>MOMA</td><td>Minimization of metabolic adjustment</td><td>SSB</td><td>Single-stranded binding protein</td></tr><tr><td>mRNA NER</td><td>Messenger RNA</td><td>TLR</td><td>Toll-like receptor</td></tr><tr><td>NF-κB</td><td>Nucleotide excision repair</td><td>tRNA</td><td>Transfer RNA</td></tr><tr><td></td><td>Nuclear factor</td><td>TSS</td><td>Transcription start site</td></tr><tr><td></td><td>kappa-light-chain-enhancer of activated B cells</td><td>UV</td><td>Ultraviolet</td></tr></table>