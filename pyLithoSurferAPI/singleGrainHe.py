from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class SingleGrainHe(APIRequests):

    path = URL_BASE + "/api/single-grain-hes"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    @property
    def diffusionModDiffusionModName(self):
        return self._diffusionModDiffusionModName

    @diffusionModDiffusionModName.setter
    def diffusionModDiffusionModName(self, value):
        self._diffusionModDiffusionModName = value

    @property
    def diffusionModId(self):
        return self._diffusionModId

    @diffusionModId.setter
    def diffusionModId(self, value):
        self._diffusionModId = value

    @property
    def errorTypeErrorType(self):
        return self._errorTypeErrorType

    @errorTypeErrorType.setter
    def errorTypeErrorType(self, value):
        self._errorTypeErrorType = value

    @property
    def errorTypeId(self):
        return self._errorTypeId

    @errorTypeId.setter
    def errorTypeId(self, value):
        self._errorTypeId = value

    @property
    def euNg(self):
        return self._euNg

    @euNg.setter
    def euNg(self, value):
        self._euNg = value

    @property
    def euPpm(self):
        return self._euPpm

    @euPpm.setter
    def euPpm(self, value):
        self._euPpm = value

    @property
    def ft(self):
        return self._ft

    @ft.setter
    def ft(self, value):
        self._ft = value

    @property
    def grainAge(self):
        return self._grainAge

    @grainAge.setter
    def grainAge(self, value):
        self._grainAge = value

    @property
    def grainAgeErr(self):
        return self._grainAgeErr

    @grainAgeErr.setter
    def grainAgeErr(self, value):
        self._grainAgeErr = value

    @property
    def grainEradius(self):
        return self._grainEradius

    @grainEradius.setter
    def grainEradius(self, value):
        self._grainEradius = value

    @property
    def grainLen(self):
        return self._grainLen

    @grainLen.setter
    def grainLen(self, value):
        self._grainLen = value

    @property
    def grainName(self):
        return self._grainName

    @grainName.setter
    def grainName(self, value):
        self._grainName = value

    @property
    def grainThick(self):
        return self._grainThick

    @grainThick.setter
    def grainThick(self, value):
        self._grainThick = value

    @property
    def grainWid(self):
        return self._grainWid

    @grainWid.setter
    def grainWid(self, value):
        self._grainWid = value

    @property
    def he4Ncc(self):
        return self._he4Ncc

    @he4Ncc.setter
    def he4Ncc(self, value):
        self._he4Ncc = value

    @property
    def he4Nmol(self):
        return self._he4Nmol

    @he4Nmol.setter
    def he4Nmol(self, value):
        self._he4Nmol = value

    @property
    def he4NmolPerGram(self):
        return self._he4NmolPerGram

    @he4NmolPerGram.setter
    def he4NmolPerGram(self, value):
        self._he4NmolPerGram = value

    @property
    def heliumGrainName(self):
        return self._heliumGrainName

    @heliumGrainName.setter
    def heliumGrainName(self, value):
        self._heliumGrainName = value

    @property
    def heliumId(self):
        return self._heliumId

    @heliumId.setter
    def heliumId(self, value):
        self._heliumId = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def labId(self):
        return self._labId

    @labId.setter
    def labId(self, value):
        self._labId = value

    @property
    def labLabName(self):
        return self._labLabName

    @labLabName.setter
    def labLabName(self, value):
        self._labLabName = value

    @property
    def massUg(self):
        return self._massUg

    @massUg.setter
    def massUg(self, value):
        self._massUg = value

    @property
    def mineralId(self):
        return self._mineralId

    @mineralId.setter
    def mineralId(self, value):
        self._mineralId = value

    @property
    def mineralMineral(self):
        return self._mineralMineral

    @mineralMineral.setter
    def mineralMineral(self, value):
        self._mineralMineral = value

    @property
    def nT(self):
        return self._nT

    @nT.setter
    def nT(self, value):
        self._nT = value

    @property
    def rawAge(self):
        return self._rawAge

    @rawAge.setter
    def rawAge(self, value):
        self._rawAge = value

    @property
    def rawAgeErr(self):
        return self._rawAgeErr

    @rawAgeErr.setter
    def rawAgeErr(self, value):
        self._rawAgeErr = value

    @property
    def smNg(self):
        return self._smNg

    @smNg.setter
    def smNg(self, value):
        self._smNg = value

    @property
    def smPpm(self):
        return self._smPpm

    @smPpm.setter
    def smPpm(self, value):
        self._smPpm = value

    @property
    def thNg(self):
        return self._thNg

    @thNg.setter
    def thNg(self, value):
        self._thNg = value

    @property
    def thPpm(self):
        return self._thPpm

    @thPpm.setter
    def thPpm(self, value):
        self._thPpm = value

    @property
    def thURatio(self):
        return self._thURatio

    @thURatio.setter
    def thURatio(self, value):
        self._thURatio = value

    @property
    def uNg(self):
        return self._uNg

    @uNg.setter
    def uNg(self, value):
        self._uNg = value

    @property
    def uPpm(self):
        return self._uPpm

    @uPpm.setter
    def uPpm(self, value):
        self._uPpm = value

