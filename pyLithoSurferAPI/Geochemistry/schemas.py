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

    locationId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    sampleId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)


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
    oxTotal: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
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
    id: Optional[Series[pa.FLoat]] = pa.Field( nullable=True, coerce=True)
    isotopeId: Optional[Series[pa.Int]] = pa.Field( nullable=False, coerce=True)
    isotopeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    spotID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})


class OxideConcentrationSchema(pa.SchemaModel):

    class Config:
        name = "OxideConcentrationSchema"
        strict = True

    aliquotName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    concentration: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    error: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    gcdataPointId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    oxideId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    oxideName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    spotID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})