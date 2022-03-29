import os
import requests

def _get_token(username: str, password: str, remember_me=False, url_base="http://testapp.lithodat.com"):
    url = url_base + '/api/authenticate'
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    data = {'username': username,
            'password': password,
            'rememberMe': remember_me}

    return requests.post(url, json=data, headers=headers)

def select_database(database="test"):

    if database == "production":

        url_base = 'http://app.lithodat.com'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_PROD_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_PROD_PASSWORD", None)
        selected_db="production"
    
    elif database == "test":
    
        url_base = 'http://testapp.lithodat.com'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_TEST_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_TEST_PASSWORD", None)
        selected_db="test"
    
    elif database == "development":
    
        url_base = 'http://devapp.lithodat.com'
        LITHODAT_USERNAME = os.environ.get("LITHODAT_DEV_USERNAME", None)
        LITHODAT_PASSWORD = os.environ.get("LITHODAT_DEV_PASSWORD", None)
        selected_db="development"
    
    LITHOSURFER_API_KEY = _get_token(username=LITHODAT_USERNAME,
                                     password=LITHODAT_PASSWORD,
                                     url_base=url_base).json()['id_token']

    session = requests.Session()
    session.headers = {'Accept': 'application/json',
                       'Content-Type': 'application/json'}
    session.headers["Authorization"] = f"Bearer {LITHOSURFER_API_KEY}"

    from .REST import APIRequests

    APIRequests.URL_BASE = url_base
    APIRequests.SESSION = session

    return selected_db

select_database()