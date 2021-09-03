from pyLithoSurferAPI import Location
from pyLithoSurferAPI import Sample
from pyLithoSurferAPI import SampleWithLocation
from pyLithoSurferAPI.listUtilities import * 
from pyLithoSurferAPI.core.schemas import LocationSchema, SampleSchema, PersonSchema
import numpy as np
import urllib
from tqdm import tqdm


class SampleWithLocationUploader(object):

    def __init__(self, datapackageId, locations_df, samples_df):
        self.datapackageId = datapackageId
        self.locations_df = locations_df
        self.samples_df = samples_df
        self.validated = False

    def validate(self):

        # Validate Samples
        self.samples_df = SampleSchema.validate(self.samples_df)
        
        if "sampleMethodId" not in self.samples_df.columns:
            if "sampleMethodName" in self.samples_df.columns:
                self.samples_df["sampleMethodId"] = map_string_to_list_indices(self.samples_df.sampleMethodName, get_sampleMethod_id)
            else:
                self.samples_df["sampleMethodId"] = get_sampleMethod_id("Unknown")
                self.samples_df["sampleMethodName"] = "Unknown"

        if "sampleKindId" not in self.samples_df.columns:
            if "sampleKindName" in self.samples_df.columns:
                self.samples_df["sampleKindId"] = map_string_to_list_indices(self.samples_df.sampleKindName, get_sampleKind_id)
            else:
                self.samples_df["sampleKindId"] = get_sampleKind_id("Unknown")
                self.samples_df["sampleKindName"] = "Unknown"
        
        if "locationKindId" not in self.samples_df.columns:
            if "locationKindName" in self.samples_df.columns:
                self.samples_df["locationKindId"] = map_string_to_list_indices(self.samples_df.locationKindName, get_locationKind_id)
            else:
                self.samples_df["locationKindId"] = get_locationKind_id("Unknown")
                self.samples_df["locationKindName"] = "Unknown"
        
        if "referenceElevationSource" not in self.samples_df.columns:
            self.samples_df["referenceElevationSource"] = "API_LOOKUP"
            self.samples_df["referenceElevationKindId"] = get_elevation_kind_id("Ground level")
            self.samples_df["referenceElevationKindName"] = "Ground level"
        
        if "referenceElevationKindId" not in self.samples_df.columns:
            if "referenceElevationKindName" in self.samples_df.columns:
                self.samples_df["referenceElevationKindId"] = map_string_to_list_indices(self.samples_df.referenceElevationKindName, get_elevation_kind_id)
            else:
                self.samples_df["referenceElevationKindId"] = get_elevation_kind_id("Unknown")
                self.samples_df["referenceElevationKindName"] = "Unknown"
        
        self.samples_df["dataPackageId"] = self.datapackageId
        self.samples_df = self.samples_df.replace({np.nan: None})
        self.samples_df = SampleSchema.validate(self.samples_df)
        
        # Validate Location
        self.locations_df = LocationSchema.validate(self.locations_df)

        if "name" not in self.locations_df.columns:
            self.locations_df["name"] = self.samples_df.reindex(self.locations_df.index).copy()["name"]

        if "celestialId" not in self.locations_df.columns:
            if "celestialName" in self.locations_df.columns:
                self.locations_df["celestialId"] = map_string_to_list_indices(self.locations_df.celestialName, get_celestial_id)
            else:
                self.locations_df["celestialId"] = get_celestial_id("Earth")
                self.locations_df["celestialName"] = "Earth"

        self.locations_df = self.locations_df.replace({np.nan: None})
        self.locations_df = LocationSchema.validate(self.locations_df)

        self.validated = True
        return

    def upload(self, update=False, update_strategy="merge_keep", debug=False):

        print("Upload Samples and Locations")

        if not self.validated:
            raise ValueError("Data not validated")

        self.samples_df["locationId"] = None
        self.samples_df["id"] = None
        self.locations_df["id"] = None

        for index in tqdm(self.samples_df.index):

            # Check for existing samples at location
            loc_args = self.locations_df.loc[index].to_dict()
            samp_args = self.samples_df.loc[index].to_dict()
            
            lat = loc_args.get("lat")
            lon = loc_args.get("lon")
            name = samp_args.get("name") 
            
            query = {"locationCriteria.lon.greaterThan": lon - 0.001,
                     "locationCriteria.lon.lessThan": lon + 0.001,
                     "locationCriteria.lat.greaterThan": lat - 0.001,
                     "locationCriteria.lat.lessThan": lat + 0.001,
                     "name.equals": name}

            response = SampleWithLocation.get_from_query(urllib.parse.urlencode(query))
            records = response.json() 

            if records:
                sample_with_location_id = records[0]["id"]
            else:
                sample_with_location_id = None

            if sample_with_location_id is None: 
               
                location = Location(**loc_args)
                sample = Sample(**samp_args)    
           
                # Create SampleWithLocation object.
                SampWLocation = SampleWithLocation(location=location, sample=sample)
                SampWLocation.new(debug=False)

            elif update:

                if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
                    raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")
                    
                old_loc_args = records[0]["locationDTO"]
                old_samp_args = records[0]["sampleDTO"]
                
                if update_strategy == "merge_keep":
                    loc_args.update(old_loc_args)
                    samp_args.update(old_samp_args)
                
                if update_strategy == "merge_replace":
                    old_loc_args.update(loc_args)
                    old_samp_args.update(samp_args)
                    samp_args = old_samp_args
                    loc_args = old_loc_args

                if update_strategy == "replace":
                    loc_args["id"] = old_loc_args["id"]
                    samp_args["id"] = old_samp_args["id"]

                args = records[0]
                args.pop("id")
                location_id = loc_args.pop("id")
                sample_id = samp_args.pop("id")
                loc_args = {k:v for k, v in loc_args.items() if k in Location().to_dict().keys()}
                samp_args = {k:v for k, v in samp_args.items() if k in Sample().to_dict().keys()}
                # Create Location
                location = Location(**loc_args)
                location.id = location_id
                # Create Sample
                sample = Sample(**samp_args)    
                sample.id = sample_id
                # Create SampleWithLocation
                SampWLocation = SampleWithLocation(location=location, sample=sample)
                SampWLocation.id = sample_with_location_id
                SampWLocation.update()

            else:
                raise ValueError("Sample with location exist and you have chosen not to update")
           
            self.locations_df.loc[index, "id"] = SampWLocation.location.id
            self.samples_df.loc[index, "id"] = SampWLocation.sample.id
            self.samples_df.loc[index, "locationId"] = SampWLocation.location.id

        with pd.ExcelWriter('output.xlsx') as writer:  
            self.samples_df.to_excel(writer, sheet_name='Samples')
            self.locations_df.to_excel(writer, sheet_name='Locations')   


class PersonUploader(object):

    def __init__(self, persons_df):
        self.persons_df = persons_df

    def validate(self):
        self.persons_df = self.persons_df.dropna(how="any")
        self.persons_df = self.persons_df.drop_duplicates()
        self.persons_df = PersonSchema.validate(self.persons_df)
        return self.persons_df

    def upload(self, update=False, update_strategy="merge_keep", debug=False):
        from pyLithoSurferAPI.person import get_person_id, Person

        self.persons_df["id"] = None

        for index in tqdm(self.persons_df.index):

            row = self.persons_df.loc[index]
            args = row.to_dict()
            person_id = get_person_id(name=args["name"], firstName=args["firstName"])

            if (person_id is None):
                
                person = Person(**args)
                person.new(debug=debug) 
                person_id = person.id

            elif update:

                if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
                    raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")
                    
                query = {"id.equals": person_id}
                response = Person.get_from_query(urllib.parse.urlencode(query))

                if update_strategy == "merge_keep":
                    old_args = response.json()[0]
                    args.update(old_args)
                
                if update_strategy == "merge_replace":
                    old_args = response.json()[0]
                    old_args.update(args)
                    args = old_args

                args = {k:v for k, v in args.items() if k in Person().to_dict().keys()}
                person = Person(**args)
                person.id = person_id
                person.update()


            self.persons_df.loc[index, "id"] = person_id

        with pd.ExcelWriter('persons_output.xlsx') as writer:  
           self.persons_df.to_excel(writer, sheet_name='Persons')
            

