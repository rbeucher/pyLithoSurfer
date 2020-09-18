from . import session, URL_BASE
import json


class PasswordChange(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def currentPassword(self):
        return self._currentPassword

    @currentPassword.setter
    def currentPassword(self, value):
        self._currentPassword = value

    @property
    def newPassword(self):
        return self._newPassword

    @newPassword.setter
    def newPassword(self, value):
        self._newPassword = value

