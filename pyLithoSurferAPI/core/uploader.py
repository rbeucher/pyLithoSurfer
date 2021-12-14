import os

import numpy as np
import pandas as pd

from pyLithoSurferAPI.core.lists import get_list_name_to_id_mapping as get_id
from pyLithoSurferAPI.core.schemas import DataPointSchema
from pyLithoSurferAPI.core.tables import DataPoint
from pyLithoSurferAPI.management.tables import DataPackage

from tqdm import tqdm


class Uploader(object):

    @staticmethod
    def validate(dataframe, schema, lists=None):

        dataframe = schema.validate(dataframe)

        for key, val in lists.items():
            if key + "Id" not in dataframe.columns:
                if key + "Name" in dataframe.columns:
                    uniques = dataframe[key + "Name"].unique()
                    mapping = {}
                    for unique in uniques:
                        mapping[unique] = val.get_id_from_name(unique)
                    dataframe[key + "Id"] = dataframe[key + "Name"].map(mapping)
        
        dataframe = dataframe.replace({np.nan: None})
        dataframe = schema.validate(dataframe)
        return dataframe.astype(object).where(pd.notnull(dataframe), None)

    def get_unique_query(self, args):
        return {}

    def upload(self, update=False, update_strategy="merge_keep"):
        
        self.dataframe["id"] = None
        self.errors_df = pd.DataFrame(columns=["id", "exception"])

        for index in tqdm(self.dataframe.index):

            args = self.dataframe.loc[index].to_dict()
            response = self.query(self.get_unique_query(args))
            records = response.json()

            if len(records) == 1:
                existing_id = records[0]["id"]
                old_args =  {k:v for k,v in records[0].items() if v is not None}
            else:
                existing_id = None

            if existing_id is None:
                obj = self(**args) 
                obj.new() 

            elif update:
                dtp_args = self._update_args(old_args, args, update_strategy)
                obj = self(**args) 
                obj.update()

            self.dataframe.loc[index, "id"] = obj.id
            self.dataframe.loc[index, "dataPointId"] = obj.dataPoint.id

    def save_dataframe(self, outfile="output.xlsx"):
       
        if os.path.isfile(outfile):
            mode = "a"
        else:
            mode = "w"

        with pd.ExcelWriter(outfile, mode=mode, if_sheet_exists="replace") as writer:  
            self.dataframe.to_excel(writer, sheet_name=self.name)
            self.errors_df.to_excel(writer, sheet_name=self.name+"Errors")  

    def _update_args(self, old_args, new_args, update_strategy):

        if update_strategy not in ["merge_keep", "merge_replace", "replace"]:
            raise ValueError(f"Update strategy must be 'replace', 'merge_keep', 'merge_replace'")

        old_args = {k:v for k,v in old_args.items() if v is not None}

        if update_strategy == "merge_keep":
            return new_args.update(old_args)
        
        if update_strategy == "merge_replace":
            new_args["id"] = old_args["id"]
            return old_args.update(new_args)

        if update_strategy == "replace":
            for key, val in old_args.items():
                if key not in new_args.keys():
                    new_args[key] = None
            new_args["id"] = old_args["id"]
            return new_args 