# TerraSpectra – Week 2 Day 4

**Role:** ML Model & Inference Engineer  
**Task:** 3D-CNN Model Evaluation

## 1. Objective

The objective of Day 4 is to evaluate the performance of the developed 3D-CNN model using standard classification metrics.

## 2. Work Completed

- Created `src/evaluate_3dcnn.py`.
- Implemented trained model checkpoint loading.
- Prepared model prediction functionality.
- Added accuracy calculation.
- Added precision and recall metrics.
- Implemented F1-score calculation.
- Generated a confusion matrix.
- Added a classification report.

## 3. Evaluation Metrics

| Metric | Purpose |
|---|---|
| Accuracy | Measures overall correct predictions |
| Precision | Measures how many positive predictions are correct |
| Recall | Measures how many actual positive samples are identified |
| F1-score | Combines precision and recall |
| Confusion Matrix | Shows correct and incorrect classifications |

## 4. Expected Outcome

The evaluation pipeline provides a systematic way to measure the classification performance of the 3D-CNN model.

## 5. Limitations

Evaluation results depend on the quality of the dataset and trained checkpoint. Final performance should be reported using a separate test dataset that was not used during training.

## 6. Next Day Plan

Analyze the evaluation results, identify model limitations, and explore improvements to the 3D-CNN architecture.
