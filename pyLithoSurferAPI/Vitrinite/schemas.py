import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional

class VitriniteDataPointSchema(pa.SchemaModel):

    class Config:
        name = "VitriniteDataPointSchema"
        strict = True

    groupID: Optional[Series[pa.String]]
    id: Optional[Series[pa.Int64]]
    groupID: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    kerogenType: Optional[Series[pa.String]] =  pa.Field( nullable=True)
    nmeasure: Optional[Series[pa.String]] =  pa.Field( nullable=True)
    nomeas: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    omPct: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
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
    tMax: Optional[Series[pa.Float]] =  pa.Field( nullable=True, coerce=True)
    locationId: Series[pa.Int64] =  pa.Field( nullable=False, coerce=True)
    sampleId: Series[pa.Int64] = pa.Field( nullable=False, coerce=True)