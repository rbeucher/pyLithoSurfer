import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional


class FTBinnedLengthDataSchema(pa.SchemaModel):

    class Config:
        name = "FTBinnedLengthDataSchema"
        strict = True
    
    cfIrradiation: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True)
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    dParAvg: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 5.})
    dParError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 5.})
    dParNumTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPer: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 5.})
    dPerError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 5.})
    dPerNumTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    etchingTime:   Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftdataPointId: Optional[Series[pa.Int]] = pa.Field( nullable=True, coerce=True)
    i0x1:   Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
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
    mountID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)


class FTCountDataSchema(pa.SchemaModel):

    class Config:
        name = "FTCountDataSchema"
        strict = True

    area: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    dPar: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 5.})
    dParUncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 5.})
    dParNum: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPer: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 5.})
    dPerUncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 5.})
    dPerNum: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncertaintyTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncertaintyTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
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
    ageUncertaintyTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ageUncertaintyTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ageComment: Optional[Series[pa.String]] = pa.Field( nullable=True)
    meanAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    centralAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    pooledAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    popAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    analyticalSessionID: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    area: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    chi2pct: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    description: Optional[Series[pa.String]] = pa.Field( nullable=True)
    dPar: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 10.})
    dParNumTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dParStandardError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPer: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 3.})
    dPerNumTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPerStandardError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 3})
    dispersion: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dosimeterId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dosimeterName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    meanAgeUncertaintyMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    centralAgeUncertaintyMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    pooledAgeUncertaintyMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    popAgeUncertaintyMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    etchantId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    etchantName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    etchingTemp: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    etchingTime: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    etchableRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftUDeterminationTechniqueId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftUDeterminationTechniqueName: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    ftAgeEquationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftAgeEquationName: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    ftCharacterisationMethodId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftCharacterisationMethodName: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    ftAnalyticalSoftwareId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftAnalyticalSoftwareName: Optional[Series[pa.String]] = pa.Field( nullable=False, str_length={"max_value": 255})
    ftAnalyticalAlgorithmId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftAnalyticalAlgorithmName: Optional[Series[pa.String]] = pa.Field( nullable=False, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    irradiationReactorId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    irradiationReactorName: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    irradiationBatch: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    kParameter: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kParameterStandardDeviation: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lambdaFId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lambdaFName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    lambdaId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lambdaName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    machineId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    machineName: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    mineralId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    mineralName: Series[pa.String] = pa.Field( nullable=True, str_length={"max_value": 255})
    batchID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    mtl: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 20.})
    mtl1se: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 20.})
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
    rmr0StandardDeviation: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    stdDevMu: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCaRatio: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCaRatioStandardDeviation: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)  
    uCont: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uStandardDeviation: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaCalibration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaUncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaUncertaintyTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaUncertaintyTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    cfIrradiation: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True)

    dataPackageName: Series[pa.String] = pa.Field(coerce=True)
    dataPackageId: Optional[Series[pa.String]] = pa.Field(coerce=True)
    locationId: Series[pa.Float] = pa.Field( nullable=True, coerce=True)
    sampleId: Series[pa.Float] = pa.Field( nullable=True, coerce=True)


class FTDataPointBatchSchema(pa.SchemaModel):

    class Config:
        name = "FTDataPointBatchSchema"
        strict = True   

    datapackageName: Series[pa.String] = pa.Field(coerce=True)
    dataPackageId: Optional[Series[pa.Float]] = pa.Field(coerce=True)
    datapointName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    sampleName: Series[pa.String] = pa.Field( coerce=True, nullable=False)
    sampleId: Optional[Series[pa.Float]] = pa.Field(coerce=True) 
    description: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    literature: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    laboratory: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    analyst: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    funding: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mineral: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mineralId: Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)    
    mountID: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    referenceMaterialId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    referenceMaterialName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})      
    batchID:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftCharacterisationMethodId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftCharacterisationMethodName: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    ftAnalyticalSoftwareId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftAnalyticalSoftwareName: Optional[Series[pa.String]] = pa.Field( nullable=False, str_length={"max_value": 255})
    ftAnalyticalAlgorithmId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftAnalyticalAlgorithmName: Optional[Series[pa.String]] = pa.Field( nullable=False, str_length={"max_value": 255})
    ftUDeterminationTechniqueId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftUDeterminationTechniqueName: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    noOfGrains: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    area: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    rhod: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    nd: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rhoS: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ns: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rhoi: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ni: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dosimeter: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    uCont: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uStandardDeviation: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCaRatio: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCaRatioStandardDeviation: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)  
    dPar: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 10.})
    dParStandardError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dParNumTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPer: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 10.})
    dPerStandardError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 3})
    dPerNumTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rmr0: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rmr0StandardDeviation: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kParameter: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kParameterStandardDeviation: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rmr0Equation: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    chi2pct: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dispersion:  Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftAgeEquation: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    meanAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    meanUncertaintyMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    centralAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    centralAgeUncertaintyMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pooledAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pooledAgeUncertaintyMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    popAgeMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    popAgeUncertaintyMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ageUncertaintyType: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ageComment: Optional[Series[pa.String]] = pa.Field( nullable=True)
    mtl: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    mtl1se: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    nTracks: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    stdDevMu: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    cfIrradiation: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True)
    etchant: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    etchingTime: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    etchingTemp: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaCalibration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaUncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaUncertaintyTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zetaUncertaintyTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    etchableRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lambdaFId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lambdaFName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    lambdaId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lambdaName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    qEfficiencyFactor: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    irradiationReactor: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    neutronDose: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    irradiationBatch: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    machine: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    Tag: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})

class FTLengthDataSchema(pa.SchemaModel):

    class Config:
        name = "FTLengthDataSchema"
        strict = True

    apparentLength: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 20.})
    azimuth: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 180.})
    cAxisAngle: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 180})
    cAxisCorrectedLength: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 20.})
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    correctedZDepth: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPar: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 10.})
    dParUncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 3.})
    dParNum: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dPer: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 10.})
    dPerError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 10.})
    dPerNum: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dip: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 90})
    uncertaintyTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncertaintyTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftdataPointId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    grainName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rmr0: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 20.})
    kParameter: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    trackLength: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)#, in_range={"min_value": 0., "max_value": 20.})
    trackID: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    trackTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    trackTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})


class FTSingleGrainSchema(pa.SchemaModel):

    class Config:
        name = "FTSingleGrainSchema"
        strict = True

    ageUncertaintyMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    ageUncertaintyTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ageUncertaintyTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ageMa: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 9999})
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftdataPointId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    grainName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kParameter: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rmr0: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, in_range={"min_value": 0., "max_value": 20.})
    uCont: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uUncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCaRatio: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uCaRatioUncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uUncertaintyTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uUncertaintyTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
