
# TerraSpectra - EDA Methodology

## 1. Dataset Inspection
Identify the dataset source, file format, image dimensions,
spectral bands, wavelength information and class labels.

## 2. Data Quality Analysis
Inspect missing values, NaN/Inf values, pixel value ranges,
data types and dimensional consistency.

## 3. Spectral Analysis
Visualize selected spectral bands using spatial plots.
Extract spectral signatures from representative pixels.
Compare signatures across available classes.

## 4. Dimensionality Reduction
Apply Principal Component Analysis (PCA) to explore
spectral dimensionality and variance distribution.
Record explained variance and cumulative explained variance.

## 5. Visualization
Generate:
- Selected band images
- Spectral signature plots
- PCA explained variance plots
- Class distribution charts
- Data quality summaries

## 6. Scientific Considerations
- PCA and preprocessing must be fitted using training data only
  when used in model evaluation.
- Disease interpretations require reliable disease labels.
- Actual findings will be recorded after dataset availability.

## Week 1 Status
EDA methodology and analysis framework prepared.
Dataset-based experiments remain pending.
