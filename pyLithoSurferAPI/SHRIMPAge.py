from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import pandas as pd
import numpy as np
from .utilities import *
from .GeoeventAtAge import GeoeventAtAge
from .Statement import Statement


class SHRIMPAge(APIRequests):
        
    path = URL_BASE+'/api/shrimp-ages'

    def __init__(self,
                 calcName: str = None,
                 id: Union[int, np.int16, np.int32, np.int64] = 0,
                 mswd: Union[float, np.float16, np.float32, np.float64] = 0,
                 numberAnalysesCombined: Union[int, np.int16, np.int32, np.int64] = 0,
                 rmQcTest: str = None,
                 shrimpdataPointId: Union[int, np.int16, np.int32, np.int64] = 0,
                ):
        
        self.calcName = calcName
        self.id = id
        self.mswd = mswd
        self.numberAnalysesCombined = numberAnalysesCombined
        self.rmQcTest = rmQcTest
        self.shrimpdataPointId = shrimpdataPointId

    
    @property
    def calcName(self):
        return self._calcName

    @calcName.setter
    def calcName(self, value: str):
        self._calcName = convert_str(value)
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = int(value)
    
    @property
    def mswd(self):
        return self._mswd

    @mswd.setter
    def mswd(self, value: float):
        self._mswd = convert_float(value)
    
    @property
    def numberAnalysesCombined(self):
        return self._numberAnalysesCombined

    @numberAnalysesCombined.setter
    def numberAnalysesCombined(self, value: int):
        self._numberAnalysesCombined = int(value)
    
    @property
    def rmQcTest(self):
        return self._rmQcTest

    @rmQcTest.setter
    def rmQcTest(self, value: str):
        self._rmQcTest = convert_str(value)
    
    @property
    def shrimpdataPointId(self):
        return self._shrimpdataPointId

    @shrimpdataPointId.setter
    def shrimpdataPointId(self, value: int):
        self._shrimpdataPointId = int(value)


class SHRIMPAgeCRUD(APIRequests):

    path = URL_BASE+'/api/shrimp/shrimp-ages'

    def __init__(self, geoeventAtAge: GeoeventAtAge, statement: Statement, shrimpAge: SHRIMPAge):

        self.geoEventAtAge = geoeventAtAge
        self.statement = statement
        self.shrimpAge = shrimpAge

        self.id = None    

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64, None]):
        self._id = convert_int(value)

    @property
    def geoeventAtAge(self):
        return self._geoeventAtAge

    @geoeventAtAge.setter
    def geoeventAtAge(self, value: GeoeventAtAge):
        self._geoeventAtAge = value
    
    @property
    def statement(self):
        return self._statement

    @statement.setter
    def statement(self, value: Statement):
        self._statement = value
    
    @property
    def shrimpAge(self):
        return self._shrimpAge

    @shrimpAge.setter
    def shrimpAge(self, value: SHRIMPAge):
        self._shrimpAge = value