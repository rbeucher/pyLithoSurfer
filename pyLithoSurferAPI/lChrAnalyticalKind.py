from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class lChrAnalyticalKind(APIRequests):

    path = URL_BASE + "/api/l-chr-analytical-kinds"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def analyticalKind(self):
        return self._analyticalKind

    @analyticalKind.setter
    def analyticalKind(self, value):
        self._analyticalKind = value

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

