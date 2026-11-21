# Week 2 Progress Report (19–21 November 2026)

**Contributor:** Vridhi  
**Project:** TerraSpectra – Hyperspectral Crop Disease Forecasting  
**Branch:** `vridhi`

## 1. Work Summary

### 19 November 2026
- No verified code changes or commits recorded.
- Dataset availability remained pending.

### 20 November 2026
- No verified code changes or commits recorded.
- Continued project work was pending the next development session.

### 21 November 2026

#### Data Quality Improvements
- Improved `src/data_qa.py`.
- Added a reusable missing-label cleaning function.
- Updated class balance reporting to handle missing labels.
- Improved train, validation and test split summaries.
- Added validation for empty and all-missing label inputs.

#### Automated Testing
- Expanded `tests/test_data_qa.py`.
- Added tests for:
  - Class balance reporting.
  - Missing-label handling.
  - Empty labels.
  - All-missing labels.
  - Split summary generation.
  - Empty validation splits.
  - All-empty and all-missing splits.

#### Test Results
- Total automated tests: 11
- Passed: 11
- Failed: 0

Tests were performed using synthetic data. Actual hyperspectral dataset validation is still pending.

## 2. GitHub Update

**Branch:** `vridhi`

**Latest commit:** `059fc3c`

**Commit message:** `test: improve data QA edge case handling`

Changes successfully pushed to the remote repository.

Working tree status: Clean.

## 3. Pending Work
- Obtain and verify the actual hyperspectral dataset.
- Inspect missing values and invalid pixels in real data.
- Verify class labels and sample distribution.
- Perform real-data spectral analysis and PCA.
- Continue preprocessing and evaluation work after dataset verification.

## 4. Conclusion

Data QA utilities and automated testing have been improved. All 11 automated tests passed successfully using synthetic data. Actual dataset-based analysis remains pending dataset availability.