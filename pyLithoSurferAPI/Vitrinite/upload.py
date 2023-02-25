from pyLithoSurferAPI.management.tables import DataPackage
from pyLithoSurferAPI.core.tables import DataPoint
from pyLithoSurferAPI.Vitrinite.schemas import VitriniteDataPointSchema
from pyLithoSurferAPI.Vitrinite.tables import VitriniteDataPointCRUD, VitriniteDataPoint
from pyLithoSurferAPI.uploader import Uploader
from tqdm import tqdm


class VitriniteDataPointUploader(Uploader):

    name = "VitriniteDataPoint"

    def __init__(self, vitrinite_datapoints_df):

        Uploader.__init__(self, vitrinite_datapoints_df)

        self.dataframe = vitrinite_datapoints_df
        self.validated = False

    def validate(self, lazy=False):
       lists = {"dataPackage": DataPackage}
       self.dataframe = Uploader._validate(self.dataframe, VitriniteDataPointSchema, lists, lazy=lazy)
       self.validated = True

    def upload(self, update=False, update_strategy="merge_keep"):
        
        if not self.validated:
            raise ValueError("Data not validated")

        self.dataframe["id"] = None

        for index in tqdm(self.dataframe.index):

            vitrinite_args = self.dataframe.loc[index].to_dict()
            sampleId = vitrinite_args.pop("sampleId")
            locationId = vitrinite_args.pop("locationId")
            dataPackageId = vitrinite_args.pop("dataPackageId")

            if vitrinite_args.get("dataPointId"):
                vitrinite_args.pop("dataPointId")

            dpts_args = {"dataPackageId": dataPackageId,
                         "dataStructure": "SIMPLE",
                         "dataEntityId": None,
                         "name": None,
                         "locationId": locationId,
                         "sampleId": sampleId}
            
            query = {"dataPointLithoCriteria.sampleId.equals": sampleId,
                     "dataPointLithoCriteria.dataStructure.equals": "SIMPLE",
                     "dataPointLithoCriteria.dataPackageId.equals": dataPackageId}

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

                VitriniteDataptsCRUD = VitriniteDataPointCRUD(datapoint, vitrinite_datapoint) 
                VitriniteDataptsCRUD.new() 
                
                # Recover Datapoint
                self.dataframe.loc[index, "id"] = VitriniteDataptsCRUD.id
                self.dataframe.loc[index, "dataPointId"] = VitriniteDataptsCRUD.dataPoint.id

            elif update:

                old_dpts_args = records[0]["dataPointDTO"]
                dpts_args = Uploader._update_args(old_dpts_args, dpts_args, update_strategy)
                old_vitrinite_args = records[0]["vitriniteDataPointDTO"]
                vitrinite_args = Uploader._update_args(old_vitrinite_args, vitrinite_args, update_strategy)

                # Create DataPoint
                datapoint = DataPoint(**dpts_args)

                # Create VitriniteDataPoint
                vitrinite_datapoint = VitriniteDataPoint(**vitrinite_args)

                VitriniteDataptsCRUD = VitriniteDataPointCRUD(datapoint, vitrinite_datapoint) 
                VitriniteDataptsCRUD.id = vitrinite_datapoint.id
                VitriniteDataptsCRUD.dataPointId = datapoint.id
                VitriniteDataptsCRUD.dataPoint.dataEntityId = vitrinite_datapoint.id
                VitriniteDataptsCRUD.dataPoint.shrimp_datapoint_id = vitrinite_datapoint.id
                VitriniteDataptsCRUD.update()
                self.dataframe.loc[index, "id"] = VitriniteDataptsCRUD.id
                self.dataframe.loc[index, "dataPointId"] = datapoint.id

            index = VitriniteDataptsCRUD.id
            self.dataframe_out.loc[index] = dpts_args
            self.dataframe_out.loc[index, "locationId"] = locationId
            self.dataframe_out.loc[index, "sampleId"] = sampleId
            self.dataframe_out.loc[index, "id"] = VitriniteDataptsCRUD.id
            self.dataframe_out.loc[index, "dataPointId"] = datapoint.id
