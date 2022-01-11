import os
import numpy as np
import pandas as pd

from tqdm import tqdm
from .REST import APIRequests

class Uploader(object):

    def __init__(self, dataframe):

        self.dataframe = dataframe

    @staticmethod
    def _validate(dataframe, schema, lists=None):

        dataframe = schema.validate(dataframe)

        if lists:
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

    def save(self, outfile="output.xlsx"):
       
        kwargs = {}
        if os.path.isfile(outfile):
            kwargs["mode"] = "a"
            kwargs["if_sheet_exists"] = "replace"
        else:
            kwargs["mode"] = "w"

        with pd.ExcelWriter(outfile, **kwargs) as writer:  
            self.dataframe.to_excel(writer, sheet_name=self.name)

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