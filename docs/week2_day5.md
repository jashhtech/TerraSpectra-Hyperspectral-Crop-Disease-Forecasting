# TerraSpectra – Week 2 Day 5

**Role:** ML Model & Inference Engineer  
**Task:** 3D-CNN Model Improvement and Performance Analysis

## 1. Objective

The objective of Day 5 is to improve the 3D-CNN training process and make model training more stable and reliable.

## 2. Work Completed

- Improved the existing 3D-CNN training pipeline.
- Added reproducible random seed settings.
- Implemented weight decay to help reduce overfitting.
- Added a learning rate scheduler.
- Implemented early stopping.
- Added validation loss monitoring.
- Implemented best model checkpoint saving.

## 3. Techniques Used

| Technique | Purpose |
|---|---|
| Random Seed | Improves reproducibility |
| Weight Decay | Helps control overfitting |
| Learning Rate Scheduler | Adjusts learning rate during training |
| Early Stopping | Stops training when validation performance stops improving |
| Best Checkpoint | Saves the model with the lowest validation loss |

## 4. Expected Outcome

The improved pipeline provides better control over model training, monitors validation performance, and saves the best-performing checkpoint.

## 5. Limitations

Actual performance improvement must be verified using the real hyperspectral dataset. Validation results alone do not establish final test performance.

## 6. Next Day Plan

Compare the baseline CNN and 3D-CNN models and document their performance using suitable evaluation metrics.
