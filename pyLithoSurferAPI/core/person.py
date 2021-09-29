from pyLithoSurferAPI import URL_BASE
from pyLithoSurferAPI.REST import APIRequests
import pandas as pd


class Person(APIRequests):

    path = URL_BASE + "/api/core/people"


