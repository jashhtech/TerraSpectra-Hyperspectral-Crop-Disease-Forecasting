\# Week 2: Dataset Validation Report



\## Dataset

UAV-Based Multispectral Maize Dataset (Corrected v2.1)



Source: https://zenodo.org/records/22062459



\## Dataset Structure

\- Image patches: 1,792

\- Mask files: 1,792

\- Patch dimensions: 224 x 224

\- Spectral channels: 6

\- Image format: NPY

\- Mask format: PNG



\## Spectral Band Order

1\. Blue

2\. Green

3\. Red

4\. Red-edge

5\. NIR

6\. Alpha



\## Validation Results

\- Matched image-mask pairs: 1,792

\- Missing masks: 0

\- Missing images: 0

\- Valid image shapes: 1,792

\- Mask dimensions: 224 x 224

\- Mask classes: 0, 1, 2, 3, 4

\- Empty masks: 96

\- Validation errors: 0



\## Implementation

Created src/dataset\_validator.py to validate image-mask

pairing, patch shapes, mask dimensions, mask classes,

and empty masks directly from the ZIP archive.



\## Status

Dataset structural validation completed successfully.

