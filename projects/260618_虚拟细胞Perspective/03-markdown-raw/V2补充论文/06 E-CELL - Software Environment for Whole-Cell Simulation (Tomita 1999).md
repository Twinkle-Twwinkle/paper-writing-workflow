# E-CELL: software environment for whole-cell simulation

"3"25 0.\*4"<sup></sup>- &/4" "3)\*.040<sup></sup>- 05\*\$)\* ",")"3)\*<sup></sup>- )0."3\*.0/ )\*.\*95<sup>-</sup>- !52\* "4359",\*<sup></sup>- 5.\*)\*,0 \*803)\*<sup></sup>- "/",0 "\*40<sup></sup>- ",52" "/\*%"<sup></sup>- "43585,\* !5(\*<sup></sup>- 2"\*( &/4&2<sup></sup> "/% -8%&  54\$)\*30/ <sup></sup>

<sup></sup>"#02"4028 '02 \*0\*/'02."4\*\$3- &\*0 /\*6&23\*48-  /%0- 5+\*3"7"-  - "1"/ "/% <sup></sup>)& /34\*454& '02 &/0.\*\$ &3&"2\$)-  &%\*\$"- &/4&2 2\*6&- 0\$,6\*--&-  - 

  	  -     -     - 

## Abstract

Motivation: Genome sequencing projects and further systematic functional analyses of complete gene sets are producing an unprecedented mass of molecular information for a wide range of model organisms. This provides us with a detailed account of the cell with which we may begin to build models for simulating intracellular molecular processes to predict the dynamic behavior of living cells. Previous work in biochemical and genetic simulation has isolated well-characterized pathways for detailed analysis, but methods for building integrative models of the cell that incorporate gene regulation, metabolism and signaling have not been established. We, therefore, were motivated to develop a software environment for building such integrative models based on gene sets, and running simulations to conduct experiments in silico.

Results: E-CELL, a modeling and simulation environment for biochemical and genetic processes, has been developed. The E-CELL system allows a user to define functions of proteins, protein–protein interactions, protein–DNA interactions, regulation of gene expression and other features of cellular metabolism, as a set of reaction rules. E-CELL simulates cell behavior by numerically integrating the differential equations described implicitly in these reaction rules. The user can observe, through a computer display, dynamic changes in concentrations of proteins, protein complexes and other chemical compounds in the cell. Using this software, we constructed a model of a hypothetical cell with only 127 genes sufficient for transcription, translation, energy production and phospholipid synthesis. Most of the genes are taken from Mycoplasma genitalium, the organism having the smallest known chromosome, whose complete

580 kb genome sequence was determined at TIGR in 1995. We discuss future applications of the E-CELL system with special respect to genome engineering. Availability: The E-CELL software is available upon request. Supplementary information: The complete list of rules of the developed cell model with kinetic parameters can be obtained via our web site at: http://e-cell.org/. Contact: mt@sfc.keio.ac.jp

## Introduction

The complete genomes of more than 18 microorganisms have been sequenced. The availability of this new information on the gene content of organisms has led to the emergence of a number of heretofore unavailable approaches to biology. Systematic analyses of genes/proteins are now under way in numerous centers around the world, and comprehensive catalogues of protein function are being constructed.

The challenge created by genomics is to understand how all the cellular proteins work collectively as a living system. By attempting to understand the dynamics in living cells, we should be able to predict consequences of changes introduced into the cell and/or its environment, e.g. knocking out a gene or altering available metabolites. Possible consequences of such intervention include cell death, changes in growth rate, and an increase or decrease in the expression of specific genes. The development of sufficiently refined cell models which allow predictions of such behavior would complement the experimental efforts now being made systematically to modify and engineer entire genomes.

In this paper, we present E-CELL, a computer software environment for modeling and simulation of the cell. The E-CELL system is a generic object-oriented environment for simulating molecular processes in user-definable models, equipped with graphical interfaces that allow observation and interaction. E-CELL provides a unified, object-oriented framework for modeling and simulation of the complex interactions among the gene products of completed genomes. Our modeling approach described in this paper attempts to link diverse cellular processes such as gene expression, signaling and metabolism, to construct a cell model for conducting experiments in silico.

## Previous work in simulations of cellular processes

Many attempts have been made to simulate molecular processes in both cellular and viral systems. Perhaps the most active area of cellular simulation is the kinetics of biochemical metabolic pathways. Several software packages for quantitative simulation of biochemical metabolic pathways, based on numerical integration of rate equations, have been developed, including GEPASI (Mendes, 1993, 1997), KIN-SIM (Barshop et al., 1983; Dang and Frieden, 1997), MIST (Ehlde and Zacchi, 1995), METAMODEL (Cornish-Bowden and Hofmeyr, 1991) and SCAMP (Sauro, 1993).

In predicting cell behavior, the simulation of a single or a few interconnected pathways can be useful when the pathway(s) being studied is relatively isolated from other biochemical processes. However, in reality, even the simplest and most well-studied pathways, such as glycolysis, can exhibit complex behavior due to connectivity. Moreover, simulations of metabolic pathways alone cannot account for the longer time-scale effects of processes such as gene regulation, cell division cycle and signal transduction.

Several groups have proposed and analyzed gene regulation and expression models by simulation (Meyers and Friedland, 1984; Koile and Overton, 1989; Karp, 1993; Arita et al., 1994; McAdams and Shapiro, 1995). The cell division cycle (Tyson, 1991; Novak and Tyson, 1995) and signal transduction mechanisms (Bray et al., 1993) have also been active areas of research for biological modeling and simulation. Most of them have utilized qualitative models to deal with the general lack of quantitative data in molecular biology. However, while qualitative models are generally useful when information is incomplete (Kuipers, 1986), they often generate ambiguous results (Kuipers, 1985), the behaviors of which are difficult to predict due to combinatorial explosion (for a review on computer simulations in biology, see Galper et al., 1993).

Previous studies in biochemical and genetic simulations have usually limited their models to focus on only one of the several levels of the time-scale hierarchy in cellular processes. Linking the gaps between the various levels of this hierarchy is an extremely challenging problem that has yet to be adequately addressed. This paper presents a step towards integrative simulation of several levels of cellular processes.

## Implementation of the E-CELL system

The E-CELL system is, in essence, a rule-based simulation system and is written in C++, an object-oriented programming language. The model consists of three lists, and is loaded at runtime. The substance list defines all objects which make up the cell and the culture medium. The rule list defines all of the reactions which can take place within the cell, and the system list defines spatial and/or functional structure of the cell and its environment. The state of the cell at each time frame is expressed as a list of concentration values of all substances within the cell, along with global values for cell volume, pH and temperature. The simulator engine generates the next state in time by computing all of the functions defined in the reaction rule list. In addition to using the sample models provided with the system, the user can create user-defined models by writing original substance and rule lists. Graphical interfaces are provided to allow observation and interaction throughout the simulation process.

A substance can be a substrate, product or catalyst of a reaction. Typical substances include proteins, protein complexes, DNA (genes), RNA and small molecules. The list of substance concentrations is updated with the new values computed by the simulator engine after each time interval.

In a single time interval, each rule in the rule list is called upon by the simulator engine to compute the change in concentration of each substance. The net change in concentration for each substance is added to the present concentration at the end of each time interval to update the set of state variables, i.e. to generate the next state of the cell. By encapsulating numerical integration methods into object classes, virtually any integration algorithm can be used for simulation of an E-CELL model. Furthermore, E-CELL allows the assignment of any numerical integration algorithm for each compartment of the cell model, facilitating the optimization of the simulation for the user’s purpose (e.g. simulation accuracy or speed). Different time intervals (∆t) can also be defined for each spatial or functional compartment and they can be redefined through the control panel at runtime by the user. In the present version, the system defaults to 1 ms for ∆t and the user can select between the first-order Euler [error is $O ( \Delta t ^ { 2 } ) ]$ or fourth-order Runge–Kutta $[ O ( \Delta t ^ { 5 } ) ]$ methods for the numerical integration in each compartment. The Euler method is used in compartments with discrete, stochastic reactions such as DNA–protein binding, and the Runge–Kutta method is used for compartments with deterministic reactions defined by continuous rate functions.

The simulation of our present whole-cell model runs at ∼1/20 of real time on a laptop computer with Pentium-II 200 MHz, and about four times faster on a DEC alpha 21264A 533 MHz with 1 ms integration step and monolithic integration model. A single pathway such as glycolysis runs ∼30 times faster under the same conditions.

## User interfaces

The E-CELL system provides several graphical interfaces which allow the user to observe the cell’s state and manipulate it interactively (Figure 1). The tracer interface is the most important interface which allows the user to select substances or reactions of interest and observe dynamic changes in their quantity or rate, respectively. Since the state of the cell in an E-CELL simulation is defined as the list of all substance quantities, this interface provides the most direct means of observing the cell. Observing dynamical changes in reaction rates is equally important, as the systemic behavior of the cell is characterized by the interaction of a large number of individual reactions. The tracer interface is implemented as a window displaying a twodimensional plot in which animated line graphs represent changes in the quantity of selected substances or reactions. Each window can display up to six substances simultaneously, and multiple tracers may be invoked to observe all substances of interest. This interface can also produce a ‘dump file’ of traced data for further analysis.

![](images/0fec0b3e41a1f53915ea41ee33f6e9d0693e5291c2c6be2a10c224b57e5db454.jpg)  
Fig. 1. A snapshot of user interfaces of the E-CELL system. The tracer window for ‘glycolysis1’ (upper right) shows dynamic changes in quantities of glycolytic metabolites: D-glucose 6-phosphate (C00092), protein histidine (C00615), D-fructose 6-phosphate (C00085), D-fructose 1,6-biphosphate (C00354), D-glyceraldehyde 3-phosphate (C00118) and glycerone phosphate (C00111). The other tracer window (left) shows changes in quantities of ATP (C00002), ADP (C00008), NADH (C00004), NAD+ (C00003) and CTP (C00063). Two reactor windows (lower left) show activities of phosphopyruvate hydratase (EC 4.2.1.11) and fructose-biphosphate aldolase (EC 4.1.2.13). Two substance windows (bottom left) show precise quantities of ATP (C00002) and D-glucose 6-phosphate (C00092). The GeneMapWindow (bottom right) shows current activities (the number of mRNA molecules) of all genes in the cell. Different colors indicate an increase or decrease of activities. Knocked-out genes are marked ‘OFF’.

![](images/d8424129d2fa8eb1a576414c6ee9733a647e93f03f2c747b7e21142f3ef82542.jpg)  
Fig. 2. Metabolism overview of the model cell. It has pathways for glycolysis and phospholipid biosynthesis, as well as transcription and translation metabolisms.

![](images/8956edd8c75da61c48b2f15b5690c1a23b93292a0b7765cdbd5fee740663805c.jpg)  
Fig. 3. Ontology structure of the E-CELL system. There are three fundamental classes: Substance, Reactor and System. Reactors and CellComponents are the user-definable classes. See our web site for more detailed information.

The substance window shows the exact quantity of a selected substance. It also allows the user to alter the quantity at will during the simulation process. The reactor window displays the activity of a selected reaction. The activity of a reaction is defined as the amount of product produced in the reaction per second. The gene map window provides the user with a means of monitoring the expression level of all genes at a glance by graphically displaying the quantity of mRNA transcripts for each gene. The gene map window also allows the user to knock out a selected gene or group of genes by a click of the mouse.

step, we are constructing a model of a hypothetical, minimal cell, based on the gene set of Mycoplasma genitalium, the selfreplicating organism having the smallest known genome, whose complete 580 kb genome sequence was determined in 1995 (Fraser et al., 1995). We have reduced M.genitalium’s gene set to accommodate only those genes required for what we have defined, for our purpose here, as a minimal cellular metabolism.

In constructing E-CELL, the primary focus of our interest is to develop a framework for constructing simulatable cell models based on gene sets derived from completed genomes. As a first

This model cell takes up glucose from the culture medium using a phosphotransferase system, generates ATP by catabolizing glucose to lactate through glycolysis and fermentation, and exports lactate out of the cell. Since enzymes and other proteins are modeled to degrade spontaneously over time, they must be constantly synthesized in order for the cell to sustain ‘life’. The protein synthesis is implemented by modeling the molecules necessary for transcription and translation, namely RNA polymerase, ribosomal subunits, rRNAs, tRNAs and tRNA ligases. The cell also takes up glycerol and fatty acid, and produces phosphatidyl glycerol for membrane structure using a phospholipid biosynthesis pathway (Figure 2). The model cell is ‘self-supporting’, but not capable of proliferating; the cell does not have pathways for DNA replication or the cell cycle.

The cell model is basically constructed with three classes of objects: Substances, Genes and reaction rules. The reactions rules are internally represented as Reactor objects. The entire ontology structure of the system is shown in Figure 3.

## Modeling the cell

## Substances

All molecular species within the cell are defined as Substances. The same molecule in different states (e.g. phosphorylation) is defined as separate molecular species, and each spatial compartment of the model retains a list of all of the substance objects it may contain.

All of the enzymes in our hypothetical model cell are listed in Table 3 and the other small-molecule Substances present in the cell, such as intermediate metabolites, amino acids, nucleotides and cations, are listed in Table 4. Multi-protein complexes, protein–DNA complexes, protein–RNA complexes and other multi-molecule complexes are also defined as Substances, although they are not listed in the table.

## Genes

DNA sequences in chromosomes are modeled as a doubly linked list of GenomicElements. The GenomicElement class can have fragments of sequence such as coding sequences, protein binding sites and intergenic spacers. The Gene class is defined as a GenomicElement which has a transcribed sequence.

The genome of the cell consists of 127 genes including 20 tRNA genes and two rRNA genes. Out of the 127 genes, 120 have been identified in the genome of M.genitalium (Table 1 and 2). Four of the seven genes which have not been identified in M.genitalium are for the phospholipid biosynthesis pathway (acylglycerol lipase, glycerol-1-phosphatase, phosphatidylglycerophosphatase and diacylglycerol kinase). The phospholipid biosynthesis pathway of M.genitalium is not well characterized and it is not clear how the functions of these genes are substituted for. Nucleoside-phosphate kinase and nucleoside-diphosphate kinase have also not been identified in M.genitalium, but we have added them to the cell model in order to compensate for the lack of a nucleotide biosynthesis pathway; these enzymes provide a recycling mechanism for degraded DNA/RNA in the model cell, accounting for the lack of nucleotide biosynthesis. The last of the seven E-CELL genes not found in M.genitalium is glutamine–tRNA ligase, whose function is probably substituted for by glutamate–tRNA ligase in M.genitalium, as it is in Gram-positive bacteria (Fraser et al., 1995).

## Reaction rules

A typical reaction in a metabolic pathway is transformation of one molecular species into another, catalyzed by an enzyme which remains unaltered. For example, the enzyme 6-phosphofructasokinase (EC 2.7.1.11) catalyzes the transformation of D-fructose 6-phosphate (C00085) into D-fructose 1,6-biphosphate (C00354), consuming ATP (C00002) and generating ADP (C00008) and H+ (C00080) (E-CELL Substance IDs shown in parentheses). Schematically, such a reaction can be defined in an E-CELL reaction rule as follows:

$$
\mathrm { C O 0 0 8 5 + C O 0 0 0 2  C O 0 3 5 4 + C O 0 0 0 8 + C O 0 0 8 0 }
$$

[EC 2.7.1.11]

Pathways can then be implemented by defining a series of reactions which use the products of another reaction as participating reactants.

Table 1. The number of genes in important pathways of the hypothetical cell
<table><tr><td>Gene type</td><td>M.gen</td><td>Other</td><td>Total</td></tr><tr><td>Glycolysis</td><td>9</td><td>0</td><td>9</td></tr><tr><td>Lactate fermentation</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Phospholipid biosynthesis</td><td>4</td><td>4</td><td>8</td></tr><tr><td>Phosophotransferase system</td><td>2</td><td>0</td><td>2</td></tr><tr><td>Glycerol uptake</td><td>1</td><td>0</td><td>1</td></tr><tr><td>RNA polymerase</td><td>6</td><td>2</td><td>8</td></tr><tr><td>Amino acid metabolism</td><td>2</td><td>0</td><td>2</td></tr><tr><td>Ribosomal L subunit</td><td>30</td><td>0</td><td>30</td></tr><tr><td>Ribosomal S subunit</td><td>19</td><td>0</td><td>19</td></tr><tr><td>rRNA</td><td>2</td><td>0</td><td>2</td></tr><tr><td>tRNA</td><td>20</td><td>0</td><td>20</td></tr><tr><td>tRNA ligase</td><td>19</td><td>1</td><td>20</td></tr><tr><td>Initiation factor</td><td>4</td><td>0</td><td>4</td></tr><tr><td>Elongation factor</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Protein coding genes</td><td>98</td><td>7</td><td>105</td></tr><tr><td>RNA coding genes</td><td>22</td><td>0</td><td>22</td></tr><tr><td>Total</td><td>120</td><td>7</td><td>127</td></tr></table>

The binding reaction of two or more molecules to form a complex can be expressed in a similar way, where the resulting complex would be defined as a separate molecular species. For example, the reaction in which a GTP (C00044) molecule binds to elongation factor Tu (GXtleftu) can be defined as follows:

[none]

where ‘GXtleftu+GTP’ is a Substance object representing the complex. Other molecular binding phenomena, such as protein–DNA interaction and ribosome formation from ribosomal proteins, can be modeled in a similar fashion.

Besides quantitative information for each substance, information concerning the location of a substance is often important. We have defined the same molecular species at two different locations as two different objects. For example, the uptake of glycerol (C00116) into the cytoplasm catalyzed by the membrane protein GlycerolUptake PassiveTransport (Egu001) is defined as:

ENVIRONMENT:C00116 → CYTOPLASM:C00116

$$
[ \mathtt { E g u 0 } 0 1 ]
$$

where ENVIRONMENT:C00116 and CYTOPLASM:C00116 represent glycerol in the environment (culture medium) and cytoplasm, respectively.

## Using biological knowledgebases for model construction

In order to obtain efficiently the necessary information to implement the pathways in our cell model, we have been utilizing knowledgebases such as EcoCyc (Karp et al., 1996)

Table 2. Protein coding genes in the hypothetical cell.
<table><tr><td>ID</td><td>name</td><td>ID</td><td>name</td></tr><tr><td>MG005</td><td>Serine-tRNA ligase</td><td>MG215</td><td>6-phosphofructokinase (pfkA)</td></tr><tr><td>MG021</td><td>Methionine-tRNA ligase</td><td>MG216</td><td>pyruvate kinase (pyk)</td></tr><tr><td>MG023</td><td>fructose-bisphosphate aldolase (tsr)</td><td>MG232</td><td>ribosomal protein L21</td></tr><tr><td>MG033</td><td>glycerol uptake facilitator(glpF)</td><td>MG234</td><td>ribosomal protein L27</td></tr><tr><td>MG035</td><td>Histidine-tRNA ligase</td><td>MG249</td><td>RNA polymerase sigma S subunit</td></tr><tr><td>MG036</td><td>Aspartate-tRNA ligase</td><td>MG251</td><td>Glycine-tRNA ligase</td></tr><tr><td>MG038</td><td>glycerol kinase (glpK)</td><td>MG253</td><td>Cysteine-tRNA ligase</td></tr><tr><td>MG041</td><td>Protein histidine(HPr)(ptsH)</td><td>MG257</td><td>ribosomal protein L31</td></tr><tr><td>MG069</td><td>phosphotransferase enzymeII(ptsG)</td><td>MG266</td><td>Leucine-tRNA ligase</td></tr><tr><td>MG070</td><td>ribosomal protein S2</td><td>MG283</td><td>Proline-tRNA ligase</td></tr><tr><td>MG081</td><td>ribosomal protein L11</td><td>MG292</td><td>Alanine-tRNA ligase</td></tr><tr><td>MG082</td><td>ribosomal protein L1</td><td>MG300</td><td>phosphoglycerate kinase (pgk)</td></tr><tr><td>MG087</td><td>ribosomal protein S12</td><td>MG301</td><td>G3PD (gapA)</td></tr><tr><td>MG088</td><td>ribosomal protein S7</td><td>MG311</td><td>ribosomal protein S4</td></tr><tr><td>MG089</td><td>Elongation Factor G</td><td>MG325</td><td>ribosomal protein L33</td></tr><tr><td>MG090</td><td>ribosomal protein S6</td><td>MG334</td><td>Valine-tRNA ligase</td></tr><tr><td>MG092</td><td>ribosomal protein S18</td><td>MG340</td><td>RNA polymerase beta&#x27; subunit</td></tr><tr><td>MG093</td><td>ribosomal protein L9</td><td>MG341</td><td>RNA polymerase beta subunit</td></tr><tr><td>MG111</td><td>phosphoglucose isomerase B (pgiB)</td><td>MG344</td><td>Lipase</td></tr><tr><td>MG113</td><td>Asparagine-tRNA ligase</td><td>MG345</td><td>Isoleucine-tRNA ligase</td></tr><tr><td>MG114</td><td>PGP synthase (pgsA)</td><td>MG351</td><td>inorganic pyrophosphate (ppa)</td></tr><tr><td>MG126</td><td>Tryptophan-tRNA ligase</td><td>MG361</td><td>ribosomal protein L10</td></tr><tr><td>MG136</td><td>Lysine-tRNA ligase</td><td>MG362</td><td>ribosomal protein L7</td></tr><tr><td>MG142</td><td>translation initiation factor2</td><td>MG363</td><td>ribosomal protein L32</td></tr><tr><td>MG150</td><td>ribosomal protein S10</td><td>MG363.1</td><td>ribosomal protein S20</td></tr><tr><td>MG151</td><td>ribosomal protein L3</td><td>MG365</td><td>Methionyl-tRNA formyltransferase</td></tr><tr><td>MG152</td><td>ribosomal protein L4</td><td>MG375</td><td>Threonine-tRNA ligase</td></tr><tr><td>MG153</td><td>ribosomal protein L23</td><td>MG378</td><td>Arginine-tRNA ligase</td></tr><tr><td>MG154</td><td>ribosomal protein L2</td><td>MG407</td><td>enolase (eno)</td></tr><tr><td>MG155</td><td>ribosomal protein S19</td><td>MG417</td><td>ribosomal protein S9</td></tr><tr><td>MG156</td><td>ribosomal protein L22</td><td>MG418</td><td>ribosomal protein L13</td></tr><tr><td>MG157</td><td>ribosomal protein S3</td><td>MG424</td><td>ribosomal protein S15</td></tr><tr><td>MG158</td><td>ribosomal protein L16</td><td>MG426</td><td>ribosomal protein L28</td></tr><tr><td>MG159</td><td>ribosomal protein L29</td><td>MG429</td><td>proteinphosphotransferase(ptsI)</td></tr><tr><td>MG160</td><td>ribosomal protein S17</td><td>MG430</td><td>phosphoglycerate mutase (pgm)</td></tr><tr><td>MG161</td><td>ribosomal protein L14</td><td>MG431</td><td>triosephosphate isomerase (tpiA)</td></tr><tr><td>MG162</td><td>ribosomal protein L24</td><td>MG433</td><td>Transcription elongation factor Ts</td></tr><tr><td>MG163</td><td>ribosomal protein L5</td><td>MG437</td><td>CDP-diglyceride synthetase (cdsA)</td></tr><tr><td>MG164</td><td>ribosomal protein S14</td><td>MG444</td><td>ribosomal protein L19</td></tr><tr><td>MG165</td><td>ribosomal protein S8</td><td>MG446</td><td>ribosomal protein S16</td></tr><tr><td>MG166</td><td>ribosomal protein L6</td><td>MG451</td><td>Transcription elongation factor Tu</td></tr><tr><td>MG167</td><td>ribosomal protein L18</td><td>MG455</td><td>Tyrosine-tRNA ligase</td></tr><tr><td>MG168</td><td>ribosomal protein S5</td><td>MG460</td><td>L-lactate dehydrogenase (ldh)</td></tr><tr><td>MG173</td><td>translation initiation factorl</td><td>MG462</td><td>Glutamate-tRNA ligase</td></tr><tr><td>MG174</td><td>ribosomal protein L36</td><td>MG466</td><td>ribosomal protein L34</td></tr><tr><td>MG175</td><td>ribosomal protein S13</td><td>SCMNPK</td><td>Nucleoside-phosphate kinase</td></tr><tr><td>MG176</td><td>ribosomal protein S11</td><td>ECNDK</td><td>Nucleoside-diphosphate kinase</td></tr><tr><td>MG177</td><td>RNA polymerase alpha core subunit</td><td>ECGLNS</td><td>Glutamine-tRNA ligase</td></tr><tr><td>MG178</td><td>ribosomal protein L17</td><td>T0001</td><td>Acylglycerol lipase</td></tr><tr><td>MG194</td><td>Phenylalanine-tRNA ligase alpha</td><td>T0002</td><td>Glycerol-1-phosphatase</td></tr><tr><td>MG196</td><td>transltion initiation factor3</td><td>ECPGPB</td><td>Phosphatidylglycerophosphatase</td></tr><tr><td>MG197</td><td>ribosomal protein L35</td><td>ECDGKA</td><td>Diacylglycerol kinase (dgkA)</td></tr><tr><td>MG198</td><td>ribosomal protein L20</td><td></td><td></td></tr></table>

and KEGG (Kanehisa, 1996). Both of these knowledgebases provide links between information on genes, enzymes and metabolic pathways which proved essential in our effort to construct a model cell.

Table 3. Enzymes in the hypothetical cell
<table><tr><td>ID</td><td>name</td></tr><tr><td>EC1.1.1.27</td><td>L-Lactate dehydrogenase</td></tr><tr><td>EC1.2.1.12</td><td>Glyceraldehyde-3-phosphate dehydrogenase (phosphorylating)</td></tr><tr><td>EC2.1.2.9</td><td>Methionyl-tRNA formyltransferase</td></tr><tr><td>EC2.7.1.107</td><td>Diacylglycerol kinase</td></tr><tr><td>EC2.7.1.11</td><td>6-Phosphofructasokinase</td></tr><tr><td>EC2.7.1.30</td><td>Glycerol kinase</td></tr><tr><td>EC2.7.1.40</td><td>Pyruvate kinase</td></tr><tr><td>EC2.7.1.69</td><td>phosphotransferasesystem enzyme II, ABC component(ptsG)</td></tr><tr><td>EC2.7.2.3</td><td>Phosphoglycerate kinase</td></tr><tr><td>EC2.7.3.9</td><td>phosphoenolpyruvate-proteinphosphotransferase(ptsI)</td></tr><tr><td>EC2.7.4.4</td><td>Nucleoside-phosphate kinase</td></tr><tr><td>EC2.7.4.6</td><td>Nucleoside-diphosphate kinase</td></tr><tr><td>EC2.7.7.41</td><td>CDPdiglyceride pyrophosphorylase</td></tr><tr><td>EC2.7.8.5</td><td>CDPdiacylglycerol-glycerol-3-phsophate 3-phosphatidyltransferase</td></tr><tr><td>EC3.1.1.23</td><td>Acylglycerol lipase</td></tr><tr><td>EC3.1.1.3</td><td>Lipase</td></tr><tr><td>EC3.1.3.21 EC3.1.3.27</td><td>Glycerol-1-phosphatase</td></tr><tr><td>EC3.6.1.1</td><td>Phosphatidylglycerophosphatase</td></tr><tr><td>EC3.6.1.1</td><td>Inorganic pyrophosphatase Pyrophosphatase</td></tr><tr><td>EC4.1.2.13</td><td></td></tr><tr><td>EC4.2.1.11</td><td>Fructose-bisphosphate aldolase</td></tr><tr><td>EC5.3.1.1</td><td>Phosphopyruvate hydratase</td></tr><tr><td>EC5.3.1.9</td><td>Triose-phosphate isomerase</td></tr><tr><td>EC5.4.2.1</td><td>Glucose-6-phosphate isomerase</td></tr><tr><td>EC6.1.1.1</td><td>Phosphoglycerate mutase Tyrosine-tRNA ligase</td></tr><tr><td>EC6.1.1.10</td><td>Methionine-tRNA ligase</td></tr><tr><td>EC6.1.1.11</td><td>Serine-tRNA ligase</td></tr><tr><td>EC6.1.1.12</td><td>Aspartate-tRNA ligase</td></tr><tr><td>EC6.1.1.14</td><td></td></tr><tr><td>EC6.1.1.15</td><td>Glycine-tRNA ligase Proline-tRNA ligase</td></tr><tr><td>EC6.1.1.16</td><td>Cysteine-tRNA ligase</td></tr><tr><td>EC6.1.1.17</td><td></td></tr><tr><td>EC6.1.1.18</td><td>Glutamate-tRNA ligase</td></tr><tr><td>EC6.1.1.19</td><td>Glutamine-tRNA ligase</td></tr><tr><td></td><td>Arginine-tRNA ligase</td></tr><tr><td>EC6.1.1.2</td><td>Tryptophan-tRNA ligase</td></tr><tr><td>EC6.1.1.20</td><td>Phenylalanine-tRNA ligase</td></tr><tr><td>EC6.1.1.21</td><td>Histidine-tRNA ligase</td></tr><tr><td>EC6.1.1.22</td><td>Asparagine-tRNA ligase</td></tr><tr><td>EC6.1.1.3</td><td>Threonine-tRNA ligase</td></tr><tr><td>EC6.1.1.4 EC6.1.1.5</td><td>Leucine-tRNA ligase</td></tr><tr><td>EC6.1.1.6</td><td>Isoleucine-tRNA ligase</td></tr><tr><td>EC6.1.1.7</td><td>Lysine-tRNA ligase</td></tr><tr><td></td><td>Alanine-tRNA ligase</td></tr><tr><td>EC6.1.1.9</td><td>Valine-tRNA ligase</td></tr></table>

KEGG was first used to construct the overall structure of the model cell’s metabolism based on the gene set of M.genitalium as determined by Fraser et al. (1995). KEGG has a large collection of species-non-specific metabolic pathway diagrams, and provides the utility of highlighting the enzymes which are known/thought to be present in a species of interest. We retrieved diagrams for all of the metabolic pathways which are present in M.genitalium according to KEGG, and manually constructed a single comprehensive network diagram of M.genitalium (not shown).

For our purpose, EcoCyc proved highly useful in obtaining more detailed information about the enzymes and pathways.

Although EcoCyc itself does not include kinetic information, its rich references to the literature enabled us to obtain much of the further information we required to build the model.

## Transcription and translation

Complex reactions such as transcription and translation are modeled in detail as a series of reactions, part of which is illustrated in Figure 4.

Since our present model cell does not need to switch the genes on and off, it does not have any regulatory factors, such as repressors and enhancers. We have therefore not implemented gene regulatory reaction rules, although the software itself allows the user to write rules for sophisticated gene regulatory reactions such as repressor proteins binding to DNA regulatory regions.

Table 4. Small molecules in the hypothetical cell
<table><tr><td>ID name</td><td></td><td>ID name</td><td></td></tr><tr><td>C00001</td><td>H2O</td><td>C00148</td><td>L-Proline</td></tr><tr><td>C00002</td><td>ATP</td><td>C00152</td><td>L-Asparagine</td></tr><tr><td>C00003</td><td>NAD+</td><td>C00162</td><td>Fatty acid</td></tr><tr><td>C00004</td><td>NADH</td><td>C00165</td><td>Diacyl-glycerol</td></tr><tr><td>C00008</td><td>ADP</td><td>C00183</td><td>L-Valine</td></tr><tr><td>C00009</td><td>Orthophosphate</td><td>C00186</td><td>(S)-Lactate</td></tr><tr><td>C00013</td><td>Pyrophosphate</td><td>C00188</td><td>L-Threonine</td></tr><tr><td>C00015</td><td>UDP</td><td>C00197</td><td>3-Phospho-D-glycerate</td></tr><tr><td>C00020</td><td>AMP</td><td>C00234</td><td>10-Formyltetrahydrofolate</td></tr><tr><td>C00022</td><td>Pyruvate</td><td>C00236</td><td>3-Phospho-D-glycerate phosphate</td></tr><tr><td>C00025</td><td>L-Glutamate</td><td>C00269</td><td>CDPdiacylglycerol</td></tr><tr><td>C00031 C00035</td><td>D-Glucose</td><td>C00305</td><td>Mg2+</td></tr><tr><td></td><td>GDP</td><td>C00344</td><td>Phosphotidylglycerol</td></tr><tr><td>C00037 C00041</td><td>Glycine</td><td>C00354</td><td>D-Fructose 1,6-bisphosphate</td></tr><tr><td>C00044</td><td>L-Alanine</td><td>C00407</td><td>L-Isoleucine</td></tr><tr><td>C00047</td><td>GTP</td><td>C00416</td><td>Diacyl-sn-glycerol 3-phosphate</td></tr><tr><td>C00049</td><td>L-Lysine</td><td>C00615</td><td>Protein histidine</td></tr><tr><td>C00055</td><td>L-Aspartate</td><td>C00631</td><td>2-Phospho-D-glycerate</td></tr><tr><td>C00062</td><td>CMP</td><td>C00787</td><td>tRNA(Tyr)</td></tr><tr><td>C00063</td><td>L-Arginine</td><td>C01635</td><td>tRNA(Ala)</td></tr><tr><td>C00064</td><td>CTP</td><td>C01636</td><td>tRNA(Arg)</td></tr><tr><td>C00065</td><td>L-Glutamine</td><td>C01637</td><td>tRNA(Asn)</td></tr><tr><td>C00073</td><td>L-Serine</td><td>C01638</td><td>tRNA(Asp)</td></tr><tr><td>C00074</td><td>L-Methionine</td><td>C01639</td><td>tRNA(Cys)</td></tr><tr><td>C00075</td><td>Phosphoenolpyruvate</td><td>C01640</td><td>tRNA(Gln)</td></tr><tr><td>C00078</td><td>UTP</td><td>C01641</td><td>tRNA(Glu)</td></tr><tr><td>C00079</td><td>L-Tryptophan</td><td>C01642</td><td>tRNA(Gly)</td></tr><tr><td>C00080</td><td>L-Phenylalanine</td><td>C01643</td><td>tRNA(His)</td></tr><tr><td>C00082</td><td>H+</td><td>C01644</td><td>tRNA(Ile)</td></tr><tr><td></td><td>L-Tyrosine</td><td>C01645</td><td>tRNA(Leu)</td></tr><tr><td>C00085 C00092</td><td>D-Fructose 6-phosphate</td><td>C01646</td><td>tRNA(Lys)</td></tr><tr><td>C00093</td><td>D-Glucose 6-phosphate</td><td>C01647</td><td>tRNA(Met)</td></tr><tr><td>C00097</td><td>sn-Glycerol3-Phosphate</td><td>C01648</td><td>tRNA(Phe)</td></tr><tr><td>C00101</td><td>L-Cysteine</td><td>C01649</td><td>tRNA(Pro)</td></tr><tr><td>C00105</td><td>Tetrahydrofolate</td><td>C01650</td><td>tRNA(Ser)</td></tr><tr><td>C00111</td><td>UMP</td><td>C01651</td><td>tRNA(Thr)</td></tr><tr><td></td><td>Glycerone phosphate</td><td>C01652</td><td>tRNA(Trp)</td></tr><tr><td>C00112</td><td>CDP</td><td>C01653</td><td>tRNA(Val)</td></tr><tr><td>C00116</td><td>Glycerol</td><td>C01885</td><td>Monoacyl-glycerol</td></tr><tr><td>C00118</td><td>D-Glyceraldehyde 3-phosphate</td><td>C03294</td><td>N-Formylmethionyl-tRNA</td></tr><tr><td>C00123 C00135</td><td>L-Leucine</td><td>C03892</td><td>Phosphatidylglycerophosphate</td></tr><tr><td></td><td>L-Histidine</td><td>C04085</td><td>Protein N(pai)-phosphohistidine</td></tr><tr><td>C00144</td><td>GMP</td><td></td><td></td></tr></table>

Our current model does not utilize actual nucleotide or amino acid sequence information. Although the length of each gene, mRNA and protein is represented, we have made the assumption that each contains equal proportions of nucleotides and amino acids, respectively. In the current cell model, these simplified reaction rules have produced satisfactory results in simulation, and we plan to sustain this level of abstraction until necessary.

## Reaction kinetics

Generalizing chemical reactions as:

$$
\mathsf { v } _ { 1 } S _ { 1 } + \mathsf { v } _ { 2 } S _ { 2 } + \ldots  \mathsf { v } _ { j } S _ { j } + \ldots + \mathsf { v } _ { n } S _ { n }
$$

![](images/0911efe91f1d9a0504e08b9108e68d0ff6f222fb1404c4eba48e34472c009f15.jpg)  
Fig. 4. The transcription metabolism in the model cell.

where $S _ { n }$ is a concentration of the nth substance and $\nu _ { n }$ is a stoichiometric coefficient for the substance, the velocity of each reaction can be expressed as a function of ${ \bf \nabla } \cdot { \bf S _ { s } }$ and $\nu _ { \mathrm { { s } } } .$

Most non-enzymatic reactions are first-order reactions. Their velocities directly depend on concentrations of the substrates and can be expressed as:

$$
v = k \cdot \prod _ { i } ^ { j - 1 } [ S _ { i } ] ^ { v _ { i } }
$$

where v is the velocity of the reaction and k is the rate constant.

Enzymatic reaction with a substrate and a product can be expressed as the Michaelis–Menten equation:

$$
v = \frac { V _ { \mathrm { m a x } } \cdot [ S ] } { [ S ] + K _ { m } }
$$

where [S] is the substrate concentration, $V _ { \mathrm { m a x } }$ is the maximal velocity of the reaction and $K _ { \mathrm { m } }$ is the Michaelis constant. One can easily derive equations for reactions involving more than one substrate or product, and incorporate the effects of inhibitor(s) and activator(s) under this Henri–Michaelis–

Menten model. For example, the rate equation for a random bi bi reversible enzymatic reaction with an inhibitor and an activator (each product is competitive with each substrate) would be:

$$
\boldsymbol { v } = \frac { \frac { [ S _ { 1 } ] [ S _ { 2 } ] } { \alpha K _ { 1 } K _ { 2 } } { \boldsymbol { V } } _ { \mathrm { f } } - \frac { [ S _ { 3 } ] [ S _ { 4 } ] } { \beta K _ { 3 } K _ { 4 } } { \boldsymbol { V } } _ { \mathrm { r } } } { 1 + \frac { [ S _ { 1 } ] } { K _ { 1 } } + \frac { [ S _ { 2 } ] } { K _ { 2 } } + \frac { [ S _ { 3 } ] } { K _ { 3 } } + \frac { [ S _ { 4 } ] } { K _ { 4 } } + \frac { [ S _ { 1 } ] [ S _ { 2 } ] } { \alpha K _ { 1 } K _ { 2 } } + \frac { [ S _ { 3 } ] [ S _ { 4 } ] } { \beta K _ { 3 } K _ { 4 } } + \frac { [ S _ { 2 } ] [ S _ { 4 } ] } { \gamma K _ { 2 } K _ { 4 } } + \frac { [ S _ { 1 } ] [ S _ { 3 } ] } { \delta K _ { 1 } K _ { 3 } } }
$$

where $K _ { n }$ is the dissociation constant for $S _ { n } , V _ { \mathrm { f } }$ and $V _ { \mathrm { r } }$ are forward and reverse maximal velocity, α, β, γ and $\delta$ are the ratios of dissociation constants of complexes (K<sub>complex</sub>):

$$
\begin{array} { r l } & { \alpha = K _ { [ E S _ { 1 } S _ { 2 } ] } / K _ { [ E S _ { 1 } ] } = K _ { [ E S _ { 1 } S _ { 2 } ] } / K _ { [ E S _ { 2 } ] } , } \\ & { \beta = K _ { [ E S _ { 3 } S _ { 4 } ] } / K _ { [ E S _ { 3 } ] } = K _ { [ E S _ { 3 } S _ { 4 } ] } / K _ { [ E S _ { 4 } ] } , } \\ & { \gamma = K _ { [ E S _ { 2 } S _ { 4 } ] } / K _ { [ E S _ { 2 } ] } = K _ { [ E S _ { 2 } S _ { 4 } ] } / K _ { [ E S _ { 4 } ] } , } \\ & { \delta = K _ { [ E S _ { 1 } S _ { 3 } ] } / K _ { [ E S _ { 1 } ] } = K _ { [ E S _ { 1 } S _ { 3 } ] } / K _ { [ E S _ { 1 } ] } . } \end{array}
$$

Given a reaction mechanism, such equations can be mechanically derived by hand or with the assistance of computer programs. For more complex enzymatic reactions for which rapid equilibrium assumptions are not inadequate, methods such as the King–Altman method can be used (Segel, 1975).

Some reactions, such as dimer formation and DNA–protein binding, reach equilibrium within a millisecond, which is the default single time unit of the system. For a rapid equilibrium such as:

$$
\mathsf { v } _ { 1 } S _ { 1 } + \mathsf { v } _ { 2 } S _ { 2 } + \ldots + \mathsf { v } _ { n } S _ { n } \Longleftrightarrow C
$$

where $C$ is a complex, the following equation holds at equilibrium:

$$
K _ { \mathrm { d } } \cdot [ C ] = \prod _ { i } ^ { n } [ S _ { i } ] ^ { \nu _ { i } }
$$

where $K _ { \mathrm { d } }$ is the dissociation constant of the reaction. This equation provides a simple way to compute directly the concentration of each molecular species at equilibrium by only one dissociation constant, i.e. it assumes the binding of more than two Substances to occur simultaneously. However, in reality, the formation of molecular complexes with many components occurs in a stepwise fashion, and in some cellular processes, such as protein signaling, a more detailed representation may be necessary for accurate simulation (Bray et al., 1997). Since we have not implemented any complex signaling pathways in our present cell model, we feel that the use of the simple equation above is justified.

Although some kinetic parameter values can be derived from information available in existing databases, many are unknown. We have assigned values for these parameters by estimations based on available information. Barkai and Leibler (1997) have recently argued that cellular processes are ‘robust’ in many of their properties, in the sense that considerable variation in kinetic parameters often does not affect the behavior of the system as a whole. Many of our simulation results are consistent with their argument; increasing or decreasing a particular parameter by one order of magnitude seldom changes the qualitative behavior of our model cell.

![](images/55c377ea6100a15bf0ae91ba50d4a949dc70b772769048899413e4d1a9321101.jpg)  
Fig. 5. The quantity of ATP increases temporarily and then decreases rapidly when glucose in the culture medium is completely drained at 20 s. The y-axis is the number of ATP molecules (×1000) in the cytoplasm and the x-axis is the elapsed time in seconds.

## Virtual experiments

The E-CELL interfaces provide a means of conducting ‘experiments in silico’. For example, we can ‘starve’ the cell by draining glucose from the culture medium. The cell would eventually ‘die’, running out of ATP. If glucose is added back, it may or may not recover, depending on the duration of starvation. We can also ‘kill’ the cell by knocking out an essential gene for, for example, protein synthesis. The cell would become unable to synthesize proteins, and all enzymes would eventually disappear due to spontaneous degradation.

Figure 5 is a trace of the quantity of ATP in the starving cell. Glucose in the culture medium was drained at 20 s. It is interesting that the quantity of ATP temporarily increases at the initiation of starvation. This is explained by the fact that some ATP is consumed in the glycolysis pathway before it produces enough ATP for a net increase. The shortage of glucose to fuel glycolysis arrests the ATP consumption at the beginning of the pathway before the intermediates for ATP production are completely consumed. This results in a temporary increase of net ATP in the cytoplasm. After a short period, however, the quantity of ATP falls sharply.

Figure 6 is a trace of the quantity of mRNA, in which the cell was starved at 1000 s. Messenger RNA levels are usually close to steady state due to continuing transcription and degradation. When the cell runs out of ATP after starvation, transcription can no longer continue and mRNAs are rapidly lost by degradation.

![](images/f58ebdc91f0bd1b68d01cfeb894f41f3372758c3f28a8bf95c5358372b39f2a1.jpg)  
Fig. 6. A trace of mRNA levels before and after starvation of the cell. Before starvation at 1000 s, synthesis by transcription and spontaneous degradation are close to equilibrium. The loss of ATP following starvation causes transcription to stop, and mRNA levels decrease rapidly.

## Application to genome engineering

One of our ultimate goals is to model the real cell of M.genitalium, the organism having the smallest known chromosome. Because of the small number of genes (470 proteins, 37 RNAs), M.genitalium is a prime candidate for exhaustive functional (proteome) analysis. Because there are still many genes whose functions are not yet known, it will probably be necessary to hypothesize putative proteins to complement missing metabolic functions, in order for the model cell to work in silico.

## Metabolic requirements

The assessment of the metabolic requirements of the cell is an excellent example of a potential application for E-CELL. At present, M.genitalium is grown in a complex medium containing several chemically undefined components including fetal bovine serum, and also extracts of yeast and beef. The problem of designing a chemically defined growth medium could be addressed through a purely empirical approach. However, a more interesting approach is one that is informed by knowledge of the complete genome sequence. By combining knowledge of the metabolic enzymes present in the cell with information concerning protein transporters of metabolites across the cell membrane, it should be possible to evaluate whether a particular defined medium can support growth, by using the E-CELL model. The main difficulty in this approach is that identification of gene function solely on the basis of sequence is uncertain. Comparison of laboratory results with E-CELL predictions should help to overcome this difficulty. Agreement between the model and laboratory growth experiments will be evaluated for a large number of different chemically defined media. Differences between experimental observations and the E-CELL predictions will be used to refine the model. This could lead to the identification of new enzymes or transporters among genes with previously unassigned roles, or to the removal of a questionable role assignment based on a marginal level of sequence similarity.

## Gene expression

Another area in which we plan to apply the E-CELL software is in the deciphering of gene regulatory networks. Gene expression patterns of M.genitalium are currently being determined at TIGR under a variety of growth conditions. We expect that these results will suggest specific mechanisms for control of transcript levels which can be modeled by rules in the E-CELL system. We will conduct parallel experiments in the laboratory and in silico with the E-CELL system; given an appropriate model of the cell, we can change initial values of ingredients of the culture medium and observe increases and decreases of mRNA levels. The results of those in silico experiments should be consistent with results of biological and biochemical experiments. The computer model will then be refined as necessary.

## Minimal gene set

We expect that the E-CELL system will be useful in defining the minimal set of genes required for a self-replicating cell under a specific set of laboratory conditions. At TIGR, work is under way to identify the genes of M.genitalium which are non-essential, by gene disruption experiments using transposons. If the E-CELL model is sufficiently detailed and accurate, then these gene disruption experiments can be modeled in silico to predict a minimal gene set. The laboratory experiments will lead to the prediction of a reduced gene set which should be a close approximation to the truly minimal Mycoplasma genome. Alternative predictions of a minimal gene set can also be proposed on theoretical grounds, or by deducing a core set of genes conserved between M.genitalium and other microbial genomes. The E-CELL system should be useful in modeling cells based on these alternative proposals for a minimal cellular genome.

We expect that a combination of laboratory experiments and in silico modeling using the E-CELL system will lead to a more reliable prediction of the minimal gene complement for a self-replicating cell than could be obtained by either method alone.

## Concluding remarks

We have constructed a hypothetical cell using the first version of E-CELL, and have developed hundreds of reaction rules for a partial set of metabolic pathways of M.genitalium, including glycolysis, lactate fermentation, glycose uptake, glycerol and fatty acid uptake, phospholipid biosynthesis, gene transcription, protein synthesis, polymerase and ribosome assembly, protein degradation and mRNA degradation.

Our model cell’s gene set of 127 genes is much smaller than the ‘minimal gene set’ derived through sequence comparison of the first two sequenced genomes (Fleischman et al., 1995; Fraser et al., 1995) by Musheginan and Koonin (1996). This is not surprising since our model lacks several important features present in all real living cells. The model cell does not proliferate; we are currently modeling cell growth, DNA replication, chromosome segregation and cell division. (The next version of the E-CELL system will have features to support modeling cell division, including dynamic compartment creation/deletion, programmable compartment volume, dynamic reactor/substance creation/deletion, and dynamic DNA sequence representation.)

Furthermore, the present cell model relies on unrealistically favorable environmental conditions. All of the amino acids and nucleotides must exist, and pH and osmolarity must be kept at physiologically stable levels at all times. The model also lacks cell structure proteins, which would be indispensable in any natural environment.

To address these problems, we are currently modeling amino acid and nucleotide biosynthesis pathways. We also plan to model homeostasis of pH and osmolarity, as well as proteins for membrane and cell structure.

An additional point which is worth mentioning is that although simulation is the primary focus of this research, the modeling process has involved much knowledge integration. Although our efforts to gather extensive information on a single organism, M. genitalium, involved much manual methods (e.g. creating diagrams of metabolic networks) and are not, of course, completely automated, we have derived many routine protocols for modeling pathways. We would like to integrate E-CELL’s knowledge representation scheme with the schemes of knowledgebases such as EcoCyc and KEGG to facilitate and, where applicable, automate information retrieval, which has proven to be a largely time-consuming part of the modeling process.

The applications of E-CELL, such as genome engineering, have only just begun. The approaches to defining a minimal gene set, described in ‘User interfaces’, are testable in principle. At TIGR a longer term goal of this work is the engineering of the genome to produce living cells with substantially reduced genomes. This will allow us to test proposals for minimal gene sets directly. It will be interesting to compare real cells so created with their computer models. Comparison of the models with the results of laboratory experiments will allow further refinement of the computer models. This, in turn, will lead to a better understanding of the experimental results, and hence a better understanding of the essential requirements of a minimal living cell.

## Acknowledgements

We would like to thank Peter Karp and Doug Brutlag for useful comments on the early draft of this paper. Masanori Arita kindly helped us in reviewing literature on biological simulations. Many of the ideas presented in this paper were inspired by discussions with other E-CELL project members of Tomita Lab. at Keio University, including Junko Shinada, Keiko Miura, Hisako Nakano, Daisuke Kamiyoshikawa, Ryo Matsushima, Akiko Kawase, Naoko Watanabe, Ken Satoyoshi and Yusuke Saito. We also thank for useful comments Scott Peterson and Karen Ketchum of the Institute for Genomic Research, as well as Nobuyoshi Shimizu and his colleagues at the Department of Molecular Biology, Keio University.

This work was supported by the Eizai Research Institute and also in part by a Grant-in-Aid for Scientific Research on Priority Areas ‘Genome Science’ from the Ministry of Education and Science in Japan, as well as a Travelling Fellowship from the Company of Biologists for T.S.S.

## References

Arita,M., Hagiya,M. and Shiratori,T. (1994) GEISHA SYSTEM: an environment for simulating protein interaction. In Takagi,T. (ed.), Proceedings, Genome Informatics Workshop 1994. Universa Academy Press, Tokyo, pp. 81–89.

Barkai,N. and Leibler,S. (1997) Robustness in simple biochemica networks. Nature, 387, 913–917.

Barshop,B.A., Wrenn,R.F. and Frieden,C. (1983) Analysis of numerical methods for computer simulation of kinetic processes: development of KINSIM—a flexible, portable system. Anal. Biochem., 130, 134–145.

Bray,D. (1998) SIGNALING COMPLEXES: Biophysical constraints on intracellular communication. Annu. Rev. Biophys. Biomol. Struct., 27, 59–75.

Bray,D., Bourret,R.B. and Simon,M.I. (1993) Computer simulation of the phosphorylation cascade controlling bacterial chemotaxis. Mol. Biol. Cell, 4, 469–482.

Cornish-Bowden,A. and Hofmeyr,J.H. (1991) MetaModel: a program for modeling and control analysis of metabolic pathways on the IBM PC and compatibles. Comput. Applic. Biosci., 7, 89–93.

Dang,Q. and Frieden,C. (1997) New PC versions of the kinetic-simulation and fitting programs, KINSIM and FITSIM. Trends Biochem. Sci., 22, 317.

Ehlde,M. and Zacchi,G. (1995) MIST: a user-friendly metabolic simulator. Comput. Applic. Biosci., 11, 201–207.

Fleischmann,R.D. et al. (1995) Whole-genome random sequencing and assembly of Haemophilus influenzae Rd. Science, 269, 496–512.

Fraser,C.M. et al. (1995) The minimal gene complement of Mycoplasma genitalium. Science, 270, 397–403.

Galper,A.R., Brutlag,D.L. and Millis,D.H. (1993) Knowledge-based simulation of DNA metabolism: prediction of action and envisionment of pathways. In Hunter,L. (ed.), Artificial Intelligence and Molecular Biology. AAAI Press/The MIT Press, CA/MA, pp. 429–436.

Kanehisa,M. (1996) Toward pathway engineering: a new database of genetic and molecular pathways. Sci. Technol. Jpn, 59, 34–38.

Karp,P.D. (1993) A qualitative biochemistry and its application to the regulation of the tryptophan operon. In Hunter,L. (ed.), Artificial Intelligence and Molecular Biology. AAAI Press/The MIT Press, CA/MA, pp. 289–324.

Karp,P.D., Riley,M., Paley,S.M. and Pelligrini-Toole,A. (1996) Eco-Cyc: encyclopedia of E.coli genes and metabolism. Nucleic Acids Res., 24, 32–40.

Kuipers,B. (1986) Qualitative simulation. Artif. Intell., 29, 289–338.

McAdams,H.H. and Shapiro,L. (1995) Circuit simulation of genetic networks. Science, 269, 650–656.

Mendes,P. (1993) GEPASI: a software package for modeling the dynamics, steady states and control of biochemical and other systems. Comput. Applic. Biosci., 9, 563–571.

Mendes,P. (1997) Biochemistry by numbers: simulation of biochemical pathways with Gepasi 3. Trends Biochem. Sci., 22, 361–363.

Meyers,S. and Friedland,P. (1984) Knowledge-based simulation of genetic regulation in bacteriophage lambda. Nucleic Acids Res., 12, 1–9.

Mushegian,A.R. and Koonin,E.V. (1996) A minimal gene set for cellular life derived by comparison of complete bacterial genomes. Proc. Natl Acad. Sci. USA, 93, 10268–10273.

Novak,B. and Tyson,J.J. (1995) Quantitative analysis of a molecular model of mitotic control in fission yeast. J. Theor. Biol., 173, 283–305.

Sauro,H.M. (1993) SCAMP: a general-purpose simulator and metabolic control analysis program. Comput. Applic. Biosci., 9, 441–450.

Segel,I.H. (1975) Enzyme Kinetics: Behavior and Analysis of Rapid Equilibrium and Steady State Enzyme Systems. John Wiley & Sons, New York.

Tyson,J.J. (1991) Modeling the cell division cycle: cdc2 and cyclin interactions. Proc. Natl Acad. Sci. USA, 88, 7328–7332.