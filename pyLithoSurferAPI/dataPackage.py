from . import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import json


class DataPackage(APIRequests):

    path = URL_BASE + "/api/data-packages"

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def describtion(self):
        return self._describtion

    @describtion.setter
    def describtion(self, value):
        self._describtion = value

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

