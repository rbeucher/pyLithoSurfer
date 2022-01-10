import os

import numpy as np
import pandas as pd

from pyLithoSurferAPI.FTrack.schemas import FTDataPointSchema
from pyLithoSurferAPI.core.lists import LErrorType, ReferenceMaterial

from pyLithoSurferAPI.core.tables import DataPoint, Material
from pyLithoSurferAPI.FTrack.tables import FTDataPoint, FTDataPointCRUD
from pyLithoSurferAPI.FTrack.lists import (LFTAgeAnalyticalTechnique, 
                                           LDosimeter,
                                           LEtchant,
                                           LFTAgeEquation,
                                           LFTAgeType,
                                           LFTAnalyticalMethod,
                                           LIrradiationReactor,
                                           LLambdaF, LLambda, LRmr0Equation)

from pyLithoSurferAPI.uploader import Uploader
from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm



class FTDataPointUploader(Uploader):

    name = "FTDataPoint"

    def __init__(self, datapackageId, ft_datapoints_df):

        self.datapackageId = datapackageId 
        self.ft_datapoints_df = ft_datapoints_df
        self.validated = False

    def validate(self):

        ft_list = {"dataPackage": DataPackage,
                   "ageErrorType": LErrorType,
                   "ftAgeAnalyticalTechnique": LFTAgeAnalyticalTechnique,
                   "dosimeter": LDosimeter,
                   "etchant": LEtchant,
                   "ftAgeEquation": LFTAgeEquation,
                   "ftAgeTyp": LFTAgeType,
                   "ftAnalyticalMethod": LFTAnalyticalMethod,
                   "irradiationReactor": LIrradiationReactor,
                   "lambdaF": LLambdaF,
                   "lambda": LLambda,
                   "mineral": Material,
                   "referenceMaterial": ReferenceMaterial,
                   "rmr0Equation": LRmr0Equation,
                   "zetaErrorType": LErrorType 
                   }

        self.ft_datapoints_df = Uploader._validate(self.ft_datapoints_df, FTDataPointSchema, ft_list)
        self.validated = True

    def upload(self, update=False, update_strategy="merge_keep"):
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.ft_datapoints_df["id"] = None

        for index in tqdm(self.ft_datapoints_df.index):

            ft_args = self.ft_datapoints_df.loc[index].to_dict()
            sampleId = ft_args.pop("sampleId")
            locationId = ft_args.pop("locationId")
            if ft_args.get("dataPointId"):
                ft_args.pop("dataPointId")

            dpts_args = {"dataPackageId": self.datapackageId,
                         "dataStructure": "FT",
                         "dataEntityId": None,
                         "name": None,
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.dataStructure.equals": "FT",
                     "dataPointLithoCriteria.sampleId.equals": int(sampleId),
                     "dataPointLithoCriteria.dataPackageId.equals": self.datapackageId}

            response = FTDataPointCRUD.query(query)
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

                # Create FTDataPoint
                ft_datapoint = FTDataPoint(**ft_args)

                # Use FTDataPointCRUD to create the Datapoint and
                # the FTDatapoint
                FTDataptsCRUD = FTDataPointCRUD(datapoint, ft_datapoint) 
                FTDataptsCRUD.new() 
                
                # Recover Datapoint
                self.ft_datapoints_df.loc[index, "id"] = FTDataptsCRUD.id
                self.ft_datapoints_df.loc[index, "dataPointId"] = FTDataptsCRUD.dataPoint.id

            elif update:

                old_dpts_args = records[0]["dataPointDTO"]
                dpts_args = self._update_args(old_dpts_args, dpts_args, update_strategy)
                old_ft_args = records[0]["ftdataPointDTO"]
                ft_args = self._update_args(old_ft_args, ft_args, update_strategy)

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create FTDataPoint
                ft_datapoint = FTDataPoint(**ft_args)

                # Use FTDataPointCRUD to create the Datapoint and
                # the FTDatapoint
                FTDataptsCRUD = FTDataPointCRUD(datapoint, ft_datapoint) 
                FTDataptsCRUD.id = ft_datapoint.id
                FTDataptsCRUD.dataPointId = datapoint.id
                FTDataptsCRUD.dataPoint.dataEntityId = ft_datapoint.id
                FTDataptsCRUD.dataPoint.ftdatapoint_id = ft_datapoint.id
                FTDataptsCRUD.update()
                self.ft_datapoints_df.loc[index, "id"] = FTDataptsCRUD.id
                self.ft_datapoints_df.loc[index, "dataPointId"] = datapoint.id