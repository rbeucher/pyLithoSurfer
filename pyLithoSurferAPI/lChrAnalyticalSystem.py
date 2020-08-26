from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class lChrAnalyticalSystem(APIRequests):

    path = URL_BASE + "/api/l-chr-analytical-systems"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def analyticalSystem(self):
        return self._analyticalSystem

    @analyticalSystem.setter
    def analyticalSystem(self, value):
        self._analyticalSystem = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

