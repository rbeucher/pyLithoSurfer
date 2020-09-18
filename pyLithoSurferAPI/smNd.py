from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class SmNd(APIRequests):

    path = URL_BASE + "/api/sm-nds"

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
    def dMage(self):
        return self._dMage

    @dMage.setter
    def dMage(self, value):
        self._dMage = value

    @property
    def epsilonNdt(self):
        return self._epsilonNdt

    @epsilonNdt.setter
    def epsilonNdt(self, value):
        self._epsilonNdt = value

    @property
    def error20(self):
        return self._error20

    @error20.setter
    def error20(self, value):
        self._error20 = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nd143Nd144(self):
        return self._nd143Nd144

    @nd143Nd144.setter
    def nd143Nd144(self, value):
        self._nd143Nd144 = value

    @property
    def ndppm(self):
        return self._ndppm

    @ndppm.setter
    def ndppm(self, value):
        self._ndppm = value

    @property
    def sm147Nd144(self):
        return self._sm147Nd144

    @sm147Nd144.setter
    def sm147Nd144(self, value):
        self._sm147Nd144 = value

    @property
    def smppm(self):
        return self._smppm

    @smppm.setter
    def smppm(self, value):
        self._smppm = value

