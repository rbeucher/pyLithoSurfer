from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class chronoProperty(APIRequests):

    path = URL_BASE + "/api/chrono-properties"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def chronoId(self):
        return self._chronoId

    @chronoId.setter
    def chronoId(self, value):
        self._chronoId = value

    @property
    def chronoName(self):
        return self._chronoName

    @chronoName.setter
    def chronoName(self, value):
        self._chronoName = value

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

    @property
    def propName(self):
        return self._propName

    @propName.setter
    def propName(self, value):
        self._propName = value

    @property
    def propValue(self):
        return self._propValue

    @propValue.setter
    def propValue(self, value):
        self._propValue = value

