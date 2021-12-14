from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.core.tables import Location
from pyLithoSurferAPI.utilities import NumpyEncoder
import json

class Sample(APIRequests):

    API_PATH = "/api/samples"

class SampleWithLocation(APIRequests):

    API_PATH = '/api/core/sample-with-locations'

    def __init__(self, location: Location, sample: Sample, id = None):

        self.location = location
        self.sample = sample
        self.id = id 

    def _send_payload(self, func):
        data = {}
        
        location = self.location.to_dict()
        data["locationDTO"] = location

        sample = self.sample.to_dict()
        data["sampleDTO"] = sample
        data["id"] = self.id

        headers = APIRequests.SESSION.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = func(self.path(), data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        response.raise_for_status()

        records = response.json()
        self.id = records["id"]
        self.location.id = records["locationDTO"]["id"]
        self.sample.id = records["sampleDTO"]["id"]
        return records   
    
    def new(self):
        return self._send_payload(APIRequests.SESSION.post)
    
    def update(self):
        return self._send_payload(APIRequests.SESSION.put)