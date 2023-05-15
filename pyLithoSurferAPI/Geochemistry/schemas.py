import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional


class GCDataPointSchema(pa.SchemaModel):

    class Config:
        name = "GCDataPointSchema"
        strict = True

    analysisScaleId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    analysisScaleName:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    analyticalSessionID:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    batchID:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    dataReductionSoftwareId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dataReductionSoftwareName:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    elementErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    elementErrorTypeName:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    geochemAnalyticalTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    geochemAnalyticalTypeName:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    laicpmsid: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    mineralId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    mineralName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mountID: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    oxideErrorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    oxideErrorTypeName:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    referenceMaterialId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    referenceMaterialName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})

    dataPackageName: Series[pa.String] = pa.Field(coerce=True)
    dataPackageId: Optional[Series[pa.String]] = pa.Field(coerce=True)
    locationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    sampleId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    description: Optional[Series[pa.String]] = pa.Field(coerce=True)

class GCDataPointBatchSchema(pa.SchemaModel):

    class Config:
        name = "GCDataPointBatchSchema"
        strict = True

    Tag: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Datapoint Name")
    dataPackageName: Series[pa.String] = pa.Field(coerce=True, alias="Datapackage Name")
    dataPackageId: Optional[Series[pa.Float]] = pa.Field(coerce=True, alias="Datapackage NameId")
    sampleName: Series[pa.String] = pa.Field( coerce=True, nullable=False, alias="Sample Name")
    sampleId: Optional[Series[pa.Float]] = pa.Field( coerce=True, alias="Sample NameId")
    description: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    geochemAnalyticalType:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    geochemAnalyticalTypeId:  Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)
    dataReductionSoftware:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    dataReductionSoftwareId:  Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)
    analyticalSessionID:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    analyst: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    batchID:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mountID: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    analysisScale:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    analysisScaleId:  Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)
    mineral: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mineralId: Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)
    oxideUncertaintyType:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    oxideUncertaintyTypeId:  Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)
    elementUncertaintyType:  Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    elementUncertaintyTypeId:  Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)

class GCAliquotSchema(pa.SchemaModel):

    class Config:
        name = "GCAliquotSchema"
        strict = True

    aliquotName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    domainId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    domainName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    elementTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    gcdataPointId: Optional[Series[pa.Int]] = pa.Field( nullable=False, coerce=True)
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    oxideTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    spotID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})

class ElementalConcentrationSchema(pa.SchemaModel):

    class Config:
        name = "ElementalConcentrationSchema"
        strict = True

    aliquotName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    concentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    elementId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    elementName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    error: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    gcdataPointId: Optional[Series[pa.Int]] = pa.Field( nullable=False, coerce=True)
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    isotopeId: Optional[Series[pa.Int]] = pa.Field( nullable=False, coerce=True)
    isotopeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    spotID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})

class ElementalConcentrationBatchSchema(pa.SchemaModel):

    class Config:
        name = "ElementalConcentrationBatchSchema"
        strict = True

    gcDatapointId: Series[pa.Int] = pa.Field( nullable=False, coerce=True)
    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Datapoint Name")
    aliquotName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    aliquotNameId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    concentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Conc")
    elementId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    element: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    uncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Uncertainty")
    spotID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    
class OxideConcentrationBatchSchema(pa.SchemaModel):

    class Config:
        name = "OxideConcentrationBatchSchema"
        strict = True

    aliquotName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    concentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    error: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    gcDatapointId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    oxideId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    oxideName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    spotID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})