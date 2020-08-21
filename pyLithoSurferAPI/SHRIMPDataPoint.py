from . import session, URL_BASE
import json


class SHRIMPDataPoint(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def ageAverageKindId(self):
        return self._ageAverageKindId

    @ageAverageKindId.setter
    def ageAverageKindId(self, value):
        self._ageAverageKindId = value

    @property
    def ageAverageKindName(self):
        return self._ageAverageKindName

    @ageAverageKindName.setter
    def ageAverageKindName(self, value):
        self._ageAverageKindName = value

    @property
    def ageErrorMax(self):
        return self._ageErrorMax

    @ageErrorMax.setter
    def ageErrorMax(self, value):
        self._ageErrorMax = value

    @property
    def ageErrorMin(self):
        return self._ageErrorMin

    @ageErrorMin.setter
    def ageErrorMin(self, value):
        self._ageErrorMin = value

    @property
    def analyteId(self):
        return self._analyteId

    @analyteId.setter
    def analyteId(self, value):
        self._analyteId = value

    @property
    def analyteName(self):
        return self._analyteName

    @analyteName.setter
    def analyteName(self, value):
        self._analyteName = value

    @property
    def errorAgeTypeId(self):
        return self._errorAgeTypeId

    @errorAgeTypeId.setter
    def errorAgeTypeId(self, value):
        self._errorAgeTypeId = value

    @property
    def errorAgeTypeName(self):
        return self._errorAgeTypeName

    @errorAgeTypeName.setter
    def errorAgeTypeName(self, value):
        self._errorAgeTypeName = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def mineralId(self):
        return self._mineralId

    @mineralId.setter
    def mineralId(self, value):
        self._mineralId = value

    @property
    def mineralName(self):
        return self._mineralName

    @mineralName.setter
    def mineralName(self, value):
        self._mineralName = value

    @property
    def mountId(self):
        return self._mountId

    @mountId.setter
    def mountId(self, value):
        self._mountId = value

    @property
    def ngrains(self):
        return self._ngrains

    @ngrains.setter
    def ngrains(self, value):
        self._ngrains = value

    @property
    def nspots(self):
        return self._nspots

    @nspots.setter
    def nspots(self, value):
        self._nspots = value

    @property
    def singleGrainId(self):
        return self._singleGrainId

    @singleGrainId.setter
    def singleGrainId(self, value):
        self._singleGrainId = value

    @property
    def singleGrainName(self):
        return self._singleGrainName

    @singleGrainName.setter
    def singleGrainName(self, value):
        self._singleGrainName = value

