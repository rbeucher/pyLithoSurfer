import os

import numpy as np
import pandas as pd
from pyLithoSurferAPI.core.lists import (LErrorType, LGeoEvent, LAnalyticalMethod)
from pyLithoSurferAPI.core.lists import get_list_name_to_id_mapping as get_id
from pyLithoSurferAPI.core.tables import (DataPoint, GeoeventAtAge, Material,
                                          Statement)
from pyLithoSurferAPI.core.upload import SampleWithLocationUploader
from pyLithoSurferAPI.AgeModel.schemas import (AgeDataPointSchema)
from pyLithoSurferAPI.AgeModel.tables import AgeDataPoint, AgeDataPointCRUD

from pyLithoSurferAPI.management.tables import DataPackage
from pyLithoSurferAPI.uploader import Uploader
from tqdm import tqdm


class AgeDataPointUploader(Uploader):

    name = "AgeDataPoint"
    
    def __init__(self, datapackageId, age_datapoints_df):

        self.datapackageId = datapackageId 
        self.age_datapoints_df = age_datapoints_df
        self.validated = False

    def validate(self):

        age_list = {"errorType": LErrorType,
                    "analyticalMethod": LAnalyticalMethod,
                    "geoEvent": LGeoEvent
                    }

        self.age_datapoints_df.dropna(subset=["age"], inplace=True)
        self.age_datapoints_df = Uploader._validate(self.age_datapoints_df, AgeDataPointSchema, age_list)
        self.validated = True

    def upload(self, update=False, update_strategy="merge_keep"):
    
        statement_keys = ["calculatedConfidence", "dataPointId", "description",
         "geoEventAtAgeId", "humanConfidence", "statementId",
         "relevance", "tempAtAgeId", "tempGradientId"] 

        geoEvent_keys = ["age", "ageError", "errorTypeId", "errorTypeName",
        "geoEventId", "geoEventName"]
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.age_datapoints_df["id"] = None
        self.age_datapoints_df["dataPointId"] = None

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

                # Use AgeDataPointCRUD to create the Datapoint and
                # the AgeDatapoint
                AgeDataptsCRUD = AgeDataPointCRUD(datapoint, age_datapoint, geo_event, statement) 
                AgeDataptsCRUD.new() 
                
                # Recover Datapoint
                self.age_datapoints_df.loc[index, "id"] = AgeDataptsCRUD.id
                self.age_datapoints_df.loc[index, "dataPointId"] = AgeDataptsCRUD.dataPoint.id
    
            elif update:

                if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
                    raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")

                old_dpts_args = records[0]["dataPointDTO"]
                dpts_args = self._update_args(old_dpts_args, dpts_args, update_strategy)
                old_age_args = records[0]["ageDataPointDTO"]
                age_args = self._update_args(old_age_args, age_args, update_strategy)
                old_stat_args = records[0]["geoEventAtAgeExtendsStatementDTO"]["statementDTO"]
                stat_args = self._update_args(old_stat_args, stat_args, update_strategy)
                old_event_args = records[0]["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"]
                event_args = self._update_args(old_event_args, event_args, update_strategy)

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)
                
                # Create a Statement
                statement = Statement(**stat_args)
                statement.dataPointId = datapoint.id
            
                # Create a geoEvent
                geo_event = GeoeventAtAge(**event_args)

                # Create AgeDataPoint
                age_datapoint = AgeDataPoint(**age_args)

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
