from . import session, URL_BASE
import json


class lChrAnalyticalMethod(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def analyticalMethod(self):
        return self._analyticalMethod

    @analyticalMethod.setter
    def analyticalMethod(self, value):
        self._analyticalMethod = value

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

