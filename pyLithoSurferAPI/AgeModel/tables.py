from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import DataPoint
from pyLithoSurferAPI.core.tables import GeoeventAtAge
from pyLithoSurferAPI.core.tables import Statement
import json


class AgeDataPoint(APIRequests):
        
    API_PATH = '/api/age-data-points'


class AgeDataPointCRUD(APIRequests):

    API_PATH = '/api/age/age-datapoints'

    def __init__(self, dataPoint: DataPoint, ageDataPoint: AgeDataPoint, geoeventAtAge: GeoeventAtAge, statement: Statement,  dataPointID=None, id=None):

        self.dataPoint = dataPoint
        self.ageDataPoint = ageDataPoint
        self.dataPointID = dataPointID
        self.geoeventAtAge = geoeventAtAge
        self.statement = statement
        self.id = id 

    def _send_payload(self, func):
        data = {}
        
        ageDataPoint = self.ageDataPoint.to_dict()
        data["ageDataPointDTO"] = ageDataPoint 
        dataPoint = self.dataPoint.to_dict()
        data["dataPointDTO"] = dataPoint
        data["dataPointId"] = self.dataPointID
        data["dataPointDTO"]["ageDataPointId"] = self.id
        data["id"] = self.id
        data["geoEventAtAgeExtendsStatementDTO"] = {}

        geoeventAtAge = self.geoeventAtAge.to_dict()
        data["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"] = geoeventAtAge
         
        statement = self.statement.to_dict()
        data["geoEventAtAgeExtendsStatementDTO"]["statementDTO"] = statement
        data["geoEventAtAgeExtendsStatementDTO"]["statementDTO"]["geoEventAtAgeId"] = geoeventAtAge["id"] 

        data["geoEventAtAgeExtendsStatementDTO"]["id"] = ageDataPoint["id"]
        data["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"]["id"] = geoeventAtAge["id"]

        headers = APIRequests.SESSION.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = func(self.path(), data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        response.raise_for_status() 
        response = response.json()
        
        self.id = response["id"]
        
        self.dataPoint.id = response["dataPointDTO"]["id"]
        self.dataPointID = self.dataPoint.id
        self.ageDataPoint.id = response["ageDataPointDTO"]["id"]
        self.geoeventAtAge.id = response["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"]["id"]
        self.geoeventAtAgeId = self.geoeventAtAge.id
        self.statement.id = response["geoEventAtAgeExtendsStatementDTO"]["statementDTO"]["id"]
        
        return response

    def new(self):
        return self._send_payload(APIRequests.SESSION.post)
    
    def update(self):
        return self._send_payload(APIRequests.SESSION.put)
    