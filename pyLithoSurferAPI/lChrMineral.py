from . import session, URL_BASE
import json


class lChrMineral(object):

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
    def mineral(self):
        return self._mineral

    @mineral.setter
    def mineral(self, value):
        self._mineral = value

    @property
    def synonym(self):
        return self._synonym

    @synonym.setter
    def synonym(self, value):
        self._synonym = value

