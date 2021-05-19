from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *
from .REST import check_response

class Location(APIRequests):

    path = URL_BASE + "/api/locations"

    def __init__(self,
                lat: Union[float, np.float16, np.float32, np.float64],
                lon: Union[float, np.float16, np.float32, np.float64],
                latLonPrecision: Union[float, np.float16, np.float32, np.float64],
                name: str = "unknown",
                captureMethodId: Union[int, np.int16, np.int32, np.int64] = 0,
                captureMethodName: str = None,
                celestialId: Union[int, np.int16, np.int32, np.int64] = 0,
                celestialName: str = None,
                description: str = None):
        """[summary]

        Args:
            lat (float): Latitude
            lon (float): Longitude
            name (str): Location name
            latLonPrecision (float): Precision of the Lat / Lon
            captureMethodId (int, optional): capture Method Id. Defaults to 0 (Unknown), GPS is 6.
            celestialId (int, optional): celestial object. Defaults to 0 (Earth).
            description (str, optional): location description. Defaults to None.

        Returns:
            Location object
        """

        if not name:
            name = "unknown"

        if not isinstance(name, str) and np.isnan(name):
            name = "unknown"

        self.name = str(name)
        self.lat = convert_float(lat)
        self.lon = convert_float(lon)
        self.latLonPrecision = convert_float(latLonPrecision)

        self.captureMethodId = convert_int(captureMethodId)
        self.celestialId = convert_int(celestialId)
        self.description = convert_str(description)

        self.id = 0

    def new(self, *args, **kwargs):
        
        name = self.name.replace(" ", "%20")
        response = self.get_from_query(f"name.in={name}")
        
        if check_response(response):
            new_args = response.json()
            if len(new_args) >= 1:
                new_id = new_args[0].pop("id")
                self.__init__(**new_args[0])
                self.id = new_id
                return response.json()
                
        super().new(*args, **kwargs)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._id = int(value)
    
    @property
    def celestialId(self):
        return self._celestialId

    @celestialId.setter
    def celestialId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._celestialId = int(value)
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = convert_str(value)

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._lat = convert_float(value)

    @property
    def captureMethodId(self):
        return self._captureMethodId

    @captureMethodId.setter
    def captureMethodId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._captureMethodId = convert_int(value)

    @property
    def captureMethodName(self):
        return self._captureMethodName

    @captureMethodName.setter
    def captureMethodName(self, value: str):
        self._captureMethodName = convert_str(value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = convert_str(value)

    @property
    def locPredefinedId(self):
        return self._locPredefinedId

    @locPredefinedId.setter
    def locPredefinedId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._locPredefinedId = convert_int(value)

    @property
    def locPredefinedName(self):
        return self._locPredefinedName

    @locPredefinedName.setter
    def locPredefinedName(self, value: str):
        self._locPredefinedName = convert_str(value)

    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._lon = convert_float(value)

    @property
    def latLonPrecision(self):
        return self._latLonPrecision

    @latLonPrecision.setter
    def latLonPrecision(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._latLonPrecision = convert_float(value)
