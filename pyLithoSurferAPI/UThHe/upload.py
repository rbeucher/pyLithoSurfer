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
                                          LLambda)

from pyLithoSurferAPI.uploader import Uploader
from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm



class HeDataPointUploader(Uploader):

    name = "HeDataPoints"

    def __init__(self, datapackageId, he_datapoints_df):

        self.datapackageId = datapackageId 
        self.dataframe = he_datapoints_df
        self.validated = False

    def validate(self):

        he_list = {"dataPackage": DataPackage,
                   "alphaStopDistRef": LHeAlphaStopDistRef,
                   "correctedHeAgeMethod": LHeCorrectedAgeMethod,
                   "euequation": LHeeUEquation,
                   "ftEquation": LHeFTEquation,
                   "grainDimensionEquation": LHeGrainDimensionEq,
                   "heAgeEquation": LHeAgeEquation,
                   "meanCorrectedHeAgeError": LErrorType,
                   "meanUncorrectedHeAgeErrorType": LErrorType,
                   "mineral": Material,
                   "referenceMaterial": ReferenceMaterial,
                   "rftequation": LHeRFTEq,
                   "rsvequation": LHeRSVEq,
                   "weightedMeanCorrectedHeAgeErrorType": LErrorType,
                   "weightedMeanUncorrectedHeAgeErrorType": LErrorType
                   }

        self.dataframe = Uploader._validate(self.dataframe, HeDataPointSchema, he_list)
        self.validated = True

    def upload(self, update=False, update_strategy="replace"):
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            he_args = self.dataframe.loc[index].to_dict()
            sampleId = he_args.pop("sampleId")
            locationId = he_args.pop("locationId")
            if he_args.get("dataPointId"):
                he_args.pop("dataPointId")

            dpts_args = {"dataPackageId": self.datapackageId,
                         "dataStructure": "HE",
                         "dataEntityId": None,
                         "name": None,
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.dataStructure.equals": "HE",
                     "dataPointLithoCriteria.sampleId.equals": int(sampleId),
                     "dataPointLithoCriteria.dataPackageId.equals": self.datapackageId}

            response = HeDataPointCRUD.query(query)
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
                old_he_args = records[0]["ftdataPointDTO"]
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
                HeDataptsCRUD.dataPoint.ftdatapoint_id = he_datapoint.id
                HeDataptsCRUD.update()
                self.dataframe.loc[index, "id"] = HeDataptsCRUD.id
                self.dataframe.loc[index, "dataPointId"] = datapoint.id


class HeWholeGrainsUploader(HeWholeGrainCRUD, Uploader):

    name = "HeWholeGrain"

    def __init__(self, datapackageId, he_whole_grains_df):

        self.datapackageId = datapackageId 
        self.dataframe = he_whole_grains_df
        self.validated = False

    def validate(self):

        he_list = {"dataPackage": DataPackage,
                   "aliquotMassErrorType": LErrorType,
                   #"aliquotType": None,
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

        self.dataframe = Uploader._validate(self.dataframe, HeWholeGrainSchema, he_list)
        self.validated = True

    def get_unique_query(self, args):
        
        query = {"hedataPointId.equals": args["hedataPointId"],
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

            self.dataframe.loc[index, "id"] = obj.id


class HeInSituUploader(HeInSituCRUD, Uploader):

    name = "HeInSitu"

    def __init__(self, datapackageId, he_in_situ_df):

        self.datapackageId = datapackageId 
        self.dataframe = he_in_situ_df
        self.validated = False

    def validate(self):

        he_list = {"dataPackage": DataPackage,
                   "crysFrag": LHeCrysFrag,
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
                   "pitRelationship": None
                   }

        self.dataframe = Uploader._validate(self.dataframe, HeInSituSchema, he_list)
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

            self.dataframe.loc[index, "id"] = obj.id