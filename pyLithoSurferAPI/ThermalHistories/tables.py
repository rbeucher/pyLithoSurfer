
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import DataPoint
import json


class THistCRUD(APIRequests):

    API_PATH = "/api/th/THist"


class THistInputCRUD(APIRequests):

    API_PATH = "/api/th/THistInput"


class THistNickpointCRUD(APIRequests):

    API_PATH = "/api/th/THistNickpoint"


class THModelConstraintCRUD(APIRequests):

    API_PATH = "/api/th/THModelConstraint"


class THPredResultCRUD(APIRequests):

    API_PATH = "/api/th/THPredResult"


class THPredResultCRUD(APIRequests):

    API_PATH = "/api/th/THPredResult"


class THDataPoint(APIRequests):

    API_PATH = "/api/THDataPoint"


class THDataPointCRUD(APIRequests):

    API_PATH = "/api/th/THDataPoint"

    def __init__(self, dataPoint: DataPoint, thDataPoint: THDataPoint, dataPointID=None, id=None):

        self.dataPoint = dataPoint
        self.thDataPoint = thDataPoint
        self.dataPointID = dataPointID
        self.id = id 

    def _send_payload(self, func):
        data = {}
        
        dataPoint = self.dataPoint.to_dict()
        data["dataPointDTO"] = dataPoint
        thDataPoint = self.thDataPoint.to_dict()
        data["extendingDataPointDTO"] = thDataPoint 
        data["dataPointId"] = self.dataPointID
        data["dataPointDTO"]["thdataPointId"] = self.id
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
        self.thDataPoint.id = response["extendingDataPointDTO"]["id"]
        
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
        th_args = records["extendingDataPointDTO"]
        # Create DataPoint
        datapoint = DataPoint(**dpts_args)
        # Create FTDataPoint
        th_datapoint = THDataPoint(**th_args)

        # Use THDataPointCRUD to create the Datapoint and
        # the THDatapoint
        obj =  THDataPointCRUD(datapoint, th_datapoint) 
        obj.id = th_datapoint.id
        obj.dataPointID = datapoint.id
        obj.dataPoint.dataEntityId = th_datapoint.id
        obj.dataPoint.ftdatapoint_id = th_datapoint.id
        return obj

