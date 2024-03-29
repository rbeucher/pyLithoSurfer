import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional


class HeWholeGrainSchema(pa.SchemaModel):

    class Config:
        name = "HeWholeGrainSchema"
        strict = True

    aliquotID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    aliquotMass: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    aliquotMassError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    aliquotMassErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    aliquotMassErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    aliquotTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    aliquotTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    assumedMineralDensity: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    avgAliquotHeightSD: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    avgAliquotLengthSD: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    avgAliquotSurfaceAreaSD: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    avgAliquotVolumeSD: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    avgAliquotWidthSD: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    caContent: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    caContentError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    correctedHeAge: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    crysFragId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    crysFragName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    eU: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    eUError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    euerrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    euerrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ft: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    aliquotGeometryId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    aliquotGeometryName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    aliquotHeight: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    aliquotLength: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    aliquotMorphologyId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    aliquotMorphologyName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    aliquotSurfaceArea: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    aliquotVolume: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    aliquotWidth: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4Amount: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4AmountError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4AmountErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4AmountErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    he4Concentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4ConcentrationError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4ConcentrationErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4ConcentrationErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    heDataPointId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    minChemFormula: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    numAliquots: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rFT: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rSV: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smAmount: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smAmountError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smAmountErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smAmountErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    smConcentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smConcentrationError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smConcentrationErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smConcentrationErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    tau: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    tauErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    tauErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    tauFT: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    tauFTErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    tauFTErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    thAmount: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thAmountError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thAmountErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thAmountErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    thConcentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thConcentrationError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thConcentrationErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thConcentrationErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    thURatio: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uAmount: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uAmountError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uConcentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uConcentrationError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uamountErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uamountErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    uconcentrationErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uconcentrationErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    uncorrectedHeAge: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncorrectedHeAgeError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncorrectedHeAgeErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncorrectedHeAgeErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    vsRatio: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zrContent: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zrContentError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zrContentErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    zrContentErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    

class HeDataPointSchema(pa.SchemaModel):

    class Config:
        name = "HeDataPointSchema"
        strict = True

    alphaStopDistRefId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    alphaStopDistRefName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    analyticalSessionID: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    chi2pctCorrected: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    chi2pctUncorrected: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    confidenceInterval95Corrected: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    confidenceInterval95Uncorrected: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    correctedHeAgeMethodId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    correctedHeAgeMethodName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    euequationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    euequationName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    ftEquationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    ftEquationName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    grainDimensionEquationsId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    grainDimensionEquationsName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    heAgeEquationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    heAgeEquationName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    iqrCorrected: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    iqrUncorrected: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    meanCorrectedHeAge: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    meanCorrectedHeAgeError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    meanCorrectedHeAgeErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    meanCorrectedHeAgeErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    meanUncorrectedHeAge: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    meanUncorrectedHeAgeError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    meanUncorrectedHeAgeErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    meanUncorrectedHeAgeErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mineralId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    mineralName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mountID: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mswdCorrected: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    mswdUncorrected: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    numAliquots: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    referenceMaterialId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    referenceMaterialName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    rftequationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rftequationName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    rsvequationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    rsvequationName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    uncertaintyComment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    weightedMeanCorrectedHeAge: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    weightedMeanCorrectedHeAgeError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    weightedMeanCorrectedHeAgeErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    weightedMeanCorrectedHeAgeErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    weightedMeanUncorrectedHeAge: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    weightedMeanUncorrectedHeAgeError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    weightedMeanUncorrectedHeAgeErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    weightedMeanUncorrectedHeAgeErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})

    locationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    sampleId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)

    
class HeInSituSchema(pa.SchemaModel):

    class Config:
        name = "HeInSituSchema"
        strict = True

    ageCalibrationFactor: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    comment: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    correctedHeAge: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    crysFragId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    crysFragName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    eU: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    eUError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    euerrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    euerrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    grainID: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    he4Amount: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4AmountError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4AmountErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4AmountErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    he4Concentraion: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4ConcentrationError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4ConcentrationErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    he4ConcentrationErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    heDataPointId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pParentPitVolumeError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    parentPitVolume: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    parentPitVolumeError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    parentPitVolumeErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    parentPitVolumeErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    pitRelationshipId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pitRelationshipName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    pitVolume: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pitVolumeErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pitVolumeErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    smAmount: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smAmountError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smAmountErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smAmountErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    smConcentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smConcentrationError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smConcentrationErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    smConcentrationErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    tau: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    tauErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    tauErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    thAmount: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thAmountError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thAmountErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thAmountErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    thConcentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thConcentrationError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thConcentrationErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thConcentrationErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    uAmount: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uAmountError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uConcentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uConcentrationError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uamountErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uamountErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    uconcentrationErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uconcentrationErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}),
    uncorrectedHeAge: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncorrectedHeAgeError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncorrectedHeAgeErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncorrectedHeAgeErrorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})  