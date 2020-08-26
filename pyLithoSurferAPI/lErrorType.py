from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class lErrorType(APIRequests):

    path = URL_BASE + "/api/l-error-types"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def errorType(self):
        return self._errorType

    @errorType.setter
    def errorType(self, value):
        self._errorType = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

