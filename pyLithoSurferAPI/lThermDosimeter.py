from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class LThermDosimeter(APIRequests):

    path = URL_BASE + "/api/l-therm-dosimeters"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def dosimeterGlassName(self):
        return self._dosimeterGlassName

    @dosimeterGlassName.setter
    def dosimeterGlassName(self, value):
        self._dosimeterGlassName = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def uPpm(self):
        return self._uPpm

    @uPpm.setter
    def uPpm(self, value):
        self._uPpm = value

