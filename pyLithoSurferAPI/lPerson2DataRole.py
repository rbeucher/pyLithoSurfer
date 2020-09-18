from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class LPerson2DataRole(APIRequests):

    path = URL_BASE + "/api/l-person-2-data-point-roles"

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

