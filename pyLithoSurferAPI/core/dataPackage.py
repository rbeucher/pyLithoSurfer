from pyLithoSurferAPI import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json
import urllib.parse


class DataPackage2Editor(APIRequests):
        
    path = URL_BASE+'/api/management/data-package-2-editors'


class DataPackage2Supervisor(APIRequests):
        
    path = URL_BASE+'/api/management/data-package-2-supervisors'


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
        responseA = A.query(urllib.parse.urlencode(query))
        for item in responseA.json():
            if item["login"] == name:
                user_id = item["id"]
        
        if not user_id:
            raise ValueError("""Cannot find user id""")

        B = LithoUser()
        query = {"userId.in": user_id}
        response = B.query(urllib.parse.urlencode(query))
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

    def get_id_from_name(self, name: str):
        entries = self.get_all()
        values = entries[entries.name == name]["id"].values
        if len(values) > 1:
            raise ValueError(f"Multiple ids present for {name}")
        else:
            return values[0]