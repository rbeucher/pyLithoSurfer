import pandera as pa
from pandera.typing import Index, DataFrame, Series
from typing import Optional


class THDataPointSchema(pa.SchemaModel):

    class Config:
        name = "THDataPointSchema"
        strict = True

    finalTemperature: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    finalTemperatureRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    modelApproachName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    modelIterations: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    modelSoftwareName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    modelTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    temperatureGradient: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    temperatureGradientRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    variableOffset: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True)

    dataPackageName: Series[pa.String] = pa.Field(coerce=True)
    dataPackageId: Optional[Series[pa.String]] = pa.Field(coerce=True)

    
class THDataPointBatchSchema(pa.SchemaModel):

    class Config:
        name = "THDataPointBatchSchema"
        strict = True

    Tag: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Key")
    dataPackageName: Series[pa.String] = pa.Field(coerce=True, alias="Datapackage Name")
    dataPackageId: Optional[Series[pa.Float]] = pa.Field(coerce=True, alias="Datapackage NameId")
    laboratory: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Associated Literature")
    analyst: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Analyst")
    modelSoftware: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Model Software") 
    modelApproach: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Model Approach")
    modelType: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Model Type")
    modelIterations: Optional[Series[pa.Float]] = pa.Field(coerce=True, alias="Number of Model iterations")
    temperatureGradient: Optional[Series[pa.Float]] = pa.Field(coerce=True, alias="Temperature Gradient")
    temperatureGradientRange: Optional[Series[pa.Float]] = pa.Field(coerce=True, alias="Temperature Gradient Range")
    temperatureGradientRange: Optional[Series[pa.Float]] = pa.Field(coerce=True, alias="Temperature Gradient Range")
    variableOffset: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True, alias="Offset Allowed to Vary?")
    description: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Model Comment")


class THistSchema(pa.SchemaModel):

    class Config:
        name = "THistSchema"
        strict = True

    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    name: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    sampleName: Series[pa.String] = pa.Field( coerce=True, nullable=False)
    sampleId: Optional[Series[pa.Float]] = pa.Field( coerce=True)
    thdataPointId: Optional[Series[pa.Int]] = pa.Field( nullable=False, coerce=True)
    description: Optional[Series[pa.String]] = pa.Field(coerce=True)

class THistBatchSchema(pa.SchemaModel):

    class Config:
        name = "THistBatchSchema"
        strict = True


class THistInputSchema(pa.SchemaModel):

    class Config:
        name = "THistInputSchema"
        strict = True

    aliquotID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    annealingModelId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    annealingModelName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    dataTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dataTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    datapointIDId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    datapointIDName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    diffusionModelId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    diffusionModelName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    histRef: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    implantedTracks: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True)
    kinematicTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kinematicTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    mineral: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mineralId: Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)    
    populationID: Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)    
    populationTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    populationTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    thdataPointId: Optional[Series[pa.Int]] = pa.Field( nullable=False, coerce=True)
    projectedLengths: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True)


class THistInputBatchSchema(pa.SchemaModel):

    class Config:
        name = "THistInputBatchSchema"
        strict = True
    
    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    histRef: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    aliquotID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255})
    mineral: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    mineralId: Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)    
    populationID: Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)    
    populationTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    populationTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    annealingModelId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    annealingModelName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    dataTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dataTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    kinematicTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kinematicTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    diffusionModelId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    diffusionModelName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    projectedLengths: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True)
    implantedTracks: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True)
    datapointIDId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    datapointIDName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)

class THistNickPointSchema(pa.SchemaModel):

    class Config:
        name = "THistNickPointSchema"
        strict = True
    
    histRef: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    modelTemp: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    modelTime: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pathTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pathTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    thdataPointId: Optional[Series[pa.Int]] = pa.Field( nullable=False, coerce=True)


class THistNickPointBatchSchema(pa.SchemaModel):

    class Config:
        name = "THistNickPointBatchSchema"
        strict = True

    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    histRef: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    pathTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pathTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    modelTemp: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    modelTime: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)

class THModelConstraintSchema(pa.SchemaModel):

    class Config:
        name = "THModelConstraintSchema"
        strict = True
    
    constraintTempMean: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    constraintTempRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    constraintTimeMean: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    constraintTimeRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    constraintTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    constraintTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    description: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Model Comment")


class THModelConstraintBatchSchema(pa.SchemaModel):

    class Config:
        name = "THModelConstraintBatchSchema"
        strict = True

    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    literature: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    constraintTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    constraintTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    constraintTempMean: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    constraintTempRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    constraintTimeMean: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    constraintTimeRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    description: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Model Comment")


class TPredResultSchema(pa.SchemaModel):

    class Config:
        name = "THPredResultSchema"
        strict = True

    histRef: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})
    id: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    predictedGOF: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    predictedParameterId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    predictedParameterName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    predictedResult: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    predictedUncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thdataPointId: Optional[Series[pa.Int]] = pa.Field( nullable=False, coerce=True)
    uncertaintyTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncertaintyTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)

class TPredResultBatchSchema(pa.SchemaModel):

    class Config:
        name = "THPredResultBatchSchema"
        strict = True

    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    histRef: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255})   
    predictedParameterId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    predictedParameterName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)   
    predictedResult: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    predictedUncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncertaintyTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncertaintyTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    predictedGOF: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)