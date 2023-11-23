<p align="center">
  <img width="180" src="./resources/logo/MUSE_LOGO2.png" alt="MUSE_LOGO">
  <h1 align="center">MUSE ArcGIS Toolbox</h1>
</p>

# Paper Link:
<a href="https://doi.org/10.1080/136588197242329">Jianxin Yang, Wenwu Tang, Jian Gong, Rui Shi, Minrui Zheng, Yunzhe Dai,Simulating urban expansion using cellular automata model with spatiotemporally explicit representation of urban demand,Landscape and Urban Planning</a>

<a href="http://dx.doi.org/10.2139/ssrn.4171720">Yang, Jianxin and Yang, Shengbing and Li, Jingjing and Gong, Jian and Li, Jingye and Yuan, Man and Dai, Yunzhe, A Distance-Driven Urban Simulation Model (DISUSIM): Accounting For Urban Morphology At Multiple Landscape Levels</a>

<a href="https://doi.org/10.1080/136588197242329">CHRISTOPHER J. BROOKES (1997) A parameterized region-growing programme for site allocation on raster suitability maps, International Journal of Geographical Information Science</a>

# 1. Introduction
The **MUSE (Multi-engine Urban Expansion Simulator)** is a sophisticated cellular automata-based model meticulously designed for simulating urban growth. It integrates three distinct patch size generators and employs four diverse patch generation techniques. The primary objective of MUSE is to accurately replicate the intricate patterns and procedures inherent in urban land expansion. The four patch-generating algorithms at the core of MUSE are:

- **Distance-Constrained Patch Shape (Dis-PGE)**
- **Neighborhood-Constrained Patch Shape (Nei-PGE)**
- **Spatially-Constrained Patch Shape (SPGE)**
- **Parameterized Patch-Growing Engine with Tradeoff between Maximized Cell Suitability and Optimized Patch Shape (PPGE)**

Furthermore, MUSE offers three patch size controllers to facilitate precise patch size determination:

- **Lognormal Distribution:** This Patch Size Controller operates under the assumption that patch areas follow a log-normal distribution (refer to Equation (4)).
- **Power Distribution:** The Patch Size Controller assumes that patch areas follow a power-law distribution (refer to Equation (5)).
- **History:** The third Patch Size Controller utilizes historical patch area sizes from previous periods.

With MUSE, users gain the capability to create diverse spatial patterns for urban land structures. They can construct patches of varying sizes and forms using different algorithms and generators, effectively mimicking the dynamic process of urban expansion. This versatile model holds immense potential for applications in decision support, land resource management, urban planning, and land use planning. Whether you are a researcher, urban planner, or decision-maker, MUSE empowers you to explore and understand the complexities of urban growth, contributing valuable insights to the fiel

# 2. Operation Environment

| Items               | System Requirements                                      |
|---------------------|-----------------------------------------------------------|
| Operating System    | Windows 10 and above                                     |
| CPU                 | Intel® Core™ i5 7th generation or newer / AMD Ryzen™ 5 2nd generation or newer |
| Memory              | 8GB of RAM or more                                       |
| Storage Space       | At least 10GB of available space                         |
| Software Environment | ArcGIS Pro 2.7 or later                                   |

# 3. Data Preparation

To set up MUSE Toolbox, navigate to the installation directory, where the example files are stored. This directory contains 9 essential files, including 4 CSV files and 5 TIFF files, crucial for MUSE's operation. Data preparation techniques using these sample files are detailed in the documentation.

## 2.1 CSV Documents

### 2.1.1 Stepwise Demand of Urban Development

- **File**: [\_05_StepwiseIncreasment.csv](_TEST_FILES/_05_StepwiseIncreasment.csv)
- **Description**: Records yearly rise in the number of urban land grid cells and the proportion of organic patches from 2005 to 2015.

### 2.1.2 History Patch Size Controller Data

- **File**: [\_09_History_CellSize.csv](_TEST_FILES/_09_History_CellSize.csv)
- **Description**: Records 5000 patch sizes in historical periods.

### 2.1.3 Gaussian Correction Parameter Data

- **File**: [\_08_GaussianParams.csv](_TEST_FILES/_08_GaussianParams.csv)
- **Description**: Documents mean parameter 'b' and standard deviation parameter 'c' for Gaussian correction from 2005 to 2015.

### 2.1.4 Stepwise Percent of Organic Growth Data

- **File**: [\_06_StepwiseOrganic.csv](_TEST_FILES/_06_StepwiseOrganic.csv)
- **Description**: Documents area ratios of newly added organic patches from 2005 to 2015.

Feel free to refer to the documentation for detailed information on data preparation and utilization in MUSE.

# 3. Data Preparation

To ensure the proper operation of the MUSE program, users are required to provide 5 TIF files containing specific spatial data crucial for model execution. These files cover essential information such as the distribution of urban construction land at the base and model validation simulation sites, probability of urban construction appropriateness, urban development construction constraints, and urban center point data. It is imperative that these files maintain rigorous consistency in spatial features, including the same number of rows and columns, projection coordinates, and spatial resolution. Refer to Figure 3-6 for an example file.

![Figure 2-1: Model Input Data Files](https://github.com/Mr-ShiRui/MUSE/blob/master/resources/doc/2-1%20Model%20Input%20Data%20Files.png)

## 2.2 TIF Files Overview

### 2.2.1. Base Period Urban Construction Land Data
- **Function**: Describes the spatial distribution of urban construction land during the baseline period. 
- **Format**: Values are denoted by 0 and 1, where 0 signifies undeveloped land and 1 represents developed urban areas.
- **File Name**: [_01_UrbanLand2005_Changsha.tif](_TEST_FILES/_01_UrbanLand2005_Changsha.tif)

### 2.2.2. Model Validation Simulation Urban Construction Land Data
- **Function**: Reflects the urban construction land distribution at the validation simulation point.
- **Format**: Similar to the base period data, values range from 0 to 1, representing undeveloped and developed land.
- **File Name**: [_02_UrbanLand2015_Changsha.tif](_TEST_FILES/_02_UrbanLand2015_Changsha.tif)

### 2.2.3. Urban Construction Suitability Probability File
- **Function**: Represents the probability of urban construction suitability based on diverse driving factor data.
- **Format**: Values range from 0 to 1, where higher values indicate higher suitability for urban development.
- **File Name**: [_04_UrbanSuitability2005.tif](_TEST_FILES/_04_UrbanSuitability2005.tif)

### 2.2.4. Urban Development Construction Restriction File
- **Function**: Provides information on spatial constraints for urban development, such as water bodies, protected farmland, historical and cultural conservation areas, etc.
- **Format**: Values are expressed as 0 for open development areas and 1 for restricted development areas.
- **File Name**: [_03_Constraints_Water.tif](_TEST_FILES/_03_Constraints_Water.tif)

### 2.2.5. Urban Center Point Data
- **Function**: Specifies the locations of urban center points, typically situated in areas like central business districts (CBD), government institutions, or key city hubs.
- **Format**: Values vary between 0 and 1, with 0 representing non-center grid cells and 1 denoting center grid cells.
- **File Name**: [_07_CityCenter.tif](_TEST_FILES/_07_CityCenter.tif)

Feel free to refer to Table 1 for a quick reference to each model input data file, including data sources, value ranges, and corresponding example files.

# Table 1: List of Model Input Data Files

| File Names                                                  | Data Sources                               | Values Range                                         | Corresponding Example File                     |
|-------------------------------------------------------------|--------------------------------------------|------------------------------------------------------|------------------------------------------------|
| Simulated Base-Year Urban Construction Land Spatial Distribution Data | Remote Sensing Data, Land Survey Data, etc. | 0 (Undeveloped Land), 1 (Developed Land)             | [_01_UrbanLand2005_Changsha.tif](_TEST_FILES/_01_UrbanLand2005_Changsha.tif)  |
| Model Validation Urban Construction Land Spatial Distribution Data | Remote Sensing Data, Land Survey Data, etc. | 0 (Undeveloped Land), 1 (Developed Land)             | [_02_UrbanLand2015_Changsha.tif](_TEST_FILES/_02_UrbanLand2015_Changsha.tif)   |
| Urban Construction Suitability Probability File              | Evaluated based on Driver Factor Data     | 0-1 (Urban Construction Suitability Probability)     | [_04_UrbanSuitability2005.tif](_TEST_FILES/_04_UrbanSuitability2005.tif)     |
| Urban Development and Construction Restriction File         | Set based on Real Conditions and Simulated Scenario Requirements | 0 (Developable Area), 1 (Restricted Development Area) | [_03_Constraints_Water.tif](_TEST_FILES/_03_Constraints_Water.tif)      |
| Urban Center Point Data                                      | Set based on Real Conditions and Simulated Scenario Requirements | 0 (Non-Center Point), 1 (Center Point)               | [_07_CityCenter.tif](_TEST_FILES/_07_CityCenter.tif)              |


