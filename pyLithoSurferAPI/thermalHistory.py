from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class thermalHistory(APIRequests):

    path = URL_BASE + "/api/thermal-histories"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

