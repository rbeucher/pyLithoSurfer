from pyLithoSurferAPI.Geochemistry.schemas import GCDataPointSchema, GCAliquotSchema, ElementalConcentrationSchema, OxideConcentrationSchema
from pyLithoSurferAPI.core.lists import LErrorType, ReferenceMaterial

from pyLithoSurferAPI.core.tables import DataPoint, Material
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


class GCDataPointUploader(Uploader):

    name = "GCDataPoints"

    def __init__(self, datapackageId, gc_datapoints_df, skip_columns=None):

        Uploader.__init__(self, gc_datapoints_df)

        self.datapackageId = datapackageId 
        self.validated = False
        self.skip_columns = skip_columns


    def validate(self, lazy=False):

        gc_list = {"dataPackage": DataPackage,
                   "analysisScaleName": LGCAnalysisScale,
                   "dataReductionSoftwareName": LDataReductionSoftware,
                   "elementErrorTypeName": LErrorType,
                   "geochemAnalyticalTypeName": LGCAnalyticalTechnique,
                   "mineralName": Material,
                   "oxideErrorTypeName": LErrorType,
                   "referenceMaterialName": ReferenceMaterial}
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
            if gc_args.get("dataPointId"):
                gc_args.pop("dataPointId")

            dpts_args = {"dataPackageId": self.datapackageId,
                         "dataStructure": "GC",
                         "dataEntityId": None,
                         "name": f"Data Entry {str(datetime.now())}",
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.dataStructure.equals": "GC",
                     "dataPointLithoCriteria.sampleId.equals": int(sampleId),
                     "dataPointLithoCriteria.dataPackageId.equals": self.datapackageId}

            if gc_args["mineralId"]:
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