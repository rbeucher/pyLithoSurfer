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

from .basket import basket
from .chrono import chrono
from .chronoProperty import chronoProperty
from .community import community
from .dataPackage import dataPackage
from .dataPoint import dataPoint
from .datapointProperty import datapointProperty
from .entry import entry
from .entryProperty import entryProperty
from .fissionTrack import fissionTrack
from .gradientAndTemp import gradientAndTemp
from .helium import helium
from .institution import institution
from .kArgon import kArgon
from .lChrAgeKind import lChrAgeKind
from .lChrAgeKindProcess import lChrAgeKindProcess
from .lChrAnalyticalKind import lChrAnalyticalKind
from .lChrAnalyticalMethod import lChrAnalyticalMethod
from .lChrAnalyticalSystem import lChrAnalyticalSystem
from .lChrAvgKind import lChrAvgKind
from .lChrMineral import lChrMineral
from .lChrTectEnv import lChrTectEnv
from .lChrThMod import lChrThMod
from .lErrorType import lErrorType
from .lithoRequest import lithoRequest
from .lithoUser import lithoUser
from .lLab import lLab
from .lLithologyType import lLithologyType
from .lLocCapture import lLocCapture
from .lLocKind import lLocKind
from .lLocPredefined import lLocPredefined
from .location import location
from .locationProperty import locationProperty
from .lSampleType import lSampleType
from .lThermDiffusion import lThermDiffusion
from .lThermDosimeter import lThermDosimeter
from .lThermEtch import lThermEtch
from .lVerticalDatum import lVerticalDatum
from .rbSr import rbSr
from .reOs import reOs
from .sample import sample
from .singleGrain import singleGrain
from .singleGrainHe import singleGrainHe
from .smNd import smNd
from .thermalHistory import thermalHistory
from .trackLength import trackLength
from .user import user
from .vitrinite import vitrinite
