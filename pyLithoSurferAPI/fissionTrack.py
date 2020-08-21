from . import session, URL_BASE
import json


class fissionTrack(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def areaCntCm2(self):
        return self._areaCntCm2

    @areaCntCm2.setter
    def areaCntCm2(self, value):
        self._areaCntCm2 = value

    @property
    def cAxisCorr(self):
        return self._cAxisCorr

    @cAxisCorr.setter
    def cAxisCorr(self, value):
        self._cAxisCorr = value

    @property
    def cfIrrad(self):
        return self._cfIrrad

    @cfIrrad.setter
    def cfIrrad(self, value):
        self._cfIrrad = value

    @property
    def chiSqPct(self):
        return self._chiSqPct

    @chiSqPct.setter
    def chiSqPct(self, value):
        self._chiSqPct = value

    @property
    def chronoId(self):
        return self._chronoId

    @chronoId.setter
    def chronoId(self, value):
        self._chronoId = value

    @property
    def chronoName(self):
        return self._chronoName

    @chronoName.setter
    def chronoName(self, value):
        self._chronoName = value

    @property
    def clWtpct(self):
        return self._clWtpct

    @clWtpct.setter
    def clWtpct(self, value):
        self._clWtpct = value

    @property
    def dispPct(self):
        return self._dispPct

    @dispPct.setter
    def dispPct(self, value):
        self._dispPct = value

    @property
    def dosimeterIdx(self):
        return self._dosimeterIdx

    @dosimeterIdx.setter
    def dosimeterIdx(self, value):
        self._dosimeterIdx = value

    @property
    def dparCnt(self):
        return self._dparCnt

    @dparCnt.setter
    def dparCnt(self, value):
        self._dparCnt = value

    @property
    def dparErr(self):
        return self._dparErr

    @dparErr.setter
    def dparErr(self, value):
        self._dparErr = value

    @property
    def dparSd(self):
        return self._dparSd

    @dparSd.setter
    def dparSd(self, value):
        self._dparSd = value

    @property
    def dparUm(self):
        return self._dparUm

    @dparUm.setter
    def dparUm(self, value):
        self._dparUm = value

    @property
    def dperUm(self):
        return self._dperUm

    @dperUm.setter
    def dperUm(self, value):
        self._dperUm = value

    @property
    def etchingComment(self):
        return self._etchingComment

    @etchingComment.setter
    def etchingComment(self, value):
        self._etchingComment = value

    @property
    def etchingTime(self):
        return self._etchingTime

    @etchingTime.setter
    def etchingTime(self, value):
        self._etchingTime = value

    @property
    def grainCnt(self):
        return self._grainCnt

    @grainCnt.setter
    def grainCnt(self, value):
        self._grainCnt = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def incompleteData(self):
        return self._incompleteData

    @incompleteData.setter
    def incompleteData(self, value):
        self._incompleteData = value

    @property
    def mtlError(self):
        return self._mtlError

    @mtlError.setter
    def mtlError(self, value):
        self._mtlError = value

    @property
    def mtlSd(self):
        return self._mtlSd

    @mtlSd.setter
    def mtlSd(self, value):
        self._mtlSd = value

    @property
    def mtlUm(self):
        return self._mtlUm

    @mtlUm.setter
    def mtlUm(self, value):
        self._mtlUm = value

    @property
    def nd(self):
        return self._nd

    @nd.setter
    def nd(self, value):
        self._nd = value

    @property
    def neutronFlux(self):
        return self._neutronFlux

    @neutronFlux.setter
    def neutronFlux(self, value):
        self._neutronFlux = value

    @property
    def ni(self):
        return self._ni

    @ni.setter
    def ni(self, value):
        self._ni = value

    @property
    def ns(self):
        return self._ns

    @ns.setter
    def ns(self, value):
        self._ns = value

    @property
    def ohWtpct(self):
        return self._ohWtpct

    @ohWtpct.setter
    def ohWtpct(self, value):
        self._ohWtpct = value

    @property
    def rhoD(self):
        return self._rhoD

    @rhoD.setter
    def rhoD(self, value):
        self._rhoD = value

    @property
    def rhoI(self):
        return self._rhoI

    @rhoI.setter
    def rhoI(self, value):
        self._rhoI = value

    @property
    def rhoS(self):
        return self._rhoS

    @rhoS.setter
    def rhoS(self, value):
        self._rhoS = value

    @property
    def singTrackLen(self):
        return self._singTrackLen

    @singTrackLen.setter
    def singTrackLen(self, value):
        self._singTrackLen = value

    @property
    def singleGrain(self):
        return self._singleGrain

    @singleGrain.setter
    def singleGrain(self, value):
        self._singleGrain = value

    @property
    def thermDosimeterDosimeterGlassName(self):
        return self._thermDosimeterDosimeterGlassName

    @thermDosimeterDosimeterGlassName.setter
    def thermDosimeterDosimeterGlassName(self, value):
        self._thermDosimeterDosimeterGlassName = value

    @property
    def thermDosimeterId(self):
        return self._thermDosimeterId

    @thermDosimeterId.setter
    def thermDosimeterId(self, value):
        self._thermDosimeterId = value

    @property
    def thermEtchEtchant(self):
        return self._thermEtchEtchant

    @thermEtchEtchant.setter
    def thermEtchEtchant(self, value):
        self._thermEtchEtchant = value

    @property
    def thermEtchId(self):
        return self._thermEtchId

    @thermEtchId.setter
    def thermEtchId(self, value):
        self._thermEtchId = value

    @property
    def trackCnt(self):
        return self._trackCnt

    @trackCnt.setter
    def trackCnt(self, value):
        self._trackCnt = value

    @property
    def uCaRatio(self):
        return self._uCaRatio

    @uCaRatio.setter
    def uCaRatio(self, value):
        self._uCaRatio = value

    @property
    def uPpm(self):
        return self._uPpm

    @uPpm.setter
    def uPpm(self, value):
        self._uPpm = value

    @property
    def uPpmCalc(self):
        return self._uPpmCalc

    @uPpmCalc.setter
    def uPpmCalc(self, value):
        self._uPpmCalc = value

    @property
    def uPpmError(self):
        return self._uPpmError

    @uPpmError.setter
    def uPpmError(self, value):
        self._uPpmError = value

    @property
    def xiCalib(self):
        return self._xiCalib

    @xiCalib.setter
    def xiCalib(self, value):
        self._xiCalib = value

    @property
    def zeta(self):
        return self._zeta

    @zeta.setter
    def zeta(self, value):
        self._zeta = value

    @property
    def zetaErr(self):
        return self._zetaErr

    @zetaErr.setter
    def zetaErr(self, value):
        self._zetaErr = value

