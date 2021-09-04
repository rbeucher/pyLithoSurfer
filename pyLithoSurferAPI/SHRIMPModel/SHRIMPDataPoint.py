from pyLithoSurferAPI import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import DataPoint
from pyLithoSurferAPI.REST import check_response
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

     # POST
    def new(self, debug=False):
        data = {}
        
        dataPoint = self.dataPoint.to_dict()
        if "id" in dataPoint.keys():
            dataPoint.pop("id")
        data["dataPointDTO"] = dataPoint
        shrimpDataPoint = self.shrimpDataPoint.to_dict()
        if "id" in shrimpDataPoint.keys():
            shrimpDataPoint.pop("id")
        data["shrimpdataPointDTO"] = shrimpDataPoint 

        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = session.post(self.path, data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        if debug:
            print(response.json())
        check_response(response)
        response = response.json()
        if "id" in response.keys():
            self.id = response["id"]
        if "dataPointDTO" in response.keys() and "id" in response["dataPointDTO"].keys():
            self.dataPoint.id = response["dataPointDTO"]["id"]
            self.dataPointID = self.dataPoint.id
        if "shrimpdataPointDTO" in response.keys() and "id" in response["shrimpdataPointDTO"].keys():
            self.shrimpDataPoint.id = response["shrimpdataPointDTO"]["id"]
        return response   
    