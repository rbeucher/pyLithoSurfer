import numpy as np
import pandas as pd
from typing import Union


url = str

# Convert if data is not nan or None
# This is to make sure that we are pushing the right type to the API.
convert_int = lambda x: int(x) if not pd.isna(x) else None
convert_float = lambda x: float(x) if not pd.isna(x) else None

def convert_str(value):
        if value is None:
            return None
        if isinstance(value, str):
            return value.strip()
        if np.isnan(value):
            return None


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
    from . import session, URL_BASE
    from .REST import check_response
    path = URL_BASE + "/api/other/elevation" + f"?lat={lat}&lon={lon}"
    response = session.get(path)
    check_response(response)
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