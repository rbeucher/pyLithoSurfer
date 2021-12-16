
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.uploader import Uploader

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


class LPerson2DataPointRole(APIRequests):

    API_PATH = "/api/core/l-person-2-data-point-roles"


class LPerson2SampleRole(APIRequests):

    API_PATH = "/api/core/l-person-2-sample-roles"


class Person2Data(APIRequests):

    API_PATH = "/api/core/person-2-data-points"


class Person2Sample(APIRequests):

    API_PATH = "/api/core/person-2-samples"


class StratigraphicUnit(APIRequests, Uploader):

    API_PATH = "/api/core/stratigraphic-units"

    @classmethod
    def get_id_from_name(cls, name):
        import pandas as pd
        
        query = {"name.contains": name}
        response = cls.query(query)
        records = response.json()
        if len(records) > 1:
            df = pd.DataFrame.from_records(records)
            print(df)
            chosen_id = input("Choose id:")
            return chosen_id
        elif len(records):
            return records[0]["id"]
        else:
            raise ValueError(f"cannot find {name}")


class Statement(APIRequests):
        
    API_PATH = '/api/statements'


class Material(APIRequests):

    API_PATH = '/api/core/materials'


class Machine(APIRequests):

    API_PATH = '/api/core/machines'

