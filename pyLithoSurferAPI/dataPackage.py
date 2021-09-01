from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json
from .dataPackage2Editor import DataPackage2Editor
from .dataPackage2Supervisor import DataPackage2Supervisor
from .utilities import get_id_from_list
import urllib.parse

class DataPackage(APIRequests):

    path = URL_BASE + "/api/management/data-packages"

    def __init__(self, distribution="PRIVATE", workflowState="IN_PROGRESS", **kwargs):
        self.distribution = distribution
        self.workflowState = workflowState
        for key, val in kwargs.items():
            setattr(self, key, val)

    def new(self, *args, **kwargs):
        from . import LITHODAT_USERNAME as name
        from . import User, LithoUser
        A = User()
        query={"login.in": name}
        responseA = A.get_from_query(urllib.parse.urlencode(query))
        for item in responseA.json():
            if item["login"] == name:
                user_id = item["id"]
        
        if not user_id:
            raise ValueError("""Cannot find user id""")

        B = LithoUser()
        query = {"userId.in": user_id}
        response = B.get_from_query(urllib.parse.urlencode(query))
        if response:
            litho_user_id = response.json()[0]["id"]        

        if not litho_user_id:
            raise ValueError("""Cannot find lithouser id""")

        responseB = super().new(*args, **kwargs)
        if responseB and responseB["id"]:
            data_package_id = responseB["id"]
            dpkg2editor = DataPackage2Editor(dataPackageId=data_package_id, lithoUserId=litho_user_id)
            responseC = dpkg2editor.new(*args, **kwargs)
            dpkg2supervisor = DataPackage2Supervisor(dataPackageId=data_package_id, lithoUserId=litho_user_id)
            responseD = dpkg2supervisor.new(*args, **kwargs)

        return [responseA, responseB, responseC, responseD]        

    @property
    def description(self):
        return self._describtion

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def distribution(self):
        return self._distribution

    @distribution.setter
    def distribution(self, value):
        self._distribution = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def institutionId(self):
        return self._institutionId

    @institutionId.setter
    def institutionId(self, value):
        self._institutionId = value

    @property
    def institutionName(self):
        return self._institutionName

    @institutionName.setter
    def institutionName(self, value):
        self._institutionName = value

    @property
    def licenseText(self):
        return self._licenseText

    @licenseText.setter
    def licenseText(self, value):
        self._licenseText = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def workflowState(self):
        return self._workflowState

    @workflowState.setter
    def workflowState(self, value):
        self._workflowState = value

    def get_id_from_name(self, name: str):
        entries = self.get_all()
        values = entries[entries.name == name]["id"].values
        if len(values) > 1:
            raise ValueError(f"Multiple ids present for {name}")
        else:
            return values[0]