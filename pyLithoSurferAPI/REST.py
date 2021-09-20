from . import session, URL_BASE
from abc import ABC
import json
import pandas as pd
import urllib
from pyLithoSurferAPI.utilities import NumpyEncoder

class ForbiddenException(Exception):
    pass


class UnauthorizedException(Exception):
    pass


class NotFoundException(Exception):
    pass


class ItemNotFoundException(Exception):
    pass


def check_response(response):
    status_code = response.status_code
    if status_code in [200, 204]:
        return True
    else:
        f = open("errors.log", "a")
        f.write(str(response.json())+"\n\n")
        f.close()
        print(response.json())
        if status_code == 401:
            raise(UnauthorizedException)
        elif status_code == 403:
            raise(ForbiddenException)
        elif status_code == 404:
            raise(NotFoundException)
        elif status_code == 500:
            raise(ItemNotFoundException)

class APIRequests(ABC):

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    # GET ALL
    @classmethod
    def get_all(cls):
        return cls.get_entries(cls.count())
    
    # GET N ENTRIES
    @classmethod
    def get_entries(cls, nentries=1):
        response = session.get(cls.path, data={"size": nentries})
        check_response(response)
        records = response.json()
        return pd.DataFrame.from_records(records)

    # POST
    def new(self):
        data = self.to_dict()
        if "id" in data.keys():
            data.pop("id")
        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = session.post(self.path, data=json.dumps(data), headers=headers)
        check_response(response)
        response = response.json()
        if "id" in response.keys():
            self.id = response["id"]
        return response

    # PUT
    def update(self):
        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        response = session.put(self.path, data=self.to_json(), headers=headers)
        check_response(response)
        return response

    # COUNT
    @classmethod
    def count(cls):
        path = cls.path + "/" + "count"
        response = session.get(path)
        check_response(response)
        return response.json()   

    # DELETE
    def delete(self):
        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        path = self.path + "/" + str(self.id)
        response = session.delete(path)
        check_response(response)
        return response

    # GET FROM ID
    def get_from_id(self, id_value):
        path = self.path + "/" + str(id_value)
        response = session.get(path)
        check_response(response)
        data = response.json()
        self.__init__(**data)
        return response

    @classmethod
    def query(cls, query):
        query = urllib.parse.urlencode(query)
        headers = session.headers
        headers["Accept"] = "application/json"
        path = cls.path + "?" + str(query)
        response = session.get(path)
        return response

    @classmethod
    def get_from_query(cls, query):
        response = cls.query(query)
        records = response.json()
        objects_list = []
        for record in records:
            objects_list.append(cls(**record))
        return objects_list

    def to_json(self):
        return json.dumps(self, default=lambda o: {key.replace("_", ""): val for key, val in o.__dict__.items()}, 
            sort_keys=True) 

    def to_dict(self):
        return {key.replace("_", ""): val for key, val in self.__dict__.items()}

    @classmethod
    def get_id_from_name(cls, name):
       
        if (name is None):
            return None

        query = {"name.equals": name}
        response = cls.query(query)
        records = response.json()
        
        if not records:
            print(f"Cannot find {name} in list")
            return None
        
        return records[0]["id"]