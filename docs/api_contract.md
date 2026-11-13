# TerraSpectra API Contract

## Health API

GET /health

Response:
{
  "status": "healthy"
}

## Inference API

POST /inference/predict

Input:
- image_id
- scene_id

Output:
- disease
- confidence
- latitude
- longitude

## Map Layer

Map output:
- prediction coordinates
- disease category
- confidence score