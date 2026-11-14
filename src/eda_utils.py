
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


def data_quality_report(cube):
    """Check hyperspectral cube: (height, width, bands)."""
    cube = np.asarray(cube)

    print("Shape:", cube.shape)
    print("Data type:", cube.dtype)
    print("Total values:", cube.size)
    print("NaN values:", np.isnan(cube).sum())
    print("Infinite values:", np.isinf(cube).sum())
    print("Valid min:", np.nanmin(cube))
    print("Valid max:", np.nanmax(cube))

    return cube


def plot_band(cube, band_index=0):
    """Display one spectral band."""
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
    spectrum = cube[row, col, :]

    x = wavelengths if wavelengths is not None else np.arange(len(spectrum))

    plt.figure(figsize=(10, 5))
    plt.plot(x, spectrum)
    plt.xlabel("Wavelength" if wavelengths is not None else "Band")
    plt.ylabel("Reflectance / Intensity")
    plt.title(f"Pixel spectrum ({row}, {col})")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def normalize_cube(cube):
    """Normalize bands using training-data statistics."""
    h, w, bands = cube.shape
    pixels = cube.reshape(-1, bands)

    scaler = StandardScaler()
    normalized = scaler.fit_transform(pixels)

    return normalized.reshape(h, w, bands), scaler


def run_pca(cube, n_components=3):
    """PCA on pixels; fit only on training data in final experiments."""
    h, w, bands = cube.shape
    pixels = cube.reshape(-1, bands)

    valid = np.isfinite(pixels).all(axis=1)
    valid_pixels = pixels[valid]

    scaler = StandardScaler()
    scaled = scaler.fit_transform(valid_pixels)

    pca = PCA(n_components=n_components)
    transformed = pca.fit_transform(scaled)

    print("Explained variance:", pca.explained_variance_ratio_)
    print("Cumulative variance:",
          np.cumsum(pca.explained_variance_ratio_))

    return transformed, pca, scaler, valid


def plot_pca_variance(pca):
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
    print(classification_report(
        y_true, y_pred, labels=labels, zero_division=0
    ))

    cm = confusion_matrix(y_true, y_pred, labels=labels)
    ConfusionMatrixDisplay(confusion_matrix=cm).plot()
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.show()

    return cm
