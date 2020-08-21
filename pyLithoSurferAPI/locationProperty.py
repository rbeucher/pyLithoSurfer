from . import session, URL_BASE
import json


class locationProperty(object):

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
    def locationId(self):
        return self._locationId

    @locationId.setter
    def locationId(self, value):
        self._locationId = value

    @property
    def locationLocName(self):
        return self._locationLocName

    @locationLocName.setter
    def locationLocName(self, value):
        self._locationLocName = value

    @property
    def propName(self):
        return self._propName

    @propName.setter
    def propName(self, value):
        self._propName = value

    @property
    def propValue(self):
        return self._propValue

    @propValue.setter
    def propValue(self, value):
        self._propValue = value

