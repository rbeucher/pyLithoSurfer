from pyLithoSurferAPI.core.tables import Location
from pyLithoSurferAPI.core.tables import Material
from pyLithoSurferAPI.core.sample import Sample
from pyLithoSurferAPI.core.sample import SampleWithLocation
from pyLithoSurferAPI.core.lists import LSampleMethod, LSampleKind, LLocationKind, LElevationKind, LCelestial 
from pyLithoSurferAPI.core.schemas import LocationSchema, SampleSchema, PersonSchema
from pyLithoSurferAPI.core.lists import get_list_name_to_id_mapping as get_id
from pyLithoSurferAPI.utilities import get_elevation_from_google
import pandas as pd
import numpy as np
from tqdm import tqdm
import os


class SampleWithLocationUploader(object):

    def __init__(self, datapackageId, locations_df, samples_df):
        self.datapackageId = datapackageId
        self.locations_df = locations_df
        self.samples_df = samples_df
        self.validated = False

    def validate(self):

        # Validate Samples
        self.samples_df = SampleSchema.validate(self.samples_df)
        
        if "materialId" not in self.samples_df.columns:
            if "materialName" in self.samples_df.columns:
                materials = self.samples_df.materialName.unique()
                mapping = {}
                for material in materials:
                    mapping[material] = Material.get_id_from_name(material)
                self.samples_df["materialId"] = self.samples_df.materialName.map(mapping)
            #else:
            #    self.samples_df["materialId"] = Material.get_id_from_name("Unknown")
            #    self.samples_df["materialName"] = "Unknown"
        
        if "sampleMethodId" not in self.samples_df.columns:
            if "sampleMethodName" in self.samples_df.columns:
                self.samples_df["sampleMethodId"] = self.samples_df.sampleMethodName.map(get_id(LSampleMethod))
            else:
                self.samples_df["sampleMethodId"] = LSampleMethod.get_id_from_name("Unknown")
                self.samples_df["sampleMethodName"] = "Unknown"

        if "sampleKindId" not in self.samples_df.columns:
            if "sampleKindName" in self.samples_df.columns:
                self.samples_df["sampleKindId"] = self.samples_df.sampleKindName.map(get_id(LSampleKind))
            else:
                self.samples_df["sampleKindId"] = LSampleKind.get_id_from_name("Unknown")
                self.samples_df["sampleKindName"] = "Unknown"
        
        if "locationKindId" not in self.samples_df.columns:
            if "locationKindName" in self.samples_df.columns:
                self.samples_df["locationKindId"] = self.samples_df.locationKindName.map(get_id(LLocationKind))
            else:
                self.samples_df["locationKindId"] = LLocationKind.get_id_from_name("Unknown")
                self.samples_df["locationKindName"] = "Unknown"
        
        if "referenceElevationKindId" not in self.samples_df.columns:
            if "referenceElevationKindName" in self.samples_df.columns:
                self.samples_df["referenceElevationKindId"] = self.samples_df.referenceElevationKindName.map(get_id(LElevationKind))
            else:
                self.samples_df["referenceElevationKindId"] = LElevationKind.get_id_from_name("Unknown")
                self.samples_df["referenceElevationKindName"] = "Unknown"
        
        self.samples_df["dataPackageId"] = self.datapackageId
        self.samples_df = self.samples_df.replace({np.nan: None})
        self.samples_df = SampleSchema.validate(self.samples_df)
        self.samples_df = self.samples_df.replace({np.nan: None})
        
        # Validate Location
        self.locations_df = LocationSchema.validate(self.locations_df)

        if "celestialId" not in self.locations_df.columns:
            if "celestialName" in self.locations_df.columns:
                self.locations_df["celestialId"] = self.locations_df.celestialName.map(get_id(LCelestial))
            else:
                self.locations_df["celestialId"] = LCelestial.get_id_from_name("Earth")
                self.locations_df["celestialName"] = "Earth"

        self.locations_df = self.locations_df.replace({np.nan: None})
        self.locations_df = LocationSchema.validate(self.locations_df)
        self.locations_df = self.locations_df.replace({np.nan: None})

        self.validated = True
        return

    def upload(self, update=False, update_strategy="merge_keep"):

        print("Upload Samples and Locations")

        if not self.validated:
            raise ValueError("Data not validated")

        self.samples_df["locationId"] = None
        self.samples_df["id"] = None
        self.locations_df["id"] = None
        self.errors_df = pd.DataFrame(columns=["sample.name", "exception"])

        for index in tqdm(self.samples_df.index):

            # Check for existing samples at location
            loc_args = self.locations_df.loc[index].to_dict()
            samp_args = self.samples_df.loc[index].to_dict()
            loc_args = {k:v for k,v in loc_args.items() if v is not None}
            samp_args = {k:v for k,v in samp_args.items() if v is not None}
            if "id" not in loc_args.keys():
                loc_args["id"] = None
            if "id" not in samp_args.keys():
                samp_args["id"] = None
            
            lat = loc_args.get("lat")
            lon = loc_args.get("lon")
            name = samp_args.get("name") 
            igsn = samp_args.get("igsn", None) 
            
            query = {"dataPackageId.equals": self.datapackageId,
                     "name.equals": name}

            response = SampleWithLocation.query(query)
            records = response.json() 

            if records:
                sample_with_location_id = records[0]["id"]
            else:
                sample_with_location_id = None

            if sample_with_location_id is None: 
               
                location = Location(**loc_args)
                sample = Sample(**samp_args)    
           
                try:
                    # Create SampleWithLocation object.
                    SampWLocation = SampleWithLocation(location=location, sample=sample)
                    SampWLocation.new()
                except Exception as e:
                    self.errors_df.loc[index] = [sample.name, str(type(e))]

            elif update:

                if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
                    raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")
                    
                old_loc_args = records[0]["locationDTO"]
                old_samp_args = records[0]["sampleDTO"]
                old_loc_args = {k:v for k,v in old_loc_args.items() if v is not None}
                old_samp_args = {k:v for k,v in old_samp_args.items() if v is not None}
                
                if update_strategy == "merge_keep":
                    loc_args.update(old_loc_args)
                    samp_args.update(old_samp_args)
                
                if update_strategy == "merge_replace":
                    old_loc_args.update(loc_args)
                    old_samp_args.update(samp_args)
                    samp_args = old_samp_args
                    loc_args = old_loc_args

                if update_strategy == "replace":
                    for key, val in old_loc_args.items():
                        if key not in loc_args.keys():
                            loc_args[key] = None
                    for key, val in old_samp_args.items():
                        if key not in samp_args.keys():
                            samp_args[key] = None                            

                loc_args["id"] = old_loc_args["id"]
                samp_args["id"] = old_samp_args["id"]

                # Create Location
                location = Location(**loc_args)
                # Create Sample
                sample = Sample(**samp_args)    
                sample.locationId = location.id

                try:
                    # Create SampleWithLocation
                    SampWLocation = SampleWithLocation(location=location, sample=sample)
                    SampWLocation.id = sample_with_location_id
                    SampWLocation.update()
                except Exception as e:
                    self.errors_df.loc[index] = [sample.name, str(type(e))]

            else:
                continue
           
            self.locations_df.loc[index, "id"] = SampWLocation.location.id
            self.samples_df.loc[index, "id"] = SampWLocation.sample.id
            self.samples_df.loc[index, "locationId"] = SampWLocation.location.id

        if os.path.isfile("output.xlsx"):
            mode = "a"
        else:
            mode = "w"

        with pd.ExcelWriter('output.xlsx', mode=mode) as writer:  
            self.samples_df.to_excel(writer, sheet_name='Samples')
            self.locations_df.to_excel(writer, sheet_name='Locations')
            self.errors_df.to_excel(writer, sheet_name="Errors")   


class PersonUploader(object):

    def __init__(self, persons_df):
        self.persons_df = persons_df

    def validate(self):
        self.persons_df = self.persons_df.dropna(how="any")
        self.persons_df = self.persons_df.drop_duplicates()
        self.persons_df = PersonSchema.validate(self.persons_df)
        return self.persons_df

    def upload(self, update=False, update_strategy="merge_keep"):
        from pyLithoSurferAPI.core.person import get_person_id, Person

        self.persons_df["id"] = None

        for index in tqdm(self.persons_df.index):

            row = self.persons_df.loc[index]
            args = row.to_dict()
            person_id = get_person_id(name=args["name"], firstName=args["firstName"])

            if (person_id is None):
                
                person = Person(**args)
                person.new() 
                person_id = person.id

            elif update:

                if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
                    raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")
                    
                query = {"id.equals": person_id}
                response = Person.query(query)

                if update_strategy == "merge_keep":
                    old_args = response.json()[0]
                    args.update(old_args)
                
                if update_strategy == "merge_replace":
                    old_args = response.json()[0]
                    old_args.update(args)
                    args = old_args

                if update_strategy == "replace":
                    for key, val in old_args.items():
                        if key not in args.keys():
                            args[key] = None

                person = Person(**args)
                person.id = person_id
                person.update()

            self.persons_df.loc[index, "id"] = person_id

        with pd.ExcelWriter('persons_output.xlsx') as writer:  
           self.persons_df.to_excel(writer, sheet_name='Persons')
            

