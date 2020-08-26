from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class reOs(APIRequests):

    path = URL_BASE + "/api/re-os"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def chronoId(self):
        return self._chronoId

    @chronoId.setter
    def chronoId(self, value):
        self._chronoId = value

    @property
    def chronoName(self):
        return self._chronoName

    @chronoName.setter
    def chronoName(self, value):
        self._chronoName = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def os187ppb(self):
        return self._os187ppb

    @os187ppb.setter
    def os187ppb(self, value):
        self._os187ppb = value

    @property
    def rePpm(self):
        return self._rePpm

    @rePpm.setter
    def rePpm(self, value):
        self._rePpm = value

