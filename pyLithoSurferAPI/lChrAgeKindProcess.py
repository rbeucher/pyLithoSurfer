from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class lChrAgeKindProcess(APIRequests):

    path = URL_BASE + "/api/l-chr-age-kind-processes"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def ageKindProcess(self):
        return self._ageKindProcess

    @ageKindProcess.setter
    def ageKindProcess(self, value):
        self._ageKindProcess = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

