from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import pandas as pd
import numpy as np
from .utilities import *


class DataPackage2Supervisor(APIRequests):
        
    path = URL_BASE+'/api/management/data-package-2-supervisors'

    def __init__(self,
                 dataPackageId: Union[int, np.int16, np.int32, np.int64] = 0,
                 dataPackageName: str = None,
                 id: Union[int, np.int16, np.int32, np.int64] = 0,
                 lithoUserId: Union[int, np.int16, np.int32, np.int64] = 0,
                ):
        
        self.dataPackageId = dataPackageId
        self.dataPackageName = dataPackageName
        self.id = id
        self.lithoUserId = lithoUserId

    
    @property
    def dataPackageId(self):
        return self._dataPackageId

    @dataPackageId.setter
    def dataPackageId(self, value: int):
        self._dataPackageId = int(value)
    
    @property
    def dataPackageName(self):
        return self._dataPackageName

    @dataPackageName.setter
    def dataPackageName(self, value: str):
        self._dataPackageName = convert_str(value)
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = int(value)
    
    @property
    def lithoUserId(self):
        return self._lithoUserId

    @lithoUserId.setter
    def lithoUserId(self, value: int):
        self._lithoUserId = int(value)
    
        