
from pyLithoSurferAPI.REST import APIRequests


class FTBinnedLengthData(APIRequests):

    API_PATH = "/api/fissiontrack/ft/FTBinnedLengthData"


class FTCountData(APIRequests):

    API_PATH = "/api/fissiontrack/ft-count-data"


class FTDataPoint(APIRequests):

    API_PATH = "/api/ft-data-points"


class FTDataPointCRUD(APIRequests):

    API_PATH = "/api/fissiontrack/ft/FTDataPoint"

    def __init__(self, dataPoint: DataPoint, ftDataPoint: ftDataPoint, dataPointID=None, id=None):

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

        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = func(self.path(), data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        response.raise_for_status() 
        response = response.json()
        
        self.id = response["id"]
        
        self.dataPoint.id = response["dataPointDTO"]["id"]
        self.dataPointID = self.dataPoint.id
        self.ftDataPoint.id = response["ftdataPointDTO"]["id"]
        
        return response

    def new(self):
        return self._send_payload(session.post)
    
    def update(self):
        return self._send_payload(session.put)


class FTLengthData(APIRequests):

    API_PATH = "/api/fissiontrack/ft-length-data"


class FTRawDataPoint(APIRequests):

    API_PATH = "/api/ft-raw-data-points"


class FTRawDataPointCRUD(APIRequests):

    API_PATH = "/api/fissiontrack/ftraw-datapoints"
    
    def __init__(self, dataPoint: DataPoint, ftrawDataPoint: ftrawDataPoint, dataPointID=None, id=None):

        self.dataPoint = dataPoint
        self.ftrawDataPoint = ftrawDataPoint
        self.dataPointID = dataPointID
        self.id = id 

    def _send_payload(self, func):
        data = {}
        
        dataPoint = self.dataPoint.to_dict()
        data["dataPointDTO"] = dataPoint
        ftrawDataPoint = self.ftrawDataPoint.to_dict()
        data["ftrawdataPointDTO"] = ftrawDataPoint 
        data["dataPointId"] = self.dataPointID
        data["dataPointDTO"]["ftrawDataPointId"] = self.id
        data["id"] = self.id

        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = func(self.path(), data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        response.raise_for_status() 
        response = response.json()
        
        self.id = response["id"]
        
        self.dataPoint.id = response["dataPointDTO"]["id"]
        self.dataPointID = self.dataPoint.id
        self.ftrawDataPoint.id = response["ftrawDataPointDTO"]["id"]
        
        return response

    def new(self):
        return self._send_payload(session.post)
    
    def update(self):
        return self._send_payload(session.put)


class FTSingleGrain(APIRequests):

    API_PATH = "/api/fissiontrack/ft/FTSingleGrain"