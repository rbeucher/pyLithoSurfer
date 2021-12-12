import os
import requests

DB_MODE = "DEV"
URL_BASE = None
LITHODAT_USERNAME = None
LITHODAT_PASSWORD = None

def set_credentials(DB_MODE="PROD"):
    global URL_BASE
    global LITHODAT_PASSWORD
    global LITHODAT_USERNAME

    if DB_MODE == "PROD":
        URL_BASE = 'http://app.ausgeochem.com.au'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_PROD_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_PROD_PASSWORD", None)
        print("You are now using PRODUCTION")
    elif DB_MODE == "TEST":
        URL_BASE = 'http://testapp.lithodat.com'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_TEST_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_TEST_PASSWORD", None)
        print("You are now using TEST")
    elif DB_MODE == "DEV":
        URL_BASE = 'http://devapp.lithodat.com'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_DEV_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_DEV_PASSWORD", None)
        print("You are now using DEV")
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
session.headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}
session.headers["Authorization"] = f"Bearer {LITHOSURFER_API_KEY}"