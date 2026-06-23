# Bringing the genetically minimal cell to life on a computer in 4D

Graphical abstract

![](images/ff73616f468edd02bb425e04c31ed667deeea48dc646ec35561a954a9b5a1b3a.jpg)

## Authors

Zane R. Thornburg, Andrew Maytin, Jiwoong Kwon, ..., Angad P. Mehta, Taekjip Ha, Zaida Luthey-Schulten

## Correspondence

zan@illinois.edu

## In brief

Simulating the complete cell cycle of the minimal cell provides a platform to understand the progression of complete states over time. The spatial heterogeneity of the intracellular environment can strongly affect biochemical reactions that control phenotypes.

## Highlights

• Presents a whole-cell spatial and kinetic model for the entire cell cycle

• Simulations include genetic information processes, metabolism, growth, and cell division

• Whole-cell modeling predicts many cellular properties simultaneously

• Assimilation of a wide array of experiments is necessary for construction and validation

Article

# Bringing the genetically minimal cell to life on a computer in 4D

Zane R. Thornburg,<sup>1,2,3,16</sup> Andrew Maytin,<sup>4,5,16</sup> Jiwoong Kwon,<sup>6,7,8</sup> Troy A. Brier,<sup>3</sup> Benjamin R. Gilbert,<sup>3</sup> Enguang Fu,<sup>3,4</sup> Yang-Le Gao,<sup>3</sup> Jordan Quenneville,<sup>3</sup> Tianyu Wu,<sup>4,9</sup> Henry Li,<sup>4</sup> Talia Long,<sup>3</sup> Weria Pezeshkian,<sup>10</sup> Lijie Sun,<sup>11</sup> Daniela Matias de C. Bittencourt,<sup>11</sup> John I. Glass,<sup>11</sup> Angad P. Mehta,<sup>3,4,12,13,14</sup> Taekjip Ha,<sup>6,7,8,15</sup> and Zaida Luthey-Schulten<sup>1,3,4,5,12,17,</sup>\*

<sup>1</sup>Beckman Institute for Advanced Science and Technology, University of Illinois at Urbana-Champaign, Urbana, IL, USA   
<sup>2</sup>Cancer Center at Illinois, University of Illinois at Urbana-Champaign, Urbana, IL, USA   
<sup>3</sup>Department of Chemistry, University of Illinois at Urbana-Champaign, Urbana, IL, USA   
<sup>4</sup>NSF Science and Technology Center for Quantitative Cell Biology, Urbana, IL, USA   
<sup>5</sup>Department of Physics, University of Illinois at Urbana-Champaign, Urbana, IL, USA   
<sup>6</sup>Department of Biophysics and Biophysical Chemistry, Johns Hopkins University School of Medicine, Baltimore, MD, USA   
<sup>7</sup>Program in Cellular and Molecular Medicine, Boston Children’s Hospital, Boston, MA, USA   
<sup>8</sup>Department of Pediatrics, Harvard Medical School, Boston, MA, USA   
<sup>9</sup>Center for Biophysics and Quantitative Biology, University of Illinois at Urbana-Champaign, Urbana, IL, USA   
<sup>10</sup>Niels Bohr International Academy, Niels Bohr Institute, University of Copenhagen, Blegdamsvej 17, 2100 Copenhagen, Denmark   
<sup>11</sup>J. Craig Venter Institute, La Jolla, CA, USA   
<sup>12</sup>Carl R. Woese Institute for Genomic Biology, University of Illinois at Urbana-Champaign, Urbana, IL, USA   
<sup>13</sup>Department of Biochemistry, University of Illinois at Urbana-Champaign, Urbana, IL, USA   
<sup>14</sup>Department of Bioengineering, University of Illinois at Urbana-Champaign, Urbana, IL, USA   
<sup>15</sup>Howard Hughes Medical Institute, Boston, MA, USA   
<sup>16</sup>These authors contributed equally   
<sup>17</sup>Lead contact   
\*Correspondence: zan@illinois.edu   
https://doi.org/10.1016/j.cell.2026.02.009

## SUMMARY

We present a whole-cell spatial and kinetic model for the ∼100 min cell cycle of the genetically minimal bacterium JCVI-syn3A. We simulate the complete cell cycle in 4D (space and time), including all genetic information processes, metabolic networks, growth, and cell division. By integrating hybrid computational methods, we model the dynamics of morphological transformations. Growth is driven by insertion of lipids and membrane proteins and constrained by fluorescence imaging data. Chromosome replication and segregation are controlled by the essential structural maintenance of chromosome proteins, analogous to condensin (SMC) and topoisomerase proteins in Brownian dynamics simulations, with replication rates responding to deoxyribonucleotide triphosphate (dNTP) pools from metabolism. The model captures the origin-to-terminus ratio measured in our DNA sequencing and recovers other experimental measurements, such as doubling time, mRNA half-lives, protein distributions, and ribosome counts. Because of stochasticity, each replicate cell is unique. We predict not only the average behavior of partitioning to daughter cells but also the heterogeneity among them.

## INTRODUCTION

To develop a full understanding of the rules governing cellular life, we must know the complete quantitative characteristics of cells as a function of time and space (4D) and how the underlying chemical and physical processes act in unison to drive changes in cell state. Determining the molecular composition and architecture of an entire cell simultaneously is not currently possible with any single experiment, but there have been significant strides in computational modeling of cell states, as well as emerging efforts to concatenate the growing number of large biological datasets to form snapshots of cell states using machine learning (ML) and artificial intelligence (AI).<sup>5</sup> Assimilation of quantitative biological data in this manner is a promising avenue to predict the complete molecular context of a cell at varying time points in the cell’s life cycle. However, predicting snapshots of a cell state using ML or AI methods, both in molecular composition and physical characteristics, is a product of sampling possible outcomes and will not tell us about the underlying biological, chemical, and physical processes that caused the temporal progression of the cell’s state.

Modeling has several levels of resolution that can be employed, depending on the spatial and temporal characteristics of the biological processes that are being targeted. At the finest level of resolution, a near-atomic structure of a minimal bacterium (JCVI-syn3A) has been modeled using the coarse-grained Martini force field.<sup>6,7</sup> Structural models of Mycoplasma genitalium and JCVI-syn3A have also been created.<sup>8,9</sup> Although these models achieve atomic resolutions of (nearly) complete cell states, they are either static or can only be simulated for short times (≪1 s). Atomic-resolution models are great for capturing structure and high-resolution, short-timescale interactions, but they are not capable of simulating the mechanics and chemistry that take place over minutes to hours in processes such as gene expression and cell division.

At the other end of the complexity scale, whole-cell reaction networks have been treated using steady-state flux and kinetic models. Flux balance analysis (FBA) methods have been applied to many cells, from simple bacteria to eukaryotes such as yeast and human cells, to predict fluxes through metabolic reactions.<sup>10,11</sup> FBA has proven to be a useful tool for predicting average behavior and even making claims about gene essentiality, but it lacks dynamics and cell-to-cell heterogeneity. There have been a few whole-cell kinetic models to date, including Mycoplasma genitalium<sup>3</sup> and Escherichia coli,<sup>4,1</sup> <sup>2</sup> as well as our own model of a minimal bacterium.<sup>1</sup> Although the kinetic models include reaction dynamics to dictate temporal progression of the cell state, they treat cells or cell compartments primarily as well-stirred systems lacking heterogeneous spatial organization. These well-stirred models have proven themselves as predictive tools, but they cannot probe the dependence of stochastic processes on the spatial localization of molecular participants (e.g., RNA polymerase [RNAP] must diffuse and bind to promoters on the DNA). 13–15

Building a fully physics-based model of an entire cell to explore the dynamics of a complete cell cycle in a holistic manner is both highly appealing and crucial in the quest to understand the foundations of life through a bottom-up approach. In this context, an organism consisting of the fewest components and processes would provide an excellent platform. JCVI-syn3A is a genetically minimal bacterium with a synthetic genome that has been genetically reduced from Mycoplasma mycoides subsp. capri str. GM12.<sup>16,17</sup> Syn3A has a doubling time of 105 min and a single 543 kbp circular chromosome consisting of 493 genes.<sup>18</sup> Although a previous iteration, JCVI-syn3.0, had fewer genes, Syn3A reintroduced genes that allow the cell to divide and maintain regular spherical morphologies.<sup>17–19</sup> Syn3A’s minimal genome and annotated gene essentialities,<sup>17–19</sup> proteomics, transcriptomic and DNA sequencing data, essential metabolic map,<sup>18</sup> cryo-electron tomograms (cryo-ET),<sup>21,22</sup> chromosome contact maps,<sup>21</sup> predicted structural proteome, 23 and now imaging of the symmetric division and additional DNA sequencing make it a strong candidate for whole-cell modeling over its entire cell cycle.

Previously we simulated the cell cycle of Syn3A as a wellstirred system using hybrid stochastic-deterministic kinetics.<sup>1</sup> Several parameters in the well-stirred model were obtained from simplified 4D simulations of the first 20 min of the cell cycle, assuming static morphology and ribosome positions from cryo-ET before any DNA replication had occurred. The spatially resolved model is more computationally expensive, but even short 4D simulations can provide predictions of probabilistic factors such as the average number of active ribosomes, RNAPs, and degradosomes, as well as the distribution of mRNA halflives. From well-stirred simulations, behaviors emerged that reflected experimental measurements of Syn3A and related bacteria.

To fully understand and characterize the spatial dynamics that dictate life for Syn3A, we need to simulate the entire cell cycle, including DNA replication and dynamics, ribosome movement, and division in 4D. Here, we present a 4D whole-cell model (4DWCM) that simulates the entire cell cycle of Syn3A, including expression of all 493 genes, kinetics of the entire metabolic network, ribosome biogenesis, chromosome dynamics (including DNA replication), and morphological changes during growth and division. We again hybridize multiple simulation techniques into one model to accurately represent the broad range of lengths, concentrations, and rates that define the cell state and cell cycle progression. Although the well-stirred components for metabolism remain mostly unchanged from our previous model,<sup>1</sup> making the spatial components of genetic information processes and cell morphology dynamic posed significant challenges. Methods were developed to communicate a coarsegrained continuum model of the DNA to our simulation software Lattice Microbes (LMs<sup>24</sup>), update morphology based on the incorporation of membrane components, allow ribosomes to assemble and diffuse on lattice sizes smaller than their diameter, and other procedures that stem from these major additions. The DNA replication dynamics accompanied by informed kinetic parameters<sup>25,26</sup> from recent SMC loop extrusion experiments are in agreement with the DNA sequencing data provided here. Constraints from our fluorescence imaging experiments characterizing cell morphology, DNA localization, and formation of the septum support the symmetric cell division of Syn3A. By creating a model that imposes spatial heterogeneity and its inherent stochasticity on reactions such as DNA replication initiation, transcription, translation, and mRNA degradation, we uncover the dependence, sensitivity, and variations of cell cycle progression on key rates in the 4D dynamics. Overall, we analyzed the cell cycle dynamics of 50 unique replicate cells. This 4DWCM presents a leap forward in our ability to more accurately probe the fundamental behaviors of cellular life.

## RESULTS

The breadth of data provided by the 4DWCM is challenging to represent visually. To summarize a few highlights of the spatial heterogeneity of our simulated cell states, we show 3D visualizations in Figure 1 of a representative cell through its cell cycle, and the full trajectory is shown in Video S1. The reaction-diffusion master equation (RDME) component of the simulations requires that the 3D space be discretized into a cubic lattice, in this case with edge lengths of 10 nm. Chromosomes are represented as circular homopolymers consisting of 10 bp monomers. As lipids and membrane proteins are incorporated into the membrane, we update the morphology on the lattice throughout growth and division. Figure 1A shows the progression of DNA replication, growth, and division over the course of a cell cycle. Figures 1B–1G show various components of a cell state, all from the same frame of time for a single-cell simulation during division. All proteins and RNA are treated as individual particles, as shown in Figure 1C. Chromosome dynamics are communicated to LM by imposing the LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) DNA monomers onto the lattice to define an excluded volume that reduces diffusion of lattice particles through and around the DNA (Figure 1D). Reactive particles representing the monomers, corresponding to transcription start sites (assumed to be the first nucleotide in the respective gene’s coding sequence), are placed onto the LM lattice. The boundary for the chromosomes in LAMMPS is smaller than the membrane boundary in LM to prevent the DNA from overlapping the membrane (Figures 1D and 1E). We define lattice site types with specific reaction and diffusion rules to differentiate the peripheral membrane sites from the membrane and cytoplasm, as shown in Figure 1F. Degradosome particles are restricted to the peripheral membrane sites, and we show the sugar transporter PtsG as a representative membrane protein. Ribosomes have a hybrid treatment, where their centers of mass are treated as particles, and their excluded volumes are treated as crosses, both on the RDME lattice, as shown in Figures 1B and 1G, respectively (also see Figure S1).

![](images/d79884bb1a5047a4e6696258cfaa832a3ddd18929218b42b1ac4db47c8bb5978.jpg)

Figure 1. Visualization of 3D components of the 4DWCM

(A) Cell cycle progress from initial conditions to 2 h of biological time, showing lattice membrane (green 10 nm cubes), ribosomes (yellow: inactive, purple: active), and DNA (10 bp beads, blue and red differentiate daughter chromosomes).

(B) Zoomed-in view of the representation in (A). (C) The cytoplasm is dense with proteins (gray particles) and RNA (orange particles).

(D) The DNA is projected onto the lattice (white cubes), and the promoter particles (red particles: promoters, green particles: RNAP bound) are placed according to their position from LAMMPS. (E) The membrane boundary in LAMMPS (dark gray spheres) must be smaller than the lattice membrane to prevent DNA-membrane overlap on the lattice.

(F) PtsG sugar transporters (brown particles) are restricted to the membrane and are not allowed to diffuse back into the peripheral membrane (blue cubes) or cytoplasm (cyan cubes) regions. Degradosomes (pink particles) are restricted to the peripheral membrane.

(G) Excluded volume of ribosomes is maintained by projecting their volume onto lattice cubes (red cubes, center of mass; yellow cubes, excluded volume).

(B)–(G) are all from the 85 min time point of the same simulation. Generated using VMD.<sup>27</sup> See also Figure S1.

## Construction of the 4DWCM

Constructing a 4DWCM to simulate an entire cell cycle of Syn3A requires hybridization of computational methods at multiple levels of resolution. We have summarized the algorithm that communicates biological information between computational methods and a break-

down of the computational expenses with a flowchart shown in Figure 2. Gene expression reactions are handled stochastically through spatially localized reactions in the RDME and well-stirred reactions in the chemical master equation (CME), as implemented in LM,<sup>1,28</sup> and metabolism is simulated as a system of ordinary differential equations (ODEs); the details of reactions and their kinetics are all discussed in STAR Methods. To make the chromosome(s) dynamic required the addition of yet another method: Brownian dynamics (BD) simulated on a separate GPU using LAMMPS.<sup>7,29</sup> Morphological updates during growth and division are determined by the scavenging of lipids from the environment, synthesis of other lipids from metabolism, and the translocation of membrane proteins. Each membrane component is assigned a surface area contribution, resulting in the total cell surface area growing as a function of time. For completeness, the initial counts/concentrations obtained from -omics data, a table of the kinetic parameters, and a thermodynamic analysis of the kinetic parameters are provided in Tables S1 and S2, and the few parameter changes are discussed in STAR Methods.

![](images/268eeb783864f4221bdb1f8d8978ce2a8baa00d25b15502b5767582de25ee8c4.jpg)

![](images/e10258253206bceeb8e3177b3b38107b44c927b48e31bdbade29622cdb806dab.jpg)  
Figure 2. Flowchart of the hybrid simulation algorithm for the 4DWCM  
The parent method is the reaction-diffusion master equation (RDME) solver implemented in LM. Time steps are 50 μs. The hybrid algorithm interrupts the RDME solver at an interval of 12.5 biological ms. The primary methods communicated are well-stirred stochastic kinetics through a global (cell-wide) chemical master equation (CME) simulation, ordinary differential equations (ODEs) for metabolism, and Brownian dynamics (BD; integrated with LAMMPS) for the chromosomes. The average computational expense of each component is summarized in the bar chart.

Dynamics, replication, and partitioning of chromosomes To simulate the chromosome configuration, we use a polymer model based on our previous chromosome dynamics simulations.<sup>7</sup> In our simulations we incorporate the physical effects of two classes of proteins: topoisomerases and SMC (structural maintenance of chromosome proteins, analogous to condensin). Although the actions of SMC looping and topoisomerases are sufficient to disentangle daughter chromosomes from one another, partitioning into daughter cells required the introduction of a repulsive force of approximately 12 pN between daughter chromosomes to accelerate their movement during cell division (Figure 3A). DNA replication (Figure 3B) is implemented with the ‘‘train-track’’ model.<sup>30</sup> Before DNA is replicated, the process is initiated by the essential protein DnaA. To simulate the DNA’s polymer behavior, we employ an elastic worm-like chain model (Figure 3C) using the potential energy functions from Brackley et al.<sup>31</sup> We also incorporate excluded volume interactions between strands of DNA (Figure 3D) and between DNA and boundary particles (Figure 3E). SMC complexes form and extrude loops of DNA, causing structural changes on the size of hundreds to thousands of base pairs per loop.<sup>32</sup> As shown in Figure 3F, we mimic the effect of SMC by anchoring the loop to one bead on our homopolymer and updating the ‘‘hinge’’ position of the loop to progressively extrude DNA. We update anchor positions once and hinge positions 10 times every 4 s of biological time. The rate of hinge position movement is based on experimental measurements,<sup>26</sup> but it is unclear how frequently we should update anchor positions when we assume the dimers only bind to the chromosome non-specifically in Syn3A.<sup>7,21</sup> Topoisomerases transiently cut DNA to allow double-strand pas-

![](images/20d6b51dc0a8f6b5e4913cdafb307e8d0d88d9f618099300f757650cf06deaa2.jpg)

Figure 3. Coarse-grained modeling of the minimal cell chromosome

(A) Snapshots of the cell at approximately 45 and 90 min into the cell cycle. A 12 pN force is applied to each daughter chromosome in opposite directions to facilitate partitioning. A window cutout highlights the replication forks and terminus.

(B) DNA replication follows the train-track model.   
The window cutout from (A) is magnified.

(C) Bending interactions (red dashed line) impose local curvature with a persistence length of 45 nm; stretching (blue dashed line) is governed by a finite extensible nonlinear elastic (FENE) potential. DNA is coarse-grained at 10 bp resolution, with a bead diameter of 3.4 nm.

(D) Excluded volume interactions between DNA strands include a ‘‘hard’’ repulsion to prevent strand crossing and a soft ‘‘topo’’ repulsion that allows it; an example where strand crossing can be seen visually is magnified.

(E) Excluded volume interactions between DNA and the boundary (red dashed line) are set to be a hard-core repulsion.

(F) SMC-driven loop extrusion is modeled by introducing a harmonic bond between each anchor and hinge, with the hinge translocating in steps of ∼20 beads simulating the reeling motion of the SMC complex. Anchors are updated (randomly placed) every 4 s; hinges are updated (translocated) every 0.4 s.

sage and then re-ligate the DNA. We incorporate the effects of topoisomerases by periodically switching the potential from the hard-excluded volume potential to a soft potential that allows DNA monomers to pass through one another, as shown in Figure 3D. Without

an effect to resolve strand crossings, we found previously<sup>7</sup> and here that our simulations would never be able to disentangle and partition chromosomes between two daughter cells.

## 4D whole-cell modeling reflects experiment

In bacterial cells, the timing of the cell cycle is typically characterized by three periods for cells with a single DNA replication event: B—the time between birth and replication initiation, C—the time to replicate the DNA, and D—the time to divide the cell after the end of replication.<sup>33</sup> We predict two key timings, shown in Figure 4A: doubling the membrane in 105 min and the chromosome in 51 min on average. The predicted doubling time is in very close agreement with the experimental doubling time of 105 min.<sup>18</sup> We made a similar prediction in our previous wellstirred model, but the predicted doubling time was 97 min.<sup>1</sup> The slow-down in predicted doubling time comes from an underproduction of proteins (discussed below), resulting in slower surface area growth from incorporation of fewer membrane proteins.

Through fluorescence imaging of JCVI-syn3B, a variant of Syn3A with a ‘‘landing pad’’ system to mediate genetic modification,<sup>34</sup> we observe that the minimal cell undergoes roughly

A  
![](images/c4e405e4a2af554c2910b2ab4a9bce16576344b800772871af2324f0d29684f2.jpg)

B  
![](images/01372ea4aba93acdab263be66a9be728f621292002ee96da377eb1ccdcc69704.jpg)

C  
![](images/84b686b796427eb287187ad52ca6c53f3ad5117612d7bee40e2ca784e3524020.jpg)

![](images/52a987a7cfb2a3677d28c7b6504e44ffcbc729b23bef184347507a2b90562a98.jpg)  
symmetric division. Dividing cell shapes most frequently exhibit prolate (early cell division state) and dumbbell-like (late cell division state) morphologies. A few representative cells at different stages of the cell cycle are shown in Figure 4C. The gene encoding labeled FtsZ was introduced as an additional copy rather than a substitute for the original, to minimize disruption of the division machinery. FtsZ is a cytoplasmic protein that polymerizes at the division plane during cell division. The distribution of morphologies for 1,319 analyzed cells (Figure S2) is shown in Figure 4D. Spherical cells appear larger than previous cryo-ET,<sup>21</sup> but this discrepancy is consistent with observations for similar organisms, where cell sizes can vary by hundreds of nanometers depending on the imaging method and sample preparation.<sup>35</sup> The fraction of prolate and dividing cells observed in the imaging data is lower than expected based on our simulated cell cycle in which division begins approximately 60 min into a 105 min cycle, which corresponds to roughly 40% of cells dividing for asynchronous cell cycles. A full-field-of-view z stack movie with overlays around all segmented cells is visualized in Video S2. The discrepancy in the percentage of dividing cell shapes (including prolate morphologies) depends on our qualitative definition for prolate assignment (see STAR Methods and Figure S2), and a more lax constraint predicts up to 30% of cells in prolate states.  
Figure 4. The 4DWCM accurately mimics experiments

We also observed cells with ‘‘budding’’ morphologies and ‘‘cell-in-cell’’ intracellular membrane structures. Budding structures do not indicate that division of Syn3A occurs through budding, as an extracellular membrane structure that contained ribosomes but no DNA was previously annotated in cryo-ET of Syn3A.<sup>21</sup> In late-exponential phase Syn3A, roughly 15% of analyzed cells contained cell-in-cell structures (statistics shown in Figure S2). The causes of these budding and cell-in-cell structures are not known, but irregular morphologies, including cell-(A) Timing of DNA, volume, and surface area doubling in simulated cell cycles. Vertical lines represent average times among the population. The combined DNA and surface area doubling times predict an ori:ter ratio of 1.28. Shaded regions represent the full range of the simulated population, except for the DNA. The DNA shaded region excludes the cell with a replication initiation time of 46 min.

(B) Experimental DNA sequencing of Syn3A in late exponential growth phase shows that Syn3A has an ori:ter ratio of 1.21. Each trace represents a technical replicate (n = 3 replicates). The dip at 22 kbp is likely due to natural evolution, resulting in deletion of the tetM gene.

(C) Fluorescence imaging of JCVI-syn3B with a second copy of FtsZ labeled with mCherry (red), DNA stained with Hoechst 33342 (blue), and the membrane stained with FM1-43FX (green).

(D) Pie chart showing fraction of the inspected total (n = 1,319 cells) that were annotated as prolate, dividing, and budding.   
See also Figure S2.

in-cell structures, have been observed in other imaging of Syn3A.<sup>19,22</sup>

We combine the new fluorescence imaging and previous cryo-ET observations<sup>21</sup> into two constraints on the morphology during our simulations, such that the cell (1) grows spherically from 200 to 250 nm in radius (∼98% increase in cell volume), given our coarse-grained resolution of 10 nm lattice cubes, and then (2) maintains a constant volume as the surface area grows during symmetric division until the end of the cell cycle. The dividing cell morphologies shown in Figure 1 are generated using a geometric approach where we treat the shape as two overlapping spheres that have the total instantaneous surface area and volume of the dividing cell. Although this does not include the kinetics and mechanics of FtsZ polymerization, the rate of change for the morphology is a direct result of the chemical reactions synthesizing the membrane components. As shown in Figure S3, we tested a physics-based approach to generate dividing cell shapes using a discretized version of the Helfrich Hamiltonian implemented in the software FreeDTS.<sup>36</sup> This method generates membrane shapes by minimizing constraints on the curvature and surface area-to-volume ratio obtained from our kinetic model. In the absence of a kinetic model of FtsZ polymerization to constrict the membrane at the division plane, the resulting morphologies obtained from FreeDTS are more elongated than the shapes observed in the fluorescence imaging. Because we use a geometric model for division, we also cannot predict the cell-in-cell morphologies observed in imaging. However, the methods used by FreeDTS have been shown to predict cell-in-cell morphologies,<sup>37</sup> so future integration of morphologies predicted by FreeDTS has the possibility of predicting both regular and irregular cell division.

In our simulations, the predicted DNA replication and membrane doubling times correspond to an average B period of

![](images/6a21960638ea8a6e7fced8a9d4a57b2e5ab7e8ef86ef11ee55f890afa5035ab0.jpg)

![](images/88d92d1e64a6cd95124c39d17032b162f3ba3be2ee98ae1f8ae5746e3c796998.jpg)

![](images/1c8178c5bbb1b950b2ba68351feb096ba3622877d782ea84645a93d811686738.jpg)

D  
![](images/3917d266ad8d51c77dda3044c8cf5bd4d14e90f6d423365a8bfbdef72d9f1947.jpg)

![](images/502966016bedb57bfee0f35a17caeb80b7bad05f43da9467874fdf828c0d9126.jpg)

F  
![](images/1455f100e32851822e91b0560b6b2a455b67cdb39b86ea3ff72101a594dd6e81.jpg)

![](images/b8e0823362fa4d05f1329c2e6ba01524747a201cc47587e6208ffd82406b2fa4.jpg)

H  
![](images/4d570ae09d6e1076bd45dcfe496090d4cfe12088f8ebdd8ba8e4ecf1aceab49a.jpg)

![](images/7111bff27ac573ec2bf0341e8d1aa2e3aa3a2590a57d91f452c7c400517dab07.jpg)

J  
![](images/af8f287f68a93cfb3fbf08d78639f834e6eecef4b98fdfc69fb5d9105901a9fe.jpg)

![](images/dfacf9d04d6a4de1300ee6d1e8046a500aa9b2298466e307571274c23b128bfc.jpg)

L  
![](images/f561069b44799dad24b473e11c7e1e7dcd3bd222761952d4fbbe3b64c99196a6.jpg)  
Figure 5. Dynamics of gene expression and macromolecular assembly

(A–C) Cells have averages of 881 ribosomes (A), 176 RNAP (B), and 192 degradosomes (C) at the average predicted division time (105 min, vertical lines). (D) After a cell cycle, there are averages of roughly 100 incomplete large and small ribosomal subunits waiting for ribosomal proteins to be translated. (E) On average, roughly 55% of ribosomes are actively translating, 70% of RNAP are actively transcribing, and 10% of degradosomes are actively degrading at any one time.

(F) Scaled protein count (counts at 105 min divided by initial condition) shows the model comes slightly short of doubling the counts of proteins in a cell cycle.   
(G) Average number of proteins made per mRNA for all 452 genes.

(H) Distribution of mRNA half-lives.

(I) Once a gene is duplicated through DNA replication, we measure the difference in the number of transcription events between genes (transcription events gene copy 1 − gene copy 2). A positive value means the original gene copy is transcribed more frequently after replication, and a negative value corresponds to more transcription on the daughter.

roughly 5 min (ori:ter 1:1), C period 46 min (2:1), and D period 54 min (2:2). By uniformly sampling time points throughout the average simulated cell cycle, our simulations exhibit an ori:ter ratio of 1.28. In whole-genome sequencing (WGS), we calculate an average ori:ter ratio of 1.21 for both late- and mid-exponential phase cells and 1.0 for stationary phase cells (Figures 4B and S2). The consistency between predicted and experimental ori:ter ratios supports the assumption that Syn3A typically only initiates replication once per cell cycle. This agreement also suggests that our model recovers not only a realistic doubling time but also realistic B, C, and D periods and, consequently, a realistic DNA replication elongation rate. The model uses a DNA replication elongation rate of 100 bp/s, as measured in Mycoplasma capricolum,<sup>38</sup> and if we had used the 600 bp/s rate from E. coli,<sup>39</sup> the cells would instead have an estimated ori:ter ratio of 1.05. As additional validation for the ori:ter ratio of 1.21, we analyzed DNA sequencing coverage data from a recent study that tracked the evolution of Syn3A over ∼400 generations and found values ranging from 1.0 to 1.2.<sup>20</sup>

Additionally, our sequencing data revealed a significant drop in coverage at the tetM locus. tetM encodes the tetracycline resistance protein TetM, which was not needed in our growth conditions because tetracycline was absent from the medium. A similar observation was made in the evolutionary study mentioned above, where mutations frequently arose in tetM.<sup>20</sup> The authors suggested that the strong tetM promoter, 20 combined with the absence of tetracycline, made tetM expression energetically costly,<sup>40</sup> leading to frequent mutations that downregulated or disrupted it. Although our data show a notable reduction in coverage rather than a complete deletion, this finding aligns with the idea that tetM is nonessential under these conditions.

## Formation of macromolecular complexes

A significant limitation of the previous simplified and early cell cycle 4D simulations was that the number of ribosomes, RNAP, and degradosomes was constant, and ribosomes and degradosomes did not diffuse.<sup>1</sup> The assembly reactions and diffusion rules for these complexes are now simulated and are described in the STAR Methods. The total counts of ribosomes, RNAP, and degradosomes over the course of a cell cycle are shown in Figures 5A–5C. The counts of RNAP and degradosomes rapidly increase from 0 to 93 and 120, respectively, because we initialize their components unassembled, and they rapidly assemble in the first second of biological time. On average, the components are synthesized and assembled at rates such that the numbers of complexes come slightly short of doubling in an average cell cycle. This is due to the slight underproduction of proteins by our model, which is discussed in more detail below. We track each state of assembly for the complexes, so we can count the number of ribosomes that sit in incomplete states, as shown in Figure 5. We find that on average, there are roughly 100 small subunit (SSU) and large subunit (LSU) complexes or intermediates that are waiting on ribosomal proteins to be synthesized to finish assembly, as shown in Figure 5D.

## Activity of gene expression complexes and competition for mRNA

The activity of gene expression complexes (RNAP, ribosomes, and degradosomes) is a quantity that is strongly tied to growth rate. 4 For the conditions and parameters in our model, we predict that, on average, roughly 55% of ribosomes, 70% of RNAP, and 10% of degradosomes are active at any one time throughout the cell cycle, as shown in Figure 5E. The active fraction of degradosomes is lower than we previously predicted,<sup>1</sup> but there is currently no available experimental comparison. The effects reducing the degradosome active fraction will be described in more detail below. The RNAP fraction is significantly higher than previously predicted. The higher active RNAP fraction is because our model now uses more informed assembly and stoichiometry to assemble RNAP complexes, which reduced the total count of complexes from 187 to 93, based on proteomics of the alpha subunit. Additionally, we found that the overall cell state and protein production are sensitive to the binding rate of the RNAP to promoters. This was already known, because scaling the promoter strengths by an order of magnitude or less has been shown to affect the overall protein production in our previous models.<sup>1,42</sup> The rate of RNAP binding to promoters presents itself as a global variable that is sensitive in the spatially heterogeneous reactions. We do not treat co-transcription of polycistronic operons in these simulations; each gene is transcribed independently. However, we allow multiple RNAP to read the genes coding for rRNA, up to 7 per 23S gene and 3 per 16S gene, based on an RNAP spacing of 400 bp (a conservative estimate from transcription measurements in E. coli<sup>41,43</sup>). This spacing acts as an upper bound on the total number of RNAP that can simultaneously transcribe the same gene. In our simulations, we observe average occupations of 1.5 ± 1 per gene copy out of 7 and 1 ± 1 out of 3. Although this shows that the rRNA genes experience near-constant transcription on average, 4 the cells still slightly underproduce ribosomes (discussed below).

The active fraction of ribosomes has been estimated to be as high as 85% in E. coli,<sup>41</sup> greater than our prediction here of 55%. In giving the ribosomes the ability to diffuse in these simulations, we had to sacrifice a critical effect in the overall translation dynamics: polysomes. The fraction of ribosomes involved in polysomes has been measured or experimentally estimated in several bacteria, including 20%–40% in Syn3A,<sup>21</sup> 26.2% in Mycoplasma pneumoniae,<sup>44,45</sup> and up to 70% in E. coli.<sup>46</sup> Given the fractions of ribosomes in polysomes observed in experiments, our predicted fraction of active ribosomes is not unreasonable in the absence of polysomes.

One of our key metrics in evaluating the accuracy of our models has been the ability to double the counts of proteins over the course of a cell cycle.<sup>1,42</sup> We again show this metric here in Figure 5F, and the average number of every protein in the simulation is provided in Table S3. Our distribution is not as narrow as it was in the well-stirred model, now exhibiting a tail out to almost 6 times the proteomics counts for some proteins. This tail is composed mostly of proteins with initial counts of 10 particles (10 or fewer measured in proteomics<sup>1,42</sup>), and the rest have initial counts of less than 50. However, the median of the distribution falling below 2 shows that most proteins are underproduced in our simulations. We observe several underproduced proteins whose counts are only increased to 1.25–1.5 times their initial counts after a cell cycle, all of which have long protein sequences (gene length >3 kb). We found that three key effects come into play in the rate of protein production in Syn3A: translation efficiency, mRNA lifetimes, and transcription rate. Our simulations lack the translational effects of polysomes, meaning that each mRNA can only be translated by a single ribosome at a time. We showed previously that polysomes play a significant role in doubling the number of proteins whose mRNA can be translated by more than one ribosome simultaneously.<sup>1</sup> In the absence of polysomes, proteins with longer sequences that would benefit from simultaneous translation from multiple ribosomes are underproduced.

Because we track every transcription, translation, and mRNA degradation event, we can calculate the average translation efficiency and mRNA half-life for every type of mRNA in Syn3A, as shown in Figures 5G and 5H, respectively. Our previous simplified 4D simulations exhibited average and median half-lives of 1.97 and 1.48 min, respectively.<sup>1</sup> Although our average and median mRNA half-lives have shifted slightly, the overall distribution still fits within the observed distribution in Bacillus subtilis, where individual mRNA were observed to have half-lives from less than 1 to 20 min.<sup>47</sup> The average and median fall in the range observed for other bacteria<sup>1,48,49</sup> and deviate slightly from a previous assumption that the median would be close to 2 min as measured in another Mycoplasma,<sup>18</sup> but this requires further validation in the absence of genome-wide mRNA degradation measurements for Syn3A. The most impactful change to the computational half-lives was an adjustment of the ratio of the binding rates for mRNA to ribosomes and degradosomes. Using the binding rates of mRNA to ribosomes and degradosomes from the previous model, preliminary simulations showed that the simulated cells would fall significantly short of doubling the counts of most proteins. We found that the ratio of these binding rates is among the most sensitive parameters in the 3D stochastic kinetics. Relative to our previous simplified 4D model,<sup>1</sup> the final parameter set here increases the binding rate of mRNA to ribosomes by a factor of 1.3 and reduces the binding rate of mRNA to degradosomes by a factor of 0.3, both values still coming from experimental measurements (see STAR Methods). These changes are reflected in the distribution of mRNA half-lives and translation efficiencies, showing that mRNA is longer lived and that more proteins can be translated per mRNA during the longer lifetimes. The increased mRNA lifetimes and translation efficiency then give us a distribution of protein production that comes closer to doubling the counts of most proteins. There are more reported values for parameters that could be tested, but testing multiple parameter sets in these simulations is computationally expensive, and other biological factors such as polysomes should be integrated before further varying these sensitive parameters. Preliminary 4DWCM simulations of 4 replicate cells showed that simply increasing the abundance of degradosomes significantly increased the doubling time.

We analyzed the difference in transcription events per cell cycle between both copies of each gene on the simulated daughter chromosomes (shown in Figure 5I). Most gene copies are unbiased, and we found no clear trend in the identities of genes that exhibit bias toward a specific gene copy. However, we found 81 genes that were not transcribed in one to three cell cycles spread across the 50 simulated cells. This does not imply that all 81 genes go unexpressed in the same cell, as these skipped genes are distributed among the 50 cells. This is not an unreasonable prediction considering that some proteins perform their functions infrequently. As long as some proteins are inherited from the previous generation, the cell can live. Also, given that the maximum number of cells in which a gene goes untranscribed is 3/50, and assuming the daughter generation has the same probability of skipping expression, the likelihood of not transcribing these genes in two consecutive generations is only 0.36% of all cells. The number of cells in which each gene goes untranscribed is listed in Table S3. The genes that go untranscribed are all low in proteomics value (<60), and the majority of them are genes of unknown function.

## Replication initiation kinetics are sensitive in 3D

DnaA controls the timing of DNA replication initiation through polymerization reactions that unwind DNA near the origin. We use a model based on the reaction scheme from our previous well-stirred simulations .<sup>1,42</sup> In short, we treat the origin of replication as an individual particle on the RDME lattice that follows the origin monomer on the BD DNA at the sequence position we identified previously.<sup>42</sup> The RDME particle undergoes state changes as more DnaA bind (the simulated kinetics are described in STAR Methods). We simulated 12 replicate cells using the reported average on and off rates of 100 mM<sup>−</sup> <sup>1</sup>s<sup>−</sup> <sup>1</sup> and $0 . 5 5 \ { \mathsf { s } } ^ { - 1 }$ for DnaA domain III binding to single-stranded DNA (ssDNA),<sup>50</sup> an assumption that worked in our previous wellstirred model.<sup>1</sup> However, when we implemented these rates in the 4D model, replication did not initiate within the first 60 min of the cell cycle in any of the 12 cells. This motivated an exploration of the available kinetic parameters for the on and off rates. In the same in vitro single-molecule study as the average rates, we identified and implemented on and off rates of 140 mM<sup>−</sup> <sup>1</sup>s<sup>−</sup> <sup>1</sup> and $0 . 4 2 \ { \mathsf { s } } ^ { - 1 }$ , measured for a DNA construct similar to the origin of Syn3A, consisting of both an AT-rich ssDNA and dsDNA sequence containing two DnaA domain IV binding sites (boxes).<sup>50</sup> With this change, replication initiates in almost every simulated cell within the first 15 min of the cell cycle, and the range of filament lengths at the time of replication initiation is 20 to 23 DnaA. Distribution of replication initiation times is shown in Figure 5J. Even the cell that did not initiate replication until 46 min into its cell cycle successfully completed replication and division within 2 h. To probe the sensitivity of DnaA binding to the origin in Syn3A, we performed all-atom simulations that show that the mutation of just three amino acids interacting with the DnaA box substantially reduces the binding affinity of DnaA to the origin, as shown in Figure S4.

## Genetic information reactions and metabolism are codependent

Although we will not discuss the dynamics of metabolism thoroughly here, it is still a critical factor driving the overall progression of the cell cycle in the 4DWCM. The pools of metabolites, with initial conditions based on measurements in E. coli,<sup>51</sup> dictate the synthesis rate of macromolecules such as DNA and RNA, and the uptake rates of lipids determine the rate of growth for the membrane. We show the concentrations of all metabolites and fluxes through all metabolic reactions in Data S1. Additionally, the energetic costs of all ATP-activated processes were once again quantified and are shown in Figure S5, but we do not observe any significant differences in ATP costs from the previous well-stirred model. As an example of the connection between metabolism and genetic information, we show the transcription rate for the dnaA gene in Figure 5K. The average transcription rate is reduced to roughly 55% of the maximum transcription elongation rate (corresponding to roughly 11 nt/s) with a range anywhere from roughly 30% to 80% until the volume has doubled. Once the volume doubles, some cells fully recover a maximum transcription elongation rate and some are still slowed down. Variations in transcription speed are due to fluctuations in the pools of nucleoside triphosphates (NTPs), as the elongation rate depends directly on the instantaneous NTP concentrations, as described in the STAR Methods. A significant difference from the previous well-stirred model is that this model does not accumulate large quantities of NTPs due to re-balancing of the nucleoside uptake rates, the glucose uptake rate, and the glycolysis reaction fructose 1,6 bisphosphate aldolase (FBA). The molecules that are most commonly limiting the rate of transcription are uridine triphosphate (UTP) and guanosine triphosphate (GTP), both of which have average pools around 0.3 mM but are sometimes fully depleted. Concentrations of 1–10 mM GTP and 8 mM UTP have been estimated for E. coli,<sup>52</sup> but no measurement has been performed yet in Syn3A. Although the NTP pools here seem too low, the uptake rates are generating excess pools of NTP precursors such as uridine and adenosine. Additionally, there are excess pools of all dNTPs, as can be seen in Data S1. Therefore, we are likely missing some balancing effects between NTP and dNTP pools in the metabolic rates, an example of which is metabolic inhibition. The average transcription rate being reduced is directly connected to protein formation by affecting the overall number of transcripts that are made. Although the average transcription elongation rate makes transcription look like a continuous process, we show that the mRNA population still depends on the stochastic probability of transcribing the gene and degrading the mRNA through the mRNA counts of dnaA for a single cell shown in Figure 5L. We also show the total number of DnaA proteins made as a function of time for the same cell to show the bursty nature of gene expression; proteins can only be made when mRNA is present.

## Partitioning of macromolecules to daughter cells is stochastic

Because we treat all proteins, RNA, DNA, and selected complexes in a 3D representation, our model automatically predicts the partitioning of these molecules to daughter cells once the division model isolates the daughter cells’ cytoplasms and separates their membranes. The random diffusion of particles on the lattice determines their locations at the time of division. We show a representative selection of particles and how their particles were partitioned in Figure 6: ribosomes, degradosomes (a peripheral membrane particle), PtsG (a transmembrane protein), and GapDH (a monomeric cytoplasmic protein). The population distributions appear to be random distributions approaching a binomial distribution. For each particle type chosen to select its region, the cell-to-cell variations show that our simulations have no significant bias toward one daughter cell over another for partitioning particles after division. Of note, the distribution for degradosome count differences shows peaks at the edges of the distributions. This is because of the DNA coarsegraining on the RDME lattice. If large portions of the DNA are pushed into contact with the membrane, the DNA lattice sites exclude peripheral membrane proteins such as degradosomes, resulting in a bias against that side of the dividing cell.

## DISCUSSION

Cells are not well-stirred reactor systems. Their intracellular environment is spatially heterogeneous and consists of many slowmoving, low-population components that need to encounter each other in 3D space for these components to react and perform their biological functions. Achieving spatial reaction-diffusion dynamics has been a significant challenge in the field of whole-cell modeling. Here, we presented a 4DWCM over an entire cell cycle of the genetically minimal cell, JCVI-syn3A. Simulating an entire cell cycle in 3D posed several challenges, the most significant of which included making chromosomes dynamic and partitioning them to daughter cells, updating morphology and connecting it to the hybrid stochastic-deterministic chemistry, and diffusing ribosomes. Overcoming each of these challenges required advances and integration of new computational methods and algorithms. With the advances in computational methods that we present here, we hope to illuminate the interwoven nature of the biology, chemistry, and physics that govern life for cells. Syn3A is the most genetically minimal organism that grows and regularly divides independently,<sup>19</sup> and our 4DWCM offers a platform with the minimal components for cellular life. In addition to the increasing interest in minimal cells such as Syn3A/B,<sup>53</sup> this 4DWCM acts as a foundation for complexifying reaction networks and pathways that exist in naturally occurring organisms.

One of the most powerful aspects of all-atom molecular dynamics is the transferability of the force fields to make predictions about interactions between molecules.<sup>54</sup> Unfortunately, no one organism has a complete set of experimentally determined kinetic parameters, chemical composition, and physical characteristics, so the model we present here, as well as other whole-cell models, has depended on the transferability of quantities among related organisms.<sup>1,3,4</sup> Further validation of cell states predicted by whole-cell models will help to inform which parameters are and are not transferable between organisms and may also provide insight into underlying biological effects that result in organism-to-organism variations up to orders of magnitude for some parameters. Individual datasets alone may not be enough to validate the individual cell states predicted by our 4DWCM. The variations that we predict in the macromolecular composition of daughter cells highlight the need for compiled predictions of complete cell states using experimental measurements at different points in the cell cycle. Assimilation of the data to construct these snapshots of cells at different points in time draws attention to the significant value in the growing interest of using ML and AI to build virtual cells from quantitative measurements from a wide array of experiments.<sup>5</sup> We see virtual cells and the 4DWCM as complementary methods to assemble cell states and then predict how the chemical and physical processes drive the changes between the predicted states.

![](images/d47b4aad30df24170f760009dbd5c70c20004b7136ea650d0f5caa9d9733584e.jpg)

![](images/44550f49616304975cdccd709e4a50325e84ebe10a1771a2b43572d1cafbc4c7.jpg)

![](images/c23e47808416af3b61d614d099c3f18a71526ff2a01a0a6da0c162e0824abbf5.jpg)

![](images/18b3ccb82bbbcb5092f9c606ac6376944a5ff974e65fd14faeef0f6ce26dce84.jpg)

![](images/155bae6492f66d23ae1b5b2e0cefb06e4d656dc6e29825072e67aa4805ce9cb4.jpg)

![](images/eb0659aaf983672ed42b4059bb0d88d61b5629507e237eb277f32883af918de0.jpg)

![](images/1cec86589ee92a1ee14bd29614a09ca8c61b56adc5a19c02198742050a29306a.jpg)

![](images/a34349c86ea761d3472bd69df1ea3cc8f6ad1cce98d3951d11c268e48502e8b9.jpg)  
Figure 6. Partitioning of macromolecules to daughter cells resulting from random diffusion on the RDME lattice after division Left: distribution of counts per cell among the population of divided cells. Right: difference in particle counts between pairs of daughter cells. Positive values correspond to more particles in the daughter cell in the positive z direction (relative to the division plane), and negative values correspond to more particles in the daughter cell in the negative z direction. All counts were taken from the 105 min time point, corresponding to the average predicted division time (n = 50 simulated cells).

## Limitations of the study

Among the most significant limitations of our 4DWCM is the required computational time and resources to achieve statistically significant sampling. Our simulations require 4–6 days of computational time on two high-performance computing GPUs per cell cycle. To obtain the 50 replicate cell cycles presented here required roughly 15,000 GPU h (625 GPU days) on NVIDIA A100 GPUs. This limits the sampling that can be performed to small populations of cells. Well-stirred simulations can take as little as a few hours per cell cycle and can simulate multiple cells in parallel.<sup>1,4,12,42</sup> We previously showed that 4D simulations can be used to better constrain and parameterize related wellstirred models.<sup>1</sup> Although we cannot simulate large numbers of cells with 4D models, and well-stirred models lack the predictive power of 4D models, we can build the crossroads between the two levels of complexity to accelerate the development of more predictive wholecell models. Another computational limitation comes with the frequency at which frames of the RDME simulation are written to the trajectory file. We previously hypothesized that the lifetime of a mRNA depends on the spatial proximity of the gene

to the membrane where the degradosomes are located.<sup>1</sup> The proximity of the fbaA/0131 gene particle on the RDME lattice for the mother chromosome and both daughter chromosomes to the nearest membrane lattice site in a single cell is shown in Figure S3. Gene-membrane proximity was averaged over the entire cell cycle, and we tried to correlate the proximity with bulk properties, including mRNA degradation rate, mRNA halflife, and protein production rate. We found no statistically significant correlations. To better quantify the relation between spatial proximity to the membrane and mRNA lifetime would require us to record every time step of the RDME trajectory, dramatically increasing the simulation time and storage requirements.

Although our model has made many predictions, it is still incomplete, and there are some important ingredients yet to be included: transcription of polycistronic RNA from operonal structures, coupled genetic information processing reactions, a kinetic model of FtsZ to drive cell division, and assembly reactions for all macromolecular complexes. The assumptions of the current transcription model have two known inaccuracies: independent transcription for all genes and promoter strengths assigned based on proteomics counts, both discussed in the STAR Methods. It is known that many genes are transcribed cooperatively into polycistronic RNA,<sup>20</sup> but this will require significant complexification of the reaction model and tracking of transcriptional states, as well as a more thorough quantitative study of long-read RNA sequencing to determine the operonal structures in Syn3A’s genome. Our current and previous models have all parameterized the promoter strengths based on the quantitative proteomics data,<sup>1,18,42</sup> limiting the transferability of the transcription model to other organisms. A model based on quantitative transcriptomics to help connect expression levels to sequence predictions of promoter sites and transcription termination sites should be more transferable to other bacteria.

Although our doubling time is in close agreement with experimental data, the protein abundances obtained from our wellstirred model, which included polysomes for a fixed cell geometry, are in better agreement with experimental proteomics.<sup>1</sup> The proteomics comparison suggests that polysomes are important for doubling the proteome in a cell cycle, especially for large proteins. Incorporation of polysomes will require integration of another simulation method to handle the diffusion of ribosomes separately. Other cooperative processes, such as coupled transcription-translation and membrane protein translation-translocation, are emerging as important factors in gene expression.<sup>44,45,55</sup> A well-stirred model of assembly reactions for all complexes is in development, and this model will need to be adapted to 4D, with the incorporation of coupled translationtranslocation of membrane proteins.

The artificial 12 pN force to partition chromosomes to daughter cells draws into question the predictive power of the physica model of chromosome dynamics. We found that the physical locations of genes within these small cells do not appear to correlate with bulk properties such as mRNA lifetimes, so the overal outcomes and predictions of our spatial reaction model should still hold even with a more biologically informed model of chromosome partitioning. Mechanisms that are known to partition chromosomes in other organisms, such as the Min system in E. coli<sup>56</sup> or the ParABS system in B. subtilis or C. crescentus,<sup>57</sup> are not present in the Syn3A genome. Unfortunately, we cannot simulate enough BD time steps to determine whether entropic segregation is sufficient to partition the chromosomes to daughter cells. Although entropic segregation is one hypothesis, we made several simplifying assumptions about SMC behavior in our model that could be refined and complexified to better partition the chromosomes.<sup>58–61</sup> Additionally, we assumed a fixed dwell time of 4 s and assumed that all SMCs remain bound during that 4 s dwell time. We have started exploring procedures with varied SMC physics and dwell times, and a preliminary study, as shown in Video S3 exhibits chromosome configurations suggesting that it is likely possible that our fictitious force could be replaced by a better SMC model. However, the procedures that could partition chromosomes with SMC are currently too computationally expensive; we estimate that these procedures would increase the simulation time to multiple weeks per cell.

Finally, there are still several organism-specific datasets required for a full-confidence validation of our 4DWCM, as discussed above. The most significant datasets are quantitative metabolomics,<sup>62</sup> genome-wide mRNA half-lives, proteome-wide protein half-lives, a survey of DNA-associated proteins, and long-read transcriptomics to tell us about operonal structures. To determine the transferability of the model for making predictions in related organisms, validation through these experiments will be incredibly valuable. In addition to datasets that still need to be measured, some recent experiments provide foundations for developing some of the model components discussed above, for example, the physical model of cell division using FtsZ. Such datasets include high-resolution structural data for Syn3A’s morphology<sup>22</sup> and lipidomics studies that quantified the effects of controlled lipid diets on the growth rate and morphology of Syn3A.<sup>63,64</sup> As we develop a physics-based model that can more accurately represent the growth and division of Syn3A, both regular and irregular, a more detailed kinetic model of lipid scavenging based on the controlled lipid diet experiments may provide insight into how the membrane physics and chemistry of lipid scavenging and synthesis act in unison to decide cell fate.

## RESOURCE AVAILABILITY

## Lead contact

Requests for further information and resources should be directed to and will be fulfilled by the lead contact, Zaida Luthey-Schulten (zan@illinois.edu).

## Materials availability

This study did not generate new materials.

## Data and code availability

• All original code to run and analyze the 4DWCM, including tables and graphics describing the program, are available on GitHub at https:// github.com/Luthey-Schulten-Lab/Minimal\_Cell\_4DWCM and Zenodo at https://doi.org/10.5281/zenodo.15579158.

• Files containing all particle counts for the 50 simulated cells are available through Zenodo at https://doi.org/10.5281/zenodo.15579158. Four representative LM RDME trajectory files from the 4DWCM are also provided.

• DNA sequencing data have been deposited in the NCBI SRA under BioProject PRJNA1257452.

• The plasmid sequence for genetic labeling of FtsZ in JCVI-syn3B is deposited in Mendeley Data under the DOI: https://doi.org/10.17632/ x59cx6ns2h.1.

• Any additional data reported in this paper, and the information required to reanalyze the data, are available from the lead contact upon request.

## ACKNOWLEDGMENTS

A.M., T.W., E.F., J.K., J.I.G., and Z.L.-S. are supported in part by NSF MCB 2221237. Z.L.-S., T.H., and A.P.M. are supported in part by the NSF Science and Technology Center for Quantitative Cell Biology (NSF DBI 2243257). W.P.’s research is supported by the Novo Nordisk Foundation (grant nos. NNF18SA0035142 and NNF22OC0079182) and the Independent Research Fund Denmark (grant no. 10.46540/2064-00032B). D.M.d.C.B. was supported by the Brazilian Agricultural Research Corporation (EMBRAPA, Brazil, #21195.002926/2019-98) and the National Institute of Science and Technology in Synthetic Biology (INCT BioSyn – CNPq, Brazil, #465603/2014-9; and FAP-DF, Brazil, #0193.001.262/2017). Z.R.T.’s research reported in this publication was supported by the Cancer Center at Illinois - Beckman Institute Postdoctoral Fellows Program sponsored by the Cancer Center at Illinois and the Beckman Institute for Advanced Science and Technology, University of Illinois, Urbana-Champaign. The content is solely the responsibility of the authors and does not necessarily represent the official views of the program sponsors. This research used the Delta advanced computing and data resource, which is supported by the National Science Foundation (award OAC 2005572) and the State of Illinois. Delta is a joint effort of the University of Illinois Urbana-Champaign and its National Center for Supercomputing Applications. We thank Glenn Fried for assisting with access to the shared facilities at the Carl R. Woese Institute for Genomic Biology at UIUC. We thank Chris Fields, Alvaro Hernandez, and Chris Wright from the Roy J. Carver Biotechnology Center sequencing facility at UIUC for assistance with collecting and processing the DNA sequencing data. The authors would like to thank Jay Cournoyer for assistance in culturing the JCVI-syn3A/B cell lines. All-atom simulations performed by Tianyu Wu were assisted by Aaron Chan. Ron Acda provided useful feedback and minor assistance in revising the GitHub documentation. The authors also thank Martin Gruebele, Rohit Bhargava, Kim S. Wise, Clyde A. Hutchison III, and Hamilton O. Smith for helpful discussions.

## AUTHOR CONTRIBUTIONS

Conceptualization, Z.R.T. and Z.L.-S.; methodology – development of 4DWCM, Z.R.T., A.M., T.A.B., and B.R.G.; software, T.W., W.P., and H.L.; investigation – analysis of simulations and additional simulations, E.F., T.W., and T.L.; investigation – cell imaging, J.K., Y.-L.G., and L.S.; investigation – DNA sequencing, J.Q.; resources – cell lines, D.M.d.C.B. and L.S.; writing – original draft, Z.R.T., A.M., and Z.L.-S.; funding acquisition, Z.L.-S.; resources, A.P.M. and J.I.G.; supervision, A.P.M., T.H., J.I.G., and Z.L.-S.; writing – review & editing, all authors.

## DECLARATION OF INTERESTS

The authors declare no competing interests.

## DECLARATION OF GENERATIVE AI AND AI-ASSISTED TECHNOLOGIES IN THE WRITING PROCESS

During the preparation of this work, the author(s) used ChatGPT in order to write Python functions to generate more aesthetically appealing plots. After using this tool, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication.

## STAR★METHODS

Detailed methods are provided in the online version of this paper and include the following:

KEY RESOURCES TABLE   
EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS ○ JCVI-syn3A-mCherry ○ JCVI-syn3B+FtsZ:mCherry ○ Growth Medium   
METHOD DETAILS ○ Syn3B Sample Preparation for Fluorescence Imaging ○ Airyscan Imaging ○ Growth Curve Experiments for DNA Sequencing ○ Genomic DNA extraction and Sequencing ○ Construction of the Syn3A 4DWCM ○ Initial Conditions ○ Simulation Methods for Chemical Reactions ○ Hybrid Simulation Algorithm ○ Simulating Chromosome Dynamics ○ Chemical Reaction Models ○ Diffusion ○ Cell Growth and Division in 3D ○ Molecular Dynamics of DnaA Binding to DNA ○ Computational Environments for Clusters and Supercomputing Resources   
QUANTIFICATION AND STATISTICAL ANALYSIS ○ Segmentation and analysis of fluorescence imaging

○ DNA coverage analysis

○ Calculation of mRNA half-lives

○ Analysis of 4DWCM trajectories

## SUPPLEMENTAL INFORMATION

Supplemental information can be found online at https://doi.org/10.1016/j.cell.   
2026.02.009.

Received: June 10, 2025   
Revised: December 9, 2025   
Accepted: February 9, 2026   
Published: March 9, 2026

## REFERENCES

1. Thornburg, Z.R., Bianchi, D.M., Brier, T.A., Gilbert, B.R., Earnest, E.E., Melo, M.C.R., Safronova, N., Sa´ enz, J.P., Cook, A.T., Wise, K.S., et al. (2022). Fundamental behaviors emerge from simulations of a living minimal cell. Cell 185, 345–360.e28. https://doi.org/10.1016/j.cell.2021.12.025.

2. Luthey-Schulten, Z., Thornburg, Z.R., and Gilbert, B.R. (2022). Integrating cellular and molecular structures and dynamics into whole-cell models. Curr. Opin. Struct. Biol. 75, 102392. https://doi.org/10.1016/j. sbi.2022.102392.

3. Karr, J.R., Sanghvi, J.C., Macklin, D.N., Gutschow, M.V., Jacobs, J.M., Bolival, B., Assad-Garcia, N., Glass, J.I., and Covert, M.W. (2012). A whole-cell computational model predicts phenotype from genotype. Cell 150, 389–401. https://doi.org/10.1016/j.cell.2012.05.044.

4. Macklin, D.N., Ahn-Horst, T.A., Choi, H., Ruggero, N.A., Carrera, J., Mason, J.C., Sun, G., Agmon, E., DeFelice, M.M., Maayan, I., et al. (2020). Simultaneous cross-evaluation of heterogeneous e. coli datasets via mechanistic simulation. Science 369, eaav3751. https://doi.org/10. 1126/science.aav3751.

5. Bunne, C., Roohani, Y., Rosen, Y., Gupta, A., Zhang, X., Roed, M., Alexandrov, T., AlQuraishi, M., Brennan, P., Burkhardt, D.B., et al. (2024). How to build the virtual cell with artificial intelligence: Priorities and opportunities. Cell 187, 7045–7063. https://doi.org/10.1016/j.cell.2024.11.015.

6. Stevens, J.A., Gru¨ newald, F., van Tilburg, P.A.M., Ko¨ nig, M., Gilbert, B.R., Brier, T.A., Thornburg, Z.R., Luthey-Schulten, Z., and Marrink, S.J. (2023). Molecular dynamics simulation of an entire cell. Front. Chem. 11, 1106495. https://doi.org/10.3389/fchem.2023.1106495.

7. Gilbert, B.R., Thornburg, Z.R., Brier, T.A., Stevens, J.A., Gru¨ newald, F., Stone, J.E., Marrink, S.J., and Luthey-Schulten, Z. (2023). Dynamics of chromosome organization in a minimal bacterial cell. Front. Cell Dev. Biol. 11, 1214962. https://doi.org/10.3389/fcell.2023.1214962.

8. Maritan, M., Autin, L., Karr, J., Covert, M.W., Olson, A.J., and Goodsell, D.S. (2022). Building structural models of a whole mycoplasma cell. J. Mol. Biol. 434, 167351. https://doi.org/10.1016/j.jmb.2021.167351.

9. Goodsell, D.S., and Autin, L. (2024). Integrative modeling of JCVI-Syn3A nucleoids with a modular approach. Curr. Res. Struct. Biol. 7, 100121. https://doi.org/10.1016/j.crstbi.2023.100121.

10. King, Z.A., Lu, J., Dra¨ ger, A., Miller, P., Federowicz, S., Lerman, J.A., Ebrahim, A., Palsson, B.O., and Lewis, N.E. (2015). BiGG models: A platform for integrating, standardizing and sharing genome-scale models. Nucleic Acids Res. 44, D515–D522. https://doi.org/10.1093/nar/gkv1049.

11. Mardinoglu, A., and Palsson, B.Ø. (2024). Genome-scale models in human metabologenomics. Nat. Rev. Genet. 26, 123–140. https://doi.org/ 10.1038/s41576-024-00768-0.

12. Sun, G., DeFelice, M.M., Gillies, T.E., Ahn-Horst, T.A., Andrews, C.J., Krummenacker, M., Karp, P.D., Morrison, J.H., and Covert, M.W. (2024). Cross-evaluation of e. coli’s operon structures via a whole-cell model suggests alternative cellular benefits for low- versus high-expressing operons. Cell Syst. 15, 227–245.e7. https://doi.org/10.1016/j. cels.2024.02.002.

13. Montero Llopis, P., Jackson, A.F., Sliusarenko, O., Surovtsev, I., Heinritz, J., Emonet, T., and Jacobs-Wagner, C. (2010). Spatial organization of the flow of genetic information in bacteria. Nature 466, 77–81. https://doi. org/10.1038/nature09152.

14. Bakshi, S., Siryaporn, A., Goulian, M., and Weisshaar, J.C. (2012). Superresolution imaging of ribosomes and rna polymerase in live escherichia coli cells. Mol. Microbiol. 85, 21–38. https://doi.org/10.1111/j.1365- 2958.2012.08081.x.

15. Lato, D.F., and Golding, G.B. (2020). Spatial patterns of gene expression in bacterial genomes. J. Mol. Evol. 88, 510–520. https://doi.org/10.1007 s00239-020-09951-3.

16. Gibson, D.G., Glass, J.I., Lartigue, C., Noskov, V.N., Chuang, R.-Y., Algire, M.A., Benders, G.A., Montague, M.G., Ma, L., Moodie, M.M., et al. (2010). Creation of a bacterial cell controlled by a chemically synthesized genome. Science 329, 52–56. https://doi.org/10.1126/science.1190719.

17. Hutchison, C.A., Chuang, R.-Y., Noskov, V.N., Assad-Garcia, N., Deerinck, T.J., Ellisman, M.H., Gill, J., Kannan, K., Karas, B.J., Ma, L., et al. (2016). Design and synthesis of a minimal bacterial genome. Science 351, aad6253. https://doi.org/10.1126/science.aad6253.

18. Breuer, M., Earnest, E.E., Merryman, C., Wise, K.S., Sun, L., Lynott, M.R., Hutchison, C.A., Smith, H.O., Lapek, J.D., Gonzalez, D.J., et al. (2019). Essential metabolism for a minimal cell. eLife 8, e36842. https://doi. org/10.7554/elife.36842.

19. Pelletier, J.F., Sun, L., Wise, K.S., Assad-Garcia, N., Karas, B.J., Deerinck, T.J., Ellisman, M.H., Mershin, A., Gershenfeld, N., Chuang, R.-Y., et al. (2021). Genetic requirements for cell division in a genomically minimal cell. Cell 184, 2430–2440.e16. https://doi.org/10.1016/j.cell.2021.03.008.

20. Sandberg, T.E., Wise, K.S., Dalldorf, C., Szubin, R., Feist, A.M., Glass, J.I., and Palsson, B.O. (2023). Adaptive evolution of a minimal organism with a synthetic genome. iScience 26, 107500. https://doi.org/10.1016/j. isci.2023.107500.

21. Gilbert, B.R., Thornburg, Z.R., Lam, V., Rashid, F.M., Glass, J.I., Villa, E., Dame, R.T., and Luthey-Schulten, Z. (2021). Generating chromosome geometries in a minimal cell from cryo-electron tomograms and chromosome conformation capture maps. Front. Mol. Biosci. 8, 644133. https:// doi.org/10.3389/fmolb.2021.644133.

22. Ali, M., Peck, A., Yu, Y., Schwartz, J., Glass, J., Zheng, S., and Paraan, M. (2024). CryoET of near-minimal cells mycoplasma mycoides JCVI-Syn3A for the development of subtomogram averaging pipelines. Chan Zuckerberg CryoET Data Portal DS-10442. https://cryoetdataportal.czscience. com/datasets/10442.

23. Bianchi, D.M., Pelletier, J.F., Hutchison, C.A., Glass, J.I., and Luthey-Schulten, Z. (2022). Toward the complete functional characterization of a minimal bacterial proteome. J. Phys. Chem. B 126, 6820–6834. https://doi.org/10.1021/acs.jpcb.2c04188.

24. Hallock, M.J., Stone, J.E., Roberts, E., Fry, C., and Luthey-Schulten, Z. (2014). Simulation of reaction diffusion processes over biologically relevant size and time scales using multi-GPU workstations. Parallel Comput. 40, 86–99. https://doi.org/10.1016/j.parco.2014.03.009.

25. Ryu, J.-K., Rah, S.-H., Janissen, R., Kerssemakers, J.W.J., Bonato, A., Michieletto, D., and Dekker, C. (2022). Condensin extrudes DNA loops in steps up to hundreds of base pairs that are generated by ATP binding events. Nucleic Acids Res. 50, 820–832. https://doi.org/10.1093/nar/ gkab1268.

26. Ganji, M., Shaltiel, I.A., Bisht, S., Kim, E., Kalichava, A., Haering, C.H., and Dekker, C. (2018). Real-time imaging of DNA loop extrusion by condensin. Science 360, 102–105. https://doi.org/10.1126/science.aar7831.

27. Humphrey, W., Dalke, A., and Schulten, K. (1996). VMD: Visual molecular dynamics. J. Mol. Graph. 14, 33–38. https://doi.org/10.1016/0263- 7855(96)00018-5.

28. Roberts, E., Stone, J.E., and Luthey-Schulten, Z. (2012). Lattice microbes: High-performance stochastic simulation method for the reac-

tion-diffusion master equation. J. Comput. Chem. 34, 245–255. https:// doi.org/10.1002/jcc.23130.

29. Thompson, A.P., Aktulga, H.M., Berger, R., Bolintineanu, D.S., Brown, W.M., Crozier, P.S., in ’t Veld, P.J., Kohlmeyer, A., Moore, S.G., Nguyen, T.D., et al. (2022). LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum scales. Comput. Phys. Commun. 271, 108171. https://doi.org/10.1016/j.cpc.2021.108171.

30. Gogou, C., Japaridze, A., and Dekker, C. (2021). Mechanisms for chromosome segregation in bacteria. Front. Microbiol. 12, 685687. https:// doi.org/10.3389/fmicb.2021.685687.

31. Brackley, C.A., Morozov, A.N., and Marenduzzo, D. (2014). Models for twistable elastic polymers in Brownian dynamics, and their implementation for LAMMPS. J. Chem. Phys. 140, 135103. https://doi.org/10.1063/ 1.4870088.

32. Kim, E., Barth, R., and Dekker, C. (2023). Looping the genome with SMC complexes. Annu. Rev. Biochem. 92, 15–41. https://doi.org/10.1146/annurev-biochem-032620-110506.

33. Wang, J.D., and Levin, P.A. (2009). Metabolism, cell growth and the bacterial cell cycle. Nat. Rev. Microbiol. 7, 822–827. https://doi.org/10.1038/ nrmicro2202.

34. Bittencourt, D.M., Bittencourt, D.M.C., Brown, D.M., Assad-Garcia, N., Romero, M.R., Sun, L., Palhares de Melo, L.A.M., Freire, M., and Glass, J.I. (2024). Minimal bacterial cell JCVI-syn3B as a chassis to investigate interactions between bacteria and mammalian cells. ACS Synth. Biol. 13, 1128–1141. https://doi.org/10.1021/acssynbio.3c00513.

35. Matteau, D., Lachance, J.C., Grenier, F., Gauthier, S., Daubenspeck, J.M., Dybvig, K., Garneau, D., Knight, T.F., Jacques, P.E<sup>´</sup> ., and Rodrigue, S. (2020). Integrative characterization of the near-minimal bacterium mesoplasma florum. Mol. Syst. Biol. 16, e9844. https://doi.org/10. 15252/msb.20209844.

36. Pezeshkian, W., and Ipsen, J.H. (2024). Mesoscale simulation of biomembranes with FreeDTS. Nat. Commun. 15, 548. https://doi.org/10. 1038/s41467-024-44819-w.

37. De Franceschi, N.D., Pezeshkian, W., Fragasso, A., Bruininks, B.M.H., Tsai, S., Marrink, S.J., and Dekker, C. (2022). Synthetic membrane shaper for controlled liposome deformation. ACS Nano 17, 966–978. https://doi.org/10.1021/acsnano.2c06125.

38. Seto, S., and Miyata, M. (1998). Cell reproduction and morphological changes in mycoplasma capricolum. J. Bacteriol. 180, 256–264. https://doi.org/10.1128/jb.180.2.256-264.1998.

39. Yao, N.Y., Georgescu, R.E., Finkelstein, J., and O’Donnell, M.E. (2009). Single-molecule analysis reveals that the lagging strand increases replisome processivity but slows replication fork progression. Proc. Natl. Acad. Sci. USA 106, 13236–13241. https://doi.org/10.1073/pnas.0906157106.

40. Moger-Reischer, R.Z., Glass, J.I., Wise, K.S., Sun, L., Bittencourt, D.M.C., Lehmkuhl, B.K., Schoolmaster, D.R., Lynch, M., and Lennon, J.T. (2023). Evolution of a minimal cell. Nature 620, 122–127. https:// doi.org/10.1038/s41586-023-06288-x.

41. Bremer, H., and Dennis, P.P. (2008). Modulation of chemical composition and other parameters of the cell at different exponential growth rates. EcoSal Plus 3, 1–48. https://doi.org/10.1128/ecosal.5.2.3.

42. Thornburg, Z.R., Melo, M.C.R., Bianchi, D., Brier, T.A., Crotty, C., Breuer, M., Smith, H.O., Hutchison, C.A., Glass, J.I., and Luthey-Schulten, Z. (2019). Kinetic modeling of the genetic information processes in a minimal cell. Front. Mol. Biosci. 6, 130. https://doi.org/10.3389/fmolb.2019.00130.

43. Kim, S., Beltran, B., Irnov, I., and Jacobs-Wagner, C. (2019). Long-distance cooperative and antagonistic RNA polymerase dynamics via DNA supercoiling. Cell 179, 106–119.e16. https://doi.org/10.1016/j.cell. 2019.08.033.

44. O’Reilly, F.J., Xue, L., Graziadei, A., Sinn, L., Lenz, S., Tegunov, D., Blo¨ tz, C., Singh, N., Hagen, W.J.H., Cramer, P., et al. (2020). In-cell architecture of an actively transcribing-translating expressome. Science 369, 554–557. https://doi.org/10.1126/science.abb3758.

45. Xue, L., Lenz, S., Zimmermann-Kogadeeva, M., Tegunov, D., Cramer, P., Bork, P., Rappsilber, J., and Mahamid, J. (2022). Visualizing translation dynamics at atomic detail inside a bacterial cell. Nature 610, 205–211. https://doi.org/10.1038/s41586-022-05255-2.

46. Forchhammer, J., and Lindahl, L. (1971). Growth rate of polypeptide chains as a function of the cell growth rate in a mutant of escherichia coli 15. J. Mol. Biol. 55, 563–568. https://doi.org/10.1016/0022- 2836(71)90337-8.

47. Hambraeus, G., von Wachenfeldt, C., and Hederstedt, L. (2003). Genome-wide survey of mRNA half-lives in bacillus subtilis identifies extremely stable mRNAs. Mol. Genet. Genomics 269, 706–714. https:// doi.org/10.1007/s00438-003-0883-6.

48. Rauhut, R., and Klug, G. (1999). mRNA degradation in bacteria. FEMS Microbiol. Rev. 23, 353–370. https://doi.org/10.1111/j.1574-6976.1999. tb00404.x.

49. Steiner, P.A., De Corte, D., Geijo, J., Mena, C., Yokokawa, T., Rattei, T., Herndl, G.J., and Sintes, E. (2019). Highly variable mRNA half-life time within marine bacterial taxa and functional genes. Environ. Microbiol. 21, 3873–3884. https://doi.org/10.1111/1462-2920.14737.

50. Cheng, H.-M., Gro¨ ger, P., Hartmann, A., and Schlierf, M. (2014). Bacteria initiators form dynamic filaments on single-stranded DNA monomer by monomer. Nucleic Acids Res. 43, 396–405. https://doi.org/10.1093/ nar/gku1284.

51. Yus, E., Maier, T., Michalodimitrakis, K., van Noort, V., Yamada, T., Chen, W.-H., Wodke, J.A.H., Gu¨ ell, M., Martı´nez, S., Bourgeois, R., et al. (2009). Impact of genome reduction on bacterial metabolism and its regulation. Science 326, 1263–1268. https://doi.org/10.1126/science.1177263.

52. Park, J.O., Rubin, S.A., Xu, Y.-F., Amador-Noguez, D., Fan, J., Shlomi, T., and Rabinowitz, J.D. (2016). Metabolite concentrations, fluxes and free energies imply efficient enzyme usage. Nat. Chem. Biol. 12, 482–489. https://doi.org/10.1038/nchembio.2077.

53. Seidel, Z.P., Kumar, R., Conroy Araujo, M.M., Glass, S.A., Rodriguez, R., Goshia, T., and Glass, J.I. (2025). Meeting proceedings from 4th minimal cell workshop: Exploring JCVI minimal cell fundamental insights and integrative applications. ACS Synth. Biol. 14, 1905–1911. https://doi.org/10. 1021/acssynbio.5c00159.

54. Hwang, W., Austin, S.L., Blondel, A., Boittier, E.D., Boresch, S., Buck, M., Buckner, J., Caflisch, A., Chang, H.-T., Cheng, X., et al. (2024). CHARMM at 45: Enhancements in accessibility, functionality, and speed. J. Phys. Chem. B 128, 9976–10042. https://doi.org/10.1021/acs.jpcb.4c04100.

55. Jensen, R.K., Xue, L., Marotta, F., Somody, J.C., Selkrig, J., Lenz, S., Rappsilber, J., Savitski, M.M., Kosinski, J., Typas, A., et al. (2025). Incell discovery and characterization of a non-canonical bacterial protein translocation-folding complex. Preprint at bioRxiv. https://doi.org/10. 1101/2025.04.25.650208.

56. Di Ventura, B., Knecht, B., Andreas, H., Godinez, W.J., Fritsche, M., Rohr, K., Nickel, W., Heermann, D.W., and Sourjik, V. (2013). Chromosome segregation by the escherichia coli Min system. Mol. Syst. Biol. 9, 686. https://doi.org/10.1038/msb.2013.44.

57. Jalal, A.S.B., and Le, T.B.K. (2020). Bacterial chromosome segregation by the ParABS system. Open Biol. 10, 200097. https://doi.org/10.1098/ rsob.200097.

58. Branda˜ o, H.B., Ren, Z., Karaboja, X., Mirny, L.A., and Wang, X. (2021). DNA-loop-extruding SMC complexes can traverse one another in vivo. Nat. Struct. Mol. Biol. 28, 642–651. https://doi.org/10.1038/s41594- 021-00626-1.

59. Liao, Q., Branda˜ o, H.B., Ren, Z., and Wang, X. (2025). Replisomes restrict SMC-mediated DNA-loop extrusion in vivo. Preprint at bioRxiv. https://doi.org/10.1101/2025.02.23.639750.

60. Branda˜ o, H.B., Paul, P., van den Berg, A.A., Rudner, D.Z., Wang, X., and Mirny, L.A. (2019). RNA polymerases as moving barriers to condensin loop extrusion. Proc. Natl. Acad. Sci. USA 116, 20489–20499. https:// doi.org/10.1073/pnas.1907009116.

61. Barth, R., Davidson, I.F., van der Torre, J., Taschner, M., Gruber, S., Peters, J.-M., and Dekker, C. (2025). SMC motor proteins extrude DNA asymmetrically and can switch directions. Cell 188, 749–763.e21. https://doi.org/10.1016/j.cell.2024.12.020.

62. Haas, D., Thamm, A.M., Sun, J., Huang, L., Sun, L., Beaudoin, G.A.W., Wise, K.S., Lerma-Ortiz, C., Bruner, S.D., Breuer, M., et al. (2022). Metabolite damage and damage control in a minimal genome. mBio 13, e0163022. https://doi.org/10.1128/mbio.01630-22.

63. Justice, I., Kiesel, P., Safronova, N., von Appen, A., and Saenz, J.P. (2024). A tuneable minimal cell membrane reveals that two lipid species suffice for life. Nat. Commun. 15, 9679. https://doi.org/10.1038/s41467- 024-53975-y.

64. Safronova, N., Junghans, L., Oertel, J., Fahmy, K., and Saenz, J.P. (2024). Chemically defined lipid diets reveal the versatility of lipidome remodeling in genomically minimal cells. Preprint at bioRxiv. https://doi. org/10.1101/2024.10.04.616688.

65. Chang, A., Jeske, L., Ulbrich, S., Hofmann, J., Koblitz, J., Schomburg, I., Neumann-Schaal, M., Jahn, D., and Schomburg, D. (2021). BRENDA, the ELIXIR core data resource in 2021: new developments and updates. Nucleic Acids Res. 49, D498–D508. https://doi.org/10.1093/nar/gkaa1025.

66. Langmead, B., and Salzberg, S.L. (2012). Fast gapped-read alignment with Bowtie 2. Nat. Methods 9, 357–359. https://doi.org/10.1038/ nmeth.1923.

67. Danecek, P., Bonfield, J.K., Liddle, J., Marshall, J., Ohan, V., Pollard, M.O., Whitwham, A., Keane, T., McCarthy, S.A., Davies, R.M., et al. (2021). Twelve years of SAMtools and BCFtools. GigaScience 10, giab008. https://doi.org/10.1093/gigascience/giab008.

68. Phillips, J.C., Hardy, D.J., Maia, J.D.C., Stone, J.E., Ribeiro, J.V., Bernardi, R.C., Buch, R., Fiorin, G., He´ nin, J., Jiang, W., et al. (2020). Scalable molecular dynamics on CPU and GPU architectures with NAMD. J. Chem. Phys. 153, 044130. https://doi.org/10.1063/5.0014475.

69. Best, R.B., Zhu, X., Shim, J., Lopes, P.E.M., Mittal, J., Feig, M., and MacKerell, A.D. (2012). Optimization of the additive CHARMM all-atom protein force field targeting improved sampling of the backbone ϕ, ψ and side-chain χ1 and χ<sup>2</sup> dihedral angles. J. Chem. Theor. Comput. 8, 3257–3273. https://doi.org/10.1021/ct300400x.

70. Huang, J., Rauscher, S., Nawrocki, G., Ran, T., Feig, M., de Groot, B.L., Grubmu¨ ller, H., and MacKerell, A.D. (2016). CHARMM36m: an improved force field for folded and intrinsically disordered proteins. Nat. Methods 14, 71–73. https://doi.org/10.1038/nmeth.4067.

71. Abramson, J., Adler, J., Dunger, J., Evans, R., Green, T., Pritzel, A., Ronneberger, O., Willmore, L., Ballard, A.J., Bambrick, J., et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493–500. https://doi.org/10.1038/s41586-024-07487-w.

72. Schneider, C.A., Rasband, W.S., and Eliceiri, K.W. (2012). Nih image to imagej: 25 years of image analysis. Nat. Methods 9, 671–675. https:// doi.org/10.1038/nmeth.2089.

73. Chen, S.S., Sperling, E., Silverman, J.M., Davis, J.H., and Williamson, J.R. (2012). Measuring the dynamics of e. coli ribosome biogenesis using pulse-labeling and quantitative mass spectrometry. Mol. Biosyst. 8, 3325–3334. https://doi.org/10.1039/c2mb25310k.

74. Hindmarsh, A.C., and Odepack, A. (1983). Systematized Collection of ODE Solvers. In Scientific Computing, 1, R.S. Stepleman, M. Carver, R. Peskin, W.F. Ames, and R. Vichnevetsky, eds. (North-Holland Publishing Company), pp. 55–64.

75. Petzold, L. (1983). Automatic selection of methods for solving stiff and nonstiff systems of ordinary differential equations. SIAM J. Sci. Stat. Comput. 4, 136–148. https://doi.org/10.1137/0904010.

76. Mantelli, S., Muller, P., Harlepp, S., and Maaloum, M. (2011). Conformational analysis and estimation of the persistence length of DNA using atomic force microscopy in solution. Soft Matter 7, 3412. https://doi. org/10.1039/c0sm01160f.

77. Bonato, A., and Michieletto, D. (2021). Three-dimensional loop extrusion. Biophys. J. 120, 5544–5552. https://doi.org/10.1016/j.bpj.2021.11.015.

78. Banigan, E.J., van den Berg, A.A., Branda˜ o, H.B., Marko, J.F., and Mirny, L.A. (2020). Chromosome organization by one-sided and two-sided loop extrusion. eLife 9, e53558. https://doi.org/10.7554/elife.53558.

79. Bianco, P., Bongini, L., Melli, L., Dolfi, M., and Lombardi, V. (2011). Piconewton-millisecond force steps reveal the transition kinetics and mechanism of the double-stranded DNA elongation. Biophys. J. 101, 866–874. https://doi.org/10.1016/j.bpj.2011.06.039.

80. Jun, S., and Wright, A. (2010). Entropy as the driver of chromosome segregation. Nat. Rev. Microbiol. 8, 600–607. https://doi.org/10.1038/ nrmicro2391.

81. Harju, J., van Teeseling, M.C.F., and Broedersz, C.P. (2024). Loop-extruders alter bacterial chromosome topology to direct entropic forces for segregation. Nat. Commun. 15, 4618. https://doi.org/10.1038/ s41467-024-49039-w.

82. Seba, M., Boccard, F., and Duigou, S. (2024). Activity of MukBEF fo chromosome management in e. coli and its inhibition by MatP. eLife 12, RP91185. https://doi.org/10.7554/elife.91185.

83. Letzkus, M., Trela, C., and Mera, P.E. (2024). Three factors ParA, TipN, and DnaA-mediated chromosome replication initiation are contributors of centromere segregation in caulobacter crescentus. Mol. Biol. Cell 35, ar68. https://doi.org/10.1091/mbc.e23-12-0503.

84. Trussart, M., Yus, E., Martinez, S., Bau�, D., Tahara, Y.O., Pengo, T., Widjaja, M., Kretschmer, S., Swoger, J., Djordjevic, S., et al. (2017). Defined chromosome structure in the genome-reduced bacterium mycoplasma pneumoniae. Nat. Commun. 8, 14665. https://doi.org/10. 1038/ncomms14665.

85. Papagiannakis, A., Yu, Q., Govers, S.K., Lin, W.-H., Wingreen, N.S., and Jacobs-Wagner, C. (2025). DNA/polysome phase separation and cell width confinement couple nucleoid segregation to cell growth in escherichia coli. eLife 14, RP104276. https://doi.org/10.7554/elife.104276.1.

86. Hofmeyr, J.-H.S., Gqwaka, O.P.C., and Rohwer, J.M. (2013). A generic rate equation for catalysed, template-directed polymerisation. FEBS Lett. 587, 2868–2875. https://doi.org/10.1016/j.febslet.2013.07.011.

87. Meadow, N.D., Mattoo, R.L., Savtchenko, R.S., and Roseman, S. (2005). Transient state kinetics of enzyme i of the phosphoenolpyruvate:glycose phosphotransferase system of escherichia coli: Equilibrium and secondorder rate constants for the phosphotransfer reactions with phosphoenolpyruvate and HPr. Biochemistry 44, 12790–12796. https://doi.org/ 10.1021/bi0502846.

88. Wallen, J.R., Zhang, H., Weis, C., Cui, W., Foster, B.M., Ho, C.M.W., Hammel, M., Tainer, J.A., Gross, M.L., and Ellenberger, T. (2017). Hybrid methods reveal multiple flexibly linked DNA polymerases within the bacteriophage T7 replisome. Structure 25, 157–166. https://doi.org/10. 1016/j.str.2016.11.019.

89. Malinen, A.M., Turtola, M., Parthiban, M., Vainonen, L., Johnson, M.S., and Belogurov, G.A. (2012). Active site opening and closure control translocation of multisubunit RNA polymerase. Nucleic Acids Res. 40, 7442–7451. https://doi.org/10.1093/nar/gks383.

90. Siwiak, M., and Zielenkiewicz, P. (2013). Transimulation - protein biosynthesis web service. PLoS One 8, e73943. https://doi.org/10.1371/journal. pone.0073943.

91. Bremer, H., and Dennis, P.P. (1996). Modulation of chemical composition and other parameters of the cell by growth rate. Escherichia coli and Salmonella. Cell. Mol. Biol. 2, 1553–1569.

92. Young, R., and Bremer, H. (1976). Polypeptide-chain-elongation rate in escherichia coli B/r as a function of growth rate. Biochem. J. 160, 185–194. https://doi.org/10.1042/bj1600185.

93. Morellet, N., Hardouin, P., Assrir, N., van Heijenoort, C., and Golinelli-Pimpaneau, B. (2022). Structural insights into the dimeric form of bacillus

subtilis RNase Y using NMR and AlphaFold. Biomolecules 12, 1798. https://doi.org/10.3390/biom12121798.

94. Garrey, S.M., Blech, M., Riffell, J.L., Hankins, J.S., Stickney, L.M., Diver, M., Hsu, Y.-H.R., Kunanithy, V., and Mackie, G.A. (2009). Substrate binding and active site residues in RNases E and G: role of the 5’-sensor. J. Biol. Chem. 284, 31843–31850. https://doi.org/10.1074/jbc.m109. 063263.

95. Bartholoma¨ us, A., Fedyunin, I., Feist, P., Sin, C., Zhang, G., Valleriani, A., and Ignatova, Z. (2016). Bacteria differently regulate mRNA abundance to specifically respond to various stresses. Philos. Trans. A Math. Phys. Eng. Sci. 374, 20150069. https://doi.org/10.1098/rsta.2015.0069.

96. Fazal, F.M., Koslover, D.J., Luisi, B.F., and Block, S.M. (2015). Direct observation of processive exoribonuclease motion using optical tweezers. Proc. Natl. Acad. Sci. USA 112, 15101–15106. https://doi.org/10. 1073/pnas.1514028112.

97. Cho, K.H. (2017). The structure and function of the gram-positive bacterial RNA degradosome. Front. Microbiol. 8, 154. https://doi.org/10.3389/ fmicb.2017.00154.

98. Earnest, E.E., Lai, J., Chen, K., Hallock, M.J., Williamson, J.R., and Luthey-Schulten, Z. (2015). Toward a whole-cell model of ribosome biogenesis: Kinetic modeling of SSU assembly. Biophys. J. 109, 1117–1135. https://doi.org/10.1016/j.bpj.2015.07.030.

99. Davis, J.H., Tan, Y.Z., Carragher, B., Potter, C.S., Lyumkis, D., and Williamson, J.R. (2016). Modular assembly of the bacterial large ribosomal subunit. Cell 167, 1610–1622.e15. https://doi.org/10.1016/j.cell.2016. 11.020.

100. Earnest, E.E., Cole, J.A., Peterson, J.R., Hallock, M.J., Kuhlman, T.E., and Luthey-Schulten, Z. (2016). Ribosome biogenesis in replicating cells: Integration of experiment and theory. Biopolymers 105, 735–751. https:// doi.org/10.1002/bip.22892.

101. Nomura, M., Gourse, R., and Baughman, G. (1984). Regulation of the synthesis of ribosomes and ribosomal components. Annu. Rev. Biochem. 53, 75–117. https://doi.org/10.1146/annurev.bi.53.070184. 000451.

102. Nierhaus, K.H. (1991). The assembly of prokaryotic ribosomes. Biochimie 73, 739–755. https://doi.org/10.1016/0300-9084(91)90054-5.

103. Chen, S.S., and Williamson, J.R. (2013). Characterization of the ribosome biogenesis landscape in e. coli using quantitative mass spectrometry. J. Mol. Biol. 425, 767–779. https://doi.org/10.1016/j.jmb.2012.11.040.

104. Werner, A. (2010). Predicting translational diffusion of evolutionary conserved RNA structures by the nucleotide number. Nucleic Acids Res. 39, e17. https://doi.org/10.1093/nar/gkq808.

105. Golding, I., and Cox, E.C. (2004). RNA dynamics in live escherichia coli cells. Proc. Natl. Acad. Sci. USA 101, 11310–11315. https://doi.org/10. 1073/pnas.0404443101.

106. Helfrich, W. (1973). Elastic properties of lipid bilayers: Theory and possible experiments. Z. Naturforsch. C 28, 693–703. https://doi.org/ 10.1515/znc-1973-11-1209.

107. Seifert, U., Berndl, K., and Lipowsky, R. (1991). Shape transformations of vesicles: Phase diagram for spontaneous- curvature and bilayercoupling models. Phys. Rev. A 44, 1182–1202. https://doi.org/10.1103/ physreva.44.1182.

108. Gompper, G., and Kroll, D.M. (1998). Membranes with fluctuating topology: Monte Carlo simulations. Phys. Rev. Lett. 81, 2284–2287. https:// doi.org/10.1103/physrevlett.81.2284.

109. Siggel, M., Kehl, S., Reuter, K., Ko¨ finger, J., and Hummer, G. (2022). Tri-Mem: A parallelized hybrid Monte Carlo software for efficient simulations of lipid membranes. J. Chem. Phys. 157, 174801. https://doi.org/10. 1063/5.0101118.

## STAR★METHODS

## KEY RESOURCES TABLE

<table><tr><td>REAGENT or RESOURCE</td><td>SOURCE</td><td>IDENTIFIER</td></tr><tr><td>Bacterial and virus strains</td><td></td><td></td></tr><tr><td>JCVI-syn3A+mCherry</td><td>JCVI</td><td>N/A</td></tr><tr><td>JCVI-syn3B+FtsZ:mCherry</td><td>JCVI</td><td>N/A</td></tr><tr><td>Chemicals, peptides, and recombinant proteins</td><td></td><td></td></tr><tr><td>Mycoplasma Broth Base</td><td>BD</td><td>Cat#DF0554-17-1</td></tr><tr><td>Bacto Tryptone</td><td>BD</td><td>Cat#211705</td></tr><tr><td>Bacto Peptone</td><td>BD</td><td>Cat#211677</td></tr><tr><td>Glucose 20% w/v stock</td><td>Thermo Fisher Scientific</td><td>Cat#G8270</td></tr><tr><td>CMRL1066 (10X stock w/o phenol red; w/o bicrb; w/o Gln)</td><td>Thermo Fisher Scientific</td><td>Cat#21-540-026</td></tr><tr><td>Sodium bicarbonate 7.5% w/v stock</td><td>Thermo Fisher Scientific</td><td>Cat#S6014</td></tr><tr><td>L-glutamine 200 mM stock</td><td>Thermo Fisher Scientific</td><td>Cat#25030081</td></tr><tr><td>Yeast extract solution</td><td>Thermo Fisher Scientific</td><td>Cat#18180059</td></tr><tr><td>TC Yeastolate 2% w/v stock, autoclaved</td><td>Gibco</td><td>Cat#255772</td></tr><tr><td>Serum (heat inactivated FBS, HS) OR substitute (KO)</td><td>Thermo Fisher Scientific</td><td>Cat#10828028</td></tr><tr><td>Penicilln G (400,000 U/mL stock)</td><td>Sigma-Aldrich</td><td>Cat#P3032-1MU</td></tr><tr><td>Phenol red (0.5%w/v filter sterilized)</td><td>Sigma-Aldrich</td><td>Cat#P0290-100ML</td></tr><tr><td>KnockOut Serum Replacement Paraformaldehyde (32%)</td><td>ThermoFisher</td><td>Cat#10828028</td></tr><tr><td></td><td>Electron Microscopy Sciences</td><td>Cat#15680</td></tr><tr><td>Phosphate-buffered silane (PBS)</td><td>Corning</td><td>Cat#21-040-CV</td></tr><tr><td>Poly-D-lysine Hoechst 33342</td><td>Gibco</td><td>Cat#A3890401</td></tr><tr><td></td><td>Thermo Scientific</td><td>Cat#62249</td></tr><tr><td>FM1-43FX</td><td>Invitrogen</td><td>Cat#F35355</td></tr><tr><td>PrimeSTAR Max DNA Polymerase</td><td>Takara</td><td>#R045A</td></tr><tr><td>Critical commercial assays</td><td></td><td></td></tr><tr><td>PureLink gDNA extraction kit</td><td>Thermo Fisher Scientific</td><td>Cat#K182001</td></tr><tr><td>Qubit dsDNA HS Assay Kit</td><td>Thermo Fisher Scientific</td><td>Cat#Q33230</td></tr><tr><td>Illumina DNA Prep Kit</td><td>Illumina</td><td>Cat#20060060</td></tr><tr><td>Illumina MiSeq</td><td>Illumina</td><td>Cat#SY-410-1003</td></tr><tr><td>Deposited data</td><td></td><td></td></tr><tr><td>gDNA Sequencing (mid-exponential, late-exponential, and stationary cells)</td><td>This study</td><td>NCBI SRA PRJNA1257452</td></tr><tr><td>JCVI-syn3A genome</td><td>Breuer et al. 18</td><td>GenBank: CP016816.2</td></tr><tr><td>Genome sequencing</td><td>Sandberg et al.20</td><td>NCBI SRA GSE205017 / Aledb: https://aledb.ucsd.edu/ ale/project/52/</td></tr><tr><td>Illumina RNAseq</td><td>Sandberg et al.20</td><td>NCBI SRA GSE205017</td></tr><tr><td>Mass spectrometry data of Syn3A</td><td>Breuer et al. 18</td><td>MassIVE - Accession Number: 000081687</td></tr><tr><td>Proteomics of Syn3A</td><td>Breuer et al.18</td><td>ProteomeXchange  Accession Number: PXD008159</td></tr><tr><td>Partial Relative Metabolomics</td><td>Haas et al.62</td><td>https://doi.org/10.6084/m9.figshare.20020574</td></tr><tr><td>E. coli Metabolomics</td><td>Park et al.52</td><td>Supplementary Iation t://</td></tr><tr><td>BRENDA</td><td>Chang et al..65</td><td>10.1038/nchembio.2077 https://www.brenda-enzymes.org/</td></tr></table>

(Continued on next page)

<table><tr><td colspan="3">Continued</td></tr><tr><td>REAGENT or RESOURCE</td><td>SOURCE</td><td>IDENTIFIER</td></tr><tr><td>Software and algorithms</td><td></td><td></td></tr><tr><td>Lattice Microbes - v2.5</td><td>Luthey-Schulten Lab</td><td>https://github.com/Luthey-Schulten-Lab/Lattice_ Microbes</td></tr><tr><td>odecell - v1.0</td><td>Thornburg et al.1</td><td>https://github.com/Luthey-Schulten-Lab/odecell</td></tr><tr><td>FreeDTS version 6.7.2023</td><td>Pezeshkian and Ipsen 36</td><td>https://github.com/weria-pezeshkian/FreeDTS</td></tr><tr><td>sc_chain_gen version 7.20.2023</td><td>Gilbert et al.7</td><td>https://github.com/Luthey-Schulten-Lab/sc_chain_ generation</td></tr><tr><td>LAMMPS version 19Nov.2024</td><td>Thompson et al.29</td><td>https://www.lammps.org</td></tr><tr><td>btree_chromo</td><td>Gilbert et al.?</td><td>https://github.com/Luthey-Schulten-Lab/btree_ chromo_gpu</td></tr><tr><td>Docker version 20.10.11</td><td>Docker Inc.</td><td>https://www.docker.com/</td></tr><tr><td>Apptainer version 1.3.5-1.el8</td><td>Singularity/Apptainer Development Team, Int&#x27;l.</td><td>https://doi.org/10.5281/zenodo.1310023</td></tr><tr><td>VMD - v2.0 alpha</td><td>Humphrey et al.27</td><td>https://www.ks.uiuc.edu/Research/vmd/</td></tr><tr><td>bcl2fastq - v2.20</td><td>Illumina</td><td>https://support.illumina.com/sequencing/sequencing_ software/bcl2fastq-conversion-software.html</td></tr><tr><td>Bowtie 2 - v2.5.4</td><td>Langmead and Salzberg66</td><td>https://bowtie-bio.sourceforge.net/bowtie2/</td></tr><tr><td>Samtools - v1.21</td><td>Danecek et al.67</td><td>index.shtml https://github.com/samtools/samtools</td></tr><tr><td>NAMD - v3.0.1</td><td>Phillips et al. 688</td><td>https://www.ks.uiuc.edu/Research/namd/</td></tr><tr><td>CHARMM - v36m</td><td>Best et al.6; Huang et al.70</td><td>https://academiccharmm.org/</td></tr><tr><td>AlphaFold - v3 (2025.07.05)</td><td>Abramson et al.71</td><td>https://deepmind.google/science/alphafold/</td></tr><tr><td>ImageJ - v1.54r Other</td><td>Schneider et al.72</td><td>https://github.com/imagej/lmageJ/releases/tag/v1.54r</td></tr><tr><td colspan="3"></td></tr><tr><td>8-well chambered coverslip</td><td>Fisher Scientific</td><td>Cat#12-565-470</td></tr></table>

## EXPERIMENTAL MODEL AND STUDY PARTICIPANT DETAILS

## JCVI-syn3A-mCherry

A frozen stock of the genetically minimal bacterium Syn3A-mCherry was provided by the JCVI. Frozen stocks were scrapped and inoculated into 10 mL of SP4 media (see formulation above) under BSL2 conditions and incubated at 37 ∘C with shaking. Once the media acidifies (∼2 days), cells are used for experiments.

## JCVI-syn3B+FtsZ:mCherry

JCVI-syn3B is a genetic variant of Syn3A with a ‘‘landing pad’’ system to mediate genetic modification that has the same doubling time as Syn3A when no genetic modifications have been inserted in the landing pad. Genetic insertion of Ftsz:mCherry (JCVI-SYN3A\_0522 fused with an mCherry gene) was performed as described previously for insertion of a single gene to the Syn3B genetic landing pad.<sup>34</sup> To minimize disruption to the cell division machinery, the original gene copy was left intact and mCherry was added at the C-terminal end of the genetically inserted second copy of FtsZ.

Gibson assembly was used to construct the plasmid. JCVI-syn1.0 (GeneBank accession number is CP002027) served as the template to amplify fragment 1 using primers 5’-GAATTCGCCAGAACCAGCAGCGGAGCCAGCGGATCCTTTTAAAAATGTCGGAAAGT CATC-3’ and 5’-AGCAAAGTGGGTGATAAATAAATGACAAACGAATTTAAACAAATAGC-3’, and fragment 2 using primers 5’-CGT TTGTCATTTATTTATCACCCACTTTG-3’ and 5’-ATTTGAACGTTGCGAAGCAACAGAAGCATAATAACAATTATTAAT-3’. The vector backbone was amplified using primers 5’-AAGGATCCGCTGGCTCCGCTGCTGGTTCTGGCGAATTCATGGTATCAAAAGGAGA AGAAGATAATATG-3’ and 5’-TAATTGTTATTATGCTTCTGTTGCTTCGCAACGTTCAAATC-3’, with the ptxB-FLAG plasmid (not published) as the template. PrimeSTAR Max DNA polymerase (Takara, #R045A) was used to amplify the fragments. PCR was performed with an initial denaturation at 98∘C for 3 minutes, followed by 30 cycles of 98∘C for 10 seconds, 55∘C for 10 seconds, and 72∘ C for 1 minute, with a final extension at 72∘C for 5 minutes. Primers 5’-TCCTCCAGCTCCTAATCCTT-3’ and 5’-TGTTTGTCGGTGAAC GCTCT-3’ were used for colony PCR to identify positive clones. The final plasmid was confirmed by sequencing.

## Growth Medium

SP4 part 1: Resuspend 3.5 g Mycoplasma Broth Base, 10 g Bacto Tryptone, and 5.3 g Bacto Peptone in distilled water to a final volume of 600 mL. Adjust pH to 7.5. Autoclave for 15 minutes at 121∘C.

SP4 part 2: Combine the following: 25 mL Glucose (20% w/v stock), 50 mL CMRL 1066 (10X stock, w/o phenol red, w/o bicarbonate, w/o Gln), 6 mL Sodium Bicarbonate (7.5% w/v), 5 mL L-glutamine (200 mM), 35 mL Yeast Extract Solution (15% w/v), 100 mL TC Yeastolate (2% w/v), 170 mL KnockOut Serum Replacement, 2.5 mL Penicillin G (400,000 U/mL), and 1.5 mL Phenol Red (1% w/v). Filter sterilize (0.2 μm) and store at 4∘C.

SP4 medium: Combine SP4 part 1 and SP4 part 2 with a 1.5:1 ratio under sterile conditions.

## METHOD DETAILS

## Syn3B Sample Preparation for Fluorescence Imaging

Minimal JCVI-syn3B cells expressing the FtsZ:mCherry fusion protein were cultured in SP4 medium supplemented with KnockOut Serum Replacement (ThermoFisher #10828028). For each experiment, cells were freshly prepared from frozen stocks. A small portion of the frozen cells was scraped and transferred to 20 mL of culture medium, followed by static incubation at 37∘ C for 24 h.

Cells were fixed during the logarithmic growth phase by adding 2 mL of 32% paraformaldehyde (Electron Microscopy Sciences #15680) and incubating for 30 min on a nutator. Fixed cells were then harvested by centrifugation at 4,500 × g for 10 min. The resulting pellet was resuspended in 1 mL of phosphate-buffered silane (Corning #21-040-CV) and seeded onto an 8-well chambered coverslip (Fisher Scientific, #12-565-470) coated with poly-D-lysine (Gibco, #A3890401).

After approximately 6 hours of incubation, cells were rinsed twice with PBS and sequentially stained with 1 μg/mL Hoechst 33342 (Thermo Scientific, #62249) for 10 min at room temperature, followed by pre-cooled 5 μg/mL FM1-43FX (Invitrogen, #F35355) for 1 min on ice. After each staining step, cells were washed three times with PBS for 5 min to remove excess dye.

## Airyscan Imaging

A Zeiss LSM 900 confocal microscope equipped with an Airyscan 2 module was used to acquire three-color images of fixed JCVIsyn3B FtsZ:mCherry cells. All images were captured in Airyscan mode with an xy pixel size of 35-nm and a z-step of 130-nm for 3D imaging. Fluorescence signals were collected for 1.1 μs per pixel per color channel. Sub-diffraction-limited image processing was performed using ZEN software (Zeiss).

## Growth Curve Experiments for DNA Sequencing

48 hours post thaw, 1 mL of stationary phase Syn3A-mCherry culture was collected and centrifuged at 12,000 × g for 10 minutes. The cell pellet was then resuspended in 1 mL PBS. 80 μL of culture was used to seed 20 mL SP4 media cultures, one for each timepoint in triplicate. Cultures were left to grow at 37 ∘C with rotation for 5 (mid-exponential phase), 9 (late exponential), or 21 hours (stationary phase). After growth, cultures were centrifuged at 13,000 × g for 10 minutes at 4 ∘C. Cell pellets were snap-frozen and stored at -80 ∘ C until processed.

## Genomic DNA extraction and Sequencing

Syn3A-mCherry cells for DNA sequencing were collected at 5 (mid-exponential), 9 (late exponential), and 21 (stationary) hours of growth. Frozen cell pellets were processed in parallel using the TrueLink gDNA extraction kit (ThermoFisher #K182001) as per manufacturer instructions. gDNA concentrations were quantified using Qubit, as per manufacturer instructions.

The shotgun genomic libraries were prepared with the Illumina DNA Prep kit (Illumina, #20060060). The library pool was quantitated by qPCR and sequenced on one MiSeq flowcell for 251 cycles from each end of the fragments using a MiSeq 500-cycle sequencing kit version 2. Fastq files were generated and demultiplexed with the bcl2fastq v2.20 Conversion Software (Illumina). Phix DNA is used as a spike-in control for MiSeq runs.

## Construction of the Syn3A 4DWCM

The remainder of the methods details describe the methods used in the 4DWCM. We describe the initial conditions, the simulation methods, the hybrid algorithm the connects the simulations methods, and the physical and chemical details for individual processes. We also include a discussion of the construction of the computational environments used to simulate the 4DWCM.

## Initial Conditions

## Computational Growth Medium

In Thornburg et al., we published a defined growth medium composition for Syn3A in which the exact concentration of each nutrient was controlled except for lipids and fatty acids.<sup>1</sup> We used this formulation to determine the concentration of extracellular nutrients in the simulations. Because we only simulate a single cell, we assume that the depletion of nutrients from the medium is negligible relative to bulk solution over the course of a single cell cycle. We therefore set the growth medium concentrations as fixed constants in the simulation. The exact concentrations used in the simulated growth medium are provided in Table S1.

## Metabolites

We previously generated a set of initial concentrations for intracellular metabolites from scaling metabolomics values reported for E. coli.<sup>1</sup> We did not modify these values from the previous models, and they are re-stated in Table S1.

## Macromolecular Complexes

RNAP and degradosomes are both initialized with counts of zero for the number of assembled complexes. The individual protein sub units are randomly distributed throughout the cytoplasm and then quickly assemble early in the simulation. We find that the vast majority of RNAP and degradosome complexes that can form through the initial proteomics are assembled in <1 second of biological time in our simulations.

Each replicate cell is initialized with 500 ribosomes. The previously published cryo-electron tomograms of Syn3A showed that the ribosomes are uniformly distributed throughout the cytoplasm.<sup>21</sup> Based on this observation, we randomly distribute the initial 500 ribosomes throughout the cytoplasm by randomly sampling a uniform distribution. Additionally, to account for excluded volume effects, no two ribosome center of mass particles are placed in the same lattice site. For each ribosome center of mass particle, we then build a cross consisting of 7 lattice sites around the center of the mass that are assigned the ‘‘ribo\_center’’ site type for the center of mass and ‘‘ribosomes’’ for each lattice site sharing a face with the center site (shown in Figure S1).

## Proteins

All non-ribosomal proteins are initialized to their proteomics values reported in Thornburg et al.<sup>1</sup> For cytoplasmic proteins, the particles are randomly distributed throughout the cytoplasm, DNA, and outer\_cytoplasm (membrane periphery) regions at ratios of 1/2, 1/3, and 1/6 roughly reflecting the ratio of the volumes of the three regions to achieve a uniform random distribution of proteins throughout the cell. The particles for all transmembrane proteins are randomly distributed throughout the membrane region. The peripheral membrane protein particles are randomly distributed throughout the outer\_cytoplasm region.

Ribosomal proteins are initialized with reduced counts from the reported proteomics values. We assume that the counts reported in the proteomics also include the proteins incorporated into ribosomes. To determine the number of free ribosomal proteins in the initial conditions, we subtracted the number that would be incorporated into ribosomes (500 per protein) from the respective protein’s proteomics count. However, not all ribosomal proteins have enough counts detected in the proteomics to form 500 ribosomes. We believe this is likely due to proteins stuck to rRNA that stay stuck during the trypsin digestion process, therefore reducing the number of proteins detected in mass spec. In this case, we assume that there are enough proteins to form 500 ribosomes and add an additional 25 proteins to the initial condition for the respective ribosomal protein. We chose 25 proteins because it has been reported that roughly 5% of ribosomal proteins are not ribosome-associated per ribosomal protein.<sup>73</sup>

The initial counts for the number of free proteins for the entire proteome are provided in the supplemental information.

## RNA

All rRNA are assumed to be in complete ribosomes at the start of the simulation, so the number of all free rRNA are initialized to 0. We use the same initial conditions as the previous model for counts of tRNA. We distribute a total of 200 tRNA per isoform for the 20 types of tRNA. This was chosen by scaling the total number of tRNA observed in E. coli to the same concentration in Syn3A, which corresponds to a total of roughly 6,000 tRNA molecules per cell for a 200 nm radius Syn3A cell.<sup>1</sup> Syn3A has a total of 29 tRNA isoforms among the 20 types of tRNA.

In the absence of quantitative transcriptomics, we used the average counts of mRNA from our previous model as the initial conditions. Each cell is initialized with a different count of each mRNA. To determine the initial count for each type of mRNA, we randomly sample a Poisson distribution whose average value corresponds to twice the average count observed in the previous model.<sup>1</sup> We sample distributions with twice the average because in initial testing, we were already able to observe the average total mRNA content of cells with updated kinetic parameters for genetic information processing. When we quantified the average total mRNA count using the updated parameters, we observed the total mRNA count to be double the total observed in the previous model (400 vs 200 total mRNA). We make the assumption that the individual mRNA abundances are also roughly twice the average counts observed in the previous model. The general increase in mRNA abundance is a result of increasing mRNA stability (and therefore lifetimes) by increasing the binding rate to ribosomes and decreasing their binding rate to degradosomes. The binding rates are discussed below and the increased lifetimes are shown in Figure 5. A complete table of the average counts used to sample the Poisson distributions are provided in the supplemental information.

## Chromosome Configuration

The initial chromosome configuration is generated using the program sc\_chain\_generation. This program iteratively grows the circular chromosome into a spherical boundary as a series of spherocylinders representing a set number of beads. The exact algorithms are described in depth by Gilbert and coworkers.<sup>7</sup> We chose to iteratively generate the chromosome over 4 stages: 2000 12-bead, 8000 6-bead, 18000 3-bead, and finally 54338 1-bead growth stages. The final stage corresponds to 10 bp per bead for the 543 kbp chromosome of Syn3A. We generate this configuration within a spherical boundary 1900 A<sup>˚</sup> in radius, a reduced volume from the full cell to ensure that the chromsome does not intersect with membrane lattice cubes in the RDME representation.

Once the initial configuration has been generated, we impose the chromsome configuration on the RDME lattice. To do this, we iterate over each of the 54338 beads in the chromosome and divide their x, y, and z coordinates by the resolution of the RDME lattice (10 nm). Then, for each coordinate, we set the corresponding lattice site to the DNA site type. Some particles may correspond to the same lattice site, in which case the site is still just set to the DNA site type.

We also need to place particles onto the lattice to represent the transcription start site for each gene in the genome. First, the transcription start and end sites are assigned to individual 10 bp beads in the configuration. The genomic sequence positions were ob tained from the NCBI GenBank entry for Syn3A: CP016816.2. While the transcription start site typically is found upstream of the coding sequence (CDS), we take the genomic sequence position of the CDS for each protein-coding gene as the start and end sites for transcription.

## Morphology: RDME Lattice Site Types

The RDME simulation requires site types to be defined for every position in the cubic lattice to evaluate diffusion propensities and determine reaction localization. We first initialize a simulation with a simulation box of dimensions $6 4 \times 6 4 \times 1 2 8$ in units of lattice sites whose edges lengths are 10 nm. The size of the z-dimension is twice the size of x and y because the simulation box will contain two cells divided along the z-axis after division. With the simulation box initialized, the cellular regions can be defined using the RegionBuilder function in jLM. RegionBuilder contains functions to build filled predefined shapes (e.g. spheres and cubes) as binary arrays with dimensions equal to the size of the simulation box. It also contains functions to manipulate the binary arrays by growing or reducing regions. Because the regions are first defined as binary arrays, they can be manipulated using logical operations. First, we define a cytoplasmic sphere with radius 20 lattice cubes (200 nm) centered at the midpoint of the simulation box (32,32,64). From this sphere, we use the dilate function of RegionBuilder to create a sphere one lattice site thicker using the se26 option. The dilate options are se6 if contiguity of the new layer is not important or se26 if contiguity needs to be maintained in the new layer of lattice sites. 6 corresponds to the number of faces for adjacent cubes and 26 includes all edge and vertex adjacencies. We then use a logical operation to exclude the cytoplasm from the new sphere by using the $\mathbb { \sim } \mathbb { \alpha } \sim \mathbb { \beta }$ (and not) operation between the two binary arrays. This leaves a spherical shell that defined the cytoplasm peripheral to the membrane with region name outer\_cytoplasm. From the first dilated sphere, we then add one more layer of lattice sites using the same procedure and then exclude both the cytoplasm and outer\_cytoplasm to leave a spherical shell for the membrane. Everything outside of the membrane is defined as extracellular. Once all region shapes are constructed (including the ribosomes and DNA), they need to be combined into the RDME site lattice. Because there will be overlaps between regions (e.g. between cytoplasm and DNA), an order of priority is assigned to each site type. The priority order from lowest to highest priority is as follows: extracellular, cytoplasm, outer\_cytoplasm, ribosomes, DNA, ribo\_centers, and membrane. This order is assigned so that only the membrane is exposed to the extracellular environment and so that the DNA excludes ribosome diffusion into the DNA, but does not exclude the center of mass chemically active site from performing translation.

## Simulation Methods for Chemical Reactions

## ODE

Ordinary differential equations (ODEs) model the time evolution of metabolite concentrations in a deterministic framework. This method was applied to processes such as glycolysis, nucleotide synthesis, lipid synthesis, and transporter activity. We solved the resulting stiff ODE system using the LSODA solver from the ODEPACK software suite, employing the backward differentiation formula (BDF) method with order varying between 1 and $5 . ^ { 7 4 , 7 5 }$ The system of ODEs was constructed using the odeCELL package, which provides a simple API for specifying kinetic parameters, defining custom enzyme kinetics rate forms, and mapping reactions to differential equations.

## CME

The chemical master equation (CME) captures the stochastic dynamics of well-stirred systems by modeling the probability distribution over discrete particle counts and simulating chemical reactions as probabilistic transitions between states. Unlike the deterministic ODE model, which reports only mean concentrations, the CME approach captures both distributions and fluctuations, which is especially important in systems with low copy numbers. This method was used to simulate transcription and tRNA charging. Stochastic simulations were performed using the Gillespie direct algorithm as implemented in version 2.5 of Lattice Microbes (LM). The CME system was constructed using the pyLM package, which provides Python bindings to the underlying LM codebase. RDME

The reaction-diffusion master equation (RDME) extends the CME by incorporating spatial resolution, dividing the system into subvolumes where reactions occur and between which particles diffuse. Simulations of the RDME sample trajectories from the underlying probability distribution $P ( \pmb { x } , t ) ,$ , where the state vector x encodes the copy numbers of all species in all subvolumes:

$$
\begin{array} { l } { \displaystyle \frac { d P ( \mathbf { x } , t ) } { d t } = \mathbf { R } P ( \mathbf { x } , t ) + \mathbf { D } P ( \mathbf { x } , t ) \ = \ \displaystyle \sum _ { v } ^ { V } \sum _ { r } ^ { R } [ - a _ { r } ( \pmb { x } _ { v } ) P ( \pmb { x } _ { v } , t ) + a _ { r } ( \pmb { x } _ { v } - \pmb { \mathbb { S } } _ { r } ) P ( \pmb { x } _ { v } - \pmb { \mathbb { S } } _ { r } , t ) ] } \\ { \displaystyle \qquad + \ \sum _ { v } ^ { V } \sum _ { \xi } ^ { i j , k } \sum _ { \alpha } ^ { N } \big [ - d _ { v } ^ { \alpha } \pmb { x } _ { v } ^ { \alpha } P ( \pmb { x } , t ) + d _ { v + \xi } ^ { \alpha } \big ( \pmb { x } _ { v + \xi } ^ { \alpha } + 1 \big ) P \big ( \pmb { x } + \mathbb { 1 } _ { v + \xi } ^ { \alpha } - \mathbb { 1 } _ { v } ^ { \alpha } , t \big ) \big ] } \end{array}\tag{Equation 1}
$$

Here, the first term R corresponds to the CME description, which accounts for reactions occurring within each subvolume v according to the stoichiometric matrix $\pmb { s }$ and reaction propensities $a _ { r } ( { \pmb x } _ { v } )$ for each of the R reactions specified by r. The second term D is the diffusion operator, where $d _ { v } ^ { \alpha }$ is the diffusion propensity of species α in volume $v ,$ with ξ indexing the six Cartesian directions for the six neighboring volumes.

We used the RDME framework to simulate spatial and stochastic processes including RNAP diffusion and binding to gene start sites, translation, diffusion and binding of mRNA and degradosomes during mRNA degradation, membrane protein insertion, and replication initiation. Diffusion is described in further detail below. Importantly, RNAP and degradosomes were assigned distinct diffusion coefficients to reflect their differing mobilities from other proteins, and ribosomes diffuse within a special scheme that represents the ribosome on the lattice. Simulations were conducted using the multi-particle diffusion algorithm in Lattice Microbes v2.5.<sup>24,28</sup> The spatial model and reaction network were constructed using the jLM package, which extends pyLM to support spatial modeling and interactive visualization.

## Hybrid Simulation Algorithm

The hybrid simulations are built on the platform of performing ‘‘hook’’ simulations in the single-GPU 32-bit RDME solver in LM IntMpdRdmeSolver. A summary of the hybrid simulation algorithm is shown in Figure 2. The hookSimulation function allows the user to interrupt the stochastic reaction-diffusion solver to perform user-defined functions through the jLM Python API. In a hookSimulation, the user can manipulate site types and the positions and numbers of particles in the RDME. Because the procedures exist inside a Python API, the user can execute any Python functions while the RDME solver is paused. The only restriction is that the hookSimulation function must return one of three recognized values by the LM solver: 0, 1, or 2. If the user returns a value of 0, nothing is changed in the RDME solver. If the user returns 1, the LM solver will read any manual changes made to the particle lattice and copy the updated particle lattice to the GPU. If the user returns 2, the solver also reads any changes to the site type lattice and writes the current state of the site types to the LM trajectory file.

The procedure for the 4DWCM hookSimulation function can be found in the deposited code for the model in Hook.py. The frequency of interruption to perform a hookSimulation is a user-defined variable at the start of the simulation in units of RDME time steps. Here, our hook frequency is 250 time steps, or 12.5 ms of biological time. This frequency was determined by the frequency required to update ribosome positions (discussed in Diffusion). Because we are communicating between spatially-localized and well-stirred reaction methods, we chose to track all particle counts dynamically in a single Python dictionary. The instantaneous particle counts and some state variables (e.g. volume and surface area) are dynamically updated throughout communication and are converted to and from concentrations only within the ODE model for metabolism. To communicate the different methods at their own frequencies, we simply implemented conditionals that follow timers for individual processes. The timer for communicating with BD chromosome dynamics is set to enter DNA communication every 4 s of biological time. Once the hookSimulation passes the DNA communication conditional or functions, it enters into the procedure to update the ribosome excluded volume. Ribosomes are updated after DNA because the ribosome excluded volumes depend on the excluded volume of the DNA. A timer is set for 1 s of biological time for the global CME and metabolic ODE simulations. The simulation first enters into the global CME procedure, reads the current cell state from the RDME, executes a 1 s simulation of well-stirred stochastic reactions for transcription and tRNA charging, and then the results are read from the CME trajectory into the particle counts and RDME lattice. The cell state is then communicated to the ODE model of metabolism where metabolites, transporters, and metabolic enzymes’ particle counts are first converted to concentrations using the instantaneous cell volume. The costs of genetic information are communicated to the metabolite pools. We then integrate 1 s of biological time using LSODA as described above. The results are communicated to the overall particle counts. Finally, also at an interval of one second, we write out the cell state. The particle counts dictionary and metabolic fluxes are recorded to a csv file. We save the particle and site lattice as binary npy files in the case that we need to restart the simulation from the current cell state. If the simulation is at an interval of one second, the hookSimulation function returns 2 to the LM solver to write the RDME state to the LM trajectory file. Otherwise, we return 1 so that the updated ribosome excluded volumes are copied back to the GPU.

## Computational Expense of the 4DWCM

The average computational expense for each of the major components of the 4DWCM are plotted in Figure 2. The component requiring the most time is the RDME solver itself performing diffusion and spatially-localized stochastic reactions on the lattice. Second, is the time to update ribosome positions. In order to maintain excluded volume and have the ribosomes obey Stokes-Einstein diffusion, we update the projections of the excluded volume of every ribosome every 12.5 ms, or 80 times per biological second. The other notable contributor is the ‘‘DNA time’’. While the time presented in the performance plot corresponds to the Growth and Division and Brownian Dynamics components of the flowchart, it does not include the time spent integrating the BD on the second GPU. The BD simulations are executed in parallel and take a similar amount of time per biological second compared to the total time spent in other processes. The time in the plot represents the time to perform communications, update morphology on the lattice, move particles to keep them in their respective regions (e.g. cytoplasm and membrane), and execute any serialized DNA processes. For example, the boundary in LM and LAMMPS must be synchronized, so we update the position of the membrane in LAMMPS serially instead of in parallel any time the morphology changes.

## Simulating Chromosome Dynamics

In our minimal cell model, the chromosomal DNA is represented using a coarse-grained bead-spring polymer, implemented using the code btree\_chromo which calls LAMMPS as a library. Chromosome dynamics are simulated in hook intervals corresponding to 4 seconds of biological time. This approach builds upon the methodology introduced by Gilbert et al.,<sup>7</sup> enabling us to model the influence of SMC complexes and topoisomerases. In this section, we briefly review the core aspects of the original model and highlight the key modifications and extensions required to adapt it to the 4DWCM.

## Polymer Representation and Brownian Dynamics

Syn3A’s chromosome is modeled as an elastic worm-like chain, with a coarse-graining of 10 base pairs per bead, with each bead having diameter $\sigma _ { \mathsf { D N A } } { = } 3 . 4 ~ \mathsf { n m } . ^ { 3 1 }$ Bonds between DNA beads are finite extensible nonlinear elastic (FENE) using bond\_style fene in LAMMPS:

$$
U _ { i } ^ { s } ~ = ~ - ~ \frac { \kappa _ { s } L _ { 0 } ^ { 2 } } { 2 } \vert \boldsymbol { 0 } \boldsymbol { \mathrm { g } } \left[ \mathbb { 1 } ~ - ~ \left( I _ { i } / L _ { 0 } \right) ^ { 2 } \right] + U _ { \mathrm { L J , c u t } }\tag{Equation 2}
$$

where l is the distance between DNA beads i and $i + 1 , \kappa _ { S } ~ = ~ 1 0 0 k _ { B } T / \sigma _ { \mathsf { D N A } } ^ { 2 } , L _ { 0 } ~ = ~ 1 . 5 \sigma _ { \mathsf { D N A } } ,$ , and $U _ { \mathsf { L J , c u t } }$ is a Lennard Jones potential with $\epsilon = k _ { B } T$ and $\sigma = \sigma _ { \mathsf { D N A } }$ . The bending potential is implemented using angle\_style cosine:

$$
U _ { i } ^ { b } = \kappa _ { b } [ 1 - \cos ( \pi - \theta _ { i } ) ]\tag{Equation 3}
$$

where $\theta _ { j }$ is the angle between DNA beads i and $j + 1$ and $\kappa _ { b } = I _ { p } k _ { B } T / \sigma _ { \mathsf { D N A } }$ with persistence length $I _ { p } = 4 5 \ : \mathsf { n m } . ^ { 7 6 }$

Excluded volume effects are implemented via a ‘‘hard’’ potential which does not allow strand crossing, and ‘‘topo’’ potential which allows strand crossing. The hard Lennard-Jones potential is implemented with pair\_style hard,

$$
U _ { i j } ^ { \mathrm { h a r d } } ~ = ~ 4 \epsilon \left[ \left( \frac { \sigma } { r _ { i j } } \right) ^ { 1 2 } - ~ \left( \frac { \sigma } { r _ { i j } } \right) ^ { 6 } \right] \theta \Big ( 2 ^ { \frac { 1 } { 6 } } \sigma - r _ { i j } \Big )\tag{Equation 4}
$$

where $r _ { i j }$ is the distance between beads i and $j , \sigma \ = \ \sigma _ { \mathsf { D N A } }$ , and the potential strength is $\epsilon = 5 k _ { B } T .$ . Every five looping cycles (i.e. every two seconds of biological time), we replace the hard potential with a ‘‘topoisomerase’’ potential which is implemented with pair\_style soft:

$$
U _ { i j } ^ { \mathrm { t o p o } } = A \left[ 1 + \cos \left( \frac { \pi r _ { i j } } { r _ { c } } \right) \right] \theta \left( r _ { c } - r _ { i j } \right)\tag{Equation 5}
$$

where $r _ { \mathsf { c } } = \sigma _ { \mathsf { D N A } }$ is the cutoff distance, and the potential strength is $A = 0 .$ 1k<sub>B</sub>T or 1:0k<sub>B</sub>T. When simulating topoisomerase action, we perform the following sequence: 1) minimize with $A = 0 . 1 k _ { B } T$ and harmonic bonds, 2) Minimize with $A = 0 . 1 k _ { B } T$ and FENE bonds, 3) Run 5000 BD steps with $A = 0 . 1 k _ { B } T$ and FENE bonds, 4) Minimize with $A = 1 . 0 k _ { B } T$ and harmonic bonds, 5) Minimize with $A = ~ 1 . 0 k _ { B } T$ and FENE bonds. Steps 1–3 allow strand crossings, and steps 4–5 ramp up the potential to avoid clashes when simulating with the hard potential.

Excluded volume between the DNA and the cell membrane is implemented with a hard potential, with the boundary particles representing cell membrane shapes being kept fixed during all minimizations and BD. For our model, we do not implement any attractive forces between the DNA and boundary particles, which could arise through translation-transcription coupling.

The system evolves under Brownian dynamics, modeled as Langevin dynamics in the large friction (no mass) limit. The equation of motion for each bead is given by $\begin{array} { r } { \gamma \frac { d r } { d t } = - \nabla U + { \pmb R } ( t ) } \end{array}$ where γ is the translational damping constant, U represents the total interaction potential, and $\pmb { R } ( t )$ is a stochastic noise term satisfying the fluctuation-dissipation theorem, with an assumed temperature of 310 K. We use a timestep of 0.1 ns for integration. Time stepping was performed using a custom version of fix brownian that was modified to work with the Kokkos package in LAMMPS (see ‘‘GPU Acceleration’’ below). The translational damping constant for the DNA was calculated using the Stokes-Einstein equation $\gamma = 6 \pi \eta r _ { \mathsf { D N A } }$ , with a dynamic viscosity $\overline { { \eta } }$ of 1.2 Pa s, which is derived from mRNA diffusion in E. coli as described in our previous 4DWCM.<sup>1</sup>

## SMC Looping Model

We employ a simple model of SMC looping with one-sided extrusion and a 4 second residence time, using the methodology of Bonato and Micheletto, as implemented by Gilbert et al. Loop extrusion by an SMC dimer involves one domain anchoring to the chromosome while another domain acts as a hinge that extrudes DNA while the anchor remains anchored in place on the chromosome. At the start of each 4 second hook interval, anchor beads are selected randomly and uniformly across the chromosome, emulating SMC binding non-specifically with the DNA. Hinge beads are selected 6 beads away from the anchor in a random direction along the polymer. Anchor and hinge pairs are connected by harmonic bonds $U _ { \mathrm { \small l o o p } } = \textstyle \frac { 1 } { 2 } k _ { \mathrm { \small l o o p } } ( d - d _ { 0 } ) ^ { 2 }$ where $k _ { I o o p }$ is the loop stiffness and $d _ { 0 }$ is the preferred loop size. For our simulations, $d _ { 0 }$ is set to 4r<sub>DNA</sub> and $k _ { \mathsf { l o o p } }$ is set to $0 . 3 3 k _ { B } T .$ . Anchor-hinge bonds are relaxed by sequence of two energy minimizations; the first with harmonic bonds between DNA beads, and the second with FENE bonds between DNA beads. Every $0 . 4$ seconds (ten times every 4 second hook interval), the hinge beads are updated by the SMC step size, which we take to be Poisson distributed with a mean of 20 beads and truncated at a maximum of 30 beads. The step size of roughly 200 bp, and step frequency of 1 per 0.4 seconds, are based on values observed from in vitro experiments of yeast condensin, where the rate of loop extrusion by SMC complexes was observed to take place at rates up to 600 bp/s, with individual step sizes of the complex having a median around 200 $\mathsf { \Delta } \mathsf { b } \mathsf { p } . { } ^ { 2 5 , 2 6 }$ When choosing the new hinge bead, only beads whose distance from the anchor is less than 50 nm (roughly the size of a fully extended SMC complex) are considered. In btree\_chromo, SMC looping is performed by calling the function simulator\_run\_loops. For each 0.4 s biological time interval, we run 10000 BD steps, corresponding to 1 μs of simulated time.

This study employed simplified SMC–SMC and SMC–replisome interaction dynamics. SMC proteins were allowed to extrude past one another, but Hi-C data from B. subtilis are best reproduced by simulations in which SMCs can block each other and, in some cases, facilitate each other’s unloading.<sup>58</sup> Similarly, extrusion past replication forks was prohibited in our model, although there is evidence that occasional bypassing occurs.<sup>59</sup> We also do not explicitly model interactions between SMC and RNA polymerase, although RNAP can act as a moving barrier that significantly impedes SMC extrusion at highly transcribed operons.<sup>60</sup> Additionally, we assumed a fixed dwell time of 4 second and assume that all SMCs remain bound during that 4 second dwell time. The binding and unbinding kinetics of SMC proteins remain poorly characterized, but it is likely that the actual dwell time exceeds 4 seconds and that only a fraction of SMCs are bound at any given time. Finally, while SMC proteins extrude unidirectionally in our model, recent studies have shown that SMCs can switch direction, effectively acting as two-sided extruders,<sup>61</sup> and simulations incorporating two-sided extrusion, rather than one-sided, better reproduce the juxtaposition of bacterial chromosomal arms.<sup>78</sup>

## Partitioning of Daughter Chromosomes

Fluorescence imaging in this study shows that daughter chromosomes are spatially segregated into distinct cell volumes by the onset of FtsZ-ring constriction, indicating that partitioning occurs rapidly following replication. Since the precise mechanisms underlying chromosome partitioning remain unknown, we treat partitioning as a geometric constraint in our model by applying a repulsive force between daughter DNA strands to ensure segregation into distinct daughter volumes. We applied a repulsive partitioning force of magnitude 12 pN (corresponding to 5k<sub>B</sub>T=1:7 nm), active for each of the 10000 × 0.1 ns BD timesteps during each loop cycle of 0.4 biological seconds. In btree\_chromo, this force can be toggled using the command switch\_fork\_partition\_repulsion:T. This force was applied only to already-replicated DNA and restricted to a spherical region of 2000 A<sup>˚</sup> centered between the daughter cells. A 12 pN force is applied to every DNA bead in each daughter chromosome, directed along the unit vector connecting their centers of mass. This vector is computed at the beginning of each 0.4 s interval, and the forces are applied in opposite directions to drive segregation. It was deactivated (switch\_fork\_partition\_repulsion:F) once chromosomes were fully partitioned (i.e., both chromosomes had passed the mid-plane and entered their respective daughter volumes), which prevented the partitioned chromosomes from being pressed against opposite sides of the cell.

The 12 pN partitioning force used in our simulations exceeds thermal forces, which are typically considered to be below 10 pN.<sup>79</sup> However, because we apply frequent energy minimizations and simulate only 1 μs of Brownian dynamics for each 0.4 seconds of biological time, the force magnitude is decoupled from real-time dynamics. In our simulations, the partitioning force serves as a constraint to ensure reliable separation of the daughter chromosomes into their respective cellular volumes without inducing excessive compaction at the cell poles, and does not represent a quantitatively calibrated value based on the underlying physics or biological mechanisms.

## Omission of Potential Biological Mechanisms Contributing to Partitioning

It is still not fully understood which mechanisms contribute to chromosome segregation and partitioning in various cellular contexts. Proposed drivers include SMC- and topoisomerase-mediated loop extrusion and disentanglement, and entropic forces.<sup>30,80</sup> Although our simulations explicitly model SMC complexes and topoisomerases, they lack sufficient Brownian dynamics (BD) timesteps to capture entropic segregation, were it to occur. The ‘‘fork partition force’’ discussed above emulates daughter-daughter repulsion that could arise from entropic effects. To further complicate things, recent findings suggest that entropic forces may hinder, rather than promote, segregation in some contexts,<sup>81</sup> underscoring the need for out-of-equilibrium dynamics.

BLAST searches of the Syn3A genome indicate that it lacks a ParABS system, as it does not contain genes encoding either ParA or ParB, nor does it possess complete signature parS sites. The ParABS system, which is present in Bacillus subtilis and Caulobacter crescentus, promotes chromosome alignment and segregation by preferentially loading SMC at parS sites near the origin of replication.<sup>57</sup> In E. coli, the SMC complex MukBEF loads preferentially on newly replicated DNA and is excluded from the Ter region by the MatP/matS system,<sup>82</sup> and the Min system aids in chromosome partitioning through MinD mediated transient DNA-membrane tethering events,<sup>56</sup> neither of which we were able to identify in Syn3A. We were also unable to identify genes encoding PopZ and TipN, which, in C. crescentus, function alongside the ParABS system to anchor the chromosome to the membrane and facilitate partitioning.<sup>83</sup> In Mycoplasma pneumoniae, super-resolution imaging suggests anchoring of the Ter-proximal region of the DNA to the attachment organelle.<sup>84</sup> Not only does Syn3A lack orthologs of genes for chromosome-partitioning proteins, but cryo-electron tomograms of Syn3A also show no visible attachment organelle or analogous structures.<sup>21</sup> In contrast, cryo-ET of M. pneumoniae shows a distinct membrane-associated attachment organelle.<sup>45</sup> In the minimal cell, there is no evidence of preferential loading or unbinding for SMC, nor has there been direct observation of DNA-membrane anchoring. As part of our efforts to model partitioning mechanisms, we tested an origin-origin repulsive force inspired by DNA-membrane tethering systems found in other bacteria but this had negligible impact on partitioning and was not pursued further. We also did not model transcription-translation coupling, although it could plausibly assist in partitioning through functioning as DNA-membrane tethering. It has also been proposed that contributions from polysomes may aid in chromosome partitioning.<sup>85</sup> As discussed earlier, polysomes were not included in our model.

## Omission of the Twisting Potential

In contrast to Gilbert et al., we do not include a twisting potential in our representation of the DNA polymer. Although supercoiling plays a critical role in genetic information processing by regulating transcription and influences chromosome conformation through the transient formation of localized writhe in the form of plectonemes, given the coarse-grained resolution of our model (10 nm cubes), the effects of supercoiling are expected to have a small affect on the chromosome conformation when projected onto the lattice. Consequently, we do not explicitly model supercoiling generated by complexes such as SMC-ScpAB, DNA gyrase, RNA polymerase, or DNA polymerase. Furthermore, the 1 kb resolution 3C-Seq contact map that we have for Syn3A indicates that there is no persistent supercoiling, meaning that if plectonemes do form, they must be transient and rapidly resolved.<sup>21</sup>

The Kokkos package, described below, does not currently support the polytorsion potential used in the Gilbert et al. methodology, which used aspherical particles and quaternions to represent the DNA beads as rigid bodies. Additionally, energy minimizations in LAMMPS do not adjust quaternions, meaning torsional degrees of freedom remain fixed during minimization. While it is possible to reintroduce torsional angles using dihedral interactions with phantom beads, this approach was not pursued in the current study to maintain computational efficiency while focusing on large-scale chromosomal organization.

## GPU Acceleration

Simulations were conducted using LAMMPS with the Kokkos package to leverage GPU acceleration. The Kokkos backend allowed efficient parallelization of Brownian dynamics and energy minimizations. For this study, custom Kokkos versions for fix brownian and fix addforce were written, based off of the existing Kokkos versions of fix langevin and fix setforce already in LAMMPS. For our system size of approximately 100K beads, using LAMMPS with Kokkos on the Delta A100 GPUs improved performance by about a factor of 10 compared to CPU-only execution.

## Communicating Chromosomes Between LM and LAMMPS

The state of the DNA on the LM RDME lattice depends directly on the BD chromosome state, but also communicates cell state information to the LAMMPS simulations. In the direction of the chromosome model to the RDME, the coordinates of the 10 bp beads determine the lattice sites in the RDME that are assigned the ‘‘DNA’’ site type and determine where chemically active particles (e.g. gene start sites, the origin of replication particle) are located on the lattice. Reassigning the site types first involves reassigning all intracellular lattice sites that were previously DNA to cytoplasm. Subsequently, each lattice site containing any monomers from the new chromosome configuration are assigned as a DNA lattice site. Following the site type update, chemically relevant DNA particles are moved on the lattice. Based on their positions in the genome, corresponding particles in the chromosome configuration are mapped to individual 10 bp particles. Their current state (e.g. whether a gene has an RNAP bound or not) and position is checked on the RDME lattice and that particle is deleted. A particle in the same chemical state is then placed in the lattice site containing the 10 bp bead corresponding to that particle’s position in the genome. Communication with the membrane boundary is discussed in the morphology Methods.

We determine the communication time to the chromosome based on the loop extrusion rate of SMC. As mentioned above, we selected to communicate with the chromosome to update their positions every 10 loop extrusion steps, corresponding to 4 seconds of biological time. As input to btree\_chromo, we count the instantaneous number of SMC proteins and use that information to determine the total number of loops that are simulated. This number is calculated simply as half of the number of proteins from the gene smc/0415, rounded down, and is written to the input file of btree\_chromo as the integer loop count in the function simulator\_run\_loops. At the communication time, once the information is communicated from the BD chromosome model to the 4DWCM, the next 4 s of biological time are set to run as a background process on a second GPU using the Python subprocess.Popen functionality. Running as a background process on a second GPU means that the rest of the 4DWCM can continue with the chromosome dynamics being calculated in parallel, eliminating a wait time of 2-5 minutes per 4 seconds of biological time. As discussed below, updating division morphologies are instead performed serially.

## DNA Replication

We previously simulated DNA replication in the stochastic well-stirred kinetics where replication forks work read through entire genes all-at-once.<sup>1</sup> Because the BD chromosome structure is at a resolution of 10 bp, we also increased the resolution of replication kinetics to 10 bp increments. The replication forks independently traverse the opposite arms of the mother chromosome while replicating the DNA, with beads for the left and right daughter chromosomes appearing in locations centered about the location of the mother’s corresponding bead, consistent with the so-called ‘‘train-track’’ model.<sup>30</sup> As a simplification, we assume that both the leading and lagging strands are replicated simultaneously. The replication topology (the position of the replication forks at 10 bp resolution) is tracked explicitly in the BD chromosome model. Using this information, we calculate the rate of replication in front of each replication fork independently. We continue to use the replication rate of 100 bp/s,<sup>38</sup> and the chromosome state is updated in the RDME at an interval of 4 seconds, meaning the maximum amount of replication per fork per communication is 400 bp. We determine the rate of replication given the instantaneous pools of dNTPs using the template-driven, enzyme catalyzed rate form for DNA replication<sup>86</sup> (excluding the binding step)

$$
V _ { \mathrm { D N A \ r e p l i c a t i o n } } = \frac { 1 0 0 \mathrm { b p } / s } { \frac { K _ { D 1 } K _ { D 2 } } { \left[ \mathrm { d N T P } _ { 1 } \right] \left[ \mathrm { d N T P } _ { 2 } \right] } + \sum _ { i } N _ { i } \frac { K _ { D i } } { \left[ \mathrm { d N T P } _ { i } \right] } + 4 0 0 \mathrm { b p } - 1 }\tag{Equation 6}
$$

where the input sequence is the 400 bp in front of the respective replication fork. Other variables are described in greater detail below. Using the instantaneous dNTP pools from the metabolism as input, the polymerization rate gives us an instantaneous rate of replication that determines the number of base pairs (divided by 10 to determine the number of Brownian dynamics beads) that are replicated at the communication time. In btree\_chromo we update the replication state using the transform function whose input variables are the number of DNA beads to add at each replication fork using the train-track model described above. Because the chromosome state in the RDME is read directly from the state in the BD simulation, we do not need to manipulate the replication state on the RDME lattice.

## Chemical Reaction Models

## Metabolism

The set of metabolic reactions remains unchanged from the well-stirred model simulated in Thornburg et ${ \mathsf { a l . } } ^ { 1 }$ The systems biology markup language (SBML) reaction model is read into the model using cobrapy to set the reaction set and stoichiometries. We store kinetic parameters in an Excel file (see Table S2) that has forward and reverse catalytic rate constants, a Michaelis-Menten constant for each substrate and product, and an enzyme annotation for each metabolic reaction. The complete set of kinetic parameters for the metabolic reactions along with the free energy calculations for central, nucleotide, and lipid metabolism are provided in the the supplemental information. The changes in parameters from the previous model are described below.

In glycolysis, we increased the forward rate of the fructose bisphosphate aldolase reaction (FBA) from $2 1 . 0 \mathsf { s } ^ { - 1 } \mathsf { t o } 6 4 . 5 \mathsf { s } ^ { - 1 }$ , both of which are reported values in ${ \mathsf { B R E N D A . } } ^ { 6 5 }$ Two parameters were changed in the phosphorelay reactions for glucose uptake. First, we increased the rate of PtsI binding to phosphoenolpyruvate (PEP) (reaction GLCpts0) from $\mathsf { 6 } , \mathsf { 0 0 0 \mathsf { m M } ^ { - 1 } s ^ { - 1 } }$ to $1 0 , 0 0 0 \mathsf { m } \mathsf { M } ^ { - 1 } \mathsf { s } ^ { - 1 }$ . Both of these values come from kinetic measurements performed on the same protein in $\bar { E } . c o l i . ^ { 8 7 }$ We also increased the rate of PtsG taking up and phosphorylating a glucose molecule (reaction GLCpts4) from 0.88 mM $^ { - 1 } \mathsf { s } ^ { - 1 } \mathsf { t o } \mathsf { 1 } . 2 9 \mathsf { m } \mathsf { M } ^ { - 1 } \mathsf { s } ^ { - 1 }$ The new rate constant was calculated from the glucose uptake rate measured in M. pneumoniae with the corresponding PtsG proteomics count and external glucose concentration.<sup>51</sup>

$$
k _ { F } ~ = ~ { \frac { 1 8 , 0 0 0 / s / \left( N _ { A } V _ { M , p n e u m o n i a e } \right) } { 2 5 1 \mathrm { { P t s G } } / \left( N _ { A } V _ { M , p n e u m o n i a e } \right) \times 1 0 9 ~ { \mathrm { g l u c o s e } } / L / \left( 1 8 0 g / \mathsf { m o l } \right) } } ~ = ~ 1 . 2 9 \mathsf { m M } ^ { - 1 } s ^ { - 1 }\tag{Equation 7}
$$

The combination of increased glucose uptake and increased rate of the FBA reaction resulted in all cells surviving for the entire cell cycle. We chose to simulate the set of parameters in which more cells are healthy to demonstrate that there is a solution to the set of parameters in which the entire population of simulated cells is healthy. In the absence of a measured death rate for Syn3A, it is unclear which parameter set better mimics the real cell fates of Syn3A.

The other metabolic parameters changed were the uptake rates of (deoxy)nucleosides. In our previous well-stirred model, we observed excess build-up of (d)NTPs. We do not account for inhibitory mechanisms in the metabolic kinetics, which could result in sufficient uptake rate reductions such that the cell does not build up excess pools of nucleotides. In the absence of inhibition, we instead reduce the following uptake rates: adenosine, guanosine, uridine, deoxyadenosine, and deoxyguanosine uptake rates were reduced from $2 . 0 , 1 . 0 , 2 . 0 , 1 . 5 ,$ and $1 . 0 { \mathsf { s } } ^ { - 1 }$ to 1.5, 0.5, 1.5, 1.0, and $0 . 5 { \mathsf { s } } ^ { - 1 }$ , respectively. Don!

## Replication Initiation

Replication initiation as previously simulated in the well-stirred stochastic kinetics representation. With spatially-localized DNA particles, we now move this set of reaction to the RDME representation. The following reactions are based strongly off of our previous reaction models.<sup>1,42</sup> In transcription, RNAP particles diffuse to chemically-active promoter particles on the RDME lattice whose positions follow their respective monomer in the BD chromosome. Similarly, we will treat the origin (oriC) as a single RDME particle whose position follows the origin monomer in the BD chromosome. Although the replication initiation conglomeration will be larger than the size of a single 10 nm lattice site, the replication initiation protein will only look for a single position relative to the origin at any one time. Therefore, we assume that because we are not concerned with the excluded volume of the origin that we can represent the origin as a single particle that undergoes many state changes as proteins bind. The protein responsible for initiating bacterial DNA replication is DnaA. DnaA has two DNA-binding domains: domain IV to double-stranded DNA and domain III to single-stranded DNA. Replication initiation begins by a single DnaA protein binding to a 9/9 consensus sequence (TTATCCACA) with a high affinity (HA) near oriC. In our model this is modeled as a single binding reaction:

$$
\mathrm { o r i C } + \mathsf { D n a A } \to \mathrm { o r i C \_ H A \_ D n a A } , k _ { \mathrm { b i n d } } ^ { \mathsf { D n a A , H A } } = 7 . 8 \times 1 0 ^ { 6 } M ^ { - 1 } s ^ { - 1 }\tag{Equation 8}
$$

We assume that this binding is irreversible. Following the first DnaA, there are two nearby 7/9 consensus sequences within 5 bp of the HA site. We assume that DnaA binding to these with its dsDNA binding domain with a low affinity (LA). We assume that the order of binding to these two sites does not matter and that the DnaA will bind irreversibly to them one after the other.

$$
\mathsf { o r i C \_ H A _ { \_ } D n a A } + \mathsf { D n a A } \to \mathsf { o r i C _ { \_ } L A 1 _ { \_ } D n a A } , k _ { \mathrm { b i n d } } ^ { \mathsf { D n a A , L A } } = 3 . 5 \times 1 0 ^ { 4 } M ^ { - 1 } s ^ { - 1 }\tag{Equation 9}
$$

$$
\mathsf { o r i C \_ L A 1 \_ D n a A } + \mathsf { D n a A } \to \mathsf { o r i C \_ L A 2 \_ D n a A } , k _ { \mathrm { b i n d } } ^ { \mathsf { D n a A , L A } } = 3 . 5 \times 1 0 ^ { 4 } M ^ { - 1 } s ^ { - 1 }\tag{Equation 10}
$$

Following the first three DnaA bound to the dsDNA sites near oriC, we assume that a small amount of torque is applied to the DNA opening up a small amount of ssDNA in the known AT-rich region directly neighboring the dsDNA binding sites.<sup>42</sup> DnaA is known to bind cooperatively and also to ssDNA, so we simulate the remainder of replication initiation as a reversible polymerization reaction where DnaA bind to the end of the filament along the DNA one DnaA at a time. These reactions follow the scheme

$$
\mathrm { o r i C \_ s s D N A \_ D n a A _ { \varepsilon } } + \mathrm { D n a A } \to \mathrm { o r i C \_ s s D N A \_ D n a A _ { \varepsilon + 1 } } , k _ { \mathrm { o r i n } } ^ { \mathrm { D n a A , s s D N A } } = 1 4 0 \mathsf { m M } ^ { - 1 } \bar { s } ^ { - 1 }\tag{Equation 11}
$$

$$
\mathrm { o r i C _ { - } s s D N A _ { - } D n a A _ {  } o r i C _ { - } s s D N A _ { - } D n a A _ {  - 1 } + D n a A _ { , } k _ { o f f } ^ { D n a A , s s D N A } = 0 . 4 2 s ^ { - 1 } }\tag{Equation 12}
$$

where i is the number of DnaA bound to the ssDNA (excludes the 3 bound to dsDNA). Based on the length of the AT-rich region, we assume that the filament can consist of up to 30 DnaA. However, while DnaA is the initiation protein, its responsibility is to open the origin so that the replication machinery can be loaded. The final reaction of replication initiation is the loading of the replisome. Based on the size of a complete replisome as the most conservative estimate, we assume that the machinery can be loaded once there are 20 DnaA in the filament so that a large enough pocket of ssDNA has been formed. A minimum of 20 corresponds to roughly 20 nm of linear DNA. Based on a molecular reconstruction of a bacterial replisome (PDB: 5IKN),<sup>88</sup> we assume 20 nm of linear DNA is sufficient to load the first replisome. We simulate the replisome loading reaction using a representative protein, DNA helicase DnaB. We assume that if the DnaB finds an unwound origin, it will be immediately recruited to assist in replication, so we simulate the binding as a set of fast reactions

$$
\mathsf { o r i C \mathrm { _ { - } S s D N A _ { - } D n a A _ { + } } } + \mathsf { D n a B \to o r i C _ { \mathrm { i + 1 } } } . \mathsf { D n a B } , k _ { \mathrm { b i n d } } ^ { \mathsf { D n a B } } = \mathsf { 1 } . 0 \times 1 0 ^ { 7 } \mathsf { m M } ^ { - 1 } \mathsf { s } ^ { - 1 }\tag{Equation 13}
$$

where i is the number of DnaA in the filament ranging from 20 to 30. We keep the number of DnaA in the species name so that we can track the number of DnaA bound to oriC at the time of replication initiation. We assume that two replisomes are required, so oriC undergoes this reaction twice. However, once a single DnaB binds, we assume that the state of the origin particle is irreversible and also that no more DnaA need to bind.

In the phase of replication initiation when DnaA are forming a filament along ssDNA, we first used the parameters from our previous well-stirred model: $\mathsf { 1 0 0 m M ^ { - 1 } s ^ { - 1 } }$ for binding and $0 . 5 5 { \mathsf { s } } ^ { - 1 }$ for the on and off rate, respectively.<sup>1,42</sup> In early testing, we found that these rates were not sufficient to initiate replication in the 4D model. The spatial localization adds the restriction that DnaA must diffuse to the oriC particle, affecting the overall rate of polymerization of DnaA. The new rates favor stronger binding of DnaA to ssDNA: $1 4 0 \mathsf { m } \mathsf { M } ^ { - 1 } \mathsf { s } ^ { - 1 }$ for binding and $0 . 4 2 { \sf s } ^ { - 1 }$ . Both sets come from the same single molecule FRET study.<sup>50</sup> The original parameters represent the average values measured in the experiments and the new parameter set represents a set with a bias toward stronger DnaA binding when the ssDNA is preceded by dsDNA containing the strong and intermediate signatures.

## Transcription of mRNA and tRNA, Translation and mRNA Degradation

The transcription, translation, and degradation reactions were modeled as binding events between macromolecular polymers (DNA, mRNA) with their respective machinery (RNA Polymerase, Ribosome, and degradosome), followed by (de)polymerization reactions. Binding in the RDME occurs when the molecules diffuse into the same lattice cube and subsequently interact. These reaction kinetics are implemented similarly to our previous model,<sup>1</sup> which provides a detailed account of the underlying methods. Here, we briefly summarize the methods and focus on key changes introduced in the present work.

The binding rates of polymers and corresponding macromolecular machinery were estimated based on the frequency of the binding events reported for E. coli; each case will be discussed individually below. The stochastic binding reactions follow a simple bimolecular form (A+B to C). In the RDME (Equation 1), the propensity a<sub>r</sub>, which quantifies the probability per unit time that reaction r will occur, is calculated for a second order binding reaction as $\frac { k _ { \mathrm { { b i n d } } } n _ { A } n _ { B } } { N _ { A } V } ,$ , where $k _ { \mathrm { b i n d } }$ is macroscopic binding rate reported in units of $M ^ { - 1 } s ^ { - 1 } , \boldsymbol { n } _ { A }$ and $n _ { B }$ are the absolute counts of molecules A and B respectively, $N _ { A }$ is Avogadro’s constant, and V is the volume. Over long times, the average number of reaction events per unit time equals the time-averaged propensity, and we approximated the propensity by the observed frequency of binding events. Rearranging, we obtain the formula for the macroscopic binding rate k<sub>bind</sub>:

$$
k _ { \mathrm { b i n d } } = \frac { \mathsf { f r e q u e n c y } \times N _ { A } \times V } { n _ { A } \times n _ { B } }\tag{Equation 14}
$$

The Hofmeyr rate form<sup>86</sup> is applied to catalyzed, template-directed polymerization of RNAs and proteins as described in our previous work.<sup>1</sup> For RNA synthesis (i.e. transcription elongation), the enzyme and template pair is RNAP and DNA, and for protein synthesis (i.e. translation elongation), the pair is ribosome and mRNA. The formula for the Hofmeyr rate—excluding the step where the enzyme binds to the template polymer—takes the form:

$$
V _ { \mathrm { p o b y m e r i z a t i o n } } = \frac { k _ { \mathrm { c a t } } } { \frac { K _ { D 1 } K _ { D 2 } } { \left[ \mathsf { M o n o m e r } _ { 1 } \right] \left[ \mathsf { M o n o m e r } _ { 2 } \right] ^ { + } \sum _ { i } N _ { i } \frac { K _ { D i } } { \left[ \mathsf { M o n o m e r } _ { i } \right] ^ { + } } k _ { \mathrm { \sf { p o b y m e r } } } - 1 } N _ { \mathrm { t e m p l a t e , p o b y m e r } } } ,\tag{Equation 15}
$$

Here, $k _ { \mathrm { c a t } }$ is the intrinsic elongation speed of enzyme on the template in units of length (bp/nt/aa) per second. $N _ { j }$ is the number of monomers of type i in the product polymer. $K _ { D , j }$ are the dissociation constants of monomers of type i in the polymer (e.g. ATP, CTP, UTP, and GTP for transcription). The concentrations of monomers are dynamic over the cell cycle, and shortages—which occur if consumption overtakes synthesis—can slow or in some cases even halt chain elongation. For transcription, the monomers are NTPs with $K _ { D , \mathsf { N T P } }$ of 0.1 mM, and for translation, monomers are aa:tRNAs with $K _ { D , \tt a a a : t R N A }$ of $1 \ \mu \mathsf { M } .$ 42

First, we describe the parameterization for transcription reactions, starting with the transcription of tRNA-coding genes. Due to the lack of measurements for RNAP binding with tRNA-coding genes, we instead take the value measured for rRNA-coding genes. We use the values of 10 initiations of transcription of rRNA genes per minute and 11,400 RNAP molecules in a single E. coli as measured by Bremer and Dennis<sup>41</sup> The volume of a single E. coli cell is taken as 1fL, so the binding rate between tRNA genes with RNAP $k _ { \mathrm { b i n d } } ^ { \mathrm { r R N A g e n e s : R N A P } }$ was calculated as

$$
{ k _ { \mathrm { b i n d } } ^ { \mathrm { r P N A g e n e s . R N A P } } } \ = \ { \frac { \displaystyle { \frac { 1 0 } { 6 0 } } \times V _ { E . c o l i } \times N _ { A } } { \displaystyle { 1 1 4 0 0 } } } = 8 . 8 \times 1 0 ^ { 3 } { M ^ { - 1 } } { s ^ { - 1 } }\tag{Equation 16}
$$

Thus, the binding between tRNA-coding genes with RNAP occurs via

$$
{ \mathsf { R N A P } } + G _ { \mathsf { t R N A } } \to { \mathsf { R N A P } } : G _ { \mathsf { t R N A } } , k _ { \mathsf { b i n d } } ^ { \mathsf { t R N A } } { \mathsf { \_ g e n e s s : } } { \mathsf { R N A P } } = { \mathsf { 8 . 8 \times 1 0 } } ^ { 3 } M ^ { - 1 } s ^ { - 1 }\tag{Equation 17}
$$

The elongation speed of RNAP on tRNA-coding genes is taken as 85 nt per second, which is the value measured for RNAP on rRNA-coding genes in E. coli.<sup>41</sup> The elongation occurs via

$$
\mathsf { R N A P : } G _ { \mathsf { t R N A } } \to \mathsf { t R N A } + \mathsf { R N A P } + G _ { \mathsf { t R N A } } , V _ { \mathsf { p o l y r m e r i z a t i o n } } ^ { \mathsf { t r a n s c r i p t i o n , t R N A } }\tag{Equation 18}
$$

$$
V _ { \mathrm { p o n s l a t i o n , t R M A } } ^ { \mathrm { t r a n s l a t i o n , t R M A } } = \frac { 8 5 \ : \mathsf { n t / s } } { \frac { K _ { D 1 , \mathrm { N T P } _ { 1 } } K _ { D 2 , \mathrm { N T P } _ { 2 } } } { [ \mathsf { N T P } _ { 1 } ] [ \mathsf { N T P } _ { 2 } ] } + \sum _ { i } N _ { i } \frac { K _ { D i , \mathrm { N T P } _ { i } } } { [ \mathsf { N T P } _ { i } ] } + L _ { \mathrm { t R N A } } - 1 } N _ { \mathrm { R M P : G _ { i } \times \mathsf { n t } } } ,\tag{Equation 19}
$$

A promoter strength S<sup>locusNum</sup> was introduced as a prefactor at the transcription level to distinguish the expression strengths of the 455 different mRNAs. It was incorporated into both the binding and the elongation reactions to account for variations in both RNAP binding affinity and transcription elongation speed. Promoter strengths were scaled according to the absolute protein counts,<sup>1</sup> using the formula

$$
S _ { \mathrm { p r o m o t e r } } ^ { \mathrm { l o c u s N u m } } = \frac { \mathsf { l n i t . P t n . C n t . } } { 1 8 0 } ,\tag{Equation 20}
$$

where 180 is the average count of the 455 mRNA-coding proteins, and the initial protein count as described in the section initial conditions. Ribosomal proteins use proxy promoters strengths corresponding to 500 proteins if their experimental proteomics value was less than 500. If their experimental proteomics count is greater than 500, that value is used instead.

was scaled as

$$
k _ { \mathrm { b i n d } } ^ { \mathrm { m R N A g e n e s ; R N A P } } = 8 . 8 \times 1 0 ^ { 3 } \times \frac { 2 0 } { 8 5 } = 2 . 1 \times 1 0 ^ { 3 } M ^ { - 1 } s ^ { - 1 } ,\tag{Equation 21}
$$

since the average elongation speed of RNAP on protein encoding genes is taken as 20 nt/s. 89

The binding rate of RNAP with each unique gene $k _ { \mathrm { b i n } } ^ { G _ { - } }$ <sup>locusNum:RNAP</sup> is d

$$
\mathrm { R N A P } + G _ { \mathrm { m R N A } } ^ { \mathrm { i o c u s N u m } }  \mathrm { R N A P : } G _ { \mathrm { m R N A } } ^ { \mathrm { l o c u s N u m } } , k _ { \mathrm { b i n d } } ^ { G \mathrm { - l o c u s N u m : R N A P } } = S _ { \mathrm { p r o m e t e r } } ^ { \mathrm { l o c u s N u m } } k _ { \mathrm { b i n d } } ^ { \mathrm { m R N A g e n e s : R N A P } }\tag{Equation 22}
$$

The elongation speed of ${ \mathsf { R N A P } }$ on mRNA-coding genes is assumed to scale linearly with the promoter strength S<sup>locusNum</sup> as

$$
\mathsf  R N A P : \mathsf { G } _ { \mathsf { m R N A } } ^ { \mathsf { l o c u s N u m } } \to \mathsf { m R N A } + \mathsf { R N A P } + \mathsf { G } _ { \mathsf { m R N A } } ^ { \mathsf { l o c u s N u m } } , V _ { \mathsf { p o l y m e r i z a t i o n } } ^ { \mathsf { t r a n s c r i p t i o n } , \mathsf { m R N A } }\tag{Equation 23}
$$

$$
V _ { \mathrm { p o b y m e n t i z a t i o n } } ^ { \mathrm { t r a n s l a t i o n , m R M A } } = \frac { \operatorname* { m i n } \left( 8 5 \mathrm { \ n t } \mathord { \left/ { \vphantom { \mathrm { \ n t } } } \right. \kern - delimiterspace } \mathrm { s } , \mathrm { S } _ { \mathrm { p r o m o t e r } } ^ { \mathrm { l o c u s N u m } } \times 2 0 \mathrm { \ n t } \mathord { \left/ { \vphantom { \mathrm { \ n t } } } \right. \kern - delimiterspace } \mathrm { s } \right) } { K _ { D 1 , \mathrm { N T P } _ { 1 } } K _ { D 2 , \mathrm { N I P } _ { 2 } } } + \sum _ { i } N _ { i } \frac { K _ { D i , \mathrm { N T P } _ { i } } } { [ \mathsf { N T P } _ { i } ] } + L _ { \mathrm { m R N A } } - 1 \mathrm { \ n t } _ { \mathrm { m e } ; \mathrm { G } _ { \mathrm { m R M A } } ^ { \mathrm { l o c u s N u m } } }\tag{Equation 24}
$$

Translation was conducted in a similar fashion as transcription. Reported values for the mean time for translation initiation per mRNA vary widely, with a minimum of 1 second and median of 15 seconds.<sup>90</sup> In our model, we assume a translation initiation frequency of 40 events per minute. The number of ribosomes in slow-growing E. coli has been experimentally measured as 6800.<sup>91</sup>

$$
k _ { \mathrm { b i n d } } ^ { \mathrm { m R N A ; r i b o s o m e } } \ = \ { \frac { { \frac { 4 0 } { 6 0 } } \times V _ { E . c o l i } \times N _ { A } } { 6 8 0 0 } } = 5 . 9 \times 1 0 ^ { 4 } M ^ { - 1 } s ^ { - 1 }\tag{Equation 25}
$$

The translation speed was set to 12 aa/s.<sup>92</sup> The synthesis of proteins happens via the binding and elongation reactions

$$
\mathrm { R i b o s o m e + \ m R N A  R i b o s o m e : \ m R N A , } k _ { \mathrm { b i n d } } ^ { \mathrm { m R N A , r h o s o m e } } = 5 . 9 \times 1 0 ^ { 4 } M ^ { - 1 } s ^ { - 1 }\tag{Equation 26}
$$

$$
\mathsf { R i b o s o m e : m R N A \to R i b o s o m e + m R N A + p r o t e i n , v _ { p o l y m e r i z a t i o n } ^ { t r a n s l a t i o n } }\tag{Equation 27}
$$

$$
V _ { \mathrm { p o b y m e r i z a t i o n } } ^ { \mathrm { t r a n s l a t i o n } } = \frac { 1 2 { \mathrm { a a } } / s } { \frac { K _ { D 1 , t \mathrm { R N A } _ { 1 } } K _ { D 2 , \mathrm { t R N A } _ { 2 } } } { \left[ \left[ \mathrm { R N A } : { \mathrm { a a } } _ { 1 } \right] \left[ \mathrm { t R N A } : { \mathrm { a a } } _ { 2 } \right] ^ { + } \right] ^ { N _ { i } } \left[ \mathrm { t R N A } : { \mathrm { a a } } _ { i } \right] } + L _ { \mathrm { p r o t e i n } } - 1 }\tag{Equation 28}
$$

Finally, we describe the parameterization of mRNA degradation. The degradosome is localized in the peripheral membrane region via its scaffold RNase Y, which anchors the complex through its N-terminal transmembrane helix embedded in the membrane.<sup>93</sup> Therefore mRNA must diffuse to the periphery in order to bind with the degradosome. The binding rate between mRNA and degradosome $k _ { \mathrm { b i n d } } ^ { \mathsf { m R N } }$ <sup>A:degradosome</sup> is estimated based on the observed value of 11 cleavage events of RNase E per minute per RNase E,<sup>94</sup> and 7800 mRNAs<sup>95</sup> measured in E. coli.

$$
k _ { \mathrm { b i n d } } ^ { \mathrm { m R N A : d e g r a d o s o m e } } = \frac { \displaystyle \frac { 1 1 } { 6 0 } \times V _ { E . c o l i } \times N _ { A } } { 7 8 0 0 } = 1 . 4 \times 1 0 ^ { 4 } M ^ { - 1 } s ^ { - 1 }\tag{Equation 29}
$$

The degradation rate of an mRNA polymer chain was considered constant over the length of the chain,<sup>1</sup> with the speed taken to be 88 nt $/ \mathsf { s } . ^ { \bar { 9 6 } }$ The product of mRNA degradation is a collection of nucleotide monophosphates. The respective reactions are

$$
\mathrm { D e g r a d o s o m e } + \mathsf { m R N A } \to \mathrm { D e g r a d o s o m e } : \mathsf { m R N A } , k _ { \mathrm { b i n d } } ^ { \mathsf { m R A } \times \mathsf { d o s o m e } } = 1 . 4 \times 1 0 ^ { 4 } M ^ { - 1 } s ^ { - 1 }\tag{Equation 30}
$$

$$
\mathsf { D e g r a d o s o m e : m R N A } \to \mathsf { D e g r a d o s o m e } + \sum _ { i } \mathsf { N M P } _ { i } , v _ { \mathrm { d e g r a d a t i o n } } ^ { \mathsf { m R M A } } = \frac { 8 8 \mathsf { n t / s } } { L _ { \mathsf { m R M A } } }\tag{Equation 31}
$$

ATP energizes bond formation in tRNAs and mRNAs and breaks down mRNAs at the expense of one ATP molecule per monomer. Two GTP molecules are required in protein chain elongation for each amino acid, one for the delivery of aa: tRNA to the A site, and another for the shift of the ribosome to the next codon.

Simultaneous Transcription of rRNA Genes by Multiple RNAP

While we do not handle polycistronic RNA/transcription of multiple genes in operonal structures, we found that we will never generate sufficient rRNA to double the number of ribosomes in a cell cycle unless we allow multiple RNAP to read the genes coding for rRNA simultaneously. We handle this in a manner similar to the origin particle for DNA replication initiation where we have single particles that undergo state changes that track the number of molecules associated with the particle. In this case, the gene particles associ ated with the rRNA genes undergo the state changes based on the number of RNAP transcribing the gene. We assume a RNAP spacing of 400 nt, so the 5S genes can only have one RNAP at a time, but the 16S and 23S genes can have up to 4 and 7 RNAP at once, respectively.

The kinetics are implemented as follows. On the RDME lattice, the genes start in free states where no RNAP are bound. Once an RNAP diffuses and binds to the gene particle through the reactions described above, the gene is switched to a state indicating that 1 RNAP is bound to the gene and that the start of the gene is occupied. In the global CME kinetics, the transcription reactions are not for the entire gene like all other genes. Instead, we transcribe the gene in increments of 400 nt. Once the RNAP has transcribed the first 400 nt of the gene, we switch the state of the gene particle on the RDME lattice to indicate that the start of the gene is now unoccupied even though there is an RNAP still actively transcribing downstream on the gene. This particle can now react with a second RNAP in the RDME to initiate a second simultaneous transcription event. In the global CME, the transcription of this RNAP is also simulated in increments of 400 nt. However, we restrict the transcription of the second RNAP so that it cannot pass the transcription state of the first RNAP. The resolution of this traffic is limited to 400 nt because of the resolution of the individual transcription reactions. So once the first RNAP advances to its next 400 nt increment, the second RNAP can advance past the start site, once again freeing the start site of the gene. Because of this implementation, we also allow for gaps in transcription because the timescale between transcription initiation reactions is stochastic. RNAP progress in 400 nt increments until the end of the gene where the last transcription elongation reaction in determined by the remaining length of the gene sequence. As mentioned above, we allow RNAP to initiate on rRNA genes until all 400 nt increments are fully occupied.

## RNAP and Degradosome Assembly

The assembly of RNAP and degradosomes were handled in a simple fashion. For the RNAP, we assumed the complete complex to be two alpha subunits rpoA/0645 and the two different beta subunits rpoB/0804 and rpoC/0803 (beta’). Our assembly assembly pathway assumes the two alpha units bind first, then the beta, and finally the beta’. For these reactions we assumed a fast binding rate of $1 0 ^ { 7 } \ M ^ { - 1 } { \mathsf { s } } ^ { - 1 }$ . The degradosome is a complex that consists of several proteins, some of which are metabolic proteins whose roles in the degradosome are unknown.<sup>97</sup> For this reason, we assume the assembly of a minimal number of proteins to constitute a ‘‘complete’’ degradosome: the scaffold protein and endoribonuclease RNase Y rny/0359 and an exoribonuclease RNase J1 rnjA/ 0600. The binding of these two proteins uses the same fast binding rate as the RNAP assembly reactions.

## Ribosome Assembly

Assembly of the ribosome is more complicated due to the tens of proteins and 3 rRNA species involved in the complex. We base our parameters on the assembly of the 30S small subunit (SSU) in E. coli. The kinetic parameters come from pulse-chase experiments.<sup>98,99</sup> In the kinetic model for ribosome biogenesis, we determined a hierarchical association of rproteins to the RNAs forming the small subunit. An assembly tree of intermediates at two different temperatures was constructed based on fluxes in the reactions of individual proteins/ribosomal RNA interactons.<sup>98,100</sup> The hierarchical pathways were consistent with the in vitro assembly map assigning primary, secondary, and tertiary rproteins.<sup>101,102</sup> Because of the tens of proteins involved in the complex, there are combinatorially many ways to assemble the SSU. Primary rproteins bind directly to the 16S rRNA and secondary and tertiary proteins bind once other proteins have bound. The number of assembly intermediates in the tree can be trimmed to enhance computational performance. An assembly tree of only 145 intermediates was obtained by choosing reactions that were observed to have flux above a predetermined threshold. We further reduced this branched tree to a linear pathway consisting of only 19 intermediates in which only one rprotein was added at a time. We found that the assembly time was not significantly affected in the volume of Syn3A with this reaction set, with assembly times still being less than 1 minute after a 16S rRNA is transcribed. We additionally found that the variations in diffusion coefficient for each intermediate throughout assembly did not significantly affect assembly time, so we have assigned uniform diffusion coefficients for all intermediates to the diffusion coefficients of their respective rRNA backbone. We also also assume a linear reaction scheme for the assembly of the 50S large subunit (LSU). This reaction scheme follows the binding order reported by in E. coli.<sup>99,103</sup> Because the rate constants for each binding reaction have not been as precisely quantified as the SSU assembly reactions, we assume two approximate binding rates: one weak binding rate $( 1 0 ^ { 4 } ~ \mathsf { M } ^ { - 1 } \mathsf { s } ^ { - 1 } )$ and one strong binding rate $( 1 0 ^ { 6 } \mathsf { M } ^ { - 1 } \mathsf { s } ^ { - 1 } )$ . These values were estimated from the orders of magnitude for weak and strong binding reactions in the SSU assembly. Whether a ribosomal protein (or the 5S rRNA) are a weak or strong binder was assigned using the weak/strong binding strength assignment in the LSU assembly maps for E. coli.<sup>99,103</sup> Syn3A’s genome codes for two rRNA operons. While the isolated rRNA particles are fully differentiable, we do not differentiate assembled ribosomes or SSU/LSU intermediates based on rRNA isoform.

## tRNA Charging

The reactions to charge tRNA are simulated in the global CME representations. We use the global CME because tRNA and aminoacyl tRNA synthetases (aaRS) are particles that are low in count whose states are dynamically changed by small molecules that are high in concentration and fast diffusers: ATP and amino acids. We assume a reaction scheme that begins with the aaRS binding with an ATP.

$$
a a R S + A T P  a a R S : A T P\tag{Equation 32}
$$

We then assume the aaRS:ATP complex binds with the corresponding amino acid.

$$
a a { \mathsf { R S } } : { \mathsf { A T P } } + { \mathsf { A A } }  a { \mathsf { a R S } } : { \mathsf { A T P } } : { \mathsf { A A } }\tag{Equation 33}
$$

We do not account for the possibility of the aaRS binding to the incorrect amino acid. The aaRS:ATP:AA then binds to an isoform of its respective tRNA.

$$
a a { \mathsf { R S } } : { \mathsf { A T P } } : { \mathsf { A A } } + { \mathsf { t R N A } }  a { \mathsf { a R S } } : { \mathsf { A T P } } : { \mathsf { A A } } : { \mathsf { t R N A } }\tag{Equation 34}
$$

Again, we do not allow for the aaRS to bind to the incorrect type of tRNA. While there are 20 tRNA types, Syn3A has redundant isoforms for some with a total of 29 tRNA-coding genes.<sup>42</sup> Finally, we simulate a conversion reaction where the aaRS releases the charged tRNA, an AMP, and a di-phosphate.

$$
a a \mathsf { R S } : \mathsf { A T P } : \mathsf { A A } : \mathsf { t R N A } \to \mathsf { A A } : \mathsf { t R N A } + a \mathsf { a R S } + \mathsf { A M P } + \mathsf { P P i }\tag{Equation 35}
$$

To communicate the costs of translation to the charged tRNA pools, we treat the cost counters like particles in the well-stirred global CME. Instead of simply subtracting the cost counters for translation from the charged tRNA pools, the cost particles undergo fast reactions with their respective charged tRNA to convert them into a ‘‘paid’’ state.

$$
A A : t R N A + C O S t \_ A A  t R N A + C O S t \_ A A  p a i d\tag{Equation 36}
$$

Because we are communicating the cumulative cost per biological second, the total cost of translation almost always exceeds the total amount of charged tRNA because we only have roughly 200 tRNA per isoform. If we were to use the method of subtracting the cost from the available pools, we would almost always artificially have remaining costs that are not paid. By allowing the cost counters to be paid one amino acid at a time through a fictitious reaction, the translational AA:tRNA costs are dynamically paid off every biological second.

There are two special cases in tRNA charging: the formylmethionine and glutamine tRNAs. For glutamine, the charging mechanism involves mischarging the tRNA with a glutamate and then replacing it with a glutamine.<sup>18</sup> Here, we instead simulate a lumped reaction that mimics the above charging mechanisms, but uses the glutamyl-tRNA amidotransferase protein in place of the aaRS. Accounting for the mischarging reactions explicitly would require a custom algorithm to track the mass balance of the aaRS and tRNA states. While this is possible, it is not a targeted interest in this model, so we chose to summarize its effects with a lumped reaction. We do not explicitly simulate the reaction to convert the charged MET:tRNA\_MET into FMET:tRNA\_MET. Instead, we account for the formylated methionine tRNA by accounting for its cost in two places: the MET:tRNA\_MET and the metabolite 10fthfglu3. We add the FMET:tRNA cost to the MET:tRNA cost to account for the use of the methionine in the global CME. To account for the formylation, we treat the substrate for the methionine-tRNA formyltransferase reaction (10fthfglu3) as the pool to pay for the cost and communicate with it in the same way we communicate with other metabolic pools.

## Diffusion

## Protein and RNA Diffusion

The diffusion rate of all cytoplasmic proteins is set to a conservative estimate of $1 \mu \mathsf { m } ^ { 2 } / \mathsf { s }$ given the dense crowding of Syn3A’s cytoplasm.<sup>21</sup> To account for excluded volume of DNA, the diffusion into DNA lattice cites for cytoplasmic proteins is reduced to $0 . 5 \mu \mathrm { m } ^ { 2 } / \mathsf { s }$ because we estimate that the DNA occupies roughly half a lattice site on average. For ribosome excluded volume, we assume that proteins can exit the center lattice site of ribosome projections, but are forbidden from re-entering the center sites. The remainder of the cross projection is a slight overestimate of the excluded volume, so we assume a reduced diffusion rate of $0 . 5 \mu \mathsf { m } ^ { 2 } ,$ <sup>2</sup>/s for proteins into and out of the cross. We assume a diffusion coefficient of $0 . 1 \ \mu \mathsf { m } ^ { 2 } / \mathsf { s }$ for transmembrane proteins. Cytoplasmic proteins are forbidden to enter the membrane lattice sites and transmembrane proteins are forbidden to leave membrane lattice sites. Peripheral membrane particles obey the same diffusion rates as cytoplasmic proteins. However, their locomotion is restricted so that once they diffuse into a peripheral membrane cytoplasmic lattice site, they stay in the peripheral membrane lattice sites (they do not re-enter the cytoplasm and cannot enter the membrane).

The diffusion coefficients of all RNA are calculated estimates based on hydrodynamic radius.<sup>104</sup> We used a modified version of the Stokes-Einstein relation where the diffusion coefficient can be approximated as

$$
D = \frac { k _ { B } T } { 6 \pi \eta R _ { H } }\tag{Equation 37}
$$

in which $\eta$ is the viscosity of the environment and the hydrodynamic radius can be approximated as

$$
R _ { H } = \biggl ( \frac { 3 m _ { m } L _ { \tt R N A } } { 4 \pi N _ { A } \rho } \biggr ) ^ { 1 / 3 } .\tag{Equation 38}
$$

The viscosity was previously estimated to be 1.2 PA⋅s from the diffusion coefficient of an mRNA in $E . c o l i . ^ { 1 , 1 0 5 }$ We assume a temperature T of 310 K, an average molar mass $m _ { m }$ of $3 3 7 \thinspace 9 \thinspace \mathsf { m o l } ^ { - 1 }$ per nucleotide, and a density ρ of $1 . 8 \mathsf { g c m } ^ { - 1 } .$ <sup>1</sup> With these values we calculate a length-dependent $( L _ { \mathsf { R N A } } )$ diffusion coefficient for every RNA. RNA particles are able to diffuse into any lattice site in the cytoplasm including DNA and ribosomes, but are forbidden from entering membrane lattice sites.

## RNAP and Degradosome Diffusion

Once protein complexes assemble, they are free to diffuse within their respective simulation space (e.g. degradosomes in the peripheral membrane and RNAP in the cytoplasm). Degradosomes and RNAP are assigned diffusion coefficients of $0 . 0 3 1 \ \mu \mathrm { m } ^ { 2 } / \mathsf { s }$ and $0 . 2 2 \ \mu \mathsf { m } ^ { 2 } / \mathsf { s }$ respectively and are assumed to fit into a single 10 nm lattice cube. Diffusion of degradosomes is restricted so that they cannot leave the peripheral membrane layer of the cytoplasm.

## Ribosome Diffusion

Ribosomes are roughly 20 nm in diameter, so they are considerably larger than a single 10 nm lattice cube and cannot be treated with normal diffusion in the RDME using 10 nm lattice cubes. To accurately represent a ribosome on the lattice, we utilize a center of mass particle around which we construct a 3D cross shape as shown in Figure S1. This projection of the ribosome is used to exclude the volume of the ribosome, influencing protein diffusion around ribosomes. The center of mass particle is also utilized as the reactive particle to initiate translation, so mRNA are allowed to diffuse into ribosome sites. Proteins are totally excluded from the center lattice site of the ribosome cross. The 7 lattice sites making up the ribosome lattice site projection overestimate the total volume of the ribosome, so we allow proteins to enter the exterior lattice sites of the cross at a reduced rate (∼50%) of their cytoplasmic diffusion rate.

To allow ribosomes to diffuse on the lattice, we need to dynamically update the position of their projection on the lattice to correctly exclude their volume. The center of mass particle of ribosomes is assigned a diffusion coefficient of $0 . 0 0 1 \mu \mathrm { m } ^ { 2 } / \mathsf { s }$ and is only allowed to diffuse with the ribosome’s lattice sites. We assigned this diffusion coefficient based on the calculated diffusion coefficient for ribosomes from Brownian Dynamics simulations by Benjamin Gilbert where ribosomes were simulated as hard spheres with radii of 10 nm in the presence of a single chromosome within a cell of radius 200 nm.<sup>7</sup> Gilbert et al. calculated a diffusion coefficient range $\mathsf { o f } \sim 0 . 0 1 \mathrm { ~ - ~ } 0 . 0 3 \mu \mathsf { m } ^ { 2 } / \mathsf { s }$ for the ribosomes, however the simulations did not include the exact crowding that ribosomes would experience in Syn3A and instead used the estimated viscosity of E. coli cytoplasm from Thornburg et al.,<sup>1</sup> and Syn3A cytoplasm appears significantly more dense in cryo-electron tomograms.<sup>21</sup> As a conservative estimate, as Earnest et al. calculated when treating the dense nucleoid region of $E . c o l i , ^ { 9 8 , 1 0 0 }$ we reduced the diffusion rate of the ribosomes by an order of magnitude within the dense cytoplasm of Syn3A to a value of 0.001 μm<sup>2</sup>/s. With the diffusion coefficient and knowledge that the center of mass can diffuse only one lattice site (10 nm) without updating the excluded volume lattice sites, we can use Stokes-Einstein diffusion to determine the frequency at which the excluded volume sites need to be updated to maintain realistic diffusion. The minimum frequency can be calculated as

$$
\Delta t = \frac { \left( 1 0 \mathsf { n m } \right) ^ { 2 } } { 6 \times 0 . 0 0 1 \mu m ^ { 2 } s ^ { - 1 } } = 0 . 0 1 7 s .\tag{Equation 39}
$$

As a conservative estimate that also serves as a consistent frequency for all communication procedures, we chose to update the ribosome lattice sites every 12.5 ms or 250 RDME time steps.

Because each ribosome is independent in the RDME representation, they will diffuse apart even if they are translating the same mRNA. Adding polysomes then necessitates treating the diffusion of ribosomes in another computational method and communicating their positions to the RDME lattice. We attempted to add ribosomes as diffusing obstacles for the chromosomes in the Brownian dynamics LAMMPS simulations, but they caused frequent clashes with SMC loops. Unfortunately, even if the ribosomes were not causing clashing issues with SMC loops, the Brownian dynamics simulations still do not simulate enough time steps to reach the biological times to recover realistic diffusion. Therefore, addition of polysomes presents a significant challenge and will require integration of another method into the hybrid simulations.

## Cell Growth and Division in 3D

## Calculating Cell Surface Area Dynamically from Lipids and Membrane Proteins

The surface area and volume in the simulations are directly tied to the chemistry of synthesizing membrane components. As lipids are synthesized and membrane proteins are translocated, we iteratively update the total surface area of the system. Each second of biological time, we count the number of lipids and membrane proteins, assign each molecule a surface area contribution per particle, account for the lipid bilayer, and then sum all the surface area contributions to get the total surface area of the membrane. We use the same assumptions as the previous well-stirred model for the individual surface area contributions in units of square nanometers per particle: membrane proteins - 28, cardiolipin - 0.4, sphingomyelin (sm) - 0.45, phosphatidylcholine (pc) - 0.55, phosphatidylglycerol (pg) - 0.6, phosphatidic acid (pa) - 0.5, Gal-DAG (galfur12dgr) - 0.6, 1,2-diacylglycerol (12dgr) - 0.5, and CDP-diacylglycerol (cdpdag) - 0.5.<sup>1</sup> To account for the lipid bilayer difference, we estimate that for a spherical membrane 200 nm in radius, 51.3% of the lipids are in the outer monolayer. We assume that this fraction remains roughly constant throughout the cell cycle. The total surface area as well as the lipid and membrane protein contributions for the 50 simulated cells are shown in Figure S3.

To calculate the cell volume, we first make an assumption because we do not include the kinetics for FtsZ polymerization and neck constriction. We assume that the model grows spherically from its initial size until it approximately doubles in volume. Cells of roughly 200 nm and 250 nm (corresponding to an initial volume and a doubled volume) were previously observed in cryo-electron tomography, so it is a reasonable assumption that a cell might experience both these volumes in its cell cycle.<sup>21</sup> In the simulation, we calculate the radius for a sphere with the surface area calculated using the surface area contributions discussed above and use this radius to calculate the cell volume during spherical growth. Once the volume doubles, we assume that it remains constant throughout the remainder of the cell cycle.

## Updating Morphology During Spherical Growth

Once every 4 seconds of biological time, we update the total surface area and volume of the cell by calculating the total surface area as described above. During the period of the cell cycle when the cell grows to twice its volume, we assume that the cell grows spherically. Because we impose a cubic lattice on 3D space, our growth steps during this period are discrete even though we treat the surface area and volume as continuous quantities. From the instantaneous cell volume, we calculate the radius for a sphere with an equivalent volume. We update the morphology on the RDME lattice in increments of 10 nm because of the 10 nm lattice spacing. Therefore, we simulate membrane shape for cells with radii: 200, 210, 220, 230, 240, and 250 nm. In increments of 4 s of biological time, we check if the cell radius has passed a 10 nm threshold (following the frequency of updating the chromosome state to ensure the membrane boundaries are synchronized between methods). If a threshold has been crossed, the site types are updated on the RDME lattice to reflect the new cell size. To impose a new morphology on the lattice, we need to reconstruct the projection of each region onto the RDME lattice. The procedure for generating the regions are the same as generating the initial conditions. Once the new shapes are generated, we clear the site type lattice and reassign each lattice site to their updated site type. Ribosomes and DNA are left in place and we assume their dynamics will result in their exploration of the new space. Updating the positions of other particles during morphological changes is described below.

## Generating Membrane Shapes During Division

We tested two methods of generating membrane shapes during division. The method that more closely reflected the morphologies observed in fluorescent imaging assumes that the cell divides symmetrically as two overlapping spheres (domes). We determine the radii and center-to-center distance for the domes geometrically using only the surface area and volume of the system. A 2D projec tion schematic is shown in Figure S3A. We can determine the volume of one of the domes by integrating discs. We assume that the center of the dome is the origin and integrate these discs for a dome of radius R laterally from − R to h where h is the distance from the center of the dome to the division plane, or half the center-to-center distance between the domes.

$$
V = \int d V = \int _ { - R } ^ { h } \pi r ^ { 2 } d x = \int _ { - R } ^ { h } \pi \big ( R ^ { 2 } - x ^ { 2 } \big ) d x\tag{Equation 40}
$$

Evaluating the integral for volume gives us an equation relating the volume to the dome radius and distance to division plane.

$$
V = \frac { 2 \pi } { 3 } R ^ { 3 } + \pi R ^ { 2 } h - \frac { \pi } { 3 } h ^ { 3 }\tag{Equation 41}
$$

To connect the surface area to the dome radius and center-to-center distance, we use the surface of rotation method to rotate a 1-dimensional semicircular line about the axis of cell division. Our linear equation takes the form

$$
f ( x ) = \sqrt { R ^ { 2 } - ( x - R ) ^ { 2 } } .\tag{Equation 42}
$$

When we reduce the integral for surface of rotation, the integrand reduces to depend only on the dome radius.

$$
S A = 2 \pi \int _ { 0 } ^ { x _ { 0 } } f ( x ) \sqrt { 1 { + } f ( x ) ^ { 2 } } d x = 2 \pi \int _ { 0 } ^ { R { + } h } R d x\tag{Equation 43}
$$

Evaluating this integral gives us an equation that relates the surface area to the dome radii and distance to division plane.

$$
S A = 2 \pi R ( R + h )\tag{Equation 44}
$$

We do not solve this system of equations analytically. Once the cell volume has doubled in the simulation, we numerically solve for R and h using Equations 41 and 44 at a frequency of 4 seconds of biological time (following the frequency of updating the DNA configuration). When we solve for the parameters to determine cell shape, we double Equations 41 and 44 and set them equal to the instantaneous cell surface area and volume. The equations were solved for a single dome, but the cell consists of two mirrored domes making up the total surface area and volume. We could have instead halved the total surface area and volume of the system when solving to obtain the same results. The numerical solutions are obtained using the optimize module of the scipy Python library. After setting up the system of equations, we then use the least\_squares function to obtain the set of solutions. Because the equations are cubic, there will be multiple set of solutions and we need to choose the set that reflects the physical reality of the membrane shape. We know that the solutions that best mimics the cell shape are positive solutions where R is between its initial radius and the radius at doubled cell volume and h is between zero and the cell radius. We provide initial guesses of 0 to 300 nm to the least\_squares solver for h and R, respectively, to ensure we choose the realistic solution.

The values of h and R are then used to build two cytoplasmic spheres of radius R whose centers of mass are separated by distance h. The time-dependent values for R and h from the 50 simulated cells are shown in Figures S3C and S3D. In the solutions for R, we see that the cells increase in radius after they reach twice the initial surface area, indicating that the solutions do not perfectly preserve volume once the cell has doubled and divided. The division plane is defined as the midplane along the z axis of the simulation (z=64 lattice sites). We then define the cytoplasm of the dividing cell as the union between the two individual cytoplasmic spheres. The membrane is then constructed by building a contiguous layer of lattice sites at the surface of the cytoplasm using the dilate function implemented in jLM.

## Updating Particle Positions During Morphological Changes

As the morphology is updated on the RDME lattice, the particles need to be moved to remain inside their respective regions in the cell. As the cell grows and divides, particles that are in the membrane must stay in the membrane and particles that are cytoplasmic need to stay inside the cell. There are many solutions to the problem, but because almost all morphological changes are minimal (radial changes on the order of a single lattice site), we chose a simple method that moves particles to the nearest lattice site of the type that they were in before the change. For each site type in the simulation, excluding ribosome site types, we check each lattice site X that had site type Y before the morphological change. If lattice site X is still type Y following the morphological change, nothing is done. Otherwise, we use a K-Dimensional Tree (KDTree, scipy.spatial.KDTree function) as a binary mapping of the positions of all lattice sites of type Y following the morphological change. We then query the KDTree for the nearest lattice site to X that is type Y after the morphological change. Each particle from site X is placed into the new lattice site until all particles are placed or the site is full. If the site becomes filled, we once again query the KDTree for the next nearest lattice site of type Y and repeat the process until all particles from site X have been redistributed to the nearest sites of type Y. The algorithm for moving ribosomes is almost identical, but because they have their own lattice sites, we move them to the nearest cytoplasmic lattice site.

## Communicating the Membrane Boundary to the Chromosomes

In communicating the RDME cell state to the chromosome configuration, the current shape of the cell is communicated to the program by determining the positions of the boundary particles in the btree\_chromo simulation. Before the onset of division, the membrane boundary is constructed using the spherical\_brdy function in btree\_chromo. The input variable is the instantaneous cell radius during spherical growth in units of Angstroms. The function creates a sphere of boundary particles who have repulsive interactions with DNA monomers. The boundary particles are packed on the surface such that there are no gaps for DNA monomers to escape through.

The process during division is more complicated, as instantaneous jumps in morphology can result in DNA monomers escaping the cell. The morphology during division is generated using the function overlapping\_spheres\_bdry whose input variables are the values of R and h discussed above (in units of Angstroms). This function generates a boundary for two symmetric spherical domes of radius R and separated by a distance h. The procedure generates a boundary similar to the spherical\_brdy function where boundary particles are packed tightly enough that DNA monomers cannot pass through. At time points when the morphology is updated, a custom procedure was required to ensure the DNA stays inside the cell. Instead of executing a LAMMPS simulation in parallel, a division procedure is executed serially because the RDME and BD membranes need to be synchronized. In this custom procedure, the initial condition is the input variables for R and h for the previous morphology. To guarantee that the DNA stays inside the cell, the boundary particles cannot be moved by more than the radius of a DNA bead. With this limitation, we compare the differences between the last R and h and the values for the new morphology. If either difference is greater than the radius of a DNA bead, the BD simulation is instructed to enter a progressive set of minimizations. We calculate the number of steps in increments of DNA bead sizes between the last and new values of R and h. The greater number of steps determines the number of minimizations. The procedure then iteratively creates membrane boundaries by incrementally changing R and h from the previous values to the new values and minimizes the energy of the chromosomes in each iteration. Because of the repulsive interactions between the DNA and membrane boundary particles, and because the membrane boundary particles are moved in increments less than the DNA bead size, the minimizations push the DNA monomers to the inside of the cell as the membrane constricts during division.

At the final step of division when the membrane fuses at the division plane separating the cytoplasms of the two daughter cells, an uncommon issue can arise where some DNA monomers can still be in the division plane. In this case, we defined a rescue procedure that clears all DNA from the division plane. To pull the DNA out of the division plane, we separate the two daughter chromosomes into independent BD simulations. The chromosomes are mapped to a daughter cell based on the positions of their centers of mass relative to the centers of the daughter cells. Once chromosomes are assigned to daughter cells, the pairwise distance between every DNA monomer in the chromosome and the center of the corresponding daughter cell is calculated. If the maximum distance is greater than the radius of the daughter cell, an iterative LAMMPS simulation is initiated. Again, boundary particles can be moved only in increments less than or equal to the radius of the DNA monomers. We initiate a simulation of the isolated chromosome in a spherical boundary whose radius is equal to the maximum calculated distance from before. The system is then minimized in progressively smaller spherical boundaries in radius increments equal to the radius of a DNA monomer until the membrane’s radius is equal to the radius of the daughter cell. These minimizations ensure all DNA monomers for the chromosome are out of the division plane and inside the cytoplasm of the respective daughter cell. Once both chromosomes undergo this procedure, their coordinates are recombined into a single LAMMPS simulation and the model continues with its normal procedures.

## Generating Membrane Shapes with FreeDTS

In preliminary versions of the 4DWCM, we generated membrane shapes using the FreeDTS software to model the morphology of a growing cell by considering changes in three macroscopic characteristics: (i) an increase in volume, (ii) an increase in membrane surface area, and (iii) changes in the area difference between the two monolayers of the membrane. FreeDTS captures realistic membrane mechanics, as it uses the Helfrich Hamiltonian, which has been shown to accurately represent membrane behavior at large scales.<sup>36</sup> However, under the parameters we tested, the resulting morphologies were more elongated—resembling teardrop shapes—rather than the nearly spherical geometries observed in fluorescence imaging. An example of such a teardrop morphology is shown in Figure S3. While this approach is more appealing, as it uses an accurate physical model of the membrane, we currently lack the necessary information and appropriate models for the interacting proteins that form the Z-ring, as well as a kinetic model of FtsZ polymerization and neck constriction. We expect that in the future, once these components are incorporated, the double-spherical shapes observed in experimental settings will be reproduced using a similar physics-based model. Therefore, we opted for the geometric approach as described above. Below, we briefly describe the original methods that were used to generate dividing membrane shapes.

FreeDTS has several potentials that can be used to influence membrane shape, and in our testing we used a Hamiltonian of the form

$$
H = E _ { b } + E _ { V } + E _ { A } + E _ { s }\tag{Equation 45}
$$

where $E _ { b }$ is the bending energy of the membrane, $E _ { V }$ is a potential dictating the total volume of a closed surface, $E _ { A }$ is a potential dictating the total surface area of the system, and $E _ { s }$ is a coupling potential to maintain global curvature of the membrane. In FreeDTS, the bending potential takes the form of a discretized version of the Helfrich Hamiltonian<sup>106–108</sup> that is a function of the surface curvature up to the second order.

$$
{ \cal E } _ { b } = \sum _ { 1 } ^ { N _ { v } } \Big ( { \frac { \kappa } { 2 } } ( 2 H _ { v } - c _ { 0 } ) ^ { 2 } - \kappa _ { G } K _ { v } \Big ) A _ { v }\tag{Equation 46}
$$

Here, the energy function is discretized to the energy evaluated at each vertex v in the surface. The mean curvature $2 H _ { v } \ = \ c _ { 1 , v } +$ $\begin{array} { r } { C _ { 2 , v } , } \end{array}$ Gaussian curvature $K _ { v } ~ = ~ c _ { 1 , v } c _ { 2 , v }$ , and area contribution $A _ { v }$ are evaluated for each vertex, where $\boldsymbol { c } _ { 1 , v }$ and $\boldsymbol { c } _ { 2 , v }$ are the principa curvatures at the vertex. κ is the bending rigidity of the membrane, $\kappa _ { G }$ is the Gaussian modulus, and $c _ { 0 }$ is the spontaneous curvature. Since the membrane surface did not undergo any topological changes, we safely ignored the second term, based on the Gauss-Bonnet theorem, as the total Gaussian curvature remains constant under pure deformations.<sup>109</sup> We used a standard value for κ that is frequently used for simulating triangulated surfaces representing lipid bilayers: 30 $\mathsf { k } _ { B } \mathsf { T } . ^ { 3 6 , 1 0 9 }$ The spontaneous curvature $c _ { 0 }$ describes how the membrane prefers to be curved. Because we assumed homogeneous membrane properties, this includes effects like the mismatch in area between sides of the lipid bilayer and deformation by membrane proteins. For example, a perfectly flat lipid bilayer has no area mismatch between leaflets, corresponding to $\textsf { a c } _ { 0 }$ of 0. In testing, we used the global curvature coupling potential $( E _ { s } )$ instead, setting the coupling constant to 120 and curvature constant to 0.3, which were fixed throughout all of our simulations. This value was chosen because previous theoretical studies have shown that a curvature constant of 0.3 corresponds to dumbbell-like membrane shapes similar to the ones observed in imaging of $\mathsf { S y n 3 A } . ^ { 3 7 }$

While the parameters of the bending energy remain constant throughout our simulations, the variables come in the form of the surface area and volume of the cell as lipids and membrane proteins are incorporated into the membrane. FreeDTS has potentials to vary both the total surface area and volume of the membrane, however we will only be using the volume potential. Because we assume that the volume remains constant at twice its initial volume once the volume has doubled and continue to grow the surface area, it may seem intuitive that we should therefore utilize the area potential of FreeDTS, which takes the form

$$
{ \cal E } _ { A } = { \frac { K _ { A } } { N _ { T } } } ( A - A _ { 0 } ) ^ { 2 }\tag{Equation 47}
$$

$$
A _ { \scriptscriptstyle 0 } = N _ { \scriptscriptstyle T } ( 1 + 2 \gamma _ { \scriptscriptstyle A } ) \sqrt { 3 } I _ { D T S } ^ { \scriptscriptstyle 2 } \bigg / 4\tag{Equation 48}
$$

where $K _ { A }$ is the compressibility, $N _ { T }$ is the number of triangles in the surface, $I _ { D T S }$ is the length units within a FreeDTS simulation, and $\gamma _ { A }$ ranges from 0 to 1 to control the total surface area. In practice, topology is maintained in the simulation because the vertices have a volume exclusion between each other, and the edge lengths connecting them are constrained so that a vertex can never pass through a triangle (the edge length of a triangles can never exceed twice the diameter of a vertex). The constraints on the edge lengths are important to maintain constant topology, constraining the total surface and resulting in the range for $\gamma _ { A }$ . The equation for $A _ { 0 }$ comes from the area of an equilateral triangle: $A _ { e t } = \sqrt { 3 } a ^ { 2 } / 4$ where a is the edge length of the triangle. In the range of values for $A _ { 0 } , \gamma _ { A } = 1$ corresponds to the case when the edge length of the triangle is twice the diameter of the vertex particles and $\gamma _ { A } = 0$ corresponds to the case when the edge length is equal to the diameter of the vertex particles (minimum because the vertex particles must still exclude each other). These constraints on the total surface area mean that it is difficult to fully explore the range of total surfaces areas that the cell experiences throughout growth and division without changing the number of vertices representing the membrane by adding more vertices to add more area. The dynamic addition of vertices has not yet been implemented into FreeDTS, so instead we constrained the total volume of the cell using the potential

$$
E _ { V } = - \Delta P V + \frac { K _ { V } } { 2 } \left( \frac { V } { V _ { 0 } } - \gamma _ { V } \right) ^ { 2 }\tag{Equation 49}
$$

where $\Delta P$ is the pressure differential between the inside and outside of the membrane, $K _ { V }$ is the compressibility, $V _ { 0 }$ is the volume of a sphere with the equivalent total surface area as the membrane, and $\gamma _ { V }$ ranges from 0 to 1. The range for $\gamma _ { V }$ represents the reduced volume of the system relative to the volume of a sphere with equivalent surface area. With this potential, it is recommended to only use the pressure term or the compressibility term, and not use both simultaneously. The pressure term should be used when you have knowledge of the pressure differential and not a target volume for the system. Similarly, the compressibility term should only be used if there is knowledge of a desired target volume for the system. This is because the compressibility term typically dominates the potential if it is used.<sup>37</sup> We assumed the compressibility energy to be $1 0 ^ { 5 } ~ \mathsf { k } _ { B } \mathsf { T }$ , a value calculated for lipid vesicles,<sup>37</sup> and we consequently set $\Delta \mathsf { P }$ equal to 0.

To generate division morphologies for $\mathsf { S y n 3 A } ,$ we used FreeDTS to equilibrate triangulated vesicle shapes across a range of reduced volumes $( \gamma _ { V } = 1 . 0 0 \ : \mathrm { t o } \ : 0 . 7 )$ . Starting with $\gamma _ { V } ~ = ~ 1 . 0 0$ , we equilibrated the surface corresponding to a spherical membrane. This equilibrated shape served as the starting configuration for the next equilibration, using the same FreeDTS parameters but with $\gamma _ { V } ~ = ~ 0 . 9 9$ . Equilibrations were then sequentially performed in $\gamma _ { V }$ increments of 0.01, each equilibration using the final membrane state from the previous $\gamma _ { V }$ as the initial conditions. Because we did not generate shapes that visually matched the experimentally observed division morphologies, we will not describe the preliminary methods that were developed to communicate these membrane shapes to LM and LAMMPS.

## Molecular Dynamics of DnaA Binding to DNA

The molecular dynamics (MD) simulations were initiated from an AlphaFold $3 ^ { 7 1 }$ predicted complex containing three DnaA protein molecules bound to a double-stranded DNA fragment (5’-TAAAAATAGCTATTTAAACCTAGATTATTAACAGTTATCCACAAATTAACC TCATAATA-3’), which encompasses two low-affinity and one high-affinity DnaA-binding sites as hypothesized previously for the Syn3A origin.<sup>42</sup> Default settings were used for the AlphaFold3 web server for prediction of the initial structure. Structural inspection of the equilibrated complex revealed that residues Arg381, Ser382, and Lys383 within domain IV of all three DnaA were positioned within 5 A<sup>˚</sup> of the DNA-binding interface. A subsequent scan considering all positively charged amino acids on both strands of DNA revealed additional residues: Arg414, Arg424, Arg389; Lys397, Lys425; and His416. To evaluate their contribution to DNA affinity and stability, computational alanine-scanning mutagenesis was performed by individually substituting each of these residues with alanine for the two sets of amino acids (MT1: Arg381, Ser382, and Lys383; MT2: MT1 + Arg414, Arg424, Arg389, Lys397, Lys425, and His416). All systems (wild type and mutants) were solvated in an explicit TIP3P water box with a 12 $\mathring { \mathsf { A } }$ buffer in the short dimensions and a 25 A<sup>˚</sup> buffer along the DNA extension axis, and neutralized with 0.15 M KCl. Simulations employed the CHARMM36m force $\mathbf { f i e l d } ^ { 6 9 , 7 0 }$ for both protein and DNA under periodic boundary conditions. Long-range electrostatics were treated using the particlemesh Ewald (PME) method, and a $12 \mathring { \mathsf { A } }$ cutoff was applied for van der Waals interactions. Each system was energy-minimized and equilibrated under the ${ \mathsf { N P T } }$ ensemble at 310 K and 1.013 bar using a Langevin thermostat and barostat with damping coefficients of 1 ps− 1 and 100 fs, respectively. Production simulations were performed for 200 ns using $\mathsf { N A M D 3 . 0 . 1 } ^ { 6 8 }$ with a 2 fs time step and hydrogen bond constraints applied via the SHAKE algorithm. To preserve the complex moving across the periodic boundary, harmonic positional restraints were applied to the first two nucleotides of both ends on each strand using the complex\_restr.tcl module with a force constant of 10 kcal mol − 1 $\mathring { \mathsf { A } } ^ { - 2 }$

Visualization and post-simulation free energy analyses were performed using VMD 1.9.4a55.<sup>27</sup> Binding free energy calculations were conducted with the NAMDEnergy plugin by evaluating the nonbonded interaction energies between the DnaA residues 381– 420 and the DNA binding region. The binding interface was defined as all DNA atoms (from both strands) located within 5 A<sup>˚</sup> of the corresponding protein residues in the initial predicted structure.

## Computational Environments for Clusters and Supercomputing Resources

## Docker Instructions

To build your environment using Docker version 20.10.11, build dea9396 (Docker Inc., U.S.), start by creating a Docker image based on the Nvidia CUDA 11.6.2 development container for Ubuntu 20.04 (nvcr.io/nvidia/cuda:11.6.2-devel-ubuntu20.04). Use the docker build command with your Dockerfile. This command automatically installs all necessary dependencies, such as the latest version of Miniconda (version 24.11.1, Anaconda, U.S., Linux-x86\_64), along with make, wget, build-essential, libstdc++, libfmt, libssl, libssh, openssh-client, curl, libevent, zlib, manpages, and libsundials-dev (LLNL, U.S.), as well as Python packages including sbtab, pycvodes, pydantic, cobra, xlrd, and mpi4py. It also compiles additional software, including Lattice Microbes v2.5 (Zaida Luthey-Schulten Lab, UIUC, U.S.), odeCELL (Zaida Luthey-Schulten Lab, UIUC, U.S., https://github.com/Luthey-Schulten-Lab/Minimal\_Cell/tree main/odecell), and FreeDTS version 6.7.2023 (Niels Bohr Institute, University of Copenhagen, Denmark). To compile the software required for chromosome simulation, first install gen\_sc\_chain version 7.20.2023 (Zaida Luthey-Schulten Lab, UIUC, U.S., https:// github.com/brg4/sc\_chain\_generation), followed by compiling GCC version 11.5.0 (GNU Project, international), CMake version 3.26.4 (Kitware Inc., U.S.), and OpenMPI version 4.1.5 (Open MPI Project, international). Next, compile LAMMPS version 19Nov.2024 (Sandia National Laboratories, U.S.) and btree\_chromo (Zaida Luthey-Schulten Lab, UIUC, U.S., https://github.com/ brg4/btree\_chromo). Finally, run the Docker image interactively with the default conda environment activated using the docker run command.

## Apptainer Instructions

To compile the environment using Apptainer version 1.3.5-1.el8 (Singularity/Apptainer Development Team, international), start by running apptainer build with your.def file, which uses the Nvidia CUDA 11.6.2 development image (nvcr.io/nvidia/cuda:11.6.2- devel-ubuntu20.04) as the base. Apptainer will copy the necessary source files into the container and then install core dependencies, including the latest version of Miniconda (version 22.11.1, Anaconda, U.S.), along with make, wget, build-essential, libstdc++, libfmt, libssl, libssh, openssh-client, curl, libevent, zlib, manpages, and libsundials-dev (LLNL, U.S.). It proceeds to build software, including Lattice Microbes v2.5 (Zaida Luthey-Schulten Lab, UIUC, U.S.), odeCELL (Zaida Luthey-Schulten Lab, UIUC, U.S., https://github. com/Luthey-Schulten-Lab/Minimal\_Cell/tree/main/odecell), and FreeDTS version 6.7.2023 (Niels Bohr Institute, University of Copenhagen, Denmark). To compile the software required for chromosome simulation, first install gen\_sc\_chain version 7.20.2023 (Zan Luthey-Schulten Lab, UIUC, U.S., https://github.com/brg4/sc\_chain\_generation), followed by compiling GCC version 11.5.0 (GNU Project, international), CMake version 3.26.4 (Kitware Inc., U.S.), and OpenMPI version 4.1.5 (Open MPI Project, international). Next, compile LAMMPS version 19.Nov.2024 (Sandia National Laboratories, U.S.) and btree\_chromo (Zaida Luthey-Schulten Lab, UIUC, U.S., https://github.com/brg4/btree\_chromo). Once completed, the Apptainer container will be fully prepared for execution.

## QUANTIFICATION AND STATISTICAL ANALYSIS

## Segmentation and analysis of fluorescence imaging

The acquired 3D images were first manually segmented with ImageJ<sup>72</sup> to identify single, dividing, and budding cells (a schematic of the image analysis workflow has been prepared). Cells exhibiting stable fluorescence intensities across the z-stacks were selected for further analysis (Video S2: whole-view image with segmentation boxes). Syn3A/B cells do not have machinery for cell movement (e.g. flagella), causing the cells form clusters as the population grows. Clustering of the cells frequently prohibits classification. In total, we segmented 2,968 cells, but due to the weak adhesion of cells to the surface and clustering, 1,649 cells were not suitable for analysis (Figure S2B) leaving 1,319 cells for morphology analysis

For each cell, a single z-plane showing the clearest membrane structure was typically selected for segmentation. When a single plane did not sufficiently capture the cell’s morphology, a maximum intensity projection of multiple z-planes was used instead. We found 1,200 cells to be in spherical/prolate states, 64 cells dividing, and 55 cells budding.

Segmented single cells were further analyzed by fitting their membrane images to a Gaussian-distributed intensity function, where the intensity decays with increasing distance from the ellipsoidal edge. From the fitting results, the equivalent diameter and aspect ratio (minor axis length / major axis length) were calculated to characterize cell size and shape. Cells were classified as prolate if (1) their equivalent diameter exceeded 0.6 μm and (2) their aspect ratio was below 0.8 (Figure S2C). Of the 1,200 spherical/prolate cells, this analysis annotates 1,050 as spherical and 150 as prolate.

For cell-in-cell morphologies (Figure S2D), of the 2,968 segmented cells, 2,525 cells had no cell-in-cell structures, 249 cells had one, 113 cells had two, and 82 cells had three or more.

## DNA coverage analysis

Sequencing quality was uniformly high for all replicates, with average Phred quality scores exceeding 35 across the majority of read positions, as reported by MultiQC. Raw sequencing reads were aligned to the reference genome using Bowtie 2 v2.5.4,<sup>66</sup> and coverage profiles were generated using samtools v1.21.<sup>67</sup> For plotting the coverages in Figures 4B and S2F, we applied Gaussian smoothing to the data using a window with a standard deviation of 1000 bp generated by the scipy.signal.windows.gaussian function, and convolution was performed in the Fourier domain using the scipy.fft module.

For each coverage profile we fit a line across half of the genome from the terminus to origin (genome positions [271,690-543,379]). We decided not to include genome positions [0-271,689] in the fitting process because genomic coordinates [0-271,689] contained more dips in the data, such as the deletion of the tetM gene around [20,200-21,950], and furthermore replication should be roughly symmetric in both directions from the origin. The values of the fitted line at its endpoints were taken as proxies for the origin and terminus coverage, respectively. For late exponential growth phase, we obtained ori:ter ratios of 1.20 (replicate 1: 2120/1760), 1.21 (replicate 2: 2020/1670), and 1.21 (replicate 3: 1910/1580). Mid-exponential growth phase ratios were 1.21 (replicate 1: 1727/ 1423), 1.21 (replicate 2: 1579/1302), and 1.20 (replicate 3: 1461/1213). In the stationary phase, the ratios were 0.98 (replicate 1: 1745/1785), 0.99 (replicate 2: 1594/1616), and 0.97 (replicate 3: 1583/1624).

We used the same fitting method for the coverage profiles generated from DNA sequence datasets of 10 evolutionary endpoints that were deposited alongside a recent study.<sup>20</sup> The ratios were 1.06 (endpoint a1: 365/345), 1.10 (endpoint a2: 217/197), 1.05 (endpoint a3: 281/267), 1.13 (endpoint a4: 268/237), 1.12 (endpoint a5: 200/178), 1.07 (endpoint a6: 158/148), 1.02 (endpoint a7: 246/242), 1.12 (endpoint a8: 195/174), 1.19 (endpoint a9: 238/200), and 1.16 (endpoint a10: 243/210).

## Calculation of mRNA half-lives

Because the 4DWCM records the state of the lattice only once per biological second, we create book-keeping particles to track if gene expression events have occurred. If we do not explicitly track every gene expression reaction, there is a chance that reactions will not be accounted for in cost calculations communicated to metabolism. Additionally, we are able to accurately calculate bulkbehavior values like mRNA half-lives because we explicitly track all gene expression reactions to 1 second resolution. The following reactions create a book-keeping particle that is mapped to the gene locus for the individual RNA or protein: transcription, translation, mRNA degradation. For each process, the book-keeping particle is created as a product of the reaction. For example, the translation reaction for gene dnaA/0001 takes the form

$$
\mathsf { m R N A _ { - } 0 0 0 1 } + \mathsf { r i b o s o m e {  } m R N A _ { - } 0 0 0 1 } : \mathsf { r i b o s o m e }\tag{Equation 50}
$$

$$
\mathsf { m R N A \_ O O 0 1 : r i b o s o m e } \to \mathsf { m R N A \_ O O 0 1 } + \mathsf { r i b o s o m e } + \mathsf { p r o t e i n \_ O O 0 1 } + \mathsf { t r a n s l a t i o n \_ O O 0 1 } + \mathsf { p r o t e r a n s l a t i o n \_ H o r } .\tag{Equation 51}
$$

where translation\_0001 is the book-keeping particle for translation of DnaA.

To calculate mRNA half-lives, we utilized the book-keeping particle for mRNA degradation. The overall rate of formation of a mRNA is

$$
\frac { d [ \mathsf { m R N A } _ { i } ] } { d t } = k _ { \mathsf { t r a n s c r i p t i o n } , i } - k _ { \mathsf { d e g } , i } [ \mathsf { m R N A } _ { i } ]\tag{Equation 52}
$$

where the degradation rate $k _ { \mathsf { d e g } , j }$ is related to the half-life by

$$
t _ { 1 / 2 , i } = { \frac { \mathsf { l n } 2 } { k _ { \mathsf { d e g } , i } } } .\tag{Equation 53}
$$

To determine half-life, we set the transcription rate to 0 and the overall formation rate equal to the total number of degradation events divided by the time elapsed in the simulation. These conditions reflect mRNA half-life experiments where transcription is halted and the counts of mRNA decrease as mRNA are degraded. Using the time-averaged concentration of mRNA, we can then calculate $k _ { \mathsf { d e g } , j }$ and half-life for each mRNA. The distribution presented in Figure 5 was calculated using the number of degradation events over 105 minutes.

## Analysis of 4DWCM trajectories

The 50 simulated cells were analyzed in Python. Particle counts and fluxes were analyzed using the numpy library (for results shown in Figures 4, 5, S3, and S5) and spatial position data in the RDME lattice was analyzed using the h5py library and our own jLM library (for results shown in Figures 6 and S3). The Python Jupyter notebooks including analysis of all quantities presented in figures are available on the Github repository or Zenodo (see data and code availability).

## Supplemental figures

![](images/3738b26ee6b8a3faaf6273c5d0e159031e744ee0b7e1a23918fe01ccde065aab.jpg)

![](images/fd3f7e7bde0f94ed34486bc491a7916291e30b6664852756c702cbe53fd5e0ea.jpg)

![](images/4b4f69e52951ce1acd852d7a813080c1f6ac62c622aea44f0eeec0c75edd6049.jpg)  
Ribosome center of mass particle

![](images/1417edb02a2e2b07db0279d61687a38e50ac4596ab8f3198d1e134363cb81c66.jpg)

![](images/3f122125a642bcfea5151e6f951587580811d3da6217d430956198729e44cdce.jpg)

![](images/b3fcad2cf15f28a539d4f4cd88d6e01a04f5fe1be081d64d84f297546a2488f3.jpg)

![](images/cb7621faf02b01ef4f03e2fdf846dd7d3426b227b5d87f048089d56fda763fb8.jpg)

![](images/fe448a0376f9f639e77459d9fe6bc633de330522cc731d600b1ae83eef7ecf03.jpg)

![](images/65f9c0ac4a07969be8ad0ada311f91ba22dca1ddce452593f826c08a9af9d81f.jpg)  
Figure S1. Projection of the ribosome onto the 10 nm lattice and its diffusion rules, related to Figure 1 and STAR Methods The ribosome has a radius of 10 nm, resulting in the projections onto the lattice shown in the top left and middle. The top right shows that mRNA can diffuse into and out of ribosomes at their normal cytoplasmic rate so that mRNA can undergo translation initiation. Proteins can diffuse out of ribosomes at their cytoplasmic diffusion rate, but we reduce their diffusion rate into the ribosome because of the excluded volume of the ribosome. The center of mass particle of the ribosome starts at the center lattice site of the ribosome projection and is then allowed to diffuse within the cross. At the communication time, we update the position of the cross to reflect the new position of the center of mass particle.

A  
![](images/24bac10b9734e38eb401362e55c54f53d3dd053d5c454f03a2ee15cf00a0eee0.jpg)

![](images/b1fec597de165f8c5b4077081807e99c8c1b292924be57b103c2685a9bad495b.jpg)

![](images/3f1ba8d2787244a67ad58b7d6f8f23fdc73acc195892e5e10fabee986adb15de.jpg)

B  
![](images/ee64c4e7229bddc42f40b2dbe89f93c5e7e70010f2a5a5fe9663ec3f796c6531.jpg)

C  
![](images/00ccef5e7ddc5d888b44b4bcbc992aaf42b2b77ba1681c824ab32a3d4a0571ab.jpg)

D  
![](images/dcaf2ab5771a812ccf11412c5a482d1512d6864ee06a636adacda8741adedf30.jpg)

E  
![](images/e3df82e7911d5d51a21ddcd33d79eb1d44cc733b545c0be46fcd066cd84b4f20.jpg)

![](images/671f3b45cc1dad5f1c3276cc3d5a1aa3aa95c297422213e20ec503f358f10a1c.jpg)

Figure S2. Imaging statistics and stationary phase DNA sequencing of JCVI-syn3A/B, related to Figure 4

(A) Schematic representation of the method to analyze morphologies in fluorescent imaging of JCVI-syn3B+FtsZ:mCherry. Color channels correspond to membrane (green), DNA (blue), and FtsZ (red).

(B) Total number of segmented cells, the fraction that were excluded due to cell clusters, and the fraction that were analyzed and included in the morphology statistics.

(C) Size and aspect ratio distribution of analyzed single cells. The average cell size was determined to be $0 . 8 9 \pm 0 . 3 7 \mu \mathrm { m }$ . The larger size is likely due to the sample preparation method and lower spatial resolution in the imaging. Prolate cells were identified by quantifying the aspect ratio of their major and minor axes (see STAR Methods).

(D and E) Less than 20% of cells have ‘‘cell-in-cell’’ structures similar to the ones shown in (E). These have been observed previously in Syn3A and are known to form in late exponential phase of growth.<sup>19,22</sup>

(F) DNA sequencing was performed in triplicate during the mid-exponential (5 h of growth, n = 3 replicates) and stationary growth phase (21 h of growth, $n = 3$ replicates). The mid-exponential growth replicates exhibit the same ori:ter ratio as the late exponential (1.21). The lack of a slope in coverage in the stationary replicates corresponds to an ori:ter ratio of 1:1, indicating that the cells have stopped replicating. Each dot in a boxplot represents a technical replicate (field of imaging) and covers the 25–75 percentiles. The means and standard deviations are represented as horizontal and vertical lines, respectively.

![](images/29242876c4c4b24b03f859ad5fb6355e119e6d07bb109e4c1d47163973276690.jpg)

B  
![](images/f2049ed4a497f19e37e8d1813404d2099b44f8637d8532c26d830acc44cf10cb.jpg)

![](images/1d9b507f0627024093904d2d3715a8289fd3f3ae6e3ef1bcd106b87296e437e7.jpg)

D  
![](images/9f87fddb7f11b2f48476c19b07b0a34c274fb93e79be72779330cfab9615fd2f.jpg)

E  
![](images/9e8e38be978d82260454b5b6ee94d0ece43cefb306683506a89a22eb42ee98b8.jpg)

F  
![](images/0fd85f5c9a8567fb96cd36e60d014c676e84945a861524eea9179ba0aedbee4f.jpg)  
G

![](images/492b4330058519c7401b6a67373d7998f7d1abc7960b87eb76fd590bdf6d213a.jpg)  
Figure S3. Spatial components of growth and division, related to STAR Methods

(A) Schematic of the geometric division model. The dividing cell is treated as two overlapping spheres of radius R whose centers are separated by a center-tocenter distance of ${ \boldsymbol { 2 } } \times { \boldsymbol { h } } ,$

(B) Total surface area and contributions from lipids and membrane proteins.

(C) Center-to-center distance $( 2 \times h$ from $\mathsf { A } )$ calculated from instantaneous cell surface area and volume.

(D) Cell radii (R from A) throughout growth and division. The radius increases during spherical growth until division starts once the volume has doubled. In (B)–(D), lines show the population average and shaded regions show the full range among the population.

(E) Example of a membrane shape generated using FreeDTS. The long neck was not observed in experimental imaging. Gray particles represent vertices of the triangulated surface. Green and magenta particles represent two chromosomes fitted into the FreeDTS membrane structure.

![](images/c34152c77a940949755cb9f039886375fd1225b755e5441d2ed885978b057804.jpg)

![](images/91d7fb09439cf91358b92f02d44472d3cb84826fd0f599e0414f966ea153a06e.jpg)  
Figure S4. All-atom prediction of DnaA binding to the Syn3A genome origin of replication, related to Figure 5  
(A) The double-stranded DNA binding signatures for DnaA at the origin are highlighted in orange (complement is yellow on the reverse strand). Three DnaA monomers are colored cyan, tan, and purple to distinguish their individual binding orientations. Residues substituted to alanine in mutant type 1 (MT1) are blue (Arg381, Ser382, and Lys383); the wild type (WT) is shown in the structure. Mutant type 2 (MT2) substitutes alanine for the residues in MT1 as well as the residues shown in red (Arg414, Arg424, Arg389, Lys397, Lys425, and His416).  
(B) Interaction energy of the DnaA domain IV with the double-stranded DNA binding signature shows that substituting Arg381, Ser382, and Lys383 residues with alanines in MT1 dramatically reduces the stability of DnaA binding to the origin. Further alanine substitutions in MT2 resulted in a repulsive interaction between DnaA and the double-stranded DNA, causing all three DnaA monomers to separate from the DNA (n = 1 replicate simulation).

![](images/6f612b1b0fdb8482f24dc2035f864119b0e008ecf1ee105af0ec4fa09ff69cc4.jpg)

![](images/91a958f29fde88cdf74d7cf0198b0586777a2dee8bd7c841cd5f1e1c89a3c3e1.jpg)

B  
![](images/e8f1317352ee15f53951dc55ae31f7b910cd76d1d94585d538c68008917ec66d.jpg)

C  
![](images/e3c89b38f25eae98e987ba2875d178f0c7a6301ae8296b93c88942ae03649c5f.jpg)  
(A–C) Costs are averaged among the population (A and B) and for a representative cell (C). The total ATP generated is slightly higher than the total ATP cost to maintain the ATP pool as the cell grows and eventually divides. The cost of DNA replication is only present during replication, and the shoulders observed in the fractional cost plot (B) are a result of the variations in the start and end of DNA replication among the population. The long plateau from 60 to 90 min is a result of the cell that initiated replication 46 min into its cell cycle, resulting in its replication lasting until after 90 min. Although ATP costs are steady on average, there are fluctuations in the costs in a single cell as observed in (C) (n = 50 simulated cells).  
Figure S5. Cell-wide accounting of all ATP costs, related to Figure 5