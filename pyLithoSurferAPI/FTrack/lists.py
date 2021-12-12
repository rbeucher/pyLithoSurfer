from pyLithoSurferAPI import URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import pandas as pd

class LDosimeter(APIRequests):

    path = URL_BASE + "/api/fissiontrack/l-dosimeter"


class LEtchant(APIRequests):

    path = URL_BASE + "/api/fissiontrack/l-etchant"


class LFTAgeAnalyticalTechnique(APIRequests):

    path = URL_BASE + "/api/fissiontrack/ft/LFTAgeAnalyticalTechnique"


class LFTAgeEquation(APIRequests):

    path = URL_BASE + "/api/fissiontrack/ft/LFTAgeEquation"


class LFTAgeType(APIRequests):

    path = URL_BASE + "/api/fissiontrack/ft/LFTAgeType"


class LFTAgeEquation(APIRequests):

    path = URL_BASE + "/api/fissiontrack/l-ft-analytical-method"


class LFTAnalyticalSoftware(APIRequests):

    path = URL_BASE + "/api/fissiontrack/l-ft-analytical-software"


class LIrradiationReactor(APIRequests):

    path = URL_BASE + "/api/fissiontrack/ft/LIrradiationReactor"


class LLambda(APIRequests):

    path = URL_BASE + "/api/fissiontrack/ft/LLambda"


class LLambdaF(APIRequests):

    path = URL_BASE + "/api/fissiontrack/ft/LLambdaF"


class LRmr0Equation(APIRequests):

    path = URL_BASE + "/api/fissiontrack/ft/LRmr0Equation"


class LTrackType(APIRequests):

    path = URL_BASE + "/api/fissiontrack/l-track-type"