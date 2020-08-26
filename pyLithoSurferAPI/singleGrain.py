from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class singleGrain(APIRequests):

    path = URL_BASE + "/api/single-grains"

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
    def clCont(self):
        return self._clCont

    @clCont.setter
    def clCont(self, value):
        self._clCont = value

    @property
    def dpar(self):
        return self._dpar

    @dpar.setter
    def dpar(self, value):
        self._dpar = value

    @property
    def dper(self):
        return self._dper

    @dper.setter
    def dper(self, value):
        self._dper = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def lAPitArea(self):
        return self._lAPitArea

    @lAPitArea.setter
    def lAPitArea(self, value):
        self._lAPitArea = value

    @property
    def lAPitDepth(self):
        return self._lAPitDepth

    @lAPitDepth.setter
    def lAPitDepth(self, value):
        self._lAPitDepth = value

    @property
    def lAPitDiameter(self):
        return self._lAPitDiameter

    @lAPitDiameter.setter
    def lAPitDiameter(self, value):
        self._lAPitDiameter = value

    @property
    def lAPitShape(self):
        return self._lAPitShape

    @lAPitShape.setter
    def lAPitShape(self, value):
        self._lAPitShape = value

    @property
    def lAPitVolume(self):
        return self._lAPitVolume

    @lAPitVolume.setter
    def lAPitVolume(self, value):
        self._lAPitVolume = value

    @property
    def ni(self):
        return self._ni

    @ni.setter
    def ni(self, value):
        self._ni = value

    @property
    def ns(self):
        return self._ns

    @ns.setter
    def ns(self, value):
        self._ns = value

    @property
    def rhoD(self):
        return self._rhoD

    @rhoD.setter
    def rhoD(self, value):
        self._rhoD = value

    @property
    def rhoI(self):
        return self._rhoI

    @rhoI.setter
    def rhoI(self, value):
        self._rhoI = value

    @property
    def rhoS(self):
        return self._rhoS

    @rhoS.setter
    def rhoS(self, value):
        self._rhoS = value

    @property
    def singGrainAge(self):
        return self._singGrainAge

    @singGrainAge.setter
    def singGrainAge(self, value):
        self._singGrainAge = value

    @property
    def singGrainAgeErr(self):
        return self._singGrainAgeErr

    @singGrainAgeErr.setter
    def singGrainAgeErr(self, value):
        self._singGrainAgeErr = value

    @property
    def singGrainName(self):
        return self._singGrainName

    @singGrainName.setter
    def singGrainName(self, value):
        self._singGrainName = value

    @property
    def uCaRatio(self):
        return self._uCaRatio

    @uCaRatio.setter
    def uCaRatio(self, value):
        self._uCaRatio = value

    @property
    def uPpm(self):
        return self._uPpm

    @uPpm.setter
    def uPpm(self, value):
        self._uPpm = value

    @property
    def uSiRatio(self):
        return self._uSiRatio

    @uSiRatio.setter
    def uSiRatio(self, value):
        self._uSiRatio = value

    @property
    def uppmError(self):
        return self._uppmError

    @uppmError.setter
    def uppmError(self, value):
        self._uppmError = value

