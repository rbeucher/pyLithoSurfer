
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.uploader import Uploader
from pyLithoSurferAPI.utilities import NumpyEncoder
import json

class Archive(APIRequests):

    API_PATH = "/api/core/archives"


class DataPoint(APIRequests):

    API_PATH = "/api/core/data-points"


class Flag(APIRequests):

    API_PATH = "/api/core/flags"


class Funding(APIRequests):

    API_PATH = "/api/core/fundings"


class FundingBody(APIRequests):

    API_PATH = "/api/core/funding-bodies"


class GeoeventAtAge(APIRequests):
        
    API_PATH = '/api/geo-event-at-ages'


class Institution(APIRequests):

    API_PATH = "/api/institutionss"


class Lab2Data(APIRequests):

    API_PATH = "/api/core/lab-2-data-points"


class Lit2Data(APIRequests):

    API_PATH = "/api/core/literature-2-data-points"


class Lit2Sample(APIRequests):

    API_PATH = "/api/core/literature-2-samples"


class Literature(APIRequests):

    API_PATH = '/api/core/literature/'

    @classmethod
    def get_from_doi(cls, doi):
        import requests
        response = requests.get('https://api.crossref.org/works/' + str(doi), 
                                headers={'Accept': 'application/json'})
        if response.status_code == 200:
            data = response.json()["message"]
            return data
        return response.json()


class Location(APIRequests):

    API_PATH = "/api/locations"


class Person2Data(APIRequests):

    API_PATH = "/api/core/person-2-data-points"


class Person2Sample(APIRequests):

    API_PATH = "/api/core/person-2-samples"


class Funding2Sample(APIRequests):

    API_PATH = "/api/core/funding-2-samples"


class Funding2Data(APIRequests):

    API_PATH = "/api/core/funding-2-data-points"


class StratigraphicUnit(APIRequests):

    API_PATH = "/api/core/stratigraphic-units"

    @classmethod
    def get_id_from_name(cls, name):
        import pandas as pd
        
        query = {"name.equals": name}
        response = cls.query(query)
        records = response.json()
        if len(records) > 1:
            df = pd.DataFrame.from_records(records)
            print(df, name)
            chosen_id = input("Choose id:")
            return chosen_id
        elif len(records):
            return records[0]["id"]
        else:
            print(f"cannot find {name}")


class Statement(APIRequests):
        
    API_PATH = '/api/statements'


class Material(APIRequests):

    API_PATH = '/api/core/materials'


class Machine(APIRequests):

    API_PATH = '/api/core/machines'


class Person(APIRequests):

    API_PATH = "/api/core/people"


class Sample(APIRequests):

    API_PATH = "/api/samples"

class SampleWithLocation(APIRequests):

    API_PATH = '/api/core/sample-with-locations'

    def __init__(self, location: Location, sample: Sample, id = None, auto_set_elevation: bool = False ):

        self.location = location
        self.sample = sample
        self.auto_set_elevation = auto_set_elevation
        self.id = id 

    def _send_payload(self, func):
        data = {}
        
        location = self.location.to_dict()
        data["locationDTO"] = location

        sample = self.sample.to_dict()
        data["sampleDTO"] = sample
        data["autoSetElevationWriteConfig"] = self.auto_set_elevation
        data["id"] = self.id

        headers = APIRequests.SESSION.headers
        response = func(self.path(), data=json.dumps(data, cls=NumpyEncoder), headers=headers)

        try:
            response.raise_for_status()
        except Exception as e:
            print(json.dumps(data, cls=NumpyEncoder))
            print(response.json())
            raise e

        records = response.json()
        self.id = records["id"]
        self.location.id = records["locationDTO"]["id"]
        self.sample.id = records["sampleDTO"]["id"]
        return records   
    
    def new(self):
        return self._send_payload(APIRequests.SESSION.post)
    
    def update(self):
        return self._send_payload(APIRequests.SESSION.put)


class DatapointProperty(APIRequests):

    API_PATH = "/api/core/DatapointProperty"
