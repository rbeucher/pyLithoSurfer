from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json
from .utilities import get_id_from_list


class LErrorType(APIRequests):

    path = URL_BASE + "/api/core/l-error-types"

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
    def errorType(self):
        return self._errorType

    @errorType.setter
    def errorType(self, value):
        self._errorType = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

def get_error_type_id(value: str):
    return get_id_from_list(LErrorType, value)
