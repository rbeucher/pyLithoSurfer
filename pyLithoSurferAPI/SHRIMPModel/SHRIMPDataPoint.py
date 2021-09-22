from pyLithoSurferAPI import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import DataPoint
import json


class SHRIMPDataPoint(APIRequests):
        
    path = URL_BASE+'/api/shrimp-data-points'


class SHRIMPDataPointCRUD(APIRequests):

    path = URL_BASE+'/api/shrimp/shrimp-datapoints'

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

        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = func(self.path, data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        response.raise_for_status() 
        response = response.json()
        
        self.id = response["id"]
        
        self.dataPoint.id = response["dataPointDTO"]["id"]
        self.dataPointID = self.dataPoint.id
        self.shrimpDataPoint.id = response["shrimpdataPointDTO"]["id"]
        
        return response

    def new(self):
        return self._send_payload(session.post)
    
    def update(self):
        return self._send_payload(session.put)
    