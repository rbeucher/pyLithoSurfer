from . import session, URL_BASE
import json


class trackLength(object):

    def __init__(self, *args, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def cAxisAng(self):
        return self._cAxisAng

    @cAxisAng.setter
    def cAxisAng(self, value):
        self._cAxisAng = value

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
    def corrTrackLength(self):
        return self._corrTrackLength

    @corrTrackLength.setter
    def corrTrackLength(self, value):
        self._corrTrackLength = value

    @property
    def dpar(self):
        return self._dpar

    @dpar.setter
    def dpar(self, value):
        self._dpar = value

    @property
    def dper(self):
        return self._dper

    @dper.setter
    def dper(self, value):
        self._dper = value

    @property
    def i0x1(self):
        return self._i0x1

    @i0x1.setter
    def i0x1(self, value):
        self._i0x1 = value

    @property
    def i0x2(self):
        return self._i0x2

    @i0x2.setter
    def i0x2(self, value):
        self._i0x2 = value

    @property
    def i10x11(self):
        return self._i10x11

    @i10x11.setter
    def i10x11(self, value):
        self._i10x11 = value

    @property
    def i10x12(self):
        return self._i10x12

    @i10x12.setter
    def i10x12(self, value):
        self._i10x12 = value

    @property
    def i11x12(self):
        return self._i11x12

    @i11x12.setter
    def i11x12(self, value):
        self._i11x12 = value

    @property
    def i12x13(self):
        return self._i12x13

    @i12x13.setter
    def i12x13(self, value):
        self._i12x13 = value

    @property
    def i12x14(self):
        return self._i12x14

    @i12x14.setter
    def i12x14(self, value):
        self._i12x14 = value

    @property
    def i13x14(self):
        return self._i13x14

    @i13x14.setter
    def i13x14(self, value):
        self._i13x14 = value

    @property
    def i14x15(self):
        return self._i14x15

    @i14x15.setter
    def i14x15(self, value):
        self._i14x15 = value

    @property
    def i14x16(self):
        return self._i14x16

    @i14x16.setter
    def i14x16(self, value):
        self._i14x16 = value

    @property
    def i15x16(self):
        return self._i15x16

    @i15x16.setter
    def i15x16(self, value):
        self._i15x16 = value

    @property
    def i16x17(self):
        return self._i16x17

    @i16x17.setter
    def i16x17(self, value):
        self._i16x17 = value

    @property
    def i16x18(self):
        return self._i16x18

    @i16x18.setter
    def i16x18(self, value):
        self._i16x18 = value

    @property
    def i17x18(self):
        return self._i17x18

    @i17x18.setter
    def i17x18(self, value):
        self._i17x18 = value

    @property
    def i18x19(self):
        return self._i18x19

    @i18x19.setter
    def i18x19(self, value):
        self._i18x19 = value

    @property
    def i18x20(self):
        return self._i18x20

    @i18x20.setter
    def i18x20(self, value):
        self._i18x20 = value

    @property
    def i19x20(self):
        return self._i19x20

    @i19x20.setter
    def i19x20(self, value):
        self._i19x20 = value

    @property
    def i1x2(self):
        return self._i1x2

    @i1x2.setter
    def i1x2(self, value):
        self._i1x2 = value

    @property
    def i2x3(self):
        return self._i2x3

    @i2x3.setter
    def i2x3(self, value):
        self._i2x3 = value

    @property
    def i2x4(self):
        return self._i2x4

    @i2x4.setter
    def i2x4(self, value):
        self._i2x4 = value

    @property
    def i3x4(self):
        return self._i3x4

    @i3x4.setter
    def i3x4(self, value):
        self._i3x4 = value

    @property
    def i4x5(self):
        return self._i4x5

    @i4x5.setter
    def i4x5(self, value):
        self._i4x5 = value

    @property
    def i4x6(self):
        return self._i4x6

    @i4x6.setter
    def i4x6(self, value):
        self._i4x6 = value

    @property
    def i5x6(self):
        return self._i5x6

    @i5x6.setter
    def i5x6(self, value):
        self._i5x6 = value

    @property
    def i6x7(self):
        return self._i6x7

    @i6x7.setter
    def i6x7(self, value):
        self._i6x7 = value

    @property
    def i6x8(self):
        return self._i6x8

    @i6x8.setter
    def i6x8(self, value):
        self._i6x8 = value

    @property
    def i7x8(self):
        return self._i7x8

    @i7x8.setter
    def i7x8(self, value):
        self._i7x8 = value

    @property
    def i8x10(self):
        return self._i8x10

    @i8x10.setter
    def i8x10(self, value):
        self._i8x10 = value

    @property
    def i8x9(self):
        return self._i8x9

    @i8x9.setter
    def i8x9(self, value):
        self._i8x9 = value

    @property
    def i9x10(self):
        return self._i9x10

    @i9x10.setter
    def i9x10(self, value):
        self._i9x10 = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def kurtosisPercent(self):
        return self._kurtosisPercent

    @kurtosisPercent.setter
    def kurtosisPercent(self, value):
        self._kurtosisPercent = value

    @property
    def skewnessPercent(self):
        return self._skewnessPercent

    @skewnessPercent.setter
    def skewnessPercent(self, value):
        self._skewnessPercent = value

    @property
    def trackLength(self):
        return self._trackLength

    @trackLength.setter
    def trackLength(self, value):
        self._trackLength = value

    @property
    def trackLengthErr(self):
        return self._trackLengthErr

    @trackLengthErr.setter
    def trackLengthErr(self, value):
        self._trackLengthErr = value

