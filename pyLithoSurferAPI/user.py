from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import pandas as pd
import numpy as np
from .utilities import *


class User(APIRequests):
        
    path = URL_BASE+'/api/users'

    def __init__(self,
                 activated: bool = True ,
                 email: str = None,
                 firstName: str = None,
                 id: Union[int, np.int16, np.int32, np.int64] = 0,
                 imageUrl: str = None,
                 langKey: str = None,
                 lastName: str = None,
                 login: str = None,
                 resetDate: str = None,
                ):
        
        self.activated = activated
        self.email = email
        self.firstName = firstName
        self.id = id
        self.imageUrl = imageUrl
        self.langKey = langKey
        self.lastName = lastName
        self.login = login
        self.resetDate = resetDate

    
    @property
    def activated(self):
        return self._activated

    @activated.setter
    def activated(self, value: bool):
        self._activated = value
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = convert_str(value)
    
    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value: str):
        self._firstName = convert_str(value)
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = int(value)
    
    @property
    def imageUrl(self):
        return self._imageUrl

    @imageUrl.setter
    def imageUrl(self, value: str):
        self._imageUrl = convert_str(value)
    
    @property
    def langKey(self):
        return self._langKey

    @langKey.setter
    def langKey(self, value: str):
        self._langKey = convert_str(value)
    
    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value: str):
        self._lastName = convert_str(value)
    
    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value: str):
        self._login = convert_str(value)
    
    @property
    def resetDate(self):
        return self._resetDate

    @resetDate.setter
    def resetDate(self, value: str):
        self._resetDate = convert_str(value)
    
        