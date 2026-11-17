
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


def _validate_cube(cube):
    """Validate hyperspectral cube format: (height, width, bands)."""
    cube = np.asarray(cube, dtype=np.float64)

    if cube.ndim != 3:
        raise ValueError("Cube must have shape (height, width, bands).")

    if cube.shape[2] == 0:
        raise ValueError("Cube must contain spectral bands.")

    return cube


def data_quality_report(cube):
    """Check hyperspectral cube quality."""
    cube = _validate_cube(cube)

    print("Shape:", cube.shape)
    print("Data type:", cube.dtype)
    print("Total values:", cube.size)
    print("NaN values:", np.isnan(cube).sum())
    print("Infinite values:", np.isinf(cube).sum())

    valid = cube[np.isfinite(cube)]

    if valid.size:
        print("Valid min:", valid.min())
        print("Valid max:", valid.max())
    else:
        print("No finite values found.")

    return cube


def plot_band(cube, band_index=0):
    """Display one spectral band."""
    cube = _validate_cube(cube)

    if not 0 <= band_index < cube.shape[2]:
        raise IndexError("Invalid band index.")

    plt.figure(figsize=(8, 6))
    plt.imshow(cube[:, :, band_index], cmap="viridis")
    plt.colorbar(label="Pixel intensity")
    plt.title(f"Band {band_index}")
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.tight_layout()
    plt.show()


def plot_spectral_signature(cube, row, col, wavelengths=None):
    """Plot reflectance spectrum for one pixel."""
    cube = _validate_cube(cube)
    spectrum = cube[row, col, :]

    x = wavelengths if wavelengths is not None else np.arange(len(spectrum))

    if len(x) != len(spectrum):
        raise ValueError("Wavelength count must match number of bands.")

    plt.figure(figsize=(10, 5))
    plt.plot(x, spectrum)
    plt.xlabel("Wavelength" if wavelengths is not None else "Band")
    plt.ylabel("Reflectance / Intensity")
    plt.title(f"Pixel spectrum ({row}, {col})")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def fit_scaler(train_cube):
    """Fit StandardScaler using training pixels only."""
    train_cube = _validate_cube(train_cube)
    bands = train_cube.shape[2]
    pixels = train_cube.reshape(-1, bands)

    valid = np.isfinite(pixels).all(axis=1)

    if not valid.any():
        raise ValueError("Training cube contains no valid pixels.")

    scaler = StandardScaler()
    scaler.fit(pixels[valid])

    return scaler


def transform_cube(cube, scaler):
    """Transform a cube using an already-fitted training scaler."""
    cube = _validate_cube(cube)
    h, w, bands = cube.shape

    if bands != scaler.n_features_in_:
        raise ValueError("Cube band count does not match fitted scaler.")

    pixels = cube.reshape(-1, bands)
    valid = np.isfinite(pixels).all(axis=1)

    normalized = np.full(pixels.shape, np.nan, dtype=np.float64)

    if valid.any():
        normalized[valid] = scaler.transform(pixels[valid])

    return normalized.reshape(h, w, bands)


def normalize_cube(train_cube, scaler=None):
    """
    Fit on training data if scaler is not supplied.
    For validation/test data, always pass the training scaler.
    """
    if scaler is None:
        scaler = fit_scaler(train_cube)

    normalized = transform_cube(train_cube, scaler)

    return normalized, scaler


def fit_pca(train_cube, n_components=3, scaler=None):
    """Fit scaler and PCA using training pixels only."""
    train_cube = _validate_cube(train_cube)
    bands = train_cube.shape[2]

    if not 1 <= n_components <= bands:
        raise ValueError("n_components must be between 1 and band count.")

    if scaler is None:
        scaler = fit_scaler(train_cube)

    h, w, _ = train_cube.shape
    pixels = train_cube.reshape(-1, bands)
    valid = np.isfinite(pixels).all(axis=1)

    if valid.sum() < n_components:
        raise ValueError("Not enough valid training pixels for PCA.")

    scaled = scaler.transform(pixels[valid])

    pca = PCA(n_components=n_components)
    pca.fit(scaled)

    print("Explained variance:", pca.explained_variance_ratio_)
    print("Cumulative variance:",
          np.cumsum(pca.explained_variance_ratio_))

    return pca, scaler


def transform_pca(cube, pca, scaler):
    """Apply training-fitted scaler and PCA to any data cube."""
    cube = _validate_cube(cube)
    h, w, bands = cube.shape

    if bands != scaler.n_features_in_:
        raise ValueError("Cube band count does not match fitted scaler.")

    pixels = cube.reshape(-1, bands)
    valid = np.isfinite(pixels).all(axis=1)

    output = np.full(
        (pixels.shape[0], pca.n_components_),
        np.nan,
        dtype=np.float64
    )

    if valid.any():
        scaled = scaler.transform(pixels[valid])
        output[valid] = pca.transform(scaled)

    return output.reshape(h, w, pca.n_components_)


def run_pca(train_cube, n_components=3):
    """Fit PCA on training data and return training projections."""
    pca, scaler = fit_pca(train_cube, n_components)
    transformed = transform_pca(train_cube, pca, scaler)

    valid = np.isfinite(train_cube).all(axis=2)

    return transformed[valid], pca, scaler, valid


def plot_pca_variance(pca):
    """Plot cumulative explained variance."""
    plt.figure(figsize=(8, 5))
    plt.plot(
        np.arange(1, len(pca.explained_variance_ratio_) + 1),
        np.cumsum(pca.explained_variance_ratio_),
        marker="o"
    )
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Explained Variance")
    plt.title("PCA Explained Variance")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def evaluate_predictions(y_true, y_pred, labels=None):
    """Evaluate classification predictions."""
    print(classification_report(
        y_true, y_pred, labels=labels, zero_division=0
    ))

    cm = confusion_matrix(y_true, y_pred, labels=labels)
    ConfusionMatrixDisplay(confusion_matrix=cm).plot()
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.show()

    return cm
