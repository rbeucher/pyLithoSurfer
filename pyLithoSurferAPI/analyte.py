from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np

url = str

# Convert if data is not nan or None
# This is to make sure that we are pushing the right type to the API.
convert_str = lambda x: str(x) if x else None
convert_int = lambda x: int(x) if x else None
convert_float = lambda x: float(x) if x and not isinstance(x, np.nan) else None


class Analyte(APIRequests):

    path = URL_BASE + "/api/analytes"

    def __init__(self,    
                name: str,
                analyteKindId: Union[int, np.int16, np.int32, np.int64],
                sampleId: Union[int, np.int16, np.int32, np.int64] = None,
                specimenId: Union[int, np.int16, np.int32, np.int64] = None,
                archiveId: Union[int, np.int16, np.int32, np.int64] = None,
                description: str = None,
                igsn: str = None,
                pictureHref: url = None,
                ):
        """Analyte

        Args:
            name (str): Analyte name
            analyteKindId (Union[int, np.int16, np.int32, np.int64]): Analyte Kind Id
            sampleId (Union[int, np.int16, np.int32, np.int64], optional): Sample Id
            specimenId (Union[int, np.int16, np.int32, np.int64], optional): Specimen Id
            archiveId (Union[int, np.int16, np.int32, np.int64], optional): Archive Id
            description (str, optional): Description of the Analyte. Defaults to None.
            igsn (str, optional): IGSN Id. Defaults to None.
            pictureHref (url, optional): URL link to image of the analyte. Defaults to None.

        Returns:
            Analyte object.
        """

        self.name = convert_str(name)
        self.analyteKindId = convert_int(analyteKindId)
        self.sampleId = convert_int(sampleId)
        self.specimenId = convert_int(specimenId)
        self.archiveId = convert_int(archiveId)
        self.description = convert_str(description)
        self.igsn = convert_str(igsn)
        self.pictureHref = convert_str(pictureHref)


    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._id = convert_int(value)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = convert_str(value)
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = convert_str(value)

    @property
    def analyteKindId(self):
        return self._analyteKindId

    @analyteKindId.setter
    def analyteKindId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._analyteKindId = convert_int(value)
    
    @property
    def analyteKindName(self):
        return self._analyteKindName

    @analyteKindName.setter
    def analyteKindName(self, value: str):
        self._analyteKindName = convert_str(value)
    
    @property
    def archiveId(self):
        return self._archiveId

    @archiveId.setter
    def archiveId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._archiveId = convert_int(value)
    
    @property
    def archiveName(self):
        return self._archiveName

    @archiveName.setter
    def archiveName(self, value: str):
        self._archiveName = convert_str(value)
    
    @property
    def igsn(self):
        return self._igsn

    @igsn.setter
    def igsn(self, value: str):
        self._igsn = convert_str(value)
    
    @property
    def pictureHref(self):
        return self._pictureHref

    @pictureHref.setter
    def pictureHref(self, value: str):
        self._pictureHref = convert_str(value)
    
    @property
    def sampleId(self):
        return self._sampleId

    @sampleId.setter
    def sampleId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._sampleId = convert_int(value)
    
    @property
    def sampleName(self):
        return self._sampleName

    @sampleName.setter
    def sampleName(self, value: str):
        self._sampleName = convert_str(value)
    
    @property
    def specimenId(self):
        return self._specimenId

    @specimenId.setter
    def specimenId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._specimenId = convert_int(value)
    
    @property
    def specimenName(self):
        return self._specimenName

    @specimenName.setter
    def specimenName(self, value: str):
        self._specimenName = convert_str(value)