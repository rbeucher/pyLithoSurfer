import os

import numpy as np
import pandas as pd
from pyLithoSurferAPI.core.lists import (LErrorType, LGeoEvent, LSHRIMPAgeType,
                                         LSHRIMPSampleFormat, LSHRIMPAgeGroup,
                                         LMachineType)
from pyLithoSurferAPI.core.lists import get_list_name_to_id_mapping as get_id
from pyLithoSurferAPI.core.tables import (DataPoint, GeoeventAtAge, Material,
                                          Statement)
from pyLithoSurferAPI.core.upload import SampleWithLocationUploader
from pyLithoSurferAPI.SHRIMPModel.schemas import (SHRIMPAgeSchema,
                                                  SHRIMPDataPointSchema)
from pyLithoSurferAPI.SHRIMPModel.SHRIMPAge import SHRIMPAge, SHRIMPAgeCRUD
from pyLithoSurferAPI.SHRIMPModel.SHRIMPDataPoint import (SHRIMPDataPoint,
                                                          SHRIMPDataPointCRUD)

from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm


class SHRIMPDataPointUploader(object):

    def __init__(self, datapackageId, shrimp_datapoints_df):

        self.datapackageId = datapackageId 
        self.shrimp_datapoints_df = shrimp_datapoints_df
        self.validated = False

    def validate(self):

        self.shrimp_datapoints_df = SHRIMPDataPointSchema.validate(self.shrimp_datapoints_df)

        if "dataPackageId" not in self.shrimp_datapoints_df.columns:
            if "dataPackageName" in self.shrimp_datapoints_df.columns:
                self.shrimp_datapoints_df["dataPackageId"] = self.shrimp_datapoints_df.dataPackageName.map(get_id(DataPackage))
        
        if "mineralOfInterestId" not in self.shrimp_datapoints_df.columns:
            if "mineralOfInterestName" in self.shrimp_datapoints_df.columns:
                materials = self.shrimp_datapoints_df.mineralOfInterestName.unique()
                mapping = {}
                for material in materials:
                    mapping[material] = Material.get_id_from_name(material)
                mapping["Unknown"] = None
                self.shrimp_datapoints_df["mineralOfInterestId"] = self.shrimp_datapoints_df.mineralOfInterestName.map(mapping)

        if "sampleFormatId" not in self.shrimp_datapoints_df.columns:
            if "sampleFormatName" in self.shrimp_datapoints_df.columns:
                self.shrimp_datapoints_df["sampleFormatId"] = self.shrimp_datapoints_df.sampleFormatName.map(get_id(LSHRIMPSampleFormat))
            else:
                self.shrimp_datapoints_df["sampleFormatId"] = LSHRIMPSampleFormat.get_id_from_name("Unknown")
                self.shrimp_datapoints_df["sampleFormatName"] = "Unknown"

        if "machineId" not in self.shrimp_datapoints_df.columns:
            if "machineName" in self.shrimp_datapoints_df.columns:
                self.shrimp_datapoints_df["machineId"] = self.shrimp_datapoints_df.machineName.map(get_id(LMachineType))
            else:
                self.shrimp_datapoints_df["machineId"] = LMachineType.get_id_from_name("Unknown")
                self.shrimp_datapoints_df["machineName"] = "Unknown"

        self.shrimp_datapoints_df = self.shrimp_datapoints_df.replace({np.nan: None})
        self.shrimp_datapoints_df = SHRIMPDataPointSchema.validate(self.shrimp_datapoints_df)
        self.shrimp_datapoints_df = self.shrimp_datapoints_df.where(pd.notnull(self.shrimp_datapoints_df), None)
        self.validated = True

    def upload(self, update=False, update_strategy="merge_keep"):
        
        print("Upload SHRIMPDataPoints")

        if not self.validated:
            raise ValueError("Data not validated")

        self.shrimp_datapoints_df["id"] = None
        self.errors_df = pd.DataFrame(columns=["id", "exception"])


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
                query["mountIdentifier"] = shrimp_args["mountIdentifier"]

        
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

                try:
                    # Use SHRIMPDataPointCRUD to create the Datapoint and
                    # the SHRIMPDatapoint
                    SHRIMPDataptsCRUD = SHRIMPDataPointCRUD(datapoint, shrimp_datapoint) 
                    SHRIMPDataptsCRUD.new() 
                
                    # Recover Datapoint
                    self.shrimp_datapoints_df.loc[index, "id"] = SHRIMPDataptsCRUD.id
                    self.shrimp_datapoints_df.loc[index, "dataPointId"] = SHRIMPDataptsCRUD.dataPoint.id

                except Exception as e:
                    self.errors_df.loc[index] = [datapoint.id, str(type(e))]                

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
                    SHRIMPDataptsCRUD.dataPoint.dataEntityId = shrimp_datapoint.id
                    SHRIMPDataptsCRUD.dataPoint.shrimp_datapoint_id = shrimp_datapoint.id
                    SHRIMPDataptsCRUD.update()
                    self.shrimp_datapoints_df.loc[index, "id"] = SHRIMPDataptsCRUD.id
                    self.shrimp_datapoints_df.loc[index, "dataPointId"] = datapoint.id

                except Exception as e:
                    self.errors_df.loc[index] = [datapoint.id, str(type(e))]
        
        
        if os.path.isfile("output.xlsx"):
            mode = "a"
        else:
            mode = "w"

        with pd.ExcelWriter('output.xlsx', mode=mode) as writer:  
            self.shrimp_datapoints_df.to_excel(writer, sheet_name='SHRIMPDataPoint')
            self.errors_df.to_excel(writer, sheet_name="ShrimpErrors")   



class SHRIMPAgeUploader(SHRIMPDataPointUploader):

    shrimp_age_keys = ["ageGroupId", "ageGroupName", "ageTypeId",
     "ageTypeName", "calcName", "id", "mswd",
     "numberAnalysesCombined", "rmQcTest"]

    statement_keys = ["calculatedConfidence", "dataPointId", "description",
     "geoEventAtAgeId", "humanConfidence", "statementId",
     "relevance", "tempAtAgeId", "tempGradientId"] 

    geoEvent_keys = ["age", "ageError", "errorTypeId", "errorTypeName",
    "geoEventId", "geoEventName"]
    
    def __init__(self, datapackageId, shrimp_ages_df):

        self.datapackageId = datapackageId 
        self.shrimp_ages_df = shrimp_ages_df
        self.validated = False

    def validate(self):

        self.shrimp_ages_df.dropna(subset=["age"], inplace=True)
        self.shrimp_ages_df = SHRIMPAgeSchema.validate(self.shrimp_ages_df)

        if "errorTypeId" not in self.shrimp_ages_df.columns:
            if "errorTypeName" in self.shrimp_ages_df.columns:
                self.shrimp_ages_df["errorTypeId"] = self.shrimp_ages_df.errorTypeName.map(get_id(LErrorType))
            else:
                self.shrimp_ages_df["errorTypeId"] = LErrorType.get_id_from_name("Unknown")
                self.shrimp_ages_df["errorTypeName"] = "Unknown"
        
        if "geoEventId" not in self.shrimp_ages_df.columns:
            if "geoEventName" in self.shrimp_ages_df.columns:
                events = self.shrimp_ages_df.geoEventName.unique()
                mapping = {}
                for event in events:
                    mapping[event] = LGeoEvent.get_id_from_name(event)
                self.shrimp_ages_df["geoEventId"] = self.shrimp_ages_df.geoEventName.map(mapping)
            else:
                self.shrimp_ages_df["geoEventId"] = LGeoEvent.get_id_from_name("Unknown")
                self.shrimp_ages_df["geoEventName"] = "Unknown"
        
        if "ageTypeId" not in self.shrimp_ages_df.columns:
            if "ageTypeName" in self.shrimp_ages_df.columns:
                self.shrimp_ages_df["ageTypeId"] = self.shrimp_ages_df.ageTypeName.map(get_id(LSHRIMPAgeType))
            else:
                self.shrimp_ages_df["ageTypeId"] = LSHRIMPAgeType.get_id_from_name("Unknown date")
                self.shrimp_ages_df["ageTypeName"] = "Unknown date"
        
        if "ageGroupId" not in self.shrimp_ages_df.columns:
            if "ageGroupName" in self.shrimp_ages_df.columns:
                self.shrimp_ages_df["ageGroupId"] = self.shrimp_ages_df.ageGroupName.map(get_id(LSHRIMPAgeGroup))
            else:
                self.shrimp_ages_df["ageGroupId"] = LSHRIMPAgeGroup.get_id_from_name("Z (undefined)")
                self.shrimp_ages_df["ageGroupName"] = "Z (undefined)"

        self.shrimp_ages_df = SHRIMPAgeSchema.validate(self.shrimp_ages_df)
        self.shrimp_ages_df = self.shrimp_ages_df.where(pd.notnull(self.shrimp_ages_df), None)

    def upload(self, update=False, update_strategy="merge_keep"):
        
        self.shrimp_ages_df["id"] = None
        self.errors_df = pd.DataFrame(columns=["id", "exception"])
       
        print("Upload SHRIMPAges")

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
            
                try:
                    # Use SHRIMPAgeCRUD to create the Statement and the SHRIMPAge and
                    # the GeoEvent
                    shrimp_age_crud = SHRIMPAgeCRUD(geo_event, statement, shrimp_age)
                    shrimp_age_crud.new()
                    self.shrimp_ages_df.loc[index, "id"] = shrimp_age_crud.id

                except Exception as e:
                    self.errors_df.loc[index] = [self.id, str(type(e))]

            elif update:

                if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
                    raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")
                
                old_stat_args = records[0]["geoEventAtAgeExtendsStatementDTO"]["statementDTO"]
                old_event_args = records[0]["geoEventAtAgeExtendsStatementDTO"]["geoEventAtAgeDTO"]
                old_shrimp_age_args = records[0]["shrimpageDTO"]
                
                old_stat_args = {k:v for k,v in old_stat_args.items() if v is not None}
                old_event_args = {k:v for k,v in old_event_args.items() if v is not None}
                old_shrimp_age_args = {k:v for k,v in old_shrimp_age_args.items() if v is not None}

                if update_strategy == "merge_keep":
                    stat_args.update(old_stat_args)
                    event_args.update(old_event_args)
                    shrimp_age_args.update(old_shrimp_age_args)
                
                if update_strategy == "merge_replace":
                    old_stat_args.update(stat_args)
                    old_event_args.update(event_args)
                    old_shrimp_age_args.update(shrimp_age_args)
                    stat_args = old_stat_args
                    shrimp_dpts = old_event_args
                    shrimp_age = shrimp_age_args

                if update_strategy == "replace":
                    for key, val in old_stat_args.items():
                        if key not in stat_args.keys():
                            stat_args[key] = None
                    for key, val in old_event_args.items():
                        if key not in event_args.keys():
                            event_args[key] = None   
                    for key, val in old_shrimp_age_args.items():
                        if key not in shrimp_age_args.keys():
                            shrimp_age_args[key] = None   

                stat_args["id"] = old_stat_args["id"]
                event_args["id"] = old_event_args["id"]
                shrimp_age_args["id"] = old_shrimp_age_args["id"]

                try:

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

                except Exception as e:
                    self.errors_df.loc[index] = [index, str(type(e))]

        if os.path.isfile("output.xlsx"):
            mode = "a"
        else:
            mode = "w"

        with pd.ExcelWriter('output.xlsx', mode='a') as writer:  
            self.shrimp_ages_df.to_excel(writer, sheet_name='SHRIMPAge')
            self.errors_df.to_excel(writer, sheet_name="ShrimpAgeErrors")   

