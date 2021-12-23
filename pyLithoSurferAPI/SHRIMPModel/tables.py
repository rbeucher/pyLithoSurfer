from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import GeoeventAtAge
from pyLithoSurferAPI.core.tables import Statement
from pyLithoSurferAPI.core.tables import DataPoint
import json


class SHRIMPAge(APIRequests):
        
    API_PATH = '/api/shrimp-ages'


class SHRIMPAgeCRUD(APIRequests):

    API_PATH = '/api/shrimp/shrimp-ages'

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

        headers = APIRequests.SESSION.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = func(self.path(), data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        response.raise_for_status() 
        response = response.json()
        
        self.id = response["id"]
        self.geoeventAtAge.id = response["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"]["id"]
        self.geoeventAtAgeId = self.geoeventAtAge.id
        self.statement.id = response["geoEventAtAgeExtendsStatementDTO"]["statementDTO"]["id"]
        self.shrimpAge.id = response["shrimpageDTO"]["id"]
        
        return response  

    def new(self):
        return self._send_payload(APIRequests.SESSION.post)
    
    def update(self):
        return self._send_payload(APIRequests.SESSION.put) 


class SHRIMPDataPoint(APIRequests):
        
    API_PATH = '/api/shrimp-data-points'


class SHRIMPDataPointCRUD(APIRequests):

    API_PATH = '/api/shrimp/shrimp-datapoints'

    def __init__(self, dataPoint: DataPoint, shrimpDataPoint: SHRIMPDataPoint, dataPointID=None, id=None):

        self.dataPoint = dataPoint
        self.shrimpDataPoint = shrimpDataPoint
        self.dataPointID = dataPointID
        self.id = id 

    def _send_payload(self, func):
        data = {}
        
        dataPoint = self.dataPoint.to_dict()
        data["dataPointDTO"] = dataPoint
        shrimpDataPoint = self.shrimpDataPoint.to_dict()
        data["shrimpdataPointDTO"] = shrimpDataPoint 
        data["dataPointId"] = self.dataPointID
        data["dataPointDTO"]["shrimpdataPointId"] = self.id
        data["id"] = self.id

        headers = APIRequests.SESSION.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = func(self.path(), data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        response.raise_for_status() 
        response = response.json()
        
        self.id = response["id"]
        
        self.dataPoint.id = response["dataPointDTO"]["id"]
        self.dataPointID = self.dataPoint.id
        self.shrimpDataPoint.id = response["shrimpdataPointDTO"]["id"]
        
        return response

    def new(self):
        return self._send_payload(APIRequests.SESSION.post)
    
    def update(self):
        return self._send_payload(APIRequests.SESSION.put)


class SHRIMPSpot(APIRequests):
        
    API_PATH = '/api/shrimp-spots'

SHRIMPSpotCRUD = SHRIMPSpot
    