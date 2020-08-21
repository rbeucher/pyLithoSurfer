from . import session, URL_BASE
import json


class user(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def activated(self):
        return self._activated

    @activated.setter
    def activated(self, value):
        self._activated = value

    @property
    def authorities(self):
        return self._authorities

    @authorities.setter
    def authorities(self, value):
        self._authorities = value

    @property
    def createdBy(self):
        return self._createdBy

    @createdBy.setter
    def createdBy(self, value):
        self._createdBy = value

    @property
    def createdDate(self):
        return self._createdDate

    @createdDate.setter
    def createdDate(self, value):
        self._createdDate = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value):
        self._firstName = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def imageUrl(self):
        return self._imageUrl

    @imageUrl.setter
    def imageUrl(self, value):
        self._imageUrl = value

    @property
    def langKey(self):
        return self._langKey

    @langKey.setter
    def langKey(self, value):
        self._langKey = value

    @property
    def lastModifiedBy(self):
        return self._lastModifiedBy

    @lastModifiedBy.setter
    def lastModifiedBy(self, value):
        self._lastModifiedBy = value

    @property
    def lastModifiedDate(self):
        return self._lastModifiedDate

    @lastModifiedDate.setter
    def lastModifiedDate(self, value):
        self._lastModifiedDate = value

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        self._lastName = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value

