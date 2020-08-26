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