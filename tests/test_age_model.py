
import pandas as pd
from pyLithoSurferAPI import select_database
select_database('test')

file = "./ressources/SEA_FTRACK_Clean.xlsx"

samples = pd.read_excel(file, sheet_name="samples", index_col=0)
locations = pd.read_excel(file, sheet_name="locations", index_col=0)
age_datapoints = pd.read_excel(file, sheet_name="age_datapoints", index_col=0)
lit2data = pd.read_excel(file, sheet_name="literatures", index_col=0)
mineral_properties = pd.read_excel(file, sheet_name="mineral_property", index_col=0)

def test_upload_samples():
    
    from pyLithoSurferAPI.management.tables import DataPackage
    datapackage_id = DataPackage.get_id_from_name("romain_package")

    from pyLithoSurferAPI.core import SampleWithLocationUploader
    add_name = str(datapackage_id).zfill(8)
    samples.name = "LITH" + add_name + "-" + samples.name.astype('str')
    up = SampleWithLocationUploader(datapackageId=datapackage_id, locations_df=locations, samples_df=samples)
    up.validate()
    up.upload(update=True, update_strategy="replace")
    #up.clean()


