from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
from .REST import check_response
import json
import pandas as pd
import numpy as np
from .utilities import *
from .geoeventAtAge import GeoeventAtAge
from .statement import Statement


class SHRIMPAge(APIRequests):
        
    path = URL_BASE+'/api/shrimp-ages'

    def __init__(self,
                 ageGroupId: Union[int, np.int16, np.int32, np.int64, None] = None,
                 ageGroupName: str = None,
                 ageTypeId: Union[int, np.int16, np.int32, np.int64] = 0,
                 ageTypeName: str = None,
                 calcName: str = None,
                 mswd: Union[float, np.float16, np.float32, np.float64] = 0,
                 numberAnalysesCombined: Union[int, np.int16, np.int32, np.int64, None] = None,
                 rmQcTest: str = None,
                ):
        
        self.ageGroupId = ageGroupId
        self.ageGroupName = ageGroupName
        self.ageTypeId = ageTypeId
        self.ageTypeName = ageTypeName
        self.calcName = calcName
        self.mswd = mswd
        self.numberAnalysesCombined = numberAnalysesCombined
        self.rmQcTest = rmQcTest

        self.id = None
    
    @property
    def ageGroupId(self):
        return self._ageGroupId

    @ageGroupId.setter
    def ageGroupId(self, value):
        self._ageGroupId = value
    
    @property
    def ageGroupName(self):
        return self._ageGroupName

    @ageGroupName.setter
    def ageGroupName(self, value: str):
        self._ageGroupName = convert_str(value)
    
    @property
    def ageTypeId(self):
        return self._ageTypeId

    @ageTypeId.setter
    def ageTypeId(self, value: int):
        self._ageTypeId = int(value)
    
    @property
    def ageTypeName(self):
        return self._ageTypeName

    @ageTypeName.setter
    def ageTypeName(self, value: str):
        self._ageTypeName = convert_str(value)
    
    @property
    def calcName(self):
        return self._calcName

    @calcName.setter
    def calcName(self, value: str):
        self._calcName = convert_str(value)
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def mswd(self):
        return self._mswd

    @mswd.setter
    def mswd(self, value: float):
        self._mswd = convert_float(value)
    
    @property
    def numberAnalysesCombined(self):
        return self._numberAnalysesCombined

    @numberAnalysesCombined.setter
    def numberAnalysesCombined(self, value):
        if value:
            self._numberAnalysesCombined = int(value)
        else:
            self._numberAnalysesCombined = None
    
    @property
    def rmQcTest(self):
        return self._rmQcTest

    @rmQcTest.setter
    def rmQcTest(self, value: str):
        self._rmQcTest = convert_str(value)
    


class SHRIMPAgeCRUD(APIRequests):

    path = URL_BASE+'/api/shrimp/shrimp-ages'

    def __init__(self, geoeventAtAge: GeoeventAtAge, statement: Statement, shrimpAge: SHRIMPAge):

        self.geoeventAtAge = geoeventAtAge
        self.statement = statement
        self.shrimpAge = shrimpAge

        self.id = None    

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64, None]):
        self._id = convert_int(value)

    @property
    def geoeventAtAge(self):
        return self._geoeventAtAge

    @geoeventAtAge.setter
    def geoeventAtAge(self, value: GeoeventAtAge):
        self._geoeventAtAge = value
    
    @property
    def statement(self):
        return self._statement

    @statement.setter
    def statement(self, value: Statement):
        self._statement = value
    
    @property
    def shrimpAge(self):
        return self._shrimpAge

    @shrimpAge.setter
    def shrimpAge(self, value: SHRIMPAge):
        self._shrimpAge = value

    def new(self, debug=False):
        data = {}
        data["geoEventAtAgeExtendsStatementDTO"] = {}
        geoeventAtAge = self.geoeventAtAge.to_dict()
        if "id" in geoeventAtAge.keys():
            geoeventAtAge.pop("id")
        data["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"] = geoeventAtAge
        statement = self.statement.to_dict()
        if "id" in statement.keys():
            statement.pop("id")
        data["geoEventAtAgeExtendsStatementDTO"]["statementDTO"] = statement
        shrimpAge = self.shrimpAge.to_dict()
        if "id" in shrimpAge.keys():
            shrimpAge.pop("id")
        data["shrimpageDTO"] = shrimpAge

        headers = session.headers
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"

        response = session.post(self.path, data=json.dumps(data), headers=headers)
        if debug:
            print(response.json())
        check_response(response)
        response = response.json()
        if "id" in response.keys():
            self.id = response["id"]
        if "geoeventAtAge" in response.keys() and "id" in response["geoeventAtAge"].keys():
            self.geoeventAtAge.id = response["geoeventAtAge"]["id"]
            self.geoeventAtAgeID = self.geoeventAtAge.id
        if "statement" in response.keys() and "id" in response["statement"].keys():
            self.statement.id = response["statement"]["id"]
        if "shrimpAge" in response.keys() and "id" in response["shrimpAge"].keys():
            self.shrimpAge.id = response["shrimpAge"]["id"]
        return response   