from pyLithoSurferAPI.uploader import Uploader
from pyLithoSurferAPI.core.tables import (Location, Material, Archive, StratigraphicUnit, Sample, SampleWithLocation, Person)
from pyLithoSurferAPI.core.lists import LSampleMethod, LSampleKind, LLocationKind, LElevationKind, LCelestial 
from pyLithoSurferAPI.core.lists import get_list_name_to_id_mapping as get_id
from pyLithoSurferAPI.core.schemas import LocationSchema, SampleSchema, PersonSchema, StratigraphicUnitSchema
from pyLithoSurferAPI.management.tables import DataPackage
from pyLithoSurferAPI.utilities import get_elevation_from_google
import pandas as pd
import numpy as np
from tqdm import tqdm
import os


class SampleWithLocationUploader(Uploader):

    name = "Sample"

    def __init__(self, datapackageId, locations_df, samples_df):
        self.datapackageId = datapackageId
        self.locations_df = locations_df
        self.samples_df = samples_df
        self.samples_df["dataPackageId"] = datapackageId
        self.validated = False

    def validate(self):

        sample_lists = {
            "dataPackage": DataPackage,
            "archive": Archive,
            "material": Material,
            "sampleMethod": LSampleMethod,
            "sampleKind" : LSampleKind,
            "locationKind": LLocationKind,
            "referenceElevationKind": LElevationKind,
            }

        location_lists = {
            "celestial": LCelestial
        }

        self.locations_df = Uploader._validate(self.locations_df, LocationSchema, sample_lists)
        self.samples_df = Uploader._validate(self.samples_df, SampleSchema, location_lists)
        self.validated = True

    def get_unique_query(self, samp_args, loc_args):
            
        name = samp_args.get("name") 
        igsn = samp_args.get("igsn", None) 
        
        query = {"dataPackageId.equals": self.datapackageId,
                 "name.equals": name}

        if igsn:
            query = {"dataPackageId.equals": self.datapackageId,
                     "igsn.equals": igsn}

        return query

    def upload(self, update=False, update_strategy="merge_keep"):

        if not self.validated:
            raise ValueError("Data not validated")

        self.samples_df["locationId"] = None
        self.samples_df["id"] = None
        self.locations_df["id"] = None

        for index in tqdm(self.samples_df.index):

            loc_args = self.locations_df.loc[index].to_dict()
            samp_args = self.samples_df.loc[index].to_dict()
            loc_args = {k:v for k,v in loc_args.items() if v is not None}
            samp_args = {k:v for k,v in samp_args.items() if v is not None}
            
            loc_args["id"] = None
            samp_args["id"] = None
            
            response = SampleWithLocation.query(self.get_unique_query(samp_args, loc_args))
            records = response.json() 

            sample_with_location_id = None
            
            if len(records) == 1:
                sample_with_location_id = records[0]["id"]
               
            if sample_with_location_id is None: 
               
                SampWLocation = SampleWithLocation(Location(**loc_args), Sample(**samp_args))
                SampWLocation.new()

            elif update:

                old_loc_args = records[0]["locationDTO"]
                loc_args = self._update_args(old_loc_args, loc_args, update_strategy)
                old_samp_args = records[0]["sampleDTO"]
                samp_args = self._update_args(old_samp_args, samp_args, update_strategy)

                location = Location(**loc_args)
                sample = Sample(**samp_args)    
                sample.locationId = location.id

                SampWLocation = SampleWithLocation(location=location, sample=sample)
                SampWLocation.id = sample_with_location_id
                SampWLocation.update()

            self.locations_df.loc[index, "id"] = SampWLocation.location.id
            self.samples_df.loc[index, "id"] = SampWLocation.sample.id
            self.samples_df.loc[index, "locationId"] = SampWLocation.location.id

    def save(self, outfile="output.xlsx"):

        if os.path.isfile("output.xlsx"):
            mode = "a"
        else:
            mode = "w"

        with pd.ExcelWriter('output.xlsx', mode=mode) as writer:  
            self.samples_df.to_excel(writer, sheet_name='Samples')
            self.locations_df.to_excel(writer, sheet_name='Locations')


class PersonUploader(Uploader):

    name = "Persons"

    def __init__(self, persons_df):
        self.dataframe = persons_df

    def get_unique_query(self, args):
        
        query = {"name.equals": args["name"],
                 "firstName.equals": args["firstName"]}
        return query


class StratigraphicUnitUploader(Uploader):
    
    def __init__(self, stratigraphic_df):
        
        self.dataframe = stratigraphic_df
        self.validated = False

    def get_unique_query(self, args):
        query = {"name.equals": args.get("name", None)}
        return query

    def validate(self):
        Uploader.validate(self.dataframe, StratigraphicUnitSchema)
        self.validated = True
        return