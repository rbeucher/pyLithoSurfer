from pyLithoSurferAPI import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import GeoeventAtAge
from pyLithoSurferAPI.core.tables import Statement
import json


class SHRIMPAge(APIRequests):
        
    path = URL_BASE+'/api/shrimp-ages'


class SHRIMPAgeCRUD(APIRequests):

    path = URL_BASE+'/api/shrimp/shrimp-ages'

    def __init__(self, geoeventAtAge: GeoeventAtAge, statement: Statement, shrimpAge: SHRIMPAge, id=None):

        self.geoeventAtAge = geoeventAtAge
        self.statement = statement
        self.shrimpAge = shrimpAge
        self.id = id 

    def _send_payload(self, func):

        data = {}
        data["geoEventAtAgeExtendsStatementDTO"] = {}

        geoeventAtAge = self.geoeventAtAge.to_dict()
        data["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"] = geoeventAtAge
         
        statement = self.statement.to_dict()
        data["geoEventAtAgeExtendsStatementDTO"]["statementDTO"] = statement
        data["geoEventAtAgeExtendsStatementDTO"]["statementDTO"]["geoEventAtAgeId"] = geoeventAtAge["id"] 

        shrimpAge = self.shrimpAge.to_dict()
        data["shrimpageDTO"] = shrimpAge

        data["geoEventAtAgeExtendsStatementDTO"]["id"] = shrimpAge["id"]
        data["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"]["id"] = geoeventAtAge["id"]
        data["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"]["shrimpageId"] = shrimpAge["id"]

        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = func(self.path, data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        response.raise_for_status() 
        response = response.json()
        
        if "id" in response.keys():
            self.id = response["id"]
        
        if "geoeventAtAge" in response.keys() and "id" in response["geoeventAtAge"].keys():
            self.geoeventAtAge.id = response["geoeventAtAge"]["id"]
            self.geoeventAtAgeID = self.geoeventAtAge.id
        
        if "statement" in response.keys() and "id" in response["statement"].keys():
            self.statement.id = response["statement"]["id"]
        
        if "shrimpAge" in response.keys() and "id" in response["shrimpAge"].keys():
            self.shrimpAge.id = response["shrimpAge"]["id"]
        
        return response  

    def new(self):
        return self._send_payload(session.post)
    
    def update(self):
        return self._send_payload(session.put) 