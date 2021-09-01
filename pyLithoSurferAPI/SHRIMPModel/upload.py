from pyLithoSurferAPI.core.upload import SampleWithLocationUploader
from pyLithoSurferAPI.SHRIMPModel.schemas import SHRIMPDataPointSchema
from pyLithoSurferAPI import DataPoint, Statement, GeoeventAtAge
from pyLithoSurferAPI import SHRIMPDataPoint, SHRIMPDataPointCRUD, SHRIMPAge, SHRIMPAgeCRUD
from pyLithoSurferAPI.listUtilities import * 
import numpy as np
from tqdm import tqdm


class SHRIMPDataPointUploader(SampleWithLocationUploader):

    def __init__(self, datapackageId, locations_df, samples_df, shrimp_datapoints_df):
        
        super().__init__(datapackageId, locations_df, samples_df)
        self.shrimp_datapoints_df = shrimp_datapoints_df
        self.validated = False

    def validate(self):
        super().validate()

        self.shrimp_datapoints_df = SHRIMPDataPointSchema.validate(self.shrimp_datapoints_df)

        if "mineralOfInterestId" not in self.shrimp_datapoints_df.columns:
            raise ValueError("Mineral Name lookup not implemented")

        if "sampleFormatId" not in self.shrimp_datapoints_df.columns:
            if "sampleFormatName" in self.shrimp_datapoints_df.columns:
                self.shrimp_datapoints_df["sampleFormatId"] = map_string_to_list_indices(self.shrimp_datapoints_df.sampleFormatName, get_SHRIMPsampleFormat_id)
            else:
                self.shrimp_datapoints_df["sampleFormatId"] = get_SHRIMPsampleFormat_id("Unknown")
                self.shrimp_datapoints_df["sampleFormatName"] = "Unknown"

        self.shrimp_datapoints_df = self.shrimp_datapoints_df.replace({np.nan: None})
        self.shrimp_datapoints_df = SHRIMPDataPointSchema.validate(self.shrimp_datapoints_df)

    def upload(self):
        super().upload()

        print("Upload SHRIMPDataPoints")

        self.shrimp_datapoints_df["id"] = None

        for index in tqdm(self.samples_df.index):
            
            # Create DataPoint
            args = {"dataPackageId": self.datapackageId,
                    "dataStructure": "UPB_SHRIMP",
                    "name": self.samples_df.loc[index, "name"]}
            datapoint = DataPoint(**args)
            datapoint.locationId = self.locations_df.loc[index, "id"]
            datapoint.sampleId = self.samples_df.loc[index, "id"]

            # Create SHRIMPDataPoint
            args = self.shrimp_datapoints_df.loc[index].to_dict()
            args.pop("id")
            shrimp_datapoint = SHRIMPDataPoint(**args)

            # Use SHRIMPDataPointCRUD to create the Datapoint and
            # the SHRIMPDatapoint
            SHRIMPDataptsCRUD = SHRIMPDataPointCRUD(datapoint, shrimp_datapoint) 
            _ = SHRIMPDataptsCRUD.new(debug=False) 

            # Recover Datapoint
            datapoint = SHRIMPDataptsCRUD.dataPoint
            shrimp_datapoint = SHRIMPDataptsCRUD.shrimpDataPoint
            self.shrimp_datapoints_df.loc[index, "id"] = datapoint.id

        with pd.ExcelWriter('output.xlsx', mode='a') as writer:  
            self.shrimp_datapoints_df.to_excel(writer, sheet_name='SHRIMPDataPoint')


class SHRIMPAgeUploader(SHRIMPDataPointUploader):

    def __init__(self, datapackageId, locations_df, samples_df, shrimp_datapoints_df, shrimp_ages_df):
        
        super().__init__(datapackageId, locations_df, samples_df, shrimp_datapoints_df)
        self.shrimp_ages_df = shrimp_ages_df
        self.validated = False

    def validate(self):
        super().validate()


        self.shrimp_ages_df = SHRIMPDataPointSchema.validate(self.shrimp_ages_df)

        if "errorTypeId" not in self.shrimp_ages_df.columns:
            if "errorTypeName" in self.shrimp_ages_df.columns:
                self.shrimp_ages_df["errorTypeId"] = map_string_to_list_indices(self.shrimp_ages_df.errorTypeName, get_error_type_id)
            else:
                self.shrimp_ages_df["errorTypeId"] = get_error_type_id("Unknown")
                self.shrimp_ages_df["errorTypeName"] = "Unknown"
        
        if "geoEventId" not in self.shrimp_ages_df.columns:
            if "geoEventName" in self.shrimp_ages_df.columns:
                self.shrimp_ages_df["geoEventId"] = map_string_to_list_indices(self.shrimp_ages_df.geoEventName, get_geoEvent_id)
            else:
                self.shrimp_ages_df["geoEventId"] = get_geoEvent_id("Unknown")
                self.shrimp_ages_df["geoEventName"] = "Unknown"
        
        if "ageTypeId" not in self.shrimp_ages_df.columns:
            if "ageTypeName" in self.shrimp_ages_df.columns:
                self.shrimp_ages_df["ageTypeId"] = map_string_to_list_indices(self.shrimp_ages_df.ageTypeName, get_SHRIMPAgeType_id)
            else:
                self.shrimp_ages_df["ageTypeId"] = get_SHRIMPAgeType_id("Unknown")
                self.shrimp_ages_df["ageTypeName"] = "Unknown"

        self.shrimp_ages_df = self.shrimp_ages_df.replace({np.nan: None})
        self.shrimp_ages_df = SHRIMPDataPointSchema.validate(self.shrimp_ages_df)

    def upload(self):
        super().upload()
        
        self.shrimp_ages_df["id"] = None
        
        print("Upload SHRIMPAges")

        for index in tqdm(self.samples_df.index):
            
            # Create a Statement
            statement = Statement()
            statement.dataPointId = self.shrimp_datapoints_df.loc[index, "id"]
            
            # Create a geoEvent
            args = self.shrimp_ages_df.loc[index].to_dict()
            ageTypeId = args.pop("ageTypeId")
            ageTypeName = args.pop("ageTypeName")
            args.pop("id")
            geo_event = GeoeventAtAge(**args)
            
            # Create a SHRIMPAge
            shrimp_age = SHRIMPAge(ageTypeId=ageTypeId)        
            
            # Use SHRIMPAgeCRUD to create the Statement and the SHRIMPAge and
            # the GeoEvent
            shrimp_age_crud = SHRIMPAgeCRUD(geo_event, statement, shrimp_age)
            shrimp_age_crud.new(debug=False)

        with pd.ExcelWriter('output.xlsx', mode='a') as writer:  
            self.shrimp_ages_df.to_excel(writer, sheet_name='SHRIMPAge')

