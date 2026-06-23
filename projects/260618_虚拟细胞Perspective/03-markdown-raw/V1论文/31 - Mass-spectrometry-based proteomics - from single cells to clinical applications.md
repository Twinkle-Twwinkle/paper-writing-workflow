# Mass-spectrometry-based proteomics: from single cells to clinical applications

https://doi.org/10.1038/s41586-025-08584-0

Tiannan Guo<sup>1,2,3 ✉</sup>, Judith A. Steen<sup>4,5 ✉</sup> & Matthias Mann<sup>6,7 ✉</sup>

Received: 5 May 2024

Accepted: 2 January 2025

Published online: 26 February 2025

Check for updates

Mass-spectrometry (MS)-based proteomics has evolved into a powerful tool for comprehensively analysing biological systems. Recent technological advances have markedly increased sensitivity, enabling single-cell proteomics and spatial profling of tissues. Simultaneously, improvements in throughput and robustness are facilitating clinical applications. In this Review, we present the latest developments in proteomics technology, including novel sample-preparation methods, advanced instrumentation and innovative data-acquisition strategies. We explore how these advances drive progress in key areas such as protein–protein interactions, post-translational modifcations and structural proteomics. Integrating artifcial intelligence into the proteomics workfow accelerates data analysis and biological interpretation. We discuss the application of proteomics to single-cell analysis and spatial profling, which can provide unprecedented insights into cellular heterogeneity and tissue architecture. Finally, we examine the transition of proteomics from basic research to clinical practice, including biomarker discovery in body fuids and the promise and challenges of implementing proteomics-based diagnostics. This Review provides a broad and high-level overview of the current state of proteomics and its potential to revolutionize our understanding of biology and transform medical practice.

Proteomics, the study of all proteins in a biological system, is foundational to biomedical research, along with genomics, transcriptomics and metabolomics, and provides unique insights into cellular function and disease mechanisms. As the direct effector of biological functions and phenotypes, the proteome reflects the complex interplay between genetic predisposition, environmental factors and lifestyle influences. Whereas genomics and transcriptomics inform on cellular potential, and metabolomics focuses on downstream small molecules, proteomics directly interrogates the functional machinery inside and outside cells.

Although genomics has been the central focus of the past 20 years, the importance of proteomics is becoming more and more evident<sup>1</sup>. The increased complexity at the protein level is due to alternative splicing, varying translation rates, post-translational modifications (PTMs) and proteolytic cleavage. The resulting proteome is reflective of the interplay among genetics, lifestyle and environment, and provides structural, signalling, transport and catalysis functions attuned to its immediate conditions. This complexity necessitates dedicated methodologies for comprehensive proteomic analysis.

Among the approaches that are used to study the proteome, mass spectrometry (MS)-based proteomics has emerged as a powerful and versatile tool. Unlike affinity-based methods<sup>2–4</sup>, MS-based proteomics directly identifies and quantifies amino acid sequences, offering unbiased, systematic analyses of protein expression, modifications and interactions across various conditions<sup>5,6</sup> (Box 1). Its strengths include unrivalled quantitative accuracy, specificity and universal applicability across all organisms without requiring specific binding reagents or previous system knowledge except a sequenced genome.

Recent technological advances have overcome many previous limitations, including completeness of proteome characterization, workflow robustness, throughput and sample quantity requirements. These improvements have expanded the scope of proteomics from bulk analyses to single-cell studies and spatial profiling, providing remarkable insights into cellular heterogeneity and tissue organization.

This Review provides a broad but not exhaustive overview of the current MS-based proteomics workflow, highlighting key technological improvements and emerging capabilities since we last reviewed the field<sup>6</sup>. We explore applications in structural proteomics, PTMs, single-cell and spatial analysis and body fluid profiling. We also discuss the transition of proteomics from basic research to clinical practice, including the remaining challenges in implementing proteomics-based diagnostics. Throughout, we emphasize the transformative effect of artificial intelligence (AI) on data analysis and interpretation, concluding with an outlook on exciting future directions in proteomics research.

## The technology of MS-based proteomics

The typical MS-based proteomics workflow consists of four main stages: (i) protein extraction and enzymatic digestion into peptides; (ii) peptide separation by chromatography; (iii) ionization by electrospray<sup>7</sup> followed by mass analysis of peptides (MS1) and their fragments (MS2);

<table><tr><td colspan="2">Box 1</td></tr><tr><td colspan="2">Glossary</td></tr><tr><td>Activity-based protein profiling (ABPP): Chemical probe-based measurement of enzyme activity in complex proteomes.Chemoproteomics: Study of protein-small molecule interactions across the proteome, used in drug discovery.Cross-linking mass spectrometry (XL-MS): Links proximal amino acids to study protein structure and interactions through MS.Data-dependent acquisition (DDA): MS method selecting ions by abundance for fragmentation.Data-independent acquisition (DIA): MS method fragmenting all ions within mass range windows systematically, regardless of abundance, enabling complex mixture analysis.Deep visual proteomics (DVP): Integration of microscopy, AI and MS for single-cell-type proteomic characterization.Electrospray ionization: Soft ionization technique producing gas-phase ions from liquid samples.FFPE tissues: Formalin-fixed paraffin-embedded tissues for long-term storage, compatible with various analytical methods.Hydrogen-deuterium exchange (HDX): Measures H-D exchange in proteins to study structure and dynamics.Immunohistochemistry (IHC): Antibody-based detection of proteins in tissue sections.Ion mobility: Gas-phase separation technique distinguishing ions by size, shape and charge, enabling improved separation.Isobaric tags: Chemical labels with identical masses but different fragmentation patterns for protein quantification.Label-free quantification: MS-based protein quantification without isotope labelling, using algorithmic signal comparison.Limited proteolysis: Controlled and deliberately incomplete protein digestion to study structure and conformational changes.</td><td>Liquid chromatography (LC): Separation technique using liquid mobile phase and specialized columns, coupled to MS through electrospray.Mass spectrometry (MS): Technique measuring the mass-to-charge ratio of ions for molecular identification and quantification.Orbitrap analyser: High-resolution mass analyser using electrostatic fields to measure ion oscillations.Parallel accumulation-serial fragmentation (PASEF): Advanced acquisition method synchronizing ion mobility separation with MS/MS analysis.Post-translational modifications (PTMs): Chemical modifications of proteins after synthesis, affecting function and location.Proteomics: Large-scale study of protein structure, function, interactions and expression in biological systems.Proximity labelling: Enzymatic tagging of proteins near a cellular protein of interest, often using biotin for MS analysis.Single-cell proteomics: Analysis of protein content of individual cells, revealing cellular heterogeneity—currently limited to expression proteomics.Spatial profiling: Analysis of protein distribution while preserving spatial context in tissues and cells.Spectral library: Reference collection of mass spectra for peptide identification in DIA, increasingly using deep learning.Tandem mass tags (TMTs): Specific isobaric tags for multiplexed quantitative proteomics.Targeted analysis: Selective MS analysis of preselected peptides for enhanced sensitivity and speed.Thermal protein profiling (TPP): MS-based analysis of heat-induced protein denaturation to study drug-protein interactions.Time-of-flight (TOF) analyser: Mass analyser measuring ion flight time to determine mass-to-charge ratios.</td></tr></table>

and (iv) computational data analysis (Fig. 1). Recent advances in each of these stages have markedly improved the sensitivity, throughput and robustness of proteomic analyses.

Sample preparation has seen notable automation and standardization. Parallel processing in 96-well formats and liquid handling robots enable high-throughput, reproducible workflows with minimal manual intervention. Novel approaches such as digestion on beads have solved the challenge of detergent removal, crucial for complete protein solubilization without interfering with MS<sup>8,9</sup>. Even formalin-fixed paraffin-embedded (FFPE) tissues and archaeological samples can now be effectively analysed, expanding the range of accessible sample types<sup>10–13</sup>.

Liquid chromatography (LC) separation, historically a bottleneck in proteomics workflows, has notably improved. Shifting from nanolitre to microlitre flow rates enhances robustness without unduly compromising sensitivity, thanks to the increased sensitivity of modern mass spectrometers<sup>14</sup>. The Evosep One system, which uses preformed gradients, exemplifies this trend, allowing the analysis of 30 to 100+ samples per day with high reproducibility<sup>15</sup>. Another innovation is the μPAC chip system, which replaces packed columns with chip columns created by microlithography, ensuring consistent peptide retention times across laboratories<sup>16</sup>. Thus, we now have very robust proteomics workflows ready to move out of specialized laboratories.

MS instrumentation continues to advance at a remarkable pace. Although the Orbitrap analyser remains prevalent<sup>17,18</sup>, time-of-flight (TOF) analysers have experienced an impressive revival. The timsTOF instrument, using parallel accumulation–serial fragmentation (PASEF) technology, separates and concentrates peptide ions through ion mobility to increase the percentage of ions sequenced<sup>19</sup>. The Astral analyser is a multi-reflection TOF that is combined with an Orbitrap for MS1 analysis. It features nearly lossless detection of ions once they enter the initial quadrupole, enabling exceptional resolution and sensitivity and representing another leap in MS technology<sup>20,21</sup>.

Data-acquisition strategies have evolved to address the limitations of conventional data-dependent acquisition (DDA). Data-independent acquisition (DIA) has gained prominence, selecting sequential windows across the entire mass-to-charge range and fragmenting all peptides in each cycle<sup>22,23</sup>. Also compatible with ion mobility<sup>24</sup>, this approach overcomes the stochasticity of DDA, reducing missing values between runs. Conversely, the spectra are much more complex than in DDA and must be scored against empirical or predicted peptide libraries<sup>25</sup>. Advanced algorithms, often using machine or deep learning, have greatly improved the interpretation of complex DIA spectra, nearly doubling peptide identifications in some cases<sup>26–30</sup>. For accurate quantification, the time for completing a cycle of the chosen mass range should be kept sufficiently short to result in at least four and, ideally, closer to ten data points across the eluting peptide peaks. DIA has now become a method of choice for most applications.

New scan modes for DIA, such as sliding window approaches, promise to provide even purer fragmentation spectra than DDA, while offering the benefits of multiple measurements across elution peaks<sup>31,32</sup>. Although these innovations are not yet widely available, they will be particularly valuable for exploring the ‘dark proteome’—proteins or peptide forms not recorded in standard databases. This includes verifying the expression of alternatively spliced proteins, identifying unexpected modifications and detecting non-canonical translation products under stress conditions. Moreover, these techniques will advance the field of peptidomics, which encompasses MHC class I/ II-bound or other biologically active peptides<sup>33–36</sup>.

![](images/6d0775319cf1f5b335042aad2f2b1143166af393ef225939666998253aacb8df.jpg)  
Fig. 1 | Basic MS-based proteomics workflow, highlighting technological advances. Proteins are extracted from samples including single cells, tissues and body fluids, and digested into peptides with specific proteolytic enzymes. When multiplexing, the peptides are labelled chemically using stable-isotopelabelled tags. Robotic automation of the sample-preparation process enhances robustness and throughput in proteomic analyses. The labelled or label-free peptide mixtures are then subjected to advanced LC, including micro-pillar array columns (µPAC) and LC with preformed gradients. The separated peptides elute from the LC system at different retention time (RT) and undergo DDA or  
DIA analysis for discovery applications, or targeted MS for non-discovery applications such as clinical assays. The MS hardware depicted includes the latest hybrid instruments, such as the timsTOF and Astral instruments, which combine trapped ion mobility separation or Orbitrap with TOF mass analysers to facilitate enhanced protein identification and quantification. This workflow feeds into applications that explore protein interaction networks and enable comprehensive organismal proteome studies, linking molecular data to biological function and disease mechanisms.

That said, DDA is still widely used for diverse small-scale proteomic experiments such as affinity-purified samples, and cross-linked samples for protein structure analysis. DDA-based protein quantification using isobaric tags—particularly tandem mass tags (TMTs)—continues to be a mainstay quantification technology in which up to 32 samples can now be compared directly. Data interpretation is intuitive, but narrow precursor selection or an additional MS3 fragmentation stage should be used to avoid cross-talk of unrelated peptides or isotopes into the same reporter channels, which can distort quantitative ratios<sup>37–40</sup>.

Targeted proteomics remains crucial for clinical applications, allowing sensitive and absolute quantification of specific peptides<sup>41,42</sup>. It can now be scaled to measure hundreds of samples on a single instrument per day using short LC gradients and target thousands of peptides in a single run<sup>43</sup>. We believe the time has come for the community to provide a proteome-wide heavy proteome resource, which would greatly benefit the field for workflow-independent absolute quantification and for quick independent verification for proteins or special biological or clinical importance.

AI is revolutionizing every aspect of the proteomics workflow<sup>11,44</sup>. Deep-learning algorithms accurately predict peptide behaviour along the proteomics workflow, enhancing confidence in identifications and quantifications; examples include predicting time and order for peptide elution times, or predicting which peptides are proteotypic. AI also has a crucial role in extracting biomarker candidates and facilitating biological interpretation of results<sup>45</sup>. Integrating large language models (LLMs) such as ChatGPT promises to accelerate data interpretation and hypothesis generation further, given their very large knowledge base across biology and medicine. Furthermore, LLMs can be taught to work together with statistical tools used in proteomics and grounded in knowledge graphs<sup>46</sup>, reducing hallucinations.

These technological advances have transformed MS-based proteomics into a robust, high-throughput and highly sensitive analytical platform. Analysing minute sample amounts with unprecedented depth, accuracy and robustness opens new avenues in biological research and clinical applications, from single-cell studies to large-scale clinical trials.

## Applications of MS-based proteomics

The above technological advances in MS-based proteomics have markedly expanded its applications across biological and medical research domains. This section explores the major areas in which proteomics notably contributes to our understanding of biology and medicine.

## Expression proteomics

Understanding how the proteome changes in response to risk factors for a disease, including lifestyle, gene variants, environmental toxins and infections, can inform the development of therapeutics and companion diagnostics. Expression proteomics, the large-scale study of protein abundance changes across different conditions or cell types, has become increasingly comprehensive and quantitative, and provides complementary and different information from the transcriptome. In human cell lines, cutting-edge technologies can now quantify more than 10,000 protein groups with minimal measuring time and sample amounts. Adding upfront fractionation yielded near-comprehensive proteomes of more than 13,000 protein groups, indicating that common cell lines express at least 70% of the 20,000 human protein-coding genes<sup>47,48</sup>. These studies also revealed that cell-line proteomes are remarkably similar, unlike their tissue counterparts<sup>49</sup>. Furthermore, the proteome has turned out to be a close proxy for the functional state of a cell. The Human Proteome Project has found protein-level evidence for 90% of all protein-coding genes, validating and expanding our understanding of the expressed genome<sup>50</sup>. MS has verified the existence of small, unannotated open reading frames that had been predicted by ribosome profiling and indicated that they sometimes function as regulators of protein complexes<sup>51</sup>.

The relationship between the transcriptome and the proteome has been intensely studied. Improved accuracy in both proteomics and transcriptomics measurements should have increased reported correlations by reducing independent experimental noise, but this does not seem to have happened<sup>52</sup>. Instead, it has become apparent that transcriptome and proteome regulation are distinct in many dynamic situations, such as during development or disease progression<sup>53</sup>. Secreted proteins represent another area in which transcriptome– proteome correlations are often low; these proteins have crucial roles in circulation and the microenvironment and can be directly measured by proteomics<sup>54</sup>. Chromatin proteomics and the study of global protein turnover can help to bridge the gap between transcriptomics and proteomics<sup>55,56</sup>.

Both transcriptomics and proteomics can estimate copy numbers, with proteins typically present at 100-fold or higher copy numbers than their corresponding transcripts, especially in post-mitotic tissues<sup>57</sup>. Although transcripts are often expressed at less than one copy per cell on average, functional proteins tend to have at least 30 copies per cell, even for very-low-abundance complexes in yeast, and more than 100 in mammalian cells<sup>58</sup>. The proteome exhibits a much higher dynamic range—the difference between the lowest and the highest expressed protein—than the transcriptome<sup>59</sup>. Transcriptome-to-proteome divergence reflects the complex regulation of protein abundance through synthesis, degradation and PTMs, highlighting the importance of direct proteomic measurements for understanding cellular function.

## Interaction proteomics

Proteins, as cellular nanomachines, perform specific functions through interactions with other proteins, RNA<sup>52</sup>, DNA<sup>60,61</sup>, metabolites and small-molecule drugs<sup>62</sup>. Mapping these interactions is fundamental to understanding cellular processes in biological or disease contexts. MS-based proteomics has revolutionized our ability to do this comprehensively, benefiting from technological developments in sensitivity, throughput, depth and speed of analyses.

When combined with current MS instrumentation, conventional affinity-purification methods have yielded remarkable insights. A prime example is the recent elucidation of an essentially complete yeast interactome, providing an unprecedented view of the protein interaction landscape in a eukaryotic organism<sup>63</sup>.

Proximity labelling techniques—using biotin or other chemical labelling methods—complement conventional pull-down approaches<sup>64</sup>. These methods can capture dynamic and condition-specific protein– protein interactions, localize interactions to specific domains or identify interactions dependent on PTMs.

Biological and chemical advances have further expanded the capabilities of interaction proteomics. CRISPR–Cas9-mediated systematic knockout studies, such as the investigation of 426 proteins to understand their role in viral replication and protein networks in the HIV lifecycle<sup>65</sup>, have provided insights into complex biological systems. Combining them with high-throughput sample processing has been crucial in deciphering infection mechanisms in recent epidemics and pandemics, including COVID-19 and Zika infections, and in identifying promising vaccination or therapeutic targets<sup>66,67</sup>.

Integrating AI, particularly tools such as AlphaFold-Multimer<sup>68</sup>, with interaction proteomics data is further expanding the boundaries of what we can learn from these experiments. These tools can predict interaction interfaces in multimeric complexes, providing structural context to proteomic data and guiding further experimental design.

## PTMs

PTMs have crucial roles in regulating protein function, localization and interactions, with profound consequences for cellular processes, disease mechanisms and therapeutic interventions. MS-based proteomics has emerged as the premier tool for discovering and quantifying PTMs, with recent technological advances substantially increasing the depth and breadth of PTM analysis<sup>69,70</sup>.

Current PTM analysis workflows have been greatly improved by automating the enrichment step, incorporating ion mobility separation and increasing instrument sensitivity. Robust methods now exist for elucidating patterns of common PTMs, such as phosphorylation<sup>71</sup>, ubiquitination<sup>72</sup> and acetylation<sup>73</sup>. Researchers can now quantify tens of thousands of PTMs localized to specific amino acids, providing insights into cellular signalling networks and their dynamics in response to stimuli or inhibitors<sup>74–76</sup>.

Although most approaches measure relative changes in PTMs, obtaining stoichiometric information about the extent of modifications has become increasingly important<sup>77,78</sup>. This can be achieved by quantifying modified and unmodified peptides, revealing crucial insights into the dynamics of PTM regulation. For instance, studies have uncovered the processive nature of ubiquitination and phosphorylation during key cellular processes such as cell-cycle progression, signal transduction and ageing-associated degeneration<sup>79</sup>. It has also become clear that the average phosphorylation stoichiometry is often relatively high—for instance, in the circadian rhythm<sup>80</sup>—whereas it is generally very low for ubiquitylation<sup>81</sup>.

The field has also made considerable strides in identifying and characterizing the enzymes responsible for writing, reading and erasing PTMs. Thousands of these molecules have been discovered, each with specific roles in modifying protein chemistry and functional activity in health and disease. Understanding the complex interplay between these enzymes and their substrates remains a challenge, but one for which AI methods are poised to contribute innovative solutions. Machine learning has successfully prioritized which of the thousands of phosphorylation sites might be functional<sup>82</sup>, and the structural predictions provided by AlphaFold have been integrated at a large scale<sup>83</sup>. LLMs are already being fine-tuned to predict PTMs<sup>84</sup>.

Advanced technologies will enable the study of complex PTMs such as glycosylation and oxidative modifications. Improved workflows will address challenges in analysing rare PTMs, combinatorial modifications and large-scale profiling for systems-biology purposes<sup>76,85</sup>.

## Structural proteomics

Structural proteomics aims to help elucidate protein structures and dynamics on a large scale, complementing conventional structuralbiology techniques. Several MS-based methods have been developed, each offering unique insights.

Hydrogen–deuterium exchange MS (HDX-MS) is a classical technique that measures mass differences resulting from the isotopic exchange of exposed amide hydrogens when proteins are transiently incubated in a deuterium-enriched solvent<sup>86–89</sup>. Stringent methods and guidelines for these experiments<sup>90</sup> have enabled translational applications, including antibody–antigen interaction studies and investigations of protein drug stability<sup>91</sup>.

Cross-linking mass spectrometry (XL-MS) has seen substantial advances in recent years<sup>92</sup>. XL-MS uses chemical cross-linking reagents to covalently conjugate proximal amino acid residues within the distance defined by the linker and LC–MS to identify residue-to-residue connections. This provides information on domains and distances between sequences<sup>93</sup>. Although interpreting cross-linking data has been challenging, addressing the error of interaction networks<sup>94</sup>, developing enrichable cross-linkers<sup>95,96</sup> and novel software such as xiSearch<sup>97</sup> and Scout<sup>98</sup>, and applying AI tools such as AlphaFold-Multimer and AlphaLink<sup>99</sup> will enable structural insights and the development of protein interaction modulators.

Limited proteolysis provides high-level structural information by exploiting exposed proteolytic cleavage sites in protein complexes. This includes site-specific information by the alteration of the protease cleavage site after structural changes in proteins as well as binding of proteins and small molecules<sup>100</sup>. This approach has been applied to study age-related proteome and structure changes in cerebrospinal fluid, offering insights into conformational changes in proteins that are associated with ageing and disease<sup>101</sup>.

Integrating structural proteomics data with other structural-biology techniques, such as cryo-electron microscopy (cryo-EM), provides insights into protein complexes. For instance, PTM mapping combined with cryo-EM has helped decipher unknown densities in structural models that cannot be attributed to amino acids alone<sup>102</sup>.

![](images/6524c63852b27d71d047d3df7d960d440e41be0cbf647b79ec3dcbc37d23c947.jpg)  
Fig. 2 | Single-cell and spatial proteomics. Advances in single-cell and spatial proteomics techniques. a, Single-cell proteomics methods range from nanolitredroplet workflows, in which single cells are encapsulated for proteomic analysis, to more complex systems that integrate microfluidics for cell lysis and protein digestion. The SCoPE2 technology combines single-cell proteomics with stableisotope-labelled barcodes to enhance sensitivity and throughput, whereas labelfree approaches excel at quantitative accuracy and scalability. b, Tissue spatial proteomics approaches, including DVP and expansion proteomics, can be used to map the proteome in tissue sections, uncovering biological architecture and functional heterogeneity. LCM, laser-capture microdissection.

## Chemoproteomics

Chemoproteomics, the systematic profiling of protein–small molecule interactions on a proteome-wide scale, has become an invaluable tool in drug discovery and target identification<sup>103</sup>. Recent improvements in various approaches have expanded our ability to map the protein–small molecule interaction landscape.

Activity-based protein profiling (ABPP)<sup>104</sup> has become a cornerstone technique in chemoproteomics. It uses chemical probes designed to bind to and enrich specific protein classes or families, thus allowing the study of enzyme activities directly in complex proteomes. ABPP has been widely used to study enzyme families such as kinases, proteases and hydrolases, providing valuable insights into their functions and potential as drug targets.

Thermal protein profiling (TPP) represents another powerful chemoproteomic approach. TPP uses thermal denaturation to identify direct protein targets of small molecules<sup>105</sup>. TPP has proved to be especially valuable in elucidating the mechanisms of action of known drugs and novel compounds, aiding in target deconvolution and in predicting off-target effects.

Advances in degrader screening studies have opened new avenues for therapeutic intervention, particularly for ‘undruggable’ targets. Using MS-based proteomics to target specific substrates and E3 ubiquitin ligases, researchers have identified molecules that selectively ubiquitinate protein substrates for degradation while avoiding off-target activities<sup>106,107</sup>.

The power of chemoproteomics is further enhanced when integrated with other ‘omics’ data, such as genomics and transcriptomics. As the field advances, it promises to expand the druggable proteome and accelerate the discovery of novel therapeutic strategies.

## Single-cell proteomics

The success of single-cell transcriptomics in defining new cell types has generated tremendous interest in single-cell proteomics, which can provide a direct readout of the functional state of individual cells. However, the limited amount of protein in a single cell (typically 50–500 pg) has posed major challenges for MS-based analysis<sup>108</sup>. Note that unlike transcriptomics, proteomics cannot amplify the quantity measured; however, there is typically more than 100-fold more protein than transcript for every expressed gene, and those proteins reflect the cell-to-cell variance much better.

Advances in sample preparation, MS instrumentation and data acquisition have begun to overcome this formidable sensitivity challenge (Fig. 2a). Pioneering approaches involved lysing and proteolytically digesting a small number of cells in nanolitre droplets, followed by direct loading onto the analytical column<sup>109,110</sup>. The introduction of the SCoPE (single-cell proteomics) method, which uses isobaric labelling to combine single cells with a carrier channel, enabled the quantification of about 1,000 proteins across 100 single cells<sup>111</sup>.

Microfluidics technology has shown promise in improving ultrasensitive MS single-cell analysis. When used to isolate and process single cells, it identified 1,500 proteins per circulating tumour cell<sup>112</sup>. The reduction of LC flow rates has resulted in proportional MS signal gain, allowing the quantification of up to 2,000 proteins across the cell cycle without multiplexing in single HeLa cells using the timsTOF SCP instrument<sup>113</sup>.

DIA has become the preferred data-acquisition mode for single-cell proteomics, overcoming the contamination and ratio distortion issues associated with isobaric labelling approaches. Recent developments— such as multiplexed DIA<sup>114,115</sup> and narrow-window DIA (nDIA) on the Astral mass analyser—have pushed the boundaries even further, quantifying more than 5,000 proteins in single oocytes in a ‘One-Tip’ set-up that eliminates sample loss<sup>116,117</sup>. Similarly, the proteoCHIP EVO in a microfluidic instrument allows the automated handling of miniscule sample volumes, minimizing loss<sup>118</sup>.

The fact that there are many more copies of proteins than transcripts in single cells means that they are not subject to Poisson or shot noise. This potentially enables single-cell proteomics to define cell states with much fewer cells than transcriptomics allows. With rapid advances in throughput and the higher copy number of proteins compared to transcripts in a single cell, proteomics could have a key role in the single-cell omics field.

As technology continues to improve, integration with other singlecell modalities, such as transcriptomics and metabolomics, promises to provide a more comprehensive view of cellular states and functions. The ability to perform parallel transcriptome and proteome analysis from the same single cell is now within reach, offering unprecedented insights into cellular biology.

## Spatial proteomics

Although single-cell approaches provide valuable information about cellular heterogeneity, they often lack spatial context within tissues. Spatial proteomics aims to bridge this gap by characterizing proteomes while preserving spatial information, providing crucial insights into tissue organization and cell–cell interactions. Technological advances have considerably expanded our ability to perform spatial proteomic analyses, building on the capacity of proteomics to easily analyse FFPE tissues and fresh frozen ones (Fig. 2b).

![](images/66749f0288dc3ec70c36b6032d03c8056dd5a4d5fbc158f86cf8873e28565484.jpg)  
Fig. 3 | Development of clinical assays from discovery proteomics. Pipeline for developing clinical proteomics assays from discovery through to real-world testing. It begins with biomarker discovery (left) using data-acquisition technologies such as DIA and DDA, followed by AI-driven model building and validation. The middle section shows the steps involved in clinical assay  
development, including targeted MS methods, highlighting the requirements for accuracy, linearity and precision. LDTs, laboratory-developed tests. The right section presents the application of these assays in real-world settings, detailing the inclusion of multi-centre cohort studies and prospective clinical trials, thus showcasing the transition from research to clinical diagnostics.

One pioneering approach is deep visual proteomics (DVP), which combines imaging of tissue slides with AI-driven cell classification and microdissection, followed by deep proteomic analysis of specific cell types and states<sup>119</sup>. The effective throughput of the method is high, and functional differences between cell types and states in the same tissue context are straightforward to interpret. The power of DVP has already been shown in translational research. For example, DVP was recently used to uncover key molecular alterations that drive a lethal drug-induced skin rash called toxic epidermal necrolysis (TEN), with hyperactivation of the JAK–STAT pathway identified as a key driver<sup>120</sup>. This discovery led to the successful repurposing of an approved inhibitor to cure this condition, showcasing the potential of spatial proteomics in personalized medicine.

Other innovative approaches are pushing the boundaries of spatial resolution in proteomic analysis. Tissue expansion technology, when combined with proteomics, has enabled the study of subcellular structures, such as single nuclei from mouse hepatocytes<sup>121</sup>. The use of micro-scaffolds created by customized three-dimensional printing technology has allowed the generation of complete proteome maps of tissue slices with high spatial resolution<sup>122</sup>.

The integration of advanced microscopy technologies, including high-plex imaging, AI-driven image analysis and deep proteomic characterization, is set to provide key insights into the spatial organization of the proteome within tissues. This convergence of technologies promises to revolutionize our understanding of tissue biology, disease processes and drug responses at the cellular and subcellular levels.

## Bringing proteomics to the clinic

Translating proteomics from research laboratories to clinical practice holds immense promise for improving disease diagnosis, prognosis and treatment selection. Body fluids offer a window into the health status of patients through easily accessible samples. Blood plasma, being in contact with all organs, has long been considered a treasure trove of potential biomarkers for various diseases<sup>123,124</sup>. However, its extreme dynamic range—spanning more than ten orders of magnitude, from the most abundant proteins, such as albumin, to the least abundant, such as cytokines—poses a formidable analytical challenge. Technological advances have considerably improved our ability to probe the plasma proteome. Current MS-based proteomics workflows routinely measure 300–500 proteins in a single-injection analysis of neat plasma<sup>125–127</sup>. For instance, a workflow using liquid handlers, Evosep HPLC systems and a timsTOF mass spectrometer enabled the rapid analysis of 1,612 samples, successfully uncovering biomarkers of sepsis<sup>128</sup>. With the Astral mass spectrometer, this number has increased to about 1,000 proteins at a throughput of up to 100 samples per day, enabling successful applications to clinical cohorts. Plasma proteomics has already been shown to perform better than current clinical tests for COVID-19 (ref. 129), early-stage liver disease<sup>125</sup> and metabolic syndrome<sup>126</sup>, confirming its potential to revolutionize diagnostics.

Researchers have used various strategies to increase proteome depth to make full use of the potential of plasma proteomics. New, non-specific enrichment strategies have complemented conventional approaches such as depleting high-abundance proteins. Bead-based workflows exploiting protein coronas on surfaces<sup>130</sup>, when combined with the Astral, can now identify thousands of proteins in plasma<sup>131</sup>. However, careful validation is crucial to ensure the suitability of such methods for quantitative, robust biomarker discovery and routine clinical application. Likewise, isolating exosomes or microvesicles from blood<sup>132</sup>, which has already proven advantageous for profiling nucleic acids and lipids, could provide a window into the proteomes of particular tissue types. Nevertheless, the labour-intensive nature and variability of these and related methods can be barriers to adoption, necessitating robotics-based high-throughput approaches.

Cost remains an important factor for clinical implementation. Whereas some workflows cost hundreds of dollars per sample, recent innovations offer more economical alternatives. For example, a perchloric acid precipitation workflow maintains reproducibility, robustness and increases proteome coverage to 1,600 proteins or more, while minimizing batch effects and substantially reducing costs<sup>133</sup>. This biochemical protocol also enables high-throughput analyses of thousands of samples in weeks, essential for adequately powered clinical plasma studies and the widespread adoption of proteomics in clinical settings.

Unlike MS-based proteomics, affinity-based methods (such as Olink and SomaLogic) have been used for population-scale protein quantitative trait loci (QTL) analysis<sup>134</sup>. Evaluating the specificity of the binders used across various sample matrices is essential, especially because limited correlation among major binder platforms has been observed<sup>135,136</sup>. Orthogonal validation with MS-based methods is crucial to address this limitation<sup>137</sup>.

![](images/3ff13ed1459e872944b610ffe1573654f307997eab16f1fb91348fa5247a8d67.jpg)  
Fig. 4 | AI empowers MS-based proteomics. The use of AI in enhancing MS-based proteomics is multifaceted. AI can help with experimental planning; sample preparation using robotics; data interpretation; data acquisition;  
interpreting complex datasets; predicting PTMs; and integrating proteomics data with other omics data. These applications will ultimately facilitate comprehensive biomedical research and complex data analysis.

Apart from plasma, other body fluids are gaining attention in clinical proteomics. Urine proteomics has shown promise in classifying diseases such as COVID-19 by severity<sup>138</sup> and stratifying patients with Parkinson’s disease by genotype<sup>139</sup>. Its non-invasive nature makes it particularly attractive for paediatric applications, such as diagnosing appendicitis without exposing children to abdominal irradiation from CT scans<sup>140</sup>, or monitoring premature neonates without risking anaemia from blood draws<sup>141</sup>. Cerebrospinal fluid and tear proteomics have provided valuable insights into neurological disorders such as Alzheimer’s disease, offering more proximal and disease-specific alternatives to plasma<sup>142</sup>.

Although some MS studies identify biomarkers that lend themselves to classical ELISA formats, they generally require MS-based protein assays to be brought into the clinic. These panels can contain more than a dozen markers, each with a relatively small fold-change. We expect that MS-based peptide assays with internal standards for absolute quantification will be integral to biomarker discovery and diagnosis in clinical medicine over the next five to ten years.

Proteomics researchers have analysed tissue for decades. For instance, the Clinical Proteomic Tumor Analysis Consortium (CPTAC), launched in 2011, has characterized proteogenomic and PTM changes in more than 1,500 samples and 10 cancer types, revealing new insights, including the identification of proteomic subtypes, prioritization of driver mutations and elucidation of cancer-relevant signalling pathways and PTMs<sup>143,144</sup>. It has also been valuable in pioneering standardization efforts across several clinical centres, and in multi-omics integration.

Tissue biopsies are another cornerstone of clinical diagnostics, with most analyses today focusing on morphological changes, gene mutations or antibody-based protein assessments. Recent advances in MS-based proteomics have enabled proteomics from biopsy-scale tissue samples, expanding diagnostic or prognostic capabilities<sup>125,145,146</sup> when compared with RNA-based tests on biopsy specimens in clinical settings<sup>147</sup>. The main obstacles to the acceptance of MS-based protein diagnostics are not technical, but more related to the clinical community’s lack of awareness of technological advancements in proteomics. Moreover, in vitro diagnostics (IVDs) require stringent quality-control measures<sup>148</sup>, whereas at present, most MS-based experiments are performed in research laboratories, rather than in IVD-certified clinical ones. That said, promising targeted MS-based protein tests are currently being developed<sup>149</sup> (Fig. 3).

Note that most tissue-based proteomics studies only report potentially novel protein biomarkers discovered from a limited number of

This landmark study presents a comprehensive map of the human proteome across 32 tissues and organs, providing millions of IHC-based pictures of health and disease.

retrospective specimens<sup>143,144,150,151</sup>, without further development or validation in the clinical setting. Although some studies have reported in-depth mechanistic investigations of selected proteins and validated protein biomarkers or panels in one or several independent cohorts, few have progressed into clinically applicable tests. This process requires real-world deployment, which is notably absent from the current literature. On the basis of DDA and DIA based on complex and expensive research instruments, discovery proteomics might have difficulty qualifying as a valid and economically accessible clinical test. Instead, some form of targeted proteomics, augmented with appropriate spike-in synthetic standards, could be a more reliable approach acceptable to the clinical and regulatory environments<sup>149</sup>. Sample stability is an important consideration for MS-based protein tests, and an even greater concern for affinity-based protein and RNA-based tests, whereas it is generally less crucial for DNA-based tests.

If a single protein biomarker proves effective for medical indications, a customized immunohistochemistry (IHC)-based test would probably be preferred. However, in most instances, several protein biomarkers need to be combined into a computational model<sup>150</sup>, necessitating precise quantification, which IHC cannot provide. Given that the intensity values of different MS workflows are not directly comparable, such models are likely to be constrained to specific instruments unless spike-in standards are used. Despite the variety of MS instruments available for proteomics research, options suitable for use as medical devices in clinical tests are limited at present, although they do exist for measuring metabolites and drugs<sup>152</sup>.

With many technological barriers now overcome, it has become increasingly clear that the correct design of cohorts and studies is crucial for obtaining generalizable biomarker panels. For instance, MS-based proteomics datasets for biomarkers studies have often been greatly underpowered. Implementing a requirement for raw data to be deposited in archives enables, in principle, meta-analyses to test and better power biomarker discovery<sup>153</sup>. However, better means of linking de-identified clinical data with raw files must be implemented to avoid violating privacy regulations.

## Outlook and the role of AI in proteomics

MS-based proteomics is rapidly evolving, driven by continuous technological advancements and the integration of cutting-edge computational approaches. These innovations will continue to push the boundaries of proteomics. Advances in sample preparation, chromatography, mass analysers and data-acquisition strategies will enable deeper proteome coverage from ever-smaller samples. Increasingly automated and streamlined workflows will democratize proteomics, making it more accessible to a broader research community and fostering interdisciplinary collaborations. The considerable cost of the latest generation of MS instruments is partly offset by their throughput, but this issue must be addressed to foster broader adoption.

AI is poised to have an increasingly central role in proteomics (Fig. 4). Deep-learning algorithms will drive improvements in data acquisition and interpretation, enhancing the depth and quality of proteomics data while enabling real-time decision-making during experiments<sup>11,44</sup>.

Interpreting complex proteomics data remains a challenge, and AI and machine-learning techniques will be pivotal. From peptide and protein identification to structural elucidation, AI will facilitate the extraction of biological insights from vast proteomics datasets. Integrating AI with structural biology and network analysis promises a holistic understanding of protein complexes, interactions and their functional implications.

In clinical applications, in which security and privacy are prime concerns, highly capable ‘open weight’ LLMs that can be run locally are a welcome development. These models—in particular recently introduced ‘reasoning models’—could assist in data interpretation and deal with large data volumes while maintaining the confidentiality required in healthcare settings.

Proteomics, similarly to other omics disciplines, has embarked on a quest for LLMs or ‘foundation models’ trained on vast amounts of data that show ‘emergent properties’ of understanding<sup>154,155</sup>. We foresee models for spectrum-to-amino-acid-sequence translation shortly. More ambitiously, with sufficient proteomics data—in particular, perturbation proteomics data<sup>156</sup>—it might be possible to develop foundation models that embed knowledge about the underlying biology of cells. Although the single-cell transcriptomics community is already exploring this approach<sup>157</sup>, the quantitative and functional nature of proteomics might ultimately make it a more powerful candidate for such models.

Combining proteomics with genomics, transcriptomics and metabolomics promises a comprehensive understanding of biological systems. Multimodal data integration, facilitated by AI and advanced computational methods, will elucidate intricate molecular networks, revealing the interplay between biomolecules and their functional consequences. This holistic approach will provide a new basis for systems biology, and will be instrumental in unravelling the complexities of disease mechanisms and identifying novel therapeutic targets.

As proteomics matures, efforts to democratize access to this powerful technology and establish community-driven standards will be paramount. Open-source software, shared data repositories and collaborative initiatives will foster the dissemination of knowledge and enable researchers worldwide to leverage the full potential of proteomics. Standardizing experimental protocols, data formats and analysis pipelines will facilitate data integration, reproducibility and cross-study comparisons, ultimately accelerating scientific progress.

The future of MS-based proteomics is full of exciting possibilities. We are delighted that this potential is also increasingly recognized outside the field—as exemplified by the planned massive investment in the π-HuB (proteomic navigator of the human body) project in China<sup>158</sup>. By harnessing the synergies of technological innovations, computational advances and interdisciplinary collaborations, proteomics will continue to push the boundaries of our understanding of biological systems. This progress will pave the way for transformative biomedical discoveries and translational applications.

1. Ball, P. How Life Works: A User’s Guide to the New Biology (Univ. Chicago Press, 2024).

Gold, L. et al. Aptamer-based multiplexed proteomic technology for biomarker discovery. PLoS One 5, e15004 (2010).

4. Assarsson, E. et al. Homogenous 96-plex PEA immunoassay exhibiting high sensitivity, specificity, and excellent scalability. PLoS One 9, e95192 (2014).

Aebersold, R. & Mann, M. Mass spectrometry-based proteomics. Nature 422, 198–207 (2003).

Aebersold, R. & Mann, M. Mass-spectrometric exploration of proteome structure and function. Nature 537, 347–355 (2016).

7. Fenn, J. B., Mann, M., Meng, C. K., Wong, S. F. & Whitehouse, C. M. Electrospray ionization for mass spectrometry of large biomolecules. Science 246, 64–71 (1989).

8. Hughes, C. S. et al. Ultrasensitive proteome analysis using paramagnetic bead technology. Mol. Syst. Biol. 10, 757 (2014).

9. Batth, T. S. et al. Protein aggregation capture on microparticles enables multipurpose proteomics sample preparation. Mol. Cell. Proteomics 18, 1027–1035 (2019).

10. Zhu, Y. et al. High-throughput proteomic analysis of FFPE tissue samples facilitates tumor stratification. Mol. Oncol. 13, 2305–2328 (2019).

11. Xiao, Q. et al. High-throughput proteomics and AI for cancer biomarker discovery. Adv. Drug Deliv. Rev. 176, 113844 (2021).

12. Hendy, J. Ancient protein analysis in archaeology. Sci. Adv. 7, eabb9314 (2021).

13. Mylopotamitaki, D. et al. Homo sapiens reached the higher latitudes of Europe by 45,000 years ago. Nature 626, 341–346 (2024).

14. Bian, Y., Gao, C. & Kuster, B. On the potential of micro-flow LC–MS/MS in proteomics. Expert Rev. Proteomics 19, 153–164 (2022).

15. Bache, N. et al. A novel LC system embeds analytes in pre-formed gradients for rapid, ultra-robust proteomics. Mol. Cell. Proteomics 17, 2284–2296 (2018).

16. Muller, J. B. et al. The proteome landscape of the kingdoms of life. Nature 582, 592–596 (2020).

17. Makarov, A. Electrostatic axially harmonic orbital trapping: a high-performance technique of mass analysis. Anal. Chem. 72, 1156–1162 (2000).

This comprehensive study maps dose- and time-resolved changes in the phosphoproteome after drug treatments, providing insights into drug-induced signalling dynamics and revealing principles of cellular adaptation to

This groundbreaking study comprehensively analyses tau post-translational modifications in Alzheimer’s disease, revealing distinct modification profiles that correlate with disease progression and patient heterogeneity, and providing new insights into tau pathology, diagnostics and potential therapeutic targets.

18. Eliuk, S. & Makarov, A. Evolution of Orbitrap mass spectrometry instrumentation. Annu. Rev. Anal. Chem. 8, 61–80 (2015).

19. Meier, F., Park, M. A. & Mann, M. Trapped ion mobility spectrometry and parallel accumulation–serial fragmentation in proteomics. Mol. Cell. Proteomics 20, 100138 (2021).

20. Stewart, H. I. et al. Parallelized acquisition of Orbitrap and Astral analyzers enables high-throughput quantitative analysis. Anal. Chem. 95, 15656–15664 (2023).

21. Guzman, U. H. et al. Ultra-fast label-free quantification and comprehensive proteome coverage with narrow-window data-independent acquisition. Nat. Biotechnol. 42, 1855–1866 (2024).

Together with Stewart et al. (2023), this study introduces the Astral mass analyser for proteomics use—a novel multi-reflecting TOF MS that enables ultra-fast and highly sensitive proteomics, allowing for the quantification of nearly 10,000 proteins in single-shot analyses of human cell lines.

22. Venable, J. D., Dong, M. Q., Wohlschlegel, J., Dillin, A. & Yates, J. R. Automated approach for quantitative analysis of complex peptide mixtures from tandem mass spectra. Nat. Methods 1, 39–45 (2004).

23. Gillet, L. C. et al. Targeted data extraction of the MS/MS spectra generated by dataindependent acquisition: a new concept for consistent and accurate proteome analysis. Mol. Cell. Proteomics 11, O111.016717 (2012).

24. Meier, F. et al. diaPASEF: parallel accumulation-serial fragmentation combined with dataindependent acquisition. Nat. Methods 17, 1229–1236 (2020).

25. Rost, H. L. et al. OpenSWATH enables automated, targeted analysis of data-independent acquisition MS data. Nat. Biotechnol. 32, 219–223 (2014).

26. Bruderer, R. et al. Optimization of experimental parameters in data-independent mass spectrometry significantly increases depth and reproducibility of results. Mol. Cell. Proteomics 16, 2296–2309 (2017).

27. Demichev, V., Messner, C. B., Vernardis, S. I., Lilley, K. S. & Ralser, M. DIA-NN: neural networks and interference correction enable deep proteome coverage in high throughput. Nat. Methods 17, 41–44 (2020).

This landmark paper introducing DIA-NN, a deep-neural-network-based software for analysing DIA proteomics data, greatly improved peptide identification and quantification for more comprehensive and precise proteome profiling.

28. Zhang, F., Ge, W., Ruan, G., Cai, X. & Guo, T. Data-independent acquisition mass spectrometry-based proteomics and software tools: a glimpse in 2020. Proteomics 20, e1900276 (2020).

29. The, M., Samaras, P., Kuster, B. & Wilhelm, M. Reanalysis of ProteomicsDB using an accurate, sensitive, and scalable false discovery rate estimation approach for protein groups. Mol. Cell. Proteomics 21, 100437 (2022).

30. Strauss, M. T. et al. AlphaPept: a modern and open framework for MS-based proteomics. Nat. Commun. 15, 2168 (2024).

31. Wang, Z. et al. High-throughput proteomics of nanogram-scale samples with Zeno SWATH MS. eLife 11, e83947 (2022).

32. Skowronek, P. et al. Synchro-PASEF allows precursor-specific fragment ion extraction and interference removal in data-independent acquisition. Mol. Cell. Proteomics 22, 100489 (2023).

33. Baker, M. S. et al. Accelerating the search for the missing proteins in the human proteome. Nat. Commun. 8, 14271 (2017).

34. Perdigao, N. et al. Unexpected features of the dark proteome. Proc. Natl Acad. Sci. USA 112, 15898–15903 (2015).

35. Kustatscher, G. et al. Understudied proteins: opportunities and challenges for functional proteomics. Nat. Methods 19, 774–779 (2022).

36. Hellinger, R. et al. Peptidomics. Nat. Rev. Methods Primers 3, 25 (2023).

37. Li, J. et al. TMTpro-18plex: the expanded and complete set of TMTpro reagents for sample multiplexing. J. Proteome Res. 20, 2964–2972 (2021).

38. Ting, L., Rad, R., Gygi, S. P. & Haas, W. MS3 eliminates ratio distortion in isobaric multiplexed quantitative proteomics. Nat. Methods 8, 937–940 (2011).

39. Hogrebe, A. et al. Benchmarking common quantification strategies for large-scale phosphoproteomics. Nat. Commun. 9, 1045 (2018).

40. Cheung, T. K. et al. Defining the carrier proteome limit for single-cell proteomics. Nat. Methods 18, 76–83 (2021).

41. Picotti, P., Bodenmiller, B., Mueller, L. N., Domon, B. & Aebersold, R. Full dynamic range proteome analysis of S. cerevisiae by targeted proteomics. Cell 138, 795–806 (2009).

42. Picotti, P. & Aebersold, R. Selected reaction monitoring-based proteomics: workflows, potential, pitfalls and future directions. Nat. Methods 9, 555–566 (2012).

43. Wichmann, C. et al. MaxQuant.Live enables global targeting of more than 25,000 peptides. Mol. Cell. Proteomics 18, 982–994 (2019).

44. Mann, M., Kumar, C., Zeng, W. F. & Strauss, M. T. Artificial intelligence for proteomics and biomarker discovery. Cell Syst. 12, 759–770 (2021).

45. Gyori, B. M. & Vitek, O. Beyond protein lists: AI-assisted interpretation of proteomic investigations in the context of evolving scientific knowledge. Nat. Methods 21, 1387–1389 (2024).

46. Santos, A. et al. A knowledge graph to interpret clinical proteomics data. Nat. Biotechnol. 40, 692–702 (2022).

47. Bekker-Jensen, D. B. et al. An optimized shotgun strategy for the rapid generation of comprehensive human proteomes. Cell Syst. 4, 587–599 (2017).

48. Sinitcyn, P. et al. Global detection of human variants and isoforms by deep proteome sequencing. Nat. Biotechnol. 41, 1776–1786 (2023).

49. Lundberg, E. et al. Defining the transcriptome and proteome in three functionally different human cell lines. Mol. Syst. Biol. 6, 450 (2010).

50. Adhikari, S. et al. A high-stringency blueprint of the human proteome. Nat. Commun. 11, 5301 (2020).

51. Chen, J. et al. Pervasive functional translation of noncanonical human open reading frames. Science 367, 1140–1146 (2020).

52. Buccitelli, C. & Selbach, M. mRNAs, proteins and the emerging principles of gene expression control. Nat. Rev. Genet. 21, 630–644 (2020).

53. Liu, Y., Beyer, A. & Aebersold, R. On the dependency of cellular protein levels on mRNA abundance. Cell 165, 535–550 (2016).

54. Knecht, S. et al. An introduction to analytical challenges, approaches, and applications in mass spectrometry-based secretomics. Mol. Cell. Proteomics 22, 100636 (2023).

55. van Mierlo, G. & Vermeulen, M. Chromatin proteomics to study epigenetics—challenges and opportunities. Mol. Cell. Proteomics 20, 100056 (2021).

56. Ross, A. B., Langer, J. D. & Jovanovic, M. Proteome turnover in the spotlight: approaches, applications, and perspectives. Mol. Cell. Proteomics 20, 100016 (2021).

57. Azimifar, S. B., Nagaraj, N., Cox, J. & Mann, M. Cell-type-resolved quantitative proteomics of murine liver. Cell Metab. 20, 1076–1087 (2014).

58. Kulak, N. A., Pichler, G., Paron, I., Nagaraj, N. & Mann, M. Minimal, encapsulated proteomicsample processing applied to copy-number estimation in eukaryotic cells. Nat. Methods 11, 319–324 (2014).

59. MacCoss, M. J. et al. Sampling the proteome by emerging single-molecule and mass spectrometry methods. Nat. Methods 20, 339–346 (2023).

60. Qin, W., Cho, K. F., Cavanagh, P. E. & Ting, A. Y. Deciphering molecular interactions by proximity labeling. Nat. Methods 18, 133–143 (2021).

61. Ma, T., Ye, Z. & Wang, L. Genome wide approaches to identify protein–DNA interactions. Curr. Med. Chem. 26, 7641–7654 (2019).

62. Lucero, B., Francisco, K. R., Liu, L. J., Caffrey, C. R. & Ballatore, C. Protein–protein interactions: developing small-molecule inhibitors/stabilizers through covalent strategies. Trends Pharmacol. Sci. 44, 474–488 (2023).

63. Michaelis, A. C. et al. The social and structural architecture of the yeast protein interactome. Nature 624, 192–200 (2023). This comprehensive study maps the near-complete protein–protein interaction network in yeast, providing insights into the social and structural architecture of an entire proteome and revealing fundamental principles of protein complex organization.

64. Branon, T. C. et al. Efficient proximity labeling in living cells and organisms with TurboID. Nat. Biotechnol. 36, 880–887 (2018).

65. Hiatt, J. et al. A functional map of HIV–host interactions in primary human T cells. Nat. Commun. 13, 1752 (2022).

66. Thorne, L. G. et al. Evolution of enhanced innate immune evasion by SARS-CoV-2. Nature 602, 487–495 (2022).

67. Shah, P. S. et al. Comparative flavivirus–host protein interaction mapping reveals mechanisms of dengue and Zika virus pathogenesis. Cell 175, 1931–1945 (2018).

68. Evans, R. et al. Protein complex prediction with AlphaFold-Multimer. Preprint at bioRxiv https://doi.org/10.1101/2021.10.04.463034 (2022).

69. Riley, N. M. & Coon, J. J. Phosphoproteomics in the age of rapid and deep proteome profiling. Anal. Chem. 88, 74–94 (2016).

70. Skowronek, P. et al. Rapid and in-depth coverage of the (phospho-)proteome with deep libraries and optimal window design for dia-PASEF. Mol. Cell. Proteomics 21, 100279 (2022).

71. Chang, A., Leutert, M., Rodriguez-Mias, R. A. & Villen, J. Automated enrichment of phosphotyrosine peptides for high-throughput proteomics. J. Proteome Res. 22, 1868–1880 (2023).

72. Poirson, J. et al. Proteome-scale discovery of protein degradation and stabilization effectors. Nature 628, 878–886 (2024).

73. Lund, P. J. et al. Isotopic labeling and quantitative proteomics of acetylation on histones and beyond. Methods Mol. Biol. 1977, 43–70 (2019).

74. Clague, M. J., Urbe, S. & Komander, D. Breaking the chains: deubiquitylating enzyme specificity begets function. Nat. Rev. Mol. Cell Biol. 20, 338–352 (2019).

75. Needham, E. J., Parker, B. L., Burykin, T., James, D. E. & Humphrey, S. J. Illuminating the dark phosphoproteome. Sci. Signal. 12, eaau8645 (2019).

76. Zecha, J. et al. Decrypting drug actions and protein modifications by dose- and timeresolved proteomics. Science 380, 93–101 (2023).

77. Singh, S. A. et al. FLEXIQinase, a mass spectrometry-based assay, to unveil multikinase mechanisms. Nat. Methods 9, 504–508 (2012).

78. Mair, W. et al. FLEXITau: quantifying post-translational modifications of tau protein in vitro and in human disease. Anal. Chem. 88, 3704–3714 (2016).

79. Wesseling, H. et al. Tau PTM profiles identify patient heterogeneity and stages of Alzheimer’s disease. Cell 183, 1699–1713 (2020).

80. Robles, M. S., Humphrey, S. J. & Mann, M. Phosphorylation Is a central mechanism for circadian control of metabolism and physiology. Cell Metab. 25, 118–127 (2017).

81. Prus, G., Satpathy, S., Weinert, B. T., Narita, T. & Choudhary, C. Global, site-resolved analysis of ubiquitylation occupancy and turnover rate reveals systems properties. Cell 187, 2875–2892 (2024).

A comprehensive global analysis of human ubiquitylation stoichiometry and turnover rates, revealing unexpectedly low occupancy levels and providing insights into the dynamics and regulation of this crucial PTM.

82. Ochoa, D. et al. The functional landscape of the human phosphoproteome. Nat. Biotechnol. 38, 365–373 (2020).

83. Bludau, I. et al. The structural context of posttranslational modifications at a proteome-wide scale. PLoS Biol. 20, e3001636 (2022).

84. Shrestha, P., Kandel, J., Tayara, H. & Chong, K. T. Post-translational modification prediction via prompt-based fine-tuning of a GPT-2 model. Nat. Commun. 15, 6699 (2024).

85. Vieitez, C. et al. High-throughput functional characterization of protein phosphorylation sites in yeast. Nat. Biotechnol. 40, 382–390 (2022).

86. Ma, R., Meng, H., Wiebelhaus, N. & Fitzgerald, M. C. Chemo-selection strategy for limited proteolysis experiments on the proteomic scale. Anal. Chem. 90, 14039–14047 (2018).

87. Pepelnjak, M., de Souza, N. & Picotti, P. Detecting protein–small molecule interactions using limited proteolysis–mass spectrometry (LiP–MS). Trends Biochem. Sci. 45, 919–920 (2020).

88. Piersimoni, L., Kastritis, P. L., Arlt, C. & Sinz, A. Cross-linking mass spectrometry for investigating protein conformations and protein–protein interactions—a method for all seasons. Chem. Rev. 122, 7500–7531 (2022).

89. Zheng, J., Strutzenberg, T., Pascal, B. D. & Griffin, P. R. Protein dynamics and conformational changes explored by hydrogen/deuterium exchange mass spectrometry. Curr. Opin. Struct. Biol. 58, 305–313 (2019).

90. Masson, G. R. et al. Recommendations for performing, interpreting and reporting hydrogen deuterium exchange mass spectrometry (HDX-MS) experiments. Nat. Methods 16, 595–602 (2019).

91. Marciano, D. P., Dharmarajan, V. & Griffin, P. R. HDX-MS guided drug discovery: small molecules and biopharmaceuticals. Curr. Opin. Struct. Biol. 28, 105–111 (2014).

92. Yu, C. & Huang, L. New advances in cross-linking mass spectrometry toward structural systems biology. Curr. Opin. Chem. Biol. 76, 102357 (2023).

93. Chen, Z. A. & Rappsilber, J. Protein structure dynamics by crosslinking mass spectrometry. Curr. Opin. Struct. Biol. 80, 102599 (2023).

94. Lenz, S. et al. Reliable identification of protein–protein interactions by crosslinking mass spectrometry. Nat. Commun. 12, 3564 (2021). This paper introduces an integrated workflow for cross-linking MS, combining optimized sample preparation, chromatography and data analysis to enhance the depth and reliability of protein interaction mapping, advancing our understanding of protein complex structures and cellular organization.

95. Wheat, A. et al. Protein interaction landscapes revealed by advanced in vivo crosslinking–mass spectrometry. Proc. Natl Acad. Sci. USA 118, e2023360118 (2021).

96. Jiang, P. L. et al. A membrane-permeable and immobilized metal affinity chromatography (IMAC) enrichable cross-linking reagent to advance in vivo cross-linking mass spectrometry. Angew. Chem. Int. Ed. 61, e202113937 (2022).

97. Mendes, M. L. et al. An integrated workflow for crosslinking mass spectrometry. Mol. Syst. Biol. 15, e8994 (2019).

98. Clasen, M. A. et al. Proteome-scale recombinant standards and a robust high-speed search engine to advance cross-linking MS-based interactomics. Nat. Methods 21, 2327–2335 (2024).

99. Stahl, K., Graziadei, A., Dau, T., Brock, O. & Rappsilber, J. Protein structure prediction with in-cell photo-crosslinking mass spectrometry and deep learning. Nat. Biotechnol. 41, 1810–1819 (2023).

100. Piazza, I. et al. A map of protein–metabolite interactions reveals principles of chemical communication. Cell 172, 358–372 (2018). This groundbreaking study presents a comprehensive map of protein–metabolite interactions in yeast, revealing widespread and functionally important associations between proteins and small molecules and providing insights into metabolitemediated cellular regulation and communication principles.

101. Shuken, S. R. et al. Limited proteolysis–mass spectrometry reveals aging-associated changes in cerebrospinal fluid protein abundances and structures. Nat. Aging 2, 379–388 (2022).

102. Arakhamia, T. et al. Posttranslational modifications mediate the structural diversity of tauopathy strains. Cell 184, 6207–6210 (2021). This first study to combine cryo-EM with MS-based proteomics studies tau filaments from the brains of individuals with Alzheimer’s disease to shed light on the molecular basis of tau pathology associated with PTMs and the structural diversity of tauopathy strains.

103. Meissner, F., Geddes-McAlister, J., Mann, M. & Bantscheff, M. The emerging role of mass spectrometry-based proteomics in drug discovery. Nat. Rev. Drug Discov. 21, 637–654 (2022).

104. Speers, A. E., Adam, G. C. & Cravatt, B. F. Activity-based protein profiling in vivo using a copper(I)-catalyzed azide-alkyne [3+2] cycloaddition. J. Am. Chem. Soc. 125, 4686–4687 (2003).

105. Le Sueur, C., Hammaren, H. M., Sridharan, S. & Savitski, M. M. Thermal proteome profiling: insights into protein modifications, associations, and functions. Curr. Opin. Chem. Biol. 71, 102225 (2022).

106. Ng, C. S. C. & Banik, S. M. Recent advances in induced proximity modalities. Curr. Opin. Chem. Biol. 67, 102107 (2022).

107. Moffat, J. G., Vincent, F., Lee, J. A., Eder, J. & Prunotto, M. Opportunities and challenges in phenotypic drug discovery: an industry perspective. Nat. Rev. Drug Discov. 16, 531–543 (2017).

108. Rosenberger, F. A., Thielert, M. & Mann, M. Making single-cell proteomics biologically relevant. Nat. Methods 20, 320–323 (2023).

109. Li, Z. Y. et al. Nanoliter-scale oil-air-droplet chip-based single cell proteomic analysis. Anal. Chem. 90, 5430–5438 (2018).

110. Zhu, Y. et al. Nanodroplet processing platform for deep and quantitative proteome profiling of 10–100 mammalian cells. Nat. Commun. 9, 882 (2018).

111. Budnik, B., Levy, E., Harmange, G. & Slavov, N. SCoPE-MS: mass spectrometry of single mammalian cells quantifies proteome heterogeneity during cell differentiation. Genome Biol. 19, 161 (2018).

112. Gebreyesus, S. T. et al. Streamlined single-cell proteomics by an integrated microfluidic chip and data-independent acquisition mass spectrometry. Nat. Commun. 13, 37 (2022).

113. Brunner, A. D. et al. Ultra-high sensitivity mass spectrometry quantifies single-cell proteome changes upon perturbation. Mol. Syst. Biol. 18, e10798 (2022).

114. Derks, J. et al. Increasing the throughput of sensitive proteomics by plexDIA. Nat. Biotechnol. 41, 50–59 (2023).

115. Thielert, M., Weiss, C. A. M., Mann, M. & Rosenberger, F. A. Spatial proteomics of single hepatocytes with multiplexed data-independent acquisition (mDIA). Methods Mol. Biol. 2817, 97–113 (2024).

116. Ye, Z. et al. Enhanced sensitivity and scalability with a Chip-Tip workflow enables deep single-cell proteomics. Nat. Methods https://doi.org/10.1038/s41592-024-02558-2 (2025).

117. Ye, Z. et al. One-Tip enables comprehensive proteome coverage in minimal cells and single zygotes. Nat. Commun. 15, 2474 (2024).

118. Ctortecka, C. et al. Automated single-cell proteomics providing sufficient proteome depth to study complex biology beyond cell type classifications. Nat. Commun. 15, 5707 (2024).

119. Mund, A. et al. Deep visual proteomics defines single-cell identity and heterogeneity. Nat. Biotechnol. 40, 1231–1240 (2022). This study introduces DVP, which combines AI-driven image analysis with highresolution mass spectrometry to map protein expression patterns in specific cell types within complex tissues, enabling exceptional spatial resolution for functional studies in proteomics.

120. Nordmann, T. M. et al. Spatial proteomics identifies JAKi as treatment for a lethal skin disease. Nature 635, 1001–1009 (2024).

This pioneering single-cell-type spatial proteomics study goes all the way from discovering the cause of a lethal disease to finding a cure for it, marking the dawn of spatial medicine.

121. Dong, Z. et al. Spatial proteomics of single cells and organelles on tissue slides using filter-aided expansion proteomics. Nat. Commun. 15, 9378 (2024).

122. Ma, M. et al. In-depth mapping of protein localizations in whole tissue by micro-scaffold assisted spatial proteomics (MASP). Nat. Commun. 13, 7736 (2022).

123. Surinova, S. et al. On the development of plasma protein biomarkers. J. Proteome Res. 10, 5–16 (2011).

124. Geyer, P. E., Holdt, L. M., Teupser, D. & Mann, M. Revisiting biomarker discovery by plasma proteomics. Mol. Syst. Biol. 13, 942 (2017).

125. Niu, L. et al. Noninvasive proteomic biomarkers for alcohol-related liver disease. Nat. Med. 28, 1277–1287 (2022).

A high-throughput plasma proteomics approach that identifies novel protein biomarkers for non-invasive diagnosis and staging of alcohol-related liver disease, outperforming existing clinical tests and demonstrating the potential of MS-based proteomics for diagnostic tools.

126. Cai, X. et al. Population serum proteomics uncovers a prognostic protein classifier for metabolic syndrome. Cell Rep. Med. 4, 101172 (2023).

127. Messner, C. B. et al. Ultra-high-throughput clinical proteomics reveals classifiers of COVID-19 infection. Cell Syst. 11, 11–24 (2020).

128. Mi, Y. et al. High-throughput mass spectrometry maps the sepsis plasma proteome and differences in patient response. Sci. Transl. Med. 16, eadh0185 (2024).

129. Shen, B. et al. Proteomic and metabolomic characterization of COVID-19 patient sera. Cell 182, 59–72 (2020).

130. Blume, J. E. et al. Rapid, deep and precise profiling of the plasma proteome with multinanoparticle protein corona. Nat. Commun. 11, 3662 (2020).

131. Heil, L. R. et al. Evaluating the performance of the Astral mass analyzer for quantitative proteomics using data-independent acquisition. J. Proteome Res. 22, 3290–3300 (2023).

132. Simpson, R. J., Lim, J. W., Moritz, R. L. & Mathivanan, S. Exosomes: proteomic insights and diagnostic potential. Expert Rev. Proteomics 6, 267–283 (2009).

133. Viode, A. et al. A simple, time- and cost-effective, high-throughput depletion strategy for deep plasma proteomics. Sci. Adv. 9, eadf9717 (2023). This study introduces a simple, time- and cost-effective high-throughput depletion strategy for deep plasma proteomics that enables the analysis of thousands of plasma proteins at an impressive coverage.

134. Sun, B. B., Suhre, K. & Gibson, B. W. Promises and challenges of populational proteomics in health and disease. Mol. Cell. Proteomics 23, 100786 (2024).

135. Bader, J. M., Albrecht, V. & Mann, M. MS-based proteomics of body fluids: the end of the beginning. Mol. Cell. Proteomics 22, 100577 (2023).

136. Katz, D. H. et al. Proteomic profiling platforms head to head: leveraging genetics and clinical traits to compare aptamer- and antibody-based methods. Sci. Adv. 8, eabm5164 (2022).

137. Geyer, P. E. et al. The circulating proteome—technological developments, current challenges, and future trends. J. Proteome Res. 23, 5279–5295 (2024).

138. Bi, X. et al. Proteomic and metabolomic profiling of urine uncovers immune responses in patients with COVID-19. Cell Rep. 38, 110271 (2022).

139. Virreira Winter, S. et al. Urinary proteome profiling for stratifying patients with familial Parkinson’s disease. EMBO Mol. Med. 13, e13257 (2021).

140. Kentsis, A. et al. Detection and diagnostic value of urine leucine-rich α-2-glycoprotein in children with suspected acute appendicitis. Ann. Emerg. Med. 60, 78–83 (2012).

141. Ahmed, S. et al. Urine proteomics for noninvasive monitoring of biomarkers in bronchopulmonary dysplasia. Neonatology 119, 193–203 (2022).

142. Tao, Q. Q. et al. Alzheimer’s disease early diagnostic and staging biomarkers revealed by large-scale cerebrospinal fluid and serum proteomic profiling. Innovation 5, 100544 (2024).

143. Mani, D. R. et al. Cancer proteogenomics: current impact and future prospects. Nat. Rev. Cancer 22, 298–313 (2022).

144. Li, Y. et al. Proteogenomic data and resources for pan-cancer analysis. Cancer Cell 41, 1397–1406 (2023).

145. Guo, T. et al. Rapid mass spectrometric conversion of tissue biopsy samples into permanent quantitative digital proteome maps. Nat. Med. 21, 407–413 (2015).

146. Cai, X. et al. High-throughput proteomic sample preparation using pressure cycling technology. Nat. Protoc. 17, 2307–2325 (2022).

147. Collins, F. S. & Varmus, H. A new initiative on precision medicine. N. Engl. J. Med. 372, 793–795 (2015).

148. Kosack, C. S., Page, A. L. & Klatser, P. R. A guide to aid the selection of diagnostic tests. Bull. World Health Organ. 95, 639–645 (2017).

149. Han, C. L. et al. Lessons learned: establishing a CLIA-equivalent laboratory for targeted mass spectrometry assays - navigating the transition from research to clinical practice. Clin. Proteomics 21, 12 (2024).

150. Sun, Y. et al. Artificial intelligence defines protein-based classification of thyroid nodules. Cell Discov. 8, 85 (2022). This multi-centre study uses AI and proteomics to develop a highly accurate proteinbased classification system for thyroid nodules, showing that AI can be integrated with molecular profiling for improved cancer diagnostics and personalized medicine.

151. Jiang, Y. et al. Proteomics identifies new therapeutic targets of early-stage hepatocellul carcinoma. Nature 567, 257–261 (2019). This large-scale proteogenomic study of early-stage hepatocellular carcinoma identifies new molecular subtypes and potential therapeutic targets, and proposed proteomics-driven precision medicine.

152. Clarke, W. & Nair, H. Mass Spectrometry for the Clinical Laboratory (Academic Press, 2017).

153. van Zalm, P. W. et al. Meta-analysis of published cerebrospinal fluid proteomics data identifies and validates metabolic enzyme panel as Alzheimer’s disease biomarkers. Cell Rep. Med. 4, 101005 (2023).

154. Theodoris, C. V. et al. Transfer learning enables predictions in network biology. Nature 618, 616–624 (2023).

155. Moor, M. et al. Foundation models for generalist medical artificial intelligence. Nature 616, 259–265 (2023).

156. Qian, L. et al. AI-empowered perturbation proteomics for complex biological systems. Cell Genom. 4, 100691 (2024).

157. Schaar, A. C. et al. Nicheformer: a foundation model for single-cell and spatial omics. Preprint at bioRxiv https://doi.org/10.1101/2024.04.15.589472 (2024).

158. He, F. et al. π-Hub: the proteomic navigator of the human body. Nature 636, 322–331 (2024).

Acknowledgements We acknowledge the following for financial support: the National Natural Science Foundation of China (Major Research Plan, grant 92259201), the National Key R&D Program of China (grant 2021YFA1301600) and the Westlake Education Foundation (to T.G.);

the Max Planck Society for the Advancement of Science (to M.M.); and the National Institutes of Health National Institute on Aging (R01 AG071858), the Rainwater Foundation and the Ellison Foundation (to J.A.S.). T.G. thanks the Guomics team for input and for assistance with preparing the figures; M.M. thanks his groups in Munich and Copenhagen for discussions that improved the manuscript; and J.A.S. thanks H. Steen, T. Wang and S. Greally for comments and suggestions and C. Uncu and M. Jha for their support.

Author contributions All authors conceptualized, wrote and edited all versions of this manuscript.

Competing interests M.M. is an indirect investor in Evosep Biosystems and OmicVision Biosciences. T.G. is a shareholder of Westlake Omics.

## Additional information

Correspondence and requests for materials should be addressed to Tiannan Guo, Judith A. Steen or Matthias Mann.

Peer review information Nature thanks Joshua Elias and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

Reprints and permissions information is available at http://www.nature.com/reprints. Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

© Springer Nature Limited 2025