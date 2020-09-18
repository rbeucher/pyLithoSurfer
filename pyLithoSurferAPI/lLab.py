from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class LLab(object):

    path = URL_BASE + "/api/l-labs"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def institute(self):
        return self._institute

    @institute.setter
    def institute(self, value):
        self._institute = value

    @property
    def labName(self):
        return self._labName

    @labName.setter
    def labName(self, value):
        self._labName = value

