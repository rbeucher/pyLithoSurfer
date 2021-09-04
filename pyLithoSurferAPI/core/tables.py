from pyLithoSurferAPI import URL_BASE
from pyLithoSurferAPI.REST import APIRequests


class Archive(APIRequests):

    path = URL_BASE + "/api/core/archives"


class DataPoint(APIRequests):

    path = URL_BASE + "/api/core/data-points"
    mandatory_args = ["dataStructure"]


class Flag(APIRequests):

    path = URL_BASE + "/api/core/flags"


class Funding(APIRequests):

    path = URL_BASE + "/api/core/fundings"


class FundingBody(APIRequests):

    path = URL_BASE + "/api/core/funding-bodies"


class GeoeventAtAge(APIRequests):
        
    path = URL_BASE+'/api/geo-event-at-ages'


class Institution(APIRequests):

    path = URL_BASE + "/api/institutionss"


class Lab2Data(APIRequests):

    path = URL_BASE + "/api/lab-2-data-points"


class Lit2Data(APIRequests):

    path = URL_BASE + "/api/core/literature-2-data-points"


class Lit2Sample(APIRequests):

    path = URL_BASE + "/api/core/literature-2-samples"


class Literature(APIRequests):

    path =  URL_BASE+'/api/core/literature/'

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

    path = URL_BASE + "/api/locations"


class LPerson2DataPointRole(APIRequests):

    path = URL_BASE + "/api/core/l-person-2-data-point-roles"


class LPerson2SampleRole(APIRequests):

    path = URL_BASE + "/api/core/l-person-2-sample-roles"


class Person2Data(APIRequests):

    path = URL_BASE + "/api/core/person-2-data-points"


class Person2Sample(APIRequests):

    path = URL_BASE + "/api/core/person-2-samples"


class StratigraphicUnit(APIRequests):

    path = URL_BASE + "/api/core/stratigraphic-units"

    @classmethod
    def get_id_from_name(cls, name):
        import pandas as pd
        
        query = {"name.contains": name}
        response = cls.get_from_query(query)
        records = response.json()
        if len(records) > 1:
            df = pd.DataFrame.from_records(records)
            print(df)
            chosen_id = input("Choose id:")
            return chosen_id
        else:
            return records[0]["id"]


class Statement(APIRequests):
        
    path = URL_BASE+'/api/statements'

