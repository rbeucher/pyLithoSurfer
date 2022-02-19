import numpy as np
import pandas as pd
from typing import Union
import json


# Python class generator using Jinja template.
def generate_code(class_name, api_address, args, dest="./"):
    import jinja2
    import pkg_resources

    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = pkg_resources.resource_filename(__name__, "/template.jinja")
    template = templateEnv.get_template(TEMPLATE_FILE)
    
    result = template.render(class_name=class_name, api_address=api_address, args=args)
    
    with open(class_name + ".py", "w") as f:
        f.write(result)


def get_elevation_from_google(lat: Union[float, np.float16, np.float32, np.float64] = 0., lon: Union[float, np.float16, np.float32, np.float64] = 0.):
    from pyLithoSurferAPI.REST import APIRequests
    API_PATH = "/api/other/elevation" + f"?lat={lat}&lon={lon}"
    response = APIRequests.SESSION.get(APIRequests.URL_BASE + API_PATH)
    response.raise_for_status()
    return response.json()


def convert_coordinates(x, y, epsg_in="epsg:4283", epsg_out="epsg:4326"):
    """ Convert from crs, the default is to convert from GDA94 to WGS84 """
    from pyproj import Transformer
    transformer = Transformer.from_crs(epsg_in, epsg_out)
    if isinstance(x, pd.Series):
        x = x.values
    if isinstance(y, pd.Series):
        y = y.values
    x, y = transformer.transform(x, y)
    return {"x": x, "y": y}


def get_connection_to_db(DB_MODE):
    import os
    import psycopg2

    user = os.environ.get(f"LITHODAT_{DB_MODE}_DBUSER")
    password = os.environ.get(f"LITHODAT_{DB_MODE}_DBPASSWORD")
    host = os.environ.get(f"LITHODAT_{DB_MODE}_DBHOST")
    database = os.environ.get(f"LITHODAT_{DB_MODE}_DBNAME")

    url = f"postgresql://{user}:{password}@{host}:5432/{database}"

    connection = psycopg2.connect(user = user,
                                 password = password,
                                 host = host,
                                 port = "5432",
                                 database = database)

    return connection


def map_to_new_literature_id(source_ids):

    connection = get_connection_to_db("TEST")
    uploaded = pd.read_sql_query("SELECT * FROM literature", connection)

    # This is required as some new literature entries may not have a source_id
    uploaded = uploaded[~pd.isnull(uploaded.source_id)].copy()

    source_ids.replace({np.nan:0}, inplace=True)

    mapping = pd.Series(uploaded.id.values,index=uploaded.source_id.astype("int")).to_dict()

    return source_ids.map(mapping)


def migrate_lithology_to_mindat(lithologies):

    import pkg_resources
    migration_filepath = pkg_resources.resource_filename(__name__, "resources/Lithology migration table.xlsx")

    connection = get_connection_to_db("TEST")
    mindat_lithologies = pd.read_sql_query("SELECT * FROM material", connection)
    # This is required as the Mindat material table is somewhat messed up.
    # There are some extra lines in the table, with some random strings in the 
    # source_id field.
    mindat_lithologies = mindat_lithologies[mindat_lithologies.source_id.str.isnumeric()]
    # This is required as some new entries may not have a source_id
    mapping = pd.Series(mindat_lithologies.id.values, index=mindat_lithologies.source_id.astype("int32")).to_dict()
    
    lit_excel = pd.read_excel(migration_filepath, sheet_name="Mapping in new Moritz DB")
    lit_excel = lit_excel[["Old Lithology 1.6", "NEW MINDAT DB in Moritz DB"]]
    lit_excel["New_indices"] = lit_excel["NEW MINDAT DB in Moritz DB"].map(mapping)
    lit_excel.replace({np.nan: 0, None: 0}, inplace=True)
    lit_excel["New_indices"] = lit_excel["New_indices"].astype("int32")
    
    mapping = pd.Series(lit_excel["New_indices"].values, index=lit_excel["Old Lithology 1.6"])
    #lithologies.replace({np.nan: 0, None: 0}, inplace=True)
    lithologies = lithologies.map(mapping)#.astype("int32")
    
    return lithologies


class NumpyEncoder(json.JSONEncoder):
    """ Custom encoder for numpy data types """
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):

            return int(obj)

        elif isinstance(obj, (np.float_, np.float16, np.float32, np.float64)):
            return float(obj)

        elif isinstance(obj, (np.complex_, np.complex64, np.complex128)):
            return {'real': obj.real, 'imag': obj.imag}

        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()

        elif isinstance(obj, (np.bool_)):
            return bool(obj)

        elif isinstance(obj, (np.void)): 
            return None
        
        return json.JSONEncoder.default(self, obj)


def check_entries(pd_series, refClass, addMissing=False):
    missing = []
    for item in pd_series.unique():
        if refClass.get_id_from_name(item) is None:
            missing.append(item)
    if addMissing:
        for item in missing:
            refClass(name=item).new()
    return missing


def clean_entries(pd_series, nan_default="Unknown", replace=None):
    # Remove Leading and Trailing blanks
    pd_series = pd_series.str.strip()
    # Capitalize
    pd_series = pd_series.str.capitalize()
    # Replace Nan values
    pd_series = pd_series.replace({np.nan: nan_default})
    return pd_series

def upload_list_excel(xlsxFile, name, Entity):
    data = pd.read_excel(xlsxFile, sheet_name=name, skiprows=11) 
    data = data[["name", "description"]]
    data = data.to_dict(orient="records")
    data = data[::-1]

    for item in data:
        name = item["name"]
        description = item["description"]
        print(name, description)
        entity = Entity(name=name, id=0)
        entity.new()
    return data

def upload_list_gsheet(sheet_id, sheet_name, Entity):
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df = pd.read_csv(url, skip_blank_lines=False, skiprows=5)
    df = df[["name", "description"]]
    df = df.to_dict(orient="records")
    df = df[::-1]

    print(f"Uploading {sheet_name}")
    for item in df:
        response = Entity.query({"name.equals": item["name"]})
        if response.json():
            continue
        name = item["name"]
        description = item["description"]
        print(name, description)
        entity = Entity(name=name, id=0)
        entity.new()
    return df
