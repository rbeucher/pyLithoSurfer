from pytest import fixture
from pyLithoSurferAPI import Literature
import pandas as pd

#@fixture
def literature_keys():
    # Responsible only for returning the test data
    return  ['id', 'calcName', 'sourceId', 'author', 'title', 'pubYear', 'litNumber',
       'journal', 'volume', 'pages', 'publisher', 'doi', 'pubMonth',
       'institution', 'litType', 'note', 'school', 'booktitle', 'editor',
       'keywords', 'abstr', 'language', 'series', 'chapter', 'howpublished',
       'litOrganization', 'otherId', 'issn', 'url']


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