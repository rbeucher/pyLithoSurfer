from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import pandas as pd
import numpy as np
from .utilities import *


class SHRIMPDataPoint(APIRequests):
        
    path = URL_BASE+'/api/shrimp-data-points'

    def __init__(self,
                age: Union[float, np.float16, np.float32, np.float64],
                ageErrorMax: Union[float, np.float16, np.float32, np.float64],
                ageErrorMin: Union[float, np.float16, np.float32, np.float64],
                mineralId: Union[int, np.int16, np.int32, np.int64],
                errorAgeTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                ageAgeKindProcessId: Union[int, np.int16, np.int32, np.int64] = None,
                ageAverageKindId: Union[int, np.int16, np.int32, np.int64] = 0,
                analyteId: Union[int, np.int16, np.int32, np.int64] = None,
                mountCoating: str = None,
                mountOpticalCharacterisation: str = None,
                mswd: Union[float, np.float16, np.float32, np.float64] = None,
                ngrains: int = None,
                nspots: int = None
                ):
        """Shrimp Data Point

        Args:
            age (Union[float, np.float16, np.float32, np.float64]): Measured Age
            ageErrorMax (Union[float, np.float16, np.float32, np.float64]): Age Error Min
            ageErrorMin (Union[float, np.float16, np.float32, np.float64]): Age Error Max
            mineralId (Union[int, np.int16, np.int32, np.int64]): Mineral Id
            errorAgeTypeId (Union[int, np.int16, np.int32, np.int64], optional): Error Type. Defaults to 0 (unknown).
            ageAgeKindProcessId (Union[int, np.int16, np.int32, np.int64], optional): Process Kind of Age. Defaults to None.
            ageAverageKindId (Union[int, np.int16, np.int32, np.int64], optional): Average Kind of Age. Defaults to 0.
            analyteId (Union[int, np.int16, np.int32, np.int64], optional): Id of the Analyte. Defaults to None.
            mountCoating (str, optional): Description of the mount coating. Defaults to None.
            mountOpticalCharacterisation (str, optional): Description of the mount optical characterisation. Defaults to None.
            mswd (Union[float, np.float16, np.float32, np.float64], optional): Mean Standard Weighted Deviation. Defaults to None.
            ngrains (int, optional): Number of grains analysed. Defaults to None.
            nspots (int, optional): Number of Spot Analysis. Defaults to None.

        Returns:
            SHRIMPDataPoint object.
        """

        self.age = convert_float(age)
        self.ageErrorMin = convert_float(ageErrorMin)
        self.ageErrorMax = convert_float(ageErrorMax)
        self.mineralId = convert_int(mineralId)
        self.errorAgeTypeId = convert_int(errorAgeTypeId)
        self.ageAgeKindProcessId = convert_int(ageAgeKindProcessId)
        self.ageAverageKindId = convert_int(ageAverageKindId)
        self.analyteId = convert_int(analyteId)
        self.mountCoating = convert_str(mountCoating)
        self.mountOpticalCharacterisation = convert_str(mountOpticalCharacterisation)
        self.mswd = convert_float(mswd)
        self.ngrains = convert_int(ngrains)
        self.nspots = convert_int(nspots)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._age = convert_float(value)

    @property
    def ageAverageKindId(self):
        return self._ageAverageKindId

    @ageAverageKindId.setter
    def ageAverageKindId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._ageAverageKindId = convert_int(value)

    @property
    def ageAverageKindName(self):
        return self._ageAverageKindName

    @ageAverageKindName.setter
    def ageAverageKindName(self, value: str):
        self._ageAverageKindName = convert_str(value)
    
    @property
    def ageKindProcessId(self):
        return self._ageKindProcessId

    @ageKindProcessId.setter
    def ageKindProcessId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._ageKindProcessId = convert_int(value)

    @property
    def ageKindProcessName(self):
        return self._ageKindProcessName

    @ageKindProcessName.setter
    def ageKindProcessName(self, value: str):
        self._ageKindProcessName = convert_str(value)

    @property
    def ageErrorMax(self):
        return self._ageErrorMax

    @ageErrorMax.setter
    def ageErrorMax(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._ageErrorMax = convert_float(value)

    @property
    def ageErrorMin(self):
        return self._ageErrorMin

    @ageErrorMin.setter
    def ageErrorMin(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._ageErrorMin = convert_float(value)

    @property
    def analyteId(self):
        return self._analyteId

    @analyteId.setter
    def analyteId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._analyteId = convert_int(value)

    @property
    def analyteName(self):
        return self._analyteName

    @analyteName.setter
    def analyteName(self, value: str):
        self._analyteName = convert_str(value)

    @property
    def errorAgeTypeId(self):
        return self._errorAgeTypeId

    @errorAgeTypeId.setter
    def errorAgeTypeId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._errorAgeTypeId = convert_int(value)

    @property
    def errorAgeTypeName(self):
        return self._errorAgeTypeName

    @errorAgeTypeName.setter
    def errorAgeTypeName(self, value: str):
        self._errorAgeTypeName = convert_str(value)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._id = convert_int(value)

    @property
    def mineralId(self):
        return self._mineralId

    @mineralId.setter
    def mineralId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._mineralId = convert_int(value)

    @property
    def mineralName(self):
        return self._mineralName

    @mineralName.setter
    def mineralName(self, value: str):
        self._mineralName = convert_str(value)

    @property
    def ngrains(self):
        return self._ngrains

    @ngrains.setter
    def ngrains(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._ngrains = convert_int(value)

    @property
    def nspots(self):
        return self._nspots

    @nspots.setter
    def nspots(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._nspots = convert_int(value)

    @property
    def singleGrainId(self):
        return self._singleGrainId

    @singleGrainId.setter
    def singleGrainId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._singleGrainId = convert_int(value)

    @property
    def singleGrainName(self):
        return self._singleGrainName

    @singleGrainName.setter
    def singleGrainName(self, value: str):
        self._singleGrainName = convert_str(value)

    @property
    def mountCoating(self):
        return self._mountCoating

    @mountCoating.setter
    def mountCoating(self, value: str):
        self._mountCoating = convert_str(value)
    
    @property
    def mountOpticalCharacterisation(self):
        return self._mountOpticalCharacterisation

    @mountOpticalCharacterisation.setter
    def mountOpticalCharacterisation(self, value: str):
        self._mountOpticalCharacterisation = convert_str(value)
    
    @property
    def mswd(self):
        return self._mswd

    @mswd.setter
    def mswd(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._mswd = convert_float(value)