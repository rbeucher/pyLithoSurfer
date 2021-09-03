from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *
from .REST import check_response
import urllib.parse


class Person(APIRequests):

    path = URL_BASE + "/api/core/people"

    def __init__(self,
                 id: int = None,
                 calcName: str = None,
                 firstName: str = None,
                 name: str = None,
                 note: str = None,
                 orcId: str = None,
                 title: str = None):

        self.firstName = convert_str(firstName)
        self.name = convert_str(name)
        self.note = convert_str(note)
        self.orcId = convert_str(orcId)
        self.title = convert_str(title)
        self.calcName = convert_str(calcName)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64, None]):
        self._id = convert_int(value)

    def new(self, *args, **kwargs):
        super().new(*args, **kwargs)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = convert_str(value)
    
    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, value: str):
        self._firstName = convert_str(value)
    
    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value: str):
        self._note = convert_str(value)
    
    @property
    def orcId(self):
        return self._orcId

    @orcId.setter
    def orcId(self, value: str):
        self._orcId = convert_str(value)
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = convert_str(value)
    
    @property
    def calcName(self):
        return self._calcName

    @calcName.setter
    def calcName(self, value: str):
        self._calcName = convert_str(value)


def get_person_id(firstName=None, name=None):
    firstNameQuery = {}
    if firstName:
        firstNameQuery = {"firstName.contains": firstName}
    nameQuery = {}
    if name:
        nameQuery = {"name.contains": name}
    query = {**firstNameQuery, **nameQuery}
    response = Person.get_from_query(urllib.parse.urlencode(query))
    records = response.json()
    if len(records) > 1:
        df = pd.DataFrame.from_records(records)
        print(df)
        chosen_id = input("Choose id:")
        return chosen_id
    elif records:
        return records[0]["id"]
    else:
        print(f"{firstName} {name} was not found")
        return