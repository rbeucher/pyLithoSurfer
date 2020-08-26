from pytest import fixture
from pyLithoSurferAPI import Literature
from pyLithoSurferAPI import SHRIMPDataPoint
import pandas as pd

#@fixture
def literature_keys():
    # Responsible only for returning the test data
    return ["abstr", "author", "booktitle", "chapter", "doi",
            "editor", "howpublished", "id", "institution",
            "journal", "keywords", "language", "month",
            "note", "number", "organization", "otherId",
            "pages", "publisher", "school", "series", "title",
            "type", "volume", "year"]


def literature_example():
    return {'id': 625501,
            'author': 'Mike T',
            'title': 'title test',
            'year': 2020,
            'number': '1',
            'journal': 'test',
            'volume': '1',
            'pages': 200,
            'publisher': 'test',
            'doi': 'test',
            'month': 1,
            'institution': 'lab inc',
            'type': 'A',
            'note': 'test',
            'school': 'test',
            'booktitle': 'test',
            'editor': 'test',
            'keywords': 'test',
            'abstr': 'test',
            'language': 'English',
            'series': '1',
            'chapter': '10',
            'howpublished': 'test',
            'organization': 'lab inc.',
            'otherId': None}


def shrimp_keys():
    # Responsible only for returning the test data
    return ['id', 'ngrains', 'nspots', 'age', 'ageErrorMin', 'ageErrorMax',
       'ageAverageKindId', 'ageAverageKindName', 'mineralId', 'mineralName',
       'errorAgeTypeId', 'errorAgeTypeName', 'analyteId', 'analyteName',
       'mountId']

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
            'mountId': None}


def test_literature_get_all():
    """ Test API Call to get all literatures entries """

    data = Literature.get_all()
    assert isinstance(data, pd.DataFrame)
    assert set(literature_keys()).issubset(list(data.columns))
    assert len(data) > 20

def test_literature_create():
    literature_instance = Literature(**literature_example())
    response = literature_instance.new()
    assert isinstance(response, dict)
    assert set(literature_keys()).issubset(list(response.keys())), "All keys should be in the response"

def test_literature_to_json():
    literature_instance = Literature(**literature_example())
    value = literature_instance.to_json()

def test_literature_to_dict():
    literature_instance = Literature(**literature_example())
    value = literature_instance.to_dict()
    assert isinstance(value, dict)

def test_literature_update():
    literature_instance = Literature(**literature_example())
    literature_instance.author = "Bob Dylan"
    response = literature_instance.update()
    assert isinstance(response, dict)
    assert response["id"] == 625501
    assert response["author"] == "Bob Dylan"

def test_literature_create():
    literature_instance = Literature(**literature_example())
    response = literature_instance.new()
    assert isinstance(response, dict)
    assert "id" in response.keys()
    assert set(literature_keys()).issubset(list(response.keys())), "All keys should be in the response"

def test_delete_entry():
    literature_instance = Literature(**literature_example())
    response = literature_instance.new()
    response = literature_instance.delete()
    assert isinstance(response, dict)

### Test SHRIMP 

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