
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import DataPoint
import json


class FTBinnedLengthDataCRUD(APIRequests):

    API_PATH = "/api/fissiontrack/FTBinnedLengthData"


class FTCountDataCRUD(APIRequests):

    API_PATH = "/api/fissiontrack/ft-count-data"


class FTDataPoint(APIRequests):

    API_PATH = "/api/ft-data-points"


class FTDataPointCRUD(APIRequests):

    API_PATH = "/api/fissiontrack/FTDataPoint"

    def __init__(self, dataPoint: DataPoint, ftDataPoint: FTDataPoint, dataPointID=None, id=None):

        self.dataPoint = dataPoint
        self.ftDataPoint = ftDataPoint
        self.dataPointID = dataPointID
        self.id = id 

    def _send_payload(self, func):
        data = {}
        
        dataPoint = self.dataPoint.to_dict()
        data["dataPointDTO"] = dataPoint
        ftDataPoint = self.ftDataPoint.to_dict()
        data["ftdataPointDTO"] = ftDataPoint 
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
        self.ftDataPoint.id = response["ftdataPointDTO"]["id"]
        
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
        ft_args = records["ftdataPointDTO"]
        # Create DataPoint
        datapoint = DataPoint(**dpts_args)
        # Create FTDataPoint
        ft_datapoint = FTDataPoint(**ft_args)

        # Use FTDataPointCRUD to create the Datapoint and
        # the FTDatapoint
        obj =  FTDataPointCRUD(datapoint, ft_datapoint) 
        obj.id = ft_datapoint.id
        obj.dataPointID = datapoint.id
        obj.dataPoint.dataEntityId = ft_datapoint.id
        obj.dataPoint.ftdatapoint_id = ft_datapoint.id
        return obj

class FTLengthDataCRUD(APIRequests):

    API_PATH = "/api/fissiontrack/ft-length-data"


class FTSingleGrainCRUD(APIRequests):

    API_PATH = "/api/fissiontrack/FTSingleGrain"