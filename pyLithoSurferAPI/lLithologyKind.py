from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class LLithologyKind(object):

    path = URL_BASE + "/api/l-lithology-kinds"

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

    @property
    def synonym_name(self):
        return self._synonym_name

    @synonym_name.setter
    def synonym_name(self, value):
        self._synonym_name = value
    
    @property
    def mindat_hyperlink(self):
        return self._mindat_hyperlink

    @mindat_hyperlink.setter
    def mindat_hypelink(self, value):
        self._mindat_hyperlink = value