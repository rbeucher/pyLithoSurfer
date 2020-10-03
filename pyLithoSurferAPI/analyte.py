from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class Analyte(APIRequests):

    path = URL_BASE + "/api/analytes"

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
    def analyteKindId(self):
        return self._analyteKindId

    @analyteKindId.setter
    def analyteKindId(self, value):
        self._analyteKindId = value
    
    @property
    def analyteKindName(self):
        return self._analyteKindName

    @analyteKindName.setter
    def analyteKindName(self, value):
        self._analyteKindName = value
    
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
    def specimenId(self):
        return self._specimenId

    @specimenId.setter
    def specimenId(self, value):
        self._specimenId = value
    
    @property
    def specimenName(self):
        return self._specimenName

    @specimenName.setter
    def specimenName(self, value):
        self._specimenName = value