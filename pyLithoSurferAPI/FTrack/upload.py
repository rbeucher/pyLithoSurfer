import os

import numpy as np
import pandas as pd

from pyLithoSurferAPI.FTrack.schemas import FTDataPointSchema
from pyLithoSurferAPI.core.lists import get_list_name_to_id_mapping as get_id

from pyLithoSurferAPI.core.tables import DataPoint
from pyLithoSurferAPI.FTrack.tables import FTDataPoint, FTDataPointCRUD

from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm



class FTDataPointUploader(object):

    def __init__(self, datapackageId, ft_datapoints_df):

        self.datapackageId = datapackageId 
        self.ft_datapoints_df = ft_datapoints_df
        self.validated = False

    def validate(self):

        self.ft_datapoints_df = FTDataPointSchema.validate(self.ft_datapoints_df)

        if "dataPackageId" not in self.ft_datapoints_df.columns:
            if "dataPackageName" in self.ft_datapoints_df.columns:
                self.ft_datapoints_df["dataPackageId"] = self.ft_datapoints_df.dataPackageName.map(get_id(DataPackage))
        
        self.ft_datapoints_df = self.ft_datapoints_df.replace({np.nan: None})
        self.ft_datapoints_df = FTDataPointSchema.validate(self.ft_datapoints_df)
        self.ft_datapoints_df = self.ft_datapoints_df.astype(object).where(pd.notnull(self.ft_datapoints_df), None)
        self.validated = True

    def upload(self, update=False, update_strategy="merge_keep"):
        
        print("Upload FTDataPoints")

        if not self.validated:
            raise ValueError("Data not validated")

        self.ft_datapoints_df["id"] = None
        self.errors_df = pd.DataFrame(columns=["id", "exception"])


        for index in tqdm(self.ft_datapoints_df.index):

            ft_args = self.ft_datapoints_df.loc[index].to_dict()
            sampleId = ft_args.pop("sampleId")
            locationId = ft_args.pop("locationId")
            if ft_args.get("dataPointId"):
                ft_args.pop("dataPointId")

            dpts_args = {"dataPackageId": self.datapackageId,
                         "dataStructure": "FTRACK",
                         "dataEntityId": None,
                         "name": None,
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.sampleId.equals": sampleId,
                     "dataPointLithoCriteria.dataStructure.equals": "FTRACK",
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

                try:
                    # Use FTDataPointCRUD to create the Datapoint and
                    # the FTDatapoint
                    FTDataptsCRUD = FTDataPointCRUD(datapoint, ft_datapoint) 
                    FTDataptsCRUD.new() 
                
                    # Recover Datapoint
                    self.ft_datapoints_df.loc[index, "id"] = FTDataptsCRUD.id
                    self.ft_datapoints_df.loc[index, "dataPointId"] = FTDataptsCRUD.dataPoint.id

                except Exception as e:
                    self.errors_df.loc[index] = [datapoint.id, str(type(e))]                

            elif update:

                if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
                    raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")

                old_dpts_args = records[0]["dataPointDTO"]
                old_ft_args = records[0]["ftdataPointDTO"]
                old_dpts_args = {k:v for k,v in old_dpts_args.items() if v is not None}
                old_ft_args = {k:v for k,v in old_ft_args.items() if v is not None}

                if update_strategy == "merge_keep":
                    dpts_args.update(old_dpts_args)
                    ft_args.update(old_ft_args)
                
                if update_strategy == "merge_replace":
                    old_dpts_args.update(dpts_args)
                    old_ft_args.update(ft_args)
                    dpts_args = old_dpts_args
                    ft_dpts = old_ft_args

                if update_strategy == "replace":
                    for key, val in old_dpts_args.items():
                        if key not in dpts_args.keys():
                            dpts_args[key] = None
                    for key, val in old_ft_args.items():
                        if key not in ft_args.keys():
                            ft_args[key] = None   

                dpts_args["id"] = old_dpts_args["id"]
                ft_args["id"] = old_ft_args["id"]

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create FTDataPoint
                ft_datapoint = FTDataPoint(**ft_args)

                try:
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

                except Exception as e:
                    self.errors_df.loc[index] = [datapoint.id, str(type(e))]
        
        
        if os.path.isfile("output.xlsx"):
            mode = "a"
        else:
            mode = "w"

        with pd.ExcelWriter('output.xlsx', mode=mode, if_sheet_exists="replace") as writer:  
            self.ft_datapoints_df.to_excel(writer, sheet_name='FTDataPoint')
            self.errors_df.to_excel(writer, sheet_name="FTErrors")   