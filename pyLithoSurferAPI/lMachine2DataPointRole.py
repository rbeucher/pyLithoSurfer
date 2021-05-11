from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json
from .utilities import get_id_from_list


class LMachine2DataPointRole(APIRequests):

    path = URL_BASE + "/api/core/l-machine_2_data_point_role"

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
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        self._kind = value


def get_machine2DataPointRole_id(value: str):
    return get_id_from_list(LMachine2DataPointRole, value)

