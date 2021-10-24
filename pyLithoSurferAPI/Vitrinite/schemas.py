import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional

class VitriniteDataPointSchema(pa.SchemaModel):

    class Config:
        name = "VitriniteDataPointSchema"
        strict = True

    groupID: Optional[Series[pa.String]]
    id: Optional[Series[pa.Int64]]
    kerogenType: Optional[Series[pa.String]]
    nmeasure: Optional[Series[pa.String]]
    nomeas: Optional[Series[pa.Float]]
    omPct: Optional[Series[pa.Float]]
    tocPct: Optional[Series[pa.Float]]
    vrEquivMethodId: Optional[Series[pa.Float]]
    vrEquivMethodName: Optional[Series[pa.String]]
    vrEquivPct: Optional[Series[pa.Float]]
    vrEquivSourceId: Optional[Series[pa.Float]]
    vrEquivSourceName: Optional[Series[pa.String]]
    vrMax: Optional[Series[pa.Float]]
    vrMeanPct: Optional[Series[pa.Float]]
    vrMin: Optional[Series[pa.Float]]
    vrSD: Optional[Series[pa.Float]]