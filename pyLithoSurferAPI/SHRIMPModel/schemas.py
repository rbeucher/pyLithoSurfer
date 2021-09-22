import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional
from pyLithoSurferAPI.core.lists import LElevationKind, LMachineType, LSHRIMPSampleFormat, LSHRIMPAgeGroup, LSHRIMPAgeType, LErrorType


class SHRIMPDataPointSchema(pa.SchemaModel):

    class Config:
        name = "SHRIMPDataPointSchema"
        strict = True

    calibrationExponent: Optional[Series[pa.Int64]]
    commonPbModel: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    confInterval95Pct: Optional[Series[pa.Float]]
    dataDescription: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    dataReductionSoftwareVersion: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    exponentType: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    i206Pb238UCalibrationUncIncl: Optional[Series[pa.Bool]]
    i206Pb238UCalibrationUncertainty: Optional[Series[pa.Float]]
    i206Pb238UReproducabilityUncertainty: Optional[Series[pa.Float]]
    i206Pb238UReproducabilityUncertaintyIncl: Optional[Series[pa.Bool]]
    i235UDecayConstant: Optional[Series[pa.Float]]
    i238U235U: Optional[Series[pa.Float]]
    i238UDecayConstant: Optional[Series[pa.Float]]
    iMFCorrApplied: Optional[Series[pa.Bool]]
    id: Optional[Series[pa.Int64]]
    instrumentalMassFractionationIMFFactor: Optional[Series[pa.Float]]
    machineId: Optional[Series[pa.Int64]]
    machineName: Optional[Series[pa.String]] = pa.Field( nullable=True, isin=LMachineType.get_all()["name"].to_list())
    mineralOfInterestId: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    mineralOfInterestName: Optional[Series[pa.String]]
    mountCoating: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    mountIGSN: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    mountIdentifier: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    mountImagingCharacterisation: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    mountInfo: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    refMaterialId: Optional[Series[pa.Int64]]
    refMaterialName: Optional[Series[pa.String]]
    sampleFormatId: Optional[Series[pa.Int64]]
    sampleFormatName: Optional[Series[pa.String]] = pa.Field( nullable=True, isin=LSHRIMPSampleFormat.get_all()["name"].to_list())
    locationId: Series[pa.Int64] =  pa.Field( nullable=False, coerce=True)
    sampleId: Series[pa.Int64] = pa.Field( nullable=False, coerce=True)


class SHRIMPAgeSchema(pa.SchemaModel):

    class Config:
        name = "SHRIMAgeSchema"
        strict = True

    ageGroupId: Optional[Series[pa.Int64]]
    ageGroupName: Optional[Series[pa.String]] = pa.Field(nullable=True, isin=LSHRIMPAgeGroup.get_all()["name"].to_list())
    ageTypeId: Optional[Series[pa.Int64]]
    ageTypeName: Optional[Series[pa.String]] = pa.Field(nullable=True, isin=LSHRIMPAgeType.get_all()["name"].to_list())
    calcName: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Int64]]
    mswd: Optional[Series[pa.Float]]
    numberAnalysesCombined: Optional[Series[pa.Int64]]
    rmQcTest: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})

    # GeoEvent
    age: Optional[Series[pa.Float]] = pa.Field( nullable=False, coerce=True)
    ageError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    errorTypeId: Optional[Series[pa.Int64]] = pa.Field( nullable=True, coerce=True)
    errorTypeName: Optional[Series[pa.String]] = pa.Field(nullable=True, isin=LErrorType.get_all()["name"].to_list())
    geoEventId:  Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    geoEventName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)

    # Statement
    calculatedConfidence: Optional[Series[pa.Float]]
    dataPointId: Series[pa.Int64] = pa.Field( nullable=False, coerce=True)
    description: Optional[Series[pa.String]]
    geoEventAtAgeId: Optional[Series[pa.Int64]]
    humanConfidence: Optional[Series[pa.Float]]
    statementId: Optional[Series[pa.Int64]]
    relevance: Optional[Series[pa.Float]]
    tempAtAgeId: Optional[Series[pa.Int64]]
    tempGradientId: Optional[Series[pa.Int64]]