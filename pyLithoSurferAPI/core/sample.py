from pyLithoSurferAPI import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.REST import check_response
from pyLithoSurferAPI.core.tables import Location
from pyLithoSurferAPI.utilities import NumpyEncoder
import json

class Sample(APIRequests):

    path = URL_BASE + "/api/samples"

class SampleWithLocation(APIRequests):

    path = URL_BASE+'/api/core/sample-with-locations'

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

        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = func(self.path, data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        check_response(response)

        records = response.json()
        self.id = records["id"]
        self.location.id = records["locationDTO"]["id"]
        self.sample.id = records["sampleDTO"]["id"]
        return records   
    
    def new(self):
        return self._send_payload(session.post)
    
    def update(self):
        return self._send_payload(session.put)