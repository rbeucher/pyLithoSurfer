import os

import numpy as np
import pandas as pd
from pyLithoSurferAPI.core.lists import (LErrorType, LGeoEvent, LSHRIMPAgeType,
                                         LSHRIMPSampleFormat, LSHRIMPAgeGroup)
from pyLithoSurferAPI.core.lists import get_list_name_to_id_mapping as get_id
from pyLithoSurferAPI.core.tables import (DataPoint, GeoeventAtAge, Material,
                                          Statement, Machine)
from pyLithoSurferAPI.core.upload import SampleWithLocationUploader
from pyLithoSurferAPI.SHRIMPModel.schemas import (SHRIMPAgeSchema,
                                                  SHRIMPDataPointSchema)
from pyLithoSurferAPI.SHRIMPModel.SHRIMPAge import SHRIMPAge, SHRIMPAgeCRUD
from pyLithoSurferAPI.SHRIMPModel.SHRIMPDataPoint import (SHRIMPDataPoint,
                                                          SHRIMPDataPointCRUD)

from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm


class SHRIMPDataPointUploader(Uploader):

    name = "SHRIMPDataPoint"

    def __init__(self, datapackageId, shrimp_datapoints_df):

        self.datapackageId = datapackageId 
        self.shrimp_datapoints_df = shrimp_datapoints_df
        self.validated = False

    def validate(self):

        shrimp_list = {"dataPackage": DataPackage,
                       "mineralOfInterest": Material,
                       "sampleFormat": LSHRIMPSampleFormat,
                       "machine": Machine
        }

        self.shrimp_datapoints_df = Uploader._validate(self.shrimp_datapoints_df, SHRIMPDataPointSchema, shrimp_list)
        self.validated = True

    def upload(self, update=False, update_strategy="merge_keep"):
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.shrimp_datapoints_df["id"] = None

        for index in tqdm(self.shrimp_datapoints_df.index):

            shrimp_args = self.shrimp_datapoints_df.loc[index].to_dict()
            sampleId = shrimp_args.pop("sampleId")
            locationId = shrimp_args.pop("locationId")
            if shrimp_args.get("dataPointId"):
                shrimp_args.pop("dataPointId")

            dpts_args = {"dataPackageId": self.datapackageId,
                         "dataStructure": "UPB_SHRIMP",
                         "dataEntityId": None,
                         "name": None,
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.sampleId.equals": sampleId,
                     "dataPointLithoCriteria.dataStructure.equals": "UPB_SHRIMP",
                     "dataPointLithoCriteria.dataPackageId.equals": self.datapackageId}

            if "mountIdentifier" in shrimp_args.keys():
                query["mountIdentifier.equals"] = shrimp_args["mountIdentifier"]

            response = SHRIMPDataPointCRUD.query(query)
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

                # Create SHRIMPDataPoint
                shrimp_datapoint = SHRIMPDataPoint(**shrimp_args)

                # Use SHRIMPDataPointCRUD to create the Datapoint and
                # the SHRIMPDatapoint
                SHRIMPDataptsCRUD = SHRIMPDataPointCRUD(datapoint, shrimp_datapoint) 
                SHRIMPDataptsCRUD.new() 
                
                # Recover Datapoint
                self.shrimp_datapoints_df.loc[index, "id"] = SHRIMPDataptsCRUD.id
                self.shrimp_datapoints_df.loc[index, "dataPointId"] = SHRIMPDataptsCRUD.dataPoint.id

            elif update:

                old_dpts_args = records[0]["dataPointDTO"]
                dpts_args = self._update_args(old_dpts_args, dpts_args, update_strategy)
                old_shrimp_args = records[0]["shrimpdataPointDTO"]
                shrimp_args = self._update_args(old_shrimp_args, shrimp_args, update_strategy)

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create SHRIMPDataPoint
                shrimp_datapoint = SHRIMPDataPoint(**shrimp_args)

                # Use SHRIMPDataPointCRUD to create the Datapoint and
                # the SHRIMPDatapoint
                SHRIMPDataptsCRUD = SHRIMPDataPointCRUD(datapoint, shrimp_datapoint) 
                SHRIMPDataptsCRUD.id = shrimp_datapoint.id
                SHRIMPDataptsCRUD.dataPointId = datapoint.id
                SHRIMPDataptsCRUD.dataPoint.dataEntityId = shrimp_datapoint.id
                SHRIMPDataptsCRUD.dataPoint.shrimp_datapoint_id = shrimp_datapoint.id
                SHRIMPDataptsCRUD.update()
                self.shrimp_datapoints_df.loc[index, "id"] = SHRIMPDataptsCRUD.id
                self.shrimp_datapoints_df.loc[index, "dataPointId"] = datapoint.id


class SHRIMPAgeUploader(Uploader):

    name = "SHIMPAge"
    
    def __init__(self, datapackageId, shrimp_ages_df):

        self.datapackageId = datapackageId 
        self.shrimp_ages_df = shrimp_ages_df
        self.validated = False

    def validate(self):

        shrimp_list = {"errorType": LErrorType,
                       "geoEvent": LGeoEvent,
                       "ageType": LSHRIMPAgeType,
                       "ageGroup": LSHRIMPAgeGroup
                       }

        self.shrimp_ages_df.dropna(subset=["age"], inplace=True)
        df = self.shrimp_ages_df 
        df.loc[pd.isnull(df["errorTypeName"]), "errorTypeName"] = "Unknown"
        df.loc[pd.isnull(df["geoEventName"]), "geoEventName"] = "Unknown"
        df.loc[pd.isnull(df["ageTypeName"]), "ageTypeName"] = "Unknown date"
        df.loc[pd.isnull(df["ageGroupName"]), "ageGroupName"] = "Z (undefined)"
        df = SHRIMPAgeSchema.validate(self.shrimp_ages_df)

    def upload(self, update=False, update_strategy="merge_keep"):
    
        shrimp_age_keys = ["ageGroupId", "ageGroupName", "ageTypeId",
         "ageTypeName", "calcName", "id", "mswd",
         "numberAnalysesCombined", "rmQcTest"]

        statement_keys = ["calculatedConfidence", "dataPointId", "description",
         "geoEventAtAgeId", "humanConfidence", "statementId",
         "relevance", "tempAtAgeId", "tempGradientId"] 

        geoEvent_keys = ["age", "ageError", "errorTypeId", "errorTypeName",
        "geoEventId", "geoEventName"]
        
        self.shrimp_ages_df["id"] = None
       
        for index in tqdm(self.shrimp_ages_df.index):

            args = self.shrimp_ages_df.loc[index].to_dict()
            args.pop("id")
            stat_args = {k:v for k,v in args.items() if k in self.statement_keys}
            event_args = {k:v for k,v in args.items() if k in self.geoEvent_keys}
            shrimp_age_args = {k:v for k,v in args.items() if k in self.shrimp_age_keys}

            query = {"geoEventAtAgeLithoCriteria.age.equals": args["age"],
                     "geoEventAtAgeLithoCriteria.statementCriteria.dataPointId.equals": args["dataPointId"]}
        
            response = SHRIMPAgeCRUD.query(query)
            records = response.json()
            
            if len(records) == 1:
                existing_id = records[0]["id"]
            elif len(records) > 1:
                existing_id = records[0]["id"]
            else:
                existing_id = None

            if existing_id is None:

                # Create a Statement
                statement = Statement(**stat_args)
            
                # Create a geoEvent
                geo_event = GeoeventAtAge(**event_args)
            
                # Create a SHRIMPAge
                shrimp_age = SHRIMPAge(**shrimp_age_args)        
            
                # Use SHRIMPAgeCRUD to create the Statement and the SHRIMPAge and
                # the GeoEvent
                shrimp_age_crud = SHRIMPAgeCRUD(geo_event, statement, shrimp_age)
                shrimp_age_crud.new()
                self.shrimp_ages_df.loc[index, "id"] = shrimp_age_crud.id

            elif update:

                old_stat_args = records[0]["geoEventAtAgeExtendsStatementDTO"]["statementDTO"]
                old_event_args = records[0]["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"]
                old_shrimp_age_args = records[0]["shrimpageDTO"]
                
                # Create a Statement
                statement = Statement(**stat_args)
            
                # Create a geoEvent
                geo_event = GeoeventAtAge(**event_args)
            
                # Create a SHRIMPAge
                shrimp_age = SHRIMPAge(**shrimp_age_args)     
            
                # Use SHRIMPAgeCRUD to create the Statement and the SHRIMPAge and
                # the GeoEvent
                shrimp_age_crud = SHRIMPAgeCRUD(geo_event, statement, shrimp_age)
                shrimp_age_crud.update()
                self.shrimp_ages_df.loc[index, "id"] = shrimp_age_crud.id