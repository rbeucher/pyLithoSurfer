from pyLithoSurferAPI import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.REST import check_response
from pyLithoSurferAPI.core.tables import Location
from pyLithoSurferAPI.utilities import NumpyEncoder
import json

class Sample(APIRequests):

    path = URL_BASE + "/api/samples"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


class SampleWithLocation(APIRequests):

    path = URL_BASE+'/api/core/sample-with-locations'

    def __init__(self, location: Location, sample: Sample, id = None):

        self.location = location
        self.sample = sample

        self.id = id 

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value: Location):
        self._location = value
    
    @property
    def sample(self):
        return self._sample

    @sample.setter
    def sample(self, value: Sample):
        self._sample = value

    def new(self, debug=False):
        data = {}
        
        location = self.location.to_dict()
        location.pop("id")
        data["locationDTO"] = location

        sample = self.sample.to_dict()
        sample.pop("id")
        data["sampleDTO"] = sample

        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = session.post(self.path, data=json.dumps(data, cls=NumpyEncoder), headers=headers)
        if debug:
            print(response.json())
        check_response(response)

        records = response.json()
        self.id = records["id"]
        self.location.id = records["locationDTO"]["id"]
        self.sample.id = records["sampleDTO"]["id"]
        return records   