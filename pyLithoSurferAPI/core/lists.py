from pyLithoSurferAPI import URL_BASE
from pyLithoSurferAPI.REST import APIRequests

class LCelestial(APIRequests):

    path = URL_BASE + "/api/core/l-celestials"


class LCountry(APIRequests):

    path = URL_BASE + "/api/core/l-countries"


class LElevationKind(APIRequests):

    path = URL_BASE + "/api/core/l-elevation-kinds"


class LErrorType(APIRequests):

    path = URL_BASE + "/api/core/l-error-types"


class LGeoEvent(APIRequests):

    path = URL_BASE + "/api/core/l-geo-events"


class LLab(object):

    path = URL_BASE + "/api/l-labs"


class LLithologyKind(object):

    path = URL_BASE + "/api/l-lithology-kinds"


class LLocationCapture(APIRequests):

    path = URL_BASE + "/api/l-loc-captures"


class LLocationKind(APIRequests):

    path = URL_BASE + "/api/core/l-location-kinds"


class LMachine2DataPointRole(APIRequests):

    path = URL_BASE + "/api/core/l-machine_2_data_point_role"


class LMachineType(APIRequests):

    path = URL_BASE + "/api/l-machine-types"


class LSampleKind(APIRequests):

    path = URL_BASE + "/api/core/l-sample-kinds"


class LSampleMethod(APIRequests):

    path = URL_BASE + "/api/core/l-sample-methods"


class LSHRIMPAgeGroup(APIRequests):

    path = URL_BASE + "/api/shrimp/lshrimp-age-groups"


class LSHRIMPAgeType(APIRequests):

    path = URL_BASE + "/api/shrimp/lshrimp-age-types"


class LSHRIMPSampleFormat(APIRequests):

    path = URL_BASE + "/api/shrimp/lshrimp-sample-formats"


class LStatementKind(APIRequests):

    path = URL_BASE + "/api/l-statement-kinds"


class LSampleMethod(APIRequests):

    path = URL_BASE + "/api/core/l-sample-methods"


class LVerticalDatum(APIRequests):

    path = URL_BASE + "/api/l-vertical-data"


class LVerticalDatumKind(APIRequests):

    path = URL_BASE + "/api/l-vertical-data"


class ReferenceMaterial(APIRequests):

    path = URL_BASE + "/api/core/reference-materials"





