# TerraSpectra – Week 2 Day 2

**Role:** ML Model & Inference Engineer  
**Task:** 3D-CNN Model Architecture Development

## 1. Objective

The objective of Day 2 is to design an initial 3D-CNN architecture for processing hyperspectral image data.

## 2. Work Completed

- Studied the working principle of 3D convolutional neural networks.
- Created `src/model_3dcnn.py`.
- Implemented three 3D convolution layers.
- Added ReLU activation functions.
- Added max pooling and adaptive average pooling.
- Implemented a classification layer.
- Prepared a dummy-input test to verify the model output dimensions.

## 3. Technologies Used

- Python
- PyTorch
- 3D Convolution
- ReLU Activation
- Max Pooling
- Adaptive Average Pooling

## 4. Expected Outcome

The model should accept a 3D hyperspectral input tensor and produce class scores for crop disease classification.

## 5. Limitations

The architecture was tested using dummy input data only. Actual dataset integration, training, and performance evaluation are pending.

## 6. Next Day Plan

Integrate the verified hyperspectral dataset with the 3D-CNN model and prepare the training pipeline.
