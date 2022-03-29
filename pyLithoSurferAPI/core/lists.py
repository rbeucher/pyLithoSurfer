
from pyLithoSurferAPI.REST import APIRequests
import pandas as pd

class LCelestial(APIRequests):

    API_PATH = "/api/core/l-celestials"


class LCountry(APIRequests):

    API_PATH = "/api/core/l-countries"


class LElevationKind(APIRequests):

    API_PATH = "/api/core/l-elevation-kinds"


class LErrorType(APIRequests):

    API_PATH = "/api/core/l-error-types"


class LGeoEvent(APIRequests):

    API_PATH = "/api/core/l-geo-events"


class LLab(APIRequests):

    API_PATH = "/api/core/labs"


class LLocationKind(APIRequests):

    API_PATH = "/api/core/l-location-kinds"


class LMachine2DataPointRole(APIRequests):

    API_PATH = "/api/core/l-machine_2_data_point_role"


class LMachineType(APIRequests):

    API_PATH = "/api/core/l-machine-types"


class LSampleKind(APIRequests):

    API_PATH = "/api/core/l-sample-kinds"


class LSampleMethod(APIRequests):

    API_PATH = "/api/core/l-sample-methods"


class LSHRIMPAgeGroup(APIRequests):

    API_PATH = "/api/shrimp/lshrimp-age-groups"


class LSHRIMPAgeType(APIRequests):

    API_PATH = "/api/shrimp/lshrimp-age-types"


class LSHRIMPSampleFormat(APIRequests):

    API_PATH = "/api/shrimp/lshrimp-sample-formats"


class LStatementKind(APIRequests):

    API_PATH = "/api/l-statement-kinds"


class LSampleMethod(APIRequests):

    API_PATH = "/api/core/l-sample-methods"


class LVerticalDatum(APIRequests):

    API_PATH = "/api/l-vertical-data"


class LVerticalDatumKind(APIRequests):

    API_PATH = "/api/l-vertical-data"


class LAnalyticalMethod(APIRequests):

    API_PATH = "/api/core/l-analytical-methods"


class ReferenceMaterial(APIRequests):

    API_PATH = "/api/core/reference-materials"


class LPerson2DataPointRole(APIRequests):

    API_PATH = "/api/core/l-person-2-data-point-roles"


class LPerson2SampleRole(APIRequests):

    API_PATH = "/api/core/l-person-2-sample-roles"


def get_list_name_to_id_mapping(ListClass):
    df = ListClass.get_all()
    return pd.Series(df.id.values, index=df.name).to_dict()
