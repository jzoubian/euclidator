#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""
Euclid Acronym Translator.
"""

__version__ = "Time-stamp: <2015-03-30 10:55:34 ycopin>"
__author__ = "Yannick Copin <y.copin@ipnl.in2p3.fr>"

import numpy as N

ecal = """
Title: Euclid Consortium Acronym List
Reference: EUCL-IAP-LI-1-001
Version: 2.02
Date: 28/02/2014

2dF:	Two Degree Field
2MASS:	Two Micron All Sky Survey
4MOST:	4-meter Multi Object Spectroscopic Telescope
A&A:	Authentication and Authorization
ABCL:	As Build Configuration List
ACRD:	Additional Cosmology Requirements Document
ACS:	Advanced Camera for Survey
AD:	Applicable Document
ADC:	Analog to Digital Converter
ADD:	Architectural Design Review
ADU:	Analog to Digital Unit
AEGIS:	All-wavelength Extended Groth strip International Survey
AGB:	Asymptotic Giant Branch
AGES:	AGN and Galaxy Evolution Survey
AGN:	Active Galactic Nuclei
AifA:	Argelander-Institut für Astronomie
AIM:	Action Items Manager
Airbus DS:	Airbus Defence and Space (Ex-Astrium)
AIT:	Assembly Integration and Testing
AIV:	Assembly Integration and Verification
ALMA:	Atacama Large Millimetre/Submillimetre Array
AMR:	Adaptive Mesh Refinement
ANNz:	Artificial Neural Network for photo-z measurement (photometric redshift measurement method)
AO:	Announcement of Opportunity
AOCS:	Attitude and Orbit Control System
APE:	Absolute Pointing Error
API:	Application Programming Interface
AR:	Acceptance Review (instruments) / Anti-Reflection
APC:	laboratoire AstroParticule et Cosmologie
APID:	Application Process ID
ASFT:	AStrium France Toulouse
ASI:	Agenzia Spaziale Italiana
ASIC:	Application Specific Integrated Circuit
AST:	EADS ASTrium (Currently Airbus Defence and Space, Airbus DS)
ATB:	Agency Technology Transfer Board
ATC:	Astronomy Technology Centre
AVM:	AVionic Model
AWG:	(ESA) Astronomy Working Group
aXe:	Software package for extraction of spectra from HST grism observations
B-mode:	Non-lensing signal in gravitational shear analysis – Curl term “B” from analogy with Electromagnetic signal
BAO:	Baryonic Acoustic Oscillations
BASSICC:	BAO SimulationS at the Institute for Computational Cosmology
BBM:	Bread Board Model
BBN:	Big Bang Nucleosynthesis
BCN:	Barcelona (consortium of institution in Barcelona for the FWA)
BOL:	Beginning Of Life
BOSS:	Baryon Oscillation Spectroscopic Survey
BPZ:	Bayesian Photo-Z (photometric redshift measurement method)
BSP:	Board Support Package
BSS:	Bottom Support Structure (NI-DS)
CAAUL:	Centro de Astronomia e Astrophysica da Universidade de Lisboa
CaC:	Cost at Completion
CAD:	Computer Aided Design
CADC:	Canadian Astronomy Data Center
CaLA:	Camera Lens Assembly
CalCD-A:	Calibration Concept Document Part A
CalCD-B:	Calibration Concept Document Part B
CalWG:	(Euclid) Calibration Working Group
CAUP:	Centro de Astrofisica da Universidade do Porto
CBE:	Current Best Estimate
CBS:	Cost Breakdown Structure
CCB:	Change Control Board / Configuration Control Board
CCD:	Charge Coupled Device
CCDWG:	(Euclid) CCD Working Group
CCIN2P3:	Centre de Calcul de l’IN2P3
CCN:	Contract Change Note
CCSDS:	Consultative Committee for Space Data System
CDE:	Coupled Dark Energy
CDF:	Concurrent Design Facility
CDM:	Cold Dark Matter
CDMS:	Command and Data Management System
CDMU:	Command and Data Management Unit
CDPU:	Control and Data Processing Unit
CDR:	Critical Design Review
CDS:	Centre de Données astronomiques de Strasbourg
CE:	Conducted Emission
CEA:	Commissariat à l'Energie Atomique
CERN:	Centre Européen pour la Recherche Nucléaire – European Organisation for Nuclear Research
CFE:	Customer Furnished Equipment
CFHT:	Canada-France-Hawaii Telescope
CFHTLenS:	Canada-France-Hawaii Telescope Lensing Survey
CFHTLS:	Canada-France-Hawaii Telescope Legacy Survey
CFI:	Customer Furnished Items
CFRP:	Carbon Fiber Reinforced Plastic
CI:	Configuration Item
CIB:	Cosmic Infrared Background
CIDL:	Configuration Item Data Lists
CIL:	Configuration Item List
CL:	CLusters of galaxies / Confidence Level / Corrector Lens
CLA:	Coupled Load analysis
CM:	Configuration Management / Common Mode / Cryo Mechanism
CMB:	Cosmic Microwave Background
CMP:	Configuration Management Plan
CMU:	Compensating Mechanism Unit (=NI-CMU)
CMD:	Command
CMOS:	Complementary Metal Oxide Silicon
CMRR:	Common Mode Rejection Ratio
CNES:	Centre National d’Etudes Spatiales (France)
CNRS:	Centre National de la Recherche Scientifique
COG:	Center Of Gravity
CoLA:	Corrector Lens Assembly
COM:	COMmunication (EC communication group)
COMBO-17:	Classifying Objects by Medium Band Observations (17 filters)
COSMOS:	COSMOlogical evolution Survey
COTS:	Commercial Off-The-Shelf
CPPM:	Centre de Physique des Particules de Marseille
CPU:	Central Processing Unit
CPV:	Commissioning and Performance Verification
CR:	Change Request / Cosmic Ray
CRB:	Change Review Board
CRC:	Cyclic Redundancy Check
CS:	Conducted Susceptibility
CSA:	Canadian Space Agency
CSIC:	CSIC
CSL:	Centre Spatial de Liège
CSRD:	Cosmological Simulations Requirements Document
CSS:	Cold Support Structure (of NI-DS)
CTE:	Charge Transfer Efficiency / Coefficient of Thermal Expansion
CTI:	Charge Transfer Inefficiency
CU:	Calibration Unit
CUS:	Common Uplink System
CV:	Cosmic Vision
CVS:	Concurrent Version System
DAC:	Digital to Analog Converter
DARK:	DARK Cosmology Centre (Denmark)
DB:	Data Base
DC:	Direct Current
DCCM:	Document Configuration and Change Management
DCU:	Detector Control Unit
DDD:	Detailed Design Document
DDL:	Deliverable Document List (Document Delivery List)
DDS:	Data Distribution System / Digital Data Storage
DDV:	Design, Development and Verification
DE:	Dark Energy
DEC:	DEClination
DeM:	Demonstration Model
DES:	Dark Energy Survey
DESC:	Dark Energy Science Collaboration
DESI:	Dark Energy Spectroscopic Instrument
DETF:	NASA Dark Energy Task Force
DGP:	Dvali, Gabadadze, Porrati model
DHS:	Data Handling System
DIT:	Detector Integration Time
DJF:	Design Justification File
DLL:	Design Limit Loads
DLR:	Deutsches zentrum für Luft- und Raumfahrt (Germany)
DM:	Dark Matter / Data Model / Development Model / Differential Mode
DMGSER:	Development Model and Ground Support Equipment Requirements
DMS:	Data Management System
DOE:	Department of Energy
DoF:	Degree of Freedom
DP:	Data Processing
DPRD:	Data Processing Requirements Document
DPRR:	Data Processing Readiness Review
DPU:	Data Processing Unit
DQ:	Data Quality
DQE:	Detected Quantum Efficiency
DQM:	Data Quality Mining
DQR:	Daily Quality Report
DR:	Data Release
DRB:	Delivery Review Board
DRD:	Document Requirements Descriptions / Document Review Description
DRL:	Document Requirements List
DS:	Deep Survey / Detection System
DTCP:	Daily Telemetry Communications Period
DTA:	Damage Threat Assessment
DTU:	Denmark Tekniske Universitet
DUNE:	Dark UNiverse Explorer
DWG:	Detector Working Group
E2E:	End-to-End
EAC:	Estimate At Completion
EACL:	Euclid Advisory and Coordination Support Lead
EACS:	Euclid Archive Core System
EADP:	Euclid Archive Development Plan
EAITM:	Electrical AIT Manager
EAITO:	Electrical AIT Operator
EAS:	Euclid Archive System
EAZY:	Easy and Accurate Z from Yale (photometric redshift measurement)
EC:	Euclid Consortium (=EMC)
ECA:	Euclid Contributing Agency
ECB:	Euclid Consortium Board
ECC:	Euclid Consortium Communication / Error Correcting Code
ECCG:	Euclid Consortium Coordination Group
ECEB:	Euclid Consortium Editorial Board
ECL:	Euclid Consortium Lead
ECMC:	Euclid Consortium Membership Committee
ECP:	Engineering Change Proposal
ECPG:	Euclid Consortium Publication Group
ECR:	Engineering Change Request
ECSGS:	Euclid Consortium Science Ground Segment
EC-SGS:	Euclid Consortium Science Ground Segment
ECSS:	European Cooperation for Space Standardization
ECSURV:	Euclid Consortium SURVey group
EDF:	Euclid Deep Field
EDFN:	Euclid Deep Field North
EDFS:	Euclid Deep Field South
EGI:	European Grid Initiative
EGSE:	Electrical Ground Support Equipment
EE:	Encircled Energy / End-to-End tests
EEE:	Electrical, Electronic, and Electromechanical
E-ELT:	European Extremely Large Telescope
EEPROM:	Electrically Erasable Programmable Read-Only Memory
EFE:	ESA Furnished Equipment
EIC:	Euclid Imaging Channels
EID-A:	Experiment Interface Document Part A
EID-B:	Experiment Interface Document Part B
EIDP:	End-Item Data Package
EIQT:	Euclid Image Quality Tool
EIR:	Euclid Instrument Requirement
ELA:	Euclid Legacy Archive
ELG:	Early Type Galaxy / Emission Line Galaxy
E-mode:	Pure gravitational lensing signal in gravitational shear analysis– Divergence term “E” from analogy with Electromagnetic signal
EM:	Electrical Model / Engineering Model
EMA:	Euclid Mission Archive
EMC:	ElectroMagnetic Compatibility / Euclid Mission Consortium (=EC)
EMI:	ElectroMagnetic Interference
EnEI:	non-Euclid Imaging
EO:	Earth Observation
EOAT:	Euclid Optimization Advisory Team
EOL:	End Of Life
EOPS:	EPO Scientist
EPER:	Extended Pixel Edge Response
EPFL:	Ecole Polytechnique Fédérale de Lausanne
E-PLM:	Extended PayLoad Model
EPLM:	Euclid PayLoad Module
EPO:	Education and Public Outreach
EQM:	Enginnering and Qualification Model
EROS:	Expérience pour la Recherche d’Objets Sombres
eROSITA:	Extended Röntgen Survey Imaging Telescope Array
ESA:	European Space Agency
ESAC:	European Space Astronomy Centre
ESO:	European Southern Observatory
ESOC:	European Space Operation Centre
ESST:	Euclid Science Study Team
ESSWG:	Euclid Sky Survey Working Group
EST:	Euclid Science Team
ESTEC:	ESA’s Space research and TEchnology Center
ESVM:	Euclid SerVice Module
ETC:	Exposure Time Calculator
ETHZ:	Eidgenössische Technische Hochschule Zürich
EVLA:	Expanded Very Large Array
EWS:	Euclid Wide Survey
EZ:	Easy-Z (redshift determination)
FA:	Funding Agency
FAR:	Flight Acceptance Review
F-CDPU:	Focal plane Control and Data Processing Unit
FCT:	Fundação para a Ciência e a Tecnologia (Portugal)
FDIR:	Failure Detection Isolation and Recovery
FE:	Front End
FEM:	Finite Element Model
FGS:	Fine Guidance Sensor
FFG:	ForschungsFörderungsGesellschaft (Austria)
FFT:	Fast Fourier Transform
FH:	Flight Harness
FIR:	Far InfraRed
FITS:	Flexible Image Transport System
FLRW:	Friedmann-Lemâitre-Roberston-Walker
FM:	Flight Model / Folding Mirror
FM1:	Folding Mirror 1
FM2:	Folding Mirror 2
FM3:	Folding Mirror 3
FMEA:	Failure Mode Effects Analysis
FMECA:	Failure Mode Effects and Criticality Analysis
FNRS:	Fonds National suisse de la Recherche Scientifique (Switzerland)
FOG:	Finger Of God
FOM:	Figure Of Merit
FOS:	Factor of Safety
FOV:	Field Of View
FP:	Focal Plane
FP7:	(European) 7 Framework Programme
FPA:	Focal Plane Array / Focal Plane Assembly
FPE:	Focal Plane Electronics
FPGA:	Field Programmable Gate Array
FPS:	Focal Plane Support
F-PSU:	Focal plane Power Supply Unit
FPT:	Full Performance Test
FRR:	Flight Readiness Review
FRW:	Friedmann-Robertson-Walker
FS:	Flight Spare
FSM:	Finite State Machine
FTA:	Fault Tree Analysis
FTE:	Full Time Equivalent
FW:	Flight Wheel
FWA:	Filter Wheel Assembly
FWHM:	Full Width Half Maximum
GADGET:	GAlaxies with Dark matter and Gas intEracT
GALFIT:	GALaxy FITing (two dimensional galaxy image decomposition program)
G3L:	Galaxy-Galaxy-Galaxy Lensing
GaBoDS:	Garching-Bonn Deep Survey
GAMA:	Galaxy and Mass Assembly
GC:	Galaxy Clustering
GCR:	Galactic Cosmic Ray
GC-SWG:	Galaxy Clustering Science Working Group
GDIR:	General Design & Interface Requirements
GDPRD:	Ground Data Processing Requirements Document
GEMS:	Galaxy Evolution from Morphology and SED Survey
GEV:	Galaxy and AGN Evolution
GFRP:	Glass Fiber Reinforced Plastic
GG:	(pure) Galaxy-Galaxy lensing signal
GGL:	Galaxy-Galaxy Lensing
GI:	Gravitational-Intrinsic ellipticity cross-correlations
GIM2D:	Galaxy Image 2-Dimension (two dimensional decomposition program)
GMM:	Geometrical Mathematical Model
GND:	GrouND
GOODS:	Great Observatory Origins Deep Survey
Gpc:	Gigaparsec
GPGPU:	General Purpose Graphical Processing Units
GPL:	General Public Licence
GR:	General Relativity
GRB:	Gamma Ray Burst
GREAT:	Gravitational lEnsing Accuracy Testing
GSDR:	Ground Segment Design Review
GSE:	Ground Support Equipment
GSFC:	Goddard Space Flight Center
GSIR:	Ground Segment Implementation Review
GSRQR:	Ground Segment Requirements Review
GSRR:	Ground Segment Readiness Review
GUI:	Graphical User Interface
GWA:	Grism Wheel Assembly
H2RG:	HAWAII 2RG - HgCdTe Astronomy Wide Area Infrared Imager 2k2 Resolution, Reference pixels and Guide mode
HAR:	Harness
HPC:	High Performance Computing
HPCC:	High Performance Computing Center
HDF:	Hubble Deep Field
HDR:	Hardware Design Review
HEALPIX:	Hierarchical Equal Area isoLatitude PIXelisation
HETDEX:	Hobby-Eberly Telescope Dark Energy Experiment
HGA:	High Gain Antenna
HgCdTe:	Hg (Mercury) Cadmium Telluride
HK:	House-Keepings (=H/K)
HSC:	HyperSuprime Camera
HST:	Hubble Space Telescope
HW:	HardWare (=H/W)
IAC:	Instituto de Astrofísica de Canarias
IADC:	Inter-Agency space Debris Coordination Committee
IAFR:	Instrument Acceptance Flight Review
IAL:	Infrastructure Abstraction Layer
IAP:	Image Analysis Pipeline / Institut d’Astrophysique de Paris
IAS:	Institut d’Astrophysique Spatiale
IASF:	INAF Istituto di Astrofisica Spaziale e Fisica cosmic
IASF-BO:	INAF Istituto di Astrofisica Spaziale e Fisica cosmica – Bologna
IASF-MI:	INAF Istituto di Astrofisica Spaziale e Fisica cosmica – Milan
IBDR:	Instrument Baseline Design Review
ICA:	Independent Component Analysis
ICD:	Interface Control Document
ICDR:	Instrument Critical Design Review
ICE:	Institut de Ciencies de l’Espai
ICG:	Institute of Cosmology and Gravitation
ICL:	Internal Communication Lead
ICM:	Intracluster Medium
ICU:	Instrument Control Unit
IDT:	Instrument Development Team
IEEC:	Institut d’Estudis Espacial de Catalunya
IF:	InterFace (=I/F)
IFA:	Institute For Astronomy (Edinburgh)
IFAE:	Institut de Fisica d’Altes Energies
IFAR:	Instrument Flight Acceptance Review
IFSI:	Istituto di Fisica della Spazio Interplanetario
IGC:	Institute for Gravitation and Cosmology (University of Portsmouth)
IGM:	InterGalactic Medium
II:	Intrinsic-Intrinsic ellipticity correlations
IICD:	Internal Interface Control Document
IIRD:	Internal Interface Requirements Document
IL:	Instrument Lead
ILS:	Independent Legacy Scientist
IM:	Interface Module
IMF:	Initial Mass Function
IN2P3:	Institut National de Physique Nucléaire et de Physique des Particules (CNRS)
INAF:	Istituto Nazionale AstroFisica (see also INAF Osservatorio Astronomico =AO*)
ING:	Isaac Newton Group (La Palma)
INSU:	Institut National des Sciences de l’Univers (CNRS)
IO:	Input Output (=I/O)
IoA:	Institute of Astronomy (University of Cambridge)
IOCR:	In Orbit Commissioning Review
IOL:	Instrument Operation Lead
IOT:	Instrument Operation Team
IPAC:	Infrared Processing and Analysis Center
IPDR:	Instrument Preliminary Design Review
IPNL:	Institut de Physique Nucléaire de Lyon
IPQE:	IntraPixel Quantum Efficiency
IPRR:	Instrument Preliminary Readiness Review
IR:	InfraRed
IRAP:	Institut de Recherche en Astrophysique et Planétologie
IRAS:	InfraRed Astronomical Satellite
IRD:	Interface Requirements Document
IQR:	Instrument Qualification Review
IRFU:	Institut de Recherche sur les lois Fondamentales de l’Univers – CEA
IRR:	Instrument Requirement Review
IS:	Instrument Scientist
ISDC:	Integral Science Data Center (Switzerland)
ISM:	Inter Stellar Medium / Iso-Static Mount
ISO:	International Organization for Standardization
ISSR:	Instrument System Requirements Review
IST:	Inter-SWG Taskforce
ISW:	Integrated Sachs Wolfe effect
IW:	Instrument Workstation
IT:	Information Technology
ITA:	Institute of Theoretical Astrophysics (University of Oslo)
ITAR:	International Traffic in Arms Regulations
ITN:	(Marie Curie) Internal Training Network
IT-Ind:	Italian Industry
ITT:	Invitation To Tender
IWS:	Instrument Work Station
JDEM:	Joint Dark Energy Mission
JHU:	John Hopkins University
JLP:	Jet Propulsion Laboratory
JMU:	John Moores University (Liverpool)
JPIP:	Joint Project Implementation Plan
JWST:	James Webb Space Telescope
KiDS:	Kilo Degree Survey
KO:	Kick Off
KSB:	Kaiser Squires and Broadhurst (shape measurement method)
L1:	Level 1 Euclid data
L2:	Level 2 Euclid data / Second Lagrange point
L3:	Level 3 Euclid data
LAM:	Laboratoire d’Astrophysique de Marseille
LBG:	Lyman Break Galaxies
LBL:	Lawrence Berkeley national Laboratory
LBT:	Large Binocular Telescope
LCDM:	Lambda Cold Dark Matter
LDAP:	Lightweight Directory Access Protocol
LDPRD:	Legacy Data Processing Requirements Document
LED:	Light Emitting Diode
LENSFIT:	LENS FITing (bayesian shape measurement method)
LEOP:	Launch and Early Operations
Le PHARE:	PHotometric Analysis for Redshift Estimate (photometric redshift measurement method)
LET:	Linear Energy Transfer
LF:	Luminosity Function
LFA:	Lead Funding Agency
LGPL:	Lesser General Public Licence
LHC:	Large Hadron Collider
LLD:	Launch Lock Device
LLI:	Long-Lead Item
LLIF:	Long-Lead Item List
LMU:	Ludwig Maximilians-Universistät München
LoA:	Letter of Agreement
LOFAR:	LOw Frequency Array for Radio astronomy
LoI:	Letter of Intent
LOS:	Line Of sight
LPNHE:	Laboratoire de Physique Nucléaire et de Hautes Energie
LPP:	Lightcurve Processing Pipeline
LRD:	Legacy Requirements Document
LRG:	Luminous Red Galaxy
LRR:	Launcher Readiness Review
LSB:	Least Significative Bit / Low Surface Brightness
LSF:	Least Square Fit
LSST:	Large Synoptic Survey Telescope
LTB:	Lemaître-Tolman-Bondi
LTG:	Late Type Galaxy
LVDS:	Low Voltage Differential Signal
M1:	Primary Mirror
M2:	Secondary mirror
M3:	Tertiary mirror
M2M:	M2 Mechanism (subsystem)
M2MM:	M2M Mechanism (mechanism part)
M&C:	Monitoring & Control
MACC:	Multi Accumulation Readout
MACHO:	Massive Compact Halo Object
MAITM:	Mechanical AIT Manager
MAITO:	Mechanical AIT Operator
MAP:	JPL Mission Assurance Plan
MC:	Monte Carlo
MCDR:	Mission Critical Design Review
MCMC:	Markov Chain Monte Carlo
MCRR:	Mission Commissioning Results Review
MCT:	Mercury Cadmium Telluride
MDE:	M2M Drive Electronics
MF:	Mass Function
MFAR:	Mission Flight Acceptance Review
MG:	Modified Gravity
MGSE:	Mechanical Ground Support Equipment
MICD:	Mechanical Interface Control Document
MINECO:	MINisterio de Economia y COmpetividad Spain
MIPS:	Mega Instructions Per Second
MIR:	Mid InfaRed
MIRD:	Mission Implementation Requirements Document
M/L:	Mass-to-Light ratio
MLA:	Multi Lateral Agreement
MLI:	Multi Layer Insulation
MMU:	Mass-Memory Unit
MOC:	Mission Operations Centre / MOlecular Contamination
MOCD-A:	Mission Operation Concept Document Part A
MOCD-D:	Mission Operation Concept Document Part B
MOGS:	Mission Operations Ground Segment
MOI:	Moment Of Inertia
MOND:	MOdified Newtonian Dynamics
MOONS:	Multi-Object Optical and Near-infrared Spectrograph for VLT
MOS:	Margin Of Safety / Multi-Object Spectrograph
MOU:	Memorandum Of Understanding
MP:	Management Plan
Mpc:	Megaparsec
MPDR:	Mission Preliminary Design Review
MPE:	Max Planck institut für Extraterrestrische physic
MPIA:	Max Planck Institut für Astronomie
MPP:	Milestone Payment Plan
MPS:	Mission Planning System
MRB:	Material Review Board
MRD:	Mission Requirements Document
MSE:	Mirror Surface Error
MSRR:	Mission System Requirements Review
MSSL:	Mullard Space Science Laboratory
MTD:	Mass and Thermal Dummy
MTF:	Modulation Transfer Function
MWA:	Murchison Wide field Array
N/A:	Not Applicable
NAOJ:	National Astronomical Observatory of Japan
NASA:	National Aeronautic and Space Administration
NBI:	Niels Bohr Institute
NC:	Non Convolutive
NCR:	Non-Conformance Request
NCRB:	Non-Conformance Review Board
NCTS:	Non-Conformance Tracking System
NDI:	Non-Destructive Inspection
NDRO:	Non Destructive Readout
NEP:	North Ecliptic Pole
NFW:	Navarro Frenk and White
NGP:	North Galactic Pole
NI-CMS:	NI-CMU Simulator
NI-CMT:	NI-CMU Test equipment
NI-CMU:	NISP Compensation Mechanism Unit
NI-CU:	NISP Calibration Unit
NI-CUS:	NI-CU Simulator
NI-CUT:	NI-CU Test equipment
NID:	NISP Interface Document
NI-DCU:	NISP Detector Control Unit
NI-DDT:	NI-DCU Development model and Test equipment
NI-DIS:	NI-DCU/DPU Test equipment I/F Simulator
NI-DIW:	NI-DCU/DPU Test equipment Instrument Workstation
NI-DPU:	NISP Data Processing Unit
NI-DS:	NISP Detection System
NI-DST:	NI-DS Test equipment
NI-DTE:	NI-DCU/DPU Test equipment
NI-DTS:	NI-DS Thermal control Simulator
NI-DTW:	NI-DCU/DPU Test equipment control Workstation
NI-EWS:	NISP EGSE control WorkStation
NI-FH:	NISP Flight Harness
NI-FPA:	NISP Focal plane Assembly
NI-FPS:	NI-FPA Simulator
NI-FTT:	NI-FPA Thermal control Test equipment
NI-FWA:	NISP Filter Wheel Assembly
NI-FWA-CR:	NISP Filter Wheel Assemby Cryo Mechanism
NI-FWS:	NI-FWA Simulator
NI-FWT:	NI-FWA Test equipment
NI-GWA:	NISP Grism Wheel Assembly
NI-GWA-CR:	NISP Grism Wheel Assembly Cry Mechanism
NI-GWS:	NI-FWA Simulator
NI-GWT:	NI-GWA Test equipment
NI-HSS:	NISP HarneSS
NI-HSS-IU:	NISP Inter Unit Harness
NI-HSS-TH:	NISP Thermal Harness
NI-ICU:	NISP Instrument Control Unit
NI-IDS:	NI-DPU/DCU Interface Simulator
NI-ISS:	NI-ICU S/C I/F Simulator
NI-OA:	NISP Optics Assembly
NI-OMA:	NISP Opto-Mechanical Assembly
NI-OMADA:	NI-OMA and Detector Assembly
NIP:	Near Infrared Photometer
NIR:	Near InfraRed
NIRDWG:	(Euclid) Near Infrared Detector Working Group
NIS:	Near Infrared Spectrograph
NI-SA:	NISP Structure Assembly
NI-SCS:	NISP Sensor Chip System
NISP:	Near Infrared Spectrometer and Photometer
NI-TC:	NISP Thermal Control
NI-ITE:	NI-ICU Test equipment
NI-ITW:	NI-ICU Test equipment Workstation
NI-IWS:	NISP Instrument Workstation
NI-OMS:	NI-OMA Simulator
NI-OTS:	NI-OMA Thermal control Simulator
NI-SIS:	NISP S/C I/F Simulator
NI-SSS:	NI-DS Sidecar Support Structure
NI-SST:	NI-SCS Test equipment
NI-WE:	NISP Warm Electronics
NI-WIS:	NI-WE Test equipment S/C I/F Simulator
NI-WIW:	NI-WE test equipment Instrument Workstation
NI-WTE:	NI-WE Test Equipment
NI-WTW:	NI-WE Test equipment control Workstation
NOVA:	Nederlandse Onderzoeschool Voor Astronomie The Netherlands
NPM:	National Project Manager
NRA:	NASA Research Announcement
NRB:	Non-conformance Review Board
NSC:	Norwegian Space Center (Norway)
NSDC:	National Space Science Data Center (NASA)
NSI:	National Space Institute (Denmark)
NSF:	National Science Foundation
NOW:	de Nederlandse organisatie voor Wetenschappeliijk Onderzoek
OABr:	INAF Osservatorio Astronomico di Brera
OAITM:	Optical AIT Manager
OAITO:	Optical AIT Operator
OAPd:	INAF Osservatorio Astronomico di Padova
OAR:	INAF Osservatorio Astronomico di Roma / Off Axis Rejection
OATo:	INAF Osservatorio Astronomico di Torino
OATs:	INAF Osservatorio Astronomico di Trieste
OB:	Optical Bench
OBSW:	On Board SoftWare
OCA:	Observatoire de la Côte d’Azur
OCD:	Operation Concept Document
OGS:	Operations Ground Segment
OGSE:	Optical Ground Support Equipment
OM:	Operation and Maintenance / Operation Model (pipelines)
ORR:	Operations Readiness Review
OSEWG:	Operations and System Engineering Working Group
OSTM:	Optical and Structural and Thermal Model
OT:	Operational Temperature
OTE:	Optical Telescope Element
OTS:	Off-The-Shelf
OU:	Organisation Unit
OU-EXT:	Organisation Unit EXTernal data
OU-LE3:	Organisation Unit LEvel3 data
OU-MER:	Organisation Unit MERged data
OU-NIR:	Organisation Unit Near InfraRed imaging data
OU-PHZ:	Organisation Unit PHoto-Z data
OU-SHE:	Organisation Unit SHEar data
OU-SIM:	Organisation Unit SIMulation data
OU-SIR:	Organisation Unit SPEctral near InfraRed imaging data
OU-SPE:	Organisation Unit SPEctral extraction and redshift data
OU-VIS:	Organisation Unit VISible imaging data
PA:	Product Assurance
PAC:	PArticulate Contamination
PAD:	Part Approval Document
PAH:	Poly-Aromatic Hydrocarbons
PanSTARRS:	Panoramic Survey Telescope Rapid response System
PAP:	Product Assurance Plan
PARD:	Product Assurance Requirement Document
PAU:	Physics of the Accelerating Universe
PCA:	Principal Component Analysis
PCB:	Printed Circuit Board
PCDU:	Power Conditioning and Distribution Unit
PCE:	Photon to electron Conversion Efficiency
PDCU:	Power Distribution Control Unit
PDD:	Payload Definition Document / Product Definition Document
PDF:	Probability Density Function
PDHU:	Processing Data Handling Unit
PDR:	Preliminary Design Review
PEM:	Proximity Electronic Module
PERD:	Payload Element Requirements Document
PI:	Principal Investigator
PIC:	Port d’Informacio Cientifica (Barcelona)
PID:	Proportional Integral Derivative
PFCI:	Potential Failure Critical Items
PFE:	Prime Furnished Equipment
PFM:	Proto-Flight Model
PFS:	Prime Focus Spectrograph
PHAT:	PHoto-z Accuracy Testing
PHOTO-z:	PHOTOmetric redshift
PL:	PayLoad (=P/L)
PLM:	PayLoad Module
PLM-RD:	PayLoad Module Requirements Document
PM:	Progress Meeting / Project Manager
PMCU:	Parameters and Mechanism Control Unit / Power and Mechanisms Control Unit
PMP:	Project Management Plan
PMRD:	Project Management Requirements Document
PN:	Planetary Nebulae
PO:	Project Office
PRACE:	PartneRship for Advanced Computing in Europe
PRNU:	Photo Response Non-Uniformity / Pixel Response Non-Uniformity
PRR:	Preliminary Requirements Review
PRODEX:	ESA Programme de Développement d’EXpériences scientifiques
PROM:	Programmable Read Only Memory
PRTECH:	Prototech (Bergen)
PS:	Project Scientist / Pan-STARRS
PS1:	Pan-STARRS-1
PS2:	Pan-STARRS-2
PSD:	Power Spectral Density
PSF:	Point Spread Function
PSR:	Pre-Ship Review
PSU:	Power Supply Unit (ROE VIS)
PT:	Product Tree
PV:	Performance Verification
QA:	Quality Assurance
QAITM:	Quality AIT Manager
QAITO:	Quality AIT Operator
QC:	Quality Control
QE:	Quantum Efficiency
QLA:	Quick Look Analysis
QM:	Qualification Model
QR:	Qualification Review
QSO:	Quasi-Stellar Object (quasar)
RA:	Right Ascension
RAM:	Random Access Memory
RAS:	Royal Astronomical Society
RB:	Requirement Baseline
RCS:	Red Cluster Sequence Survey
RD:	Reference Document
RE:	Radiated Emission
rEE50:	50% Encircled Energy radius
rEE80:	80% Encircled Energy radius
RFA:	Request For Approval
RFD:	Request For Deviation
RFI:	Request For Information
RFQ:	Request For Quotation
RFW:	Request For Waiver
RGMM:	Reduced Geometrical Mathematical Model
RMS:	Root Mean Square
RMW:	Read Modify Write
ROE:	Read-Out Electronics / Royal Observatory Edinburgh
ROI:	Region Of Interest
ROIC:	Readout Integrated Circuit
ROM:	Rough Order of Magnitude
RON:	ReadOut Noise
ROSA:	ROmanian Space Agency (Romania)
RPE:	Relative Pointing Error
R-PLM:	Reduced PayLoad Module
RPSU:	ROE Power Supply
RS:	Radiated Susceptibility
RSD:	Redshift Space Distortion
RSSD:	ESA Research and Space Support Department
RSU:	Read-out Shutter Unit
RT:	Real Time pipeline / Remote Terminal / Room Temperature
RTA:	Real Time Assessment
RTD:	Resistance Temperature Device
RTMM:	Reduced Thermal Mathematical Model
RuG:	Rijkuniversiteit Groningen
SAA:	Solar Aspect Angle
SAID:	Science Analysis Implementation Document
SAp:	Service d’Astrophysique – CEA/IRFU
SARD:	System AIV Requirements Document
SAT:	Science Archive Team
SC:	SpaceCraft (=S/C)
SCA:	Sensor Chip Assembly
SCE:	Sensor Chip Electronic
SCET:	SpaceCraft Elapsed Time
SciRD:	Science Requirements Document
SCM:	Software Configuration Management
SCMP:	Software Configuration Management Plan
SCR:	Software Change Request
SCOS:	Satellite Control and Operation System
SCS:	Sensor Chip System
SDC:	Science Data Center
SDM:	SOC Development Manager
SDR:	Software Development Repositories
SDSS:	Sloan Digital Sky Survey
SED:	Single Event Damage / Spectral Energy Distribution
SEL:	Single Event Latch-up
SEL-2:	Sun-Earth Lagrange point 2 (=L2)
SEMP:	System Engineering Management Plan
SEP:	South Ecliptic Pole / System Engineering Plan
SER:	Secrétaire d’Etat à l’Education et à la Recherche (Switzerland)
SEU:	Single Event Upset
SFR:	Star Formation Rate
SG:	Science Group
SGP:	South Galactic Pole
SGS:	Science Ground Segment
SGSS:	Science Ground Segment Scientist
SiC:	Silicon Carbide
SIDECAR:	System for Image Digitization, Enhancement, Control And Retrieval.
SIDM:	Self Interacting Dark Matter
SIM-SWG:	Simulations Science Working Group
SIP:	Science Implementation Plan
SIR:	System Integration Review
SIRD:	Science Implementation Requirements Document
SIS:	Service d’Ingénierie des Systèmes – CEA/IRFU
SISSA:	Scuola Internazionale Superiore di Studi Avanzati
SIVVP:	Software Integration, Validation and Verification Plan
SKA:	Square Kilometre Array
SL:	Strong Lensing / System Lead
SLI:	Single Layer Insulation
SME:	Surface Mirror Error
SMM:	Structural Mathematical Model
SMP:	Science Management Plan
SN:	Signal-to-Noise ratio (=S/N) / SuperNova
SNIa:	Type Ia SuperNova
SNLS:	SuperNova Legacy Survey
SNR:	Signal to Noise Ratio
SNT:	SuperNova and Transients
SOC:	Science Operation Center / Statement Of Compliance
SOCD:	Science Operations Concept Document
SOD:	Science Operation Department
SODD:	Science Output Definition Document
SOVT:	Science Operations Verification Tests
SOW:	Statement Of Work
SPA:	Software Product Assurance
SPACE:	Spectroscopic All-Sky Cosmic Explorer
SPAP:	Software Product Assurance Plan
SPBD:	System Performance Budget Document
SPC:	Science Programme Committee
SPM:	Software Product Manager
SPR:	Science Performance Review
SPT:	South Pole Telescope
SPW:	SPace Wire
SQAP:	Software Quality Assurance Plan
SQL:	Structured Query Language
SRB:	Software Review Board
SRD:	Software Requirements Document / System Requirements Document
SRE:	ESA Science and Robotic Exploration
SRE-O:	SRE-Operations department
SSA:	SunShield Assembly
SSC:	Sensor System Chip / Space Science Center (Denmark)
SRR:	System Requirements Review
SSE:	Sun-Spacecraft Earth angle
ST:	Science Team
STEP:	Shear Testing Programme
STM:	Structural & Thermal Model
SU:	Shutter Unit
SUMIRE:	Subaru Measurement of Images and REdshifts
SUR:	Science User Requirements
SVM:	SerVice Module
SVN:	SubVersioN
SVT:	System Verification Testing
SVVP:	System Validation and Verification Plan
STScI:	Space Telescope Science Institute
SW:	SoftWare (=S/W)
SWG:	Science Working Group
SWL:	Space Wire Link
SZ:	Sunyaev-Zeldovich
TA:	Telescope Assembly
TAA:	Technical Assistance Agreement
TAITM:	Thermal AIT Manager
TAITO:	Thermal AIT Operator
TAS:	Thales Alenia Space
TB:	Thermal Balance
TBA:	To Be Assigned – To Be Appointed
TBC:	To Be Confirmed
TBD:	To Be Defined/Determined
TBR:	To Be Revised
TBT:	Thermal Balance Test
TBV:	To Be Verified
TBW:	To Be Written
TC:	TeleCommands
TCS:	Thermal Control System
TDA:	Technology Development Activity
TE:	Test Equipment
TEKES:	TEknologian ja innovaatioiden KEhittämiskeskuS
TeVeS:	Tensor Vector Scalar
TGSE:	Thermal Ground Support Equipment
TH-SWG:	Theory Science Working Group
TID:	Total Ionising Dose
TIF:	Thermal InterFace
TIM:	Technical Information Meeting
TIS:	Teledyne Imaging Systems / Teledyne Imaging Sensors / Total Integrated Scattering
TLM:	Telemetry
TM:	TeleMetry
TMA:	Three Mirrors Anastigmat
TMM:	Thermal Mathematical Model
TMT:	Thirty Meter Telescope
TN:	Technical Note
Top:	Temperature Operating
ToR:	Terms of Reference
TR:	software TRansfer phase
TRL:	Technology Readiness Level
TRP:	Temperature Reference Point
TT:	(Euclid) Tiger Team
TT&C:	Telemetry, Tracking and Command
TV:	Thermal Vacuum
UAH:	University of Alcalá de Henares
UC:	University of California
UCL:	University College London
UDF:	Ultra-Deep Field
UH:	University of Helsinki / University of Hawaii
UIO:	Universitetet i Oslo
UKIDS:	UKIRT Infrared Deep Sky Survey
UKIDSS-LAS:	UKIRT Infrared Deep Sky Survey Large Area Survey
UKIRT:	United Kingdom InfraRed Telescope
UKSA:	United Kingdom Space Agency (UK)
UMA:	Universidad Autonomia de Madrid
UML:	Unified Modeling Language
UoG:	University of Geneva
UPCT:	Universidad Politécnica de CarTagena - Technical University of Cartagena
UPenn:	University of Pennsylvania
UPMC:	Université Pierre et Marie Curie
URD:	User Requirements Document
URF:	Unit Reference Frame
USM:	Universitäts-Sternwarte München
USNO:	US Naval Observatory
USS:	Upper Support Structure (NI-DS)
UTR:	Up The Ramp Readout
V&V:	Validation and Verification
VCD:	Verification Control Document
VGS:	Verification Ground Support
VI-CDPU:	VIS Control and Data Processing Unit
VI-CU:	VIS Calibration Unit
VDA:	Vapour Deposit Aluminium
VIDEO:	VISTA Deep Extragalactic Observatory survey
VI-FPA:	VIS Focal Plane Assembly
VI-FPA-DP:	VIS FPA Detector Panel
VI-FPA-ES:	VIS FPA Electronic Structure
VI-HAR:	VIS HARness
VI-FH:	VIS Flight Harness
VIKING:	VISTA Kilo degree INfrared Galaxy survey
VIMOS:	Visible wide field Imager and Multi-Object Spectrograph
VI-PMCU:	VIS Power and Mechanisms Control Unit
VIPERS:	VIMOS Public Extragalactic Redshift Survey
VIPM:	VIS Project Manager
VI-RSU:	VIS Read-out Shutter Unit
VIS:	VISible Instrument
VISTA:	Visible and Infrared Survey Telescope for Astronomy
VI-SU:	VIS Shutter Unit
VLA:	Very Large Array
VLT:	ESO Very Large Telescope
VO:	Virtual Observatory
VObs:	Virtual Observatory
VST:	VLT Survey Telescope
VVDS:	VIMOS VLT Deep survey
WA:	Worst Average PSF
WBS:	Work Breakdown Structure
WCS:	World Coordinate System
WDM:	Warm Dark Matter
WE:	Warm Electronics
WEAVE:	WHT Enhanced Area Velocity Explorer
WFC3:	HST Wide Field Camera 3
WFE:	Wave Front Error
WFS:	Wave Front Sensor
WG:	Working Group
WHT:	William Herschel Telescope
WIMP:	Weakly Interacting Massive Particle
WISE:	Wide field Infrared Survey Explorer
WFIRST:	Wide Field InfraRed Survey Telescope
WL:	Weak Lensing
WL-SWG:	Weak Lensing Science Working Group
WMAP:	Wilkinson Microwave-Anisotropy Probe
WP:	Work Package
WPBD:	Work Package Breakdown and Description
WPD:	Work Package Description
WR:	Worst worst Red PSF
WS:	Wide Survey
XC:	Cross-Correlation
XML:	eXtensible Markup Language
XMM:	X-ray Multi-Mirror Telescope
XSD:	XML Schema Definition
ZEBRA:	Zurich Extragalactic Bayesian Redshift Analyser (photometric redshift measurement method)
"""


def read(lines):
    """
    Return acronym dictionary {ACRONYM:definition} from acronym lines.
    """

    d = dict()

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, val = line.split(':')       # ACRONYM: definition
        val = val.strip()
        if key not in d:
            d[key] = val
        elif val != d[key]:
            print("%s: merging %s entries: '%s' and '%s'" %
                  (filename, key, val, d[key]))
            d[key] = ' / '.join((d[key], val))

    return d

if __name__ == '__main__':

    import optparse
    from cStringIO import StringIO
    import re

    usage = "usage: [%prog] [options] ACRONYM [ACRONYM2 ...]"
    parser = optparse.OptionParser(usage, version=__version__)

    parser.add_option("-E", "--regex", action="store_true",
                      help="Interpret arguments as regular expressions.",
                      default=False)
    parser.add_option("-R", "--reversed", action="store_true",
                      help="Reversed look-up (always regex).",
                      default=False)

    opts, args = parser.parse_args()

    d = read(StringIO(ecal))

    title = d.pop('Title')
    ref = d.pop('Reference')
    ver = d.pop('Version')
    date = d.pop('Date')
    print("%s [%s] -- v.%s (%s)" % (title, ref, ver, date))

    maxl = max( len(key) for key in d )  # Length of longest acronym

    if not args:
        args = sorted(d.keys())
    elif opts.reversed:
        args = [ key for arg in args
                 for key, val in d.items()
                 if re.search(arg, val, re.IGNORECASE) ]
    elif opts.regex:
        args = [ key for arg in args for key in d if re.search(arg, key) ]

    for arg in args:
        print("%*s: %s" % (maxl, arg,
                           d.get(arg, 'YAUA (Yet Another Unknown Acronym)')))
