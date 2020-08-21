from . import session, URL_BASE
import json


class gradientAndTemp(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def gradient(self):
        return self._gradient

    @gradient.setter
    def gradient(self, value):
        self._gradient = value

    @property
    def log(self):
        return self._log

    @log.setter
    def log(self, value):
        self._log = value

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value

