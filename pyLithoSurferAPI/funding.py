from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class Funding(APIRequests):

    path = URL_BASE + "/api/core/fundings"

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
    def grandNumber(self):
        return self._grandNumber

    @grandNumber.setter
    def grandNumber(self, value):
        self._grandNumber = value
    
    @property
    def fundingBodyId(self):
        return self._fundingBodyId

    @fundingBodyId.setter
    def fundingBodyId(self, value):
        self._fundingBodyId = value
    
    @property
    def fundingBodyName(self):
        return self._fundingBodyName

    @fundingBodyName.setter
    def fundingBodyName(self, value):
        self._fundingBodyName = value
    
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value