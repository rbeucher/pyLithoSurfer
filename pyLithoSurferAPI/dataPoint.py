from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class DataPoint(APIRequests):

    path = URL_BASE + "/api/data-points"

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
    def sampleId(self):
        return self._sampleId

    @sampleId.setter
    def sampleId(self, value):
        self._sampleId = value
    
    @property
    def sampleName(self):
        return self._sampleName

    @sampleName.setter
    def sampleName(self, value):
        self._sampleName = value
    
    @property
    def sourceId(self):
        return self._sourceId

    @sourceId.setter
    def sourceId(self, value):
        self._sourceId = value
    
    @property
    def locationId(self):
        return self._locationId

    @locationId.setter
    def locationId(self, value):
        self._locationId = value
    
    @property
    def locationName(self):
        return self._locationName

    @locationName.setter
    def locationName(self, value):
        self._locationName = value
    
    @property
    def externalDataHref(self):
        return self._externalDataHref

    @externalDataHref.setter
    def externalDataHref(self, value):
        self._externalDataHref = value
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value