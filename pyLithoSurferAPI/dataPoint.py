from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *


class DataPoint(APIRequests):

    path = URL_BASE + "/api/core/data-points"

    mandatory_args = ["dataStructure"]

    def __init__(self, 
                dataPackageId: Union[int, np.int16, np.int32, np.int64],
                dataStructure: str,
                name: str = None,
                dataEntityId: Union[int, np.int16, np.int32, np.int64] = None,
                sourceId: Union[int, np.int16, np.int32, np.int64] = None,
                locationId: Union[int, np.int16, np.int32, np.int64] = None,
                locationName: str = None,
                sampleId: Union[int, np.int16, np.int32, np.int64] = None,
                sampleName: str = None,
                dataPackageName: str = None,
                externalDataHref: url = None,
                description: str = None):
        """DataPoint

        Args:
            dataPackageId (int): Id of the package to which the datapoint belongs to.
            dataStructure (str): Type of data structure e.g. 'UPB_SHRIMP'
            dataEntityId (int): Id of the Entity (e.g. Shrimp Datapoint) in the table specified by data structure.
            name (str, optional): Name of the Datapoint. Defaults to None.
            sourceId (int, optional): Legacy Chrono ID. Defaults to None.
            locationId (int, optional): Id of the datapoint location. Defaults to None.
            locationName (str, optional): Name of the location.
            sampleId (int, optional): Id of the datapoint sample. Defaults to None.
            sampleName (str, optional): Name of the sample.
            externalDataHref (url, optional): [description]. Defaults to None.
            description (str, optional): [description]. Defaults to None.

        Returns:
            DataPoint object.
        """
        
        if not name:
            name = "unknown"

        if not isinstance(name, str) and np.isnan(name):
            name = "unknown"
        
        self.name = convert_str(name)
        self.dataPackageId = convert_int(dataPackageId)
        self.dataStructure = str(dataStructure)
        self.dataEntityId = convert_int(dataEntityId)

        self.sourceId = convert_int(sourceId)
        self.locationId = convert_int(locationId)
        self.locationName = convert_str(locationName)
        self.sampleId = convert_int(sampleId)
        self.sampleName = convert_str(sampleName)
        self.dataPackageName = convert_str(sampleName)
        self.externalDataHref = convert_str(externalDataHref)
        self.description = convert_str(description)

        self.id = None

    @property
    def dataEntityId(self):
        return self._dataEntityId

    @dataEntityId.setter
    def dataEntityId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._dataEntityId = convert_int(value)

    @property
    def dataPackageId(self):
        return self._dataPackageId

    @dataPackageId.setter
    def dataPackageId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._dataPackageId = convert_int(value)

    @property
    def dataPackageName(self):
        return self._dataPackageName

    @dataPackageName.setter
    def dataPackageName(self, value: str):
        self._dataPackageName = value

    @property
    def dataStructure(self):
        return self._dataStructure

    @dataStructure.setter
    def dataStructure(self, value: str):
        self._dataStructure = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def sampleId(self):
        return self._sampleId

    @sampleId.setter
    def sampleId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._sampleId = value
    
    @property
    def sampleName(self):
        return self._sampleName

    @sampleName.setter
    def sampleName(self, value: str):
        self._sampleName = value
    
    @property
    def sourceId(self):
        return self._sourceId

    @sourceId.setter
    def sourceId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._sourceId = value
    
    @property
    def locationId(self):
        return self._locationId

    @locationId.setter
    def locationId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._locationId = value
    
    @property
    def locationName(self):
        return self._locationName

    @locationName.setter
    def locationName(self, value: str):
        self._locationName = value
    
    @property
    def externalDataHref(self):
        return self._externalDataHref

    @externalDataHref.setter
    def externalDataHref(self, value: url):
        self._externalDataHref = value
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = value