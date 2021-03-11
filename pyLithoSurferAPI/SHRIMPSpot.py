from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import pandas as pd
import numpy as np
from .utilities import *


class SHRIMPSpot(APIRequests):
        
    path = URL_BASE+'/api/shrimp-spots'

    def __init__(self,
                 ageCalcName: str = None,
                 ageId: Union[int, np.int16, np.int32, np.int64] = 0,
                 analysisData: str = None,
                 analysisHours: Union[float, np.float16, np.float32, np.float64] = 0,
                 comment: str = None,
                 common206Pbf204Pct204Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 common206Pbf207Pct207Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 common206Pbf208Pct208Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 discordancePct204Corrected: Union[float, np.float16, np.float32, np.float64] = 0,
                 discordancePct208Corrected: Union[float, np.float16, np.float32, np.float64] = 0,
                 grainIdentifier: str = None,
                 i204CorrErrorCorrelation: Union[float, np.float16, np.float32, np.float64] = 0,
                 i204Pb206Pb: Union[float, np.float16, np.float32, np.float64] = 0,
                 i204Pb206PbError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i204Pb206PbErrorTypeId: Union[float, np.float16, np.float32, np.float64] = 0,
                 i204Pb206PbErrorTypeName: str = None,
                 i206Pb238207CorrAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238207CorrAgeErrorTypeId:  = ,
                 i206Pb238207CorrAgeErrorTypeName: str = None,
                 i206Pb238U204Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U204CorrAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U204CorrAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U204CorrAgeErrorTypeId: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U204CorrAgeErrorTypeName: str = None,
                 i206Pb238U204CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U204CorrErrorTypeId:  = ,
                 i206Pb238U204CorrErrorTypeName: str = None,
                 i206Pb238U207Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U207CorrAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U207CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U207CorrErrorTypeId:  = ,
                 i206Pb238U207CorrErrorTypeName: str = None,
                 i206Pb238U208Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U208CorrAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U208CorrAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U208CorrAgeErrorTypeId:  = ,
                 i206Pb238U208CorrAgeErrorTypeName: str = None,
                 i206Pb238U208CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238U208CorrErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i206Pb238U208CorrErrorTypeName: str = None,
                 i206Pb238UTotal: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238UTotalAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238UTotalAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238UTotalAgeErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i206Pb238UTotalAgeErrorTypeName: str = None,
                 i206Pb238UTotalError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i206Pb238UTotalErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i206Pb238UTotalErrorTypeName: str = None,
                 i207Pb206Pb204Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206Pb204CorrAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206Pb204CorrAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206Pb204CorrAgeErrorTypeId:  = ,
                 i207Pb206Pb204CorrAgeErrorTypeName: str = None,
                 i207Pb206Pb204CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206Pb204CorrErrorTypeId:  = ,
                 i207Pb206Pb204CorrErrorTypeName: str = None,
                 i207Pb206Pb208Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206Pb208CorrAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206Pb208CorrAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206Pb208CorrAgeErrorTypeId:  = ,
                 i207Pb206Pb208CorrAgeErrorTypeName: str = None,
                 i207Pb206Pb208CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206Pb208CorrErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i207Pb206Pb208CorrErrorTypeName: str = None,
                 i207Pb206PbTotal: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206PbTotalAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206PbTotalAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206PbTotalAgeErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i207Pb206PbTotalAgeErrorTypeName: str = None,
                 i207Pb206PbTotalError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb206PbTotalErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i207Pb206PbTotalErrorTypeName: str = None,
                 i207Pb235U204Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb235U204CorrAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb235U204CorrAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb235U204CorrAgeErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i207Pb235U204CorrAgeErrorTypeName: str = None,
                 i207Pb235U204CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb235U204CorrErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i207Pb235U204CorrErrorTypeName: str = None,
                 i207Pb235U208Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb235U208CorrAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb235U208CorrAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb235U208CorrAgeErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i207Pb235U208CorrAgeErrorTypeName: str = None,
                 i207Pb235U208CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb235U208CorrErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i207Pb235U208CorrErrorTypeName: str = None,
                 i207Pb235UTotalAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb235UTotalAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i207Pb235UTotalAgeErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i207Pb235UTotalAgeErrorTypeName: str = None,
                 i208CorrErrorCorrelation: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb206Pb204Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb206Pb204CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb206Pb204CorrErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i208Pb206Pb204CorrErrorTypeName: str = None,
                 i208Pb206PbTotal: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb206PbTotalError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb206PbTotalErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i208Pb206PbTotalErrorTypeName: str = None,
                 i208Pb232Th204Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb232Th204CorrAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb232Th204CorrAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb232Th204CorrAgeErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i208Pb232Th204CorrAgeErrorTypeName: str = None,
                 i208Pb232Th204CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb232Th204CorrErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i208Pb232Th204CorrErrorTypeName: str = None,
                 i208Pb232ThTotal: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb232ThTotalAge: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb232ThTotalAgeError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb232ThTotalAgeErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i208Pb232ThTotalAgeErrorTypeName: str = None,
                 i208Pb232ThTotalError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i208Pb232ThTotalErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i208Pb232ThTotalErrorTypeName: str = None,
                 i232Th: Union[float, np.float16, np.float32, np.float64] = 0,
                 i232Th238U: Union[float, np.float16, np.float32, np.float64] = 0,
                 i238U: Union[float, np.float16, np.float32, np.float64] = 0,
                 i238U206Pb204Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i238U206Pb204CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i238U206Pb204CorrErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i238U206Pb204CorrErrorTypeName: str = None,
                 i238U206Pb208Corr: Union[float, np.float16, np.float32, np.float64] = 0,
                 i238U206Pb208CorrError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i238U206Pb208CorrErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i238U206Pb208CorrErrorTypeName: str = None,
                 i238U206PbTotal: Union[float, np.float16, np.float32, np.float64] = 0,
                 i238U206PbTotalError: Union[float, np.float16, np.float32, np.float64] = 0,
                 i238U206PbTotalErrorTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 i238U206PbTotalErrorTypeName: str = None,
                 id: Union[int, np.int16, np.int32, np.int64] = 0,
                 refMaterialId: Union[float, np.float16, np.float32, np.float64] = 0,
                 refMaterialName: str = None,
                 shrimpdataPointId: Union[int, np.int16, np.int32, np.int64] = 0,
                 spotIdentifier: str = None,
                 totalDiscordancePercent: Union[float, np.float16, np.float32, np.float64] = 0,
                ):
        
        self.ageCalcName = ageCalcName
        self.ageId = ageId
        self.analysisData = analysisData
        self.analysisHours = analysisHours
        self.comment = comment
        self.common206Pbf204Pct204Corr = common206Pbf204Pct204Corr
        self.common206Pbf207Pct207Corr = common206Pbf207Pct207Corr
        self.common206Pbf208Pct208Corr = common206Pbf208Pct208Corr
        self.discordancePct204Corrected = discordancePct204Corrected
        self.discordancePct208Corrected = discordancePct208Corrected
        self.grainIdentifier = grainIdentifier
        self.i204CorrErrorCorrelation = i204CorrErrorCorrelation
        self.i204Pb206Pb = i204Pb206Pb
        self.i204Pb206PbError = i204Pb206PbError
        self.i204Pb206PbErrorTypeId = i204Pb206PbErrorTypeId
        self.i204Pb206PbErrorTypeName = i204Pb206PbErrorTypeName
        self.i206Pb238207CorrAgeError = i206Pb238207CorrAgeError
        self.i206Pb238207CorrAgeErrorTypeId = i206Pb238207CorrAgeErrorTypeId
        self.i206Pb238207CorrAgeErrorTypeName = i206Pb238207CorrAgeErrorTypeName
        self.i206Pb238U204Corr = i206Pb238U204Corr
        self.i206Pb238U204CorrAge = i206Pb238U204CorrAge
        self.i206Pb238U204CorrAgeError = i206Pb238U204CorrAgeError
        self.i206Pb238U204CorrAgeErrorTypeId = i206Pb238U204CorrAgeErrorTypeId
        self.i206Pb238U204CorrAgeErrorTypeName = i206Pb238U204CorrAgeErrorTypeName
        self.i206Pb238U204CorrError = i206Pb238U204CorrError
        self.i206Pb238U204CorrErrorTypeId = i206Pb238U204CorrErrorTypeId
        self.i206Pb238U204CorrErrorTypeName = i206Pb238U204CorrErrorTypeName
        self.i206Pb238U207Corr = i206Pb238U207Corr
        self.i206Pb238U207CorrAge = i206Pb238U207CorrAge
        self.i206Pb238U207CorrError = i206Pb238U207CorrError
        self.i206Pb238U207CorrErrorTypeId = i206Pb238U207CorrErrorTypeId
        self.i206Pb238U207CorrErrorTypeName = i206Pb238U207CorrErrorTypeName
        self.i206Pb238U208Corr = i206Pb238U208Corr
        self.i206Pb238U208CorrAge = i206Pb238U208CorrAge
        self.i206Pb238U208CorrAgeError = i206Pb238U208CorrAgeError
        self.i206Pb238U208CorrAgeErrorTypeId = i206Pb238U208CorrAgeErrorTypeId
        self.i206Pb238U208CorrAgeErrorTypeName = i206Pb238U208CorrAgeErrorTypeName
        self.i206Pb238U208CorrError = i206Pb238U208CorrError
        self.i206Pb238U208CorrErrorTypeId = i206Pb238U208CorrErrorTypeId
        self.i206Pb238U208CorrErrorTypeName = i206Pb238U208CorrErrorTypeName
        self.i206Pb238UTotal = i206Pb238UTotal
        self.i206Pb238UTotalAge = i206Pb238UTotalAge
        self.i206Pb238UTotalAgeError = i206Pb238UTotalAgeError
        self.i206Pb238UTotalAgeErrorTypeId = i206Pb238UTotalAgeErrorTypeId
        self.i206Pb238UTotalAgeErrorTypeName = i206Pb238UTotalAgeErrorTypeName
        self.i206Pb238UTotalError = i206Pb238UTotalError
        self.i206Pb238UTotalErrorTypeId = i206Pb238UTotalErrorTypeId
        self.i206Pb238UTotalErrorTypeName = i206Pb238UTotalErrorTypeName
        self.i207Pb206Pb204Corr = i207Pb206Pb204Corr
        self.i207Pb206Pb204CorrAge = i207Pb206Pb204CorrAge
        self.i207Pb206Pb204CorrAgeError = i207Pb206Pb204CorrAgeError
        self.i207Pb206Pb204CorrAgeErrorTypeId = i207Pb206Pb204CorrAgeErrorTypeId
        self.i207Pb206Pb204CorrAgeErrorTypeName = i207Pb206Pb204CorrAgeErrorTypeName
        self.i207Pb206Pb204CorrError = i207Pb206Pb204CorrError
        self.i207Pb206Pb204CorrErrorTypeId = i207Pb206Pb204CorrErrorTypeId
        self.i207Pb206Pb204CorrErrorTypeName = i207Pb206Pb204CorrErrorTypeName
        self.i207Pb206Pb208Corr = i207Pb206Pb208Corr
        self.i207Pb206Pb208CorrAge = i207Pb206Pb208CorrAge
        self.i207Pb206Pb208CorrAgeError = i207Pb206Pb208CorrAgeError
        self.i207Pb206Pb208CorrAgeErrorTypeId = i207Pb206Pb208CorrAgeErrorTypeId
        self.i207Pb206Pb208CorrAgeErrorTypeName = i207Pb206Pb208CorrAgeErrorTypeName
        self.i207Pb206Pb208CorrError = i207Pb206Pb208CorrError
        self.i207Pb206Pb208CorrErrorTypeId = i207Pb206Pb208CorrErrorTypeId
        self.i207Pb206Pb208CorrErrorTypeName = i207Pb206Pb208CorrErrorTypeName
        self.i207Pb206PbTotal = i207Pb206PbTotal
        self.i207Pb206PbTotalAge = i207Pb206PbTotalAge
        self.i207Pb206PbTotalAgeError = i207Pb206PbTotalAgeError
        self.i207Pb206PbTotalAgeErrorTypeId = i207Pb206PbTotalAgeErrorTypeId
        self.i207Pb206PbTotalAgeErrorTypeName = i207Pb206PbTotalAgeErrorTypeName
        self.i207Pb206PbTotalError = i207Pb206PbTotalError
        self.i207Pb206PbTotalErrorTypeId = i207Pb206PbTotalErrorTypeId
        self.i207Pb206PbTotalErrorTypeName = i207Pb206PbTotalErrorTypeName
        self.i207Pb235U204Corr = i207Pb235U204Corr
        self.i207Pb235U204CorrAge = i207Pb235U204CorrAge
        self.i207Pb235U204CorrAgeError = i207Pb235U204CorrAgeError
        self.i207Pb235U204CorrAgeErrorTypeId = i207Pb235U204CorrAgeErrorTypeId
        self.i207Pb235U204CorrAgeErrorTypeName = i207Pb235U204CorrAgeErrorTypeName
        self.i207Pb235U204CorrError = i207Pb235U204CorrError
        self.i207Pb235U204CorrErrorTypeId = i207Pb235U204CorrErrorTypeId
        self.i207Pb235U204CorrErrorTypeName = i207Pb235U204CorrErrorTypeName
        self.i207Pb235U208Corr = i207Pb235U208Corr
        self.i207Pb235U208CorrAge = i207Pb235U208CorrAge
        self.i207Pb235U208CorrAgeError = i207Pb235U208CorrAgeError
        self.i207Pb235U208CorrAgeErrorTypeId = i207Pb235U208CorrAgeErrorTypeId
        self.i207Pb235U208CorrAgeErrorTypeName = i207Pb235U208CorrAgeErrorTypeName
        self.i207Pb235U208CorrError = i207Pb235U208CorrError
        self.i207Pb235U208CorrErrorTypeId = i207Pb235U208CorrErrorTypeId
        self.i207Pb235U208CorrErrorTypeName = i207Pb235U208CorrErrorTypeName
        self.i207Pb235UTotalAge = i207Pb235UTotalAge
        self.i207Pb235UTotalAgeError = i207Pb235UTotalAgeError
        self.i207Pb235UTotalAgeErrorTypeId = i207Pb235UTotalAgeErrorTypeId
        self.i207Pb235UTotalAgeErrorTypeName = i207Pb235UTotalAgeErrorTypeName
        self.i208CorrErrorCorrelation = i208CorrErrorCorrelation
        self.i208Pb206Pb204Corr = i208Pb206Pb204Corr
        self.i208Pb206Pb204CorrError = i208Pb206Pb204CorrError
        self.i208Pb206Pb204CorrErrorTypeId = i208Pb206Pb204CorrErrorTypeId
        self.i208Pb206Pb204CorrErrorTypeName = i208Pb206Pb204CorrErrorTypeName
        self.i208Pb206PbTotal = i208Pb206PbTotal
        self.i208Pb206PbTotalError = i208Pb206PbTotalError
        self.i208Pb206PbTotalErrorTypeId = i208Pb206PbTotalErrorTypeId
        self.i208Pb206PbTotalErrorTypeName = i208Pb206PbTotalErrorTypeName
        self.i208Pb232Th204Corr = i208Pb232Th204Corr
        self.i208Pb232Th204CorrAge = i208Pb232Th204CorrAge
        self.i208Pb232Th204CorrAgeError = i208Pb232Th204CorrAgeError
        self.i208Pb232Th204CorrAgeErrorTypeId = i208Pb232Th204CorrAgeErrorTypeId
        self.i208Pb232Th204CorrAgeErrorTypeName = i208Pb232Th204CorrAgeErrorTypeName
        self.i208Pb232Th204CorrError = i208Pb232Th204CorrError
        self.i208Pb232Th204CorrErrorTypeId = i208Pb232Th204CorrErrorTypeId
        self.i208Pb232Th204CorrErrorTypeName = i208Pb232Th204CorrErrorTypeName
        self.i208Pb232ThTotal = i208Pb232ThTotal
        self.i208Pb232ThTotalAge = i208Pb232ThTotalAge
        self.i208Pb232ThTotalAgeError = i208Pb232ThTotalAgeError
        self.i208Pb232ThTotalAgeErrorTypeId = i208Pb232ThTotalAgeErrorTypeId
        self.i208Pb232ThTotalAgeErrorTypeName = i208Pb232ThTotalAgeErrorTypeName
        self.i208Pb232ThTotalError = i208Pb232ThTotalError
        self.i208Pb232ThTotalErrorTypeId = i208Pb232ThTotalErrorTypeId
        self.i208Pb232ThTotalErrorTypeName = i208Pb232ThTotalErrorTypeName
        self.i232Th = i232Th
        self.i232Th238U = i232Th238U
        self.i238U = i238U
        self.i238U206Pb204Corr = i238U206Pb204Corr
        self.i238U206Pb204CorrError = i238U206Pb204CorrError
        self.i238U206Pb204CorrErrorTypeId = i238U206Pb204CorrErrorTypeId
        self.i238U206Pb204CorrErrorTypeName = i238U206Pb204CorrErrorTypeName
        self.i238U206Pb208Corr = i238U206Pb208Corr
        self.i238U206Pb208CorrError = i238U206Pb208CorrError
        self.i238U206Pb208CorrErrorTypeId = i238U206Pb208CorrErrorTypeId
        self.i238U206Pb208CorrErrorTypeName = i238U206Pb208CorrErrorTypeName
        self.i238U206PbTotal = i238U206PbTotal
        self.i238U206PbTotalError = i238U206PbTotalError
        self.i238U206PbTotalErrorTypeId = i238U206PbTotalErrorTypeId
        self.i238U206PbTotalErrorTypeName = i238U206PbTotalErrorTypeName
        self.id = id
        self.refMaterialId = refMaterialId
        self.refMaterialName = refMaterialName
        self.shrimpdataPointId = shrimpdataPointId
        self.spotIdentifier = spotIdentifier
        self.totalDiscordancePercent = totalDiscordancePercent

    
    @property
    def ageCalcName(self):
        return self._ageCalcName

    @ageCalcName.setter
    def ageCalcName(self, value: str):
        self._ageCalcName = convert_str(value)
    
    @property
    def ageId(self):
        return self._ageId

    @ageId.setter
    def ageId(self, value: int):
        self._ageId = int(value)
    
    @property
    def analysisData(self):
        return self._analysisData

    @analysisData.setter
    def analysisData(self, value: str):
        self._analysisData = convert_str(value)
    
    @property
    def analysisHours(self):
        return self._analysisHours

    @analysisHours.setter
    def analysisHours(self, value: float):
        self._analysisHours = convert_float(value)
    
    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value: str):
        self._comment = convert_str(value)
    
    @property
    def common206Pbf204Pct204Corr(self):
        return self._common206Pbf204Pct204Corr

    @common206Pbf204Pct204Corr.setter
    def common206Pbf204Pct204Corr(self, value: float):
        self._common206Pbf204Pct204Corr = convert_float(value)
    
    @property
    def common206Pbf207Pct207Corr(self):
        return self._common206Pbf207Pct207Corr

    @common206Pbf207Pct207Corr.setter
    def common206Pbf207Pct207Corr(self, value: float):
        self._common206Pbf207Pct207Corr = convert_float(value)
    
    @property
    def common206Pbf208Pct208Corr(self):
        return self._common206Pbf208Pct208Corr

    @common206Pbf208Pct208Corr.setter
    def common206Pbf208Pct208Corr(self, value: float):
        self._common206Pbf208Pct208Corr = convert_float(value)
    
    @property
    def discordancePct204Corrected(self):
        return self._discordancePct204Corrected

    @discordancePct204Corrected.setter
    def discordancePct204Corrected(self, value: float):
        self._discordancePct204Corrected = convert_float(value)
    
    @property
    def discordancePct208Corrected(self):
        return self._discordancePct208Corrected

    @discordancePct208Corrected.setter
    def discordancePct208Corrected(self, value: float):
        self._discordancePct208Corrected = convert_float(value)
    
    @property
    def grainIdentifier(self):
        return self._grainIdentifier

    @grainIdentifier.setter
    def grainIdentifier(self, value: str):
        self._grainIdentifier = convert_str(value)
    
    @property
    def i204CorrErrorCorrelation(self):
        return self._i204CorrErrorCorrelation

    @i204CorrErrorCorrelation.setter
    def i204CorrErrorCorrelation(self, value: float):
        self._i204CorrErrorCorrelation = convert_float(value)
    
    @property
    def i204Pb206Pb(self):
        return self._i204Pb206Pb

    @i204Pb206Pb.setter
    def i204Pb206Pb(self, value: float):
        self._i204Pb206Pb = convert_float(value)
    
    @property
    def i204Pb206PbError(self):
        return self._i204Pb206PbError

    @i204Pb206PbError.setter
    def i204Pb206PbError(self, value: float):
        self._i204Pb206PbError = convert_float(value)
    
    @property
    def i204Pb206PbErrorTypeId(self):
        return self._i204Pb206PbErrorTypeId

    @i204Pb206PbErrorTypeId.setter
    def i204Pb206PbErrorTypeId(self, value: float):
        self._i204Pb206PbErrorTypeId = convert_float(value)
    
    @property
    def i204Pb206PbErrorTypeName(self):
        return self._i204Pb206PbErrorTypeName

    @i204Pb206PbErrorTypeName.setter
    def i204Pb206PbErrorTypeName(self, value: str):
        self._i204Pb206PbErrorTypeName = convert_str(value)
    
    @property
    def i206Pb238207CorrAgeError(self):
        return self._i206Pb238207CorrAgeError

    @i206Pb238207CorrAgeError.setter
    def i206Pb238207CorrAgeError(self, value: float):
        self._i206Pb238207CorrAgeError = convert_float(value)
    
    @property
    def i206Pb238207CorrAgeErrorTypeId(self):
        return self._i206Pb238207CorrAgeErrorTypeId

    @i206Pb238207CorrAgeErrorTypeId.setter
    def i206Pb238207CorrAgeErrorTypeId(self, value: ):
        self._i206Pb238207CorrAgeErrorTypeId = convert_(value)
    
    @property
    def i206Pb238207CorrAgeErrorTypeName(self):
        return self._i206Pb238207CorrAgeErrorTypeName

    @i206Pb238207CorrAgeErrorTypeName.setter
    def i206Pb238207CorrAgeErrorTypeName(self, value: str):
        self._i206Pb238207CorrAgeErrorTypeName = convert_str(value)
    
    @property
    def i206Pb238U204Corr(self):
        return self._i206Pb238U204Corr

    @i206Pb238U204Corr.setter
    def i206Pb238U204Corr(self, value: float):
        self._i206Pb238U204Corr = convert_float(value)
    
    @property
    def i206Pb238U204CorrAge(self):
        return self._i206Pb238U204CorrAge

    @i206Pb238U204CorrAge.setter
    def i206Pb238U204CorrAge(self, value: float):
        self._i206Pb238U204CorrAge = convert_float(value)
    
    @property
    def i206Pb238U204CorrAgeError(self):
        return self._i206Pb238U204CorrAgeError

    @i206Pb238U204CorrAgeError.setter
    def i206Pb238U204CorrAgeError(self, value: float):
        self._i206Pb238U204CorrAgeError = convert_float(value)
    
    @property
    def i206Pb238U204CorrAgeErrorTypeId(self):
        return self._i206Pb238U204CorrAgeErrorTypeId

    @i206Pb238U204CorrAgeErrorTypeId.setter
    def i206Pb238U204CorrAgeErrorTypeId(self, value: float):
        self._i206Pb238U204CorrAgeErrorTypeId = convert_float(value)
    
    @property
    def i206Pb238U204CorrAgeErrorTypeName(self):
        return self._i206Pb238U204CorrAgeErrorTypeName

    @i206Pb238U204CorrAgeErrorTypeName.setter
    def i206Pb238U204CorrAgeErrorTypeName(self, value: str):
        self._i206Pb238U204CorrAgeErrorTypeName = convert_str(value)
    
    @property
    def i206Pb238U204CorrError(self):
        return self._i206Pb238U204CorrError

    @i206Pb238U204CorrError.setter
    def i206Pb238U204CorrError(self, value: float):
        self._i206Pb238U204CorrError = convert_float(value)
    
    @property
    def i206Pb238U204CorrErrorTypeId(self):
        return self._i206Pb238U204CorrErrorTypeId

    @i206Pb238U204CorrErrorTypeId.setter
    def i206Pb238U204CorrErrorTypeId(self, value: ):
        self._i206Pb238U204CorrErrorTypeId = convert_(value)
    
    @property
    def i206Pb238U204CorrErrorTypeName(self):
        return self._i206Pb238U204CorrErrorTypeName

    @i206Pb238U204CorrErrorTypeName.setter
    def i206Pb238U204CorrErrorTypeName(self, value: str):
        self._i206Pb238U204CorrErrorTypeName = convert_str(value)
    
    @property
    def i206Pb238U207Corr(self):
        return self._i206Pb238U207Corr

    @i206Pb238U207Corr.setter
    def i206Pb238U207Corr(self, value: float):
        self._i206Pb238U207Corr = convert_float(value)
    
    @property
    def i206Pb238U207CorrAge(self):
        return self._i206Pb238U207CorrAge

    @i206Pb238U207CorrAge.setter
    def i206Pb238U207CorrAge(self, value: float):
        self._i206Pb238U207CorrAge = convert_float(value)
    
    @property
    def i206Pb238U207CorrError(self):
        return self._i206Pb238U207CorrError

    @i206Pb238U207CorrError.setter
    def i206Pb238U207CorrError(self, value: float):
        self._i206Pb238U207CorrError = convert_float(value)
    
    @property
    def i206Pb238U207CorrErrorTypeId(self):
        return self._i206Pb238U207CorrErrorTypeId

    @i206Pb238U207CorrErrorTypeId.setter
    def i206Pb238U207CorrErrorTypeId(self, value: ):
        self._i206Pb238U207CorrErrorTypeId = convert_(value)
    
    @property
    def i206Pb238U207CorrErrorTypeName(self):
        return self._i206Pb238U207CorrErrorTypeName

    @i206Pb238U207CorrErrorTypeName.setter
    def i206Pb238U207CorrErrorTypeName(self, value: str):
        self._i206Pb238U207CorrErrorTypeName = convert_str(value)
    
    @property
    def i206Pb238U208Corr(self):
        return self._i206Pb238U208Corr

    @i206Pb238U208Corr.setter
    def i206Pb238U208Corr(self, value: float):
        self._i206Pb238U208Corr = convert_float(value)
    
    @property
    def i206Pb238U208CorrAge(self):
        return self._i206Pb238U208CorrAge

    @i206Pb238U208CorrAge.setter
    def i206Pb238U208CorrAge(self, value: float):
        self._i206Pb238U208CorrAge = convert_float(value)
    
    @property
    def i206Pb238U208CorrAgeError(self):
        return self._i206Pb238U208CorrAgeError

    @i206Pb238U208CorrAgeError.setter
    def i206Pb238U208CorrAgeError(self, value: float):
        self._i206Pb238U208CorrAgeError = convert_float(value)
    
    @property
    def i206Pb238U208CorrAgeErrorTypeId(self):
        return self._i206Pb238U208CorrAgeErrorTypeId

    @i206Pb238U208CorrAgeErrorTypeId.setter
    def i206Pb238U208CorrAgeErrorTypeId(self, value: ):
        self._i206Pb238U208CorrAgeErrorTypeId = convert_(value)
    
    @property
    def i206Pb238U208CorrAgeErrorTypeName(self):
        return self._i206Pb238U208CorrAgeErrorTypeName

    @i206Pb238U208CorrAgeErrorTypeName.setter
    def i206Pb238U208CorrAgeErrorTypeName(self, value: str):
        self._i206Pb238U208CorrAgeErrorTypeName = convert_str(value)
    
    @property
    def i206Pb238U208CorrError(self):
        return self._i206Pb238U208CorrError

    @i206Pb238U208CorrError.setter
    def i206Pb238U208CorrError(self, value: float):
        self._i206Pb238U208CorrError = convert_float(value)
    
    @property
    def i206Pb238U208CorrErrorTypeId(self):
        return self._i206Pb238U208CorrErrorTypeId

    @i206Pb238U208CorrErrorTypeId.setter
    def i206Pb238U208CorrErrorTypeId(self, value: int):
        self._i206Pb238U208CorrErrorTypeId = int(value)
    
    @property
    def i206Pb238U208CorrErrorTypeName(self):
        return self._i206Pb238U208CorrErrorTypeName

    @i206Pb238U208CorrErrorTypeName.setter
    def i206Pb238U208CorrErrorTypeName(self, value: str):
        self._i206Pb238U208CorrErrorTypeName = convert_str(value)
    
    @property
    def i206Pb238UTotal(self):
        return self._i206Pb238UTotal

    @i206Pb238UTotal.setter
    def i206Pb238UTotal(self, value: float):
        self._i206Pb238UTotal = convert_float(value)
    
    @property
    def i206Pb238UTotalAge(self):
        return self._i206Pb238UTotalAge

    @i206Pb238UTotalAge.setter
    def i206Pb238UTotalAge(self, value: float):
        self._i206Pb238UTotalAge = convert_float(value)
    
    @property
    def i206Pb238UTotalAgeError(self):
        return self._i206Pb238UTotalAgeError

    @i206Pb238UTotalAgeError.setter
    def i206Pb238UTotalAgeError(self, value: float):
        self._i206Pb238UTotalAgeError = convert_float(value)
    
    @property
    def i206Pb238UTotalAgeErrorTypeId(self):
        return self._i206Pb238UTotalAgeErrorTypeId

    @i206Pb238UTotalAgeErrorTypeId.setter
    def i206Pb238UTotalAgeErrorTypeId(self, value: int):
        self._i206Pb238UTotalAgeErrorTypeId = int(value)
    
    @property
    def i206Pb238UTotalAgeErrorTypeName(self):
        return self._i206Pb238UTotalAgeErrorTypeName

    @i206Pb238UTotalAgeErrorTypeName.setter
    def i206Pb238UTotalAgeErrorTypeName(self, value: str):
        self._i206Pb238UTotalAgeErrorTypeName = convert_str(value)
    
    @property
    def i206Pb238UTotalError(self):
        return self._i206Pb238UTotalError

    @i206Pb238UTotalError.setter
    def i206Pb238UTotalError(self, value: float):
        self._i206Pb238UTotalError = convert_float(value)
    
    @property
    def i206Pb238UTotalErrorTypeId(self):
        return self._i206Pb238UTotalErrorTypeId

    @i206Pb238UTotalErrorTypeId.setter
    def i206Pb238UTotalErrorTypeId(self, value: int):
        self._i206Pb238UTotalErrorTypeId = int(value)
    
    @property
    def i206Pb238UTotalErrorTypeName(self):
        return self._i206Pb238UTotalErrorTypeName

    @i206Pb238UTotalErrorTypeName.setter
    def i206Pb238UTotalErrorTypeName(self, value: str):
        self._i206Pb238UTotalErrorTypeName = convert_str(value)
    
    @property
    def i207Pb206Pb204Corr(self):
        return self._i207Pb206Pb204Corr

    @i207Pb206Pb204Corr.setter
    def i207Pb206Pb204Corr(self, value: float):
        self._i207Pb206Pb204Corr = convert_float(value)
    
    @property
    def i207Pb206Pb204CorrAge(self):
        return self._i207Pb206Pb204CorrAge

    @i207Pb206Pb204CorrAge.setter
    def i207Pb206Pb204CorrAge(self, value: float):
        self._i207Pb206Pb204CorrAge = convert_float(value)
    
    @property
    def i207Pb206Pb204CorrAgeError(self):
        return self._i207Pb206Pb204CorrAgeError

    @i207Pb206Pb204CorrAgeError.setter
    def i207Pb206Pb204CorrAgeError(self, value: float):
        self._i207Pb206Pb204CorrAgeError = convert_float(value)
    
    @property
    def i207Pb206Pb204CorrAgeErrorTypeId(self):
        return self._i207Pb206Pb204CorrAgeErrorTypeId

    @i207Pb206Pb204CorrAgeErrorTypeId.setter
    def i207Pb206Pb204CorrAgeErrorTypeId(self, value: ):
        self._i207Pb206Pb204CorrAgeErrorTypeId = convert_(value)
    
    @property
    def i207Pb206Pb204CorrAgeErrorTypeName(self):
        return self._i207Pb206Pb204CorrAgeErrorTypeName

    @i207Pb206Pb204CorrAgeErrorTypeName.setter
    def i207Pb206Pb204CorrAgeErrorTypeName(self, value: str):
        self._i207Pb206Pb204CorrAgeErrorTypeName = convert_str(value)
    
    @property
    def i207Pb206Pb204CorrError(self):
        return self._i207Pb206Pb204CorrError

    @i207Pb206Pb204CorrError.setter
    def i207Pb206Pb204CorrError(self, value: float):
        self._i207Pb206Pb204CorrError = convert_float(value)
    
    @property
    def i207Pb206Pb204CorrErrorTypeId(self):
        return self._i207Pb206Pb204CorrErrorTypeId

    @i207Pb206Pb204CorrErrorTypeId.setter
    def i207Pb206Pb204CorrErrorTypeId(self, value: ):
        self._i207Pb206Pb204CorrErrorTypeId = convert_(value)
    
    @property
    def i207Pb206Pb204CorrErrorTypeName(self):
        return self._i207Pb206Pb204CorrErrorTypeName

    @i207Pb206Pb204CorrErrorTypeName.setter
    def i207Pb206Pb204CorrErrorTypeName(self, value: str):
        self._i207Pb206Pb204CorrErrorTypeName = convert_str(value)
    
    @property
    def i207Pb206Pb208Corr(self):
        return self._i207Pb206Pb208Corr

    @i207Pb206Pb208Corr.setter
    def i207Pb206Pb208Corr(self, value: float):
        self._i207Pb206Pb208Corr = convert_float(value)
    
    @property
    def i207Pb206Pb208CorrAge(self):
        return self._i207Pb206Pb208CorrAge

    @i207Pb206Pb208CorrAge.setter
    def i207Pb206Pb208CorrAge(self, value: float):
        self._i207Pb206Pb208CorrAge = convert_float(value)
    
    @property
    def i207Pb206Pb208CorrAgeError(self):
        return self._i207Pb206Pb208CorrAgeError

    @i207Pb206Pb208CorrAgeError.setter
    def i207Pb206Pb208CorrAgeError(self, value: float):
        self._i207Pb206Pb208CorrAgeError = convert_float(value)
    
    @property
    def i207Pb206Pb208CorrAgeErrorTypeId(self):
        return self._i207Pb206Pb208CorrAgeErrorTypeId

    @i207Pb206Pb208CorrAgeErrorTypeId.setter
    def i207Pb206Pb208CorrAgeErrorTypeId(self, value: ):
        self._i207Pb206Pb208CorrAgeErrorTypeId = convert_(value)
    
    @property
    def i207Pb206Pb208CorrAgeErrorTypeName(self):
        return self._i207Pb206Pb208CorrAgeErrorTypeName

    @i207Pb206Pb208CorrAgeErrorTypeName.setter
    def i207Pb206Pb208CorrAgeErrorTypeName(self, value: str):
        self._i207Pb206Pb208CorrAgeErrorTypeName = convert_str(value)
    
    @property
    def i207Pb206Pb208CorrError(self):
        return self._i207Pb206Pb208CorrError

    @i207Pb206Pb208CorrError.setter
    def i207Pb206Pb208CorrError(self, value: float):
        self._i207Pb206Pb208CorrError = convert_float(value)
    
    @property
    def i207Pb206Pb208CorrErrorTypeId(self):
        return self._i207Pb206Pb208CorrErrorTypeId

    @i207Pb206Pb208CorrErrorTypeId.setter
    def i207Pb206Pb208CorrErrorTypeId(self, value: int):
        self._i207Pb206Pb208CorrErrorTypeId = int(value)
    
    @property
    def i207Pb206Pb208CorrErrorTypeName(self):
        return self._i207Pb206Pb208CorrErrorTypeName

    @i207Pb206Pb208CorrErrorTypeName.setter
    def i207Pb206Pb208CorrErrorTypeName(self, value: str):
        self._i207Pb206Pb208CorrErrorTypeName = convert_str(value)
    
    @property
    def i207Pb206PbTotal(self):
        return self._i207Pb206PbTotal

    @i207Pb206PbTotal.setter
    def i207Pb206PbTotal(self, value: float):
        self._i207Pb206PbTotal = convert_float(value)
    
    @property
    def i207Pb206PbTotalAge(self):
        return self._i207Pb206PbTotalAge

    @i207Pb206PbTotalAge.setter
    def i207Pb206PbTotalAge(self, value: float):
        self._i207Pb206PbTotalAge = convert_float(value)
    
    @property
    def i207Pb206PbTotalAgeError(self):
        return self._i207Pb206PbTotalAgeError

    @i207Pb206PbTotalAgeError.setter
    def i207Pb206PbTotalAgeError(self, value: float):
        self._i207Pb206PbTotalAgeError = convert_float(value)
    
    @property
    def i207Pb206PbTotalAgeErrorTypeId(self):
        return self._i207Pb206PbTotalAgeErrorTypeId

    @i207Pb206PbTotalAgeErrorTypeId.setter
    def i207Pb206PbTotalAgeErrorTypeId(self, value: int):
        self._i207Pb206PbTotalAgeErrorTypeId = int(value)
    
    @property
    def i207Pb206PbTotalAgeErrorTypeName(self):
        return self._i207Pb206PbTotalAgeErrorTypeName

    @i207Pb206PbTotalAgeErrorTypeName.setter
    def i207Pb206PbTotalAgeErrorTypeName(self, value: str):
        self._i207Pb206PbTotalAgeErrorTypeName = convert_str(value)
    
    @property
    def i207Pb206PbTotalError(self):
        return self._i207Pb206PbTotalError

    @i207Pb206PbTotalError.setter
    def i207Pb206PbTotalError(self, value: float):
        self._i207Pb206PbTotalError = convert_float(value)
    
    @property
    def i207Pb206PbTotalErrorTypeId(self):
        return self._i207Pb206PbTotalErrorTypeId

    @i207Pb206PbTotalErrorTypeId.setter
    def i207Pb206PbTotalErrorTypeId(self, value: int):
        self._i207Pb206PbTotalErrorTypeId = int(value)
    
    @property
    def i207Pb206PbTotalErrorTypeName(self):
        return self._i207Pb206PbTotalErrorTypeName

    @i207Pb206PbTotalErrorTypeName.setter
    def i207Pb206PbTotalErrorTypeName(self, value: str):
        self._i207Pb206PbTotalErrorTypeName = convert_str(value)
    
    @property
    def i207Pb235U204Corr(self):
        return self._i207Pb235U204Corr

    @i207Pb235U204Corr.setter
    def i207Pb235U204Corr(self, value: float):
        self._i207Pb235U204Corr = convert_float(value)
    
    @property
    def i207Pb235U204CorrAge(self):
        return self._i207Pb235U204CorrAge

    @i207Pb235U204CorrAge.setter
    def i207Pb235U204CorrAge(self, value: float):
        self._i207Pb235U204CorrAge = convert_float(value)
    
    @property
    def i207Pb235U204CorrAgeError(self):
        return self._i207Pb235U204CorrAgeError

    @i207Pb235U204CorrAgeError.setter
    def i207Pb235U204CorrAgeError(self, value: float):
        self._i207Pb235U204CorrAgeError = convert_float(value)
    
    @property
    def i207Pb235U204CorrAgeErrorTypeId(self):
        return self._i207Pb235U204CorrAgeErrorTypeId

    @i207Pb235U204CorrAgeErrorTypeId.setter
    def i207Pb235U204CorrAgeErrorTypeId(self, value: int):
        self._i207Pb235U204CorrAgeErrorTypeId = int(value)
    
    @property
    def i207Pb235U204CorrAgeErrorTypeName(self):
        return self._i207Pb235U204CorrAgeErrorTypeName

    @i207Pb235U204CorrAgeErrorTypeName.setter
    def i207Pb235U204CorrAgeErrorTypeName(self, value: str):
        self._i207Pb235U204CorrAgeErrorTypeName = convert_str(value)
    
    @property
    def i207Pb235U204CorrError(self):
        return self._i207Pb235U204CorrError

    @i207Pb235U204CorrError.setter
    def i207Pb235U204CorrError(self, value: float):
        self._i207Pb235U204CorrError = convert_float(value)
    
    @property
    def i207Pb235U204CorrErrorTypeId(self):
        return self._i207Pb235U204CorrErrorTypeId

    @i207Pb235U204CorrErrorTypeId.setter
    def i207Pb235U204CorrErrorTypeId(self, value: int):
        self._i207Pb235U204CorrErrorTypeId = int(value)
    
    @property
    def i207Pb235U204CorrErrorTypeName(self):
        return self._i207Pb235U204CorrErrorTypeName

    @i207Pb235U204CorrErrorTypeName.setter
    def i207Pb235U204CorrErrorTypeName(self, value: str):
        self._i207Pb235U204CorrErrorTypeName = convert_str(value)
    
    @property
    def i207Pb235U208Corr(self):
        return self._i207Pb235U208Corr

    @i207Pb235U208Corr.setter
    def i207Pb235U208Corr(self, value: float):
        self._i207Pb235U208Corr = convert_float(value)
    
    @property
    def i207Pb235U208CorrAge(self):
        return self._i207Pb235U208CorrAge

    @i207Pb235U208CorrAge.setter
    def i207Pb235U208CorrAge(self, value: float):
        self._i207Pb235U208CorrAge = convert_float(value)
    
    @property
    def i207Pb235U208CorrAgeError(self):
        return self._i207Pb235U208CorrAgeError

    @i207Pb235U208CorrAgeError.setter
    def i207Pb235U208CorrAgeError(self, value: float):
        self._i207Pb235U208CorrAgeError = convert_float(value)
    
    @property
    def i207Pb235U208CorrAgeErrorTypeId(self):
        return self._i207Pb235U208CorrAgeErrorTypeId

    @i207Pb235U208CorrAgeErrorTypeId.setter
    def i207Pb235U208CorrAgeErrorTypeId(self, value: int):
        self._i207Pb235U208CorrAgeErrorTypeId = int(value)
    
    @property
    def i207Pb235U208CorrAgeErrorTypeName(self):
        return self._i207Pb235U208CorrAgeErrorTypeName

    @i207Pb235U208CorrAgeErrorTypeName.setter
    def i207Pb235U208CorrAgeErrorTypeName(self, value: str):
        self._i207Pb235U208CorrAgeErrorTypeName = convert_str(value)
    
    @property
    def i207Pb235U208CorrError(self):
        return self._i207Pb235U208CorrError

    @i207Pb235U208CorrError.setter
    def i207Pb235U208CorrError(self, value: float):
        self._i207Pb235U208CorrError = convert_float(value)
    
    @property
    def i207Pb235U208CorrErrorTypeId(self):
        return self._i207Pb235U208CorrErrorTypeId

    @i207Pb235U208CorrErrorTypeId.setter
    def i207Pb235U208CorrErrorTypeId(self, value: int):
        self._i207Pb235U208CorrErrorTypeId = int(value)
    
    @property
    def i207Pb235U208CorrErrorTypeName(self):
        return self._i207Pb235U208CorrErrorTypeName

    @i207Pb235U208CorrErrorTypeName.setter
    def i207Pb235U208CorrErrorTypeName(self, value: str):
        self._i207Pb235U208CorrErrorTypeName = convert_str(value)
    
    @property
    def i207Pb235UTotalAge(self):
        return self._i207Pb235UTotalAge

    @i207Pb235UTotalAge.setter
    def i207Pb235UTotalAge(self, value: float):
        self._i207Pb235UTotalAge = convert_float(value)
    
    @property
    def i207Pb235UTotalAgeError(self):
        return self._i207Pb235UTotalAgeError

    @i207Pb235UTotalAgeError.setter
    def i207Pb235UTotalAgeError(self, value: float):
        self._i207Pb235UTotalAgeError = convert_float(value)
    
    @property
    def i207Pb235UTotalAgeErrorTypeId(self):
        return self._i207Pb235UTotalAgeErrorTypeId

    @i207Pb235UTotalAgeErrorTypeId.setter
    def i207Pb235UTotalAgeErrorTypeId(self, value: int):
        self._i207Pb235UTotalAgeErrorTypeId = int(value)
    
    @property
    def i207Pb235UTotalAgeErrorTypeName(self):
        return self._i207Pb235UTotalAgeErrorTypeName

    @i207Pb235UTotalAgeErrorTypeName.setter
    def i207Pb235UTotalAgeErrorTypeName(self, value: str):
        self._i207Pb235UTotalAgeErrorTypeName = convert_str(value)
    
    @property
    def i208CorrErrorCorrelation(self):
        return self._i208CorrErrorCorrelation

    @i208CorrErrorCorrelation.setter
    def i208CorrErrorCorrelation(self, value: float):
        self._i208CorrErrorCorrelation = convert_float(value)
    
    @property
    def i208Pb206Pb204Corr(self):
        return self._i208Pb206Pb204Corr

    @i208Pb206Pb204Corr.setter
    def i208Pb206Pb204Corr(self, value: float):
        self._i208Pb206Pb204Corr = convert_float(value)
    
    @property
    def i208Pb206Pb204CorrError(self):
        return self._i208Pb206Pb204CorrError

    @i208Pb206Pb204CorrError.setter
    def i208Pb206Pb204CorrError(self, value: float):
        self._i208Pb206Pb204CorrError = convert_float(value)
    
    @property
    def i208Pb206Pb204CorrErrorTypeId(self):
        return self._i208Pb206Pb204CorrErrorTypeId

    @i208Pb206Pb204CorrErrorTypeId.setter
    def i208Pb206Pb204CorrErrorTypeId(self, value: int):
        self._i208Pb206Pb204CorrErrorTypeId = int(value)
    
    @property
    def i208Pb206Pb204CorrErrorTypeName(self):
        return self._i208Pb206Pb204CorrErrorTypeName

    @i208Pb206Pb204CorrErrorTypeName.setter
    def i208Pb206Pb204CorrErrorTypeName(self, value: str):
        self._i208Pb206Pb204CorrErrorTypeName = convert_str(value)
    
    @property
    def i208Pb206PbTotal(self):
        return self._i208Pb206PbTotal

    @i208Pb206PbTotal.setter
    def i208Pb206PbTotal(self, value: float):
        self._i208Pb206PbTotal = convert_float(value)
    
    @property
    def i208Pb206PbTotalError(self):
        return self._i208Pb206PbTotalError

    @i208Pb206PbTotalError.setter
    def i208Pb206PbTotalError(self, value: float):
        self._i208Pb206PbTotalError = convert_float(value)
    
    @property
    def i208Pb206PbTotalErrorTypeId(self):
        return self._i208Pb206PbTotalErrorTypeId

    @i208Pb206PbTotalErrorTypeId.setter
    def i208Pb206PbTotalErrorTypeId(self, value: int):
        self._i208Pb206PbTotalErrorTypeId = int(value)
    
    @property
    def i208Pb206PbTotalErrorTypeName(self):
        return self._i208Pb206PbTotalErrorTypeName

    @i208Pb206PbTotalErrorTypeName.setter
    def i208Pb206PbTotalErrorTypeName(self, value: str):
        self._i208Pb206PbTotalErrorTypeName = convert_str(value)
    
    @property
    def i208Pb232Th204Corr(self):
        return self._i208Pb232Th204Corr

    @i208Pb232Th204Corr.setter
    def i208Pb232Th204Corr(self, value: float):
        self._i208Pb232Th204Corr = convert_float(value)
    
    @property
    def i208Pb232Th204CorrAge(self):
        return self._i208Pb232Th204CorrAge

    @i208Pb232Th204CorrAge.setter
    def i208Pb232Th204CorrAge(self, value: float):
        self._i208Pb232Th204CorrAge = convert_float(value)
    
    @property
    def i208Pb232Th204CorrAgeError(self):
        return self._i208Pb232Th204CorrAgeError

    @i208Pb232Th204CorrAgeError.setter
    def i208Pb232Th204CorrAgeError(self, value: float):
        self._i208Pb232Th204CorrAgeError = convert_float(value)
    
    @property
    def i208Pb232Th204CorrAgeErrorTypeId(self):
        return self._i208Pb232Th204CorrAgeErrorTypeId

    @i208Pb232Th204CorrAgeErrorTypeId.setter
    def i208Pb232Th204CorrAgeErrorTypeId(self, value: int):
        self._i208Pb232Th204CorrAgeErrorTypeId = int(value)
    
    @property
    def i208Pb232Th204CorrAgeErrorTypeName(self):
        return self._i208Pb232Th204CorrAgeErrorTypeName

    @i208Pb232Th204CorrAgeErrorTypeName.setter
    def i208Pb232Th204CorrAgeErrorTypeName(self, value: str):
        self._i208Pb232Th204CorrAgeErrorTypeName = convert_str(value)
    
    @property
    def i208Pb232Th204CorrError(self):
        return self._i208Pb232Th204CorrError

    @i208Pb232Th204CorrError.setter
    def i208Pb232Th204CorrError(self, value: float):
        self._i208Pb232Th204CorrError = convert_float(value)
    
    @property
    def i208Pb232Th204CorrErrorTypeId(self):
        return self._i208Pb232Th204CorrErrorTypeId

    @i208Pb232Th204CorrErrorTypeId.setter
    def i208Pb232Th204CorrErrorTypeId(self, value: int):
        self._i208Pb232Th204CorrErrorTypeId = int(value)
    
    @property
    def i208Pb232Th204CorrErrorTypeName(self):
        return self._i208Pb232Th204CorrErrorTypeName

    @i208Pb232Th204CorrErrorTypeName.setter
    def i208Pb232Th204CorrErrorTypeName(self, value: str):
        self._i208Pb232Th204CorrErrorTypeName = convert_str(value)
    
    @property
    def i208Pb232ThTotal(self):
        return self._i208Pb232ThTotal

    @i208Pb232ThTotal.setter
    def i208Pb232ThTotal(self, value: float):
        self._i208Pb232ThTotal = convert_float(value)
    
    @property
    def i208Pb232ThTotalAge(self):
        return self._i208Pb232ThTotalAge

    @i208Pb232ThTotalAge.setter
    def i208Pb232ThTotalAge(self, value: float):
        self._i208Pb232ThTotalAge = convert_float(value)
    
    @property
    def i208Pb232ThTotalAgeError(self):
        return self._i208Pb232ThTotalAgeError

    @i208Pb232ThTotalAgeError.setter
    def i208Pb232ThTotalAgeError(self, value: float):
        self._i208Pb232ThTotalAgeError = convert_float(value)
    
    @property
    def i208Pb232ThTotalAgeErrorTypeId(self):
        return self._i208Pb232ThTotalAgeErrorTypeId

    @i208Pb232ThTotalAgeErrorTypeId.setter
    def i208Pb232ThTotalAgeErrorTypeId(self, value: int):
        self._i208Pb232ThTotalAgeErrorTypeId = int(value)
    
    @property
    def i208Pb232ThTotalAgeErrorTypeName(self):
        return self._i208Pb232ThTotalAgeErrorTypeName

    @i208Pb232ThTotalAgeErrorTypeName.setter
    def i208Pb232ThTotalAgeErrorTypeName(self, value: str):
        self._i208Pb232ThTotalAgeErrorTypeName = convert_str(value)
    
    @property
    def i208Pb232ThTotalError(self):
        return self._i208Pb232ThTotalError

    @i208Pb232ThTotalError.setter
    def i208Pb232ThTotalError(self, value: float):
        self._i208Pb232ThTotalError = convert_float(value)
    
    @property
    def i208Pb232ThTotalErrorTypeId(self):
        return self._i208Pb232ThTotalErrorTypeId

    @i208Pb232ThTotalErrorTypeId.setter
    def i208Pb232ThTotalErrorTypeId(self, value: int):
        self._i208Pb232ThTotalErrorTypeId = int(value)
    
    @property
    def i208Pb232ThTotalErrorTypeName(self):
        return self._i208Pb232ThTotalErrorTypeName

    @i208Pb232ThTotalErrorTypeName.setter
    def i208Pb232ThTotalErrorTypeName(self, value: str):
        self._i208Pb232ThTotalErrorTypeName = convert_str(value)
    
    @property
    def i232Th(self):
        return self._i232Th

    @i232Th.setter
    def i232Th(self, value: float):
        self._i232Th = convert_float(value)
    
    @property
    def i232Th238U(self):
        return self._i232Th238U

    @i232Th238U.setter
    def i232Th238U(self, value: float):
        self._i232Th238U = convert_float(value)
    
    @property
    def i238U(self):
        return self._i238U

    @i238U.setter
    def i238U(self, value: float):
        self._i238U = convert_float(value)
    
    @property
    def i238U206Pb204Corr(self):
        return self._i238U206Pb204Corr

    @i238U206Pb204Corr.setter
    def i238U206Pb204Corr(self, value: float):
        self._i238U206Pb204Corr = convert_float(value)
    
    @property
    def i238U206Pb204CorrError(self):
        return self._i238U206Pb204CorrError

    @i238U206Pb204CorrError.setter
    def i238U206Pb204CorrError(self, value: float):
        self._i238U206Pb204CorrError = convert_float(value)
    
    @property
    def i238U206Pb204CorrErrorTypeId(self):
        return self._i238U206Pb204CorrErrorTypeId

    @i238U206Pb204CorrErrorTypeId.setter
    def i238U206Pb204CorrErrorTypeId(self, value: int):
        self._i238U206Pb204CorrErrorTypeId = int(value)
    
    @property
    def i238U206Pb204CorrErrorTypeName(self):
        return self._i238U206Pb204CorrErrorTypeName

    @i238U206Pb204CorrErrorTypeName.setter
    def i238U206Pb204CorrErrorTypeName(self, value: str):
        self._i238U206Pb204CorrErrorTypeName = convert_str(value)
    
    @property
    def i238U206Pb208Corr(self):
        return self._i238U206Pb208Corr

    @i238U206Pb208Corr.setter
    def i238U206Pb208Corr(self, value: float):
        self._i238U206Pb208Corr = convert_float(value)
    
    @property
    def i238U206Pb208CorrError(self):
        return self._i238U206Pb208CorrError

    @i238U206Pb208CorrError.setter
    def i238U206Pb208CorrError(self, value: float):
        self._i238U206Pb208CorrError = convert_float(value)
    
    @property
    def i238U206Pb208CorrErrorTypeId(self):
        return self._i238U206Pb208CorrErrorTypeId

    @i238U206Pb208CorrErrorTypeId.setter
    def i238U206Pb208CorrErrorTypeId(self, value: int):
        self._i238U206Pb208CorrErrorTypeId = int(value)
    
    @property
    def i238U206Pb208CorrErrorTypeName(self):
        return self._i238U206Pb208CorrErrorTypeName

    @i238U206Pb208CorrErrorTypeName.setter
    def i238U206Pb208CorrErrorTypeName(self, value: str):
        self._i238U206Pb208CorrErrorTypeName = convert_str(value)
    
    @property
    def i238U206PbTotal(self):
        return self._i238U206PbTotal

    @i238U206PbTotal.setter
    def i238U206PbTotal(self, value: float):
        self._i238U206PbTotal = convert_float(value)
    
    @property
    def i238U206PbTotalError(self):
        return self._i238U206PbTotalError

    @i238U206PbTotalError.setter
    def i238U206PbTotalError(self, value: float):
        self._i238U206PbTotalError = convert_float(value)
    
    @property
    def i238U206PbTotalErrorTypeId(self):
        return self._i238U206PbTotalErrorTypeId

    @i238U206PbTotalErrorTypeId.setter
    def i238U206PbTotalErrorTypeId(self, value: int):
        self._i238U206PbTotalErrorTypeId = int(value)
    
    @property
    def i238U206PbTotalErrorTypeName(self):
        return self._i238U206PbTotalErrorTypeName

    @i238U206PbTotalErrorTypeName.setter
    def i238U206PbTotalErrorTypeName(self, value: str):
        self._i238U206PbTotalErrorTypeName = convert_str(value)
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = int(value)
    
    @property
    def refMaterialId(self):
        return self._refMaterialId

    @refMaterialId.setter
    def refMaterialId(self, value: float):
        self._refMaterialId = convert_float(value)
    
    @property
    def refMaterialName(self):
        return self._refMaterialName

    @refMaterialName.setter
    def refMaterialName(self, value: str):
        self._refMaterialName = convert_str(value)
    
    @property
    def shrimpdataPointId(self):
        return self._shrimpdataPointId

    @shrimpdataPointId.setter
    def shrimpdataPointId(self, value: int):
        self._shrimpdataPointId = int(value)
    
    @property
    def spotIdentifier(self):
        return self._spotIdentifier

    @spotIdentifier.setter
    def spotIdentifier(self, value: str):
        self._spotIdentifier = convert_str(value)
    
    @property
    def totalDiscordancePercent(self):
        return self._totalDiscordancePercent

    @totalDiscordancePercent.setter
    def totalDiscordancePercent(self, value: float):
        self._totalDiscordancePercent = convert_float(value)
    
        