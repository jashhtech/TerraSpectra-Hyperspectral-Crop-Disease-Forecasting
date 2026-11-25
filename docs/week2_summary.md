# TerraSpectra – Week 2 Progress Report

**Role:** ML Model & Inference Engineer  
**Week:** 2 (November 17–23, 2026)

## 1. Introduction

During Week 2, I focused on developing and improving the 3D-CNN model for hyperspectral crop disease classification.

The main objective was to prepare the model architecture, integrate the dataset, develop the training pipeline, and establish model evaluation methods.

## 2. Day-wise Work Completed

### Day 1 – Dataset Verification
- Reviewed the hyperspectral dataset requirements.
- Identified the expected dataset format.
- Studied spectral bands and image dimensions.
- Prepared the dataset verification documentation.

### Day 2 – 3D-CNN Architecture
- Studied 3D convolutional neural networks.
- Created `src/model_3dcnn.py`.
- Implemented 3D convolution layers.
- Added activation, pooling, and classification layers.

### Day 3 – Dataset Integration and Training
- Created `src/train_3dcnn.py`.
- Connected the dataset loader with the 3D-CNN model.
- Implemented training and validation loops.
- Added checkpoint-saving functionality.

### Day 4 – Model Evaluation
- Created `src/evaluate_3dcnn.py`.
- Implemented accuracy, precision, recall, and F1-score calculations.
- Added confusion matrix generation.
- Prepared a classification report.

### Day 5 – Model Improvement
- Improved the training pipeline.
- Added weight decay and learning rate scheduling.
- Implemented early stopping.
- Added best checkpoint saving.
- Prepared training performance analysis.

### Day 6 – Model Comparison
- Created `src/compare_models.py`.
- Prepared baseline CNN and 3D-CNN comparison.
- Added common classification metrics.
- Prepared CSV output for comparison results.

### Day 7 – Weekly Review
- Reviewed the developed source files.
- Organized weekly documentation.
- Reviewed the remaining dataset requirements.
- Prepared the development plan for Week 3.

## 3. Files Developed

| File | Purpose |
|---|---|
| `src/model_3dcnn.py` | 3D-CNN architecture |
| `src/train_3dcnn.py` | 3D-CNN training pipeline |
| `src/evaluate_3dcnn.py` | Model evaluation |
| `src/compare_models.py` | Model comparison |
| `src/analyze_training.py` | Training performance analysis |
| `docs/week2_day1.md` | Dataset verification report |
| `docs/week2_day2.md` | 3D-CNN architecture report |
| `docs/week2_day3.md` | Dataset integration report |
| `docs/week2_day4.md` | Model evaluation report |
| `docs/week2_day5.md` | Model improvement report |
| `docs/week2_day5_analysis.md` | Training analysis report |
| `docs/week2_day6.md` | Model comparison report |
| `docs/week2_summary.md` | Weekly progress report |

## 4. Technologies Used

- Python
- PyTorch
- NumPy
- Scikit-learn
- Matplotlib
- YAML
- 3D-CNN Architecture

## 5. Challenges and Limitations

- Actual hyperspectral dataset integration needs verification.
- Dataset dimensions and class labels must be confirmed.
- Training and evaluation require actual dataset files.
- Model comparison requires trained checkpoints and a separate test dataset.
- Actual performance metrics must be recorded after successful execution.

## 6. Week 3 Plan

- Study Vision Transformer architecture.
- Develop a Vision Transformer prototype.
- Explore hyperspectral feature extraction.
- Compare CNN and Transformer approaches.
- Develop an inference wrapper.
- Prepare model prediction functionality.

## 7. Conclusion

During Week 2, I prepared the initial 3D-CNN architecture, dataset integration pipeline, model evaluation methods, and model comparison framework.

These developments establish the foundation for exploring advanced deep learning architectures and inference development in Week 3.
