import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional
from pyLithoSurferAPI.core.lists import LElevationKind, LErrorType

class AgeDataPointSchema(pa.SchemaModel):

    class Config:
        name = "AgeDataPointSchema"
        strict = True

    id: Optional[Series[pa.Int64]]
    locationId: Series[pa.Int64] =  pa.Field( nullable=False, coerce=True)
    sampleId: Series[pa.Int64] = pa.Field( nullable=False, coerce=True)
    analyticalMethodId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    analyticalMethodName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)

    # GeoEvent
    age: Optional[Series[pa.Float]] = pa.Field( nullable=False, coerce=True)
    ageError: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    errorTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    errorTypeName: Optional[Series[pa.String]] = pa.Field(nullable=True, isin=LErrorType.get_all()["name"].to_list())
    geoEventId:  Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    geoEventName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)

    # Statement
    calculatedConfidence: Optional[Series[pa.Float]]= pa.Field( nullable=True, coerce=True)
    description: Optional[Series[pa.String]]= pa.Field( nullable=True)
    geoEventAtAgeId: Optional[Series[pa.Int64]]= pa.Field( nullable=True)
    humanConfidence: Optional[Series[pa.Float]]= pa.Field( nullable=True, coerce=True)
    statementId: Optional[Series[pa.Int64]]= pa.Field( nullable=True)
    relevance: Optional[Series[pa.Float]]= pa.Field( nullable=True, coerce=True)
    tempAtAgeId: Optional[Series[pa.Int64]]= pa.Field( nullable=True)
    tempGradientId: Optional[Series[pa.Int64]]= pa.Field( nullable=True)

    dataPackageName: Series[pa.String] = pa.Field(coerce=True)
    dataPackageId: Optional[Series[pa.String]] = pa.Field(coerce=True)
    locationId: Series[pa.Float] = pa.Field( nullable=True, coerce=True)
    sampleId: Series[pa.Float] = pa.Field( nullable=True, coerce=True)