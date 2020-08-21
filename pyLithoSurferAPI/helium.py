from . import session, URL_BASE
import json


class helium(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def analyticalKindAnalyticalKind(self):
        return self._analyticalKindAnalyticalKind

    @analyticalKindAnalyticalKind.setter
    def analyticalKindAnalyticalKind(self, value):
        self._analyticalKindAnalyticalKind = value

    @property
    def analyticalKindId(self):
        return self._analyticalKindId

    @analyticalKindId.setter
    def analyticalKindId(self, value):
        self._analyticalKindId = value

    @property
    def analyticalMethodAnalyticalMethod(self):
        return self._analyticalMethodAnalyticalMethod

    @analyticalMethodAnalyticalMethod.setter
    def analyticalMethodAnalyticalMethod(self, value):
        self._analyticalMethodAnalyticalMethod = value

    @property
    def analyticalMethodId(self):
        return self._analyticalMethodId

    @analyticalMethodId.setter
    def analyticalMethodId(self, value):
        self._analyticalMethodId = value

    @property
    def averageKindAverageMethod(self):
        return self._averageKindAverageMethod

    @averageKindAverageMethod.setter
    def averageKindAverageMethod(self, value):
        self._averageKindAverageMethod = value

    @property
    def averageKindId(self):
        return self._averageKindId

    @averageKindId.setter
    def averageKindId(self, value):
        self._averageKindId = value

    @property
    def avgGrainLengthUm(self):
        return self._avgGrainLengthUm

    @avgGrainLengthUm.setter
    def avgGrainLengthUm(self, value):
        self._avgGrainLengthUm = value

    @property
    def avgGrainThickUm(self):
        return self._avgGrainThickUm

    @avgGrainThickUm.setter
    def avgGrainThickUm(self, value):
        self._avgGrainThickUm = value

    @property
    def avgGrainWidthUm(self):
        return self._avgGrainWidthUm

    @avgGrainWidthUm.setter
    def avgGrainWidthUm(self, value):
        self._avgGrainWidthUm = value

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
    def grainEradiusUm(self):
        return self._grainEradiusUm

    @grainEradiusUm.setter
    def grainEradiusUm(self, value):
        self._grainEradiusUm = value

    @property
    def grainName(self):
        return self._grainName

    @grainName.setter
    def grainName(self, value):
        self._grainName = value

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
    def ngrains(self):
        return self._ngrains

    @ngrains.setter
    def ngrains(self, value):
        self._ngrains = value

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
    def thURatio(self):
        return self._thURatio

    @thURatio.setter
    def thURatio(self, value):
        self._thURatio = value

    @property
    def totalEUPpm(self):
        return self._totalEUPpm

    @totalEUPpm.setter
    def totalEUPpm(self, value):
        self._totalEUPpm = value

    @property
    def totalEuNg(self):
        return self._totalEuNg

    @totalEuNg.setter
    def totalEuNg(self, value):
        self._totalEuNg = value

    @property
    def totalHe4Ncc(self):
        return self._totalHe4Ncc

    @totalHe4Ncc.setter
    def totalHe4Ncc(self, value):
        self._totalHe4Ncc = value

    @property
    def totalHe4NmolPerGram(self):
        return self._totalHe4NmolPerGram

    @totalHe4NmolPerGram.setter
    def totalHe4NmolPerGram(self, value):
        self._totalHe4NmolPerGram = value

    @property
    def totalHeNmol(self):
        return self._totalHeNmol

    @totalHeNmol.setter
    def totalHeNmol(self, value):
        self._totalHeNmol = value

    @property
    def totalSmNg(self):
        return self._totalSmNg

    @totalSmNg.setter
    def totalSmNg(self, value):
        self._totalSmNg = value

    @property
    def totalSmPpm(self):
        return self._totalSmPpm

    @totalSmPpm.setter
    def totalSmPpm(self, value):
        self._totalSmPpm = value

    @property
    def totalThNg(self):
        return self._totalThNg

    @totalThNg.setter
    def totalThNg(self, value):
        self._totalThNg = value

    @property
    def totalThPpm(self):
        return self._totalThPpm

    @totalThPpm.setter
    def totalThPpm(self, value):
        self._totalThPpm = value

    @property
    def totalUNg(self):
        return self._totalUNg

    @totalUNg.setter
    def totalUNg(self, value):
        self._totalUNg = value

    @property
    def totalUPpm(self):
        return self._totalUPpm

    @totalUPpm.setter
    def totalUPpm(self, value):
        self._totalUPpm = value

