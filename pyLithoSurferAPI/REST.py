from . import session, URL_BASE
from abc import ABC
import json
import pandas as pd

class APIRequests(ABC):

    # GET ALL
    @classmethod
    def get_all(cls):
        response = session.get(cls.path, data={"size":222222})
        records = response.json()
        return pd.DataFrame.from_records(records)
    
    # GET N ENTRIES
    def get_entries(self, nentries=1):
        response = session.get(self.path, data={"size": nentries})
        records = response.json()
        return pd.DataFrame.from_records(records)

    # POST
    def new(self):
        data = self.to_dict()
        data.pop("id")
        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        response = session.post(self.path, data=json.dumps(data), headers=headers)
        return response.json()

    # PUT
    def update(self):
        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        response = session.put(self.path, data=self.to_json(), headers=headers)
        return response.json()

    # COUNT
    @classmethod
    def count(cls):
        path = cls.path + "/" + "count"
        response = session.get(path)
        return response.json()   

    # DELETE
    def delete(self):
        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        path = self.path + "/" + str(self.id)
        response = session.delete(path)

    # GET FROM ID
    def get_from_id(self, id_value):
        path = self.path + "/" + str(id_value)
        response = session.get(path)
        if response.status_code == 200:
            data = response.json()
            self.__init__(**data)
        return response.json()

    def to_json(self):
        return json.dumps(self, default=lambda o: {key.replace("_", ""): val for key, val in o.__dict__.items()}, 
            sort_keys=True) 

    def to_dict(self):
        return {key.replace("_", ""): val for key, val in self.__dict__.items()}