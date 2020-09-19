from pytest import fixture
from pyLithoSurferAPI import SHRIMPDataPoint
import pandas as pd


def shrimp_keys():
    # Responsible only for returning the test data
    return ['id', 'ngrains', 'nspots', 'age', 'ageErrorMin', 'ageErrorMax',
       'mountCoating', 'mountOpticalCharacterisation', 'ageAverageKindId',
       'ageAverageKindName', 'mineralId', 'mineralName', 'errorAgeTypeId',
       'errorAgeTypeName', 'analyteId', 'analyteName']

def shrimp_example():
    return {'id': 638451,
            'ngrains': None,
            'nspots': None,
            'age': 100,
            'ageErrorMin': 45,
            'ageErrorMax': 23,
            'ageAverageKindId': None,
            'ageAverageKindName': None,
            'mineralId': None,
            'mineralName': None,
            'errorAgeTypeId': None,
            'errorAgeTypeName': None,
            'analyteId': None,
            'analyteName': None,
            'issn': None,
            'url': None,
            'mountId': None}

def test_shrimp_data_get_all():
    data = SHRIMPDataPoint.get_all()
    assert isinstance(data, pd.DataFrame)

def test_shrimp_data_id():
    shrimp_instance = SHRIMPDataPoint()
    data = shrimp_instance.get_from_id(638451)
    assert isinstance(data, dict)

def test_shrimp_data_create():
    shrimp_instance = SHRIMPDataPoint(**shrimp_example())
    response = shrimp_instance.new()
    assert isinstance(response, dict)
    assert "id" in response.keys()
    assert set(shrimp_keys()).issubset(list(response.keys())), "All keys should be in the response"

def test_shrimp_data_update():
    shrimp_instance = SHRIMPDataPoint(**shrimp_example())
    shrimp_instance.ngrains = 20
    response = shrimp_instance.update()
    print(shrimp_instance.id)
    assert isinstance(response, dict)
    assert response["id"] == 638451
    assert response["ngrains"] == 20
    
def test_shrimp_data_delete_entry():
    shrimp_instance = SHRIMPDataPoint(**shrimp_example())
    response = shrimp_instance.new()
    response = shrimp_instance.delete()
    assert isinstance(response, dict)