from pyLithoSurferAPI import URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import pandas as pd


class Person(APIRequests):

    path = URL_BASE + "/api/core/people"


    @classmethod
    def get_person_id(cls, firstName=None, name=None):
    
        firstNameQuery = {}
        if firstName:
            firstNameQuery = {"firstName.contains": firstName}
        nameQuery = {}
        if name:
            nameQuery = {"name.contains": name}
        query = {**firstNameQuery, **nameQuery}
        response = cls.query(query)
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