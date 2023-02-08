from pyLithoSurferAPI.Geochemistry.schemas import GCDataPointSchema, GCAliquotSchema, ElementalConcentrationSchema, OxideConcentrationBatchSchema, GCDataPointBatchSchema, ElementalConcentrationBatchSchema
from pyLithoSurferAPI.REST import APIRequests
from pyLithoSurferAPI.core.lists import LErrorType, ReferenceMaterial

from pyLithoSurferAPI.core.tables import DataPoint, Material, SampleWithLocation
from pyLithoSurferAPI.Geochemistry.tables import GCDataPoint, GCDataPointCRUD, GCAliquotCRUD, ElementalConcentrationCRUD, OxideConcentrationCRUD
from pyLithoSurferAPI.Geochemistry.lists import (LDataReductionSoftware,
                                                 LElement,
                                                 LGCAnalysisScale,
                                                 LGCAnalyticalTechnique,
                                                 LGrainDomain,
                                                 LIsotope,
                                                 LOxide)

from pyLithoSurferAPI.uploader import Uploader
from pyLithoSurferAPI.management.tables import DataPackage
from tqdm import tqdm
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import numpy as np
import pandas as pd
from copy import copy
import json


class GCDataPointUploader(Uploader):

    name = "GCDataPoints"

    def __init__(self, gc_datapoints_df, skip_columns=None):

        Uploader.__init__(self, gc_datapoints_df)

        self.validated = False
        self.skip_columns = skip_columns


    def validate(self, lazy=False):

        gc_list = {"dataPackage": DataPackage,
                   "analysisScale": LGCAnalysisScale,
                   "dataReductionSoftware": LDataReductionSoftware,
                   "elementUncertaintyType": LErrorType,
                   "geochemAnalyticalType": LGCAnalyticalTechnique,
                   "mineral": Material,
                   "oxideUncertaintyType": LErrorType,
                   "referenceMaterial": ReferenceMaterial}
        if self.skip_columns:
            skip_df = self.dataframe[[col for col in self.skip_columns if col in self.dataframe.columns]]
            self.dataframe = self.dataframe.drop(columns=[col for col in self.skip_columns if col in self.dataframe.columns])

        self.dataframe = Uploader._validate(self.dataframe, GCDataPointSchema, gc_list, lazy=lazy)

        if self.skip_columns:
            for col in self.skip_columns:
                self.dataframe[col] = skip_df[col]  
       
        self.validated = True

    def upload(self, update=False, update_strategy="replace"):
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            gc_args = self.dataframe.loc[index].to_dict()

            gc_skip_args = {}
            for k, v in gc_args.items():
                if self.skip_columns and k in self.skip_columns:
                    gc_skip_args[k] = gc_args[k]
            gc_args = {k:v for k,v in gc_args.items() if k not in gc_skip_args.keys()}

            sampleId = gc_args.pop("sampleId")
            locationId = gc_args.pop("locationId")
            dataPackageId = gc_args.pop("dataPackageId")

            if gc_args.get("dataPointId"):
                gc_args.pop("dataPointId")

            dpts_args = {"dataPackageId": dataPackageId,
                         "dataStructure": "GC",
                         "dataEntityId": None,
                         "name": f"Data Entry {str(datetime.now())}",
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.dataStructure.equals": "GC",
                     "dataPointLithoCriteria.sampleId.equals": int(sampleId),
                     "dataPointLithoCriteria.dataPackageId.equals": dataPackageId}

            if "mineralId" in gc_args.keys():
                query["mineralId.equals"] = int(gc_args["mineralId"])

            response = GCDataPointCRUD.query(query)
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
                gc_datapoint = GCDataPoint(**gc_args)
                GCDataptsCRUD = GCDataPointCRUD(datapoint, gc_datapoint) 
                GCDataptsCRUD.new() 
                
                # Recover Datapoint
                self.dataframe.loc[index, "id"] = GCDataptsCRUD.id
                self.dataframe.loc[index, "dataPointId"] = GCDataptsCRUD.dataPoint.id

            elif update:

                old_dpts_args = records[0]["dataPointDTO"]
                dpts_args = self._update_args(old_dpts_args, dpts_args, update_strategy)
                old_gc_args = records[0]["gcdataPointDTO"]
                gc_args = self._update_args(old_gc_args, gc_args, update_strategy)

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create GCDataPoint
                gc_datapoint = GCDataPoint(**gc_args)

                # Use GCDataPointCRUD to create the Datapoint and
                # the GCDatapoint
                GCDataptsCRUD = GCDataPointCRUD(datapoint, gc_datapoint) 
                GCDataptsCRUD.id = gc_datapoint.id
                GCDataptsCRUD.dataPointID = datapoint.id
                GCDataptsCRUD.dataPoint.dataEntityId = gc_datapoint.id
                GCDataptsCRUD.dataPoint.gcdataPointId = gc_datapoint.id
                GCDataptsCRUD.update()

            index = GCDataptsCRUD.id
            self.dataframe_out.loc[index] = gc_args
            self.dataframe_out.loc[index, "locationId"] = locationId
            self.dataframe_out.loc[index, "sampleId"] = sampleId
            self.dataframe_out.loc[index, "id"] = GCDataptsCRUD.id
            self.dataframe_out.loc[index, "dataPointId"] = datapoint.id
            for k, v in gc_skip_args.items():
                self.dataframe_out.loc[index, k] = v


class GCDataPointBatchUploader(APIRequests, GCDataPointUploader):

    name = "GCDatapoints"
    API_PATH = "/api/other/importer"
    
    def __init__(self, gc_datapoints_df, skip_columns=None):

        GCDataPointUploader.__init__(self, gc_datapoints_df)

        self.validated = False
        self.skip_columns = skip_columns
        import pkg_resources
        path = pkg_resources.resource_filename(__name__, "../templates")
        environment = Environment(loader=FileSystemLoader(path))
        self.template = environment.get_template("gcdatapoints.txt")


    def validate(self, lazy=False):

        columns = ['Tag', 'Datapoint Name', 'Datapackage Name',
                   'Sample Name', 'description', 'geochemAnalyticalType',
                   'dataReductionSoftware', 'analyticalSessionID', 'analyst',
                   'batchID', 'mountID', 'analysisScale', 
                   'mineral', 'oxideUncertaintyType', 'elementUncertaintyType'] 

        for col in self.dataframe.columns:
            if col not in columns:
                raise ValueError(f"column {col} not in schema")

        list = {"Datapackage Name": DataPackage,
                "Sample Name": SampleWithLocation,
                "geochemAnalyticalType": LGCAnalyticalTechnique,
                "dataReductionSoftware": LDataReductionSoftware,
                "analysisScale": LGCAnalysisScale,
                "mineral": Material,
                "oxideUncertaintyType": LErrorType,
                "elementUncertaintyType": LErrorType,
                }
        
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
        self.dataframe = GCDataPointBatchSchema.validate(self.dataframe, lazy=lazy)
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

class GCDataPointCSVBatchUploader(APIRequests):

    name = "GCDatapoints"
    API_PATH = "/api/other/importer"
    
    def __init__(self, csvfile):

        self.validated = False
        self.csvfile = csvfile
        self.dataframe = pd.read_csv(csvfile)

    def validate(self, lazy=False):

        columns = ['Tag', 'Datapoint Name', 'Datapackage Name',
                   'Sample Name', 'description', 'geochemAnalyticalType',
                   'dataReductionSoftware', 'analyticalSessionID', 'analyst',
                   'batchID', 'mountID', 'analysisScale', 
                   'mineral', 'oxideUncertaintyType', 'elementUncertaintyType'] 

        for col in self.dataframe.columns:
            if col not in columns:
                raise ValueError(f"column {col} not in schema")

        list = {"Datapackage Name": DataPackage,
                "Sample Name": SampleWithLocation,
                "geochemAnalyticalType": LGCAnalyticalTechnique,
                "dataReductionSoftware": LDataReductionSoftware,
                "analysisScale": LGCAnalysisScale,
                "mineral": Material,
                "oxideUncertaintyType": LErrorType,
                "elementUncertaintyType": LErrorType,
                }
        
        self.dataframe = self.dataframe.replace({np.nan: None})
        for key, val in list.items():
            if key + "Id" not in self.dataframe.columns:
                uniques = self.dataframe[key].unique()
                uniques = [unique for unique in uniques if unique is not None]
                mapping = {}
                for unique in uniques:
                    mapping[unique] = val.get_id_from_name(unique)
                self.dataframe[key + ["Id"]] = self.dataframe[key].map(mapping)


        self.dataframe = GCDataPointBatchSchema.validate(self.dataframe, lazy=lazy)
        self.dataframe = self.dataframe.astype(object).where(pd.notnull(self.dataframe), None)

        self.validated = True

    def createBatch(self):
        data = {"file": self.csvfile}
        headers = copy(self.SESSION.headers) 
        headers["Content-Type"] = "multipart/form-data"
        path = self.path() + "/createBatch"
        print(data)
        response = APIRequests.SESSION.post(path, data=json.dumps(data), headers=headers)
        try:
            response.raise_for_status()
        except Exception as e:
            print(response.json())
            raise e
        response = response.json()
        return response
class ElementalConcentrationDataUploader(ElementalConcentrationCRUD, Uploader):

    name = "ElementalConcentration"

    def __init__(self, element_concentration_df):

        Uploader.__init__(self, element_concentration_df)
        self.validated = False
        self.elements = {}

    def validate(self, lazy=False):

        for col in self.dataframe.columns:
            val = LElement.get_id_from_name(col)
            if val:
                self.elements[col] = val
        self.validated = True

    def get_unique_query(self, args):
        
        query = {"GCDataPointId.equals": int(args["gcdataPointId"]),
                 "aliquotName.equals": args["aliquotName"],
                 "elementId.equals": args["elementId"]}
        return super().query(query)
    
    def upload(self, update=False, update_strategy="merge_keep"):
        
        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            args = self.dataframe.loc[index].to_dict()
            common_args = {key:val for key, val in args.items() if key not in self.elements.keys()}
            args = {key:val for key, val in args.items() if key in self.elements.keys()}
            for element, concentration in args.items():
                common_args["elementId"] = self.elements[element]
                common_args["concentration"] = concentration
                #response = self.get_unique_query(common_args)
                #records = response.json()
                records = []

                if len(records) == 1:
                    existing_id = records[0]["id"]
                    old_args =  {k:v for k,v in records[0].items() if v is not None}
                else:
                    existing_id = None

                if existing_id is None:
                    obj = ElementalConcentrationCRUD(**common_args) 
                    obj.new() 

                elif update:
                    common_args = self._update_args(old_args, common_args, update_strategy)
                    obj = ElementalConcentrationCRUD(**common_args) 
                    obj.update()

                index = obj.id
                self.dataframe_out.loc[index] = common_args
                self.dataframe_out.loc[index, "id"] = obj.id


class ElementalConcentrationBatchUploader(APIRequests, Uploader):

    name = "ElementalConcentration"
    API_PATH = "/api/other/importer"
    
    def __init__(self, ec_datapoints_df, skip_columns=None):

        Uploader.__init__(self, ec_datapoints_df)

        self.validated = False
        self.skip_columns = skip_columns
        import pkg_resources
        path = pkg_resources.resource_filename(__name__, "../templates")
        environment = Environment(loader=FileSystemLoader(path))
        self.template = environment.get_template("elementConcentration.txt")


    def validate(self, lazy=False):

        common_cols = ['gcDatapointId', 'aliquotName', 'spotID']
        other_cols = set(self.dataframe.columns) - set(common_cols)
        new_cols = copy(common_cols)
        elements_cols = []
       
        for col in other_cols:
            if "_conc" in col:
                el = col.replace("_conc", "")
                try:
                    id = LElement.get_id_from_name(el)
                    new_cols += col
                    elements_cols += col
                    if el + "_error" in self.dataframe.columns:
                        new_cols += el + "_error"
                except:
                    raise ValueError("Not good")
            elif "_error" in col:
                continue
            else:
                raise ValueError(f"column {col} is unknown")

        for col in other_cols:
            # Check the column type is float
            self.dataframe[col].astype(float)

        # Save list of elements for later
        self.elements = elements_cols

        self.dataframe = self.dataframe[new_cols].copy()
        self.dataframe = self.dataframe.replace({np.nan: None})
        # Check that the common_cols align with shema
        self.dataframe[common_cols] = ElementalConcentrationBatchSchema.validate(self.dataframe[common_cols], lazy=lazy)
        self.dataframe = self.dataframe.astype(object).where(pd.notnull(self.dataframe), None)
        self.validated = True

    def _get_payload(self, df):
        elements_id = [LElement.get_id_from_name(el) for el in self.elements]
        df = df.copy()
        df["concentration"] = df[self.elements].values.tolist()
        df = df.drop(columns=self.elements)
        rows = df.to_dict(orient="records")
        return self.template.render(batch_name=self.name, rows=rows, elements=self.elements, elements_id=elements_id)

    def importBatch(self):

        df_list = np.array_split(self.dataframe, len(self.dataframe) / 20)

        for df in tqdm(df_list):

            data = self._get_payload(df)
            path = self.path() + "/importBatch"
            response = APIRequests.SESSION.post(path, data=data, headers=self.SESSION.headers)
            try:
                response.raise_for_status()
            except Exception as e:
                print(response.json())
                raise e

        return


class OxideConcentrationBatchUploader(APIRequests, Uploader):

    name = "OxideConcentration"
    API_PATH = "/api/other/importer"
    
    def __init__(self, oxc_datapoints_df, skip_columns=None):

        Uploader.__init__(self, oxc_datapoints_df)

        self.validated = False
        self.skip_columns = skip_columns
        import pkg_resources
        path = pkg_resources.resource_filename(__name__, "../templates")
        environment = Environment(loader=FileSystemLoader(path))
        self.template = environment.get_template("oxideConcentration.txt")


    def validate(self, lazy=False):

        common_cols = ['gcDatapointId', 'aliquotName', 'spotID'] 
        other_cols = list(set(self.dataframe.columns) - set(common_cols))
        new_cols = copy(common_cols)
        oxides_cols = []
       
        for col in other_cols:
            if "_conc" in col:
                ox = col.replace("_conc", "")
                try:
                    id = LOxide.get_id_from_name(ox)
                    new_cols += col
                    oxides_cols += col
                    if ox + "_error" in self.dataframe.columns:
                        new_cols += ox + "_error"
                except:
                    raise ValueError("Not good")
            elif "_error" in col:
                continue
            else:
                raise ValueError(f"column {col} is unknown")
        
        for col in other_cols:
            # Check the column type is float
            self.dataframe[col].astype(float)

        # Save list of elements for later
        self.oxides = oxides_cols

        self.dataframe = self.dataframe[new_cols].copy()
        self.dataframe = self.dataframe.replace({np.nan: None})
        self.dataframe[common_cols] = OxideConcentrationBatchSchema.validate(self.dataframe[common_cols], lazy=lazy)
        self.dataframe = self.dataframe.astype(object).where(pd.notnull(self.dataframe), None)
        self.validated = True

    def _get_payload(self, df):
        oxides_id = [LOxide.get_id_from_name(ox) for ox in self.oxides]
        df = df.copy()
        df["concentration"] = df[self.oxides].values.tolist()
        df = df.drop(columns=self.oxides)
        rows = df.to_dict(orient="records")
        return self.template.render(batch_name=self.name, rows=rows, oxides=self.oxides, oxides_id=oxides_id)
        
    def importBatch(self):

        df_list = np.array_split(self.dataframe, len(self.dataframe) / 20)

        for df in tqdm(df_list):

            print(len(df))
            data = self._get_payload(df)
            path = self.path() + "/importBatch"
            response = APIRequests.SESSION.post(path, data=data, headers=self.SESSION.headers)
            try:
                response.raise_for_status()
            except Exception as e:
                print(response.json())
                raise e

        return


