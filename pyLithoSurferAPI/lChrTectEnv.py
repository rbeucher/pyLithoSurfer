from . import session, URL_BASE
import json


class lChrTectEnv(object):

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

