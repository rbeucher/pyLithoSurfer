from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class rbSr(APIRequests):

    path = URL_BASE + "/api/rb-srs"

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
    def i87SR86SR(self):
        return self._i87SR86SR

    @i87SR86SR.setter
    def i87SR86SR(self, value):
        self._i87SR86SR = value

    @property
    def iUncert(self):
        return self._iUncert

    @iUncert.setter
    def iUncert(self, value):
        self._iUncert = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def m87SR86SR(self):
        return self._m87SR86SR

    @m87SR86SR.setter
    def m87SR86SR(self, value):
        self._m87SR86SR = value

    @property
    def mUncert(self):
        return self._mUncert

    @mUncert.setter
    def mUncert(self, value):
        self._mUncert = value

