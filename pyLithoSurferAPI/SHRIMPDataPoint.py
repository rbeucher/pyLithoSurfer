from . import session, URL_BASE
import json
import pandas as pd


class SHRIMPDataPoint(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @classmethod
    def get_all(cls):
        path = URL_BASE+'/api/shrimp-data-points/'
        response = session.get(path, data={"size":200})
        records = response.json()
        return pd.DataFrame.from_records(records)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def ageAverageKindId(self):
        return self._ageAverageKindId

    @ageAverageKindId.setter
    def ageAverageKindId(self, value):
        self._ageAverageKindId = value

    @property
    def ageAverageKindName(self):
        return self._ageAverageKindName

    @ageAverageKindName.setter
    def ageAverageKindName(self, value):
        self._ageAverageKindName = value

    @property
    def ageErrorMax(self):
        return self._ageErrorMax

    @ageErrorMax.setter
    def ageErrorMax(self, value):
        self._ageErrorMax = value

    @property
    def ageErrorMin(self):
        return self._ageErrorMin

    @ageErrorMin.setter
    def ageErrorMin(self, value):
        self._ageErrorMin = value

    @property
    def analyteId(self):
        return self._analyteId

    @analyteId.setter
    def analyteId(self, value):
        self._analyteId = value

    @property
    def analyteName(self):
        return self._analyteName

    @analyteName.setter
    def analyteName(self, value):
        self._analyteName = value

    @property
    def errorAgeTypeId(self):
        return self._errorAgeTypeId

    @errorAgeTypeId.setter
    def errorAgeTypeId(self, value):
        self._errorAgeTypeId = value

    @property
    def errorAgeTypeName(self):
        return self._errorAgeTypeName

    @errorAgeTypeName.setter
    def errorAgeTypeName(self, value):
        self._errorAgeTypeName = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def mineralId(self):
        return self._mineralId

    @mineralId.setter
    def mineralId(self, value):
        self._mineralId = value

    @property
    def mineralName(self):
        return self._mineralName

    @mineralName.setter
    def mineralName(self, value):
        self._mineralName = value

    @property
    def mountId(self):
        return self._mountId

    @mountId.setter
    def mountId(self, value):
        self._mountId = value

    @property
    def ngrains(self):
        return self._ngrains

    @ngrains.setter
    def ngrains(self, value):
        self._ngrains = value

    @property
    def nspots(self):
        return self._nspots

    @nspots.setter
    def nspots(self, value):
        self._nspots = value

    @property
    def singleGrainId(self):
        return self._singleGrainId

    @singleGrainId.setter
    def singleGrainId(self, value):
        self._singleGrainId = value

    @property
    def singleGrainName(self):
        return self._singleGrainName

    @singleGrainName.setter
    def singleGrainName(self, value):
        self._singleGrainName = value

    def info(self):
        if self.id:
            path = URL_BASE+'/api/shrimp-data-points/' + str(self.id)
            response = session.get(path)
            if response.status_code == 200:
                return response.json()

    def get_from_id(self, id_value):
        path = URL_BASE+'/api/shrimp-data-points/' + str(id_value)
        response = session.get(path)

        if response.status_code == 200:
            data = response.json()
            self.__init__(**data)
        return response.json()

    def push_new_entry(self):
        path = URL_BASE+'/api/shrimp-data-points/'
        data = self.to_dict()
        data.pop("id")
        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        response = session.post(path, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            id_value = response.json()["id"]
            print(f"SHRIMP DATA POINT Entry with id={id_value} has been successfully created")
        else:
            print("Could not create Entry")
        return response.json()

    def update_entry(self):
        path = URL_BASE+'/api/shrimp-data-points/'
        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        response = session.put(path, data=self.to_json(), headers=headers)
        if response.status_code == 200:
            id_value = response.json()["id"]
            print(f"SHRIMP Data Entry with id={id_value} has been successfully updated")
        else:
            print("Could not update Entry")
        return response.json()

    def delete_entry(self):
        path = URL_BASE+'/api/shrimp-data-points/' + str(self.id)
        response = session.delete(path)
        if response.status_code == 200:
            print(f"SHRIMP DATA POINT Entry with id={self.id} has been deleted")
        if response.status_code == 500:
            print("Cannot find SHRIMP DATA POINT Entry with id={id_value}")
        return response.json()

    @classmethod
    def get_shrimp_data_count(cls):
        path = URL_BASE+'/api/shrimp-data-points/count'
        response = session.get(path)
        return response.json()   

    def to_json(self):
        return json.dumps(self, default=lambda o: {key.replace("_", ""): val for key, val in o.__dict__.items()}, 
            sort_keys=True) 

    def to_dict(self):
        return {key.replace("_", ""): val for key, val in self.__dict__.items()}