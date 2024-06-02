from pyLithoSurferAPI.uploader import Uploader
from pyLithoSurferAPI.core.tables import (Literature, Location, Material, Archive, StratigraphicUnit, Sample, SampleWithLocation, Person)
from pyLithoSurferAPI.core.lists import LSampleMethod, LSampleKind, LLocationKind, LElevationKind, LCelestial 
from pyLithoSurferAPI.core.schemas import LiteratureSchema, LocationSchema, SampleSchema, PersonSchema, StratigraphicUnitSchema
from pyLithoSurferAPI.management.tables import DataPackage
import pandas as pd
from tqdm import tqdm
import os


class SampleWithLocationUploader(Uploader):

    name = "Sample"

    def __init__(self, locations_df, samples_df, locations_skip=None, samples_skip=None):
        self.locations_df = locations_df
        self.samples_df = samples_df
        self.validated = False
        self.locations_out = pd.DataFrame(columns=self.locations_df.columns)
        self.samples_out = pd.DataFrame(columns=self.samples_df.columns)
        self.locations_skip = locations_skip
        self.samples_skip = samples_skip

    def validate(self, lazy=True):

        sample_lists = {
            "dataPackage": DataPackage,
            "archive": Archive,
            "material": Material,
            "sampleMethod": LSampleMethod,
            "sampleKind" : LSampleKind,
            "locationKind": LLocationKind,
            "referenceElevationKind": LElevationKind,
            "stratographicUnit": StratigraphicUnit,
            }

        location_lists = {
            "celestial": LCelestial
        }
        if self.locations_skip:
            skip_df = self.locations_df[[col for col in self.locations_skip if col in self.locations_df.columns]]
            self.locations_df = self.locations_df.drop(columns=[col for col in self.locations_skip if col in self.locations_df.columns])
        self.locations_df = Uploader._validate(self.locations_df, LocationSchema, location_lists, lazy=lazy)
        
        if self.locations_skip:
            for col in self.locations_skip:
                self.locations_df[col] = skip_df[col]

        if self.samples_skip:
            skip_df = self.samples_df[[col for col in self.samples_skip if col in self.samples_df.columns]]
            self.samples_df = self.samples_df.drop(columns=[col for col in self.samples_skip if col in self.samples_df.columns])
        self.samples_df = Uploader._validate(self.samples_df, SampleSchema, sample_lists, lazy=lazy)
        if self.samples_skip:
            for col in self.samples_skip:
                self.samples_df[col] = skip_df[col]

        self.validated = True

    def get_unique_query(self, samp_args, loc_args):
            
        name = samp_args.get("name") 
        igsn = samp_args.get("igsn", None)
        dataPackageId = samp_args.get("dataPackageId")
        
        query = {"dataPackageId.equals": dataPackageId,
                 "name.equals": name}

        if igsn:
            query = {"dataPackageId.equals": dataPackageId,
                     "name.equals": name,
                     "igsn.equals": igsn}

        return SampleWithLocation.query(query)

    def upload(self, update=False, update_strategy="merge_keep", auto_set_elevation = False):

        if not self.validated:
            raise ValueError("Data not validated")

        self.samples_df["locationId"] = None
        self.samples_df["id"] = None
        self.locations_df["id"] = None

        for index in tqdm(self.samples_df.index):

            loc_args = self.locations_df.loc[index].to_dict()
            samp_args = self.samples_df.loc[index].to_dict()

            loc_skip_args = {}
            for k, v in loc_args.items():
                if self.locations_skip and k in self.locations_skip:
                    loc_skip_args[k] = loc_args[k]
            loc_args = {k:v for k,v in loc_args.items() if k not in loc_skip_args.keys()}
            
            samp_skip_args = {}
            for k, v in samp_args.items():
                if self.samples_skip and k in self.samples_skip:
                    samp_skip_args[k] = samp_args[k]

            samp_args = {k:v for k,v in samp_args.items() if k not in samp_skip_args.keys()}

            loc_args = {k:v for k,v in loc_args.items() if v is not None}
            samp_args = {k:v for k,v in samp_args.items() if v is not None}
            
            loc_args["id"] = None
            samp_args["id"] = None
            
            response = self.get_unique_query(samp_args, loc_args)
            records = response.json() 

            sample_with_location_id = None
            
            if len(records) == 1:
                sample_with_location_id = records[0]["id"]
               
            if sample_with_location_id is None: 
               
                SampWLocation = SampleWithLocation(Location(**loc_args), Sample(**samp_args), auto_set_elevation)
                SampWLocation.new()

            elif update:

                old_loc_args = records[0]["locationDTO"]
                loc_args = self._update_args(old_loc_args, loc_args, update_strategy)
                old_samp_args = records[0]["sampleDTO"]
                samp_args = self._update_args(old_samp_args, samp_args, update_strategy)

                location = Location(**loc_args)
                sample = Sample(**samp_args)    
                sample.locationId = location.id

                SampWLocation = SampleWithLocation(location=location, sample=sample, auto_set_elevation=auto_set_elevation)
                SampWLocation.id = sample_with_location_id
                SampWLocation.update()

            index = SampWLocation.location.id
            self.locations_out.loc[index] = {k:v for k,v in loc_args.items() if v is not None}
            self.locations_out.loc[index, "id"] = SampWLocation.location.id
            for k, v in loc_skip_args.items():
                self.locations_out.loc[index, k] = v

            index = SampWLocation.sample.id
            self.samples_out.loc[index] = {k:v for k,v in samp_args.items() if v is not None}
            self.samples_out.loc[index, "id"] = SampWLocation.sample.id
            self.samples_out.loc[index, "locationId"] = SampWLocation.location.id
            for k, v in samp_skip_args.items():
                self.samples_out.loc[index, k] = v

    def save(self, outfile="output.xlsx"):

        kwargs = {}
        if os.path.isfile(outfile):
            kwargs["mode"] = "a"
            kwargs["if_sheet_exists"] = "replace"
        else:
            kwargs["mode"] = "w"

        with pd.ExcelWriter(outfile, **kwargs) as writer:  
            self.samples_out.to_excel(writer, sheet_name='Samples')
            self.locations_out.to_excel(writer, sheet_name='Locations')


class PersonUploader(Person, Uploader):

    name = "Persons"

    def __init__(self, persons_df):
        Uploader.__init__(self, persons_df)

    def get_unique_query(self, args):
        
        query = {"name.equals": args["name"],
                 "firstName.equals": args["firstName"]}
        return super().query(query)

    def validate(self, lazy=False):

        self.dataframe = Uploader._validate(self.dataframe, PersonSchema, lazy=lazy)
        self.validated = True
        return
        
    def upload(self, update=False, update_strategy="merge_keep"):
        
        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            args = self.dataframe.loc[index].to_dict()
            response = self.get_unique_query(args)
            records = response.json()

            if len(records) == 1:
                existing_id = records[0]["id"]
                old_args =  {k:v for k,v in records[0].items() if v is not None}
            else:
                existing_id = None

            if existing_id is None:
                obj = Person(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = Person(**args) 
                obj.update()

            index = obj.id
            self.dataframe_out.loc[index] = args
            self.dataframe_out.loc[index, "id"] = obj.id


class StratigraphicUnitUploader(StratigraphicUnit, Uploader):

    name = "StratigraphicUnit"
    
    def __init__(self, stratigraphic_df):
        
        Uploader.__init__(self, stratigraphic_df)

    def get_unique_query(self, args):
        query = {"name.equals": args.get("name", None)}
        return super().query(query)

    def validate(self, lazy=False):
        self.dataframe = Uploader._validate(self.dataframe, StratigraphicUnitSchema, lazy=lazy)
        self.validated = True
        return

    def upload(self, update=False, update_strategy="merge_keep"):
        
        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            args = self.dataframe.loc[index].to_dict()
            response = self.get_unique_query(args)
            records = response.json()

            if len(records) == 1:
                existing_id = records[0]["id"]
                old_args =  {k:v for k,v in records[0].items() if v is not None}
            else:
                existing_id = None

            if existing_id is None:
                obj = StratigraphicUnit(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = StratigraphicUnit(**args) 
                obj.update()
                
            index = obj.id
            self.dataframe_out.loc[index] = args
            self.dataframe_out.loc[index, "id"] = obj.id


class LiteratureUploader(Literature, Uploader):

    name = "Literature"

    def __init__(self, literature_df):

        Uploader.__init__(self, literature_df)

    def get_unique_query(self, args):
        
        query = {"title.equals": args["title"],
                 "pubYear.equals": args["pubYear"]}
        return super().query(query)
    
    def validate(self, lazy=False):

        self.dataframe = Uploader._validate(self.dataframe, LiteratureSchema, lazy=lazy)
        self.validated = True

    def upload(self, update=False, update_strategy="merge_keep"):
        
        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            args = self.dataframe.loc[index].to_dict()
            response = self.get_unique_query(args)
            records = response.json()

            if ("pubYear" in args.keys()) and args["pubYear"]:
                args["pubYear"] = int(args["pubYear"])

            if len(records) == 1:
                existing_id = records[0]["id"]
                old_args =  {k:v for k,v in records[0].items() if v is not None}
            else:
                existing_id = None

            if existing_id is None:
                obj = Literature(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = Literature(**args) 
                obj.update()

            index = obj.id            
            self.dataframe_out.loc[index] = {k:v for k,v in args.items() if v is not None}
            self.dataframe_out.loc[index, "id"] = obj.id