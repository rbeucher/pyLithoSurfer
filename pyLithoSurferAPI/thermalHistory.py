from . import session, URL_BASE
import json


class thermalHistory(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

