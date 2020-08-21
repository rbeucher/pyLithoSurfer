from . import session, URL_BASE
import json


class Literature(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = int(value)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        self._author = value

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        assert isinstance(value, int)
        self._year = value

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, value):
        assert isinstance(value, str)
        self._number = value

    @property
    def journal(self):
        return self._journal
    
    @journal.setter
    def journal(self, value):
        assert isinstance(value, str)
        self._journal = value

    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self, value):
        assert isinstance(value, str)
        self._volume = value

    @property
    def publisher(self):
        return self._publisher
    
    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def doi(self):
        return self._doi
    
    @doi.setter
    def doi(self, value):
        self._doi = value

    @property
    def month(self):
        return self._month
    
    @month.setter
    def month(self, value):
        self._month = value

    @property
    def institution(self):
        return self._institution
    
    @institution.setter
    def institution(self, value):
        self._institution = value

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, value):
        self._type = value

    @property
    def note(self):
        return self._note
    
    @note.setter
    def note(self, value):
        self._note = value

    @property
    def school(self):
        return self._school
    
    @school.setter
    def school(self, value):
        self._school = value

    @property
    def booktitle(self):
        return self._booktitle
    
    @booktitle.setter
    def booktitle(self, value):
        self._booktitle = value

    @property
    def editor(self):
        return self._editor
    
    @editor.setter
    def editor(self, value):
        self._editor = value

    @property
    def keywords(self):
        return self._keywords
    
    @keywords.setter
    def keywords(self, value):
        self._keywords = value

    @property
    def abstr(self):
        return self._abstr
    
    @abstr.setter
    def abstr(self, value):
        self._abstr = value

    @property
    def language(self):
        return self._language
    
    @language.setter
    def language(self, value):
        self._language = value

    @property
    def series(self):
        return self._series
    
    @series.setter
    def series(self, value):
        self._series = value

    @property
    def chapter(self):
        return self._chapter
    
    @chapter.setter
    def chapter(self, value):
        self._chapter = value

    @property
    def howpublished(self):
        return self._howpublished
    
    @howpublished.setter
    def howpublished(self, value):
        self._howpublished = value

    @property
    def organization(self):
        return self._organization
    
    @organization.setter
    def organization(self, value):
        self._organization = value

    @property
    def otherId(self):
        return self._otherId
    
    @otherId.setter
    def otherId(self, value):
        self._otherId = value
    
    @property
    def pages(self):
        return self._pages
    
    @pages.setter
    def pages(self, value):
        self._pages = value

    def info(self):
        if self.id:
            path = URL_BASE+'/api/literature/' + str(self.id)
            response = session.get(path)
            if response.status_code == 200:
                return response.json()

    def get_from_id(self, id_value):
        path = URL_BASE+'/api/literature/' + str(id_value)
        response = session.get(path)

        if response.status_code == 200:
            data = response.json()
            self.__init__(**data)
        return response.json()

    def get_from_doi(self, doi):
        import requests
        response = requests.get('https://api.crossref.org/works/' + str(doi), 
                                headers={'Accept': 'application/json'})
        if response.status_code == 200:
            data = response.json()["message"]
            return data
        return response.json()

    def push_new_entry(self):
        path = URL_BASE+'/api/literature/'
        data = self.to_dict()
        data.pop("id")
        response = session.post(path, data=json.dumps(data))
        if response.status_code == 200:
            id_value = response.json()["id"]
            print(f"Literature Entry with id={id_value} has been successfully created")
        else:
            print("Could not create Entry")
        return response.json()

    def update_entry(self):
        path = URL_BASE+'/api/literature/'
        response = session.put(path, data=self.to_json())
        if response.status_code == 200:
            id_value = response.json()["id"]
            print(f"Literature Entry with id={id_value} has been successfully updated")
        else:
            print("Could not update Entry")
        return response.json()

    def delete_entry(self):
        path = URL_BASE+'/api/literature/' + str(self.id)
        response = session.delete(path)
        if response.status_code == 200:
            print(f"Literature Entry with id={self.id} has been deleted")
        if response.status_code == 500:
            print("Cannot find Literature Entry with id={id_value}")
        return response.json()

    def to_json(self):
        return json.dumps(self, default=lambda o: {key.replace("_", ""): val for key, val in o.__dict__.items()}, 
            sort_keys=True) 

    def to_dict(self):
        return {key.replace("_", ""): val for key, val in self.__dict__.items()}