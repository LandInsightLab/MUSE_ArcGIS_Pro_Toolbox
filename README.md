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



