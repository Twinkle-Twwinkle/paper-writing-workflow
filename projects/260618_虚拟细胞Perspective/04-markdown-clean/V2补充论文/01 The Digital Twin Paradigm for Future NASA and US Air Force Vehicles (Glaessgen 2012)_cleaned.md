# The Digital Twin Paradigm for Future NASA and U.S. Air Force Vehicles

## Abstract

Future generations of NASA and U.S. Air Force vehicles will require lighter mass while being subjected to higher loads and more extreme service conditions over longer time periods than the present generation. Current approaches for certification, fleet management and sustainment are largely based on statistical distributions of material properties, heuristic design philosophies, physical testing and assumed similitude between testing and operational conditions and will likely be unable to address these extreme requirements. To address the shortcomings of conventional approaches, a fundamental paradigm shift is needed. This paradigm shift, the Digital Twin, integrates ultra-high fidelity simulation with the vehicle’s on-board integrated vehicle health management system, maintenance history and all available historical and fleet data to mirror the life of its flying twin and enable unprecedented levels of safety and reliability.

## Introduction

Existing methodologies for vehicle certification, fleet management and sustainment are largely based on similitude and a heuristic understanding of the effects of operational and anomalous conditions on the structural health, safety and performance of a vehicle. A common manifestation of similitude and heuristics is in the form of the “factors-of-safety” used during design and certification. So-called factors-of-safety are rooted in a heuristic legacy wherein a factor of, say, 1.5 or 2.0 has “always” been sufficient to account for a particular class of unknown unknowns (e.g., loads, material properties). Often, the history and pedigree of such factors is uncertain.

Additionally, compounding of factors-of-safety is pervasive and may lead to unnecessarily heavy structures and reduced performance without necessarily improving the actual safety of the vehicle or the probability of mission success. Even current probabilistic or reliability methodologies are inadequate because they are based on assumed similitude between the circumstances in which the underlying statistics were obtained and the environment in which the vehicle operates. When similitude is violated, probabilistic methods break down as readily as those based on factors-of-safety. Although statistical assessments are important, they must be part of an overall best-physics approach that is relevant to each individual vehicle.

Similitude is so commonplace in the current engineering process that it is often invisible to the engineers who invoke it. A ubiquitous example can be found in engineering design and analysis where computer codes (including commercial finite element codes) are used to “predict” failures. Such codes are of limited “predictive” capability because, in a general sense, they only produce responses that have previously been observed experimentally and then programmed for future assessment. For example, to account for a phenomenon such as the interaction between environment and structural damage, the issue must have been foreseen, specific experiments must have been performed and their results must have been incorporated within the models. Further, since different environments, or even different degrees of environment, have differing synergies with damage, the specific environments that will be encountered by the vehicle must have been considered during the design process. Otherwise, “worst case” scenarios must be used to ensure the health and safety of the vehicle; albeit at the expense of weight and performance.

Another common manifestation of similitude and heuristics is in the form of inspection intervals and schedules used for fleet management and sustainment. Inspection schedules are typically determined from experience with similar vehicles that have performed similar missions. Often, inspection is performed based on experience with the fleet leader, the vehicle in the fleet that experienced the most flights or the worst degradation. If, for example, unacceptable degradation of a component was found during an inspection of the fleet leader, it may be decided that all vehicles of that class be inspected immediately regardless of the specific history of each vehicle.

These issues are amplified when new designs or operating conditions are considered. Unlike the methods used to insure safety and reliability of existing vehicles that have a clear and wellunderstood legacy, many future vehicles will have little direct precedent to follow, and in some cases (e.g., long duration space missions) the vehicle may be impossible to inspect and maintain in the conventional sense. Thus, the ability to fully understand degradation and anomalous events and foresee previously unknown unknowns may represent the difference between mission success and mission failure.

The Digital Twin\* paradigm is a long-term vision aimed at addressing these and other shortcomings of current practices for certification, fleet management and sustainment. This paper focuses on a discussion of the requirements for, development of and application of the Digital Twin. The paper is composed of the following sections: conventional approaches for certification and sustainment; the concept of a Digital Twin and its applications, including certification and sustainment, vehicle health and mission management, and in-situ forensics; identification of near-term opportunities for implementing elements of the Digital Twin paradigm; a brief discussion of the advantages of the Digital Twin; its potential influence on National goals; and a brief summary and references.

## Conventional Approaches

Much of the philosophy and many of the guidelines used for certification, fleet management and sustainment of NASA and U.S. Air Force vehicles can be found in government and professional society standards and handbooks. A small sampling of requirements for structures, materials and non-destructive evaluation (NDE) is shown in Table 1. These documents include expansive discussions of structural design and test, including factors-of-safety; fracture control; materials and processing; NDE; effects of specific environments; detailed analysis of failure modes; and standards for numerical models and analysis. Many of the documents used by NASA and the U.S. Air Force are developed in-house, while others are derived from technical societies such as the American Institute of Aeronautics and Astronautics (AIAA) and the American Society of Mechanical Engineers (ASME). These documents are rooted in decades-old experience with laboratory tests, protoflight tests and flight histories. In this section, some of the conventional approaches to certification, fleet management and sustainment will be illustrated through the discussion of examples taken from several of the documents, including: NASA-STD-5001A, NASA-STD-5019 and NASA-HDBK-5010.

The criteria for determination of factors-of-safety for both deterministic and probabilistic analyses are discussed in several of the standards listed in Table 1, including NASA-STD-5001A<sup>1</sup> that specifically addresses spaceflight hardware.! ! As discussed in the standard, the accepted practice for “verification” of launch vehicles is “the prototype approach in which a separate, dedicated test structure, identical to the flight structure, is tested to demonstrate that the design meets the factor-of-safety requirements.” An alternative to the prototype approach is “the protoflight approach wherein the flight structure is tested to levels somewhat above limit stress (or load) but below yield strength.” The latter approach requires a factor-of-safety for yield that is higher than the factor-of-safety used for prototype testing. “No test” options are also allowed for metallic structures; however, according to the standard “projects which propose to use the ‘no-test’ approach generally must use larger factors of safety.” In all of these cases, “verification” depends on the ability to perform laboratory tests on a “dedicated test structure [that is] identical to the flight structure.” Additionally, the loading, boundary conditions, environment must also be representative of flight conditions.

Table 1: Sample of Publicly Available Standards and Handbooks
<table><tr><td>Standard</td><td>Title</td><td>Date</td></tr><tr><td>NASA-STD-5001A1</td><td>Structural Design and Test Factors of Safety for Spaceflight Hardware</td><td>08/05/08</td></tr><tr><td>NASA-STD-50192</td><td>Fracture Control Requirements for Spaceflight Hardware</td><td>01/07/08</td></tr><tr><td>NASA-STD-60163</td><td>Standard Materials and Process Requirements for Spacecraft</td><td>07/11/08</td></tr><tr><td>NASA-STD-50094</td><td>Non-Destructive Evaluation Requirements for Fracture Control Programs</td><td>04/07/08</td></tr><tr><td>MSFC-STD-30295</td><td>Guidelines for the Selection of Metallic Materials for Stress Corrosion Cracking Resistance in Sodium Chloride Environments</td><td>05/22/00</td></tr><tr><td>JSC 22267B6</td><td>Fatigue Crack Growth Computer Program NASGRO, Version 3.0</td><td>11/2001</td></tr><tr><td>NASA-STD-50127</td><td>Strength and Life Assessment Requirements for Liquid Fueled Space Propulsion System Engines</td><td>06/13/06</td></tr><tr><td>NASA-STD-70098</td><td>Standard for Models and Simulations</td><td>07/11/08</td></tr><tr><td>NASA-STD-50039</td><td>Fracture Control Requirements for Payloads Using the Space Shuttle</td><td>10/07/96</td></tr><tr><td>NASA-STD-501010</td><td>Fracture Control Implementation Handbook for Payloads, Experiments, and Similar Hardware</td><td>05/24/05</td></tr><tr><td>MIL-HDBK-6870A11</td><td>Fracture Control Requirements, Nondestructive for Aircraft and Missile Materials and Parts</td><td>08/28/01</td></tr><tr><td>DOT/FAA/AR- MMPDS-0312</td><td>Metallic Materials Properties Development and Standardization</td><td>2007</td></tr><tr><td>ANSI/AIAA S-08113</td><td>Space Systems  Composite Overwrapped Pressure Vessels</td><td>12/19/00</td></tr><tr><td>ASME Boiler and Pressure Vessel Code14</td><td>Rules for Construction of Pressure Vessels, Section VIII</td><td>09/2004</td></tr></table>

The minimum design and test factors-of-safety for metallic and composite structures outlined in NASA-STD-5001A<sup>1</sup> are given in Tables 2 and 3. These factors vary widely depending on circumstance and can be as large as 2.0 depending on the material and local structural configuration. Because of the apparent scatter in material response under cyclic and creep loading, the corresponding factors are even larger. According to NASA-STD-5001A<sup>1</sup>, a service life factor of 4.0 is applied to “spaceflight structures made of well-characterized materials and with sufficient load cycle data that accounts for all in-service environments,” while for “structures made of materials that are not well characterized or those that may have complex failure modes, such as composite structures, an additional factor and testing may be required by the assigned Technical Authority at the responsible NASA Center.”

Table 2: Minimum Design and Test Factors for Metallic Structures<sup>1</sup>
<table><tr><td>Verification Approach</td><td>Ultimate Design Factor</td><td>Yield Design Factor</td><td>Qualification Design Factor</td><td>Acceptance or Proof Test Factor</td></tr><tr><td>Prototype</td><td>1.4</td><td>1.0*</td><td>1.4</td><td>NA or 1.05**</td></tr><tr><td>Protoflight</td><td>1.4</td><td>1.25</td><td>NA</td><td>1.2***</td></tr></table>

NOTES:  
\* Structure must be assessed to prevent detrimental yielding during flight, acceptance, or proof testing  
\*\* Propellant tanks and solid rocket motor cases only.  
\*\*\* Protoflight level testing is required for the first article of a multiple article build. A workmanship level test is required for all subsequent copies of the first article. The workmanship test shall be approved by the responsible Technical Authority.

Table 3: Minimum Design and Test Factors for Composite/Bonded Structures<sup>1</sup>
<table><tr><td>Verification Approach</td><td>Geometry of Structure</td><td>Ultimate Design Factor</td><td>Qualification Test Factor</td><td>Acceptance or Proof Test Factor</td></tr><tr><td>Prototype</td><td>Discontinuities**</td><td>2.0*</td><td>1.4</td><td>1.05</td></tr><tr><td>Prototype</td><td>Uniform Material</td><td>1.4</td><td>1.4</td><td>1.05</td></tr><tr><td>Protoflight</td><td>Discontinuities**</td><td>2.0*</td><td>NA</td><td>1.2</td></tr><tr><td>Protoflight</td><td>Uniform Material</td><td>1.5</td><td>NA</td><td>1.2</td></tr></table>

NOTES:  
\* Factor applies to concentrated stress. For nonsafety-critical applications, this factor may be reduced to 1.4 for prototype structures and 1.5 for protoflight structures.  
\*\* Discontinuities are defined as an interruption in the physical structure or configuration of the part. These include, but are not limited to, holes, delaminations, and debonds.

Fracture critical hardware requires the additional imposition of damage tolerance requirements (see, for example, NASA-STD-5019<sup>2</sup>). Here, specific requirements, exceptions and methodologies for assessing metallic and composite pressure vessels, rotating machinery, structural components and other fracture critical hardware are discussed. The application of continuum fracture mechanics analyses, including NASGRO fatigue crack growth analysis (see JSC 22267B<sup>6</sup>), is the foundation of much of the codified fracture control methodology.

An extreme case of codified conservatism is discussed in NASA-HDBK-5010<sup>10</sup>, where separate conservatisms for crack size, applied loads, material properties, and analysis are discussed for “known cracks” in fracture critical hardware. Known cracks in fracture critical hardware require special treatment wherein upper bounds for crack size estimate accounting for “any possible nondetected adjacent cracks and/or crack tip extensions” are required, as shown in Figure 1. Here, the crack size assumed for analysis $( 2 c _ { A } )$ is a combination of the NDE-detected crack dimensions (2c<sub>D</sub>) and an adjustment based on the NDE detection capability (2c<sub>N</sub>).

Additionally, worst-case limit loads for the mission must be used to compute the far field stress state at the location of the detected crack. Typically, these loads are used in conjunction with an assumed fatigue spectrum. As an example, one of the many loading spectra developed by NASA Goddard Space Flight Center for the analysis of payloads during launch and landing of the Space Shuttle (STS) is shown in Table 4. The table shows the number of cycles during launch and landing and the percentage of the total limit stress to be applied during each of these cycles. Here, total limit stress is defined as the sum of the stresses due to low frequency, random and acoustic loading.

Table!4:!Launch!and!Landing!Spectrum!for!STS!Payloads<sup>10</sup>
<table><tr><td>Load Step</td><td colspan="3">Cycles/flight</td><td colspan="2">Cyclic Stress (% limit value)</td></tr><tr><td>Number</td><td>Launch</td><td>Landing</td><td>Total</td><td>Minimum</td><td>Maximum</td></tr><tr><td>1</td><td>1</td><td>1</td><td>2</td><td>-100</td><td>100</td></tr><tr><td></td><td>35</td><td>1</td><td>4</td><td>-90</td><td>90</td></tr><tr><td></td><td></td><td>3</td><td>8</td><td>-80</td><td>80</td></tr><tr><td></td><td>12</td><td>3</td><td>15</td><td>-70</td><td>70</td></tr><tr><td></td><td>46</td><td>3</td><td>49</td><td>-60</td><td>60</td></tr><tr><td></td><td>78</td><td>3</td><td>81</td><td>-50</td><td>50</td></tr><tr><td>NMTOON</td><td>165</td><td>13</td><td>178</td><td>-40</td><td>40</td></tr><tr><td>∞</td><td>493</td><td>148</td><td>641</td><td>-30</td><td>30</td></tr><tr><td>9</td><td>2229</td><td>891</td><td>3120</td><td>-20</td><td>20</td></tr><tr><td>10</td><td>2132</td><td>1273</td><td>3405</td><td>-10</td><td>10</td></tr><tr><td>11</td><td>2920</td><td>2099</td><td>5019</td><td>-7</td><td>7</td></tr><tr><td>12</td><td>22272</td><td>6581</td><td>28853</td><td>-5</td><td>5</td></tr><tr><td>13</td><td>82954</td><td>8701</td><td>91655</td><td>-3</td><td>3</td></tr></table>

The handbook requires analysts to use material properties corresponding to the lower bound of fracture toughness and the upper bound of fatigue crack growth rate (da/dN vs. ΔK) as shown in Figure 2. Upper bounds of fatigue crack growth rate curves are either visually estimated or statistically estimated as being three standard deviations above the mean values. Finally, analyses of known flaws must show that the component has a service life factor of four and a safety factor of 1.5 against fracture.

The codified practices that are advocated and mandated by these many standards and handbooks have been carefully developed over several decades and have certainly stood the test of time. They are invaluable tools for use by the present-day engineer for assessment of vehicle structure. However, they tend to be reactive rather than proactive and are often based on heuristic experience, worst-case scenarios and fleet leaders rather than on the specific material, structural configuration and usage of an individual vehicle. Moreover, they may not be sufficient to address the future extreme requirements of some future NASA and U.S. Air Force vehicles.

## The Digital Twin

## Concept

Future generations of aerospace vehicles will require lighter mass while being subjected to higher loads and more extreme service conditions over longer time periods than the present generation of vehicles. As a result, demands on structural materials will be greatly increased and structural margins will necessarily be decreased. Since extreme thermal, mechanical, and acoustical loadings may be impossible to reproduce in a laboratory at anything more than the component scale, the identification and quantification of limit states via computational simulation is needed.

Because the vehicles are likely to encounter conditions that cannot be foreseen, revolutionary approaches to verification and validation of the models, simulations and systems must also be developed. Additionally, the ability to modify and evaluate the consequences of modification to mission parameters in near-real time will be required. Moreover, the consequences of failure during a long-duration space mission, where the vehicle is far from home, will almost certainly be catastrophic.

Future generations of vehicles will rely on increasingly complex, heterogeneous and multifunctional material forms with increasingly complex failure modes. Thus, the extensive legacy of historical flight information incorporated in the various standards and handbooks that were based on decades of aircraft and spacecraft design experience, will likely be insufficient to either certify future extreme vehicles or to guarantee mission success. Additionally, the extensive physical testing that provided the confidence needed to assure the success of previous missions has become increasingly expensive to perform. Thus, a complete and fundamental understanding of physical processes related to degradation at the material, structural and system level and throughout the vehicle’s life-cycle is needed to move beyond the past decades of empirical and heuristic design rules that result in inefficiencies and unquantifiable reliability.

Complex missions, particularly those where external support is difficult or impossible, will necessitate complete real-time management of complex materials, structures and systems that will ultimately lead to “self-aware” vehicles. The numerous resulting engineering challenges will necessitate a shift from current empirical-based standard engineering practice to an additional emphasis on cradle-to-grave sustainment and reliability that will include (1) new multidisciplinary physics-based methods to ensure robust certification, and (2) new multidisciplinary methodolgies to ensure life-cycle sustainability. If various best-physics (i.e., the most accurate, physically realistic and robust) models can be integrated with one another and with on-board sensor suites, they will form a basis for certification of vehicles by simulation and for real-time, continuous, health management of those vehicles during their missions. They will form the foundation of a Digital Twin 15-18

A Digital Twin is an integrated multiphysics, multiscale, probabilistic simulation of an as-built vehicle or system that uses the best available physical models, sensor updates, fleet history, etc., to mirror the life of its corresponding flying twin. The Digital Twin is ultra-realistic and may consider one or more important and interdependent vehicle systems, including airframe, propulsion and energy storage, life support, avionics, thermal protection, etc. The extreme requirements of the Digital Twin motivate the integration of design of materials and revolutionary approaches for material processing. Manufacturing anomalies that may affect the vehicle are also explicitly considered, evaluated and monitored. In addition to the backbone of high-fidelity physical models of the as-built structure, the Digital Twin integrates sensor data from the vehicle’s on-board integrated vehicle health management (IVHM) system, maintenance history and all available historical and fleet data obtained using data mining and text mining.

By combining all of this information, the Digital Twin continuously forecasts the health of the vehicle or system, the remaining useful life and the probability of mission success. The Digital Twin can also predict system response to safety critical events and uncover previously unknown issues before they become critical by comparing predicted and actual responses. Finally, the systems on board the Digital Twin are capable of mitigating damage or degradation by activating self-healing mechanisms or by recommending changes in mission profile to decrease loadings thereby increasing both the life span and the probability of mission success.

## Attributes

A graphical representation of some of the attributes of a Digital Twin is shown in Figure 3. The narrative of the figure proceeds by column from the left-top pane to the right-bottom pane, as follows:

## Left Top Pane

The Digital Twin incorporates precise models of the as-built configuration of a vehicle or component, including material microstructure, defects, fabrication anomalies, etc. Determination of these parameters requires characterization at multiple length scales in the range from less than a micron to meters. Once this precise “baseline” is determined, the ultra-high fidelity physical models can be used to predict future states of the vehicle. The montage illustrates the wide range of material types, physical length scales and structural configurations that may be considered by the Digital Twin. From upper left to lower right are: failed fibers in a fiber-reinforced composite material, a finite element model of a space vehicle, a specimen undergoing arc-jet testing, the BSTRA (ball strut tie rod assembly) joint in the Space Shuttle Orbiter main engine feedline flowliner, the microstructure of an advanced alloy containing a fatigue crack, a carbon nanotube and a friction stir-welded aluminum skin-stiffened panel.

## Left Middle Pane

The Digital Twin relies heavily on its on-board IVHM system to continuously monitor aerodynamic, thermal, inertial and other loading in addition to measures of degradation in vehicle health and performance. The montage illustrates representative IVHM systems and system outputs. From left to right are: a measured strain field near a fatigue crack, a cyclic loading spectrum, an IVHM fiber optic strain sensing system and a computer tomography image of delaminations (blue squares) in a laminated composite material.

## Left Bottom Pane

The backbone of the Digital Twin is a suite of ultra-high fidelity physical models of the vehicle and its systems and structures of interest. These may include models of one or more important and interdependent vehicle systems, including airframe, propulsion and energy storage, life support, avionics, thermal protection, etc. The montage illustrates the wide range of physical phenomena, models and modeling outputs that may be included in the Digital Twin. From upper left to lower right are: an illustration of an atom modeled in a quantum mechanics or molecular dynamics simulation, a three-dimensional finite element simulation of deformation and fracture in an aluminum alloy, a hypothetical computational fluid dynamics simulation of a vehicle during atmospheric re-entry, prediction of the number of cycles needed to nucleate a fatigue crack $\mathrm { ( N _ { n u c } ) }$ , a finite element simulation of mode shapes in the Space Shuttle Orbiter main engine feedline flowliner, a multi-scale model of crack growth, and a simple model of radiation transport through boron-nitride nanotubes as a neutron shielding material.

## Center Top Pane

The Digital Twin uses its on-board IVHM system to update the physics-based models with sensor data and produce continuously refined predictions of vehicle health and probability of mission success. It can also perform option and impact investigation to answer questions regarding the impact of changes to mission profile on all future conditions of the vehicle. The figure shows Bayesian updates of the probability of failure as a function of time wherein sensor data is incorporated to increase accuracy and decrease uncertainty in the predictions.

## Center Pane

Each Digital Twin is uniquely developed for a particular vehicle and may be employed to “fly” future missions during the design and certification process, continuously assess health during flight, perform insitu forensics of the effect of potential or real hazards and virtually evaluate the effect of potential changes to the mission. A hypothetical vehicle is shown in the figure.

## Center Bottom Pane

The Digital Twin integrates fleet data, maintenance reports and other historical information via data mining and text mining to further inform simulations of the vehicle. The figure shows a notional representation of the computational and data processing capabilities of the Digital Twin as represented by the PLEIADES supercomputer at NASA Ames Research Center, a model of the human brain and streams of text and data supporting the Digital Twin.

## Right Top Pane

The Digital Twin is enabling to virtual digital certification and sustainment by replacing past decades of empirically based design rules that result in structural inefficiencies and unquantifiable reliability with ultra-high fidelity simulations, sensor systems and data that are immediately relevant to each unique vehicle. The figure shows several of the many existing standards and handbooks that may be replaced by the Digital Twin.

## Right Middle Pane

The Digital Twin mirrors the actual flight of the flying twin by using sensor updates to continuously assess vehicle health including determining remaining life of structural components and systems, estimating probability of mission success and evaluating in-situ repair (self-healing), in-flight mitigation or load

alleviation strategies and other mission modifications. The effects of modifications of mission parameters are evaluated and previously unforeseen consequences are evaluated. The figure shows estimates of remaining useful life (RUL) as a function of the number of load cycles.

## Right Bottom Pane

The Digital Twin also uses its assessment of historical norms, fabrication/manufacturing reports and maintenance data (where available) combined with Bayesian updates to high-fidelity models to perform in situ forensics, including anomaly detection/diagnosis and fault tree analysis. The figure shows a schematic of a fault tree associated with the hypothetical failure of a sensor.

## Identification of Near-Term Opportunities

Many of the technologies critical for the Digital Twin are currently being developed under related visions for multi-scale and multi-physics modeling, structural health management, highperformance computing and others. Unlike those individual visions, the vision for the Digital Twin integrates the broad range of technologies with a singular focus. However, such an ambitious concept is unlikely to attain maturity for many decades, so a series of intermediate steps is required. Among these steps is the Air Force Research Laboratory (AFRL) Digital Twin: Spiral 1<sup>17</sup>, a plan to integrate existing state-of-the-art technologies, benchmark current capabilities and identify gaps using components from an existing U.S. Air Force vehicle, specifically, the F-15, as a testbed. Another approach, being considered by NASA, is to focus on a small highly critical non-redundant component such as a microelectromechanical system (MEMS) that has characteristic length scales accessible with only the highest fidelity simulation methods and health management tools available. By exercising such ultra-high fidelity approaches on flight hardware, the shortcomings of the existing state-of-the-art in multiscale modeling, in-situ experimentation and material state awareness will be highlighted.

## Advantages Over Conventional Approaches

As a virtual instantiation of a flying vehicle, the Digital Twin is expected to be able to experience every event that its flying twin experiences. Because of its ability to mirror the life of a specific vehicle in an as-built state, the Digital Twin will necessarily revolutionize certification, fleet management and sustainment. It will also decrease system weight by reducing reliance on statistical distributions of material properties, heuristic design philosophies, physical testing and assumed similitude between testing and operational conditions. Once the vehicle is launched, the Digital Twin will increase the reliability of the flying vehicle because of its ability to continuously monitor and mitigate degradation and anomalous events. Additionally, it will enable mission managers to make knowledgeable decisions regarding the consequences of possible in-flight changes to a vehicle’s mission.

## Influence on National Goals

Although the Digital Twin represents a revolution in the paradigms used for certification, fleet management and sustainment in support of extreme flight missions, it has the ability to influence other National priorities and goals. In addition to its prominence in the recently-published roadmaps of NASA’s Office of Chief Technologist (OCT)<sup>15-16</sup> and plans of the Air Force Research Laboratory<sup>17-18</sup>, the Digital Twin paradigm can provide focus to the recent advocacy of the National Science Foundation (NSF) and the National Research Council (NRC) in the areas of Simulation Based Engineering Science (SBES)<sup>19</sup>, Integrated Computational Materials Engineering (ICME)<sup>20</sup> and Materials State Awareness<sup>21</sup><sub>.</sub>

Many of the concepts discussed in the NSF’s recommendations for SBES are pervasive throughout the themes of the Digital Twin, including, multiscale modeling of materials, dynamic simulation of sensors, and verification and validation. Because the vehicles needed for future extreme missions are unlikely to be developed using existing material forms, the design and development of new enabling (e.g., multifunctional, nanostructured, ultra-durable) materials is required and is well aligned with the NRC’s ICME roadmap. Additionally, an understanding of the exact state of the structure of the vehicle or its systems, including the existence of defects at the microstructural and, possibly, the atomistic scale, is required as a baseline for ultra-high fidelity simulations. The ability to assess the evolution of defects is a critical element within the Digital Twin’s on-board IVHM system and is well aligned with the NRC’s advocacy for developments in Materials State Awareness.

Figure 4 is taken from the executive summary of the NASA OCT roadmap for technology area 12 (TA 12)<sup>16</sup> and proposes a broad spectrum of future NASA technologies that can be focused by the Digital Twin. The headings in the ellipses within Figure 4 represent the numbers and titles of various sections in the OCT TA 12 roadmap where the technologies are discussed.

Potential spin-offs from the development of the Digital Twin span the breadth of the Nation’s industrial and manufacturing sectors, infrastructure and development of nanotechnology. By replacing conventional engineering practices with an understanding of the degradation of an individual vehicle or vehicle system, the paradigm of the Digital Twin will impact the way that physical items ranging from micro-devices to civil infrastructure are developed, certified and maintained.

## Summary

Future generations of aerospace vehicles will require lighter mass while being subjected to higher loads and more extreme service conditions over longer time periods than the present generation of vehicles. As a result, demands on structural materials will be greatly increased and structural margins will necessarily be decreased. Additionally, the requirements placed on other systems and subsystems will be greater than those previously experienced even though demands for long-term reliability will increase. Because extreme thermal, mechanical, and acoustical loadings may be impossible to reproduce in a laboratory at anything more than the component scale, the identification and quantification of limit states via computational simulation is needed. Additionally, the vehicles are likely to encounter conditions that cannot be foreseen. Thus, the ability to modify and evaluate the modification of mission parameters in near-real time will be required.

Current approaches to certification, fleet management and sustainment of NASA and U.S. Air Force vehicles are largely based on statistical distributions of material properties, heuristic design philosophies, physical testing and assumed similitude between testing and operational conditions and will likely be unable to address future extreme requirements. Some of the current approaches to certification, fleet management and sustainment were illustrated through the discussion of examples taken from several documents, including: NASA-STD-5001A, NASA-STD-5019 and NASA-HDBK-5010.

To address the shortcomings of conventional approaches, the paradigm of a Digital Twin was presented. The Digital Twin is an integrated multiphysics, multiscale, probabilistic simulation of an as-built vehicle or system that uses the best available physical models, sensor updates, fleet history, etc., to mirror the life of its corresponding flying twin. The Digital Twin is ultra-realistic and may consider one or more important and interdependent vehicle systems. The Digital Twin integrates sensor data from the vehicle’s on-board IVHM system, maintenance history and all available historical and fleet data. By combining this information, the Digital Twin continuously forecasts the health of the vehicle or system, the remaining useful life and the probability of mission success. The systems on board the Digital Twin are also capable of mitigating damage or degradation by activating self-healing mechanisms or by recommending changes in mission profile to decrease loadings thereby increasing both the life span and the probability of mission success.

Near-term opportunities for early development of the Digital Twin paradigm at AFRL and NASA were discussed and include the integration of various existing state-of-the-art technologies, benchmarking of current capabilities and identification of gaps using critical flight components as testbeds. Advantages of the Digital Twin, its potential influence on far reaching NASA, U.S. Air Force goals and broader National goals were also discussed.

## References

<sup>1</sup>Anon., “Structural Design and Test Factors of Safety for Spaceflight Hardware,” NASA-STD-5001A, August 2008.

<sup>2</sup>Anon., “Fracture Control Requirements for Spaceflight Hardware,” NASA-STD-5019, January 2008.

<sup>3</sup>Anon., “Standard Materials and Process Requirements for Spacecraft,” NASA-STD-6016, July 2008.

<sup>4</sup>Anon., “Non-Destructive Evaluation Requirements for Fracture Control Programs,” NASA-STD-5009, April 2008.

<sup>5</sup>Anon., “Guidelines for the Selection of Metallic Materials for Stress Corrosion Cracking Resistance in Sodium Chloride Environments,” MSFC-STD-3029, May 2000.

<sup>6</sup>Anon., “Fatigue Crack Growth Computer Program NASGRO,” Version 3.0, JSC 22267B, November 2001.

<sup>7</sup>Anon., “Strength and Life Assessment Requirements for Liquid Fueled Space Propulsion System Engines,” NASA-STD-5012, June 2006.

<sup>8</sup>Anon., “Standard for Models and Simulations,” NASA-STD-7009, July 2008.

<sup>9</sup>Anon., “Fracture Control Requirements for Payloads Using the Space Shuttle,” NASA-STD-5003, October 1996.

<sup>10</sup>Anon., “Fracture Control Implementation Handbook for Payloads, Experiments, and Similar Hardware,” NASA-STD-5010, May 2005.

<sup>11</sup>Anon., “Fracture Control Requirements, Nondestructive for Aircraft and Missile Materials and Parts,” Mil-HDBK-6870A, August 2001.

<sup>12</sup>Anon., “Metallic Materials Properties Development and Standardization,” DOT/FAA/AR-MMPDS-03, 2007.

<sup>13</sup>Anon., “Space Systems – Composite Overwrapped Pressure Vessels,” ANSI/AIAA S-081, December 2000.

<sup>14</sup>Anon., “Rules for Construction of Pressure Vessels,” ASME Boiler and Pressure Vessel Code, Section VIII, September 2004.

<sup>15</sup>Shafto, M., Conroy, M., Doyle, R., Glaessgen, E., Kemp, C., LeMoigne, J. and Wang, L., “Technology Area 11: Modeling, Simulation, Information Technology and Processing Roadmap,” NASA Office of Chief Technologist, November, 2010.

<sup>16</sup>Piascik, R., Vickers, J., Lowry, D., Scotti, S., Stewart, J. and Calomino, A., “Technology Area 12: Materials, Structures, Mechanical Systems, and Manufacturing Roadmap,” NASA Office of Chief Technologist, November, 2010.

<sup>17</sup>Kobryn, P.A. and Tuegel, E.J., “Condition-based Maintenance Plus Structural Integrity (CBM+SI) & the Airframe Digital Twin,” USAF Air Force Research Laboratory, 88ABW-201101428, March 2011.

<sup>18</sup>Tuegel, E.J., Ingraffea, A.R., Eason, T.J. and Spottswood, S.M., “Reengineering Aircraft Structural Life Prediction Using a Digital Twin,” International Journal of Aerospace Engineering, doi:10.1155/2011/154798, 2011.

<sup>19</sup>Anon., “Simulation-Based Engineering Science: Revolutionizing Engineering Science through Simulation,” National Science Foundation, May 2006.

<sup>20</sup>Anon., “Integrated Computational Materials Engineering: A Transformational Discipline for Improved Competitiveness and National Security,” National Research Council, ISBN: 0-309- 12000-4, 2008.

<sup>21</sup>Anon., “Proceedings of a Workshop on Materials State Awareness,” National Research Council, ISBN: 0-309-12166-3, 2008.

## Authors

E. H. Glaessgen<sup>\*</sup> Durability and Damage Tolerance Branch NASA Langley Research Center, Hampton, Virginia, 23681

D.S. Stargel<sup>†</sup> Aerospace, Chemical, and Material Sciences Air Force Office of Scientific Research, Arlington VA, 22203

## Figure Descriptions

**Figure 1.** Imposed Conservatism for Detected Cracks (Adapted from Reference 10).

**Figure 2.** Crack Growth Rate for Detected Cracks<sup>10</sup>

**Figure 3.** Graphical Representation of the Digital Twin Paradigm.

**Figure 4.** Integration of Technologies within a Digital Twin<sup>16</sup>