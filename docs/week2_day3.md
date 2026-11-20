# TerraSpectra – Week 2 Day 3

**Role:** ML Model & Inference Engineer  
**Task:** 3D-CNN Dataset Integration and Training Preparation

## 1. Objective

The objective of Day 3 is to integrate the hyperspectral dataset with the developed 3D-CNN architecture and prepare the model training pipeline.

## 2. Work Completed

- Reviewed the existing hyperspectral dataset interface.
- Connected the dataset loader with the 3D-CNN model.
- Prepared the input tensor conversion required for 3D convolution.
- Implemented training and validation data loaders.
- Added the Cross Entropy loss function.
- Configured the Adam optimizer.
- Implemented the training and validation loops.
- Added model checkpoint-saving functionality.

## 3. Technical Implementation

The following technologies were used:

- Python
- PyTorch
- Hyperspectral Dataset
- 3D Convolutional Neural Network
- DataLoader
- Adam Optimizer
- Cross Entropy Loss

## 4. Model Input

The 3D-CNN expects a five-dimensional input tensor:

(Batch Size, Channels, Spectral Bands, Height, Width)

The dataset output is converted into this format before being passed to the model.

## 5. Expected Outcome

- Integrate the dataset with the 3D-CNN architecture.
- Prepare the training and validation workflow.
- Calculate training and validation accuracy.
- Save the trained model checkpoint.

## 6. Limitations

Actual model performance depends on the availability and verification of the real hyperspectral dataset. Training results must be recorded only after successfully running the pipeline on the actual dataset.

## 7. Next Day Plan

Evaluate the 3D-CNN model using suitable classification metrics such as accuracy, precision, recall, and F1-score.
