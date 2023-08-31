from pyLithoSurferAPI.ThermalHistories.schemas import THDataPointSchema, THDataPointBatchSchema
from pyLithoSurferAPI.REST import APIRequests

from pyLithoSurferAPI.core.tables import DataPoint
from pyLithoSurferAPI.ThermalHistories.tables import THDataPoint, THDataPointCRUD
from pyLithoSurferAPI.ThermalHistories.lists import (LModelType,
                                                     LModelApproach,
                                                     LModelSoftware)

from pyLithoSurferAPI.uploader import Uploader
from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import numpy as np
import pandas as pd


class THDataPointUploader(Uploader):

    name = "THDataPoints"

    def __init__(self, th_datapoints_df, skip_columns=None):

        Uploader.__init__(self, th_datapoints_df)

        self.validated = False
        self.skip_columns = skip_columns


    def validate(self, lazy=False):

        th_list = {"dataPackage": DataPackage,
                   "modelType": LModelType,
                   "modelSoftware": LModelSoftware,
                   "modelApproach": LModelApproach}
        if self.skip_columns:
            skip_df = self.dataframe[[col for col in self.skip_columns if col in self.dataframe.columns]]
            self.dataframe = self.dataframe.drop(columns=[col for col in self.skip_columns if col in self.dataframe.columns])

        self.dataframe = Uploader._validate(self.dataframe, THDataPointSchema, th_list, lazy=lazy)

        if self.skip_columns:
            for col in self.skip_columns:
                self.dataframe[col] = skip_df[col]  
       
        self.validated = True

    def upload(self, update=False, update_strategy="replace"):
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            th_args = self.dataframe.loc[index].to_dict()

            th_skip_args = {}
            for k, v in th_args.items():
                if self.skip_columns and k in self.skip_columns:
                    th_skip_args[k] = th_args[k]
            th_args = {k:v for k,v in th_args.items() if k not in th_skip_args.keys()}

            dataPackageId = th_args.pop("dataPackageId")
            description = th_args.pop("description") if "description" in th_args.keys() else ""

            if th_args.get("dataPointId"):
                th_args.pop("dataPointId")

            dpts_args = {"dataPackageId": dataPackageId,
                         "dataStructure": "TH",
                         "dataEntityId": None,
                         "name": f"Data Entry {str(datetime.now())}",
                         "description": description}
            
            query = {"dataPointLithoCriteria.dataStructure.equals": "TH",
                     "dataPointLithoCriteria.dataPackageId.equals": dataPackageId}

            if "mineralId" in th_args.keys():
                query["mineralId.equals"] = int(th_args["mineralId"])

            response = THDataPointCRUD.query(query)
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
                th_datapoint = THDataPoint(**th_args)
                THDataptsCRUD = THDataPointCRUD(datapoint, th_datapoint) 
                THDataptsCRUD.new() 
                
                # Recover Datapoint
                self.dataframe.loc[index, "id"] = THDataptsCRUD.id
                self.dataframe.loc[index, "dataPointId"] = THDataptsCRUD.dataPoint.id

            elif update:

                old_dpts_args = records[0]["dataPointDTO"]
                dpts_args = self._update_args(old_dpts_args, dpts_args, update_strategy)
                old_th_args = records[0]["extendedDataPointDTO"]
                th_args = self._update_args(old_th_args, th_args, update_strategy)

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create THDataPoint
                th_datapoint = THDataPoint(**th_args)

                # Use THDataPointCRUD to create the Datapoint and
                # the THDatapoint
                THDataptsCRUD = THDataPointCRUD(datapoint, th_datapoint) 
                THDataptsCRUD.id = th_datapoint.id
                THDataptsCRUD.dataPointID = datapoint.id
                THDataptsCRUD.dataPoint.dataEntityId = th_datapoint.id
                THDataptsCRUD.dataPoint.thdataPointId = th_datapoint.id
                THDataptsCRUD.update()

            index = THDataptsCRUD.id
            self.dataframe_out.loc[index] = th_args
            self.dataframe_out.loc[index, "id"] = THDataptsCRUD.id
            self.dataframe_out.loc[index, "dataPointId"] = datapoint.id
            for k, v in th_skip_args.items():
                self.dataframe_out.loc[index, k] = v


class THDataPointBatchUploader(APIRequests, THDataPointUploader):

    name = "THDatapoints"
    API_PATH = "/api/other/importer"
    
    def __init__(self, th_datapoints_df, skip_columns=None):

        THDataPointUploader.__init__(self, th_datapoints_df)

        self.validated = False
        self.skip_columns = skip_columns
        import pkg_resources
        path = pkg_resources.resource_filename(__name__, "../templates")
        environment = Environment(loader=FileSystemLoader(path))
        self.template = environment.get_template("thdatapoints.txt")


    def validate(self, lazy=False):

        columns = ['Datapoint Name', 'Datapackage Name',
                   'Lab', 'Analyst', 'Associated Literature',
                   'Model Software', 'Model Approach', 'Model Type',
                   'Number of model iterations', 'Temperature Gradient', 'Temperature Gradient range', 
                   'Offset Allowed to Vary?', 'Model Comment'] 

        for col in self.dataframe.columns:
            if col not in columns:
                raise ValueError(f"column {col} not in schema")

        list = {"dataPackage": DataPackage,
                   "modelType": LModelType,
                   "modelSoftware": LModelSoftware,
                   "modelApproach": LModelApproach}
        
        if self.skip_columns:
            skip_df = self.dataframe[[col for col in self.skip_columns if col in self.dataframe.columns]]
            self.dataframe = self.dataframe.drop(columns=[col for col in self.skip_columns if col in self.dataframe.columns])

        for key, val in list.items():
            if key + "Id" not in self.dataframe.columns:
                uniques = self.dataframe[key].unique()
                uniques = [unique for unique in uniques if unique is not None]
                mapping = {}
                for unique in uniques:
                    mapping[unique] = val.get_id_from_name(unique)
                self.dataframe[key + "Id"] = self.dataframe[key].map(mapping)

        self.dataframe = self.dataframe.replace({np.nan: None})
        self.dataframe = THDataPointBatchSchema.validate(self.dataframe, lazy=lazy)
        self.dataframe = self.dataframe.astype(object).where(pd.notnull(self.dataframe), None)

        if self.skip_columns:
            for col in self.skip_columns:
                self.dataframe[col] = skip_df[col]  
       
        self.validated = True


    def _get_payload(self):
        rows = self.dataframe.to_dict(orient="records")
        return self.template.render(batch_name=self.name, rows=rows)

    def importBatch(self):
        data = self._get_payload()
        path = self.path() + "/importBatch"
        response = APIRequests.SESSION.post(path, data=data, headers=self.SESSION.headers)
        try:
            response.raise_for_status()
        except Exception as e:
            print(response.json())
            raise e
        return response

