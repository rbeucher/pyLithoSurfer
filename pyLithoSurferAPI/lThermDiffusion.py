from . import session, URL_BASE
import json


class lThermDiffusion(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def diffusionModAuthor(self):
        return self._diffusionModAuthor

    @diffusionModAuthor.setter
    def diffusionModAuthor(self, value):
        self._diffusionModAuthor = value

    @property
    def diffusionModName(self):
        return self._diffusionModName

    @diffusionModName.setter
    def diffusionModName(self, value):
        self._diffusionModName = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

