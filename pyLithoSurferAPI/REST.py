from abc import ABC
import json
import pandas as pd
import urllib
from pyLithoSurferAPI.utilities import NumpyEncoder


class APIRequests(ABC):

    URL_BASE = None
    API_PATH = None
    SESSION = None

    def __init__(self, **kwargs):
        self.id = kwargs.pop("id") if "id" in kwargs.keys() else None
        for key, val in kwargs.items():
            setattr(self, key, val)

    @classmethod
    def path(cls):
        return APIRequests.URL_BASE + cls.API_PATH

    # GET ALL
    @classmethod
    def get_all(cls):
        return cls.get_entries(cls.count())
    
    # GET N ENTRIES
    @classmethod
    def get_entries(cls, nentries=1):
        response = APIRequests.SESSION.get(cls.path()+f"?size={nentries}")
        response.raise_for_status()
        records = response.json()
        return pd.DataFrame.from_records(records)

    # POST
    def new(self):
        data = self.to_dict()
        data.pop("id")
        response = APIRequests.SESSION.post(self.path(), data=json.dumps(data), headers=self.SESSION.headers)
        try:
            response.raise_for_status()
        except Exception as e:
            print(json.dumps(data, cls=NumpyEncoder))
            print(response.json())
            raise e
        response = response.json()
        self.id = response["id"]
        return response

    # PUT
    def update(self):
        response = APIRequests.SESSION.put(self.path(), data=self.to_json(), headers=self.SESSION.headers)
        try:
            response.raise_for_status()
        except Exception as e:
            print(json.dumps(self.to_json(), cls=NumpyEncoder))
            print(response.json())
            raise e
        return response

    # COUNT
    @classmethod
    def count(cls):
        path = cls.path() + "/" + "count"
        response = APIRequests.SESSION.get(path)
        response.raise_for_status()
        return response.json()   

    # DELETE
    @classmethod
    def delete(cls, id):
        path = cls.path() + "/" + str(id)
        response = APIRequests.SESSION.delete(path)
        response.raise_for_status()
        return response

    # GET FROM ID
    def get_from_id(self, id_value):
        path = self.path() + "/" + str(id_value)
        response = APIRequests.SESSION.get(path)
        response.raise_for_status()
        data = response.json()
        self.__init__(**data)
        return response

    @classmethod
    def query(cls, query):
        query = urllib.parse.urlencode(query)
        path = cls.path() + "?" + str(query)
        response = APIRequests.SESSION.get(path)
        response.raise_for_status()
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