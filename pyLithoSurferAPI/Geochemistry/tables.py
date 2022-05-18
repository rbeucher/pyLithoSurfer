from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import DataPoint
import json

class GCDataPoint(APIRequests):

    API_PATH = "/api/gc-data-points"


class GCDataPointCRUD(APIRequests):

    API_PATH = "/api/geochem/GCDataPoint"

    def __init__(self, dataPoint: DataPoint, gcDataPoint: GCDataPoint, dataPointID=None, id=None):

        self.dataPoint = dataPoint
        self.gcDataPoint = gcDataPoint
        self.dataPointID = dataPointID
        self.id = id 

    def _send_payload(self, func):
        data = {}
        
        dataPoint = self.dataPoint.to_dict()
        data["dataPointDTO"] = dataPoint
        gcdatapoint = self.gcDataPoint.to_dict()
        data["gcdataPointDTO"] = gcdatapoint 
        data["dataPointId"] = self.dataPointID
        data["dataPointDTO"]["gcdataPointId"] = self.id
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
        self.gcDataPoint.id = response["gcdataPointDTO"]["id"]
        
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
        gc_args = records["gcdataPointDTO"]
        # Create DataPoint
        datapoint = DataPoint(**dpts_args)
        # Create GCDataPoint
        gc_datapoint = GCDataPoint(**gc_args)

        # Use GCDataPointCRUD to create the Datapoint and
        # the gcdatapoint
        obj =  GCDataPointCRUD(datapoint, gc_datapoint) 
        obj.id = gc_datapoint.id
        obj.dataPointID = datapoint.id
        obj.dataPoint.dataEntityId = gc_datapoint.id
        obj.dataPoint.gcdatapoint_id = gc_datapoint.id
        return obj


class GCAliquotCRUD(APIRequests):

    API_PATH = "/api/geochem/GCAliquot"


class ElementalConcentrationCRUD(APIRequests):

    API_PATH = "/api/geochem/ElementalConcentration"


class OxideConcentrationCRUD(APIRequests):

    API_PATH = "/api/geochem/OxideConcentration"



