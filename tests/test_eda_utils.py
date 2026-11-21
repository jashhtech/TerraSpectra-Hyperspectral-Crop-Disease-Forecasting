
import numpy as np
import pytest

from src.eda_utils import (
    _validate_cube,
    fit_scaler,
    transform_cube,
    fit_pca,
    transform_pca,
    run_pca,
    plot_band,
    plot_spectral_signature,
)


def test_scaler_uses_training_data_only():
    train = np.random.rand(10, 8, 8, 5)[0]
    validation = np.random.rand(8, 8, 5) + 10

    scaler = fit_scaler(train)
    original_mean = scaler.mean_.copy()

    transform_cube(validation, scaler)

    np.testing.assert_array_equal(scaler.mean_, original_mean)


def test_pca_output_shape():
    cube = np.random.rand(8, 8, 5)

    pca, scaler = fit_pca(cube, n_components=3)
    result = transform_pca(cube, pca, scaler)

    assert result.shape == (8, 8, 3)


def test_validate_cube_rejects_invalid_dimensions():
    with pytest.raises(ValueError):
        _validate_cube(np.random.rand(8, 8))


def test_validate_cube_rejects_zero_bands():
    with pytest.raises(ValueError):
        _validate_cube(np.empty((8, 8, 0)))


def test_scaler_rejects_all_invalid_pixels():
    cube = np.full((4, 4, 3), np.nan)

    with pytest.raises(ValueError):
        fit_scaler(cube)


def test_transform_rejects_band_mismatch():
    train = np.random.rand(8, 8, 5)
    other = np.random.rand(8, 8, 4)

    scaler = fit_scaler(train)

    with pytest.raises(ValueError):
        transform_cube(other, scaler)


def test_pca_rejects_too_many_components():
    cube = np.random.rand(4, 4, 3)

    with pytest.raises(ValueError):
        fit_pca(cube, n_components=4)


def test_pca_preserves_invalid_pixels():
    cube = np.random.rand(8, 8, 5)
    cube[0, 0, :] = np.nan

    pca, scaler = fit_pca(cube, n_components=3)
    result = transform_pca(cube, pca, scaler)

    assert np.isnan(result[0, 0, :]).all()


def test_run_pca_returns_valid_projections():
    cube = np.random.rand(8, 8, 5)
    projections, pca, scaler, valid = run_pca(
        cube, n_components=3
    )

    assert projections.shape == (64, 3)
    assert valid.sum() == 64
    assert pca.n_components_ == 3


def test_plot_band_rejects_invalid_index():
    cube = np.random.rand(8, 8, 5)

    with pytest.raises(IndexError):
        plot_band(cube, band_index=10)


def test_spectral_signature_rejects_wrong_wavelength_count():
    cube = np.random.rand(8, 8, 5)

    with pytest.raises(ValueError):
        plot_spectral_signature(
            cube, row=0, col=0, wavelengths=[400, 500]
        )
