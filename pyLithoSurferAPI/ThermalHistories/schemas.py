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
    dataPackageId: Optional[Series[pa.Float]] = pa.Field(coerce=True)
    laboratory: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Associated Literature")
    analyst: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Analyst")
    modelSoftware: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Model Software") 
    modelApproach: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Model Approach")
    modelType: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Model Type")
    modelIterations: Optional[Series[pa.Float]] = pa.Field(coerce=True, alias="Number of Model iterations")
    finalTemperature: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Final Mean Temp. Constraint")
    finalTemperatureRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Final Temp. ± Range")
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

    datapointName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Datapoint Key")
    sampleName: Series[pa.String] = pa.Field( coerce=True, nullable=False, alias="Sample Name")
    sampleId: Optional[Series[pa.Float]] = pa.Field( coerce=True)
    description: Optional[Series[pa.String]] = pa.Field(coerce=True, nullable=True, alias="Description")


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
    kinematicIndicatorId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kinematicIndicatorName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
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
    
    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Datapoint Key")
    sampleName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Sample Name")
    aliquotID: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, str_length={"max_value": 255}, alias="Aliquot ID")
    mineral: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Mineral")
    mineralId: Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True)    
    populationID: Optional[Series[pa.Float]] = pa.Field( coerce=True, nullable=True, alias="Population (if any)")    
    populationTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    populationTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Population Type")
    dataTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    dataTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Data Type")
    projectedLengths: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True, alias="Were FT lengths projected to C-axis?")
    implantedTracks: Optional[Series[pa.Bool]] = pa.Field( nullable=True, coerce=True, alias="Were Californium tracks implanted?")
    annealingModelId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    annealingModelName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias= "FT Annealing Model")
    kinematicIndicatorId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    kinematicIndicatorName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="FT Kinematic Indicator")
    diffusionModelId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    diffusionModelName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="He Diffusion Model")
    datapointIDId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    datapointIDName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Data Point")

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

    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Datapoint Key")
    sampleName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Sample Name")
    pathTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    pathTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Path Type")
    modelTemp: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Temperature")
    modelTime: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Time")

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
    literatureCalcName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True)
    literatureId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    thdataPointId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)


class THModelConstraintBatchSchema(pa.SchemaModel):

    class Config:
        name = "THModelConstraintBatchSchema"
        strict = True

    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Datapoint Key")
    literature: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Literature")
    constraintTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    constraintTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Constraint Type")
    constraintTempMean: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Constrain mean temperature")
    constraintTempRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Constrain temperature range")
    constraintTimeMean: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Constrain mean time")
    constraintTimeRange: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="constrain time range")
    description: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Model Comment")


class THPredResultSchema(pa.SchemaModel):

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

class THPredResultBatchSchema(pa.SchemaModel):

    class Config:
        name = "THPredResultBatchSchema"
        strict = True

    dataPointName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Datapoint Key")
    sampleName: Optional[Series[pa.String]] = pa.Field( nullable=True, str_length={"max_value": 255}, alias="Sample Name")   
    predictedParameterId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    predictedParameterName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Predicted Parameter")   
    predictedResult: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Predicted Result")
    predictedUncertainty: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Predicted Result Uncertainty")
    uncertaintyTypeId: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True)
    uncertaintyTypeName: Optional[Series[pa.String]] = pa.Field( nullable=True, coerce=True, alias="Predicted Result Uncertainty Type")
    predictedGOF: Optional[Series[pa.Float]] = pa.Field( nullable=True, coerce=True, alias="Predicted Goodness of Fit")