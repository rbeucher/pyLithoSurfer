from pyLithoSurferAPI.FTrack.schemas import FTBinnedLengthDataSchema, FTCountDataSchema, FTDataPointSchema, FTLengthDataSchema, FTSingleGrainSchema
from pyLithoSurferAPI.core.lists import LErrorType, ReferenceMaterial

from pyLithoSurferAPI.core.tables import DataPoint, Material, Machine
from pyLithoSurferAPI.FTrack.tables import FTBinnedLengthDataCRUD, FTCountDataCRUD, FTDataPoint, FTDataPointCRUD, FTLengthDataCRUD, FTSingleGrainCRUD
from pyLithoSurferAPI.FTrack.lists import (LFTPopulationType, LFTUDeterminationTechnique, 
                                           LDosimeter,
                                           LEtchant,
                                           LFTAgeEquation,
                                           LFTCharacterisationMethod, LFTAnalyticalSoftware, LFTAnalyticalAlgorithm,
                                           LIrradiationReactor,
                                           LLambdaF, LLambda, LRmr0Equation, LTrackType)

from pyLithoSurferAPI.uploader import Uploader
from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm



class FTDataPointUploader(Uploader):

    name = "FTDataPoints"

    def __init__(self, ft_datapoints_df, skip_columns=None):

        Uploader.__init__(self, ft_datapoints_df)
        
        self.validated = False
        self.skip_columns = skip_columns

    def validate(self, lazy=False):

        ft_list = {"dataPackage": DataPackage,
                   "ageUncertaintyType": LErrorType,
                   "dosimeter": LDosimeter,
                   "etchant": LEtchant,
                   "ftUDeterminationTechnique": LFTUDeterminationTechnique,
                   "ftAgeEquation": LFTAgeEquation,
                   "ftCharacterisationMethod": LFTCharacterisationMethod,
                   "ftAnalyticalSoftwareName" : LFTAnalyticalSoftware,
                   "ftAnalyticalAlgorithm": LFTAnalyticalAlgorithm,
                   "irradiationReactor": LIrradiationReactor,
                   "lambdaF": LLambdaF,
                   "lambda": LLambda,
                   "machine": Machine,
                   "mineral": Material,
                   "referenceMaterial": ReferenceMaterial,
                   "rmr0Equation": LRmr0Equation,
                   "zetaUncertaintyType": LErrorType,
                   "popType": LFTPopulationType
                   }
        if self.skip_columns:
            skip_df = self.dataframe[[col for col in self.skip_columns if col in self.dataframe.columns]]
            self.dataframe = self.dataframe.drop(columns=[col for col in self.skip_columns if col in self.dataframe.columns])
        
        self.dataframe = Uploader._validate(self.dataframe, FTDataPointSchema, ft_list, lazy=lazy)
        
        if self.skip_columns:
            for col in self.skip_columns:
                self.dataframe[col] = skip_df[col]     

        self.validated = True

    def upload(self, update=False, update_strategy="replace"):
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            ft_args = self.dataframe.loc[index].to_dict()

            ft_skip_args = {}
            for k, v in ft_args.items():
                if self.skip_columns and k in self.skip_columns:
                    ft_skip_args[k] = ft_args[k]
            ft_args = {k:v for k,v in ft_args.items() if k not in ft_skip_args.keys()}

            sampleId = ft_args.pop("sampleId")
            locationId = ft_args.pop("locationId")
            dataPackageId = ft_args.pop("dataPackageId")

            if ft_args.get("dataPointId"):
                ft_args.pop("dataPointId")

            dpts_args = {"dataPackageId": dataPackageId,
                         "dataStructure": "FT",
                         "dataEntityId": None,
                         "name": None,
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.dataStructure.equals": "FT",
                     "dataPointLithoCriteria.sampleId.equals": int(sampleId),
                     "dataPointLithoCriteria.dataPackageId.equals": dataPackageId}

            if ft_args["mineralId"]:
                query["mineralId.equals"] = int(ft_args["mineralId"])
            if ft_args["ftAgeEquationId"]:
                query["ftAgeEquationId.equals"] = int(ft_args["ftAgeEquationId"])
            if ft_args["ftUDeterminationTechniqueId"]:
                query["ftUDeterminationTechniqueID.equals"] = int(ft_args["ftUDeterminationTechniqueId"])
            if "mountIdCount" in ft_args.keys() and ft_args["mountIDCount"]:
                query["mountIDCount.equals"] = ft_args["mountIDCount"]
            
            # Note that these are probably temporary...
            if ft_args["population"]:
                query["population.equals"] = int(ft_args["population"])
            if ft_args["popTypeId"]:
                query["popTypeId.equals"] = int(ft_args["popTypeId"])           

            # We should not use ages but that will do the job for the Canadian
            if ft_args["meanAgeMa"]:
                query["meanAgeMa.greaterOrEqualThan"] = ft_args["meanAgeMa"]  - 0.001
                query["meanAgeMa.lessOrEqualThan"] = ft_args["meanAgeMa"]  + 0.001
            if ft_args["meanAgeUncertaintyMa"]:
                query["meanAgeUncertaintyMa.greaterOrEqualThan"] = ft_args["meanAgeUncertaintyMa"] - 0.01                      
                query["meanAgeUncertaintyMa.lessOrEqualThan"] = ft_args["meanAgeUncertaintyMa"] + 0.01                      
            if ft_args["centralAgeMa"]:
                query["centralAgeMa.greaterOrEqualThan"] = ft_args["centralAgeMa"] - 0.01    
                query["centralAgeMa.lessOrEqualThan"] = ft_args["centralAgeMa"] + 0.01    
            if ft_args["centralAgeUncertaintyMa"]:
                query["centralAgeUncertaintyMa.greaterOrEqualThan"] = ft_args["centralAgeUncertaintyMa"] - 0.01                       
                query["centralAgeUncertaintyMa.lessOrEqualThan"] = ft_args["centralAgeUncertaintyMa"] + 0.01                      
            if ft_args["pooledAgeMa"]:
                query["pooledAgeMa.greaterOrEqualThan"] = ft_args["pooledAgeMa"] - 0.01     
                query["pooledAgeMa.lessOrEqualThan"] = ft_args["pooledAgeMa"] + 0.01    
            if ft_args["pooledAgeUncertaintyMa"]:
                query["pooledAgeUncertaintyMa.greaterOrEqualThan"] = ft_args["pooledAgeUncertaintyMa"] - 0.01 
                query["pooledAgeUncertaintyMa.lessOrEqualThan"] = ft_args["pooledAgeUncertaintyMa"] + 0.01

            response = FTDataPointCRUD.query(query)
            records = response.json()

            if len(records) == 1:
                existing_id = records[0]["id"]
            elif len(records) > 1:
                print("Multiple Entries possible")
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

            index = FTDataptsCRUD.id
            self.dataframe_out.loc[index] = ft_args
            self.dataframe_out.loc[index, "locationId"] = locationId
            self.dataframe_out.loc[index, "sampleId"] = sampleId
            self.dataframe_out.loc[index, "id"] = FTDataptsCRUD.id
            self.dataframe_out.loc[index, "dataPointId"] = datapoint.id
            for k, v in ft_skip_args.items():
                self.dataframe_out.loc[index, k] = v       


class FTBinnedLengthsUploader(FTBinnedLengthDataCRUD, Uploader):

    name = "FTBinnedLengthsData"

    def __init__(self, ftbinned_lengths_df):

        Uploader.__init__(self, ftbinned_lengths_df)

        self.validated = False

    def validate(self, lazy=False):

        ft_list = { "dperErrorType": LErrorType }

        self.dataframe = Uploader._validate(self.dataframe, FTBinnedLengthDataSchema, ft_list, lazy=lazy)
        self.validated = True

    def get_unique_query(self, args):
        
        query = {"FTDataPointId.equals": int(args["ftdataPointId"])}
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
                obj = FTBinnedLengthDataCRUD(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = FTBinnedLengthDataCRUD(**args)
                obj.update()

            index = obj.id
            self.dataframe_out.loc[index] = args
            self.dataframe_out.loc[index, "id"] = obj.id



class FTSingleGrainsUploader(FTSingleGrainCRUD, Uploader):

    name = "FTSingleGrainData"

    def __init__(self, ftsingle_grains_df):

        Uploader.__init__(self, ftsingle_grains_df)

        self.validated = False

    def validate(self, lazy=False):

        ft_list = {"uErrorType": LErrorType,
                   "ageErrorType": LErrorType, 
                   }

        self.dataframe = Uploader._validate(self.dataframe, FTSingleGrainSchema, ft_list, lazy=lazy)
        self.validated = True

    def get_unique_query(self, args):

        query = {"FTDataPointId.equals": int(args["ftdataPointId"]),
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
                obj = FTSingleGrainCRUD(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = FTSingleGrainCRUD(**args) 
                obj.update()

            index = obj.id
            self.dataframe_out.loc[index] = args
            self.dataframe_out.loc[index, "id"] = obj.id


class FTCountDataUploader(FTCountDataCRUD, Uploader):

    name = "FTCountData"

    def __init__(self, ftcount_data_df):

        Uploader.__init__(self, ftcount_data_df)
        self.validated = False

    def validate(self, lazy=False):

        ft_list = {"errorType": LErrorType}

        self.dataframe = Uploader._validate(self.dataframe, FTCountDataSchema, ft_list, lazy=lazy)
        self.validated = True

    def get_unique_query(self, args):
        
        query = {"FTDataPointId.equals": int(args["ftdataPointId"]),
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
                obj = FTCountDataCRUD(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = FTCountDataCRUD(**args) 
                obj.update()

            index = obj.id
            self.dataframe_out.loc[index] = args
            self.dataframe_out.loc[index, "id"] = obj.id


class FTLengthDataUploader(FTLengthDataCRUD, Uploader):

    name = "FTLengthData"

    def __init__(self, ftlengthdata_df):

        Uploader.__init__(self, ftlengthdata_df)
        self.validated = False

    def validate(self, lazy=False):

        ft_list = {"errorType": LErrorType,
                   "trackType": LTrackType, 
                   }

        self.dataframe = Uploader._validate(self.dataframe, FTLengthDataSchema, ft_list, lazy=lazy)
        self.validated = True

    def get_unique_query(self, args):
        
        query = {"FTDataPointId.equals": int(args["ftdataPointId"]),
                 "grainName.equals": args["grainName"],
                 "trackID.equals": args["trackID"]}
                 
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
                obj = FTLengthDataCRUD(**args) 
                obj.new() 

            elif update:
                args = self._update_args(old_args, args, update_strategy)
                obj = FTLengthDataCRUD(**args) 
                obj.update()

            index = obj.id
            self.dataframe_out.loc[index] = args
            self.dataframe_out.loc[index, "id"] = obj.id