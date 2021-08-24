from pyLithoSurferAPI.lSHRIMPSampleFormat import get_SHRIMPsampleFormat_id
from pyLithoSurferAPI.lErrorType import get_error_type_id
from pyLithoSurferAPI.lLocationKind import get_locationKind_id
from pyLithoSurferAPI.lCelestial import get_celestial_id
from pyLithoSurferAPI.lElevationKind import get_elevation_kind_id
from pyLithoSurferAPI.lSampleMethod import get_sampleMethod_id
from pyLithoSurferAPI.lGeoEvent import get_geoEvent_id
from pyLithoSurferAPI.lSHRIMPAgeType import get_SHRIMPAgeType_id
from pyLithoSurferAPI.lSHRIMPSampleFormat import get_SHRIMPsampleFormat_id
from pyLithoSurferAPI.lLocationCapture import get_locationCapture_id
from pyLithoSurferAPI.lSampleKind import get_sampleKind_id
from pyLithoSurferAPI.lPerson2DataPointRole import get_person2DataPointRole_id
from pyLithoSurferAPI.lPerson2SampleRole import get_person2SampleRole_id
import pandas as pd
import numpy as np

def get_mapping_to_list_indices(data, func, replace=None):
    
    if any(pd.isna(data.unique())):
        try:
            default = func("Unknown")
            data.replace({np.nan:"Unknown"}, inplace=True)
        except:
            raise ValueError("The data contains NA values and there is no indices associated")
            
    if replace:
        data.replace(replace, inplace=True)

    mapping = {}

    for el in data.unique():
        try:
            mapping[el] = func(el)
        except:
            raise ValueError("I cannot find any index for {0}".format(el))
            
    return mapping

def map_string_to_list_indices(data, func, replace=None, **kwargs):

    return data.replace(get_mapping_to_list_indices(data, func, replace), **kwargs)