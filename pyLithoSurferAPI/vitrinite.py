from . import session, URL_BASE
from typing import Union
from pyLithoSurferAPI.REST import APIRequests
import json
import numpy as np
from .utilities import *


class Vitrinite(APIRequests):

    path = URL_BASE + "/api/vitrinites"

    def __init__(self,
                 nmeasure: Union[int, np.int16, np.int32, np.int64, None],
                 oMpct: Union[float, np.float16, np.float32, np.float64],
                 roMax: Union[float, np.float16, np.float32, np.float64],
                 roMin: Union[float, np.float16, np.float32, np.float64],
                 roPct: Union[float, np.float16, np.float32, np.float64],
                 roSD: Union[float, np.float16, np.float32, np.float64]):
        """Vitrinite

        Args:
            nmeasure (Union[int, np.int16, np.int32, np.int64, None]): [description]
            oMpct (Union[float, np.float16, np.float32, np.float64]): [description]
            roMax (Union[float, np.float16, np.float32, np.float64]): [description]
            roMin (Union[float, np.float16, np.float32, np.float64]): [description]
            roPct (Union[float, np.float16, np.float32, np.float64]): [description]
            roSD (Union[float, np.float16, np.float32, np.float64]): [description]

        Returns:
            Vitrinite object
        """
        self.nmeasure = convert_int(nmeasure)
        self.oMpct = convert_float(oMpct)
        self.roMax = convert_float(roMax)
        self.roMin = convert_float(roMin)
        self.roPct = convert_float(roPct)
        self.roSD = convert_float(roSD)

        self._id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value: Union[int, np.int16, np.int32, np.int64, None]):
        self._id = convert_int(value)

    @property
    def nmeasure(self):
        return self._nmeasure

    @nmeasure.setter
    def nmeasure(self, value: Union[int, np.int16, np.int32, np.int64, None]):
        self._nmeasure = convert_int(value)

    @property
    def oMpct(self):
        return self._oMpct

    @oMpct.setter
    def oMpct(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._oMpct = convert_float(value)

    @property
    def roMax(self):
        return self._roMax

    @roMax.setter
    def roMax(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._roMax = convert_float(value)

    @property
    def roMin(self):
        return self._roMin

    @roMin.setter
    def roMin(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._roMin = convert_float(value)

    @property
    def roPct(self):
        return self._roPct

    @roPct.setter
    def roPct(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._roPct = convert_float(value)

    @property
    def roSD(self):
        return self._roSD

    @roSD.setter
    def roSD(self, value: Union[float, np.float16, np.float32, np.float64]):
        self._roSD = convert_float(value)
