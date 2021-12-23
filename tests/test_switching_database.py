

def test_select_test_db():
    from pyLithoSurferAPI import select_database
    from pyLithoSurferAPI.REST import APIRequests
    assert(select_database("test") == "test")
    assert(APIRequests.URL_BASE == 'http://testapp.lithodat.com')

def test_select_dev_db():
    from pyLithoSurferAPI import select_database
    from pyLithoSurferAPI.REST import APIRequests
    assert(select_database("development") == "development")
    assert(APIRequests.URL_BASE == 'http://devapp.lithodat.com')

def test_select_prod_db():
    from pyLithoSurferAPI import select_database
    from pyLithoSurferAPI.REST import APIRequests
    assert(select_database("production") == "production")
    assert(APIRequests.URL_BASE == 'http://app.lithodat.com')

def test_get_auth_token():
    import os
    from pyLithoSurferAPI import _get_token
    url_base = 'http://testapp.lithodat.com'
    LITHODAT_USERNAME = os.environ.get("LITHODAT_TEST_USERNAME", None)
    LITHODAT_PASSWORD = os.environ.get("LITHODAT_TEST_PASSWORD", None)
    request = _get_token(LITHODAT_USERNAME, LITHODAT_PASSWORD)
    assert(request.status_code == 200)