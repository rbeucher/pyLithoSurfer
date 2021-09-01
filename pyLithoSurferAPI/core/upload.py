from pyLithoSurferAPI import Location
from pyLithoSurferAPI import Sample
from pyLithoSurferAPI import SampleWithLocation
from pyLithoSurferAPI.listUtilities import * 
from pyLithoSurferAPI.core.schemas import LocationSchema, SampleSchema
import numpy as np
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

    def upload(self):

        print("Upload Samples and Locations")

        if not self.validated:
            raise ValueError("Data not validated")

        self.samples_df["locationId"] = None
        self.samples_df["id"] = None
        self.locations_df["id"] = None

        for index in tqdm(self.samples_df.index):
           
           # Create Location
           args = self.locations_df.loc[index].to_dict()
           args.pop("id")
           location = Location(**args)
           
           # Create Sample
           args = self.samples_df.loc[index].to_dict()
           args.pop("id")
           sample = Sample(**args)    
           
           # Create SampleWithLocation object.
           SampWLocation = SampleWithLocation(location=location, sample=sample)
           SampWLocation.new(debug=False)
           self.locations_df.loc[index, "id"] = SampWLocation.location.id
           self.samples_df.loc[index, "id"] = SampWLocation.sample.id
           self.samples_df.loc[index, "locationId"] = SampWLocation.location.id

        with pd.ExcelWriter('output.xlsx') as writer:  
           self.samples_df.to_excel(writer, sheet_name='Samples')
           self.locations_df.to_excel(writer, sheet_name='Locations')   
