from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import pandas as pd
import numpy as np
from .utilities import *


class GeoeventAtAge(APIRequests):
        
    path = URL_BASE+'/api/geo-event-at-ages'

    def __init__(self,
                 age: Union[float, np.float16, np.float32, np.float64] = 0,
                 ageError: Union[float, np.float16, np.float32, np.float64] = 0,
                 errorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 errorTypeName: str = None,
                 geoEventId: Union[int, np.int16, np.int32, np.int64] = 0,
                 geoEventName: str = None,
                 id: Union[int, np.int16, np.int32, np.int64] = 0,
                 shrimpageId: Union[int, np.int16, np.int32, np.int64] = 0,
                ):
        
        self.age = age
        self.ageError = ageError
        self.errorTypeId = errorTypeId
        self.errorTypeName = errorTypeName
        self.geoEventId = geoEventId
        self.geoEventName = geoEventName
        self.id = id
        self.shrimpageId = shrimpageId

    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value: float):
        self._age = convert_float(value)
    
    @property
    def ageError(self):
        return self._ageError

    @ageError.setter
    def ageError(self, value: float):
        self._ageError = convert_float(value)
    
    @property
    def errorTypeId(self):
        return self._errorTypeId

    @errorTypeId.setter
    def errorTypeId(self, value: int):
        self._errorTypeId = int(value)
    
    @property
    def errorTypeName(self):
        return self._errorTypeName

    @errorTypeName.setter
    def errorTypeName(self, value: str):
        self._errorTypeName = convert_str(value)
    
    @property
    def geoEventId(self):
        return self._geoEventId

    @geoEventId.setter
    def geoEventId(self, value: int):
        self._geoEventId = int(value)
    
    @property
    def geoEventName(self):
        return self._geoEventName

    @geoEventName.setter
    def geoEventName(self, value: str):
        self._geoEventName = convert_str(value)
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = int(value)
    
    @property
    def shrimpageId(self):
        return self._shrimpageId

    @shrimpageId.setter
    def shrimpageId(self, value: int):
        self._shrimpageId = int(value)
    
        