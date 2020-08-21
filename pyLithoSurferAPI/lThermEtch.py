from . import session, URL_BASE
import json


class lThermEtch(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def etchant(self):
        return self._etchant

    @etchant.setter
    def etchant(self, value):
        self._etchant = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def strengthMolar(self):
        return self._strengthMolar

    @strengthMolar.setter
    def strengthMolar(self, value):
        self._strengthMolar = value

    @property
    def strengthPercent(self):
        return self._strengthPercent

    @strengthPercent.setter
    def strengthPercent(self, value):
        self._strengthPercent = value

