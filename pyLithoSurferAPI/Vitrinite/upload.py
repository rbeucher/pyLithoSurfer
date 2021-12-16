import os
import numpy as np
import pandas as pd
from pyLithoSurferAPI.management.tables import DataPackage
from pyLithoSurferAPI.core.tables import DataPoint
from pyLithoSurferAPI.core.lists import get_list_name_to_id_mapping as get_id
from pyLithoSurferAPI.Vitrinite.schemas import VitriniteDataPointSchema
from pyLithoSurferAPI.Vitrinite.VitriniteDataPoint import VitriniteDataPointCRUD, VitriniteDataPoint
from tqdm import tqdm


class VitriniteDataPointUploader(object):

    lists = {"dataPackage": DataPackage}

    def __init__(self, datapackageId, vitrinite_datapoints_df):

        self.datapackageId = datapackageId 
        self.dataframe = vitrinite_datapoints_df
        self.validated = False

    def upload(self, update=False, update_strategy="merge_keep"):
        
        print("Upload VitriniteDataPoints")

        if not self.validated:
            raise ValueError("Data not validated")

        self.vitrinite_datapoints_df["id"] = None

        for index in tqdm(self.vitrinite_datapoints_df.index):

            vitrinite_args = self.vitrinite_datapoints_df.loc[index].to_dict()
            sampleId = vitrinite_args.pop("sampleId")
            locationId = vitrinite_args.pop("locationId")
            if vitrinite_args.get("dataPointId"):
                vitrinite_args.pop("dataPointId")

            dpts_args = {"dataPackageId": self.datapackageId,
                         "dataStructure": "SIMPLE",
                         "dataEntityId": None,
                         "name": None,
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.sampleId.equals": sampleId,
                     "dataPointLithoCriteria.dataStructure.equals": "SIMPLE",
                     "dataPointLithoCriteria.dataPackageId.equals": self.datapackageId}

            response = VitriniteDataPointCRUD.query(query)
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

                # Create VitriniteDataPoint
                vitrinite_datapoint = VitriniteDataPoint(**vitrinite_args)

                try:
                    VitriniteDataptsCRUD = VitriniteDataPointCRUD(datapoint, vitrinite_datapoint) 
                    VitriniteDataptsCRUD.new() 
                
                    # Recover Datapoint
                    self.vitrinite_datapoints_df.loc[index, "id"] = VitriniteDataptsCRUD.id
                    self.vitrinite_datapoints_df.loc[index, "dataPointId"] = VitriniteDataptsCRUD.dataPoint.id

                except Exception as e:
                    self.errors_df.loc[index] = [datapoint.id, str(type(e))]                

            elif update:

                if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
                    raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")

                old_dpts_args = records[0]["dataPointDTO"]
                old_vitrinite_args = records[0]["vitriniteDataPointDTO"]
                old_dpts_args = {k:v for k,v in old_dpts_args.items() if v is not None}
                old_vitrinite_args = {k:v for k,v in old_vitrinite_args.items() if v is not None}

                if update_strategy == "merge_keep":
                    dpts_args.update(old_dpts_args)
                    vitrinite_args.update(old_vitrinite_args)
                
                if update_strategy == "merge_replace":
                    old_dpts_args.update(dpts_args)
                    old_vitrinite_args.update(vitrinite_args)
                    dpts_args = old_dpts_args
                    shrimp_dpts = old_vitrinite_args

                if update_strategy == "replace":
                    for key, val in old_dpts_args.items():
                        if key not in dpts_args.keys():
                            dpts_args[key] = None
                    for key, val in old_vitrinite_args.items():
                        if key not in vitrinite_args.keys():
                            shrimp_args[key] = None   

                dpts_args["id"] = old_dpts_args["id"]
                shrimp_args["id"] = old_vitrinite_args["id"]

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create VitriniteDataPoint
                vitrinite_datapoint = VitriniteDataPoint(**vitrinite_args)

                try:
                    VitriniteDataptsCRUD = VitriniteDataPointCRUD(datapoint, vitrinite_datapoint) 
                    VitriniteDataptsCRUD.id = vitrinite_datapoint.id
                    VitriniteDataptsCRUD.dataPointId = datapoint.id
                    VitriniteDataptsCRUD.dataPoint.dataEntityId = vitrinite_datapoint.id
                    VitriniteDataptsCRUD.dataPoint.shrimp_datapoint_id = vitrinite_datapoint.id
                    VitriniteDataptsCRUD.update()
                    self.vitrinite_datapoints_df.loc[index, "id"] = VitriniteDataptsCRUD.id
                    self.vitrinite_datapoints_df.loc[index, "dataPointId"] = datapoint.id

                except Exception as e:
                    self.errors_df.loc[index] = [datapoint.id, str(type(e))]
        
        
        if os.path.isfile("output.xlsx"):
            mode = "a"
        else:
            mode = "w"

        with pd.ExcelWriter('output.xlsx', mode=mode, if_sheet_exists="replace") as writer:  
            self.vitrinite_datapoints_df.to_excel(writer, sheet_name='VitriniteDataPoint')
            self.errors_df.to_excel(writer, sheet_name="VitriniteErrors")   


