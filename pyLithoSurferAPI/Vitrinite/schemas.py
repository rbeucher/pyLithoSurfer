import pandera as pa
from pandera.typing import Series
from typing import Optional

class VitriniteDataPointSchema(pa.SchemaModel):

    class Config:
        name = "VitriniteDataPointSchema"
        strict = True

    id: Optional[Series[pa.Int64]]
    comment: Optional[Series[pa.String]] =  pa.Field( nullable=True)
    groupID: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    hi: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    kerogenTypeId: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    kerogenTypeName: Optional[Series[pa.String]] =  pa.Field( nullable=True)
    nmeasure: Optional[Series[pa.String]] =  pa.Field( nullable=True)
    nomeas: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    oi: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    omPct: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    pi: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    s1: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    s2: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    s3: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    tMax: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    tocPct: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    vrEquivMethodId: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    vrEquivMethodName: Optional[Series[pa.String]] =  pa.Field( nullable=True)
    vrEquivPct: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    vrEquivSourceId: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    vrEquivSourceName: Optional[Series[pa.String]] =  pa.Field( nullable=True)
    vrMax: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    vrMeanPct: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    vrMin: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    vrSD: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)

    dataPackageName: Series[pa.String] = pa.Field(coerce=True)
    dataPackageId: Optional[Series[pa.String]] = pa.Field(coerce=True)
    locationId: Series[pa.Int64] =  pa.Field( nullable=False, coerce=True)
    sampleId: Series[pa.Int64] = pa.Field( nullable=False, coerce=True)