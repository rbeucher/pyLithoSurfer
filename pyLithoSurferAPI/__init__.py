import os
import requests

DB_MODE = "PROD"
URL_BASE = None
LITHODAT_USERNAME = None
LITHODAT_PASSWORD = None

def set_credentials(DB_MODE="PROD"):
    global URL_BASE
    global LITHODAT_PASSWORD
    global LITHODAT_USERNAME

    if DB_MODE == "PROD":
        URL_BASE = 'https://app.ausgeochem.com.au'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_PROD_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_PROD_PASSWORD", None)
        print("You are now using PRODUCTION")
    elif DB_MODE == "TEST":
        URL_BASE = 'https://testapp.lithodat.com'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_TEST_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_TEST_PASSWORD", None)
        print("You are now using TEST")
    else:
        raise ValueError("DB_MODE is incorrect")


set_credentials(DB_MODE)

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
from .lErrorType import LErrorType
from .lithoRequest import LithoRequest
from .lithoUser import LithoUser
from .lLab import LLab
from .lLocationCapture import LLocationCapture
from .lLocationKind import LLocationKind
from .lLocPredefined import LLocPredefined
from .location import Location
from .locationProperty import LocationProperty
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
from .lGeoEvent import LGeoEvent
from .lLithologyKind import LLithologyKind
from .lMachineType import LMachineType
from .lSampleMethod import LSampleMethod
from .lStatementKind import LStatementKind
from .lVerticalDatumKind import LVerticalDatumKind
from .archive import Archive
from .stratigraphicUnit import StratigraphicUnit
from .lab2data import Lab2Data
from .lit2data import Lit2Data
from .lit2sample import Lit2Sample
from .person import Person
from .person2data import Person2Data
from .person2sample import Person2Sample
from .SHRIMPAge import SHRIMPAge, SHRIMPAgeCRUD
from .SHRIMPDataPoint import SHRIMPDataPoint, SHRIMPDataPointCRUD
from .SHRIMPSpot import SHRIMPSpot, SHRIMPSpotCRUD
from .utilities import generate_code
from .user import User
from .statement import Statement
from .geoeventAtAge import GeoeventAtAge

from .lCelestial import LCelestial
from .lElevationKind import LElevationKind
from .lMachine2DataPointRole import LMachine2DataPointRole
from .lPerson2DataPointRole import LPerson2DataPointRole
from .lPerson2SampleRole import LPerson2SampleRole
from .lPerson2SampleRole import LPerson2SampleRole
from .lSampleKind import LSampleKind
from .lSHRIMPAgeGroup import LSHRIMPAgeGroup
from .lSHRIMPAgeType import LSHRIMPAgeType
from .lSHRIMPSampleFormat import LSHRIMPSampleFormat
from .flag import Flag
from .funding import Funding
from .fundingBody import FundingBody
from .sample import SampleWithLocation
from .referenceMaterial import ReferenceMaterial
