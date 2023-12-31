<p align="center">
  <img width="180" src="./resources/LOGO/MUSE_LOGO2.png" alt="MUSE_LOGO">
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

## 3.1 CSV Documents

### 3.1.1 Stepwise Demand of Urban Development

- **File**: [_05_StepwiseIncreasment.csv](_TEST_FILES/_05_StepwiseIncreasment.csv)
- **Description**: Records yearly rise in the number of urban land grid cells and the proportion of organic patches from 2005 to 2015.

### 3.1.2 History Patch Size Controller Data

- **File**: [_09_History_CellSize.csv](_TEST_FILES/_09_History_CellSize.csv)
- **Description**: Records 5000 patch sizes in historical periods.

### 3.1.3 Gaussian Correction Parameter Data

- **File**: [_08_GaussianParams.csv](_TEST_FILES/_08_GaussianParams.csv)
- **Description**: Documents mean parameter 'b' and standard deviation parameter 'c' for Gaussian correction from 2005 to 2015.

### 3.1.4 Stepwise Percent of Organic Growth Data

- **File**: [_06_StepwiseOrganic.csv](_TEST_FILES/_06_StepwiseOrganic.csv)
- **Description**: Documents area ratios of newly added organic patches from 2005 to 2015.

Feel free to refer to the documentation for detailed information on data preparation and utilization in MUSE.

## 3.2 TIF Files

To ensure the proper operation of the MUSE program, users are required to provide 5 TIF files containing specific spatial data crucial for model execution. These files cover essential information such as the distribution of urban construction land at the base and model validation simulation sites, probability of urban construction appropriateness, urban development construction constraints, and urban center point data. It is imperative that these files maintain rigorous consistency in spatial features, including the same number of rows and columns, projection coordinates, and spatial resolution. Refer to Figure 3-6 for an example file.

![Figure 2-1: Model Input Data Files](https://github.com/Mr-ShiRui/MUSE/blob/master/resources/doc/2-1%20Model%20Input%20Data%20Files.png)

### 3.2.1. Base Period Urban Construction Land Data
- **Function**: Describes the spatial distribution of urban construction land during the baseline period. 
- **Format**: Values are denoted by 0 and 1, where 0 signifies undeveloped land and 1 represents developed urban areas.
- **File Name**: [_01_UrbanLand2005_Changsha.tif](_TEST_FILES/_01_UrbanLand2005_Changsha.tif)

### 3.2.2. Model Validation Simulation Urban Construction Land Data
- **Function**: Reflects the urban construction land distribution at the validation simulation point.
- **Format**: Similar to the base period data, values range from 0 to 1, representing undeveloped and developed land.
- **File Name**: [_02_UrbanLand2015_Changsha.tif](_TEST_FILES/_02_UrbanLand2015_Changsha.tif)

### 3.2.3. Urban Construction Suitability Probability File
- **Function**: Represents the probability of urban construction suitability based on diverse driving factor data.
- **Format**: Values range from 0 to 1, where higher values indicate higher suitability for urban development.
- **File Name**: [_04_UrbanSuitability2005.tif](_TEST_FILES/_04_UrbanSuitability2005.tif)

### 3.2.4. Urban Development Construction Restriction File
- **Function**: Provides information on spatial constraints for urban development, such as water bodies, protected farmland, historical and cultural conservation areas, etc.
- **Format**: Values are expressed as 0 for open development areas and 1 for restricted development areas.
- **File Name**: [_03_Constraints_Water.tif](_TEST_FILES/_03_Constraints_Water.tif)

### 3.2.5. Urban Center Point Data
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

# User Guide for MUSE Toolbox

## 4. Toolbox Installation

### 4.1 Acquiring and Installing MUSE Toolbox

   1. Acquire the Python version of ArcGIS Pro by retrieving and extracting the compressed MUSE toolbox file to a designated directory.
   2. In ArcGIS Pro interface, navigate through the “Project” and “Package Manager” tabs, select “python” to ascertain the current Python version (e.g., Python 3.9.11).
   ![Figure 4-1 ArcGIS Pro python version](https://github.com/Mr-ShiRui/MUSE_ArcGIS_Pro_Toolbox/blob/master/resources/doc/4-1%20ArcGIS%20Pro%20python%20version.png)
   3. Replace the corresponding MUSE_CMD file for the Python version in the “MUSE_CMD” folder. Delete the original version to retain only one MUSE_CMD file. Ensure the “MUSE_Backend” directory is in the same root directory as the MUSE_Script.py script file.
   ![Figure 4-2 Replace the MUSE_CMD file](https://github.com/Mr-ShiRui/MUSE_ArcGIS_Pro_Toolbox/blob/master/resources/doc/4-2%20Replace%20the%20MUSE_CMD%20file.png)
   4. Import the toolbox in ArcGIS Pro by locating “Project” > “Toolboxes,” right-clicking, selecting “Add Toolbox,” and navigating to the directory where the MUSE toolbox is saved. Open the “MUSE.tbx” file and click “OK.”
   ![Figure 4-3 Add toolbox](https://github.com/Mr-ShiRui/MUSE_ArcGIS_Pro_Toolbox/blob/master/resources/doc/4-3%20Add%20toolbox.png)

## 4.2 Running the Toolbox

   1. Double-click on the “MUSE_CH” tool to initiate the MUSE toolbox’s primary interface.
   ![Figure 4-4 The main interface of MUSE toolbox](https://github.com/Mr-ShiRui/MUSE_ArcGIS_Pro_Toolbox/blob/master/resources/doc/4-4%20The%20main%20interface%20of%20MUSE%20toolbox.png)
   2. Select the mode (model validation or scenario prediction) and proceed with data input and parameterization.
   - In model validation mode, provide six data elements and configure Gaussian adjustment parameters.
   - In scenario prediction mode, input data as needed for future predictions.
   
### 4.2.1 Model Validation

#### (1) Data Input

   Sequentially input the required data for the MUSE tool into the first six file input fields. The relationships between the necessary input data and example files in the _TEST_FILES folder are detailed in the following table.
  
   | Parameters Name                           | File Types                                     | Example Files                           |
   |-------------------------------------------|------------------------------------------------|-----------------------------------------|
   | Urban land use map of starting time        | Base-year Urban Construction Land Data          | [_01_UrbanLand2005_Changsha.tif](_TEST_FILES/_01_UrbanLand2005_Changsha.tif)           |
   | Urban land use map if ending time          | Target-year Urban Construction Land Data        | [_02_UrbanLand2015_Changsha.tif](_TEST_FILES/_02_UrbanLand2015_Changsha.tif)         |
   | Spatial Constraints                        | Urban Development Restriction File             |  [_03_Constraints_Water.tif](_TEST_FILES/_03_Constraints_Water.tif)                |
   | Urban development suitability             | Urban Construction Suitability Probability File| [_04_UrbanSuitability2005.tif](_TEST_FILES/_04_UrbanSuitability2005.tif)            |
   | Stepwise demand of urban development      | Urban Construction Land Increment               | [_05_StepwiseIncreasment.csv](_TEST_FILES/_05_StepwiseIncreasment.csv)             |
   | Stepwise percent of organic growth         | Patch organic growth category proportion data  | [_06_StepwiseOrganic.csv](_TEST_FILES/_06_StepwiseOrganic.csv)                |


#### (2). Expansion Extent Control

   Manage expansion extent by deciding to deploy the Gaussian adjustment control module. If selected, confirm the choice as "Yes" in the dropdown box. Input data systematically for city center points, Gaussian correction parameters, and the Gaussian function weight (constrained between 0 and 1). For a detailed understanding, refer to Section 5.2. The corresponding interface for this module is shown in the following figure.

   ![Figure 4-5 Parameter input interface of expansion degree control module](https://github.com/Mr-ShiRui/MUSE_ArcGIS_Pro_Toolbox/blob/master/resources/doc/4-5%20Parameter%20input%20interface%20of%20expansion%20degree%20control%20module.png)

   | Parameters Name | File Types | Example Files |
   |------------------|------------|---------------|
   | Urban Center | City center raster data | _07_CityCenter.tif |
   | Gaussian Parameters | Parameters data based on Gaussian correction rule | _08_GaussianParams.tif |

#### 3. Input of Global Parameters

   In configuring global parameters, five crucial parameters need precise settings. Pay special attention to the total duration of the simulation period, ensuring it does not exceed the temporal span in the urban construction land increment data. The designated time span parameter is determined by subtracting one from the total number of rows in the increment data. For example, if the data encompasses 11 rows, spanning incremental information from 2006 to 2015, the time span parameter is 10 years. When configuring the simulation period length, the value should be less than or equal to 10 years, ensuring the disparity between simulation end and start does not exceed this limit. The significance and allowable ranges for each parameter in the global parameter section are detailed in the following table:

   | Parameters Name      | Parameters Description                                                                 | Value Range     |
   |-----------------------|------------------------------------------------------------------------------------------|-----------------|
   | Starting time         | Starting step of the model simulation                                                    | 1~36767         |
   | Ending time           | Ending step of the model simulation                                                      | 1~36767         |
   | Location uncertainty  | Proportion of non-randomly selected seeds in the seed selection process for patches       | 0~1             |
   | Pruning parameter     | The size of the patch seed unit library is equal to the total number of developable grid units sorted in descending order based on development probability, multiplied by a pruning coefficient. | 0~1             |
   | Type of neighborhood  | In the context of 4-neighborhood, it corresponds to the Von Neumann neighborhood, while in the case of 8-neighborhood, it corresponds to the Moore neighborhood. | 4, 8            |


### (4) Selection of Patch Size Generator

   Choose from three available patch size generators in MUSE:

   - **Lognormal Distribution:** Utilizes a lognormal distribution random generator, requiring parameters like mean and log standard deviation.
   - **Power-law Distribution:** Relies on a power-law distribution random generator, requiring parameters like scaling constant and exponent.
   - **Historical Period Patch Sizes:** Select this option if you have a custom CSV document with detailed patch size specifications .

### (5) Selection of Patch Generation Engine

   MUSE provides four algorithmic engines for patch generation. Notably, selecting the neighborhood control patch generation engine configures the patch position uncertainty parameter to 1 and the neighborhood type parameter to 8. This adjustment is due to the reliance on stochastic processes and iterative neighborhood mechanisms inherent in this engine.

   For detailed parameters associated with each engine, refer to the following table:

   | Engines Name | Parameters Name | Parameters Description                                                | Default Value | Value Range      |
   |--------------|-----------------|-------------------------------------------------------------------------|---------------|------------------|
   | SPGE         | -               | This engine does not require any input parameters.                      | -             | -                |
   | PPGE         | N               | N and D together influence the longest dimension of the plaque         | 1             | Greater than 0    |
   |              | D               | -                                                                       | 2             | Greater than 0    |
   |              | A               | The number of arms                                                      | 2             | Not less than 0   |
   |              | O               | Patch orientation                                                      | 45            | Not less than 0   |
   |              | suit_weight     | The weight of the patch shape during the generation process            | 0.5           | 0-1              |
   |              | shape_weight    | The weight of suitability during the generation process                 | 0.5           | 0-1              |
   | Nei-PGE      | beta            | Whether neighborhood repetition based on seed units controls the compactness of the patch | 1.6 | Greater than 0    |
   | Dis-PGE      | delta           | Control of patch shape based on a distance decay mechanism               | 2             | Any real number  |
  
#### (6) Output Location Selection

   When selecting output results, provide a filename for result preservation. You have the choice to append a file extension, e.g., "Exp_CS.tif," or input "Exp_CS" directly, letting the model complete the filename. See Figure 4-6 for an example of model parameter configurations.
   ![Figure 4-6 Example model parameter settings](https://github.com/Mr-ShiRui/MUSE_ArcGIS_Pro_Toolbox/blob/master/resources/doc/4-6%20Example%20model%20parameter%20settings.png)
#### (7) Examination of Simulation Results

   After the simulation concludes, the resultant files are saved in the specified directory. Access relevant information by choosing "View Details." In Figure 4-7, performance metrics like Kappa, FoM (Figure of Merit), and OA (Operational Accuracy) are available. The last line provides insight into the temporal duration of the model's execution.

   Note: In the example, a warning appears due to incongruities in row and column numbers between the restricted file and other dataset files. The model issues a warning when the difference is within 5; exceeding this threshold results in an error, prompting the model to stop. Pay careful attention to spatial consistency in simulated data during the data preparation phase to prevent such warnings and errors.
   ![Figure 4-7 Simulation output](https://github.com/Mr-ShiRui/MUSE_ArcGIS_Pro_Toolbox/blob/master/resources/doc/4-7%20Simulation%20output.png)
  

### 4.2.2 Scenario Simulation

   Initiate scenario prediction mode for simulating future urban construction land distributions. No input of urban land data for the simulation end period is required.

   ![Figure 4-8 Scenario Simulation Interface](https://github.com/Mr-ShiRui/MUSE_ArcGIS_Pro_Toolbox/blob/master/resources/doc/4-8%20Scenario%20Simulation%20Interface.png)

## 4.3 Explanation of Simulation Results

   After completing the simulation, examine the results with pixel values ranging from 0 to n. In the symbol system of ArcGIS software, utilizing a unique value display method, these pixel values appear sequentially as 0, 1, i…n. Here, i represents the value designated at the beginning of the simulation, incremented by 1, and n is the value defined at the simulation's conclusion. This configuration provides a clear depiction of the spatial arrangement of newly allocated urban construction land at each temporal interval.

   ![Figure 4-9 Simulation results of urban construction land in Changsha from 2005 to 2015](https://github.com/Mr-ShiRui/MUSE_ArcGIS_Pro_Toolbox/blob/master/resources/doc/4-9%20Simulation%20results%20of%20urban%20construction%20land%20in%20Changsha%20from%202005%20to%202015.png)

