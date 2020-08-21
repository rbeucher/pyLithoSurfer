from . import session, URL_BASE
import json


class dataPoint(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def dataEntityId(self):
        return self._dataEntityId

    @dataEntityId.setter
    def dataEntityId(self, value):
        self._dataEntityId = value

    @property
    def dataPackageId(self):
        return self._dataPackageId

    @dataPackageId.setter
    def dataPackageId(self, value):
        self._dataPackageId = value

    @property
    def dataPackageName(self):
        return self._dataPackageName

    @dataPackageName.setter
    def dataPackageName(self, value):
        self._dataPackageName = value

    @property
    def dataStructure(self):
        return self._dataStructure

    @dataStructure.setter
    def dataStructure(self, value):
        self._dataStructure = value

    @property
    def elevation(self):
        return self._elevation

    @elevation.setter
    def elevation(self, value):
        self._elevation = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

