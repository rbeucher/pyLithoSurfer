from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *

class Lab2Data(APIRequests):

    path = URL_BASE + "/api/lab-2-data-points"

    def __init__(self,
                 dataPointId: Union[int, np.int16, np.int32, np.int64],
                 labId: Union[int, np.int16, np.int32, np.int64],
                 dataPointName: str = None,
                 labName: str = None,
                 notes: str = None
                 ):

        self.dataPointId = convert_int(dataPointId)
        self.labId = convert_int(labId)
        self.notes = str(notes)
        self.dataPointName = str(dataPointName)
        self.labName = str(labName)

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
    def labId(self):
        return self._labId

    @labId.setter
    def labId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._labId = int(value)

    @property
    def labName(self):
        return self._labName

    @labName.setter
    def labName(self, value: str):
        self._labName = convert_str(value)
    
    @property
    def dataPointName(self):
        return self._dataPointName

    @dataPointName.setter
    def dataPointName(self, value: str):
        self._dataPointName = convert_str(value)
    