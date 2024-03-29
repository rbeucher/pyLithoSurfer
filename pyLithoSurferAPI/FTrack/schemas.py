import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional


class FTBinnedLengthDataSchema(pa.SchemaModel):

    class Config:
        name = "FTBinnedLengthDataSchema"
        strict = True
    
    cfIrradiation: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True)
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    dParAvg: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dParError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dParNumTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPer: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPerError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPerNumTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dperErrorTypeId: Optional[Series[pa.Int]] = pa.Field( nullable=True, coerce=True)
    dperErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftdataPointId: Optional[Series[pa.Int]] = pa.Field( nullable=True, coerce=True)
    i0x1: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i10x11: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True) 
    i11x12: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i12x13: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i13x14: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i14x15: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i15x16: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i16x17: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i17x18: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i18x19: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i19x20: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i1x2: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i2x3: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i3x4: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i4x5: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i5x6: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i6x7: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i7x8: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i8x9: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    i9x10: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    id: Optional[Series[pa.Int]] = pa.Field( nullable=True, coerce=True)


class FTCountDataSchema(pa.SchemaModel):

    class Config:
        name = "FTCountDataSchema"
        strict = True

    area: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    dPar: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dParError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dParNum: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPer: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPerError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPerNum: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    errorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    errorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftdataPointId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    grainName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ni: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ns: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rhoS: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rhoi: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)


class FTDataPointSchema(pa.SchemaModel):

    class Config:
        name = "FTDataPointSchema"
        strict = True

    ageErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ageErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ageComment: Optional[Series[pa.String]] = pa.Field( nullable=True)
    meanAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    centralAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pooledAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    popAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    analyticalSessionID: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    area: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    chi2pct: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    description: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    dPar: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dParNumTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dParStandardError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPer: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPerNumTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPerStandardError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dispersion: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dosimeterId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dosimeterName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    meanErrorMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    centralErrorMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pooledErrorMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    popErrorMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    etchantId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    etchantName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    etchingTemp: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    etchingTime: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftUDeterminationTechniqueId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftUDeterminationTechniqueName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftAgeEquationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftAgeEquationName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftCharacterisationMethodId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftCharacterisationMethodName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftAnalyticalSoftwareId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftAnalyticalSoftwareName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftAnalyticalAlgorithmId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftAnalyticalAlgorithmName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    irradiationReactorId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    irradiationReactorName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    kParameter: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kParameterStandardError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lambdaFId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lambdaFName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    lambdaId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lambdaName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    machineId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    machineName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mineralId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    mineralName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mountID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    mountIDCount: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    mountIDLength: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    mtl: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    mtl1se: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    nTracks: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    nd: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    neutronDose: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ni: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    noOfGrains: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ns: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    population: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    popTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    popTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    qEfficiencyFactor: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    range: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    referenceMaterialId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    referenceMaterialName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})   
    rhoS: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rhod: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rhoi: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rmr0: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rmr0EquationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rmr0EquationName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    rmr0StandardError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    stdDevMu: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCaRatio: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCaRatioError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)  
    uCont: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uStandardError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaCalibration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    cfIrradiation: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True)

    locationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    sampleId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)

    
class FTLengthDataSchema(pa.SchemaModel):

    class Config:
        name = "FTLengthDataSchema"
        strict = True

    apparentLength: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    azimuth: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    cAxisAngle: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    cAxisCorrectedLength: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    correctedZDepth: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPar: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dParError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dParNum: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPer: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPerError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPerNum: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dip: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    errorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    errorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftdataPointId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    grainName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rmr0: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kParameter: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    trackLength: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    trackID: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    trackTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    trackTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})


class FTSingleGrainSchema(pa.SchemaModel):

    class Config:
        name = "FTSingleGrainSchema"
        strict = True

    ageErrorMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ageErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ageErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ageMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftdataPointId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    grainName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kParameter: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rmr0: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCont: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCaRatio: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCaRatioError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uerrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uerrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})