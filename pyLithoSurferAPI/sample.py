from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class Sample(APIRequests):

    path = URL_BASE + "/api/samples"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def archiveId(self):
        return self._archiveId

    @archiveId.setter
    def archiveId(self, value):
        self._archiveId = value
    
    @property
    def sourceId(self):
        return self._sourceId

    @sourceId.setter
    def sourceId(self, value):
        self._sourceId = value
    
    @property
    def tectonicUnitId(self):
        return self._tectonicUnitId

    @tectonicUnitId.setter
    def tectonicUnitId(self, value):
        self._tectonicUnitId = value
    
    @property
    def archiveName(self):
        return self._archiveName

    @archiveName.setter
    def archiveName(self, value):
        self._archiveName = value
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def igsn(self):
        return self._igsn

    @igsn.setter
    def igsn(self, value):
        self._igsn = value
    
    @property
    def relativeElevation(self):
        return self._relativeElevation

    @relativeElevation.setter
    def relativeElevation(self, value):
        self._relativeElevation = value

    @property
    def relativeElevationAccuracy(self):
        return self._relativeElevationAccuracy

    @relativeElevationAccuracy.setter
    def relativeElevationAccuracy(self, value):
        self._relativeElevationAccuracy = value
    
    @property
    def referenceElevationKind(self):
        return self._referenceElevationKind

    @referenceElevationKind.setter
    def referenceElevationKind(self, value):
        self._referenceElevationKind = value
    
    @property
    def referenceElevationKindNote(self):
        return self._referenceElevationKindNote

    @referenceElevationKindNote.setter
    def referenceElevationKindNote(self, value):
        self._referenceElevationKindNote = value
    
    @property
    def referenceElevation(self):
        return self._referenceElevation

    @referenceElevation.setter
    def referenceElevation(self, value):
        self._referenceElevation = value
    
    @property
    def referenceElevationSource(self):
        return self._referenceElevationSource

    @referenceElevationSource.setter
    def referenceElevationSource(self, value):
        self._referenceElevationSource = value
    
    @property
    def lithologyKindId(self):
        return self._lithologyKindId

    @lithologyKindId.setter
    def lithologyKindId(self, value):
        self._lithologyKindId = value
    
    @property
    def lithologyKindName(self):
        return self._lithologyKindName

    @lithologyKindName.setter
    def lithologyKindName(self, value):
        self._lithologyKindName = value
    
    @property
    def locationId(self):
        return self._locationId

    @locationId.setter
    def locationId(self, value):
        self._locationId = value
    
    @property
    def locationKindId(self):
        return self._locationKindId

    @locationKindId.setter
    def locationKindId(self, value):
        self._locationKindId = value
    
    @property
    def locationKindName(self):
        return self._locationKindName

    @locationKindName.setter
    def locationKindName(self, value):
        self._locationKindName = value
    
    @property
    def LocationName(self):
        return self._LocationName

    @LocationName.setter
    def LocationName(self, value):
        self._LocationName = value

    @property
    def sampleMethodId(self):
        return self._sampleMethodId

    @sampleMethodId.setter
    def sampleMethodId(self, value):
        self._sampleMethodId = value
    
    @property
    def sampleMethodName(self):
        return self._sampleMethodName

    @sampleMethodName.setter
    def sampleMethodName(self, value):
        self._sampleMethodName = value
    