import os
import requests

def _get_token(username: str, password: str, remember_me=False, url_base="http://testapp.lithodat.com"):
    url = url_base + '/api/authenticate'
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    data = {'username': username,
            'password': password,
            'rememberMe': remember_me}

    return requests.post(url, json=data, headers=headers).json()['id_token']

def select_database(database="test"):

    if database == "production":

        url_base = 'http://app.ausgeochem.com.au'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_PROD_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_PROD_PASSWORD", None)
        print("You are now using Production")
    
    elif database == "test":
    
        url_base = 'http://testapp.lithodat.com'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_TEST_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_TEST_PASSWORD", None)
        print("You are now using Test")
    
    elif database == "development":
    
        url_base = 'http://devapp.lithodat.com'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_DEV_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_DEV_PASSWORD", None)
        print("You are now using Development")
    
    LITHOSURFER_API_KEY = _get_token(username=LITHODAT_USERNAME,
                                     password=LITHODAT_PASSWORD,
                                     url_base=url_base)

    session = requests.Session()
    session.headers = {'Accept': 'application/json',
                       'Content-Type': 'application/json'}
    session.headers["Authorization"] = f"Bearer {LITHOSURFER_API_KEY}"

    from .REST import APIRequests

    APIRequests.URL_BASE = url_base
    APIRequests.SESSION = session

    return

select_database()