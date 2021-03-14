from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import pandas as pd
import numpy as np
from .utilities import *
from .dataPoint import DataPoint



class SHRIMPDataPoint(APIRequests):
        
    path = URL_BASE+'/api/shrimp-data-points'

    def __init__(self,
                 calibrationExponent: Union[float, np.float16, np.float32, np.float64] = 0,
                 commonPbModel: str = None,
                 confInterval95Pct: Union[float, np.float16, np.float32, np.float64] = 0,
                 dataDescription: str = None,
                 dataReductionSoftwareVersion: str = None,
                 exponentType: str = None,
                 i206Pb238UCalibrationUncIncl: bool = True,
                 i206Pb238UCalibrationUncertainty: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238UReproducabilityUncertainty: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238UReproducabilityUncertaintyIncl: bool = True,
                 i235UDecayConstant: Union[float, np.float16, np.float32, np.float64] = 0,
                 i238U235U: Union[float, np.float16, np.float32, np.float64] = 0,
                 i238UDecayConstant: Union[float, np.float16, np.float32, np.float64] = 0,
                 iMFCorrApplied: bool = True,
                 id: Union[int, np.int16, np.int32, np.int64] = 0,
                 instrumentalMassFractionationIMFFactor: Union[float, np.float16, np.float32, np.float64] = 0,
                 machineId: Union[int, np.int16, np.int32, np.int64] = 0,
                 machineName: str = None,
                 mountCoating: str = None,
                 mountIGSN: str = None,
                 mountIdentifier: str = None,
                 mountImagingCharacterisation: str = None,
                 mountInfo: str = None,
                 refMaterialId: Union[int, np.int16, np.int32, np.int64] = 0,
                 refMaterialName: str = None,
                ):
        
        self.calibrationExponent = calibrationExponent
        self.commonPbModel = commonPbModel
        self.confInterval95Pct = confInterval95Pct
        self.dataDescription = dataDescription
        self.dataReductionSoftwareVersion = dataReductionSoftwareVersion
        self.exponentType = exponentType
        self.i206Pb238UCalibrationUncIncl = i206Pb238UCalibrationUncIncl
        self.i206Pb238UCalibrationUncertainty = i206Pb238UCalibrationUncertainty
        self.i206Pb238UReproducabilityUncertainty = i206Pb238UReproducabilityUncertainty
        self.i206Pb238UReproducabilityUncertaintyIncl = i206Pb238UReproducabilityUncertaintyIncl
        self.i235UDecayConstant = i235UDecayConstant
        self.i238U235U = i238U235U
        self.i238UDecayConstant = i238UDecayConstant
        self.iMFCorrApplied = iMFCorrApplied
        self.id = id
        self.instrumentalMassFractionationIMFFactor = instrumentalMassFractionationIMFFactor
        self.machineId = machineId
        self.machineName = machineName
        self.mountCoating = mountCoating
        self.mountIGSN = mountIGSN
        self.mountIdentifier = mountIdentifier
        self.mountImagingCharacterisation = mountImagingCharacterisation
        self.mountInfo = mountInfo
        self.refMaterialId = refMaterialId
        self.refMaterialName = refMaterialName

    
    @property
    def calibrationExponent(self):
        return self._calibrationExponent

    @calibrationExponent.setter
    def calibrationExponent(self, value: float):
        self._calibrationExponent = convert_float(value)
    
    @property
    def commonPbModel(self):
        return self._commonPbModel

    @commonPbModel.setter
    def commonPbModel(self, value: str):
        self._commonPbModel = convert_str(value)
    
    @property
    def confInterval95Pct(self):
        return self._confInterval95Pct

    @confInterval95Pct.setter
    def confInterval95Pct(self, value: float):
        self._confInterval95Pct = convert_float(value)
    
    @property
    def dataDescription(self):
        return self._dataDescription

    @dataDescription.setter
    def dataDescription(self, value: str):
        self._dataDescription = convert_str(value)
    
    @property
    def dataReductionSoftwareVersion(self):
        return self._dataReductionSoftwareVersion

    @dataReductionSoftwareVersion.setter
    def dataReductionSoftwareVersion(self, value: str):
        self._dataReductionSoftwareVersion = convert_str(value)
    
    @property
    def exponentType(self):
        return self._exponentType

    @exponentType.setter
    def exponentType(self, value: str):
        self._exponentType = convert_str(value)
    
    @property
    def i206Pb238UCalibrationUncIncl(self):
        return self._i206Pb238UCalibrationUncIncl

    @i206Pb238UCalibrationUncIncl.setter
    def i206Pb238UCalibrationUncIncl(self, value: bool):
        self._i206Pb238UCalibrationUncIncl = value
    
    @property
    def i206Pb238UCalibrationUncertainty(self):
        return self._i206Pb238UCalibrationUncertainty

    @i206Pb238UCalibrationUncertainty.setter
    def i206Pb238UCalibrationUncertainty(self, value: float):
        self._i206Pb238UCalibrationUncertainty = convert_float(value)
    
    @property
    def i206Pb238UReproducabilityUncertainty(self):
        return self._i206Pb238UReproducabilityUncertainty

    @i206Pb238UReproducabilityUncertainty.setter
    def i206Pb238UReproducabilityUncertainty(self, value: float):
        self._i206Pb238UReproducabilityUncertainty = convert_float(value)
    
    @property
    def i206Pb238UReproducabilityUncertaintyIncl(self):
        return self._i206Pb238UReproducabilityUncertaintyIncl

    @i206Pb238UReproducabilityUncertaintyIncl.setter
    def i206Pb238UReproducabilityUncertaintyIncl(self, value: bool):
        self._i206Pb238UReproducabilityUncertaintyIncl = value
    
    @property
    def i235UDecayConstant(self):
        return self._i235UDecayConstant

    @i235UDecayConstant.setter
    def i235UDecayConstant(self, value: float):
        self._i235UDecayConstant = convert_float(value)
    
    @property
    def i238U235U(self):
        return self._i238U235U

    @i238U235U.setter
    def i238U235U(self, value: float):
        self._i238U235U = convert_float(value)
    
    @property
    def i238UDecayConstant(self):
        return self._i238UDecayConstant

    @i238UDecayConstant.setter
    def i238UDecayConstant(self, value: float):
        self._i238UDecayConstant = convert_float(value)
    
    @property
    def iMFCorrApplied(self):
        return self._iMFCorrApplied

    @iMFCorrApplied.setter
    def iMFCorrApplied(self, value: bool):
        self._iMFCorrApplied = value
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = int(value)
    
    @property
    def instrumentalMassFractionationIMFFactor(self):
        return self._instrumentalMassFractionationIMFFactor

    @instrumentalMassFractionationIMFFactor.setter
    def instrumentalMassFractionationIMFFactor(self, value: float):
        self._instrumentalMassFractionationIMFFactor = convert_float(value)
    
    @property
    def machineId(self):
        return self._machineId

    @machineId.setter
    def machineId(self, value: int):
        self._machineId = int(value)
    
    @property
    def machineName(self):
        return self._machineName

    @machineName.setter
    def machineName(self, value: str):
        self._machineName = convert_str(value)
    
    @property
    def mountCoating(self):
        return self._mountCoating

    @mountCoating.setter
    def mountCoating(self, value: str):
        self._mountCoating = convert_str(value)
    
    @property
    def mountIGSN(self):
        return self._mountIGSN

    @mountIGSN.setter
    def mountIGSN(self, value: str):
        self._mountIGSN = convert_str(value)
    
    @property
    def mountIdentifier(self):
        return self._mountIdentifier

    @mountIdentifier.setter
    def mountIdentifier(self, value: str):
        self._mountIdentifier = convert_str(value)
    
    @property
    def mountImagingCharacterisation(self):
        return self._mountImagingCharacterisation

    @mountImagingCharacterisation.setter
    def mountImagingCharacterisation(self, value: str):
        self._mountImagingCharacterisation = convert_str(value)
    
    @property
    def mountInfo(self):
        return self._mountInfo

    @mountInfo.setter
    def mountInfo(self, value: str):
        self._mountInfo = convert_str(value)
    
    @property
    def refMaterialId(self):
        return self._refMaterialId

    @refMaterialId.setter
    def refMaterialId(self, value: int):
        self._refMaterialId = int(value)
    
    @property
    def refMaterialName(self):
        return self._refMaterialName

    @refMaterialName.setter
    def refMaterialName(self, value: str):
        self._refMaterialName = convert_str(value)
    

class SHRIMPDataPointCRUD(APIRequests):

    path = URL_BASE+'/api/shrimp/shrimp-datapoints'

    def __init__(self, dataPoint: DataPoint, dataPointID: int, shrimpDataPoint: SHRIMPDataPoint):

        self.dataPoint = dataPoint
        self.shrimpDataPoint = shrimpDataPoint
        self.dataPointID = datapointID

        self.id = None    

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64, None]):
        self._id = convert_int(value)
    
    @property
    def dataPointID(self):
        return self._dataPointID

    @dataPointID.setter
    def dataPointID(self, value: Union[int, np.int16, np.int32, np.int64, None]):
        self._dataPointID = convert_int(value)

    @property
    def dataPoint(self):
        return self._dataPoint

    @dataPoint.setter
    def dataPoint(self, value: DataPoint):
        self._dataPoint = value
    
    @property
    def shrimpDataPOint(self):
        return self._shrimpDataPOint

    @shrimpDataPOint.setter
    def shrimpDataPOint(self, value: SHRIMPDataPoint):
        self._shrimpDataPOint = value
    