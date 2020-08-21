from . import session, URL_BASE
import json


class kArgon(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def ar40Ar40(self):
        return self._ar40Ar40

    @ar40Ar40.setter
    def ar40Ar40(self, value):
        self._ar40Ar40 = value

    @property
    def atomAr(self):
        return self._atomAr

    @atomAr.setter
    def atomAr(self, value):
        self._atomAr = value

    @property
    def chronoId(self):
        return self._chronoId

    @chronoId.setter
    def chronoId(self, value):
        self._chronoId = value

    @property
    def chronoName(self):
        return self._chronoName

    @chronoName.setter
    def chronoName(self, value):
        self._chronoName = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def kperc(self):
        return self._kperc

    @kperc.setter
    def kperc(self, value):
        self._kperc = value

    @property
    def lambda(self):
        return self._lambda

    @lambda.setter
    def lambda(self, value):
        self._lambda = value

    @property
    def rad40k(self):
        return self._rad40k

    @rad40k.setter
    def rad40k(self, value):
        self._rad40k = value

    @property
    def sTPMoleGAR(self):
        return self._sTPMoleGAR

    @sTPMoleGAR.setter
    def sTPMoleGAR(self, value):
        self._sTPMoleGAR = value

