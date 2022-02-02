import os

import numpy as np
import pandas as pd

from pyLithoSurferAPI.FTrack.schemas import FTBinnedLengthDataSchema, FTCountDataSchema, FTDataPointSchema, FTRawDataPointSchema, FTSingleGrainSchema
from pyLithoSurferAPI.core.lists import LErrorType, ReferenceMaterial

from pyLithoSurferAPI.core.tables import DataPoint, Material, Machine
from pyLithoSurferAPI.FTrack.tables import FTBinnedLengthData, FTCountData, FTDataPoint, FTDataPointCRUD, FTLengthData, FTSingleGrain, FTRawDataPoint, FTRawDataPointCRUD
from pyLithoSurferAPI.FTrack.lists import (LFTAgeAnalyticalTechnique, 
                                           LDosimeter,
                                           LEtchant,
                                           LFTAgeEquation,
                                           LFTAgeType,
                                           LFTAnalyticalMethod, LFTAnalyticalSoftware,
                                           LIrradiationReactor,
                                           LLambdaF, LLambda, LRmr0Equation, LTrackType)

from pyLithoSurferAPI.uploader import Uploader
from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm



class FTDataPointUploader(Uploader):

    name = "FTDataPoints"

    def __init__(self, datapackageId, ft_datapoints_df):

        self.datapackageId = datapackageId 
        self.dataframe = ft_datapoints_df
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

        self.dataframe = Uploader._validate(self.dataframe, FTDataPointSchema, ft_list)
        self.validated = True

    def upload(self, update=False, update_strategy="replace"):
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            ft_args = self.dataframe.loc[index].to_dict()
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
                self.dataframe.loc[index, "id"] = FTDataptsCRUD.id
                self.dataframe.loc[index, "dataPointId"] = FTDataptsCRUD.dataPoint.id

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
                FTDataptsCRUD.dataPointID = datapoint.id
                FTDataptsCRUD.dataPoint.dataEntityId = ft_datapoint.id
                FTDataptsCRUD.dataPoint.ftdatapoint_id = ft_datapoint.id
                FTDataptsCRUD.update()
                self.dataframe.loc[index, "id"] = FTDataptsCRUD.id
                self.dataframe.loc[index, "dataPointId"] = datapoint.id

class FTRawDataPointUploader(Uploader):

    name = "FTRawDataPoints"

    def __init__(self, datapackageId, ftraw_datapoints_df):

        self.datapackageId = datapackageId 
        self.dataframe = ftraw_datapoints_df
        self.validated = False

    def validate(self):

        ft_list = {"dataPackage": DataPackage,
                   "etchant": LEtchant,
                   "ftAnalyticalMethod": LFTAnalyticalMethod,
                   "ftAnalyticalSoftwareName" : LFTAnalyticalSoftware,
                   "machine": Machine,
                   "mineral": Material,
                   }

        self.dataframe = Uploader._validate(self.dataframe, FTRawDataPointSchema, ft_list)
        self.validated = True

    def upload(self, update=False, update_strategy="replace"):
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            ftraw_args = self.dataframe.loc[index].to_dict()
            sampleId = ftraw_args.pop("sampleId")
            if ftraw_args.get("dataPointId"):
                ftraw_args.pop("dataPointId")

            dpts_args = {"dataPackageId": self.datapackageId,
                         "dataStructure": "FT_RAW",
                         "dataEntityId": None,
                         "name": None
                         # Here we should not linke sampleId and location_id
                         # Same, the ftdatapoint should not be linked here
                         }
            
            query = {"dataPointLithoCriteria.dataStructure.equals": "FT_RAW",
                     "dataPointLithoCriteria.sampleId.equals": int(sampleId),
                     "dataPointLithoCriteria.dataPackageId.equals": self.datapackageId}

            response = FTRawDataPointCRUD.query(query)
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
                ftraw_datapoint = FTRawDataPoint(**ftraw_args)

                # Use FTDataPointCRUD to create the Datapoint and
                # the FTDatapoint
                FTDataptsCRUD = FTRawDataPointCRUD(datapoint, ftraw_datapoint) 
                FTDataptsCRUD.new() 
                
                # Recover Datapoint
                self.dataframe.loc[index, "id"] = FTDataptsCRUD.id
                self.dataframe.loc[index, "dataPointId"] = FTDataptsCRUD.dataPoint.id

            elif update:

                old_dpts_args = records[0]["dataPointDTO"]
                dpts_args = self._update_args(old_dpts_args, dpts_args, update_strategy)
                old_ftraw_args = records[0]["ftrawDataPointDTO"]
                ftraw_args = self._update_args(old_ftraw_args, ftraw_args, update_strategy)

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create FTDataPoint
                ftraw_datapoint = FTRawDataPoint(**ftraw_args)

                # Use FTDataPointCRUD to create the Datapoint and
                # the FTDatapoint
                FTDataptsCRUD = FTRawDataPointCRUD(datapoint, ftraw_datapoint) 
                FTDataptsCRUD.id = ftraw_datapoint.id
                FTDataptsCRUD.dataPointID = datapoint.id
                FTDataptsCRUD.dataPoint.dataEntityId = ftraw_datapoint.id
                FTDataptsCRUD.dataPoint.ftrawDataPointId = ftraw_datapoint.id
                FTDataptsCRUD.update()
                self.dataframe.loc[index, "id"] = FTDataptsCRUD.id
                self.dataframe.loc[index, "dataPointId"] = datapoint.id





class FTBinnedLengthsUploader(FTBinnedLengthData, Uploader):

    name = "FTBinnedLengthsData"

    def __init__(self, datapackageId, ftbinned_lengths_df):

        self.datapackageId = datapackageId 
        self.dataframe = ftbinned_lengths_df
        self.validated = False

    def validate(self):

        ft_list = {"dataPackage": DataPackage,
                   "dperErrorType": LErrorType 
                   }

        self.dataframe = Uploader._validate(self.dataframe, FTBinnedLengthDataSchema, ft_list)
        self.validated = True

    def get_unique_query(self, args):
        
        query = {"ftdataPointId.equals": args["ftdataPointId"]}
        return super().query(query)
    
    def upload(self, update=False, update_strategy="merge_keep"):
        
        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            args = self.dataframe.loc[index].to_dict()
            response = self.get_unique_query(args)
            records = response.json()

            if len(records) == 1:
                existing_id = records[0]["id"]
                old_args =  {k:v for k,v in records[0].items() if v is not None}
            else:
                existing_id = None

            if existing_id is None:
                obj = FTBinnedLengthData(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = FTBinnedLengthData(**args) 
                obj.update()

            self.dataframe.loc[index, "id"] = obj.id



class FTSingleGrainsUploader(FTSingleGrain, Uploader):

    name = "FTSingleGrainData"

    def __init__(self, datapackageId, ftsingle_grains_df):

        self.datapackageId = datapackageId 
        self.dataframe = ftsingle_grains_df
        self.validated = False

    def validate(self):

        ft_list = {"dataPackage": DataPackage,
                   "uErrorType": LErrorType,
                   "ageErrorType": LErrorType, 
                   }

        self.dataframe = Uploader._validate(self.dataframe, FTSingleGrainSchema, ft_list)
        self.validated = True

    def get_unique_query(self, args):
        
        query = {"ftdataPointId.equals": args["ftdataPointId"],
                 "grainName.equals": args["grainName"]}
        return super().query(query)
    
    def upload(self, update=False, update_strategy="merge_keep"):
        
        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            args = self.dataframe.loc[index].to_dict()
            response = self.get_unique_query(args)
            records = response.json()

            if len(records) == 1:
                existing_id = records[0]["id"]
                old_args =  {k:v for k,v in records[0].items() if v is not None}
            else:
                existing_id = None

            if existing_id is None:
                obj = FTSingleGrain(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = FTSingleGrain(**args) 
                obj.update()

            self.dataframe.loc[index, "id"] = obj.id


class FTCountDataUploader(FTCountData, Uploader):

    name = "FTCountData"

    def __init__(self, datapackageId, ftcount_data_df):

        self.datapackageId = datapackageId 
        self.dataframe = ftcount_data_df
        self.validated = False

    def validate(self):

        ft_list = {"dataPackage": DataPackage,
                   "dosimeter": LDosimeter,
                   "errorType": LErrorType, 
                   }

        self.dataframe = Uploader._validate(self.dataframe, FTCountDataSchema, ft_list)
        self.validated = True

    def get_unique_query(self, args):
        
        query = {"ftrawDataPointId.equals": args["ftrawDataPointId"],
                 "grainName.equals": args["grainName"]}
        return super().query(query)
    
    def upload(self, update=False, update_strategy="merge_keep"):
        
        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            args = self.dataframe.loc[index].to_dict()
            response = self.get_unique_query(args)
            records = response.json()

            if len(records) == 1:
                existing_id = records[0]["id"]
                old_args =  {k:v for k,v in records[0].items() if v is not None}
            else:
                existing_id = None

            if existing_id is None:
                obj = FTCountData(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = FTCountData(**args) 
                obj.update()

            self.dataframe.loc[index, "id"] = obj.id


class FTLengthDataUploader(FTSingleGrain, Uploader):

    name = "FTLengthData"

    def __init__(self, datapackageId, ftsingle_grains_df):

        self.datapackageId = datapackageId 
        self.dataframe = ftsingle_grains_df
        self.validated = False

    def validate(self):

        ft_list = {"dataPackage": DataPackage,
                   "errorType": LErrorType,
                   "trackType": LTrackType, 
                   }

        self.dataframe = Uploader._validate(self.dataframe, FTSingleGrainSchema, ft_list)
        self.validated = True

    def get_unique_query(self, args):
        
        query = {"ftdataPointId.equals": args["ftdataPointId"],
                 "grainName.equals": args["grainName"]}
        return super().query(query)
    
    def upload(self, update=False, update_strategy="merge_keep"):
        
        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            args = self.dataframe.loc[index].to_dict()
            response = self.get_unique_query(args)
            records = response.json()
            records = []

            if len(records) == 1:
                existing_id = records[0]["id"]
                old_args =  {k:v for k,v in records[0].items() if v is not None}
            else:
                existing_id = None

            if existing_id is None:
                obj = FTLengthData(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = FTLengthData(**args) 
                obj.update()

            self.dataframe.loc[index, "id"] = obj.id