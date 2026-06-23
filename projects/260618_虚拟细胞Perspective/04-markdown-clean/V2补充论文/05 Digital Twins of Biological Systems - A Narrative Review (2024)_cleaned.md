# Digital Twins of Biological Systems: A Narrative Review

Abstract—The concept of Digital Twins (DTs), software models that mimic the behavior and interactions of physical or conceptual objects within their environments, has gained traction in recent years, particularly in medicine and healthcare research. DTs technology emerges as a pivotal tool in disease modeling, integrating diverse data sources to computationally model dynamic biological systems. This narrative review explores potential DT applications in medicine, from defining DTs and their history to constructing DTs, modeling biologically relevant systems, as well as discussing the benefits, risks, and challenges in their application. The influence of DTs extends beyond healthcare and can revolutionize healthcare management, drug development, clinical trials, and various biomedical research fields

Index Terms—Biological system modeling, digital twin, medical technology.

Impact Statement—Highlighting recent literature on Digital Twin technology, this minireview offers a comprehensive guide to biological system integration and actionable solutions, surpassing conventional healthcare-focused analyses with enhanced clarity and illustrative aids.

## I. INTRODUCTION

OMPUTATIONAL simulations are a powerful tool that provides a virtual environment where complex disease   
processes can be studied in a controlled and cost-effective man  
ner [1], [2], [3], [4]. The concept of digital twins (DTs) has

gained significant attention in the field of disease and biological systems modeling. A DT is a dynamic, continuously updating simulation that integrates real-time data from a physical entity into a virtual representation in cyberspace. This virtual representation analyzes the data and provides insights and recommendations that can inform decisions regarding the physical entity [5]. In the context of disease modeling, a DT can be created for an individual [6], [7], a population [8], [9], [10], or even a specific organ or system within the body [11], [12]. The primary advantage of DTs over traditional disease modeling approaches lies in their ability to incorporate real-time data from various sources, such as electronic health records, wearable devices, and environmental sensors [5]. This integration allows for a more accurate and personalized representation of the disease process, taking into account individual variations and external factors that influence disease progression. By continuously updating the simulation with new data, DTs can adapt and refine their predictions, enabling real-time monitoring and proactive decisionmaking [13]. DTs offer numerous benefits in disease modeling, including personalized medicine [14], predictive power [15], [16], [17], real-time monitoring [[4]], [18], population health management [19], [20], [21], and cost-effectiveness [22], [23], ultimately revolutionizing healthcare by improving patient outcomes and informing public health decisions. Additionally, DTs in healthcare have the potential to enable risk-free simulation of treatment strategies, enhance team collaboration with accessible patient data, and improve decision-making through real-time analytics. They allow continuous remote monitoring and timely intervention, and enhance documentation and communication with real-time reporting, ensuring transparency and patient empowerment [24]. Fig. 1 presents the results of a Scopus query that tracks the annual number of manuscripts featuring "Digital Twin" in their title, abstract, or keywords. The plot illustrates a significant surge in interest in this topic in recent years. Perhaps the significance of DTs is best illustrated through one of their precursors, as told in the story of The Ill-Fated Space Odyssey of Apollo 13. When an oxygen tank exploded two days after the launch of the Apollo 13 mission, NASA’s (United States National Aeronautics and Space Administration) engineers had to build a mirror system to simulate possible solutions and guide the astronauts to build an impromptu air purifier that allowed them to safely get back to Earth [25]. While this mirrored system does not fit the current definition of a DT, it illustrates the undeniable potential of virtual models in solving reallife problems and overcoming the need for resource-intensive research. Encouraged by the success of DTs in aviation and

Digital Object Identifier 10.1109/OJEMB.2024.3426916 manufacturing, DTs are now being explored in biomedicine to streamline testing processes, improve diagnosis and prognosis accuracy, and personalize treatment approaches, with implications extending beyond healthcare management to drug development, clinical trials, and broader biomedical research domains [25], [26].

This review explores the potential applications of DTs in biomedicine, structured as follows: Section II discusses definitions, history, and construction methods; Section III covers the benefits, risks, and challenges of DTs; Section IV reviews modeling applications and literature; and Section V provides general oversights and future perspectives.

## II. DEFINITION, HISTORY, AND CONSTRUCTION OF DTS

DT is a computational model representing the structure, behavior, and context of a unique physical asset, allowing for thorough study, analysis, and behavior prediction. Initially introduced by Dr. Michael Grieves under different names such as ‘Mirror Space Model’ and ‘Information Mirror Model’ in 2002, DTs gained practical significance when NASA adopted them for spacecraft simulations [28], [26]. The rapid advancements in computing power, data storage, and sensor technologies, alongside the increasing market demand for tools that enhance asset efficiency and reliability, have propelled DT applications in various fields. In 2014, Michael Grieves formalized the DT concept, identifying three major elements, as shown in Fig. 2: the real space (physical object), the virtual space (digital representation), and the digital thread (bidirectional data flow between real and virtual spaces). DTs have evolved into intelligent, dynamic systems incorporating smart sensors, Internet of Things (IoT), data analytics, and AI to optimize performance and predict future events [25], [26], [29].

The construction of a DT involves several stages to ensure a robust and functional model, as shown in Fig. 3. The following is a summary of the steps to build a DT as described in the literature [30], [31], [24], [31], [32], [33], [34], [35], [36].

A. The planning stage defines the application, identifies required data types, determines expected output data, and envisions a conceptual map integrating input data from multiple sources. This map includes five dimensions:

1) The real entity, be it a physical product, system, or concept, built from multi-level, multi-scale data – crucial for real-time data collection and feedback from and to the real space.

2) A virtual model that contains the physical, chemical, biological, and behavioral characteristics of the real entity. These aspects are typically fully captured by creating a multi-dimensional image through virtual, augmented, or mixed-reality technology.

3) The digital thread for real-time data transmission via advanced network technology depending on the type of interface between the physical and virtual twins.

4) A comprehensive data dimension for storage and analysis, usually in the form of Big Data. Information on the three elements of the DT model to allow for the efficient integration of multi-level data and the extraction of valuable insights.

5) A service and maintenance dimension, for both the real and virtual entities, to sustain DT performance and fidelity.

B. During the development stage, algorithms are constructed and parameterized according to input data, with validation and uncertainty quantification being essential.

C. In the personalization stage, the model is calibrated and contextualized based on the real entity and its environment, and the input data and expected output are matched. This ensures a continuous feedback loop for performance adjustment.

D. The testing and validation stage involves extensive testing under various conditions, with ongoing uncertainty quantification.

E. The final stage is an ongoing learning process that sets DTs apart from other computational models. New data is continuously integrated to improve performance and adaptability [30], [31], [32].

DTs are distinguished from simulation-only models because they provide a continuous, bidirectional exchange of data between the physical and virtual twins. This closed-loop optimization allows for not only ‘what-if’ simulations, but also for active monitoring, analysis, defect prediction, and forecasting. The data stream within the DT system is dynamic, high-dimensional, decentralized, exponentially growing, and context-aware, offering significant advantages over traditional, static, and fragmented data collection and processing methods. Advanced technologies such as IoT, Cloud Computing, AI, VR, and supercomputing tools further grant DT models an elevated level of sophistication and intelligence, as illustrated in Fig. 4 [37].

First, the IoT enables massive data exchange in cyber-physical systems and is further enhanced by developments in sensor technologies and wireless communication. IoT devices can be embedded in real space to collect, send, and receive data about the physical twin and its surrounding environment, resulting in a smart, well-informed DT that evolves with time [26]. Second, Cloud Storage and Computing provide the intense computational power necessary for DT modeling. A secure cloud server should be assigned to every DT model for the safekeeping and integration of data from different sources and the continuous exchange of information. Cloud Computing and Edge Computing are both promising tools for addressing issues of computing efficiency and providing scalable and flexible computing resources [38]. In addition, a DT model would require 5G communication technology for high-speed mass data transmission. Third, AI emulates human reasoning and provides the DT model with Big Data processing, Machine Learning (ML), image processing, and pattern recognition capabilities. Big Data analytics combined with ML can significantly improve the diagnostic and prognostic powers of the DT system by performing data analysis, data fusion, and deep learning of twin data. Fourth, Blockchain and encryption technology could be integrated into the DT model to provide a reliable guarantee for data security. Fifth, Computer-Aided Modeling, VR, Augmented Reality, and Mixed Reality technology could enable lifelike simulations that would broaden the range of potential applications, particularly in the medical field [25], [31], [37].

TABLE I SUMMARY OF THE SOCIO-ETHICAL BENEFITS OF DTS
<table><tr><td rowspan=1 colspan=1>ImprovedDiagnostics</td><td rowspan=1 colspan=1>Provide real-time, accurate diagnostics, enabling earlydisease detection and more effective treatments.</td></tr><tr><td rowspan=1 colspan=1>Less InvasiveTreatments</td><td rowspan=1 colspan=1>Enable less invasive diagnostic and treatment methods,reducing patient burden and enhancing their healthcareexperience.</td></tr><tr><td rowspan=1 colspan=1>Faster MedicineDiscovery</td><td rowspan=1 colspan=1>Accelerate drug discovery by simulating drug interactions,reducing the time to market for new treatments.</td></tr><tr><td rowspan=1 colspan=1>Cost Reduction</td><td rowspan=1 colspan=1>Precise diagnostics and treatments reduce healthcare costsby preventing unnecessary procedures and optimizingdrug treatments.</td></tr><tr><td rowspan=1 colspan=1>PatientEmpowerment</td><td rowspan=1 colspan=1>Provide patients with insights into their health, enablingactive participation in treatment decisions.</td></tr><tr><td rowspan=1 colspan=1>DataOwnership</td><td rowspan=1 colspan=1>Promote data ownership, allowing patients to control andshare their health data.</td></tr><tr><td rowspan=1 colspan=1>Fair and EqualTreatment</td><td rowspan=1 colspan=1>DHTs provide standardized, data-driven medicaldecisions, promoting equitable care for all patients.</td></tr><tr><td rowspan=1 colspan=1>LessAnimalTesting</td><td rowspan=1 colspan=1>Reduce the need for animal testing, aligning with ethicaland sustainable practices in medicine.</td></tr></table>

TABLE II

SUMMARY OF THE SOCIO-ETHICAL RISKS OF DTS
<table><tr><td rowspan=1 colspan=1>Privacy andData Security</td><td rowspan=1 colspan=1>Extensive data collection necessitates robust securitymeasures to prevent breaches and misuse, complyingwith regulations like GDPR and HIPAA.</td></tr><tr><td rowspan=1 colspan=1>InformedConsent</td><td rowspan=1 colspan=1>Transparent consent processes are vital to maintainingtrust and ensuring patients understand the implications ofsharing their data.</td></tr><tr><td rowspan=1 colspan=1>Equity andAccessibility</td><td rowspan=1 colspan=1>Ensuring equal access to DHT technology is essential toprevent healthcare disparities.</td></tr><tr><td rowspan=1 colspan=1>Trust andAutonomy</td><td rowspan=1 colspan=1>Patients must have confidence in the responsible use ofDHTs and control over their data sharing.</td></tr><tr><td rowspan=1 colspan=1>PsychologicalImpact</td><td rowspan=1 colspan=1>Interaction with DHTs can reflect aging and healthchanges, necessitating support to cope with these effects.</td></tr><tr><td rowspan=1 colspan=1>AlgorithmicBias andFairness</td><td rowspan=1 colspan=1>Ensuring fairness in algorithms is crucial to preventhealthcare disparities and biases.</td></tr><tr><td rowspan=1 colspan=1>Liability</td><td rowspan=1 colspan=1>Clear legal frameworks are needed to defineresponsibilities for errors in DHT predictions.</td></tr><tr><td rowspan=1 colspan=1>RegulatoryCompliance</td><td rowspan=1 colspan=1>Adhering to regulations from entities like the FDA andEMA is necessary for the ethical use of DHTs.</td></tr></table>

## III. BENEFITS, RISKS, AND CHALLENGES OF DTS

Generally, DTs offer a number of potential benefits, including real-time remote monitoring, flexibility, predictive maintenance, better asset administration, scenario and risk management, enhanced collaborations, and personalization of products and services [24]. In a study about the socio-ethical benefits and socio-ethical risks of DTs in healthcare, Popa et al. interviewed participants from the four major societal sectors: industry and business, civil society, policy, and research. The benefits and risks of DTs in healthcare are summarized in Tables I and II [13], [27]. Addressing various challenges in DT applications is crucial – the need for accurate and interoperable data from various sources, a lack of standardized models and protocols, the complexity of representing physiological processes and achieving physical realism and accurate future projections, time-consuming model validation, the cost of infrastructure, data management concerns, continuous model updates, transparency and interpretability, and large-scale computation [13], [24]. To address these challenges, collaboration between healthcare professionals, data scientists, policymakers, and regulatory bodies is essential. Investments in research, standardization, and governance frameworks are needed to fully leverage the potential of DTs in healthcare while overcoming these obstacles.

TABLE III  
SUMMARY OF DTS OF BIOLOGICAL SYSTEMS FOUND IN THE LITERATURE
<table><tr><td>DT Model</td><td>Summary</td><td>Ref.</td></tr><tr><td rowspan="3">Cells</td><td>DeepLife&#x27;s technology platform focuses on drug discovery. The approach involves creating DTs of human cells.</td><td rowspan="3">[45]</td></tr><tr><td>Single-cell omics data is utilized to model cell behavior.</td></tr><tr><td>The platform aims to uncover mechanisms of action for potential drugs.</td></tr><tr><td rowspan="4">Stem Cells</td><td>Research focus: Segmentation, detection, and tracking of stem celimages</td><td rowspan="4">[47]</td></tr><tr><td>Introduction of DTs in the study</td></tr><tr><td>Implementation of lightweight deep learning methods</td></tr><tr><td>Emphasis on image analysis techniques for stem cells</td></tr><tr><td rowspan="2">Brain and Neurons</td><td>Integration of DT concepts for improved understanding •Proposal: Bionic Digital Brain (BDB) for Digital Twin-Cutting Process (DTCP) framework. •BDB monitors, predicts, optimizes, and controls cutting processes in real-time.</td><td rowspan="2">[44]</td></tr><tr><td>•Digital Neurons (DN) are basic functional units for intelligent computation. The left brain gathers theoretical processing information; the right brain receives perceptive processing information.</td></tr><tr><td rowspan="2">Heart</td><td>Fusion enables BDB to output real-time optimal control solutions; the DTCP system demonstrates precision machining effects, confirming the feasibility of DT technology.</td><td rowspan="2"></td></tr><tr><td>•Cardiovascular computer model uses GPU-acceleration for heart dynamics simulation.</td></tr><tr><td rowspan="4"></td><td>Validated with accurate replication of clinical scenarios. Reduces reliance on real patients in research.</td><td rowspan="4">[40]</td></tr><tr><td>Opens possibilities for in-silico clinical trials.</td></tr><tr><td>•Introduction of a comprehensive parameter vector for ventricular electrophysiology (EP).</td></tr><tr><td>•Proposal of an abstract reference frame for unattended manipulation of model parameters.</td></tr><tr><td rowspan="4">Heart</td><td>•Development of a fast-forward electrocardiogram (ECG) model for efficient simulation.</td><td rowspan="4"></td></tr><tr><td>Novel workflow for generating CDTs, involving anatomical and functional twinning.</td></tr><tr><td>•Demonstrated efficiency and fidelity in generating biophysically-detailed CDTs at scale.</td></tr><tr><td>•Detailed mathematical description of a fully coupled multi-scale model of the human heart.</td></tr><tr><td rowspan="4">Heart</td><td>•Proposed as a powerful tool for precision medicine and clinical decision-making. Allows personalization from ion channels to the organ level, facilitating the development of DT models.</td><td rowspan="4">[52]</td></tr><tr><td>Model validated through simulations on a personalized whole heart geometry from magnetic resonance imaging data.</td></tr><tr><td>•Used to evaluate the effects of atrial ablation scar on the cardiovascular system, offering insights for understanding and treating cardiovascular diseases.</td></tr><tr><td>Standard dissolution apparatuses have limitations in replicating colonic hydrodynamics.</td></tr><tr><td rowspan="2">Proximal Colon</td><td>•Advocate for physiologically representative models for assessing oral dosage forms targeting the colon. •Introduce a DT of the Dynamic Colon Model (DCM) to simulate human ascending colon hydrodynamics.</td><td rowspan="2">[43]</td></tr><tr><td>•DT accurately replicates flow patterns under different physiological conditions.</td></tr><tr><td rowspan="4">Vertebra</td><td>Considerations include media viscosity, volume, and peristaltic wave speed for comprehensive simulation. • ReconGAN AI framework reconstructs a realistic DT of the human vertebra.</td><td rowspan="4">[52]</td></tr><tr><td>Uses DCGAN, image processing, and FE-based optimization. Generates synthetic trabecular microstructure seamlessly integrated with the cortical shell.</td></tr><tr><td>•Transforms the geometrical model into a high-fidelity FE model.</td></tr><tr><td>•Simulates vertebral fracture response under compression and flexion loading conditions.</td></tr><tr><td rowspan="6">Left Ventricle (LV) and Aortic Root</td><td></td><td rowspan="6">[53]</td></tr><tr><td>•Multi-fidelity approach efficiently personalizes a detailed active stress model.</td></tr><tr><td>Achieved with 2 to 4 organ-scale simulations, suitable for clinical applications.</td></tr><tr><td>Models reproduce clinical pressure with good agreement.</td></tr><tr><td>Comparison of simulated and clinical biomarkers, including pressure and volume.</td></tr><tr><td>Mathematical model for liver regeneration after drug-induced damage.</td></tr><tr><td rowspan="5">Liver</td><td>DT predicts perturbations and guides experiments. •Assesses whether hypothesized mechanisms explain results.</td><td rowspan="5">[41]</td></tr><tr><td>Provides expectations for how perturbations modify experimental readouts.</td></tr><tr><td>•Enhances understanding of liver regeneration dynamics.</td></tr><tr><td></td></tr><tr><td>DTs, AI, and machine learning identify personalized ankle motion axes in ankle replacement. Patient-specific axis determined using talus center of mass as the origin.</td></tr><tr><td rowspan="4">Tibiotalar Joint</td><td>Insights contribute to understanding the ankle axis for robotic arthroplasty.</td><td rowspan="4">[54]</td></tr><tr><td>•Technology enhances precision in total ankle replacement. Highlights potential of personalized approaches in joint surgeries.</td></tr><tr><td>•Authors introduce a high-performance framework for large-scale tissue simulation.</td></tr><tr><td>Framework combines a cellular Potts model and an agent-based layer.</td></tr><tr><td rowspan="4">Tumor Tissue Autonomic</td><td>Capable of simulating tissues consisting of tens of millions of cells.</td><td rowspan="4">[55]</td></tr><tr><td>•Represents a powerful tool for studying complex biological systems at a large scale.</td></tr><tr><td>• Introduction of a multiscale neurocardiac model and simulator.</td></tr><tr><td></td></tr><tr><td rowspan="4">Nervous System</td><td></td><td rowspan="4">[56]</td></tr><tr><td>• Predicts effects of sympathetic and parasympathetic stimulation on cardiac sinoatrial node (SAN) and ventricular</td><td></td></tr><tr><td></td><td></td></tr><tr><td>myocardium. Based on experimental data and atomistic simulations.</td><td></td></tr></table>

TABLE III (CONTINUED.)
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Identifies proarrhythmia conditions and provides insights for potential neuromodulatory therapies.</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1>BloodCirculation</td><td rowspan=1 colspan=1>A DT model accurately predicts post-operative portal hypertension.•The model can improve patient outcomes and modify selection criteria.</td><td rowspan=1 colspan=1>[17]</td></tr><tr><td rowspan=1 colspan=1>CardiovascularSystem</td><td rowspan=1 colspan=1>•Synthetic PPG generation from cardiovascular DT.• Validation of platform for clustering CAD and non-CAD PPG data</td><td rowspan=1 colspan=1>[39]</td></tr><tr><td rowspan=1 colspan=1>AllergicRhinitis</td><td rowspan=1 colspan=1>• Introduction of a scalable framework for modeling dynamic changes in DTs.•Applicable on cellulome- and genome-wide scales.Aims to prioritize upstream regulators (URs) for biomarker and drug discovery.Enables organization and prioritization of UR genes.•Provides a valuable tool for advancing biomarker and drug discovery efforts.</td><td rowspan=1 colspan=1>[57]</td></tr><tr><td rowspan=1 colspan=1>Breast CancerPatients</td><td rowspan=1 colspan=1>Authors propose a machine learning (ML) approach for real-time and robust DTs of cancers.Conceptualized for use in the Metaverse for diagnosis and treatment.• Utilizes four classic ML techniques: ML linear regression (ML LR), Decision tree regression (DTR), Random ForestRegression (RFR), Gradient Boosting Algorithm (GBA).Aims to enhance accuracy and efficiency in cancer diagnostics and treatment planning.•Represents an innovative application of ML techniques in the healthcare domain.</td><td rowspan=1 colspan=1>[58]</td></tr><tr><td rowspan=1 colspan=1>CervicalVertebralMaturation</td><td rowspan=1 colspan=1>•Blockchain-based metaverse for dental DTs of cervical vertebral maturation (CVM).•Utilizes MobileNetV2 for efficient automated diagnosis of CVM images.•Simple, fast, and cost-effective digital twinning suitable for medical specialists.• High-performance on a small dataset highlights the potential for low-cost deep learning in diagnosis.DTs in dentistry reduce infrastructure and cut costs for patients.</td><td rowspan=1 colspan=1>[59]</td></tr><tr><td rowspan=1 colspan=1>CognitiveUser Model</td><td rowspan=1 colspan=1>Investigates coupling a geometrical model with a cognitive digital user.•Evaluates the usability of different interface variants and virtual product representations</td><td rowspan=1 colspan=1>[60]</td></tr><tr><td rowspan=1 colspan=1>DiabetesPatients</td><td rowspan=1 colspan=1>•Research defines seven stages of diabetes reversal.Examines changes in these stages, along with metrics like hemoglobin A1c (HbA1c) and weight.•Precision nutrition therapy enabled by a DT is employed for a 90-day treatment period.Significant progress was observed in reversing diabetes stages during the therapy.•Suggests monitoring and understanding these stages could benefit clinicians and patients in precision nutrition therapy.</td><td rowspan=1 colspan=1>[61]</td></tr><tr><td rowspan=1 colspan=1>ImmuneResponse</td><td rowspan=1 colspan=1>•Introduction of a modular software design for developing medical DTs customized for individual patients using diverse data.Involves an open-source platform supporting model integration and simulation.Facilitates a decentralized, community-based model-building process.Ic  te plao tielatyunleio al.Signifies the potential for collaborative, patient-specific DT development in medical research.</td><td rowspan=1 colspan=1>[62]</td></tr><tr><td rowspan=1 colspan=1>Lung CancerPatients</td><td rowspan=1 colspan=1>•Development of a new deep neural model for searching IoT vulnerabilities in healthcare DTs.The model captures bi-directional context relationships among risky code keywords.Outperforms state-of-the-art deep learning-based methods for vulnerability detection.</td><td rowspan=1 colspan=1>[63]</td></tr><tr><td rowspan=1 colspan=1>DiabetesPatients</td><td rowspan=1 colspan=1>•Systematic method for creating a &#x27;Metabolic Digital Twin Envelope&#x27; (MDTE) for Type 1 diabetes.MDTE allows at-home tests, capturing diverse blood glucose responses with minimal testing.•Method considers errors from simplified models and unmodeled disturbances.Utilizes convex optimization for developing an insulin injection policy.•Policy minimizes peak blood glucose levels and ensures a strict lower bound on hyperglycemic events probability.</td><td rowspan=1 colspan=1>[64]</td></tr><tr><td rowspan=1 colspan=1>Patients</td><td rowspan=1 colspan=1>•Algorithm developed for automated estimation of patient height and weight during CT.Automated estimation provides high precision for protocol design in CT.</td><td rowspan=1 colspan=1>[65]</td></tr><tr><td rowspan=1 colspan=1>MultipleSclerosisPatients</td><td rowspan=1 colspan=1>•The proposed platform uses Big Data and AI to study Multiple Sclerosis patients&#x27; behavioral changes.Emphasizes understanding rare brain disorders affecting around 30 million people in Europe.•Platform includes diagnostic, rehabilitation components, and advanced analytical tools.Highlights the importance of effective data sharing and standardized processing.•Aims to translate research findings into clinical applications for improved patient care.</td><td rowspan=1 colspan=1>[66]</td></tr><tr><td rowspan=1 colspan=1>Stroke Patients</td><td rowspan=1 colspan=1>DT model accurately projects patient trajectories leading up to and beyond ischemic stroke.Utilizes ICD codes and lab values for accuracy.•Simulated trajectories closely match real data.Potential applications in informing clinical decisions.•Suggested use in providing virtual control arms for efficient clinical trials.</td><td rowspan=1 colspan=1>[67]</td></tr></table>

## IV. DTS OF BIOLOGICAL SYSTEMS

As biological systems have different levels of organization, different types of DTs can be constructed. Starting with DTs of bodily systems, organs, and then to finer components at the cellular, subcellular, and molecular levels [26].

At the system level, Laubenbacher et al. [30] present a step-bystep guide to building a DT model of the human immune system. Mazumder et al. [39] constructed a cardiovascular DT model consisting of a two-chambered heart along with pulmonary and systemic flow and components of the central nervous system to autoregulate blood pressure, modeled by hemodynamic equations and a baroreflex-based pressure control mechanism. Golse et al. [17] developed a mathematical model encompassing the entire blood circulation, automatically adjusted based on patient characteristics. Their findings illustrated that a DT model, utilizing the estimated hepatic flow rate as input data, accurately anticipated post-operative portal hypertension.

A recent study by Viola et al. [40] presented a virtual heart model with all the main features of the cardiovascular function, accounting for the dynamics of the active myocardium and passive valves, the hemodynamics of the blood, and the electrophysiology of the heart tissue. The GPU-accelerated model utilizes a vast number of spatial degrees of freedom and time steps, capturing the complexity of heart dynamics with impeccable accuracy. However, the absence of biochemical data in building this DT compromises the authors’ claim of accuracy. Other organs modeled by DT technology include the liver [41], [42], the colon [43], and the brain [44].

Significant progress has been made in the modeling of cells and cellular structures, with one recent development being the introduction of DeepLife – a platform designed for generating DTs of human cells. DeepLife utilizes omics data to simulate DTs of cells in silico. Shifting from in vitro to in silico analysis for single-cell studies carries significant implications for drug discovery. By leveraging DTs to forecast cellular responses to various molecules, DeepLife can efficiently assess billions of drug combinations [45]. In an earlier study, Karr et al. [46] formulated a ’whole-cell’ model for the bacterium Mycoplasma genitalium, a human urogenital parasite with a genome housing 525 genes. The DT model provided insights into numerous previously unobserved cellular behaviors, including in vivo rates of protein-DNA association and an inverse relationship between the durations of DNA replication initiation and replication. Additionally, directed by model predictions, the experimental analysis identified previously undetected kinetic parameters and biological functions. Du et al. [47] constructed DT models based on image analysis of stem cells, aiming to improve segmentation, detection, and tracking methods of stem cell images in the fields of regenerative medicine and tissue damage restoration. Table III shows a list of DTs of biological systems found in current literature.

Considering that the most sophisticated biological system is the human body, there have been multiple attempts to computationally model it. One of the earliest applications in this regard is HumMod, a human model comprising 5000 variables describing cardiovascular, respiratory, renal, neural, endocrine, skeletal muscle, and metabolic physiology, modeled by a collection of approximately 10000 interconnected algebraic and differential equations. HumMod is accessible at http://hummod.org [48], [49]. However, it is crucial to keep in mind that while HumMod is a digital representation of the human body, it is not a ‘DT’ as it lacks the bidirectional digital thread and the ongoing data exchange between the physical and the digital entities. On the other hand, recent attempts at constructing DTs of patients have shown incredible potential, as summarized in Table III.

## V. CONCLUSION

DTs are sophisticated models capable of simulating a spectrum of biological systems from the entire human body to cellular structures, promising a new era of possibilities in biomedicine. By facilitating disease modeling, drug testing, and personalized medicine, DTs offer enhanced diagnostic accuracy, minimally invasive treatments, expedited drug discovery, cost mitigation, patient empowerment, and ethical advancements like data ownership and reduced reliance on animal testing. However, the realization of these benefits hinges upon collaborative efforts of various stakeholders including healthcare professionals, data scientists, policymakers, and regulatory bodies. Overcoming challenges with data accuracy, establishing standardization protocols, and managing computational complexity necessitates cohesive partnerships and coordinated action. Robust governance frameworks are imperative to ensure the ethical and equitable deployment of DTs in healthcare. With continued collaboration, innovation, and ethical stewardship, DTs prompt a course towards a future where healthcare is not only data-driven and efficient but also more humane, equitable, and patient-centered.

## AUTHOR CONTRIBUTIONS

Ghufran A. Alsalloum drafted the manuscript. Ghaleb A. Husseini, Kelly M. Percival and Nour M. Al Sawaftah reviewed and edited the manuscript.

All authors read and approved the final version.

## DATA AVAILABILITY

Not applicable.

## CONFLICT OF INTEREST STATEMENT

The authors declare no conflict of interest.

## REFERENCES

[1] A. L. Jenner, R. A. Aogo, C. L. Davis, A. M. Smith, and M. Craig, “Leveraging computational modeling to understand infectious diseases,” Curr. Pathobiol. Rep., vol. 8, no. 4, pp. 149–161, 2020, doi: 10.1007/s40139-020-00213-x.

[2] L. Mais, J. Rodriguez, N. Melis, A. Vacca, and M. Mascia, “Computational modelling as a design tool for bioelectrochemical systems,” Curr. Opin. Electrochemistry, vol. 44, Apr. 2024, Art. no. 101460, doi: 10.1016/j.coelec.2024.101460.

[3] E. M. Wülfers et al., “Whole-heart computational modelling provides further mechanistic insights into ST-elevation in Brugada syndrome,” IJC Heart Vasculature, vol. 51, Apr. 2024, Art. no. 101373, doi: 10.1016/j.ijcha.2024.101373.

[4] R. Rajaganapathi, R. Mahendran, D. Sivaganesan, M. R. Vadivel, M. R. Joel, and V. Kannan, “An IoT enabled computational model and application development for monitoring cardiovascular risks,” e-Prime - Adv. Elect. Eng., Electron. Energy, vol. 8, Jun. 2024, Art. no. 100513, doi: 10.1016/j.prime.2024.100513.

[5] M. S. Dihan et al., “Digital twin: Data exploration, architecture, implementation and future,” Heliyon, vol. 10, no. 5, Mar. 2024, Art. no. e26503, doi: 10.1016/j.heliyon.2024.e26503.

[6] Q. Sun et al., “Patient spontaneous effort estimation in digital twin model with B-spline function,” IFAC-PapersOnLine, vol. 56, no. 2, pp. 2096–2101, Jan. 2023, doi: 10.1016/j.ifacol.2023.10.1111.

[7] H. Yang and Z. Jiang, “Decision support for personalized therapy in implantable medical devices: A digital twin approach,” Expert Syst. Appl., vol. 243, Jun. 2024, Art. no. 122883, doi: 10.1016/j.eswa.2023.122883.

[8] M. Parollo et al., “PO-06-063 Clinical validation of a novel digital twin framework for ventricular functional substrate simulation in ischemic and non-ischemic patients,” Heart Rhythm, vol. 21, no. 5, May 2024, Art. no. S691, doi: 10.1016/j.hrthm.2024.03.1689

[9] J. Hong and J. Kim, “The digital twin for rehabilitation of gastrointestinal motility in SCI patients: A pilot study,” Arch. Phys. Med. Rehabil., vol. 100, no. 10, pp. e127–e128, Oct. 2019, doi: 10.1016/j.apmr.2019.08.383.

[10] Y. Liu et al., “A novel cloud-Based framework for the elderly healthcare services using digital twin,” IEEE Access, vol. 7, pp. 49088–49101, 2019, doi: 10.1109/ACCESS.2019.2909828.

[11] N. A. Trayanova and A. Prakosa, “Up digital and personal: How heart digital twins can transform heart patient care,” Heart Rhythm, vol. 21, no. 1, pp. 89–99, Jan. 2024, doi: 10.1016/j.hrthm.2023.10.019.

[12] D. Guo and D. Yao, “The digital twins brain (DTB): A simulation platform for Large-Scale brain dynamics,” Int. J. Psychophysiol., vol. 168, Oct. 2021, Art. no. S197, doi: 10.1016/j.ijpsycho.2021.07.536.

[13] M. Cellina et al., “Digital twins: The new frontier for personalized medicine?,” Appl. Sci., vol. 13, no. 13, Jan. 2023, Art. no. 7940, doi: 10.3390/app13137940.

[14] A. Rahmim et al., “Theranostic digital twins for personalized radiopharmaceutical therapies: Reimagining theranostics via computational nuclear oncology,” Front. Oncol., vol. 12, 2022, Art. no. 1062592, doi: 10.3389/fonc.2022.1062592.

[15] E. A. Stahlberg et al., “Exploring approaches for predictive cancer patient digital twins: Opportunities for collaboration and innovation,” Front. Digit. Health, vol. 4, 2022, Art. no. 1007784, doi: 10.3389/fdgth.2022.1007784.

[16] G. M. Thiong’o and J. T. Rutka, “Digital twin technology: The future of predicting neurological complications of pediatric cancers and their treatment,” Front. Oncol., vol. 11, 2022, Art. no. 781499, doi: 10.3389/fonc.2021.781499.

[17] N. Golse et al., “Predicting the risk of post-hepatectomy portal hypertension using a digital twin: A clinical proof of concept,” J. Hepatol., vol. 74, no. 3, pp. 661–669, Mar. 2021, doi: 10.1016/j.jhep.2020.10.036.

[18] J. Yu, Y. Song, D. Tang, and J. Dai, “A digital twin approach based on nonparametric Bayesian network for complex system health monitoring,” J. Manuf. Syst., vol. 58, pp. 293–304, Jan. 2021, doi: 10.1016/j.jmsy.2020.07.005.

[19] R. Sahal, S. H. Alsamhi, K. N. Brown, D. O’Shea, and B. Alouffi, “Blockchain-based digital twins collaboration for smart pandemic alerting: Decentralized COVID-19 pandemic alerting use case,” Comput. Intell. Neurosci., vol. 2022, 2022, Art. no. 7786441, doi: 10.1155/2022/ 7786441.

[20] G. Fagherazzi and P. Ravaud, “Digital diabetes: Perspectives for diabetes prevention, management and research,” Diabetes Metab., vol. 45, no. 4, pp. 322–329, Sep. 2019, doi: 10.1016/j.diabet.2018.08.012.

[21] S. Elkefi and O. Asan, “Digital twins for managing health care systems: Rapid literature review,” J. Med. Internet Res., vol. 24, no. 8, 2022, Art. no. e37641, doi: 10.2196/37641.

[22] A. McClenaghan, J. Gopsill, R. Ballantyne, and B. Hicks, “Cost benefit analysis for digital twin model selection at the time of investment,” Procedia CIRP, vol. 120, pp. 1197–1202, Jan. 2023, doi: 10.1016/j.procir.2023.09.148.

[23] F. Oettl, L. Eckart, and J. Schilp, “Cost estimation approach of a digital twin implementation in industry,” Procedia CIRP, vol. 118, pp. 318–323, Jan. 2023, doi: 10.1016/j.procir.2023.06.055.

[24] A. Rasheed, O. San, and T. Kvamsdal, “Digital twin: Values, challenges and enablers from a modeling perspective,” IEEE Access, vol. 8, pp. 21980–22012, 2020, doi: 10.1109/ACCESS.2020.2970143.

[25] P. Armeni, I. Polat, L. M. De Rossi, L. Diaferia, S. Meregalli, and A. Gatti, “Digital twins in healthcare: Is it the beginning of a new Era of evidence-based medicine? a critical review,” J. Pers. Med., vol. 12, no. 8, 2022, Art. no. 1255, doi: 10.3390/jpm12081255.

[26] M. N. Kamel Boulos and P. Zhang, “Digital twins: From personalised medicine to precision public health,” J. Pers. Med., vol. 11, no. 8, 2021, Art. no. 745, doi: 10.3390/jpm11080745.

[27] E. O. Popa, M. van Hilten, E. Oosterkamp, and M. J. Bogaardt, “The use of digital twins in healthcare: Socio-ethical benefits and socioethical risks,” Life Sci. Soc. Policy, vol. 17, no. 1, pp. 1–25, 2021, doi: 10.1186/s40504-021-00113-x.

[28] M. W. Grieves, “Digital twins: Past, present, and future,” in The Digital Twin, N. Crespi, A. T. Drobot, and R. Minerva, Eds., Cham, Switzerland: Springer, 2023, pp. 97–121. doi: 10.1007/978-3-031-21343-4\_4.

[29] T. Sun, X. He, and Z. Li, “Digital twin in healthcare: Recent updates and challenges,” Digit. Health, vol. 9, 2023, Art. no. 20552076221149651, doi: 10.1177/20552076221149651.

[30] R. Laubenbacher et al., “Building digital twins of the human immune system: Toward a roadmap,” npj Digit. Med., vol. 5, no. 1, 2022, Art. no. 64, doi: 10.1038/s41746-022-00610-z.

[31] T. Sun, X. He, X. Song, L. Shu, and Z. Li, “The digital twin in medicine: A key to the future of healthcare?,” Front. Med., vol. 9, 2022, Art. no. 907066, doi: 10.3389/fmed.2022.907066.

[32] M. G. Kapteyn, J. V. R. Pretorius, and K. E. Willcox, “A probabilistic graphical model foundation for enabling predictive digital twins at scale,” Nature Comput. Sci., vol. 1, no. 5, pp. 337–347, May 2021, doi: 10.1038/s43588-021-00069-0.

[33] C. Angulo, L. Gonzalez-Abril, C. Raya, and J. A. Ortega, “A proposal to evolving towards digital twins in healthcare,” in Proc. Int. Work-Conf. Bioinf. Biomed. Eng., May 2020, pp. 418–426. doi: 10.1007/978-3-030-45385-5\_37.

[34] G. Ahmadi-Assalemi et al., “Digital twins for precision healthcare,” in Proc. Adv. Sci. Tech. Sec. Appl., New York City, USA: Springer, 2020, pp. 133–158. doi: 10.1007/978-3-030-35746-7\_8.

[35] R. Fardousi, F. Laamarti, M. A. Hossain, C. Yang, and A. E. Saddik, “Digital twins for well-being: An overview,” Digit. Twin, vol. 1, 2022, Art. no. 7, doi: 10.12688/digitaltwin.17475.1.

[36] C. Tang, W. Yi, E. Occhipinti, Y. Dai, S. Gao, and L. G. Occhipinti, “Human body digital twin: A master plan,” Sep. 2023, arXiv:2307.09225.

[37] G. Coorey et al., “The health digital twin to tackle cardiovascular disease— A review of an emerging interdisciplinary field,” NPJ Digit. Med., vol. 5, no. 1, 2022, Art. no. 126, doi: 10.1038/s41746-022-00640-7.

[38] S. Ghatti et al., “Digital twins in healthcare: A survey of current methods,” Arch. Clin. Biomed. Res., vol. 07, no. 03, pp. 365–381, 2023, doi: 10.26502/acbr.50170352.

[39] O. Mazumder, D. Roy, S. Bhattacharya, A. Sinha, and A. Pal, “Synthetic PPG generation from haemodynamic model with baroreflex autoregulation: A Digital twin of cardiovascular system,” in Proc. 41st Annu. Int. Conf. IEEE Eng. Med. Biol. Soc., Jul. 2019, pp. 5024–5029. doi: 10.1109/EMBC.2019.8856691.

[40] F. Viola, G. Del Corso, R. De Paulis, and R. Verzicco, “GPU accelerated digital twins of the human heart open new routes for cardiovascular research,” Sci. Rep., vol. 13, no. 1, 2023, Art. no. 8230, doi: 10.1038/s41598-023-34098-8.

[41] J. Zhao, A. Ghallab, R. Hassan, S. Dooley, J. G. Hengstler, and D. Drasdo, “A liver digital twin for in silico testing of cellular and inter-cellular mechanisms in regeneration after drug-induced damage,” iScience, vol. 27, Sep. 2023, Art. no. 108077, doi: 10.1016/j.isci.2023.108077.

[42] K. Subramanian, “Digital twin for drug discovery and Development—The virtual liver,” J. Indian Inst. Sci., vol. 100, no. 4, pp. 653–662, Oct. 2020, doi: 10.1007/s41745-020-00185-2.

[43] M. Schütt et al., “Simulating the hydrodynamic conditions of the human ascending colon: A digital twin of the dynamic colon model,” Pharmaceutics, vol. 14, no. 1, Jan. 2022, Art. no. 184, doi: 10.3390/pharmaceutics14010184.

[44] J. Chen et al., “Bionic digital brain realizing the digital twin-cutting process,” Robot. Comput.-Integr. Manuf., vol. 84, Dec. 2023, Art. no. 102591, doi: 10.1016/j.rcim.2023.102591.

[45] “How digital twins of human cells are accelerating drug discovery,” Accessed: Oct. 12, 2023, [Online]. Available: https://www.nature.com/ articles/d43747-022-00108-3

[46] J. R. Karr et al., “A Whole-Cell computational model predicts phenotype from genotype,” Cell, vol. 150, no. 2, pp. 389–401, Jul. 2012, doi: 10.1016/j.cell.2012.05.044.

[47] X. Du, M. Liu, and Y. Sun, “Segmentation, detection, and tracking of stem cell image by digital twins and lightweight deep learning,” Comput. Intell. Neurosci., vol. 2022, 2022, Art. no. 6003293, doi: 10.1155/2022/ 6003293.

[48] R. Hester et al., “HumMod: A modeling environment for the simulation of integrative human physiology,” Front. Physiol., vol. 2, 2011, Art. no. 12, Accessed: Oct. 12, 2023, [Online]. Available: https://www.frontiersin.org/ articles/10.3389/fphys.2011.00012

[49] C. R. I. Sims, L. R. Delima, A. Calimaran, R. Hester, and W. A. Pruett, “Validating the physiologic model hummod as a substitute for clinical trials involving acute normovolemic hemodilution,” Anesth. Analg., vol. 126, no. 1, pp. 93–101, Jan. 2018, doi: 10.1213/ANE.0000000000002430.

[50] K. Gillette et al., “A Framework for the generation of digital twins of cardiac electrophysiology from clinical 12-leads ECGs,” Med. Image Anal., vol. 71, Jul. 2021, Art. no. 102080, doi: 10.1016/j.media.2021.102080.

[51] T. Gerach et al., “Electro-Mechanical Whole-Heart digital twins: A fully coupled Multi-Physics approach,” Mathematics, vol. 9, no. 11, Art. no. 1247, Jan. 2021, doi: 10.3390/math9111247.

[52] H. Ahmadian et al., “Toward an artificial intelligence-assisted framework for reconstructing the digital twin of vertebra and predicting its fracture response,” Int. J. Numer. Methods Biomed. Eng., vol. 38, no. 6, 2022, Art. no. e3601, doi: 10.1002/cnm.3601.

[53] A. Jung, M. A. F. Gsell, C. M. Augustin, and G. Plank, “An integrated workflow for building digital twins of cardiac electromechanics—A multi-fidelity approach for personalising active mechanics,” Mathematics, vol. 10, no. 5, Jan. 2022, Art. no. 823, doi: 10.3390/math10050823.

[54] P. Hernigou, R. Olejnik, A. Safar, S. Martinov, J. Hernigou, and B. Ferre, “Digital twins, artificial intelligence, and machine learning technology to identify a real personalized motion axis of the tibiotalar joint for robotics in total ankle arthroplasty,” Int. Orthopaedics, vol. 45, no. 9, pp. 2209–2217, Sep. 2021, doi: 10.1007/s00264-021-05175-2.

[55] E. Behle, J. M. Herold, and A. H. Schug, “Towards cellular digital twins of in vivo tumors,” Biophysical J., vol. 122, no. 3, pp. 301a–302a, Feb. 2023, doi: 10.1016/j.bpj.2022.11.1700.

[56] P. C. Yang et al., “A multiscale predictive digital twin for neurocardiac modulation,” J. Physiol., vol. 601, no. 17, pp. 3789–3812, 2023, doi: 10.1113/JP284391.

[57] X. Li et al., “A dynamic single cell-based framework for digital twins to prioritize disease genes and drug targets,” Genome Med., vol. 14, no. 1, May 2022, Art. no. 48, doi: 10.1186/s13073-022-01048-4.

[58] M. B. Jamshidi, M. Ebadpour, and M. M. Moghani, “Cancer digital twins in metaverse,” in Proc. 20th Int. Conf. Mechatronics - Mechatronika, Dec. 2022, pp. 1–6, doi: 10.1109/ME54704.2022.9983328.

[59] O. Moztarzadeh et al., “Metaverse and medical diagnosis: A blockchainbased digital twinning approach based on MobileNetV2 algorithm for cervical vertebral maturation,” Diagn,, vol. 13, no. 8, 2023, Art. no. 1485, doi: 10.3390/diagnostics13081485.

[60] K. Preuss et al., “Towards a human-centered digital twin,” Procedia CIRP, vol. 118, pp. 324–329, 2023, doi: 10.1016/j.procir.2023.06.056.

[61] P. Shamanna et al., “Type 2 diabetes reversal with digital twin technologyenabled precision nutrition and staging of reversal: A retrospective cohort study,” Clin. Diabetes Endocrinol., vol. 7, no. 1, Nov. 2021, Art. no. 21, doi: 10.1186/s40842-021-00134-7.

[62] J. Masison et al., “A modular computational framework for medical digital twins,” Proc. Nat. Acad. Sci., vol. 118, no. 20, 2021, Art. no. e2024287118, doi: 10.1073/pnas.2024287118.

[63] J. Zhang, L. Li, G. Lin, D. Fang, Y. Tai, and J. Huang, “Cyber resilience in healthcare digital twin on lung cancer,” IEEE Access, vol. 8, pp. 201900–201913, 2020, doi: 10.1109/ACCESS.2020.3034324.

[64] G. C. Goodwin, M. M. Seron, A. M. Medioli, T. Smith, B. R. King, and C. E. Smart, “A systematic stochastic design strategy achieving an optimal tradeoff between peak BGL and probability of hypoglycaemic events for individuals having type 1 diabetes mellitus,” Biomed. Signal Process. Control, vol. 57, Mar. 2020, Art. no. 101813, doi: 10.1016/j.bspc.2019.101813.

[65] F. Geissler et al., “Personalized computed tomography - Automated estimation of height and weight of a simulated digital twin using a 3D camera and artificial intelligence,” RoFo Fortschr. Geb. Rontgenstrahlen Bildgeb. Verfahr., vol. 193, no. 4, pp. 437–445, 2021, doi: 10.1055/a-1253-8558.

[66] D. Petrova-Antonova, I. Spasov, I. Krasteva, I. Manova, and S. Ilieva, “A digital twin platform for diagnostics and rehabilitation of multiple sclerosis,” in Proc. Int. Conf. Computati. Sci. Appl., 2020, pp. 503–518. doi: 10.1007/978-3-030-58799-4\_37.

[67] A. Allen et al., “A digital twins machine learning model for forecasting disease progression in stroke patients,” Appl. Sci., vol. 11, 2021, Art. no. 5576, doi: 10.3390/APP11125576.

## Authors

Ghufran A. Alsalloum , Nour M. Al Sawaftah, Kelly M. Percival, and Ghaleb A. Husseini , Member, IEEE

## Figure Descriptions

**Figure 1.** Scopus search results for query: (TITLE-ABS-KEY(“Digital twin” OR “Digital twins”)) and query: (TITLE-ABS-KEY((“Digital Twin” OR “Digital twins”) AND (“Medicine” OR ” Healthcare”)))

**Figure 2.** A DT model consists of three components: the real space, the virtual space, and the bidirectional digital thread connecting them.

**Figure 3.** A DT model is constructed through 5 stages: planning stage, development stage, personalization stage, testing and validation stage, and ongoing learning stage. The 5 dimensions of DT should be addressed during the planning stage.

**Figure 4.** DT models are enhanced with the integration of advanced technology like the IoT, AI, VR, and others.