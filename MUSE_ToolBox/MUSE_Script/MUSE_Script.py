# -*- coding: utf-8 -*-
import arcpy
import csv
import os
from MUSE_Backend import MUSE_CMD


class ErrorInformation:
    def __init__(self):
        self.error_00 = "There is an error in the parameter receiving process"
        self.error_01 = "The rasters data is empty."
        self.error_02 = "The validation data is empty, please check whether the path of the urban land file at the" \
                        " end of the simulation is correct."
        self.error_03 = "The Gaussian parameter is empty. Please check the Gaussian parameter input file"
        self.error_04 = "City Center not found, please check City Center file"
        self.error_05 = "The simulation total step set in the model parameters is larger than the total step set" \
                        " in the stepwise demand of urban developemnt file"
        self.error_06 = "All the organic patch area ratio parameters in the new patch area file must be between 0" \
                        " and 1, including 0 and 1"
        self.error_07 = "Patch size is less than 0, please enter the appropriate patch size generator parameters"
        self.error_08 = "Too many seed extraction times, please check whether the parameters are set correctly"


class ModelParametersManager:
    def __init__(self):
        # 模拟年份
        self.years = None
        self.valuation = None
        # 存储栅格文件的行列数，用于与其他文件行列数对比
        self.preset_rows = None
        self.preset_cols = None

        self.params = MUSE_CMD.ModelParameters()

        # 设置参数的默认值，如果有的话
        self.params.mode = 0
        self.params.expansionControl = 0
        self.params.cityCenter = ""
        self.params.correctionParameters = ""
        self.params.cityCenterWeight = 0
        self.params.initialUrbanLand = ""
        self.params.finalUrbanLand = ""
        self.params.developmentConstraints = ""
        self.params.urbanSuitability = ""
        self.params.additionalUrbanLandArea = ""
        self.params.additionalUrbanLandOrganic = ""
        self.params.initialNode = 0
        self.params.finalNode = 0
        self.params.uncertainty = 0
        self.params.pruningCoefficient = 0
        self.params.neighborhoodType = 4
        self.params.controllerType = 0
        self.params.lognormalMean = 0
        self.params.lognormalStdDev = 0
        self.params.powerLawConstant = 0
        self.params.powerLawExponent = 0
        self.params.historicalBlockSizes = ""
        self.params.blockEngineType = 0
        self.params.parameterN = 0
        self.params.parameterD = 0
        self.params.parameterA = 0
        self.params.parameterO = 0
        self.params.shapeWeight = 0
        self.params.neighborhoodControlParam = 0
        self.params.distanceControlParam = 0
        self.params.outPut = ""

    def read_grid_dimensions(self, file_path):
        """
        读取栅格文件的行列数，并设置预设值

        参数:
        file_path: 栅格文件的路径
        preset_rows: 预设的行数 (默认为None)
        preset_cols: 预设的列数 (默认为None)
        """
        # 检查文件是否存在
        if not os.path.isfile(file_path):
            arcpy.AddError(f"The file {file_path} does not exist.")
            return False

        # 检查文件扩展名是否为栅格文件格式
        if not file_path.endswith('.tif'):
            arcpy.AddError(f"The file {file_path} is not in raster file format.")
            return False

        raster = arcpy.Raster(file_path)
        self.preset_rows = raster.height
        self.preset_cols = raster.width

        return True

    def check_tif_dimensions(self, file_path):
        # 判断文件是否存在
        if not os.path.isfile(file_path):
            arcpy.AddError(f"The file {file_path} does not exist.")
            return False

            # 判断文件扩展名是否为tif
        if not file_path.endswith('.tif'):
            arcpy.AddError(f"The file {file_path} is not in raster file format.")
            return False

        raster = arcpy.Raster(file_path)
        rows = raster.height
        cols = raster.width

        if rows != self.preset_rows or cols != self.preset_cols:
            if abs(rows - self.preset_rows) <= 5 and abs(cols - self.preset_cols) <= 5:
                arcpy.AddWarning(f"Warning: The row or column numbers of the TIF file {file_path} do not "
                                 f"match the preset values, but the difference is within 5.")
                return True
            else:
                arcpy.AddError(f"Error: The row or column numbers of the TIF file {file_path} do not "
                               f"match the preset values, and the difference exceeds 5.")
                return False
        else:
            arcpy.AddMessage(f"The row and column numbers of the TIF file {file_path} match the preset values.")
            return True

    def analyze_csv(self, file_path, required_rows, required_cols):
        # 判断文件是否存在
        if not os.path.isfile(file_path):
            arcpy.AddError(f"The file {file_path} does not exist.")

            # 判断文件扩展名是否为csv
        if not file_path.endswith('.csv'):
            arcpy.AddError(f"The file {file_path} is not in CSV format.")

        rows = 0
        cols = 0

        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            # 读取第一行来确定列数
            first_row = next(reader, None)
            if first_row:
                cols = len(first_row)
                # 使用迭代器遍历文件，计算行数
                for _ in reader:
                    rows += 1
                # 因为包含了标题行，所以行数需要+1
                rows += 1

        # 检查行数和列数是否满足要求
        if rows > required_rows and cols >= required_cols:
            arcpy.AddMessage(f"The row and column numbers of the file {file_path} meet the requirements.")
            return True
        else:
            arcpy.AddError(f"The row and column numbers of the file {file_path} do not meet the requirements. "
                           f"The required number of rows is {required_rows}, "
                           f"and the required number of columns is {required_cols}.")
            return False

    def set_parameters(
            self,
            _mode=None,
            _initialUrbanLand=None,
            _developmentConstraints=None,
            _finalUrbanLand=None,
            _additionalUrbanLandArea=None,
            _additionalUrbanLandOrganic= None,
            _urbanSuitability=None,
            _initialNode=None,
            _finalNode=None,
            _expansionControl=None,
            _cityCenter=None,
            _correctionParameters=None,
            _cityCenterWeight=None,
            _uncertainty=None,
            _pruningCoefficient=None,
            _neighborhoodType=None,
            _controllerType=None,
            _lognormalMean=None,
            _lognormalStdDev=None,
            _powerLawConstant=None,
            _powerLawExponent=None,
            _historicalBlockSizes=None,
            _blockEngineType=None,
            _parameterN=None,
            _parameterD=None,
            _parameterA=None,
            _parameterO=None,
            _shapeWeight=None,
            _neighborhoodControlParam=None,
            _distanceControlParam=None,
            _outPut=None,
    ):

        if not self.read_grid_dimensions(_initialUrbanLand):
            return False

        self.years = int(_finalNode) - int(_initialNode)

        """使用关键字参数设置参数。"""
        # 模式设置。模型验证模式下，模拟末期城市土地需要输入，否则为空。
        if _mode == "模型验证" or _mode == "Model validation":
            self.params.mode = 0
            self.params.finalUrbanLand = _finalUrbanLand
            if not self.check_tif_dimensions(self.params.finalUrbanLand):
                return False
        else:
            self.params.mode = 1
            self.params.finalUrbanLand = ""

        # 扩张程度控制打开，则需要输入城市中心地址、高斯参数地址、高斯权重
        if _expansionControl == "是" or _expansionControl == "Yes":
            self.params.expansionControl = 1
            self.params.cityCenter = _cityCenter

            if not self.check_tif_dimensions(self.params.cityCenter):
                return False
            self.params.correctionParameters = _correctionParameters
            if not self.analyze_csv(self.params.correctionParameters, self.years, 3):
                return False
            self.params.cityCenterWeight = float(_cityCenterWeight)
        else:
            self.params.expansionControl = 0
            self.params.cityCenter = ""
            self.params.correctionParameters = ""
            self.params.cityCenterWeight = 0

        self.params.initialUrbanLand = _initialUrbanLand

        self.params.developmentConstraints = _developmentConstraints
        if not self.check_tif_dimensions(self.params.developmentConstraints):
            return False

        self.params.urbanSuitability = _urbanSuitability
        if not self.check_tif_dimensions(self.params.urbanSuitability):
            return False

        self.params.additionalUrbanLandArea = _additionalUrbanLandArea
        if not self.analyze_csv(self.params.additionalUrbanLandArea, self.years, 2):
            return False

        self.params.additionalUrbanLandOrganic = _additionalUrbanLandOrganic
        if not self.analyze_csv(self.params.additionalUrbanLandOrganic, self.years, 2):
            return False

        self.params.initialNode = int(_initialNode)
        self.params.finalNode = int(_finalNode)
        self.params.uncertainty = float(_uncertainty)
        self.params.pruningCoefficient = float(_pruningCoefficient)
        self.params.neighborhoodType = int(_neighborhoodType)

        if _controllerType == "对数正态分布" or _controllerType == "Lognormal Distribution":
            self.params.controllerType = 0
            self.params.lognormalMean = float(_lognormalMean)
            self.params.lognormalStdDev = float(_lognormalStdDev)
        elif _controllerType == "幂律分布" or _controllerType == "Power distribution":
            self.params.controllerType = 1
            self.params.powerLawConstant = float(_powerLawConstant)
            self.params.powerLawExponent = float(_powerLawExponent)
        elif _controllerType == "历史时期斑块大小" or _controllerType == "History":
            self.params.controllerType = 2
            self.params.historicalBlockSizes = _historicalBlockSizes
            # 传入1表示行数无限制
            if not self.analyze_csv(self.params.historicalBlockSizes, 0, 2):
                return False
        if _blockEngineType == "简单斑块生成引擎" or _blockEngineType == "SPGE":
            self.params.blockEngineType = 0
        elif _blockEngineType == "参数化斑块生成引擎" or _blockEngineType == "PPGE":
            self.params.blockEngineType = 1
            self.params.parameterN = float(_parameterN)
            self.params.parameterD = float(_parameterD)
            self.params.parameterA = float(_parameterA)
            self.params.parameterO = float(_parameterO)
            self.params.shapeWeight = float(_shapeWeight)
        elif _blockEngineType == "邻域控制斑块生成引擎" or _blockEngineType == "NeiPGE":
            self.params.blockEngineType = 2
            self.params.neighborhoodControlParam = float(_neighborhoodControlParam)
        elif _blockEngineType == "距离控制斑块生成引擎" or _blockEngineType == "DisPGE":
            self.params.blockEngineType = 3
            self.params.distanceControlParam = float(_distanceControlParam)

        if not _outPut.endswith(".tif"):
            self.params.outPut = _outPut + ".tif"
        else:
            self.params.outPut = _outPut
        return True

    def process_parameters(self):
        param_list = []
        num_params = arcpy.GetArgumentCount()
        for i in range(num_params):
            param = arcpy.GetParameterAsText(i)
            param_list.append(param)  # 将参数添加到self.params列表中
        res = self.set_parameters(
            _mode=param_list[0],
            _initialUrbanLand=param_list[1],
            _finalUrbanLand=param_list[2],
            _developmentConstraints=param_list[3],
            _urbanSuitability=param_list[4],
            _additionalUrbanLandArea=param_list[5],
            _additionalUrbanLandOrganic=param_list[6],
            _expansionControl=param_list[7],
            _cityCenter=param_list[8],
            _correctionParameters=param_list[9],
            _cityCenterWeight=param_list[10],
            _initialNode=param_list[11],
            _finalNode=param_list[12],
            _uncertainty=param_list[13],
            _pruningCoefficient=param_list[14],
            _neighborhoodType=param_list[15],
            _controllerType=param_list[16],
            _lognormalMean=param_list[17],
            _lognormalStdDev=param_list[18],
            _powerLawConstant=param_list[19],
            _powerLawExponent=param_list[20],
            _historicalBlockSizes=param_list[21],
            _blockEngineType=param_list[22],
            _parameterN=param_list[23],
            _parameterD=param_list[24],
            _parameterA=param_list[25],
            _parameterO=param_list[26],
            _shapeWeight=param_list[27],
            _neighborhoodControlParam=param_list[29],
            _distanceControlParam=param_list[30],
            _outPut=param_list[31]
        )
        return res

    def run(self):
        try:
            arcpy.SetProgressor("step", "Running MUSE", 0, 5, 1)  # 5个步骤

            run = self.process_parameters()  # 第一个步骤
            arcpy.SetProgressorLabel("Step 1 of 5: Processing parameters")
            arcpy.SetProgressorPosition(1)

            if run:
                error_information = ErrorInformation()
                arcpy.SetProgressorLabel("Step 2 of 5: Running MUSE_CMD.main")
                arcpy.SetProgressorPosition(2)
                success = MUSE_CMD.main(self.params)

                arcpy.SetProgressorLabel("Step 3 of 5: Calculating valuation")
                arcpy.SetProgressorPosition(3)

                if success == 1:
                    self.valuation = MUSE_CMD.valuation()
                    if self.params.mode == 0:
                        arcpy.SetProgressorLabel("Step 4 of 5: Generating message")
                        arcpy.SetProgressorPosition(4)
                        message = f"Kappa:{self.valuation[0]} FoM:{self.valuation[1]} OA:{self.valuation[2]}"
                        arcpy.AddMessage(message)
                elif success == 0:
                    arcpy.AddError(error_information.error_00)
                elif success == -1:
                    arcpy.AddError(error_information.error_01)
                elif success == -2:
                    arcpy.AddError(error_information.error_02)
                elif success == -3:
                    arcpy.AddError(error_information.error_03)
                elif success == -4:
                    arcpy.AddError(error_information.error_04)
                elif success == -5:
                    arcpy.AddError(error_information.error_05)
                elif success == -6:
                    arcpy.AddError(error_information.error_06)
                elif success == -7:
                    arcpy.AddError(error_information.error_07)
                elif success == -8:
                    arcpy.AddError(error_information.error_08)
                arcpy.SetProgressorLabel("Step 5 of 5: Process completed")
                arcpy.SetProgressorPosition(5)
            else:
                arcpy.AddError("Error: Process failed")
        except Exception as e:
            arcpy.AddError(f"Error: {str(e)}")
        finally:
            arcpy.ResetProgressor()


if __name__ == '__main__':
    modelParameters = ModelParametersManager()
    modelParameters.run()
