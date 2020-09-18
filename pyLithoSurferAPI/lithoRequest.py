from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class LithoRequest(APIRequests):

    path = URL_BASE + "/api/litho-requests"

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
    def lithoUserId(self):
        return self._lithoUserId

    @lithoUserId.setter
    def lithoUserId(self, value):
        self._lithoUserId = value

    @property
    def reqArgs(self):
        return self._reqArgs

    @reqArgs.setter
    def reqArgs(self, value):
        self._reqArgs = value

    @property
    def reqMethod(self):
        return self._reqMethod

    @reqMethod.setter
    def reqMethod(self, value):
        self._reqMethod = value

    @property
    def reqProtocol(self):
        return self._reqProtocol

    @reqProtocol.setter
    def reqProtocol(self, value):
        self._reqProtocol = value

    @property
    def reqQuery(self):
        return self._reqQuery

    @reqQuery.setter
    def reqQuery(self, value):
        self._reqQuery = value

    @property
    def reqRemoteAddr(self):
        return self._reqRemoteAddr

    @reqRemoteAddr.setter
    def reqRemoteAddr(self, value):
        self._reqRemoteAddr = value

    @property
    def reqRemoteIp(self):
        return self._reqRemoteIp

    @reqRemoteIp.setter
    def reqRemoteIp(self, value):
        self._reqRemoteIp = value

    @property
    def reqTimestamp(self):
        return self._reqTimestamp

    @reqTimestamp.setter
    def reqTimestamp(self, value):
        self._reqTimestamp = value

    @property
    def reqUri(self):
        return self._reqUri

    @reqUri.setter
    def reqUri(self, value):
        self._reqUri = value

