from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class lChrAgeKind(APIRequests):

    path = URL_BASE + "/api/l-chr-age-kinds"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def ageKind(self):
        return self._ageKind

    @ageKind.setter
    def ageKind(self, value):
        self._ageKind = value

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

