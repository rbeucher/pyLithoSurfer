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