from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class entryProperty(APIRequests):

    path = URL_BASE + "/api/entry-properties"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def entryId(self):
        return self._entryId

    @entryId.setter
    def entryId(self, value):
        self._entryId = value

    @property
    def entryType(self):
        return self._entryType

    @entryType.setter
    def entryType(self, value):
        self._entryType = value

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

