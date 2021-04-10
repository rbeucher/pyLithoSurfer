from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *

class Lit2Sample(APIRequests):

    path = URL_BASE + "/api/literature-2-samples"

    def __init__(self,
                 sampleId: Union[int, np.int16, np.int32, np.int64],
                 literatureId: Union[int, np.int16, np.int32, np.int64],
                 sampleName: str = None,
                 literatureCalcName: str = None,
                 notes: str = None
                 ):

        self.sampleId = convert_int(sampleId)
        self.literatureId = convert_int(literatureId)
        self.notes = str(notes)
        self.sampleName = str(sampleName)
        self.literatureCalcName = str(literatureCalcName)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._id = int(value)

    @property
    def sampleId(self):
        return self._sampleId

    @sampleId.setter
    def sampleId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._sampleId = int(value)
    
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
    def sampleName(self):
        return self._sampleName

    @sampleName.setter
    def sampleName(self, value: str):
        self._sampleName = convert_str(value)
    