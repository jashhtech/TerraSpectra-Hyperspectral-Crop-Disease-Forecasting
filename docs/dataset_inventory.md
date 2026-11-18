

\# TerraSpectra Dataset Inventory



\## 1. Project Information

\- Project: TerraSpectra

\- Module: Data \& Dataset Pipeline

\- Owner: Hepsiba



\## 2. Dataset Selection Status

\- Dataset name: Pending confirmation

\- Source: Pending

\- License: Pending verification

\- Crop type: Pending

\- Disease/stress labels: Pending verification



\## 3. Hyperspectral Data Details

\- File format: Pending inspection

\- Number of spectral bands: Pending inspection

\- Wavelength information: Pending inspection

\- Spatial resolution: Pending inspection

\- Acquisition details: Pending inspection



\## 4. Dataset Quality

\- Missing values: Not checked

\- Invalid pixels: Not checked

\- Label consistency: Not checked

\- Data integrity: Not checked



\## 5. Model Compatibility

\- Expected input format: NPZ

\- Expected arrays: cubes, labels

\- Expected shape: (N, Bands, Height, Width)

\- Configured patch size: 64 x 64

\- Configured classes: 2 (provisional)



\## 6. Notes

Dataset source, actual format, spectral dimensions,

and class definitions must be verified before preprocessing.









\## 7. Dataset Candidates



\### Candidate 1: Wheat Septoria Hyperspectral Dataset

\- Source: Recherche Data Gouv / INRAE

\- Disease: Septoria tritici blotch

\- Crop: Durum wheat

\- Images: 1,175

\- Leaves: 3,326

\- Spectral ranges: VNIR and SWIR

\- Acquisition dates: 18

\- Labels: Healthy and infected

\- License: Etalab Open License 2.0

\- Status: Candidate - not yet approved



\### Candidate 2: Sugarcane-HSI

\- Crop: Sugarcane

\- Images: 3,245

\- Diseases: Sugarcane Mosaic Virus and smut

\- Labels: Infected and control

\- License: CC BY 4.0

\- Approximate size: 3.5 TB

\- Status: Candidate - large download



\### Candidate 3: Apple Fire Blight

\- Crop: Apple

\- Classes: Healthy, infected and water-stressed

\- Formats: ENVI HDR/DAT and CSV annotations

\- Approximate size: 48.4 GB

\- License: Etalab Open License 2.0

\- Status: Candidate - not yet approved



# TerraSpectra Dataset Inventory

## 1. Project Information
- Project: TerraSpectra
- Module: Data & Dataset Pipeline
- Owner: Hepsiba

## 2. Dataset Selection Status
- Dataset name: Pending final confirmation
- Primary candidate: UAV Maize Common Rust Dataset
- Source: Zenodo
- Source link: https://zenodo.org/records/22062459
- License: CC BY 4.0 (to be verified from dataset documentation)
- Crop type: Maize
- Disease/stress labels: Common rust, healthy, water stress and soil
- Status: Under evaluation

## 3. Hyperspectral / Multispectral Data Details
- File format: Pending inspection
- Number of spectral channels: 6 (multispectral candidate)
- Wavelength information: Pending inspection
- Spatial resolution: Pending inspection
- Acquisition details: UAV-based field imagery

## 4. Dataset Quality
- Missing values: Not checked
- Invalid pixels: Not checked
- Label consistency: Not checked
- Data integrity: Not checked

## 5. Model Compatibility
- Expected input format: NPZ
- Expected arrays: cubes, labels
- Expected shape: (N, Bands, Height, Width)
- Configured patch size: 64 x 64
- Configured classes: 2 (provisional)
- Model compatibility: Pending inspection and confirmation

## 6. Notes
Dataset source, actual file format, spectral dimensions, label definitions and model compatibility must be verified before preprocessing.

The UAV Maize dataset is multispectral, not hyperspectral. Its suitability for the final project pipeline requires team confirmation.

## 7. Dataset Candidates

### Candidate 1: Wheat Septoria Hyperspectral Dataset
- Source: Recherche Data Gouv / INRAE
- Disease: Septoria tritici blotch
- Crop: Durum wheat
- Images: 1,175
- Leaves: 3,326
- Spectral ranges: VNIR and SWIR
- Acquisition dates: 18
- Labels: Healthy and infected
- License: Etalab Open License 2.0
- Status: Candidate - not approved (laboratory leaf-level data)

### Candidate 2: Sugarcane-HSI
- Crop: Sugarcane
- Images: 3,245
- Diseases: Sugarcane Mosaic Virus and smut
- Labels: Infected and control
- License: CC BY 4.0
- Approximate size: 3.5 TB
- Status: Candidate - large download

### Candidate 3: Apple Fire Blight
- Crop: Apple
- Classes: Healthy, infected and water-stressed
- Formats: ENVI HDR/DAT and CSV annotations
- Approximate size: 48.4 GB
- License: Etalab Open License 2.0
- Status: Candidate - not approved

### Candidate 4: UAV Maize Common Rust Dataset
- Source: Zenodo
- Crop: Maize
- Disease: Common rust
- Data type: UAV multispectral imagery
- Spectral channels: 6
- Labels/classes: Healthy maize, common rust, water stress and soil
- Label type: Vegetation-index-guided pseudo-label masks
- License: CC BY 4.0
- Approximate dataset size: 1.4 GB
- Status: Candidate - under evaluation

## 8. Next Steps
- Download and extract selected dataset files.
- Inspect image patches and metadata.
- Verify spectral channels and wavelength information.
- Inspect label masks and class distribution.
- Check data quality and integrity.
- Confirm compatibility with the model pipeline.
- Finalize dataset selection with the project team.