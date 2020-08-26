from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class lithoUser(APIRequests):

    path = URL_BASE + "/api/litho-users"

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
    def institutionId(self):
        return self._institutionId

    @institutionId.setter
    def institutionId(self, value):
        self._institutionId = value

    @property
    def institutionName(self):
        return self._institutionName

    @institutionName.setter
    def institutionName(self, value):
        self._institutionName = value

    @property
    def userEmail(self):
        return self._userEmail

    @userEmail.setter
    def userEmail(self, value):
        self._userEmail = value

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, value):
        self._userId = value

