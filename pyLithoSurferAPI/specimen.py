from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *


class Specimen(APIRequests):

    path = URL_BASE + "/api/specimen"

    def __init__(self,
                specimenKindId: Union[int, np.int16, np.int32, np.int64],
                archiveId: Union[int, np.int16, np.int32, np.int64],
                shrimpdataPointId: Union[int, np.int16, np.int32, np.int64],
                name: str = None,
                description: str = None,
                igsn: str = None,
                pictureHref: url = None):
        """Specimen

        Args:
            name (str): Name of the Specimen
            specimenKindId (int): Specimen Kind Id e.g 0: "other", 1: "mount", 2: "vial": 
            archiveId (int): Id of the Archive to which the specimen belongs to.
            shrimpdataPointId (int): Id of the DataType object.
            description (str, optional): Description of the specimen. Defaults to None.
            igsn (str, optional): IGSN reference of the specimen. Defaults to None.
            pictureHref (url, optional): . Url of an image of the specimen.

        Returns:
            Specimen object
        """

        if not name or np.isnan(name):
            name = "unknown"

        self.name = str(name)
        self.specimenKindId = convert_int(specimenKindId)
        self.archiveId = convert_int(archiveId)
        self.shrimpdataPointId = convert_int(shrimpdataPointId)
        
        self.description = convert_str(description)
        self.igsn = convert_str(igsn)
        self.pictureHref = convert_str(pictureHref)

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
        self._name = convert_str(value)
    
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value: str):
        self._description = convert_str(value)

    @property
    def specimenKindId(self):
        return self._specimenKindId

    @specimenKindId.setter
    def specimenKindId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._specimenKindId = convert_int(value)
    
    @property
    def specimenKindName(self):
        return self._specimenKindName

    @specimenKindName.setter
    def specimenKindName(self, value: str):
        self._specimenKindName = convert_str(value)
    
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
    def shrimpdataPointId(self):
        return self._shrimpdataPointId

    @shrimpdataPointId.setter
    def shrimpdataPointId(self, value: Union[int, np.int16, np.int32, np.int64]):
        self._shrimpdataPointId = convert_int(value)
        