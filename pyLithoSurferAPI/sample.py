from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class Sample(APIRequests):

    path = URL_BASE + "/api/samples"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

