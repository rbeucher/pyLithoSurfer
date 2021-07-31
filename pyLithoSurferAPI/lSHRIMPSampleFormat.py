from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json
from .utilities import get_id_from_list


class LSHRIMPSampleFormat(APIRequests):

    path = URL_BASE + "/api/shrimp/lshrimp-sample-formats"

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


def get_SHRIMPsampleFormat_id(value: str):
    return get_id_from_list(LSHRIMPSampleFormat, value)
