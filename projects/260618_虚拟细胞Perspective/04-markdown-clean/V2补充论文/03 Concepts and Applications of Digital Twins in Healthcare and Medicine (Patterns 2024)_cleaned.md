# Concepts and applications of digital twins in healthcare and medicine

THE BIGGER PICTURE Recent advances in technology have facilitated the efficient collection and detailed analysis of human health data. The creation of personalized healthcare digital twins (DTs) permits simulations that predict individual health trajectories and disease progression. Using various health metrics, these DTs enable a quantitative analysis of vital life processes, provide dynamic health guidance, and refine strategies for disease treatment. This innovative approach aims to enhance the mathematical understanding of biological mechanisms, transform existing clinical practices, and truly personalize medical care.

## SUMMARY

The digital twin (DT) is a concept widely used in industry to create digital replicas of physical objects or systems. The dynamic, bi-directional link between the physical entity and its digital counterpart enables a realtime update of the digital entity. It can predict perturbations related to the physical object’s function. The obvious applications of DTs in healthcare and medicine are extremely attractive prospects that have the po tential to revolutionize patient diagnosis and treatment. However, challenges including technical obstacles, biological heterogeneity, and ethical considerations make it difficult to achieve the desired goal. Advances in multi-modal deep learning methods, embodied AI agents, and the metaverse may mitigate some difficulties. Here, we discuss the basic concepts underlying DTs, the requirements for implementing DTs in medicine, and their current and potential healthcare uses. We also provide our perspective on five hallmarks for a healthcare DT system to advance research in this field.

## INTRODUCTION

A digital twin (DT) is a digital and virtual representation of any physical entity. At the core of DTs is a mathematical model that uses data gathered from the physical entity to update the digital counterpart. This iterative approach then allows data to be generated from the digital entity indistinguishable from the physical entity.<sup>1</sup> DTs are widely used in the engineering and manufacturing industries for monitoring and modeling processes and optimizing efficiency.<sup>2</sup> Examples include jet engine performance evaluation and the development of smart cities.<sup>3</sup> In the context of medicine (Figure 1), the physical entity can refer to the patient being studied in their real-world existence, incorpo rating all molecular, physiological, lifestyle, and environmental information across time.<sup>4</sup> The virtual entity is, therefore, a digital replica of the patient, or even a virtual space of many digital patients. These digital replicas have characteristics similar to those of the patient, which enable predictions and simulations of the biological processes or disease states using data collected from the patient. The physical and virtual entities communicate via a physical-to-virtual connection to allow continuous update of the parameters that reflect the state of the physical entity.<sup>5</sup> In essence, a medical DT represents a virtual representation where clinical and medical decisions can be tested before application in the actual patient.<sup>6</sup> Therefore, this enables the real-time dynamic modeling of biochemical pathways, cells, tissues, diseases, and, ultimately, the entire human body, making personalized medicine a tantalizing reality.

The unique opportunities offered by DTs address the human population as individuals to provide improved and personalized therapies and preventions.<sup>7,8</sup> The construction of a DT in medicine will require the integration of diverse information such as clinical data, real-time physiological changes, and the -omics of an individual. For example, DTs may enable the provision of a personalized, on-demand risk profile for chronic diseases, offer lifestyle suggestions to mitigate these risks, deliver warnings about immediate health risks, and provide alerts for pre-emptive diagnostic tests.<sup>9</sup> Evaluating individual patient responses to a particular drug and forecasting its efficacy and potential adverse effects will also be possible. DTs, therefore, represent a faithful implementation of personalized medicine. 10–16

While the application of DTs in healthcare will represent an essential step toward truly personalized medicine, the significant heterogeneity inherent in human populations in genomics, physiology, lifestyles, and environment represents a real and significant hurdle. Significant developments in artificial intelligence (AI), large language models (LLMs), and wearable devices may provide solutions to some of these hurdles. This article provides an overview of the challenges and opportunities offered by these latest developments and their potential integration into a medical DT platform.

We then review some examples of DTs already used in healthcare and medicine. Finally, we suggest some critical components for the ideal medical DT.

## CHALLENGES AND OPPORTUNITIES TO DT IMPLEMENTATION IN MEDICINE

## Data acquisition

One of the major challenges of a medical DT is the acquisition of sufficient data to

make meaningful predictions about the physical entity (the patient). The All of Us research program launched by the U.S. National Institutes of Health in 2018 seeks to gather data from at least 1 million individuals to create one of the largest and most diverse datasets on health and genomics.<sup>17</sup> Furthermore, nextgeneration sequencing, high-throughput multi-omics profiling, and mass spectrometry can evaluate the transcriptome, methylome, proteome, histone post-translational modifications, and the microbiome at unprecedented speed and scale.<sup>18</sup> Nevertheless, the All of Us program focuses on the U.S. population, which may limit any predictive outputs. Therefore, the blueprint of the All of Us program should be established in multiple countries to achieve a truly global and representative cohort.

In addition, to handle large amounts of data, the medical DT should be able to ensure real-time data collection, integration, and interoperability among different platforms and systems. The maintenance of data fidelity is also very important.<sup>19</sup> For instance, constructing a high-fidelity virtual patient is challenging due to the typically sparse communication rate between the physical and virtual entities compared with mechanistic processes. Therefore, continuous monitoring of static multi-modal health data, including clinical phenotypes and multi-omics such as genomics, metabolism, physiology, and lifestyle parameters, is required. There is also a need for health data standardization to enable data integration and interoperability among different DT providers. Furthermore, advances in biosensor technology have enabled real-time data capture using small, implanted biosensors. Small broadband acoustic and mechanical sensing devices can accurately and continuously measure respiratory airflow, intestinal motility, and other physiological events, such as the cardiac cycle.<sup>20</sup> Self-sustaining wireless charging using metamaterial surfaces has been explored to enable battery-less pacemakers. 21 Soft wearable sensors with wireless communication capability will be the next frontier in population health data acquisition. Such wearable digital health technologies are developing rapidly to make previously unavailable data outside of the clinic, such as behavioral and physiological data, available to clinicians so that additional considerations can be considered in clinical decisions and diagnoses.<sup>22</sup> In addition, facial, fundus, and tongue images can be used to predict underlying pathologies such as cardiovascular disease and diabete s.<sup>23,24</sup> These images can be obtained using standard imaging tools. The ultimate application of a medical DT is, therefore, an integration of these multiscale data to observe and predict deviations from the normal state of each individual.<sup>25</sup> For example, diabetic patients can be provided with customized recommendations on how to improve their health by tracking food consumption, physical activities, and daily life routines. The medical DT platform can also search the virtual world for similar patients to glean peer insights on improving quality of life.

## Building with AI and metaverse Opportunities

To construct a medical DT with high performance in making efficient and inclusive decisions, integrating large-scale AI models into healthcare is necessary. In addition, high-quality datasets are required to train these integrated AI modules.<sup>26</sup> Data acquired from super cohorts, such as the All of Us program, are ideal for this purpose. Such integrated AI modules can take multi-modal data to make clinical diagnoses,<sup>7,27,28</sup> predict treatment outcomes,<sup>29,30</sup> and interpret radiographical images.<sup>31–33</sup> DTs created using large multi-modal AI models are more likely to mimic their real-life counterparts. Such approaches have been proposed in oncology,<sup>34</sup> cardiovascular health, 14 and neurodegenerative disorders.<sup>15</sup> Platforms for collecting and providing large amounts of multi-modal data have also been established.<sup>10,35</sup>

Recent advances in LLMs, embodied AI, and the metaverse provide exceptional opportunities to make medical DTs a reality.<sup>36</sup> LLMs refer to deep neural networks trained on vast amounts of text with billions of parameters that can understand and generate human-like text.<sup>37,38</sup> Multi-modal LLMs,<sup>28,39,40</sup> which encompass diverse input modes in addition to textual inputs within a unified framework, set the stage for a comprehensive approach to healthcare. Addressing these challenges wil require a foundation AI system<sup>41</sup> that is capable of integration and interpretation of multi-modal data and will output with both holistic and specialist modes. This offers transformative potential for various healthcare scenarios, from answering health questions to clinical diagnostics and mortality prediction.<sup>42–44</sup> Leveraging LLMs to improve medical DT models will also lead to better predictions of disease progression and optimized treatment plans (Figure 2A). Through enhanced linguistic competencies, LLMs can convincingly replicate human-like thought patterns and emotional responses.<sup>45</sup> These models can emulate behaviors, decision-making patterns, and personality traits previously perceived as human by tailoring their interactions based on natural language inputs.<sup>46</sup> These unique characteristics will allow for customization and personalization,<sup>47</sup> which align well with the need to construct medical DT models. LLMs can also collaborate with medical DT models to provide dynamic and real-time simulation of physiological processes and patient-specific health conditions. Moreover, the integration of LLMs with DTs can enhance the ability to make informed decisions in scenarios where the underlying mechanisms are not clear.<sup>14,48</sup>

Embodied AI learns from interactions with environments instead of static datasets<sup>49</sup> (Figure 2B). In medicine, embodied AI has been playing important roles in mental healthcare<sup>50</sup> and medical robotics.<sup>51</sup> One successful story is the development and use of embodied AI robots as DTs of psychotherapists that provide therapy interventions to children with autism spectrum disorders.<sup>52</sup> The incorporation of LLMs can also seamlessly integrate various models and modalities, as well as orchestrate complex tasks such as planning, scheduling, and collaboration.

This will pave the way for the development of versatile, general purpose embodied AI systems.<sup>28</sup> These LLM-powered embodied AI models are often referred to as AI agents.<sup>53</sup> Such AI agents can perceive and interpret their surroundings, tackle and resolve problems, and exhibit intelligent behaviors (Figure 2C). This can be achieved autonomously in conjunction with other AI agents or in synergy with human beings. Combining DTs with AI agents may redefine patient care, diagnosis, and treatment.<sup>54</sup> By leveraging insights gained from human behavior and decision-making processes, AI agents can be used to build virtual patient models, autonomous medical robots, or medical assistants.<sup>12</sup> For example, a DT of a brain tumor patient undergoing surgery can be built, upon which AI agents can simulate the entire surgical procedure. This enables surgeons to plan the operation by assessing different entry points, angles, and depths, which can decrease the risk of damaging healthy brain tissue. Moreover, the capability of AI agents to orchestrate multiple DT models is important, as complex clinical tasks often require the development of more than one DT.<sup>55</sup>

The metaverse represents a collective virtual shared space created by converging virtually enhanced physical reality, augmented reality, and the internet.<sup>56</sup> It is a space where digital and physical worlds intersect and open new possibilities in various domains, including medicine.<sup>57</sup> This raises the possibility that the metaverse could represent a virtual space where healthcare providers and patients can interact with DTs in real-time, allowing for more collaborative and patient-centered care. 58 For example, doctors could use the metaverse to remotely monitor patients’ DTs and adjust their treatment plans based on realtime data. In addition, the metaverse could provide a platform for multidisciplinary teams of healthcare professionals to collaborate and share insights, leading to more informed and effective treatment decisions.<sup>59</sup> Implementing DTs within a metaverse could also facilitate patient engagement and education, empowering patients to take a more active role in their healthcare.<sup>60,6</sup> To build consistent digital models for physical objects in the metaverse, 62 generative algorithms showed attractive potential. Deep generative models, including the Generative Pre-trained Transformer,<sup>63</sup> DALL-E (released by OpenAI),<sup>64</sup> as well as the booming diffusion model,<sup>65</sup> have been used to create dynamic metaverse environments. Deep generative models have also been extensively used for de novo molecular designs, compound optimization and hit identification.<sup>66–68</sup>

## Challenges

Although deep learning models have played a key role in solving important problems in computational biology, they are faced with challenges such as interpretability and generalization. 39 The interpretability of AI is one of the key hurdles to building human trust in a medical DT model, because it requires AI to provide diagnostic or treatment evidence with high transparency and interpretability. Many approaches have been tested in this area. Saliency mapping has been used to demonstrate that networks learn patterns, which agrees with accepted pathological features for Alzheimer’s disease.<sup>69</sup> The visualization of convoluted neural network ensembles that classify estrogen receptors has also been used to provide interpretability to breast magnetic resonance imaging (MRI) predictions .<sup>70</sup> Generative discriminative machines<sup>71</sup> can handle confounding variables to increase confidence in predictions.<sup>71</sup> Other approaches include interactive learning, causal reasoning, counterfactual reasoning, and mental theory to construct interpretable AI models.<sup>72–75</sup>

Explainable AI is another challenge. If human intelligence is complemented by AI and sometimes even overruled, we must understand the AI decision-making process. Furthermore, integrating expert knowledge and clinical evidence to guide AI development remains challenging, resulting in some difficulty in revealing the underlying AI explanatory structures. In addition, the AI model in a medical DT platform requires high robustness and generalization when dealing with massive and multisource data. The robustness refers to the tolerance of the model to perturbations in the input data.<sup>76</sup> Models with poor robustness are easily misled by tiny and simple perturbations in the input.<sup>77,78</sup> Many methods for improving model robustness have been applied in the biomedical field, such as an adversarial attack algorithm in gastric cancer subtype analysis models.<sup>79–81</sup> Platforms for evaluating the robustness of an AI model have also been proposed.<sup>82</sup> The degradations in the performance of a model when evaluated on previously unseen data compared with data it has already seen is known as generalization. 83 Data augmentation using generative adversarial networks can generate a large amount of training data to solve the problems of insufficient data and uneven distribution.<sup>83,84</sup> Many generative adversarial networks have been proposed for data augmentation to improve the generalizability of AI models, including Cycle-GAN,<sup>85</sup> pix2pix GAN,<sup>86</sup> and Self-Attention GAN.<sup>87</sup>

The performance of AI systems is known to deteriorate on older tasks during training, which is called catastrophic forgetting. This is a particular issue in implementing medical DTs because continuous learning is necessary. Lifelong learning is a paradigm that allows continuous learning, and to retain prior experience with old tasks while learning new tasks.<sup>88,89</sup> Such approaches should be a part of medical DT platform so they can adapt to the real world. Lifelong learning has been explored in the processing and interpretation of medical images, 90 and elastic weight consolidation has been applied to learning normal brain structure and white matter lesion segmentation.<sup>91</sup> Reduction of catastrophic forgetting has also been successful in cardiac ultrasound view classification and pneumothorax detection.<sup>92</sup> It has also been used in dealing with modality and task transitions caused by changes in protocols, parameter settings, or different scanners in a clinical setting. 93 Research on improving the lifelong learning ability of models will focus on the following aspects: task transfer and adaptation, overcoming catastrophic forgetting, exploiting task similarity, task-agnostic learning, noise tolerance, and resource efficiency and sustainability. 94

## Computing power

DT platforms require tremendous computing power.<sup>95</sup> Quantum computing is well suited to large-scale data processing, information modeling process, and real-world and virtual world communication processes.<sup>96</sup> In addition, quantum imaging techniques, combined with quantum sensors and quantum dots, are likely to usher in a new era of medical imaging,<sup>97</sup> and it is expected that quantum MRI machines will produce extremely precise imaging, with the potential to visualize individual molecules.<sup>98</sup> Combined with AI, quantum computing can also be applied to interpret diagnostic images, identifying anomalies with greater precision than the human eye.<sup>99</sup>

Quantum sensors can also be applied to acquire multi-moda data, particularly in wearable devices, to allow for highly sensitive and accurate monitoring of a physical entity. Quantum dots can be used in conjunction with quantum computing to personalize drug design, potentially enabling tailor-made drugs for each patient, maximizing efficacy and minimizing adverse reactions.<sup>61</sup> Similar approaches can also be used to develop radiation plans to kill cancer cells without harming healthy cells. 100 In neurology, quantum computing can simulate complex neural networks, aiding in the understanding and treatment of neurological disorders. This can be applied with DTs of the brain to accurately model the behavior of neurons and synapses, leading to more informed treatment strategies and a better understanding of disorders like Alzheimer’s disease or Parkinson’s disease. Quantum computing and DTs can also be used to optimize hospital operations. Quantum algorithms can analyze patient flow, resource use, and staff scheduling datasets. This enables administrators to optimize the allocation of resources, decrease waiting times and enhance overall operational efficiency in healthcare facilities. Nevertheless, significant developments are needed before quantum methods can be scaled up for these approaches described above. Current challenges include the need for error correction, the stability of qubits, as well as the development of scalable quantum hardware.

## Accessibility to data

While acquiring data from a large population makes it possible to realize the application of medical DTs, the challenge of data security, privacy, and confidentiality are critical considerations. New rules and regulations prohibit institutions from exchanging medical data without patients’ approval, resulting in the occurrence of data silos. Therefore, creative methods are required to coordinate data retrieval while protecting privacy.<sup>101</sup> To address these challenges, federated learning (FL) is a promising technology to boost data collaboration across multiple centers rather than sharing raw data. FL sidesteps privacy barriers by allowing clients to update models locally and upload model parameters to the server until the global model gains stable results. 102 Federated multi-modal learning has been implemented in predicting future oxygen requirements of symptomatic patients with coronavirus disease 2019 (COVID-19).<sup>103</sup> Cross-silo FL is also an increasingly attractive solution for predicting heart disease hospitalizations through electronic health records,<sup>104</sup> while crossdevice FL has been used to handle continuous health data from wearable devices to deliver personalized health insights.<sup>105</sup> Swarm learning is another approach that builds a model independently on private data using blockchain technology.<sup>106,107</sup> This can track and mediate access to health and genomic records. Additional challenges to accessibility and privacy lie in data heterogeneity, safety, and model communication efficiency. Data heterogeneity can result in client shifts and degrade the convergence of predictive outputs.<sup>108</sup> In addition, inversion attacks can reconstruct images from model weights or gradient updates with impressive visual details. Poisoning attacks damage the training of global models by deliberately uploading malicious local models, requiring additional privacy-enhancing techniques.<sup>101</sup> Furthermore, convergence times for FL are limited to communication bandwidths, which affect communication delay times, necessitating the development of communication-efficient FL.<sup>109</sup>

Additionally, the privacy by design approach can enhance data security and privacy at the infrastructure level by implementing robust authentication and access control measures. This includes encrypting data to prevent unauthorized access, using secure protocols like HTTPS or VPNs to protect sensitive data during transmission, anonymizing or pseudonymizing sensitive information, keeping personally identifiable data locally, and establishing a robust system for regular anomaly detection and prevention. Adapting blockchain technology in a medical DT platform can also mitigate the problem of data tampering. The decentralized nature of blockchain technology provides transparency in consent management and allows patients to see who has access and for what purposes. 110 This will facilitate data audit and allow data changes to be traced. Moreover, selfexecuting agreements based on predefined rules and conditions called smart contracts can convert physical data governance and regulatory requirements into digital processes. Additionally, tokenization capabilities of blockchain technology can facilitate individual data ownership. In summary, addressing data security, privacy protection, and data ownership is crucial in designing and implementing medical DT technology. This protects sensitive healthcare information, prevents unauthorized access or data manipulation, and fosters trust among stakeholders.<sup>9,111</sup>

## Ethics

Several ethical issues related to the extensive collection of sensitive health information arise in any discussions of a medical DT. Therefore, the protection and governance of such collected data are among the top priorities. For example, a determined adversary can hack into a DT repository to potentially harm entire populations. The issue of multiple use of the collected data also needs to be properly addressed and governed, to alleviate the inevitable concern that accumulated sensitive data could be used for purposes other than informing healthcare decisions, such as research, commercialization, or surveillance.

The provision of informed consent will also be critical, particularly with regard to transparency about how the data will be used and who will have access to the data. While the benefits and risks of participating in medical DT projects can be clearly explained to patients in detail, informed consent for collecting individualized information from wearables is more difficult. Furthermore, the extent of multi-modal data involved in the meaningful implementation of medical DTs raises privacy issues and patient confidentiality. One major ethical hurdle is re-identification from anonymized data. This is a particular problem when highly parametrized models such as neural networks are used, as a significant fraction of the training data can be reconstructed from the trained neural network model.<sup>112</sup> Indeed, a recent systematic review found re-identification rates are high.<sup>113</sup>

Data acquired from medical DT platforms will be used to inform clinical decisions, many of which may be life altering. Where the burden of accountability lies is critically important regarding liability in case of errors or adverse outcomes. In addition, the accumulated data may contain unequal representations of certain demographic groups. This creates a void in the data for machine learning and affects the performance of the medical DT platform with respect to minority groups. The clinical decisions for patients in such groups, or those with a lower socioeconomic status, may therefore contain a certain degree of bias and inequality. Furthermore, it can be envisaged, at least initially, that medical DT technologies will be implemented in settings where the more affluent will benefit. This may exacerbate the inequality gap and bias. The result may be a disproportionate health improvement for high versus low socioeconomic status patients. Unless addressed, these concerns will severely dampen the enthusiasm for the widespread implementation of a medical DT platform.

One additional concern is data ownership. Currently, consent for data provision is received from the data producers, which has led to a digital economy built on centralized data owned by large tech corporations. This system has resulted in a scenario where the data creators (the patients or participants in research) have limited control and oversight of downstream processes. Indeed, tech companies routinely trade and sell personal data for profit. Therefore, in addition to the privacy, ownership, and security issues discussed above, there is also an economic and profit issue that complicates the ethics around medical DT initiatives. Therefore, a fundamentally different approach to a data management philosophy may be needed for medical DT applications. One bold approach may be to empower individuals with full data ownership. This means medical DT applications will provide the data creator the right to keep, sell, donate, or trade their personal data for research or drug discovery. This can be implemented using smart contracts with built-in economic compensation logic. Patients can be compensated when they choose to sell or trade their anonymized data based on their nuanced preference for privacy. Mechanisms to compensate individuals for their health data can also incentivize targeted health data collection for medical research and drug discovery. Such approaches can improve individual digital rights when AI and big data become indispensable components of modern medicine.

## POTENTIAL IMPLEMENTATIONS OF DTs IN MEDICINE

## Health and disease management

## Individualized homeostasis monitoring

The classification of experimentally or clinically defined normal or healthy states differs slightly in each individual and cannot be extrapolated to large populations.<sup>25</sup> Currently, treatment personalization relies on low-resolution data and a limited picture of the clinical history of a particular person. For example, there is not yet a clear understanding of a normal blood pressure. The reasons may be due to the relatively sparse blood pressure measurements and the lack of assessment of the impact of physiological and behavioral patterns in any individual.<sup>114</sup> Without a personalized definition of normal, it is difficult to detect deviations from normal that ultimately constitute the disease state. A medical DT can define normal in each individual through continuous feedback of information between the patient and their DT. Deviations from this normal state define disease, and treatments can be leveraged to predict intervention outcomes.

## Cancer management

Medical DTs can also realize the promise of precision oncology by integrating individual proteome and clinical data with population data.<sup>115</sup> Such models continuously learn from new data, as well as individual patient care decisions from physicians, and can be used for real-time adjustment of treatments. This is particularly important in cancer recurrence or drug resistance, and patients may require different surgical, chemotherapy, or radiation regimens depending on the innate resistance of their particular tumor. Medical DT platforms can predict the onset of resistance and offer alternative treatment regimens based on the genome of individual patient tumors. Chemotherapy regimens also can be personalized depending on the patient’s metabolism to mitigate toxic side effects. Such models have shown promise in predicting treatment responses in triple-negative breast cancer .<sup>116</sup> A medical DT platform can also be used to predict metastatic disease through structured, consecutive radiology reports.<sup>117,118</sup>

## Cardiovascular disease

Improved survival and quality of life in cardiovascular disease are achieved by effective acute care and guideline-based risk factor management strategies.<sup>119</sup> DTs can be created from traditional simulation models and precursor models at different scales to create real-time, cyber-physical systems to provide tailored therapies.<sup>14,120</sup> For example, an inverse analytic DT system can detect abdominal aortic aneurysm and its severity scores using neural networks.<sup>121,122</sup> The Siemens Digital Heart is used to evaluate the success of cardiac resynchronization therapy by implanting virtual electrodes.

## Immune responses

A medical DT platform can also play an essential role in autoimmune disorders and infectious diseases. This will require multimodal, granular, and integrated information at the molecular, cellular, tissue, organ, and body levels. Such platforms can be used to predict the rejection of transplanted organs and the potential responses to immunosuppressive agents. It will also be useful in infectious diseases, particularly during a pandemic, to identify individuals who are susceptible to certain infections or at risk of fatal cytokine storms. It can also be used to predict protective immune responses and immune memory as a result of vaccination.

## medical devices

The design of customized medical devices is a great challenge. Creating DTs of different anatomical structures in the body can simplify the design and implementation of customized medical devices. Dassault Syste\` mes, based in France, developed a model of the structure and function of the human heart using MRI and electrocardiograms. This Living Heart Project has an active collaborative research agreement with the U.S. Food and Drug Administration to evaluate the use of the model in the insertion, placement, and assessment of pacemaker leads, and other cardiac medical devices. Further work from this collaboration will use DT technologies to improve the efficiency of medical devices in clinical trials and leverage simulation data as a source of evidence.

## Surgery

Surgical interventions offer curative potential for many diseases without effective pharmacological treatment alternatives. However, the surgical procedure and some of the interventions given during the perioperative period may adversely affect patient outcomes. DTs can be very useful in the perioperative period for the planning and simulation of the surgery itself, as well as for predicting surgical outcomes.<sup>123</sup> A DT platform will also be beneficial for assessing the tolerance of surgery outcomes with respect to small human-induced variations during the surgical procedure, such as during complex heart surgeries like transcatheter aortic valve replacements. Digital orthopedics has generated a DT of the foot and ankle, allowing surgeons to simulate surgery results and optimize surgical planning.

## Hospital and nursing administration

Outside of the biological and clinical settings, DT technologies can impact the administration of large healthcare institutions. DT platforms created from electronic medical records and live physiological data from wearable devices can be leveraged to provide optimized and personalized medical and nursing services. The Verto Flow platform integrates patient data from various sources using AI algorithms, which healthcare professionals can use to optimize patient care. The ThoughtWire platform can simulate the health status of a patient, alerting doctors when a patient is likely to have a life-threatening complication, and offer suggestions based on predictions to mitigate the risks.<sup>124</sup> DTs of entire hospital workflows are also being explored by GE and Siemens Healthcare, to optimize surgery schedules and simplify staffing requirements. This can improve overall hospital efficiency and shorten patient waiting times. Project BreathEasy, developed by OnScale, is a DT-inspired lung model to assist clinicians in the prediction of the ventilation requirements in COVID-19 patients. This is particularly important in low-resource regions, where ventilators are in short supply.

## Synthetic biology circuits

The use of nature in engineering and industry holds immense potential, with synthetic biology emerging as a rapidly growing field with significant economic prospects. Advances in DNA synthesis and sequencing technology have greatly decreased the costs of constructing synthetic DNA genomes. Incorporating advanced microfluidics allows for the creation of cell-free biological components. Indeed, synthetic biology closely aligns with the original concept of DTs. For example, the development of an artificial human heart required substantial DT input. 125 Incorporating DT technology in synthetic biology could create autonomic biological modules for applications like smart organs, drug production, or renewable energy. These biological modules can communicate with virtual entities on the medical DT platform using synthetic genetic circuits and optogenetic tools. The potential for biological computers suggests a future where control of the virtual entity is integrated within the physical entity. Advances in cellular state estimation and control methods can lead to intelligent

designs for biological components, furthering the discovery of new technologies in the control and integration of cellular processes.

## A MEDICAL DT: REQUIREMENTS TOWARD TRUE PERSONALIZED MEDICINE

In an era marked by groundbreaking technological advancements, healthcare is on the brink of a revolutionary transformation with the integration of DT technologies. This paradigm shift toward personalized, data-driven healthcare is encapsulated in a medical DT platform characterized by five key hallmarks (Figure 3).

## Hallmarks of a medical DT

## Representative data repository as a metaverse

At the core of a medical DT platform lies the concept of a metaverse, a virtual space of large-scale and high-fidelity digital models and entities that can be used to adjust treatment, monitor response, and track lifestyle modifications (Figure 4). This metaverse should also be where patient-specific DTs and their multi-modal biological omics and medical data coexist, and enables the seamless sharing and interaction of healthcare data. It will also be a dynamic ecosystem that integrates a patient’s comprehensive and multi-modal input to find a matching virtual counterpart and offer individualized treatment and prevention recommendations. The recommendation can be further personalized to the patient based on virtual profile latent-space prototyping if necessary. 126

## Real-time monitoring of the physical entity

The second hallmark of a medical DT platform is the real-time monitoring of physical entities. Patient-specific avatars within the metaverse closely mirror patients’ real-world health conditions. They can monitor vital signs, physiological parameters, and treatment progress. This real-time monitoring ensures timely interventions and immediate response to anomalies and empowers patients with continuous access to their health data.

## Reliable predictions by embodied AI agents

Embodied AI agents are the third hallmark of a medical DT platform. They are the digital brains of the platform, constantly analyzing vast amounts of data to offer reliable predictions and insights. These AI agents draw from comprehensive datasets within the metaverse, including historical health data, treatment outcomes, and patient-specific parameters. By simulating different scenarios, they can predict how a patient’s health will evolve, the effectiveness of potential treatments, and the probability of developing specific conditions. This proactive approach transforms healthcare from reactive to predictive, enabling early intervention and optimized treatment strategies.

## Secure data access

The fourth hallmark of a medical DT platform is a robust emphasis on secure data access, where patient data are protected with the highest security and encryption standards. Patients have control over who can access their data, and healthcare providers are granted secure, role-based access to relevant patient information. This secure data access safeguards patient privacy and complies with stringent data protection regulations.

## Ethical issues

Ethics is the fifth and perhaps the most vital hallmark of a medical DT platform. It upholds the principle that every healthcare advancement must align with patients’ best interests. This platform adheres to the highest ethical data use, research, and care delivery standards. It ensures that patient consent is always obtained and patient rights are respected. The ethical commitment extends to using healthcare data to improve patient care and the broader healthcare community while maintaining transparency and trust.

## Development of a medical DT platform

The medical DT platform can be realized using a four-stage development roadmap based on increasing functionality and complexity (Figure 5).

## Stage 1: Static twins

The simplest DT model starts with a patient model template based on retrospective data and a continuous learning process. The static twin is a traditional simulation and modeling exercise, where analysis is primarily performed offline and characterized by hypothesis-driven mathematical modeling. The static twin is obtained by modeling the state of a physical system through data collected from sensors.<sup>127</sup> Static twins can, therefore, be considered as data-driven mathematical models of patients. One example of static twins is the HeartNavigator developed by Philips. 128

## Stage 2: Progressive twins

The next step in the evolution of the DT platform should incorporate observational data to represent the patient’s current state and reliably forecast future state transitions. It will need existing techniques for simulation, model inference, data assimilation, and high-performance computing to build and test real-time, dynamic models on relatively large scales. Progressive twins integrate temporal or progressive information to construct a dynamic statistical machine learning model, which reflects the evolution of the physical entity and reliably forecasts future state transitions. Progressive twins are, therefore, in silico representations that dynamically reflect molecular, physiological, and disease states across time (e.g., aging). An example of progressive twins is the development of three-dimensional brain organoid cell culture models to recapitulate various aspects of human brain physiology in vitro and replicate basic disease processes of Alzheimer’s disease, amyotrophic lateral sclerosis, and microcephaly. 129

## Stage 3: Operational twins

One of the critical features of the DT concept is the physical-tovirtual connection. Operational twins are real-time, cyber-physical systems that use a continuous connection to monitor state changes in the physical environment. Therefore, operational twins represent a real-time interaction between the physical and virtual entities in a closed loop. For example, an automated insulin injector can be built where changes in the DT of the patient’s blood (data from glucose monitor) can be continuously monitored to determine accurate insulin dose injections throughout the day instead of relying on a fixed injection schedule.

## Stage 4: Autonomous twins

In the ultimate stage of the DT platform evolution, known as the autonomous twins, the digital and physical worlds are merged, representing the pinnacle of physical-virtual co-existence. The self-sustaining virtual worlds operate independently while interacting seamlessly with the physical world. This integration can create a metaverse populated with countless autonomous, high-resolution virtual entities. For example, an autonomic DT brain could be developed, building on in silico representations and evolving autonomously. This can dynamically reflect the biophysical information of an actual brain over time, enabling effective enhancement interventions. Autonomous twins, combined with advanced virtual reality platforms, can also revolutionize surgical practice by providing realistic performance feedback on simulated procedures tailored to each patient.<sup>123</sup> Autonomous twins can offer valuable insights and guidance for realworld decision-making. The ultimate form of autonomous twins could enable the realization of precision medicine by accelerating the discovery of medical phenomena and disease processes, shortening the timeline for drug discovery, improving surgical outcomes via virtual operations, and simulating disease progression statistics.

## Applications of a medical DT

## Creation of personalized treatment plans

A medical DT platform can use a cancer patient’s medical history, family history, genetic information, and lifestyle factors (diet, exercise, and exposure to environmental toxins) to create an AI agent. This AI agent, using an LLM, captures the patient’s unique physiological responses and medical conditions,<sup>46</sup> leveraging external tools for diagnosis and treatment.<sup>130</sup> It can perform self-diagnosis by accessing the latest medical research, clinical trials, and treatments.<sup>43</sup> It can consider various treatment options, such as chemotherapy, radiotherapy, immunotherapy, and targeted therapy and assess their potential effectiveness. The AI agent can also analyze the patient’s genetic data to identify mutations or biomarkers that could be indications for or contraindications to specific therapies. The AI agent interacts with the patient and the healthcare provider to address concerns promptly. As new data and feedback are received, the platform uses reinforcement learning to refine its models,<sup>131</sup> improving the accuracy and effectiveness of personalized treatment plans over time. Once developed, this agent can be easily customized for other patients based on their personal data.

## Remote patient monitoring

Patients with chronic illnesses, such as hypertension or diabetes, can be equipped with a wearable device that continuously streams their vital signs and health data to their virtual counterparts within the metaverse. The embodied AI agent can analyze the incoming data to detect any irregularities or signs of deterioration. If a critical situation arises, the system can alert the patient and/or healthcare provider. It can even initiate a predefined emergency response. This proactive approach to remote monitoring allows patients to maintain their health from the comfort of their homes or anywhere while receiving immediate interventions when necessary.

## Virtual clinical trials

Clinical trials are essential for testing new medications and treatments. A medical DT can revolutionize clinical trials by simulating patient responses in the metaverse. Researchers can use the DT platform to represent virtual patients with specific conditions and characteristics. These virtual patients are subjected to various treatment regimens, minimizing the risks and ethical concerns associated with actual patients. The embodied AI agents within the DT platform can analyze the treatment outcomes, providing valuable insights into the potential efficacy and safety of the treatments. This approach expedites the drug development process, reduces costs, and accelerates the availability of new therapies to actual patients.

## Hospital administration

Integrating DT platforms in hospital administration can substantially improve management of healthcare facilities. These technologies create virtual representations of hospital infrastructure, allowing administrators to monitor and manage operations in real time. For instance, a virtual operating room can provide insights into equipment use, maintenance needs and staff workflows, optimizing space layout and resource use. Clinical workflows and administrative processes can be analyzed and optimized within the virtual environment. Nursing administrators can simulate scenarios to identify bottlenecks and streamline workflows. Virtual entities of nursing staff offer real-time insights into availability, skills, and workload. The DT platform can also simulate patient flows to optimize bed management and predict congestion points. Additionally, the metaverse serves as a training ground for medical staff, allowing them to practice critical care, patient interactions, and new technologies in a risk-free environment.

## CONCLUSIONS

The DT concept has proven invaluable in industrial applications, from manufacturing to the safe operation of complex systems. Its potential in developing in vitro and in vivo research models is also evident in biomedical research. However, its most transformative application lies in clinical medicine, where DT technologies could realize personalized medicine. By combining highthroughput genetic and molecular approaches, single-cell and whole-genome sequencing, big data, cloud-based electronic medical records, and AI, DTs can deliver modern healthcare.

Beyond offering personalized treatment regimens, DT technologies can monitor and predict adverse drug reactions or interactions. Their greatest impact, however, will be in the day-to-day health monitoring of individuals. The ability to precisely predict health perturbations and provide mitigation suggestions will advance the detection and diagnosis of chronic, non-communicable diseases.

Despite the potential, implementation faces obstacles such as privacy issues, data security, and the risk of malicious attacks. Additionally, the accessibility of AI findings and interpretations needs improvement. Nevertheless, the Consortium believes the transformative potential of DTs in healthcare is too significant to be hindered by these challenges. We urge national scientific policymakers and funding bodies to increase resources in this crucial area of research.

## CONSORTIA

Members of the International Consortium of Digital Twins in Medicine include Daniel Baptista-Hon, Stephan Beck, George Church, Wei Gao, Yuanxu Gao, Shengwei Jin, Xiao Liu, Xiaohong Liu, Alexandre Loupy, Eric Oermann, Jia Qu, Pranav Rajpurkar, Zhuo Sun, Joseph Wu, Sheng Xu, Yun Yin, Jian Zhang, Kang Zhang, Hong-Yu Zhou, Marinka Zitnik, Jennifer Zhu Scott, and James Zou.

## AUTHOR CONTRIBUTIONS

Conceptualization: K.Z. and S.B.; writing – original draft: K.Z., H.Y.Z., D.B.H., Y.X.G., X.H.L., and J.W.; writing – review & editing, K.Z., H.Y.Z., D.B.H., Y.X.G., X.H.L., E.O., A.L., S.X., S.J., J.Z., Z.S., Y.Y., R.M.R., S.B., J.W., and J.Q.

## DECLARATION OF INTERESTS

The authors declare no competing interests.

## REFERENCES

1. Emmert-Streib, F. (2023). Defining a Digital Twin: A Data Science-Based Unification. Mach. Learn. Knowl. Extr. (2019). 5, 1036–1054. https://doi. org/10.3390/make5030054.

2. Marr, B. (2016). Why everyone must get ready for the 4th industrial revolution. Forbes Tech 5. https://www.forbes.com/sites/bernardmarr/2016/ 04/05/why-everyone-must-get-ready-for-4th-industrial-revolution/?sh= 246d9da63f90.

3. Tao, F., and Qi, Q. (2019). Make more digital twins. Nature 573, 490–491. https://doi.org/10.1038/d41586-019-02849-1.

4. Zhang, A., Wu, Z., Wu, E., Wu, M., Snyder, M.P., Zou, J., and Wu, J.C. (2023). Leveraging physiology and artificial intelligence to deliver advancements in health care. Physiol. Rev. 103, 2423–2450. https://doi. org/10.1152/physrev.00033.2022.

5. Grieves, M., and Vickers, J. (2017). Digital twin: Mitigating unpredictable, undesirable emergent behavior in complex systems. In Transdisciplinary perspectives on complex systems (Springer), pp. 85–113.

6. Emmert-Streib, F., and Yli-Harja, O. (2022). What Is a Digital Twin? Experimental Design for a Data-Centric Machine Learning Perspective in Health. Int. J. Mol. Sci. 23, 13149. https://doi.org/10.3390 ijms232113149.

7. Rajpurkar, P., Chen, E., Banerjee, O., and Topol, E.J. (2022). AI in health and medicine. Nat. Med. 28, 31–38. https://doi.org/10.1038/s41591- 021-01614-0.

8. Topol, E.J. (2019). High-performance medicine: the convergence of human and artificial intelligence. Nat. Med. 25, 44–56. https://doi.org/10. 1038/s41591-018-0300-7.

9. Rhee, H., Miner, S., Sterling, M., Halterman, J.S., and Fairbanks, E. (2014). The development of an automated device for asthma monitoring for adolescents: methodologic approach and user acceptability. JMIR Mhealth Uhealth 2, e27. https://doi.org/10.2196/mhealth.3118.

10. Potter, D., Brothers, R., Kolacevski, A., Koskimaki, J.E., McNutt, A., Miller, R.S., Nagda, J., Nair, A., Rubinstein, W.S., Stewart, A.K., et al. (2020). Development of CancerLinQ, a Health Information Learning Platform From Multiple Electronic Health Record Systems to Support Improved Quality of Care. JCO Clin. Cancer Inform. 4, 929–937. https://doi.org/10.1200/CCI.20.00064.

11. San, O. (2021). The digital twin revolution. Nat. Comput. Sci. 1, 307–308. https://doi.org/10.1038/s43588-021-00077-0.

12. Kamel Boulos, M.N., and Zhang, P. (2021). Digital Twins: From Personalised Medicine to Precision Public Health. J. Personalized Med. 11, 745. https://doi.org/10.3390/jpm11080745.

13. Walsh, J.R., Smith, A.M., Pouliot, Y., Li-Bland, D., Loukianov, A., and Fisher, C.K.; Consortium, f.t.M.S.O.A. (2020). Generating Digital Twins with Multiple Sclerosis Using Probabilistic Neural Networks. Preprint at arXiv. https://doi.org/10.48550/arXiv.2002.02779.

14. Coorey, G., Figtree, G.A., Fletcher, D.F., and Redfern, J. (2021). The health digital twin: advancing precision cardiovascular medicine. Nat. Rev. Cardiol. 18, 803–804. https://doi.org/10.1038/s41569-021-00630-4.

15. Fisher, C.K., Smith, A.M., Walsh, J.R., and Coalition Against Major, D.; Abbott, A.f.A.R.A.s.A.A.s.F.o.A.A.P.L.P.B.-M.S.C.C.P.I.C.F.I.E.L.; Company, F.H.-L.R.L.F.R.I.G.I.G.J.; Johnson, N.H.C.N.P.C.P.s.A.N.P.s.D.F. P.I.s.-a.C.O.C.D.I.S.C.E.M.I. (2019). Machine learning for comprehensive forecasting of Alzheimer’s Disease progression. Sci. Rep. 9, 13622. https://doi.org/10.1038/s41598-019-49656-2.

16. Masison, J., Beezley, J., Mei, Y., Ribeiro, H., Knapp, A.C., Sordo Vieira, L., Adhikari, B., Scindia, Y., Grauer, M., Helba, B., et al. (2021). A modular computational framework for medical digital twins. Proc. Natl. Acad. Sci. USA 118, e2024287118. https://doi.org/10.1073/pnas.2024287118.

17. All of Us Research Program, I., Denny, J.C., Rutter, J.L., Goldstein, D.B., Philippakis, A., Smoller, J.W., Jenkins, G., and Dishman, E. (2019). The "All of Us" Research Program. N. Engl. J. Med. 381, 668–676. https:// doi.org/10.1056/NEJMsr1809937.

18. Subramanian, I., Verma, S., Kumar, S., Jere, A., and Anamika, K. (2020). Multi-omics data integration, interpretation, and its application. Bioinf. Biol. Insights 14, 1177932219899051. https://doi.org/10.1177/ 1177932219899051.

19. Dura˜ o, L.F., Haag, S., Anderl, R., Schutzer, K., and Zancul, E. (2018). Dig-€ ital twin requirements in the context of industry 4.0. In Product Lifecycle Management to Support Industry 4. 0., 15 (Springer International Publishing), pp. 204–214.

20. Yoo, J.-Y., Oh, S., Shalish, W., Maeng, W.-Y., Cerier, E., Jeanne, E., Chung, M.-K., Lv, S., Wu, Y., Yoo, S., et al. (2023). Wireless broadband acousto-mechanical sensing system for continuous physiological monitoring. Nat. Med. 29, 3137–3148. https://doi.org/10.1038/s41591-023- 02637-5.

21. Wang, H., Chen, Y.S., and Zhao, Y. (2021). A Wearable Metasurface for High Efficiency, Free-Positioning Omnidirectional Wireless Power Transfer. New J. Phys. 23, 125003. https://doi.org/10.1088/1367-2630/ ac304a.

22. Ginsburg, G.S., Picard, R.W., and Friend, S.H. (2024). Key Issues as Wearable Digital Health Technologies Enter Clinical Care. N. Engl. J. Med. 390, 1118–1127. https://doi.org/10.1056/NEJMra2307160.

23. Wang, J., Gao, Y., Wang, F., Zeng, S., Li, J., Miao, H., Wang, T., Zeng, J., Baptista-Hon, D., Monteiro, O., et al. (2024). Accurate estimation of biological age and its application in disease prediction using a multimodal image Transformer system. Proc. Natl. Acad. Sci. USA 121, e2308812120. https://doi.org/10.1073/pnas.2308812120.

24. Xia, K., and Wang, J. (2023). Recent advances of Transformers in medica image analysis: A comprehensive review. MedComm – Future Medicine 2, e38. https://doi.org/10.1002/mef2.38.

25. Bruynseels, K., Santoni de Sio, F., and van den Hoven, J. (2018). Digital Twins in Health Care: Ethical Implications of an Emerging Engineering Paradigm. Front. Genet. 9, 31. https://doi.org/10.3389/fgene. 2018.00031.

26. Pang, J., Huang, Y., Xie, Z., Li, J., and Cai, Z. (2021). Collaborative city digital twin for the COVID-19 pandemic: A federated learning solution. Tsinghua Sci. Technol. 26, 759–771. https://doi.org/10.26599/TST. 2021.9010026.

27. Boehm, K.M., Khosravi, P., Vanguri, R., Gao, J., and Shah, S.P. (2022). Harnessing multi-modal data integration to advance precision oncology. Nat. Rev. Cancer 22, 114–126. https://doi.org/10.1038/s41568-021- 00408-3.

28. Zhou, H.Y., Yu, Y., Wang, C., Zhang, S., Gao, Y., Pan, J., Shao, J., Lu, G., Zhang, K., and Li, W. (2023). A transformer-based representationlearning model with unified processing of multi-modal input for clinical diagnostics. Nat. Biomed. Eng. 7, 743–755. https://doi.org/10.1038/ s41551-023-01045-x.

29. Wang, C., Ma, J., Shao, J., Zhang, S., Li, J., Yan, J., Zhao, Z., Bai, C., Yu, Y., and Li, W. (2022). Non-Invasive Measurement Using Deep Learning Algorithm Based on Multi-Source Features Fusion to Predict PD-L1 Expression and Survival in NSCLC. Front. Immunol. 13, 828560. https://doi.org/10.3389/fimmu.2022.828560.

30. Shao, J., Ma, J., Zhang, S., Li, J., Dai, H., Liang, S., Yu, Y., Li, W., and Wang, C. (2022). Radiogenomic System for Non-Invasive Identification of Multiple Actionable Mutations and PD-L1 Expression in Non-Small Cell Lung Cancer Based on CT Images. Cancers 14, 4823. https://doi. org/10.3390/cancers14194823.

31. Tiu, E., Talius, E., Patel, P., Langlotz, C.P., Ng, A.Y., and Rajpurkar, P. (2022). Expert-level detection of pathologies from unannotated chest X-ray images via self-supervised learning. Nat. Biomed. Eng. 6, 1399– 1406. https://doi.org/10.1038/s41551-022-00936-9.

32. Zhou, H.-Y., Chen, X., Zhang, Y., Luo, R., Wang, L., and Yu, Y. (2022). Generalized radiograph representation learning via cross-supervision between images and free-text radiology reports. Nat. Mach. Intell. 4, 32–40. https://doi.org/10.1038/s42256-021-00425-9.

33. Zhang, K., Liu, X., Shen, J., Li, Z., Sang, Y., Wu, X., Zha, Y., Liang, W., Wang, C., Wang, K., et al. (2020). Clinically Applicable AI System for Accurate Diagnosis, Quantitative Measurements, and Prognosis of COVID-19 Pneumonia Using Computed Tomography. Cell 181, 1423– 1433.e11. https://doi.org/10.1016/j.cell.2020.04.045.

34. Hernandez-Boussard, T., Macklin, P., Greenspan, E.J., Gryshuk, A.L., Stahlberg, E., Syeda-Mahmood, T., and Shmulevich, I. (2021). Digital twins for predictive oncology will be a paradigm shift for precision cancer care. Nat. Med. 27, 2065–2066. https://doi.org/10.1038/s41591-021- 01558-5.

35. Bjornsson, B., Borrebaeck, C., Elander, N., Gasslander, T., Gawel, D.R., Gustafsson, M., Jornsten, R., Lee, E.J., Li, X., Lilja, S., et al. (2019). Digital twins to personalize medicine. Genome Med. 12, 4. https://doi.org/10. 1186/s13073-019-0701-3.

36. Wang, D.Q., Feng, L.Y., Ye, J.G., Zou, J.G., and Zheng, Y.F. (2023). Accelerating the integration of ChatGPT and other large-scale AI models

into biomedical research and healthcare. MedComm – Future Medicine 2, e43. https://doi.org/10.1002/mef2.43.

37. Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J.D., Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., and Askell, A. (2020). Language models are few-shot learners. Adv. Neural Inf. Process. Syst. 33, 1877– 1901. https://doi.org/10.48550/arXiv.2005.14165.

38. Chowdhery, A., Narang, S., Devlin, J., Bosma, M., Mishra, G., Roberts, A., Barham, P., Chung, H.W., Sutton, C., and Gehrmann, S. (2022). Palm: Scaling language modeling with pathways. Preprint at arXiv. https://doi.org/10.48550/arXiv.2204.02311.

39. Acosta, J.N., Falcone, G.J., Rajpurkar, P., and Topol, E.J. (2022). Multimodal biomedical AI. Nat. Med. 28, 1773–1784. https://doi.org/10. 1038/s41591-022-01981-2.

40. Huang, Z., Bianchi, F., Yuksekgonul, M., Montine, T.J., and Zou, J. (2023). A visual–language foundation model for pathology image analysis using medical Twitter. Nat. Med. 29, 2307–2316. https://doi.org/10.1038/ s41591-023-02504-3.

41. Bommasani, R., Hudson, D.A., Adeli, E., Altman, R., Arora, S., von Arx, S., Bernstein, M.S., Bohg, J., Bosselut, A., Brunskill, E., et al. (2022). On the Opportunities and Risks of Foundation Models. Preprint at arXiv. https:// doi.org/10.48550/arXiv.2108.07258.

42. Thirunavukarasu, A.J., Ting, D.S.J., Elangovan, K., Gutierrez, L., Tan, T.F., and Ting, D.S.W. (2023). Large language models in medicine. Nat. Med. 29, 1930–1940. https://doi.org/10.1038/s41591-023-02448-8.

43. Singhal, K., Azizi, S., Tu, T., Mahdavi, S.S., Wei, J., Chung, H.W., Scales, N., Tanwani, A., Cole-Lewis, H., Pfohl, S., et al. (2023). Large language models encode clinical knowledge. Nature 620, 172–180. https://doi. org/10.1038/s41586-023-06291-2.

44. Jiang, L.Y., Liu, X.C., Nejatian, N.P., Nasir-Moin, M., Wang, D., Abidin, A., Eaton, K., Riina, H.A., Laufer, I., Punjabi, P., et al. (2023). Health systemscale language models are all-purpose prediction engines. Nature 619, 357–362. https://doi.org/10.1038/s41586-023-06160-y.

45. Kosinski, M. (2023). Theory of mind may have spontaneously emerged in large language models. Preprint at arXiv. https://doi.org/10.48550/arXiv. 2302.02083.

46. Joon, J., Carrie, M., Liang, P., and Michael. (2023). Generative Agents: Interactive Simulacra of Human Behavior. Preprint at arXiv. https://doi. org/10.48550/arXiv.2304.03442.

47. George, A.S., and George, A.H. (2023). A review of ChatGPT AI’s impact on several business sectors. Partners Universal International Innovation Journal 1, 9–23.

48. Barricelli, B.R., Casiraghi, E., and Fogli, D. (2019). A survey on digital twin: Definitions, characteristics, applications, and design implications. IEEE Access 7, 167653–167671. https://doi.org/10.1109/ACCESS.2019. 2953499.

49. Duan, J., Yu, S., Tan, H.L., Zhu, H., and Tan, C. (2022). A survey of embodied ai: From simulators to research tasks. IEEE Trans. Emerg. Top. Comput. Intell. 6, 230–244. https://doi.org/10.1109/TETCI.2022. 3141105.

50. Fiske, A., Henningsen, P., and Buyx, A. (2019). Your Robot Therapist Will See You Now: Ethical Implications of Embodied Artificial Intelligence in Psychiatry, Psychology, and Psychotherapy. J. Med. Internet Res. 21, e13216. https://doi.org/10.2196/13216.

51. Yip, M., Salcudean, S., Goldberg, K., Althoefer, K., Menciassi, A., Opfermann, J.D., Krieger, A., Swaminathan, K., Walsh, C.J., Huang, H., and Lee, I.C. (2023). Artificial intelligence meets medical robotics. Science 381, 141–146. https://doi.org/10.1126/science.adj3312.

52. Wood, L.J., Zaraki, A., Robins, B., and Dautenhahn, K. (2021). Developing kaspar: a humanoid robot for children with autism. Int. J. Soc. Robot. 13, 491–508. https://doi.org/10.1007/s12369-019-00563-6.

53. Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., et al. (2024). A survey on large language model based autonomous agents. Front. Comput. Sci. 18, 186345. https://doi. org/10.1007/s11704-024-40231-1.

54. Croatti, A., Gabellini, M., Montagna, S., and Ricci, A. (2020). On the integration of agents and digital twins in healthcare. J. Med. Syst. 44, 161–168. https://doi.org/10.1007/s10916-020-01623-5.

55. Wu, W.-T., Li, Y.-J., Feng, A.-Z., Li, L., Huang, T., Xu, A.-D., and Lyu, J. (2021). Data mining in clinical big data: the frequently used databases, steps, and methodological models. Mil. Med. Res. 8, 44. https://doi. org/10.1186/s40779-021-00338-z.

56. Venkatesan, M., Mohan, H., Ryan, J.R., Schurch, C.M., Nolan, G.P., Frakes, D.H., and Coskun, A.F. (2021). Virtual and augmented reality for biomedical applications. Cell Rep. Med. 2, 100348. https://doi.org 10.1016/j.xcrm.2021.100348.

57. Zhang, G.H., Yuan, T.H., Yue, Z.S., Wang, L., and Dou, G.R. (2022). The presence of diabetic retinopathy closely associated with the progression of non-alcoholic fatty liver disease: A meta-analysis of observational studies. Front. Mol. Biosci. 9, 1019899. https://doi.org/10.3389/fmolb. 2022.1019899.

58. Hassani, H., Huang, X., and Macfeely, S. (2022). Impactful Digital Twin in the Healthcare Revolution. Big Data Cogn. Comput. 6, 83. https://doi. org/10.3390/bdcc6030083.

59. Yang, D., Zhou, J., Chen, R., Song, Y., Song, Z., Zhang, X., Wang, Q., Wang, K., Zhou, C., Sun, J., et al. (2022). Expert consensus on the metaverse in medicine. Clinical eHealth 5, 1–9. https://doi.org/10.1016/j.ceh. 2022.02.001.

60. Chengoden, R., Victor, N., Huynh-The, T., Yenduri, G., Jhaveri, R.H., Alazab, M., Bhattacharya, S., Hegde, P., Maddikunta, P.K.R., and Gadekallu, T.R. (2023). Metaverse for Healthcare: A Survey on Potential Applications, Challenges and Future Directions. IEEE Access 11, 12765–12795. https://doi.org/10.1109/access.2023.3241628.

61. Emani, P.S., Warrell, J., Anticevic, A., Bekiranov, S., Gandal, M., McConnell, M.J., Sapiro, G., Aspuru-Guzik, A., Baker, J.T., Bastiani, M., et al. (2021). Quantum computing at the frontiers of biological sciences. Nat. Methods 18, 701–709. https://doi.org/10.1038/s41592-020-01004-3.

62. Niraula, D., Jamaluddin, J., Matuszak, M.M., Haken, R.K.T., and Naqa, I.E. (2021). Quantum deep reinforcement learning for clinical decision support in oncology: application to adaptive radiotherapy. Sci. Rep. 11, 23545. https://doi.org/10.1038/s41598-021-02910-y.

63. Floridi, L., and Chiriatti, M. (2020). GPT-3: Its Nature, Scope, Limits, and Consequences. Minds Mach. 30, 681–694. https://doi.org/10.1007/ s11023-020-09548-1.

64. Ramesh, A., Dhariwal, P., Nichol, A., Chu, C., and Chen, M. (2022). Hierarchical Text-Conditional Image Generation with CLIP Latents. Preprint at arXiv. https://doi.org/10.48550/arXiv.2204.06125.

65. Ho, J., Jain, A., and Abbeel, P. (2020). Denoising diffusion probabilistic models. Preprint at arXiv. https://doi.org/10.48550/arXiv.2006.11239.

66. Butler, K.T., Davies, D.W., Cartwright, H., Isayev, O., and Walsh, A. (2018). Machine learning for molecular and materials science. Nature 559, 547–555. https://doi.org/10.1038/s41586-018-0337-2.

67. Elton, D.C., Boukouvalas, Z., Fuge, M.D., and Chung, P.W. (2019). Deep learning for molecular design—a review of the state of the art. Preprint at arXiv. https://doi.org/10.48550/arXiv.1903.04388.

68. Sanchez-Lengeling, B., and Aspuru-Guzik, A. (2018). Inverse molecular design using machine learning: Generative models for matter engineering. Science 361, 360–365. https://doi.org/10.1126/science.aat2663.

69. Tang, Z., Chuang, K.V., DeCarli, C., Jin, L.W., Beckett, L., Keiser, M.J., and Dugger, B.N. (2019). Interpretable classification of Alzheimer’s disease pathologies with a convolutional neural network pipeline. Nat. Commun. 10, 2173. https://doi.org/10.1038/s41467-019-10212-1.

70. Papanastasopoulos, Z., Samala, R.K., Chan, H.-P., Hadjiiski, L.M., Paramagul, C., Helvie, M.A., and Neal, C.H. (2020). Explainable AI for medical imaging: deep-learning CNN ensemble for classification of estrogen re ceptor status from breast MRI. Medical imaging 2020: Computer-aided diagnosis 11314, 228–235. SPIE.

71. Varol, E., Sotiras, A., Zeng, K., and Davatzikos, C. (2018). Generative discriminative models for multivariate inference and statistical mapping in medical imaging. In Medical Image Computing and Computer Assisted

Intervention –. MICCAI 2018, 11 (Springer International Publishing), pp. 540–548.

72. Schramowski, P., Stammer, W., Teso, S., Brugger, A., Herbert, F., Shao, X., Luigs, H.-G., Mahlein, A.-K., and Kersting, K. (2020). Making deep neural networks right for the right scientific reasons by interacting with their explanations. Nat. Mach. Intell. 2, 476–486. https://doi.org/10. 1038/s42256-020-0212-3.

73. Barnett, A.J., Schwartz, F.R., Tao, C., Chen, C., Ren, Y., Lo, J.Y., and Rudin, C. (2021). A case-based interpretable deep learning model for classification of mass lesions in digital mammography. Nat. Mach. Intell. 3, 1061–1070. https://doi.org/10.1038/s42256-021-00423-x.

74. Prosperi, M., Guo, Y., Sperrin, M., Koopman, J.S., Min, J.S., He, X., Rich, S., Wang, M., Buchan, I.E., and Bian, J. (2020). Causal inference and counterfactual prediction in machine learning for actionable healthcare. Nat. Mach. Intell. 2, 369–375. https://doi.org/10.1038 s42256-020-0197-y.

75. Akula, A.R., Wang, K., Liu, C., Saba-Sadiya, S., Lu, H., Todorovic, S., Chai, J., and Zhu, S.C. (2022). CX-ToM: Counterfactual explanations with theory-of-mind for enhancing human trust in image recognition models. iScience 25, 103581. https://doi.org/10.1016/j.isci.2021. 103581.

76. Goodfellow, I.J., Shlens, J., and Szegedy, C.J.C. (2014). Explaining and Harnessing Adversarial Examples. Preprint at arXiv. https://doi.org/10. 48550/arXiv.1412.6572.

77. Kurakin, A., Goodfellow, I.J., and Bengio, S. (2016). Adversarial examples in the physical world. Preprint at arXiv. https://doi.org/10.48550/arXiv. 1607.02533.

78. Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I.J., and Fergus, R.J.C. (2013). Intriguing properties of neural networks. Preprint at arXiv. https://doi.org/10.48550/arXiv.1312.6199.

79. Madry, A., Makelov, A., Schmidt, L., Tsipras, D., and Vladu, A. (2017). Towards deep learning models resistant to adversarial attacks. Preprint at arXiv. https://doi.org/10.48550/arXiv.1706.06083.

80. Ghaffari Laleh, N., Truhn, D., Veldhuizen, G.P., Han, T., van Treeck, M., Buelow, R.D., Langer, R., Dislich, B., Boor, P., Schulz, V., and Kather, J.N. (2022). Adversarial attacks and adversarial robustness in computational pathology. Nat. Commun. 13, 5711. https://doi.org/10.1038/ s41467-022-33266-0.

81. Han, T., Nebelung, S., Pedersoli, F., Zimmermann, M., Schulze-Hagen, M., Ho, M., Haarburger, C., Kiessling, F., Kuhl, C., Schulz, V., and Truhn, D. (2021). Advancing diagnostic performance and clinical usability of neural networks via adversarial training and dual batch normalization. Nat. Commun. 12, 4315. https://doi.org/10.1038/s41467-021-24464-3.

82. Dong, Y., Fu, Q.A., Yang, X., Pang, T., Su, H., Xiao, Z., and Zhu, J. (2020). Benchmarking adversarial robustness on image classification. In In proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 321–331.

83. Zhang, C., Bengio, S., Hardt, M., Recht, B., and Vinyals, O. (2021). Understanding deep learning (still) requires rethinking generalization. Preprint at arXiv. https://doi.org/10.48550/arXiv.1611.03530.

84. Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., and Bengio, Y. (2020). Generative adversarial networks. Preprint at arXiv. https://doi.org/10.48550/arXiv.1406.2661.

85. Zhu, J.-Y., Park, T., Isola, P., and Efros, A.A. (2017). Unpaired image-toimage translation using cycle-consistent adversarial networks. In Proceedings of the IEEE international conference on computer vision, pp. 2223–2232.

86. Isola, P., Zhu, J.-Y., Zhou, T., and Efros, A.A. (2017). Image-to-image translation with conditional adversarial networks. In Proceedings of the IEEE conference on computer vision and pattern recognition, pp. 1125–1134.

87. Zhang, H., Goodfellow, I., Metaxas, D., and Odena, A. (2019). Self-attention generative adversarial networks. In International conference on machine learning (PMLR), pp. 7354–7363.

88. Parisi, G.I., Kemker, R., Part, J.L., Kanan, C., and Wermter, S. (2019). Continual lifelong learning with neural networks: A review. Neural Network. 113, 54–71. https://doi.org/10.1016/j.neunet.2019.01.012.

89. Hassabis, D., Kumaran, D., Summerfield, C., and Botvinick, M. (2017). Neuroscience-inspired artificial intelligence. Neuron 95, 245–258. https://doi.org/10.1016/j.neuron.2017.06.011.

90. Karani, N., Chaitanya, K., Baumgartner, C., and Konukoglu, E. (2018). A lifelong learning approach to brain MR segmentation across scanners and protocols. In International Conference on Medical Image Computing and Computer-Assisted Intervention (Cham: Springer International Publishing), pp. 476–484.

91. Baweja, C., Glocker, B., and Kamnitsas, K. (2018). Towards continual learning in medical imaging. Preprint at arXiv. https://doi.org/10.48550/ arXiv.1811.02496.

92. Ravishankar, H., Venkataramani, R., Anamandra, S., Sudhakar, P., and Annangi, P. (2019). Feature transformers: privacy preserving lifelong learners for medical imaging. In Medical Image Computing and Computer Assisted Intervention–MICCAI 2019: 22nd International Conference, Shenzhen, China, October 13–17, 2019, Proceedings, Part IV, 22 (Springer International Publishing), pp. 347–355.

93. Hofmanninger, J., Perkonigg, M., Brink, J.A., Pianykh, O., Herold, C., and Langs, G. (2020). Dynamic memory to alleviate catastrophic forgetting in continuous learning settings. In Medical Image Computing and Computer Assisted Intervention –. MICCAI 2020, 23 (Springer Internationa Publishing), pp. 359–368.

94. Kudithipudi, D., Aguilar-Simon, M., Babb, J., Bazhenov, M., Blackiston, D., Bongard, J., Brna, A.P., Chakravarthi Raja, S., Cheney, N., Clune, J., et al. (2022). Biological underpinnings for lifelong learning machines. Nat. Mach. Intell. 4, 196–210. https://doi.org/10.1038/s42256-022- 00452-0.

95. Monroe, C., Raymer, M.G., and Taylor, J. (2019). The US national quantum initiative: From act to action. Science 364, 440–442. https://doi.org/ 10.1126/science.aax0578.

96. Nielsen, M.A., and Chuang, I. (2002). Quantum Computation and Quantum Information. American Association of Physics Teachers (Cambridge: Cambridge university press). https://doi.org/10.1017/CBO9780511976667.

97. Parsons, D.F. (2011). Possible medical and biomedical uses of quantum computing. NeuroQuantology 9, 412. https://doi.org/10.14704/nq.2011. 9.3.412.

98. Sullivan, M.D., Edlund, M.J., Fan, M.-Y., DeVries, A., Braden, J.B., and Martin, B.C. (2010). Risks for possible and probable opioid misuse among recipients of chronic opioid therapy in commercial and medicaid insurance plans: The TROUP Study. Pain 150, 332–339. https://doi.org/ 10.1016/j.pain.2010.05.020.

99. Dilsizian, S.E., and Siegel, E.L. (2014). Artificial intelligence in medicine and cardiac imaging: harnessing big data and advanced computing to provide personalized medical diagnosis and treatment. Curr. Cardiol. Rep. 16, 441–448. https://doi.org/10.1007/s11886-013-0441-8.

100. Solenov, D., Brieler, J., and Scherrer, J.F. (2018). The Potential of Quantum Computing and Machine Learning to Advance Clinical Research and Change the Practice of Medicine. Mo. Med. 115, 463–467.

101. Kaissis, G., Ziller, A., Passerat-Palmbach, J., Ryffel, T., Usynin, D., Trask, A., Lima, I., Mancuso, J., Jungmann, F., Steinborn, M.-M., et al. (2021). End-to-end privacy preserving deep learning on multi-institutional medical imaging. Nat. Mach. Intell. 3, 473–484. https://doi.org/10.1038/ s42256-021-00337-8.

102. Lu, Y., Huang, X., Zhang, K., Maharjan, S., and Zhang, Y. (2021). Communication-efficient federated learning and permissioned blockchain for digital twin edge networks. IEEE Internet Things J. 8, 2276–2288. https://doi.org/10.1109/JIOT.2020.3015772.

103. Dayan, I., Roth, H.R., Zhong, A., Harouni, A., Gentili, A., Abidin, A.Z., Liu, A., Costa, A.B., Wood, B.J., Tsai, C.-S., et al. (2021). Federated learning for predicting clinical outcomes in patients with COVID-19. Nat. Med. 27, 1735–1743. https://doi.org/10.1038/s41591-021-01506-3.

104. Brisimi, T.S., Chen, R., Mela, T., Olshevsky, A., Paschalidis, I.C., and Shi, W. (2018). Federated learning of predictive models from federated elec-

tronic health records. Int. J. Med. Inf. 112, 59–67. https://doi.org/10. 1016/j.ijmedinf.2018.01.007.

105. Torres-Soto, J., and Ashley, E.A. (2020). Multi-task deep learning for cardiac rhythm detection in wearable devices. NPJ Digit. Med. 3, 116–118. https://doi.org/10.1038/s41746-020-00320-4.

106. Warnat-Herresthal, S., Schultze, H., Shastry, K.L., Manamohan, S., Mukherjee, S., Garg, V., Sarveswara, R., Handler, K., Pickkers, P., Aziz, N.A.,€ et al. (2021). Swarm learning for decentralized and confidential clinical machine learning. Nature 594, 265–270. https://doi.org/10.1038/ s41586-021-03583-3.

107. Dwork, C., and Roth, A. (2013). The Algorithmic Foundations of Differential Privacy. FNT. in Theoretical Computer Science 9, 211–407. https:// doi.org/10.1561/0400000042.

108. Bercea, C.I., Wiestler, B., Rueckert, D., and Albarqouni, S. (2022). Federated disentangled representation learning for unsupervised brain anomaly detection. Nat. Mach. Intell. 4, 685–695. https://doi.org/10.1038/ s42256-022-00515-2.

109. Yang, Z., Chen, M., Wong, K.-K., Poor, H.V., and Cui, S. (2021). Federated learning for 6G: Applications, challenges, and opportunities. Preprint at arXiv. https://doi.org/10.48550/arXiv.2101.01338.

110. Li, L., Gu, F., Li, H., Guo, J., and Gu, X. (2021). Digital twin bionics: a biological evolution-based digital twin approach for rapid product development. IEEE Access 9, 121507–121521. https://doi.org/10.1109/AC-CESS.2021.3108218.

111. Shahzad, M., Shafiq, M.T., Douglas, D., and Kassem, M. (2022). Digital twins in built environments: an investigation of the characteristics, applications, and challenges. Buildings 12, 120. https://doi.org/10.3390/ buildings12020120.

112. Haim, N., Vardi, G., Yehudai, G., Shamir, O., and Irani, M. (2022). Reconstructing Training Data from Trained Neural Networks. Preprint at arXiv. https://doi.org/10.48550/arXiv.2206.07758.

113. Chikwetu, L., Miao, Y., Woldetensae, M.K., Bell, D., Goldenholz, D.M., and Dunn, J. (2023). Does deidentification of data from wearable devices give us a false sense of security? A systematic review. Lancet. Digit. Health 5, e239–e247. https://doi.org/10.1016/S2589-7500(22)00234-5.

114. Steinhubl, S.R., Muse, E.D., Barrett, P.M., and Topol, E.J. (2016). Off the cuff: rebooting blood pressure treatment. Lancet 388, 749. https://doi. org/10.1016/S0140-6736(16)31348-4.

115. Zhang, Q., Xu, Y., Kang, S., Chen, J., Yao, Z., Wang, H., Wu, Q., Zhao, Q., Zhang, Q., Xu, R.h., et al. (2022). A novel computational framework for integrating multidimensional data to enhance accuracy in predicting the prognosis of colorectal cancer. MedComm – Future Medicine 1, e27. https://doi.org/10.1002/mef2.27.

116. Wu, C., Jarrett, A.M., Zhou, Z., Elshafeey, N., Adrada, B.E., Candelaria, R.P., Mohamed, R.M., Boge, M., Huo, L., White, J.B., et al. (2022). MRI-based digital models forecast patient-specific treatment responses to neoadjuvant chemotherapy in triple-negative breast cancer. Cancer Res. 82, 3394–3404. https://doi.org/10.1158/0008-5472.CAN-22-1329.

117. Batch, K.E., Yue, J., Darcovich, A., Lupton, K., Liu, C.C., Woodlock, D.P., El Amine, M.A.K., Causa-Andrieu, P.I., Gazit, L., Nguyen, G.H., et al. (2022). Developing a Cancer Digital Twin: Supervised Metastases Detection From Consecutive Structured Radiology Reports. Front. Artif. Intell. 5, 826402. https://doi.org/10.3389/frai.2022.826402.

118. Maeda, T., Tateishi, U., Komiyama, M., Fujimoto, H., Watanabe, S., Terauchi, T., Moriyama, N., Arai, Y., Sugimura, K., and Kakizoe, T. (2006). Distant metastasis of prostate cancer: early detection of recurrent tumor with dual-phase carbon-11 choline positron emission tomography/ computed tomography in two cases. Jpn. J. Clin. Oncol. 36, 598–601. https://doi.org/10.1093/jjco/hyl059.

119. Dilsizian, M.E., and Siegel, E.L. (2018). Machine Meets Biology: a Primer on Artificial Intelligence in Cardiology and Cardiac Imaging. Curr. Cardiol. Rep. 20, 139. https://doi.org/10.1007/s11886-018-1074-8.

120. Corral-Acero, J., Margara, F., Marciniak, M., Rodero, C., Loncaric, F., Feng, Y., Gilbert, A., Fernandes, J.F., Bukhari, H.A., Wajdan, A., et al. (2020). The ’Digital Twin’ to enable the vision of precision cardiology. Eur. Heart J. 41, 4556–4564. https://doi.org/10.1093/eurheartj/ehaa159.

121. Chakshu, N.K., Sazonov, I., and Nithiarasu, P. (2021). Towards enabling a cardiovascular digital twin for human systemic circulation using inverse analysis. Biomech. Model. Mechanobiol. 20, 449–465. https://doi.org 10.1007/s10237-020-01393-6.

122. Gliszczynski, M., and Ciszewska-Mlinari- c, M. (2021). Digital Twin and Medical Devices: Technological Significance of Convergent Inventions. J. Global Inf. Technol. Manag. 24, 134–148. https://doi.org/10.1080/ 1097198X.2021.1914498.

123. Ahmed, H., and Devoto, L. (2021). The Potential of a Digital Twin in Surgery. Surg. Innovat. 28, 509–510. https://doi.org/10.1177/1553350620975896.

124. Monteith, M. (2020). Further reducing the rate of code blue calls through early warning systems and enabling technologies. Healthc. Manag. Forum 33, 30–33. https://doi.org/10.1177/0840470419872770.

125. Medicine, D.U.S.o. (2022). New Generation Artificial Heart Implanted in Patient at Duke – First in U.S. https://medschool.duke.edu/news/newgeneration-artificial-heart-implanted-patient-duke-first-us.

126. Kleinerman, A., Rosenfeld, A., Benrimoh, D., Fratila, R., Armstrong, C., Mehltretter, J., Shneider, E., Yaniv-Rosenfeld, A., Karp, J., Reynolds, C.F., et al. (2021). Treatment selection using prototyping in latent-space

with application to depression treatment. PLoS One 16, e0258400. https://doi.org/10.1371/journal.pone.0258400.

127. Erol, T., Mendi, A.F., and Dogan, D. (2020). The digital twin revolution in healthcare. th International Symposium on Multidisciplinary Studies and Innovative Technologies (ISMSIT) 2020, 1–7. Istanbul, Turkey.

128. van Houten, H. (2020). How a virtual heart could save your real one. https://www.philips.com/a-w/about/news/archive/blogs/innovationmatters/20181112-how-a-virtual-heart-could-save-your-real-one.html.

129. Jorfi, M., D’Avanzo, C., Kim, D.Y., and Irimia, D. (2018). Three-Dimensional Models of the Human Brain Development and Diseases. Adv. Healthcare Mater. 7, 1700723. https://doi.org/10.1002/adhm. 201700723.

130. Qin, Y., Liang, S., Ye, Y., Zhu, K., Yan, L., Lu, Y., Lin, Y., Cong, X., Tang, X., and Qian, B. (2023). Toolllm: Facilitating large language models to master 16000+ real-world apis. Preprint at arXiv. https://doi.org/10. 48550/arXiv.2307.16789.

## Authors

Kang Zhang,<sup>1,2,3,10,15,16,</sup>\* Hong-Yu Zhou,<sup>4,16</sup> Daniel T. Baptista-Hon,<sup>3,15,16</sup> Yuanxu Gao,<sup>5,16</sup> Xiaohong Liu,<sup>6,16</sup> Eric Oermann,<sup>7</sup> Sheng Xu,<sup>8</sup> Shengwei Jin,<sup>2,9</sup> Jian Zhang,<sup>1,9</sup> Zhuo Sun,<sup>10</sup> Yun Yin,<sup>11</sup> Ronald M. Razmi,<sup>12</sup> Alexandre Loupy,<sup>13</sup> Stephan Beck,<sup>6,</sup>\* Jia Qu,<sup>1,2,</sup>\* Joseph Wu,<sup>14,</sup>\* and International Consortium of Digital Twins in Medicine

<sup>1</sup>National Clinical Eye Research Center, Eye Hospital, Wenzhou Medical University, Wenzhou 325000, China
<sup>2</sup>Institute for Clinical Data Science, Wenzhou Medical University, Wenzhou 325000, China
<sup>3</sup>Institute for AI in Medicine and Faculty of Medicine, Macau University of Science and Technology, Macau 999078, China
<sup>4</sup>Department of Biomedical Informatics, Harvard Medical School, Boston, MA 02138, USA
<sup>5</sup>Department of Big Data and Biomedical AI, College of Future Technology, Peking University, Beijing 100000, China
<sup>6</sup>Cancer Institute, University College London, WC1E 6BT London, UK
<sup>7</sup>NYU Langone Medical Center, New York University, New York, NY 10016, USA
<sup>8</sup>Department of Chemical Engineering and Nanoengineering, University of California San Diego, San Diego, CA 92093, USA
<sup>9</sup>Department of Anesthesia and Critical Care, The Second Affiliated Hospital and Yuying Children’s Hospital, Wenzhou Medical University, Wenzhou 325000, China
<sup>10</sup>Institute for Advanced Study on Eye Health and Diseases, Wenzhou Medical University, Wenzhou 325000, China
<sup>11</sup>Faculty of Business and Health Science Institute, City University of Macau, Macau 999078, China
<sup>12</sup>Zoi Capital, New York, NY 10013, USA
<sup>13</sup>Universite´ Paris Cite´ , INSERM U970 PARCC, Paris Institute for Transplantation and Organ Regeneration, 75015 Paris, France
<sup>14</sup>Cardiovascular Research Institute, Stanford University, Stanford, CA 94305, USA
<sup>15</sup>Guangzhou National Laboratory, Guangzhou 510005, China
<sup>16</sup>These authors contributed equally

\*Correspondence: kang.zhang@gmail.com (K.Z.), s.beck@ucl.ac.uk (S.B.), jia.qu@eye.ac.cn (J.Q.), joewu@stanford.edu (J.W.)

https://doi.org/10.1016/j.patter.2024.101028

## Figure Descriptions

**Figure 1.** Basics of DTs

A virtual entity, a physical entity, and an input data flow for real-time collection and monitoring of the physical entity’s state or physiological functions, along with an output data flow for real-time interaction and communication, such as transmitting diagnosis and treatment solutions.

**Figure 2.** Building with AI and metaverse

(A) Building DTs with LLMs.

(B) Combining embodied AI with LLM-powered DTs to construct AI agents.

(C) Metaverse provides a shared space for physical and virtual entities to communicate regarding patient care.

**Figure 3.** Hallmarks of the DT platform

Any healthcare DT should include basic physicalvirtual two-way communication, a metaverse of representative data, embodied AI agents based on LLM interfaces, reliable learning and prediction of multi-modal data, real-time patient monitoring, secure data storage, access to patient data, and adherence to ethical standards.

**Figure 4.** Representative data repository as a metaverse

(1) The DT platform integrates extensive multi-modal biological omics and medical data from patients, generating algorithms for individualized guidance in prevention, risk assessment, and therapies.

(2) The platform uses comprehensive patient input to match their virtual counterpart in the deeply phenotyped DT database, providing personalized treatment and prevention recommendations.

**Figure 5.** Development of the DT platform

1. Static twins: Hypothesis-driven, mathematical modeling for characterization of the physical entity.

2. Progressive twins: The dynamic modeling of the physical entity using temporal or progressive information.

3. Operational twins: Real-time interaction of the physical and virtual entities with each other, in a closedloop approach for therapy, preventative care and/ or human enhancement.

4. Autonomous twins: in the metaverse, to generate

$$
\begin{array} { r } { T ( s _ { t } , o _ { t } )  s _ { t + 1 } , r _ { t + 1 } } \\ { D ( s _ { t + 1 } , r _ { t + 1 } )  s ^ { \prime } _ { t + 2 } , r ^ { \prime } _ { t + 2 } } \end{array}
$$

Data; Virtual twin; Physical entity

131. Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., et al. (2022). Training language models to follow instructions with human feedback. Preprint at arXiv. https://doi.org/10.48550/arXiv.2203.02155.