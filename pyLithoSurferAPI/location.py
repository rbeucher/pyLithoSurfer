from . import session, URL_BASE
import json


class location(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def lat(self):
        return self._lat

    @lat.setter
    def lat(self, value):
        self._lat = value

    @property
    def locCaptureId(self):
        return self._locCaptureId

    @locCaptureId.setter
    def locCaptureId(self, value):
        self._locCaptureId = value

    @property
    def locCaptureMethod(self):
        return self._locCaptureMethod

    @locCaptureMethod.setter
    def locCaptureMethod(self, value):
        self._locCaptureMethod = value

    @property
    def locName(self):
        return self._locName

    @locName.setter
    def locName(self, value):
        self._locName = value

    @property
    def locPredefinedId(self):
        return self._locPredefinedId

    @locPredefinedId.setter
    def locPredefinedId(self, value):
        self._locPredefinedId = value

    @property
    def locPredefinedName(self):
        return self._locPredefinedName

    @locPredefinedName.setter
    def locPredefinedName(self, value):
        self._locPredefinedName = value

    @property
    def locationGroupIdx(self):
        return self._locationGroupIdx

    @locationGroupIdx.setter
    def locationGroupIdx(self, value):
        self._locationGroupIdx = value

    @property
    def lockKindId(self):
        return self._lockKindId

    @lockKindId.setter
    def lockKindId(self, value):
        self._lockKindId = value

    @property
    def lockKindKind(self):
        return self._lockKindKind

    @lockKindKind.setter
    def lockKindKind(self, value):
        self._lockKindKind = value

    @property
    def lon(self):
        return self._lon

    @lon.setter
    def lon(self, value):
        self._lon = value

    @property
    def precisionM(self):
        return self._precisionM

    @precisionM.setter
    def precisionM(self, value):
        self._precisionM = value

    @property
    def qcIdx(self):
        return self._qcIdx

    @qcIdx.setter
    def qcIdx(self, value):
        self._qcIdx = value

    @property
    def uploadIdx(self):
        return self._uploadIdx

    @uploadIdx.setter
    def uploadIdx(self, value):
        self._uploadIdx = value

