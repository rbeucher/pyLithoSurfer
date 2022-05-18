from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.utilities import NumpyEncoder
from pyLithoSurferAPI.core.tables import DataPoint
import json

class GCDataPoint(APIRequests):

    API_PATH = "/api/gc-data-points"


class GCDataPointCRUD(APIRequests):

    API_PATH = "/api/geochem/GCDataPoint"


class GCAliquotCRUD(APIRequests):

    API_PATH = "/api/geochem/GCAliquot"


class ElementalConcentrationCRUD(APIRequests):

    API_PATH = "/api/geochem/ElementalConcentration"


class OxideConcentrationCRUD(APIRequests):

    API_PATH = "/api/geochem/OxideConcentration"



