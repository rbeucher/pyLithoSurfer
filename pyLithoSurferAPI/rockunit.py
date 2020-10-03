from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class RockUnit(APIRequests):

    path = URL_BASE + "/api/rock-units"

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
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    
    @property
    def ageMin(self):
        return self._ageMin

    @ageMin.setter
    def ageMin(self, value):
        self._ageMin = value
    
    @property
    def ageMax(self):
        return self._ageMax

    @ageMax.setter
    def ageMax(self, value):
        self._ageMax = value