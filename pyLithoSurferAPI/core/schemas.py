import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional
from pyLithoSurferAPI.core.lists import LElevationKind, LLocationKind, LSampleKind, LSampleMethod, LCelestial, LErrorType, LGeoEvent
from pyLithoSurferAPI.core.tables import Archive
from pyLithoSurferAPI.management.tables import DataPackage

class SampleSchema(pa.SchemaModel):

    class Config:
        name = "SampleSchema"
        strict = True
    
    archiveId: Optional[Series[pa.Int64]]
    archiveName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, isin=Archive.get_all()["name"].to_list())
    archiveNote: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    collectDateMax: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 10})
    collectDateMin: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 10})
    dataPackageId: Optional[Series[pa.Int64]]
    dataPackageName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, isin=DataPackage.get_all()["name"].to_list())
    description: Optional[Series[pa.String]] = pa.Field(nullable=True)
    id: Optional[Series[pa.Int64]]
    igsn: Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255})
    igsnHandleURL: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    igsnMintingTimestamp: Optional[Series[pa.DateTime]]
    locationId: Optional[Series[pa.Int64]]
    locationKindId: Optional[Series[pa.Int64]]
    locationKindName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, isin=LLocationKind.get_all()["name"].to_list())
    locationName: Optional[Series[pa.String]]
    materialId: Optional[Series[pa.Float]] = pa.Field(coerce=True, nullable=True)
    materialName: Optional[Series[pa.String]]  = pa.Field(coerce=True, nullable=True)
    name: Series[pa.String] = pa.Field(nullable=False, coerce=True, str_length={"min_value": 0, "max_value": 255})
    referenceElevation: Optional[Series[pa.Float]] = pa.Field(nullable=True, coerce=True)
    referenceElevationKindId: Optional[Series[pa.Int64]]
    referenceElevationKindName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, isin=LElevationKind.get_all()["name"].to_list())
    referenceElevationKindNote: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    referenceElevationSource:  Optional[Series[pa.String]]
    relativeElevationAccuracy: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    relativeElevationMax: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    relativeElevationMin: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True) 
    sampleKindId: Optional[Series[pa.Int64]]
    sampleKindName: Optional[Series[pa.String]] = pa.Field(nullable=True, isin=LSampleKind.get_all()["name"].to_list())
    sampleMethodId: Optional[Series[pa.Int64]]
    sampleMethodName: Optional[Series[pa.String]]= pa.Field(nullable=True, isin=LSampleMethod.get_all()["name"].to_list())
    sourceId: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    stratographicUnitId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    stratographicUnitName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)


class LocationSchema(pa.SchemaModel):

    class Config:
        name = "LocationSchema"
        strict = True
    
    calcName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    captureMethodId: Optional[Series[pa.Int64]]
    captureMethodName: Optional[Series[pa.String]]
    celestialId: Optional[Series[pa.Int64]]
    celestialName: Optional[Series[pa.String]] = pa.Field( nullable=False, isin=LCelestial.get_all()["name"].to_list())
    description: Optional[Series[pa.String]] = pa.Field( nullable=True)
    id: Optional[Series[pa.Int64]]
    lat: Series[pa.Float] = pa.Field( nullable=False, coerce=True, ge=-90, le=90)
    latLonPrecision: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    lon: Series[pa.Float] = pa.Field( nullable=False, coerce=True, ge=-180., le=180)
    name: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})


class DataPointSchema(pa.SchemaModel):

    class Config:
        name = "DataPointSchema"
        strict = True

    dataEntityId: Optional[Series[pa.Int64]]
    dataPackageId: Series[pa.Int64]
    dataPackageName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, isin=DataPackage.get_all()["name"].to_list())
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

    class Config:
        name = "GeoEventAtAgeSchema"
        strict = True

    age: Series[pa.Float]
    ageError: Optional[Series[pa.Float]]
    errorTypeId: Optional[Series[pa.Int64]]
    errorTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, isin=LErrorType.get_all()["name"].to_list())
    geoEventId: Optional[Series[pa.Int64]]
    geoEventName: Optional[Series[pa.String]] = pa.Field( nullable=True, isin=LGeoEvent.get_all()["name"].to_list())
    id: Optional[Series[pa.Int64]]
    shrimpageId: Optional[Series[pa.Int64]]


class StatementSchema(pa.SchemaModel):
    
    class Config:
        name = "StatementSchema"
        strict = True

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
    
    class Config:
        name = "PersonSchema"
        strict = True
    
    calcName: Optional[Series[pa.String]]
    firstName: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    id: Optional[Series[pa.Int64]]
    name: Series[pa.String] = pa.Field( nullable=False, str_length={"max_value": 255})
    note: Optional[Series[pa.String]]
    orcId: Optional[Series[pa.String]]
    title: Optional[Series[pa.String]]


class LiteratureSchema(pa.SchemaModel):
    
    class Config:
        name = "LiteratureSchema"
        strict = True
    
    abstr: Optional[Series[pa.String]] = pa.Field( nullable=True)
    author: Series[pa.String]
    booktitle: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    chapter: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    doi: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    editor: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    howpublished: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    institution: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    issn: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    journal: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    keywords: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    language: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    litNumber: Optional[Series[pa.String]] = pa.Field(nullable=True, coerce=True, str_length={"max_value": 255})
    litOrganization: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    litType: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    note: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    otherId: Optional[Series[pa.Int]] = pa.Field(nullable=True, str_length={"max_value": 255})
    pages: Optional[Series[pa.String]] = pa.Field(nullable=True, coerce=True, str_length={"max_value": 255})
    pubMonth: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    pubYear: Series[pa.Int] = pa.Field(nullable=True, coerce=True, str_length={"max_value": 255})
    publisher: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    school: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    series: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    sourceId: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    title: Series[pa.String]
    url: Optional[Series[pa.String]] = pa.Field(nullable=True, str_length={"max_value": 255})
    volume: Optional[Series[pa.Int]] = pa.Field(nullable=True, str_length={"max_value": 255})



class StratigraphicUnitSchema(pa.SchemaModel):

    baseAge: Optional[Series[pa.Float]]
    baseAgeName: Optional[Series[pa.String]]
    createdById:  Optional[Series[pa.Int]]
    createdTimestamp:  Optional[Series[pa.String]]
    description: Optional[Series[pa.String]]
    event: Optional[Series[pa.String]]
    geologicalProvince: Optional[Series[pa.String]]
    id:  Optional[Series[pa.Int]]
    lastEditedById:  Optional[Series[pa.Int]]
    lastEditedTimestamp: Optional[Series[pa.String]]
    name: Optional[Series[pa.String]]
    rank: Optional[Series[pa.String]]
    source:  Optional[Series[pa.String]]  = pa.Field( nullable=True, str_length={"max_value": 255}, isin=["MANUAL_ENTRY", "ASUD", "MACROSTRAT"])
    sourceId:  Optional[Series[pa.String]]  = pa.Field( nullable=True, coerce=True)
    thicknessMax: Optional[Series[pa.Float]]
    thicknessMin: Optional[Series[pa.Float]]
    topAge: Optional[Series[pa.Float]]
    topAgeName: Optional[Series[pa.String]]
