from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class entry(APIRequests):

    path = URL_BASE + "/api/entries"

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
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

