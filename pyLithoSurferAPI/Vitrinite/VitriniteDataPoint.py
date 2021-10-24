from pyLithoSurferAPI import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import DataPoint
import json


class VitriniteDataPoint(APIRequests):
        
    path = URL_BASE+'/api/vitrinite-data-points'


class VitriniteDataPointCRUD(APIRequests):

    path = URL_BASE+'/api/vitrinite/vitrinite-datapoints'

    def __init__(self, dataPoint: DataPoint, vitriniteDataPoint: VitriniteDataPoint, dataPointID=None, id=None):

        self.dataPoint = dataPoint
        self.vitriniteDataPoint = vitriniteDataPoint
        self.dataPointID = dataPointID
        self.id = id 

    def _send_payload(self, func):
        data = {}
        
        dataPoint = self.dataPoint.to_dict()
        data["dataPointDTO"] = dataPoint
        vitriniteDataPoint = self.vitriniteDataPoint.to_dict()
        data["vitriniteDataPointDTO"] = vitriniteDataPoint 
        data["dataPointId"] = self.dataPointID
        data["dataPointDTO"]["vitriniteDataPointId"] = self.id
        data["id"] = self.id

        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = func(self.path, data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        response.raise_for_status() 
        response = response.json()
        
        self.id = response["id"]
        
        self.dataPoint.id = response["dataPointDTO"]["id"]
        self.dataPointID = self.dataPoint.id
        self.vitriniteDataPoint.id = response["vitriniteDataPointDTO"]["id"]
        
        return response

    def new(self):
        return self._send_payload(session.post)
    
    def update(self):
        return self._send_payload(session.put)
    