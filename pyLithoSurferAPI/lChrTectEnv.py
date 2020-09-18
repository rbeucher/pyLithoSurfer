from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class LChrTectEnv(APIRequests):

    path = URL_BASE + "/api/l-chr-tect-envs"

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
    def tectEnv(self):
        return self._tectEnv

    @tectEnv.setter
    def tectEnv(self, value):
        self._tectEnv = value

