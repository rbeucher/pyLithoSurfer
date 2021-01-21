from . import session, URL_BASE
from abc import ABC
import json
import pandas as pd


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
    if status_code == 200:
        return True
    elif status_code == 401:
        raise(UnauthorizedException)
    elif status_code == 403:
        raise(ForbiddenException)
    elif status_code == 404:
        raise(NotFoundException)
    elif status_code == 500:
        raise(ItemNotFoundException)


class APIRequests(ABC):

    check_duplicates = []

    # GET ALL
    @classmethod
    def get_all(cls):
        response = session.get(cls.path, data={"size":222222})
        check_response(response)
        records = response.json()
        return pd.DataFrame.from_records(records)
    
    # GET N ENTRIES
    def get_entries(self, nentries=1):
        response = session.get(self.path, data={"size": nentries})
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

        if hasattr(self, "name"):
            name = self.name.replace(" ", "%20")
            response = self.get_from_query(f"name.in={name}")
            
            if check_response(response):
                new_args = response.json()
                if len(new_args) >= 1:
                    new_id = new_args[0].pop("id")
                    self.__init__(**new_args[0])
                    self.id = new_id
                    return response.json()

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
        return response.json()

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
        return response.json()

    # GET FROM ID
    def get_from_id(self, id_value):
        path = self.path + "/" + str(id_value)
        response = session.get(path)
        check_response(response)
        data = response.json()
        self.__init__(**data)
        return response.json()

    def get_from_query(self, query):
        headers = session.headers
        headers["Accept"] = "application/json"
        path = self.path + "?" + str(query)
        print(path)
        response = session.get(path)
        return response

    def to_json(self):
        return json.dumps(self, default=lambda o: {key.replace("_", ""): val for key, val in o.__dict__.items()}, 
            sort_keys=True) 

    def to_dict(self):
        return {key.replace("_", ""): val for key, val in self.__dict__.items()}