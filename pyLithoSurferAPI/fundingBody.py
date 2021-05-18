from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class FundingBody(APIRequests):

    path = URL_BASE + "/api/core/funding-bodies"

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
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    
    @property
    def countryId(self):
        return self._countryId

    @countryId.setter
    def countryId(self, value):
        self._countryId = value
    
    @property
    def countryName(self):
        return self._countryName

    @countryName.setter
    def countryName(self, value):
        self._countryName = value
    
    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self, value):
        self._logo = value
    
    @property
    def logoContentType(self):
        return self._logoContentType

    @logoContentType.setter
    def logoContentType(self, value):
        self._logoContentType = value
    
    @property
    def shortName(self):
        return self._shortName

    @shortName.setter
    def shortName(self, value):
        self._shortName = value