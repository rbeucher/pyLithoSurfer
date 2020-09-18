from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class LVerticalDatum(APIRequests):

    path = URL_BASE + "/api/l-vertical-data"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def abreviation(self):
        return self._abreviation

    @abreviation.setter
    def abreviation(self, value):
        self._abreviation = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def epsgCode(self):
        return self._epsgCode

    @epsgCode.setter
    def epsgCode(self, value):
        self._epsgCode = value

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

