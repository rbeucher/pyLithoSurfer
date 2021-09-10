import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional
from pyLithoSurferAPI.core.lists import LElevationKind


class SampleSchema(pa.SchemaModel):
    
    archiveId: Optional[Series[pa.Int64]]
    archiveName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    archiveNote: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    collectDateMax: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 10})
    collectDateMin: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 10})
    dataPackageId: Optional[Series[pa.Int64]]
    dataPackageName: Optional[Series[pa.String]]
    description: Optional[Series[pa.String]] = pa.Field(nullable=True)
    id: Optional[Series[pa.Int64]]
    igsn: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    igsnHandleURL: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    igsnMintingTimestamp: Optional[Series[pa.DateTime]]
    locationId: Optional[Series[pa.Int64]]
    locationKindId: Optional[Series[pa.Int64]]
    locationKindName: Optional[Series[pa.String]]
    locationName: Optional[Series[pa.String]]
    materialId: Optional[Series[pa.Float]] = pa.Field(coerce=True, nullable=True)
    materialName: Optional[Series[pa.String]]  = pa.Field(coerce=True, nullable=True)
    name: Series[pa.String] = pa.Field(nullable=False, coerce=True, str_length={"min_value": 0, "max_value": 255})
    referenceElevation: Optional[Series[pa.Float]] = pa.Field(nullable=True, coerce=True)
    referenceElevationKindId: Optional[Series[pa.Int64]]
    referenceElevationKindName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, isin=LElevationKind.get_all()["name"].to_list())
    referenceElevationKindNote: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    referenceElevationSource: Series[pa.String]
    relativeElevationAccuracy: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    relativeElevationMax: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    relativeElevationMin: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True) 
    sampleKindId: Optional[Series[pa.Int64]]
    sampleKindName: Optional[Series[pa.String]]
    sampleMethodId: Optional[Series[pa.Int64]]
    sampleMethodName: Optional[Series[pa.String]]
    sourceId: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    stratographicUnitId: Optional[Series[pa.Int64]]
    stratographicUnitName: Optional[Series[pa.String]]


class LocationSchema(pa.SchemaModel):
    
    calcName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    captureMethodId: Optional[Series[pa.Int64]]
    captureMethodName: Optional[Series[pa.String]]
    celestialId: Optional[Series[pa.Int64]]
    celestialName: Optional[Series[pa.String]]
    description: Optional[Series[pa.String]] = pa.Field( nullable=True)
    id: Optional[Series[pa.Int64]]
    lat: Series[pa.Float] = pa.Field( nullable=False, coerce=True, ge=-90, le=90)
    latLonPrecision: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lon: Series[pa.Float] = pa.Field( nullable=False, coerce=True, ge=-180., le=180)
    name: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})


class DataPointSchema(pa.SchemaModel):

    dataEntityId: Optional[Series[pa.Int64]]
    dataPackageId: Series[pa.Int64]
    dataPackageName: Optional[Series[pa.String]]
    dataStructure: Series[pa.String] = pa.Field()
    description: Optional[Series[pa.String]]
    externalDataHref: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Int64]]
    locationId: Series[pa.Int64]
    locationName: Optional[Series[pa.String]]
    name: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    sampleId: Series[pa.Int64]
    sampleName: Optional[Series[pa.String]] 
    shrimpdataPointId: Series[pa.Int64]
    sourceId: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})



class GeoEventAtAgeSchema(pa.SchemaModel):
    
    age: Series[pa.Float]
    ageError: Optional[Series[pa.Float]]
    errorTypeId: Optional[Series[pa.Int64]]
    errorTypeName: Optional[Series[pa.String]]
    geoEventId: Optional[Series[pa.Int64]]
    geoEventName: Optional[Series[pa.String]]
    id: Optional[Series[pa.Int64]]
    shrimpageId: Optional[Series[pa.Int64]]


class StatementSchema(pa.SchemaModel):

    calculatedConfidence: Optional[Series[pa.Int32]]
    dataPointId: Optional[Series[pa.Int64]]
    description: Optional[Series[pa.String]] 
    geoEventAtAgeId: Optional[Series[pa.Int64]]
    humanConfidence: Optional[Series[pa.Int32]]
    id: Optional[Series[pa.Int64]]
    relevance: Optional[Series[pa.Float]]
    tempAtAgeId: Optional[Series[pa.Int64]]
    tempGradientId: Optional[Series[pa.Int64]]


class PersonSchema(pa.SchemaModel):
    
    calcName: Optional[Series[pa.String]]
    firstName: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    id: Optional[Series[pa.Int64]]
    name: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    note: Optional[Series[pa.String]]
    orcId: Optional[Series[pa.String]]
    title: Optional[Series[pa.String]]