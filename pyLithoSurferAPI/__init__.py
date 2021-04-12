import os
import requests

URL_BASE = 'https://testapp.lithodat.com'

LITHODAT_USERNAME = os.environ.get("LITHODAT_USERNAME", None)
LITHODAT_PASSWORD = os.environ.get("LITHODAT_PASSWORD", None)

def get_token(username: str, password: str, remember_me=False):
    url = URL_BASE + '/api/authenticate'
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    data = {'username': username,
            'password': password,
            'rememberMe': remember_me}
    return requests.post(url, json=data, headers=headers).json()['id_token']

LITHOSURFER_API_KEY = get_token(LITHODAT_USERNAME, LITHODAT_PASSWORD)

class APIKeyMissingError(Exception):
    pass

if LITHOSURFER_API_KEY is None:
    raise APIKeyMissingError("""All methods require an API key""")

session = requests.Session()
session.headers = {}
session.headers["Authorization"] = f"Bearer {LITHOSURFER_API_KEY}"
#session.headers["Accept"] = "*/*"
#session.headers["Content-Type"] = "*/*"

from .literature import Literature
from .SHRIMPDataPoint import SHRIMPDataPoint

from .basket import Basket
from .community import Community
from .dataPackage import DataPackage
from .dataPoint import DataPoint
from .datapointProperty import DatapointProperty
from .fissionTrack import FissionTrack
from .tempGradient import TempGradient
from .helium import Helium
from .institution import Institution
from .kArgon import KArgon
from .lErrorAgeType import LErrorAgeType
from .lithoRequest import LithoRequest
from .lithoUser import LithoUser
from .lLab import LLab
from .lLocCapture import LLocCapture
from .lLocationKind import LLocationKind
from .lLocPredefined import LLocPredefined
from .location import Location
from .locationProperty import LocationProperty
from .lSampleType import LSampleType
from .lThermDiffusion import LThermDiffusion
from .lThermDosimeter import LThermDosimeter
from .lThermEtch import LThermEtch
from .rbSr import RbSr
from .reOs import ReOs
from .sample import Sample
from .singleGrain import SingleGrain
from .singleGrainHe import SingleGrainHe
from .smNd import SmNd
from .thermalHistory import ThermalHistory
from .trackLength import TrackLength
from .user import User
from .vitrinite import Vitrinite
from .lcountry import LCountry
from .lGeochemEvent import LGeochemEvent
from .lLithologyKind import LLithologyKind
from .lMachineType import LMachineType
from .lMineral import LMineral
from .lPerson2DataRole import LPerson2DataRole
from .lPerson2SampleRole import LPerson2SampleRole
from .lSampleMethod import LSampleMethod
from .lSampleType import LSampleType
from .lSpecimenKind import LSpecimenKind
from .lStatementKind import LStatementKind
from .lVerticalDatumKind import LVerticalDatumKind
from .lShrimp_age_average_kind import LSHRIMPAgeAverageKinds
from .lShrimp_age_kind_process import LSHRIMPAgeKindProcesses
from .archive import Archive
from .rockunit import RockUnit
from .lab2data import Lab2Data
from .lit2data import Lit2Data
from .lit2sample import Lit2Sample
from .person import Person
from .person2data import Person2Data
from .SHRIMPAge import SHRIMPAge, SHRIMPAgeCRUD
from .SHRIMPDataPoint import SHRIMPDataPoint, SHRIMPDataPointCRUD
from .SHRIMPSpot import SHRIMPSpot, SHRIMPSpotCRUD
from .utilities import generate_code
from .user import User