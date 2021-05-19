from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *

class Lit2Data(APIRequests):

    path = URL_BASE + "/api/core/literature-2-data-points"

    def __init__(self,
                 dataPointId: Union[int, np.int16, np.int32, np.int64],
                 literatureId: Union[int, np.int16, np.int32, np.int64],
                 dataPointName: str = None,
                 literatureCalcName: str = None,
                 notes: str = None
                 ):

        self.dataPointId = convert_int(dataPointId)
        self.literatureId = convert_int(literatureId)
        self.notes = str(notes)
        self.dataPointName = str(dataPointName)
        self.literatureCalcName = str(literatureCalcName)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._id = int(value)

    @property
    def dataPointId(self):
        return self._dataPointId

    @dataPointId.setter
    def dataPointId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._dataPointId = int(value)
    
    @property
    def literatureId(self):
        return self._literatureId

    @literatureId.setter
    def literatureId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._literatureId = int(value)

    @property
    def literatureCalcName(self):
        return self._literatureCalcName

    @literatureCalcName.setter
    def literatureCalcName(self, value: str):
        self._literatureCalcName = convert_str(value)
    
    @property
    def dataPointName(self):
        return self._dataPointName

    @dataPointName.setter
    def dataPointName(self, value: str):
        self._dataPointName = convert_str(value)
    