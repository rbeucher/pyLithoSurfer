from . import session, URL_BASE
import json


class datapointProperty(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def datapointId(self):
        return self._datapointId

    @datapointId.setter
    def datapointId(self, value):
        self._datapointId = value

    @property
    def datapointName(self):
        return self._datapointName

    @datapointName.setter
    def datapointName(self, value):
        self._datapointName = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

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

