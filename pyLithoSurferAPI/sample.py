from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *
from .REST import check_response



class Sample(APIRequests):

    path = URL_BASE + "/api/samples"

    def __init__(self,
                lithologyKindId:  Union[int, np.int16, np.int32, np.int64],
                locationId:  Union[int, np.int16, np.int32, np.int64],
                locationKindId:  Union[int, np.int16, np.int32, np.int64],
                sampleMethodId:  Union[int, np.int16, np.int32, np.int64],
                relativeElevation: Union[float, np.float16, np.float32, np.float64],
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
                tectonicUnitId:  Union[int, np.int16, np.int32, np.int64] = None,
                igsn: str = None,
                archiveName: str = None,
                lithologyKindName: str = None,
                locationKindName: str = None,
                locationName: str = None,
                referenceElevationKindName: str = None,
                sampleMethodName: str = None,
                tectonicUnitName: str = None,
                dataPackageName: str = None,
                archiveNote: str = None,
                igsnHandleURL: str = None,
                pickingDate: str = None,
                pickingDateRange: str = None,
                materialId: Union[int, np.int16, np.int32, np.int64] = None,
                materialName: str = None
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
            tectonicUnitId (int, optional): [description]. Tectonic Unit Id.
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
        self.lithologyKindId = convert_int(lithologyKindId)
        self.locationKindId = convert_int(locationKindId)
        self.sampleMethodId = convert_int(sampleMethodId)
        self.relativeElevation = convert_float(relativeElevation)

        self.relativeElevationAccuracy = convert_float(relativeElevationAccuracy)
        self.relativeElevation = convert_float(relativeElevation)
        self.archiveId = convert_int(archiveId)
        self.locationId = convert_int(locationId)
        self.referenceElevation = convert_float(referenceElevation)
        self.referenceElevationKindId = convert_int(referenceElevationKindId)
        self.referenceElevationKindNote = convert_str(referenceElevationKindNote)
        self.referenceElevationSource = convert_str(referenceElevationSource)
        self.sourceId = convert_int(sourceId)
        self.tectonicUnitId = convert_int(tectonicUnitId)
        self.dataPackageId = convert_int(dataPackageId)
        self.igsn = convert_str(igsn)
        self.archiveNote = convert_str(archiveNote)
        self.igsnHandleURL = convert_str(igsnHandleURL)

        self.id = None

    def new(self, *args, **kwargs):
        
        name = self.name.replace(" ", "%20")
        response = self.get_from_query(f"name.in={name}")
        
        if check_response(response):
            old_args = response.json()
            if len(old_args) >= 1:
                data = self.to_dict()
                if "id" in data.keys():
                    data.pop("id")
                for key, val in old_args[0].items():
                    if key in data.keys():
                        old_args[0][key] = data[key]

                new_id = old_args[0].pop("id")
                self.__init__(**old_args[0])
                self.id = new_id
                test = self.update()
                return response.json()
        
        super().new(*args, **kwargs)

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
    def tectonicUnitId(self):
        return self._tectonicUnitId

    @tectonicUnitId.setter
    def tectonicUnitId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._tectonicUnitId = convert_int(value)
    
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
    def relativeElevation(self):
        return self._relativeElevation

    @relativeElevation.setter
    def relativeElevation(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._relativeElevation = convert_float(value)

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
    def lithologyKindId(self):
        return self._lithologyKindId

    @lithologyKindId.setter
    def lithologyKindId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._lithologyKindId = convert_int(value)
    
    @property
    def lithologyKindName(self):
        return self._lithologyKindName

    @lithologyKindName.setter
    def lithologyKindName(self, value: str):
        self._lithologyKindName = convert_str(value)
    
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
    def pickingDate(self):
        return self._pickingDate

    @pickingDate.setter
    def pickingDate(self, value: str):
        self._pickingDate = convert_str(value)
    
    @property
    def pickingDateRange(self):
        return self._pickingDateRange

    @pickingDateRange.setter
    def pickingDateRange(self, value: str):
        self._pickingDateRange = convert_str(value)

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