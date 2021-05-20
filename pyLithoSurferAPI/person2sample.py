from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *

class Person2Sample(APIRequests):

    path = URL_BASE + "/api/core/person-2-samples"

    def __init__(self,
                 dataPointId: Union[int, np.int16, np.int32, np.int64],
                 personId: Union[int, np.int16, np.int32, np.int64],
                 dataPointName: str = None,
                 personCalcName: str = None,
                 notes: str = None,
                 roleId: Union[int, np.int16, np.int32, np.int64] = None,
                 roleName: str = None
                 ):

        self.dataPointId = convert_int(dataPointId)
        self.personId = convert_int(personId)
        self.notes = convert_str(notes)
        self.dataPointName = convert_str(dataPointName)
        self.personCalcName = convert_str(personCalcName)
        self.roleId = convert_int(roleId)
        self.roleName = convert_str(roleName)

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
    def personId(self):
        return self._personId

    @personId.setter
    def personId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._personId = int(value)

    @property
    def personCalcName(self):
        return self._personCalcName

    @personCalcName.setter
    def personCalcName(self, value: str):
        self._personCalcName = convert_str(value)
    
    @property
    def dataPointName(self):
        return self._dataPointName

    @dataPointName.setter
    def dataPointName(self, value: str):
        self._dataPointName = convert_str(value)
    
    @property
    def roleId(self):
        return self._roleId

    @roleId.setter
    def roleId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._roleId = int(value)
    
    @property
    def roleName(self):
        return self._roleName

    @roleName.setter
    def roleName(self, value: str):
        self._roleName = convert_str(value)