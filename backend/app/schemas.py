from pydantic import BaseModel, Field
from typing import List

class InferenceRequest(BaseModel):
    image_id: str
    scene_id: str

class Prediction(BaseModel):
    latitude: float
    longitude: float
    disease: str
    confidence: float = Field(ge=0, le=1)

class InferenceResponse(BaseModel):
    status: str
    predictions: List[Prediction]

class MapLayerResponse(BaseModel):
    layer_name: str
    visible: bool
    color: str