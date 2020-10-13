from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class Location(APIRequests):

    path = URL_BASE + "/api/locations"

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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value

    @property
    def captureMethodId(self):
        return self._captureMethodId

    @captureMethodId.setter
    def captureMethodId(self, value):
        self._captureMethodId = value

    @property
    def captureMethodName(self):
        return self._captureMethodName

    @captureMethodName.setter
    def captureMethodName(self, value):
        self._captureMethodName = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def locPredefinedId(self):
        return self._locPredefinedId

    @locPredefinedId.setter
    def locPredefinedId(self, value):
        self._locPredefinedId = value

    @property
    def locPredefinedName(self):
        return self._locPredefinedName

    @locPredefinedName.setter
    def locPredefinedName(self, value):
        self._locPredefinedName = value

    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value):
        self._lon = value

    @property
    def latLonPrecision(self):
        return self._latLonPrecision

    @latLonPrecision.setter
    def latLonPrecision(self, value):
        self._latLonPrecision = value
