from pyLithoSurferAPI.core.upload import SampleWithLocationUploader
from pyLithoSurferAPI.SHRIMPModel.schemas import SHRIMPDataPointSchema
from pyLithoSurferAPI.core.tables import DataPoint, Statement, GeoeventAtAge
from pyLithoSurferAPI.SHRIMPModel.SHRIMPDataPoint import SHRIMPDataPoint, SHRIMPDataPointCRUD
from pyLithoSurferAPI.SHRIMPModel.SHRIMPAge import SHRIMPAge, SHRIMPAgeCRUD
from pyLithoSurferAPI.core.lists import LSHRIMPSampleFormat, LErrorType, LGeoEvent, LSHRIMPAgeType
from pyLithoSurferAPI.core.lists import get_list_name_to_id_mapping as get_id
import numpy as np
import pandas as pd
from tqdm import tqdm


class SHRIMPDataPointUploader(object):

    def __init__(self, datapackageId, shrimp_datapoints_df):

        self.datapackageId = datapackageId 
        self.shrimp_datapoints_df = shrimp_datapoints_df
        self.validated = False

    def validate(self):

        self.shrimp_datapoints_df = SHRIMPDataPointSchema.validate(self.shrimp_datapoints_df)

        if "mineralOfInterestId" not in self.shrimp_datapoints_df.columns:
            raise ValueError("Mineral Name lookup not implemented")

        if "sampleFormatId" not in self.shrimp_datapoints_df.columns:
            if "sampleFormatName" in self.shrimp_datapoints_df.columns:
                self.shrimp_datapoints_df["sampleFormatId"] = self.shrimp_datapoints_df.sampleFormatName.map(get_id(LSHRIMPSampleFormat))
            else:
                self.shrimp_datapoints_df["sampleFormatId"] = LSHRIMPSampleFormat.get_id_from_name("Unknown")
                self.shrimp_datapoints_df["sampleFormatName"] = "Unknown"

        self.shrimp_datapoints_df = self.shrimp_datapoints_df.replace({np.nan: None})
        self.shrimp_datapoints_df = SHRIMPDataPointSchema.validate(self.shrimp_datapoints_df)
        self.validated = True

    def upload(self, update=False, update_strategy="merge_keep", debug=False):
        
        print("Upload SHRIMPDataPoints")

        if not self.validated:
            raise ValueError("Data not validated")

        self.shrimp_datapoints_df["id"] = None
        self.errors_df = pd.DataFrame(columns=["id", "exception"])


        for index in tqdm(self.shrimp_datapoints_df.index):

            shrimp_args = self.shrimp_datapoints_df.loc[index].to_dict()
            sampleId = shrimp_args.pop("sampleId")
            locationId = shrimp_args.pop("locationId")

            dpts_args = {"dataPackageId": self.datapackageId,
                         "dataStructure": "UPB_SHRIMP",
                         "name": None,
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.sampleId.equals": sampleId,
                     "dataPointLithoCriteria.dataStructure.equals": "UPB_SHRIMP",
                     "dataPointLithoCriteria.dataPackageId.equals": self.datapackageId,
                     "mountIdentifier.equals": shrimp_args["mountIdentifier"]}
        
            response = SHRIMPDataPointCRUD.query(query)
            records = response.json()

            if len(records) == 1:
                existing_id = records[0]["id"]
            elif len(records) > 1:
                #print(records)
                #continue
                existing_id = records[0]["id"]
                #raise ValueError("Muliple Datapoints exists")
            else:
                existing_id = None

            if existing_id is None: 

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create SHRIMPDataPoint
                shrimp_datapoint = SHRIMPDataPoint(**shrimp_args)

                # Use SHRIMPDataPointCRUD to create the Datapoint and
                # the SHRIMPDatapoint
                SHRIMPDataptsCRUD = SHRIMPDataPointCRUD(datapoint, shrimp_datapoint) 
                _ = SHRIMPDataptsCRUD.new(debug=debug) 

                # Recover Datapoint
                datapoint = SHRIMPDataptsCRUD.dataPoint
                shrimp_datapoint = SHRIMPDataptsCRUD.shrimpDataPoint
                self.shrimp_datapoints_df.loc[index, "id"] = shrimp_datapoint.id

            elif update:

                if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
                    raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")

                old_dpts_args = records[0]["dataPointDTO"]
                old_shrimp_args = records[0]["shrimpdataPointDTO"]
                old_dpts_args = {k:v for k,v in old_dpts_args.items() if v is not None}
                old_shrimp_args = {k:v for k,v in old_shrimp_args.items() if v is not None}

                if update_strategy == "merge_keep":
                    dpts_args.update(old_dpts_args)
                    shrimp_args.update(old_shrimp_args)
                
                if update_strategy == "merge_replace":
                    old_dpts_args.update(dpts_args)
                    old_shrimp_args.update(shrimp_args)
                    dpts_args = old_dpts_args
                    shrimp_dpts = old_shrimp_args

                if update_strategy == "replace":
                    for key, val in old_dpts_args.items():
                        if key not in dpts_args.keys():
                            dpts_args[key] = None
                    for key, val in old_shrimp_args.items():
                        if key not in shrimp_args.keys():
                            shrimp_args[key] = None   

                dpts_args["id"] = old_dpts_args["id"]
                shrimp_args["id"] = old_shrimp_args["id"]

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create SHRIMPDataPoint
                shrimp_datapoint = SHRIMPDataPoint(**shrimp_args)

                try:
                    # Use SHRIMPDataPointCRUD to create the Datapoint and
                    # the SHRIMPDatapoint
                    SHRIMPDataptsCRUD = SHRIMPDataPointCRUD(datapoint, shrimp_datapoint) 
                    SHRIMPDataptsCRUD.id = shrimp_datapoint.id
                    SHRIMPDataptsCRUD.dataPointId = datapoint.id
                    SHRIMPDataptsCRUD.update(debug=debug)
                except Exception as e:
                    self.errors_df.loc[index] = [datapoint.id, str(type(e))]

        with pd.ExcelWriter('output.xlsx', mode='a') as writer:  
            self.shrimp_datapoints_df.to_excel(writer, sheet_name='SHRIMPDataPoint')
            self.errors_df.to_excel(writer, sheet_name="ShrimpErrors")   



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
                self.shrimp_ages_df["errorTypeId"] = self.shrimp_ages_df.errorTypeName.apply(LErrorType.get_id_from_name)
            else:
                self.shrimp_ages_df["errorTypeId"] = LErrorType.get_id_from_name("Unknown")
                self.shrimp_ages_df["errorTypeName"] = "Unknown"
        
        if "geoEventId" not in self.shrimp_ages_df.columns:
            if "geoEventName" in self.shrimp_ages_df.columns:
                self.shrimp_ages_df["geoEventId"] = self.shrimp_ages_df.geoEventName.apply(LGeoEvent.get_id_from_name)
            else:
                self.shrimp_ages_df["geoEventId"] = LGeoEvent.get_id_from_name("Unknown")
                self.shrimp_ages_df["geoEventName"] = "Unknown"
        
        if "ageTypeId" not in self.shrimp_ages_df.columns:
            if "ageTypeName" in self.shrimp_ages_df.columns:
                self.shrimp_ages_df["ageTypeId"] = self.shrimp_ages_df.ageTypeName.apply(LSHRIMPAgeType.get_id_from_name)
            else:
                self.shrimp_ages_df["ageTypeId"] = LSHRIMPAgeType.get_id_from_name("Unknown")
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

