from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import pandas as pd
import numpy as np
from .utilities import *


class Statement(APIRequests):
        
    path = URL_BASE+'/api/statements'

    def __init__(self,
                 dataPointId: Union[int, np.int16, np.int32, np.int64] = 0,
                 description: str = None,
                 geoEventAtAgeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 id: Union[int, np.int16, np.int32, np.int64] = 0,
                 tempAtAgeId: Union[int, np.int16, np.int32, np.int64, None] = None,
                 tempGradientId: Union[int, np.int16, np.int32, np.int64, None] = None,
                ):
        
        self.dataPointId = dataPointId
        self.description = description
        self.geoEventAtAgeId = geoEventAtAgeId
        self.id = id
        self.tempAtAgeId = tempAtAgeId
        self.tempGradientId = tempGradientId

    
    @property
    def dataPointId(self):
        return self._dataPointId

    @dataPointId.setter
    def dataPointId(self, value: int):
        self._dataPointId = int(value)
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = convert_str(value)
    
    @property
    def geoEventAtAgeId(self):
        return self._geoEventAtAgeId

    @geoEventAtAgeId.setter
    def geoEventAtAgeId(self, value: int):
        self._geoEventAtAgeId = int(value)
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = int(value)
    
    @property
    def tempAtAgeId(self):
        return self._tempAtAgeId

    @tempAtAgeId.setter
    def tempAtAgeId(self, value):
        if value:
            self._tempAtAgeId = value
        else:
            self._tempAtAgeId = None
    
    @property
    def tempGradientId(self):
        return self._tempGradientId

    @tempGradientId.setter
    def tempGradientId(self, value):
        self._tempGradientId = value
    
        