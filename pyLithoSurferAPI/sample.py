from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *
from .REST import check_response
from .location import Location
import urllib.parse


class Sample(APIRequests):

    path = URL_BASE + "/api/samples"

    def __init__(self,
                id: Union[int, np.int16, np.int32, np.int64] = None,
                materialId: Union[int, np.int16, np.int32, np.int64] = None,
                locationKindId:  Union[int, np.int16, np.int32, np.int64] = None,
                sampleMethodId:  Union[int, np.int16, np.int32, np.int64] = None,
                sampleKindId:  Union[int, np.int16, np.int32, np.int64] = None,
                locationId:  Union[int, np.int16, np.int32, np.int64] = None,
                name: str = "unknown",
                description: str = None,
                relativeElevationAccuracy: Union[float, np.float16, np.float32, np.float64] = None,
                referenceElevation: Union[float, np.float16, np.float32, np.float64] = 0.,
                archiveId:  Union[int, np.int16, np.int32, np.int64] = None,
                referenceElevationKindId:  Union[int, np.int16, np.int32, np.int64] = None,
                referenceElevationKindNote: str = None,
                referenceElevationSource: str = "SOURCE",
                sourceId: str = None,
                dataPackageId: Union[int, np.int16, np.int32, np.int64] = None,
                stratographicUnitId:  Union[int, np.int16, np.int32, np.int64] = None,
                igsn: str = None,
                archiveName: str = None,
                locationKindName: str = None,
                locationName: str = None,
                referenceElevationKindName: str = None,
                sampleMethodName: str = None,
                sampleKindName: str = None,
                stratographicUnitName: str = None,
                dataPackageName: str = None,
                archiveNote: str = None,
                igsnHandleURL: str = None,
                materialName: str = None,
                collectDateMax: str = None,
                collectDateMin: str = None,
                igsnMintingTimestamp: str = None,
                relativeElevationMin: Union[int, np.int16, np.int32, np.int64] = None,
                relativeElevationMax: Union[int, np.int16, np.int32, np.int64] = None,
                ):
        """Sample

        Args:
            lithologyKindId (int): Lithology Id
            locationId (int): Location Id
            locationKindId (int): Kind of Location
            sampleMethodId (int): Sampling method
            relativeElevation (int): [description]
            name (str), optional: Name of the sample
            description (str, optional): Description of the sample
            archiveId (int): Id of the archive to which the sample belongs to.
            relativeElevationAccuracy (int, optional): [description]. Defaults to None.
            referenceElevation (int, optional): [description]. Defaults to 0 (sea level).
            referenceElevationKindId (int, optional): Reference Elevation Kind.
            referenceElevationKindNote (str, optional): [description]. Defaults to None.
            referenceElevationSource (str): Source of the reference Elevation.
            sourceId (str, optional): [description]. Legacy ID from Sample table.
            stratographicUnitId (int, optional): [description]. Stratigraphic Unit Id.
            igsn (str, optional): [description]. IGSN reference..

        Returns:
            Sample object
        """

        if not name:
            name = "unknown"

        if not isinstance(name, str) and np.isnan(name):
            name = "unknown"

        self.name = convert_str(name)
        self.description = convert_str(description)
        self.materialId = convert_int(materialId)
        self.locationKindId = convert_int(locationKindId)
        self.sampleMethodId = convert_int(sampleMethodId)
        self.sampleKindId = convert_int(sampleKindId)

        self.relativeElevationAccuracy = convert_float(relativeElevationAccuracy)
        self.relativeElevationMin = convert_float(relativeElevationMin)
        self.relativeElevationMax = convert_float(relativeElevationMax)
        self.archiveId = convert_int(archiveId)
        self.locationId = convert_int(locationId)
        self.referenceElevation = convert_float(referenceElevation)
        self.referenceElevationKindId = convert_int(referenceElevationKindId)
        self.referenceElevationKindNote = convert_str(referenceElevationKindNote)
        self.referenceElevationSource = convert_str(referenceElevationSource)
        self.sourceId = convert_int(sourceId)
        self.stratographicUnitId = convert_int(stratographicUnitId)
        self.dataPackageId = convert_int(dataPackageId)
        self.igsn = convert_str(igsn)
        self.archiveNote = convert_str(archiveNote)
        self.igsnHandleURL = convert_str(igsnHandleURL)
        
        self.collectDateMax = convert_str(collectDateMax)
        self.collectDateMin = convert_str(collectDateMin)
        self.igsnMintingTimestamp = convert_str(igsnMintingTimestamp)

        self.id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64, None]):
        self._id = convert_int(value)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = convert_str(value)
    
    @property
    def archiveId(self):
        return self._archiveId

    @archiveId.setter
    def archiveId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._archiveId = convert_int(value)
    
    @property
    def sourceId(self):
        return self._sourceId

    @sourceId.setter
    def sourceId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._sourceId = convert_int(value)
    
    @property
    def archiveName(self):
        return self._archiveName

    @archiveName.setter
    def archiveName(self, value: str):
        self._archiveName = convert_str(value)
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = convert_str(value)

    @property
    def igsn(self):
        return self._igsn

    @igsn.setter
    def igsn(self, value: str):
        self._igsn = convert_str(value)
    
    @property
    def relativeElevationMin(self):
        return self._relativeElevationMin

    @relativeElevationMin.setter
    def relativeElevationMin(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._relativeElevationMin = convert_float(value)
    
    @property
    def relativeElevationMax(self):
        return self._relativeElevationMax

    @relativeElevationMax.setter
    def relativeElevationMax(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._relativeElevationMax = convert_float(value)

    @property
    def relativeElevationAccuracy(self):
        return self._relativeElevationAccuracy

    @relativeElevationAccuracy.setter
    def relativeElevationAccuracy(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._relativeElevationAccuracy = convert_float(value)
    
    @property
    def referenceElevationKindId(self):
        return self._referenceElevationKindId

    @referenceElevationKindId.setter
    def referenceElevationKindId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._referenceElevationKindId = convert_int(value)
    
    @property
    def referenceElevationKindNote(self):
        return self._referenceElevationKindNote

    @referenceElevationKindNote.setter
    def referenceElevationKindNote(self, value: str):
        self._referenceElevationKindNote = convert_str(value)
    
    @property
    def referenceElevation(self):
        return self._referenceElevation

    @referenceElevation.setter
    def referenceElevation(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._referenceElevation = convert_float(value)
    
    @property
    def referenceElevationSource(self):
        return self._referenceElevationSource

    @referenceElevationSource.setter
    def referenceElevationSource(self, value: str):
        self._referenceElevationSource = convert_str(value)
    
    @property
    def stratographicUnitId(self):
        return self._stratographicUnitId

    @stratographicUnitId.setter
    def stratographicUnitId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._stratographicUnitId = convert_int(value)
    
    @property
    def stratographicUnitName(self):
        return self._stratographicUnitName

    @stratographicUnitName.setter
    def stratographicUnitName(self, value: str):
        self._stratographicUnitName = convert_str(value)
    
    @property
    def locationId(self):
        return self._locationId

    @locationId.setter
    def locationId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._locationId = convert_int(value)
    
    @property
    def locationKindId(self):
        return self._locationKindId

    @locationKindId.setter
    def locationKindId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._locationKindId = convert_int(value)
    
    @property
    def locationKindName(self):
        return self._locationKindName

    @locationKindName.setter
    def locationKindName(self, value: str):
        self._locationKindName = convert_str(value)
    
    @property
    def LocationName(self):
        return self._LocationName

    @LocationName.setter
    def LocationName(self, value: str):
        self._LocationName = convert_str(value)

    @property
    def sampleMethodId(self):
        return self._sampleMethodId

    @sampleMethodId.setter
    def sampleMethodId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._sampleMethodId = convert_int(value)
    
    @property
    def sampleMethodName(self):
        return self._sampleMethodName

    @sampleMethodName.setter
    def sampleMethodName(self, value: str):
        self._sampleMethodName = convert_str(value)
    
    @property
    def sampleKindId(self):
        return self._sampleKindId

    @sampleKindId.setter
    def sampleKindId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._sampleKindId = convert_int(value)
    
    @property
    def sampleKindName(self):
        return self._sampleKindName

    @sampleKindName.setter
    def sampleKindName(self, value: str):
        self._sampleKindName = convert_str(value)
    
    @property
    def dataPackageName(self):
        return self._dataPackageName

    @dataPackageName.setter
    def dataPackageName(self, value: str):
        self._dataPackageName = convert_str(value)
    
    @property
    def dataPackageId(self):
        return self._dataPackageId

    @dataPackageId.setter
    def dataPackageId(self, value: Union[int, np.int16, np.int32, np.int64, None]):
        self._dataPackageId = convert_int(value)

    @property
    def archiveNote(self):
        return self._archiveNote

    @archiveNote.setter
    def archiveNote(self, value: str):
        self._archiveNote = convert_str(value)
    
    @property
    def igsnHandleURL(self):
        return self._igsnHandleURL

    @igsnHandleURL.setter
    def igsnHandleURL(self, value: str):
        self._igsnHandleURL = convert_str(value)
    
    @property
    def igsnMintingTimestamp(self):
        return self._igsnMintingTimestamp

    @igsnMintingTimestamp.setter
    def igsnMintingTimestamp(self, value: str):
        self._igsnMintingTimestamp = convert_str(value)
    
    @property
    def materialId(self):
        return self._materialId

    @materialId.setter
    def materialId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._materialId = convert_int(value)
    
    @property
    def materialName(self):
        return self._materialName

    @materialName.setter
    def materialName(self, value: str):
        self._materialName = convert_str(value)

    @property
    def collectDateMax(self):
        return self._collectDateMax

    @collectDateMax.setter
    def collectDateMax(self, value: str):
        self._collectDateMax = convert_str(value)

    @property
    def collectDateMin(self):
        return self._collectDateMin

    @collectDateMin.setter
    def collectDateMin(self, value: str):
        self._collectDateMin = convert_str(value)
    

class SampleWithLocation(APIRequests):

    path = URL_BASE+'/api/core/sample-with-locations'

    def __init__(self, location: Location, sample: Sample, id: Union[int, np.int16, np.int32, np.int64] = None):

        self.location = location
        self.sample = sample

        self.id = id 

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64, None]):
        self._id = convert_int(value)

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

        response = session.post(self.path, data=json.dumps(data), headers=headers)
        if debug:
            print(response.json())
        check_response(response)

        records = response.json()
        self.id = records["id"]
        self.location.id = records["locationDTO"]["id"]
        self.sample.id = records["sampleDTO"]["id"]
        return records   