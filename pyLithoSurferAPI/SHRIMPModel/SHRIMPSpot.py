from pyLithoSurferAPI import session, URL_BASE
from pyLithoSurferAPI.REST import APIRequests


class SHRIMPSpot(APIRequests):
        
    path = URL_BASE+'/api/shrimp-spots'

SHRIMPSpotCRUD = SHRIMPSpot