
# Week 2 - Day 2 Progress Report

**Date:** 18 November 2026  
**Contributor:** Vridhi  
**Project:** TerraSpectra - Hyperspectral Crop Disease Forecasting

## 1. Objectives
- Create automated tests for EDA utilities.
- Verify data quality assessment functions.
- Test preprocessing and PCA functionality.
- Check that validation data does not affect training scaler statistics.

## 2. Work Completed

### Automated Testing
- Installed pytest.
- Created `tests/test_data_qa.py`.
- Created `tests/test_eda_utils.py`.

### Data QA Testing
- Tested class balance reporting.
- Tested train, validation and test split summaries.

### EDA Utility Testing
- Tested training-only scaler fitting.
- Verified validation data does not change fitted scaler statistics.
- Tested PCA transformation output dimensions.

## 3. Test Results

Total tests: 4  
Passed: 4  
Failed: 0

All four automated tests passed successfully.

## 4. Dataset Status
Actual hyperspectral dataset is still pending.
Testing was performed using synthetic data only.
No real dataset analysis or model performance claims are made.

## 5. Next Steps
- Continue testing preprocessing utilities.
- Add edge-case tests.
- Perform actual data quality checks when the dataset becomes available.