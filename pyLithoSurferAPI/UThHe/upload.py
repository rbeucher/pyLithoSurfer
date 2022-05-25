from pyLithoSurferAPI.UThHe.schemas import HeDataPointSchema, HeInSituSchema, HeWholeGrainSchema
from pyLithoSurferAPI.core.lists import LErrorType, ReferenceMaterial

from pyLithoSurferAPI.core.tables import DataPoint, Material
from pyLithoSurferAPI.UThHe.tables import HeDataPoint, HeDataPointCRUD, HeWholeGrainCRUD, HeInSituCRUD
from pyLithoSurferAPI.UThHe.lists import (LHeAgeEquation,
                                          LHeAlphaStopDistRef,
                                          LHeCorrectedAgeMethod,
                                          LHeCrysFrag,
                                          LHeeUEquation,
                                          LHeFTEquation,
                                          LHeGrainDimensionEq,
                                          LHeGrainGeometry,
                                          LHeGrainMorphology,
                                          LHeRFTEq,
                                          LHeRSVEq,
                                          LPitRelationship,
                                          LHeAliquotType)

from pyLithoSurferAPI.uploader import Uploader
from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm
from datetime import datetime


class HeDataPointUploader(Uploader):

    name = "HeDataPoints"

    def __init__(self, he_datapoints_df, skip_columns=None):

        Uploader.__init__(self, he_datapoints_df)
        self.validated = False
        self.skip_columns = skip_columns


    def validate(self, lazy=False):

        he_list = {"dataPackage": DataPackage,
                   "alphaStopDistRef": LHeAlphaStopDistRef,
                   "correctedHeAgeMethod": LHeCorrectedAgeMethod,
                   "euequation": LHeeUEquation,
                   "ftEquation": LHeFTEquation,
                   "grainDimensionEquation": LHeGrainDimensionEq,
                   "heAgeEquation": LHeAgeEquation,
                   "meanCorrectedHeAgeErrorType": LErrorType,
                   "meanUncorrectedHeAgeErrorType": LErrorType,
                   "mineral": Material,
                   "referenceMaterial": ReferenceMaterial,
                   "rftequation": LHeRFTEq,
                   "rsvequation": LHeRSVEq,
                   "weightedMeanCorrectedHeAgeErrorType": LErrorType,
                   "weightedMeanUncorrectedHeAgeErrorType": LErrorType
                   }
        if self.skip_columns:
            skip_df = self.dataframe[[col for col in self.skip_columns if col in self.dataframe.columns]]
            self.dataframe = self.dataframe.drop(columns=[col for col in self.skip_columns if col in self.dataframe.columns])

        self.dataframe = Uploader._validate(self.dataframe, HeDataPointSchema, he_list, lazy=lazy)

        if self.skip_columns:
            for col in self.skip_columns:
                self.dataframe[col] = skip_df[col]  
       
        self.validated = True

    def upload(self, update=False, update_strategy="replace"):
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            he_args = self.dataframe.loc[index].to_dict()

            he_skip_args = {}
            for k, v in he_args.items():
                if self.skip_columns and k in self.skip_columns:
                    he_skip_args[k] = he_args[k]
            he_args = {k:v for k,v in he_args.items() if k not in he_skip_args.keys()}

            sampleId = he_args.pop("sampleId")
            locationId = he_args.pop("locationId")
            dataPackageId = he_args.pop("dataPackageId")

            if he_args.get("dataPointId"):
                he_args.pop("dataPointId")

            dpts_args = {"dataPackageId": dataPackageId,
                         "dataStructure": "HE",
                         "dataEntityId": None,
                         "name": None,
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.dataStructure.equals": "HE",
                     "dataPointLithoCriteria.sampleId.equals": int(sampleId),
                     "dataPointLithoCriteria.dataPackageId.equals": dataPackageId}

            if he_args["mineralId"]:
                query["mineralId.equals"] = int(he_args["mineralId"])

            # We should not use ages but that will do the job for the Canadian
            if ("meanCorrectedHeAge" in he_args.keys()) and he_args["meanCorrectedHeAge"]:
                query["meanCorrectedHeAge.greaterOrEqualThan"] = he_args["meanCorrectedHeAge"] - 0.001
                query["meanCorrectedHeAge.lessOrEqualThan"] = he_args["meanCorrectedHeAge"] + 0.001
            if ("meanUncorrectedHeAge" in he_args.keys()) and he_args["meanUncorrectedHeAge"]:
                query["meanUncorrectedHeAge.greaterOrEqualThan"] = he_args["meanUncorrectedHeAge"] - 0.001 
                query["meanUncorrectedHeAge.lessOrEqualThan"] = he_args["meanUncorrectedHeAge"] + 0.001

            response = HeDataPointCRUD.query(query)
            records = response.json()

            if len(records) == 1:
                existing_id = records[0]["id"]
            elif len(records) > 1:
                existing_id = records[0]["id"]
            else:
                existing_id = None

            if not dpts_args["name"]:
                dpts_args["name"] = f"Data Entry {str(datetime.now())}" 

            if existing_id is None:

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create FTDataPoint
                he_datapoint = HeDataPoint(**he_args)

                # Use FTDataPointCRUD to create the Datapoint and
                # the FTDatapoint
                HeDataptsCRUD = HeDataPointCRUD(datapoint, he_datapoint) 
                HeDataptsCRUD.new() 
                
                # Recover Datapoint
                self.dataframe.loc[index, "id"] = HeDataptsCRUD.id
                self.dataframe.loc[index, "dataPointId"] = HeDataptsCRUD.dataPoint.id

            elif update:

                old_dpts_args = records[0]["dataPointDTO"]
                dpts_args = self._update_args(old_dpts_args, dpts_args, update_strategy)
                old_he_args = records[0]["heDataPointDTO"]
                he_args = self._update_args(old_he_args, he_args, update_strategy)

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create FTDataPoint
                he_datapoint = HeDataPoint(**he_args)

                # Use FTDataPointCRUD to create the Datapoint and
                # the FTDatapoint
                HeDataptsCRUD = HeDataPointCRUD(datapoint, he_datapoint) 
                HeDataptsCRUD.id = he_datapoint.id
                HeDataptsCRUD.dataPointID = datapoint.id
                HeDataptsCRUD.dataPoint.dataEntityId = he_datapoint.id
                HeDataptsCRUD.dataPoint.heDataPointId = he_datapoint.id
                HeDataptsCRUD.update()

            index = HeDataptsCRUD.id
            self.dataframe_out.loc[index] = he_args
            self.dataframe_out.loc[index, "locationId"] = locationId
            self.dataframe_out.loc[index, "sampleId"] = sampleId
            self.dataframe_out.loc[index, "id"] = HeDataptsCRUD.id
            self.dataframe_out.loc[index, "dataPointId"] = datapoint.id
            for k, v in he_skip_args.items():
                self.dataframe_out.loc[index, k] = v  


class HeWholeGrainsUploader(HeWholeGrainCRUD, Uploader):

    name = "HeWholeGrain"

    def __init__(self, he_whole_grains_df):

        Uploader.__init__(self, he_whole_grains_df)
        self.validated = False

    def validate(self, lazy=False):

        he_list = {"aliquotMassErrorType": LErrorType,
                   "aliquotType": LHeAliquotType,
                   "crysFrag": LHeCrysFrag,
                   "euerrorType": LErrorType,
                   "ftErrorType": LErrorType,
                   "grainGeometry": LHeGrainGeometry,
                   "grainMorphology": LHeGrainMorphology,
                   "he4AmountErrorType": LErrorType,
                   "he4ConcentrationErrorType": LErrorType,
                   "smAmountErrorType": LErrorType,
                   "smConcentrationErrorType": LErrorType,
                   "tauErrorType": LErrorType,
                   "tauFTErrorType": LErrorType,
                   "thAmountErrorType": LErrorType,
                   "thConcentrationErrorType": LErrorType,
                   "uamountErrorType": LErrorType,
                   "uconcentrationErrorType": LErrorType,
                   "uncorrectedHeAgeErrorTyp": LErrorType,
                   "zrContentErrorType": LErrorType
                   }

        self.dataframe = Uploader._validate(self.dataframe, HeWholeGrainSchema, he_list, lazy=lazy)
        self.validated = True

    def get_unique_query(self, args):
        
        query = {"heDataPointId.equals": int(args["heDataPointId"]),
                 "aliquotID.equals": args["aliquotID"]}
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
                obj = HeWholeGrainCRUD(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = HeWholeGrainCRUD(**args) 
                obj.update()

            index = obj.id
            self.dataframe_out.loc[index] = args
            self.dataframe_out.loc[index, "id"] = obj.id


class HeInSituUploader(HeInSituCRUD, Uploader):

    name = "HeInSitu"

    def __init__(self, he_in_situ_df):

        Uploader.__init__(self, he_in_situ_df)
        self.validated = False

    def validate(self, lazy=False):

        he_list = {"crysFrag": LHeCrysFrag,
                   "he4AmountErrorType": LErrorType,
                   "he4ConcentrationErrorType": LErrorType,
                   "parentPitVolumeErrorType": LErrorType,
                   "pitVolumeErrorType": LErrorType,
                   "smAmountErrorType": LErrorType,
                   "smConcentrationErrorType": LErrorType,
                   "tauErrorType": LErrorType,
                   "thAmountErrorType": LErrorType,
                   "thConcentrationErrorType": LErrorType,
                   "uamountErrorType": LErrorType,
                   "uconcentrationErrorType": LErrorType,
                   "uncorrectedHeAgeErrorType": LErrorType,
                   "euerrorType": LErrorType,
                   "pitRelationship": LPitRelationship
                   }

        self.dataframe = Uploader._validate(self.dataframe, HeInSituSchema, he_list, lazy=lazy)
        self.validated = True

    def get_unique_query(self, args):
        return []
    
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
                obj = HeInSituCRUD(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = HeInSituCRUD(**args) 
                obj.update()

            index = obj.id
            self.dataframe_out.loc[index] = args
            self.dataframe_out.loc[index, "id"] = obj.id