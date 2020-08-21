from . import session, URL_BASE
import json


class vitrinite(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

