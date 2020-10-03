from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class Specimen(APIRequests):

    path = URL_BASE + "/api/specimen"

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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def specimenKindId(self):
        return self._specimenKindId

    @specimenKindId.setter
    def specimenKindId(self, value):
        self._specimenKindId = value
    
    @property
    def specimenKindName(self):
        return self._specimenKindName

    @specimenKindName.setter
    def specimenKindName(self, value):
        self._specimenKindName = value
    
    @property
    def archiveId(self):
        return self._archiveId

    @archiveId.setter
    def archiveId(self, value):
        self._archiveId = value
    
    @property
    def archiveName(self):
        return self._archiveName

    @archiveName.setter
    def archiveName(self, value):
        self._archiveName = value
    
    @property
    def igsn(self):
        return self._igsn

    @igsn.setter
    def igsn(self, value):
        self._igsn = value
    
    @property
    def pictureHref(self):
        return self._pictureHref

    @pictureHref.setter
    def pictureHref(self, value):
        self._pictureHref = value
    
    @property
    def shrimpdataPointId(self):
        return self._shrimpdataPointId

    @shrimpdataPointId.setter
    def shrimpdataPointId(self, value):
        self._shrimpdataPointId = value