from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class StratigraphicUnit(APIRequests):

    path = URL_BASE + "/api/stratigraphic-units"

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
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value
    
    @property
    def baseAge(self):
        return self._baseAge

    @baseAge.setter
    def baseAge(self, value):
        self._baseAge = value
    
    @property
    def baseAgeName(self):
        return self._baseAgeName

    @baseAgeName.setter
    def baseAgeName(self, value: str):
        self._baseAgeName = value
    
    @property
    def topAge(self):
        return self._topAge

    @topAge.setter
    def topAge(self, value):
        self._topAge = value
    
    @property
    def topAgeName(self):
        return self._topAgeName

    @topAgeName.setter
    def topAgeName(self, value: str):
        self._topAgeName = value
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value

    @property
    def event(self):
        return self._event

    @event.setter
    def event(self, value: str):
        self._event = value
    
    @property
    def geologicalProvince(self):
        return self._geologicalProvince

    @geologicalProvince.setter
    def geologicalProvince(self, value: str):
        self._geologicalProvince = value
    
    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value: str):
        self._rank = value
    
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value: str):
        self._source = value
    
    @property
    def sourceId(self):
        return self._sourceId

    @sourceId.setter
    def sourceId(self, value: str):
        self._sourceId = value

    @property
    def thicknessMax(self):
        return self._thicknessMax

    @thicknessMax.setter
    def thicknessMax(self, value):
        self._thicknessMax = value
    
    @property
    def thicknessMin(self):
        return self._thicknessMin

    @thicknessMin.setter
    def thicknessMin(self, value):
        self._thicknessMin = value