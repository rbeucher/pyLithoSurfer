import os

import numpy as np
import pandas as pd
from pyLithoSurferAPI.core.lists import (LErrorType, LGeoEvent, LAnalyticalMethod)
from pyLithoSurferAPI.core.lists import get_list_name_to_id_mapping as get_id
from pyLithoSurferAPI.core.tables import (DataPoint, GeoeventAtAge, Material,
                                          Statement)
from pyLithoSurferAPI.core.upload import SampleWithLocationUploader
from pyLithoSurferAPI.AgeModel.schemas import (AgeDataPointSchema)
from pyLithoSurferAPI.AgeModel.AgeDataPoint import AgeDataPoint, AgeDataPointCRUD

from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm


class AgeDataPointUploader(object):
    
    age_keys = ["id"]

    statement_keys = ["calculatedConfidence", "dataPointId", "description",
     "geoEventAtAgeId", "humanConfidence", "statementId",
     "relevance", "tempAtAgeId", "tempGradientId"] 

    geoEvent_keys = ["age", "ageError", "errorTypeId", "errorTypeName",
    "geoEventId", "geoEventName"]

    def __init__(self, datapackageId, age_datapoints_df):

        self.datapackageId = datapackageId 
        self.age_datapoints_df = age_datapoints_df
        self.validated = False

    def validate(self):

        self.age_datapoints_df.dropna(subset=["age"], inplace=True)
        self.age_datapoints_df = AgeDataPointSchema.validate(self.age_datapoints_df)
        
        if "errorTypeId" not in self.age_datapoints_df.columns:
            if "errorTypeName" in self.age_datapoints_df.columns:
                self.age_datapoints_df["errorTypeId"] = self.age_datapoints_df.errorTypeName.map(get_id(LErrorType))
            else:
                self.age_datapoints_df["errorTypeId"] = LErrorType.get_id_from_name("Unknown")
                self.age_datapoints_df["errorTypeName"] = "Unknown"

        if "analyticalMethodId" not in self.age_datapoints_df.columns:
            if "analyticalMethodName" in self.age_datapoints_df.columns:
                self.age_datapoints_df["analyticalMethodId"] = self.age_datapoints_df.analyticalMethodName.map(get_id(LAnalyticalMethod))
            else:
                self.age_datapoints_df["analyticalMethodId"] = None
                self.age_datapoints_df["analyticalMethodName"] = None
        
        if "geoEventId" not in self.age_datapoints_df.columns:
            if "geoEventName" in self.age_datapoints_df.columns:
                events = self.age_datapoints_df.geoEventName.unique()
                mapping = {}
                for event in events:
                    mapping[event] = LGeoEvent.get_id_from_name(event)
                self.age_datapoints_df["geoEventId"] = self.age_datapoints_df.geoEventName.map(mapping)
            else:
                self.age_datapoints_df["geoEventId"] = LGeoEvent.get_id_from_name("Unknown")
                self.age_datapoints_df["geoEventName"] = "Unknown"
        
        self.age_datapoints_df = self.age_datapoints_df.replace({np.nan: None})
        self.age_datapoints_df = AgeDataPointSchema.validate(self.age_datapoints_df)
        self.age_datapoints_df = self.age_datapoints_df.astype(object).where(pd.notnull(self.age_datapoints_df), None)
        self.validated = True

    def upload(self, update=False, update_strategy="merge_keep"):
        
        print("Upload AgeDataPoints")

        if not self.validated:
            raise ValueError("Data not validated")

        self.age_datapoints_df["id"] = None
        self.age_datapoints_df["dataPointId"] = None
        self.errors_df = pd.DataFrame(columns=["id", "exception"])


        for index in tqdm(self.age_datapoints_df.index):

            age_args = self.age_datapoints_df.loc[index].to_dict()
            analyticalMethodId = age_args.pop("analyticalMethodId")
            sampleId = age_args.pop("sampleId")
            locationId = age_args.pop("locationId")
            stat_args = {k:v for k,v in age_args.items() if k in self.statement_keys}
            event_args = {k:v for k,v in age_args.items() if k in self.geoEvent_keys}

            dpts_args = {"dataPackageId": self.datapackageId,
                         "dataStructure": "AGE",
                         "dataEntityId": None,
                         "name": None,
                         "analyticalMethodId": analyticalMethodId, 
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.sampleId.equals": sampleId,
                     "dataPointLithoCriteria.dataStructure.equals": "AGE",
                     "dataPointLithoCriteria.dataPackageId.equals": self.datapackageId}

            response = AgeDataPointCRUD.query(query)
            records = response.json()

            if len(records) == 1:
                existing_id = records[0]["id"]
            elif len(records) > 1:
                existing_id = records[0]["id"]
            else:
                existing_id = None

            if existing_id is None:

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create a Statement
                statement = Statement(**stat_args)
            
                # Create a geoEvent
                geo_event = GeoeventAtAge(**event_args)

                # Create AgeDataPoint
                age_datapoint = AgeDataPoint(**age_args)

                try:
                    # Use AgeDataPointCRUD to create the Datapoint and
                    # the AgeDatapoint
                    AgeDataptsCRUD = AgeDataPointCRUD(datapoint, age_datapoint, geo_event, statement) 
                    AgeDataptsCRUD.new() 
                    
                    # Recover Datapoint
                    self.age_datapoints_df.loc[index, "id"] = AgeDataptsCRUD.id
                    self.age_datapoints_df.loc[index, "dataPointId"] = AgeDataptsCRUD.dataPoint.id
    
                except Exception as e:
                    self.errors_df.loc[index] = [datapoint.id, str(type(e))]                

            elif update:

                if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
                    raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")

                old_dpts_args = records[0]["dataPointDTO"]
                old_age_args = records[0]["ageDataPointDTO"]
                old_stat_args = records[0]["geoEventAtAgeExtendsStatementDTO"]["statementDTO"]
                old_event_args = records[0]["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"]
                old_dpts_args = {k:v for k,v in old_dpts_args.items() if v is not None}
                old_age_args = {k:v for k,v in old_age_args.items() if v is not None}
                old_stat_args = {k:v for k,v in old_stat_args.items() if v is not None}
                old_event_args = {k:v for k,v in old_event_args.items() if v is not None}

                if update_strategy == "merge_keep":
                    dpts_args.update(old_dpts_args)
                    age_args.update(old_age_args)
                    stat_args.update(old_stat_args)
                    event_args.update(old_event_args)
                
                if update_strategy == "merge_replace":
                    old_dpts_args.update(dpts_args)
                    old_age_args.update(age_args)
                    old_stat_args.update(stat_args)
                    old_event_args.update(event_args)
                    dpts_args = old_dpts_args
                    age_dpts = old_age_args
                    stat_args = old_stat_args
                    event_args = old_event_args

                if update_strategy == "replace":
                    for key, val in old_dpts_args.items():
                        if key not in dpts_args.keys():
                            dpts_args[key] = None
                    for key, val in old_age_args.items():
                        if key not in age_args.keys():
                            age_args[key] = None   
                    for key, val in old_event_args.items():
                        if key not in event_args.keys():
                            event_args[key] = None   
                    for key, val in old_stat_args.items():
                        if key not in stat_args.keys():
                            stat_args[key] = None   

                dpts_args["id"] = old_dpts_args["id"]
                age_args["id"] = old_age_args["id"]
                event_args["id"] = old_event_args["id"]
                stat_args["id"] = old_stat_args["id"]

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)
                
                # Create a Statement
                statement = Statement(**stat_args)
                statement.dataPointId = datapoint.id
            
                # Create a geoEvent
                geo_event = GeoeventAtAge(**event_args)

                # Create AgeDataPoint
                age_datapoint = AgeDataPoint(**age_args)

                try:
                    # Use AgeDataPointCRUD to create the Datapoint and
                    # the AgeDatapoint
                    AgeDataptsCRUD = AgeDataPointCRUD(datapoint, age_datapoint, geo_event, statement)
                    AgeDataptsCRUD.id = age_datapoint.id
                    AgeDataptsCRUD.dataPointId = datapoint.id
                    AgeDataptsCRUD.dataPoint.dataEntityId = age_datapoint.id
                    AgeDataptsCRUD.dataPoint.age_datapoint_id = age_datapoint.id
                    AgeDataptsCRUD.update()
                    self.age_datapoints_df.loc[index, "id"] = AgeDataptsCRUD.id
                    self.age_datapoints_df.loc[index, "dataPointId"] = datapoint.id

                except Exception as e:
                    self.errors_df.loc[index] = [datapoint.id, str(type(e))]
        
        
        if os.path.isfile("output.xlsx"):
            mode = "a"
        else:
            mode = "w"

        with pd.ExcelWriter('output.xlsx', mode=mode, if_sheet_exists="replace") as writer:  
            self.age_datapoints_df.to_excel(writer, sheet_name='AgeDataPoint')
            self.errors_df.to_excel(writer, sheet_name="AgeErrors")   

