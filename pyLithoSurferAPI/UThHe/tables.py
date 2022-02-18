
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import DataPoint
import json


class HeWholeGrainCRUD(APIRequests):

    API_PATH = "/api/helium/HeWholeGrain"


class HeDataPoint(APIRequests):

    API_PATH = "/api/he-data-points"


class HeInSituCRUD(APIRequests):

    API_PATH = "/api/helium/HeInSitu"


class HeDataPointCRUD(APIRequests):

    API_PATH = "/api/helium/HeDataPoint"

    def __init__(self, dataPoint: DataPoint, heDataPoint: HeDataPoint, dataPointID=None, id=None):

        self.dataPoint = dataPoint
        self.heDataPoint = heDataPoint
        self.dataPointID = dataPointID
        self.id = id 

    def _send_payload(self, func):
        data = {}
        
        dataPoint = self.dataPoint.to_dict()
        data["dataPointDTO"] = dataPoint
        heDataPoint = self.heDataPoint.to_dict()
        data["heDataPointDTO"] = heDataPoint 
        data["dataPointId"] = self.dataPointID
        data["dataPointDTO"]["ftdataPointId"] = self.id
        data["id"] = self.id

        headers = APIRequests.SESSION.headers
        response = func(self.path(), data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        try:
            response.raise_for_status()
        except Exception as e:
            print(json.dumps(data, cls=NumpyEncoder))
            print(response.json())
            raise e
        response = response.json()
        
        self.id = response["id"]
        
        self.dataPoint.id = response["dataPointDTO"]["id"]
        self.dataPointID = self.dataPoint.id
        self.heDataPoint.id = response["hedataPointDTO"]["id"]
        
        return response

    def new(self):
        return self._send_payload(APIRequests.SESSION.post)
    
    def update(self):
        return self._send_payload(APIRequests.SESSION.put)

    @classmethod
    def get_from_id(cls, id_value):
        path = cls.path() + "/" + str(id_value)
        response = APIRequests.SESSION.get(path)
        response.raise_for_status()
        records = response.json()
        dpts_args = records["dataPointDTO"]
        he_args = records["hedataPointDTO"]
        # Create DataPoint
        datapoint = DataPoint(**dpts_args)
        # Create FTDataPoint
        he_datapoint = HeDataPoint(**ft_args)

        # Use FTDataPointCRUD to create the Datapoint and
        # the FTDatapoint
        obj =  HeDataPointCRUD(datapoint, he_datapoint) 
        obj.id = he_datapoint.id
        obj.dataPointID = datapoint.id
        obj.dataPoint.dataEntityId = he_datapoint.id
        obj.dataPoint.ftdatapoint_id = he_datapoint.id
        return obj

