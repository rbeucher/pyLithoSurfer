from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class chrono(APIRequests):

    path = URL_BASE + "/api/chronos"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

