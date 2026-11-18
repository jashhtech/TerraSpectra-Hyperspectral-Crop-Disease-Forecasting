
import numpy as np
from src.eda_utils import (
    fit_scaler,
    transform_cube,
    fit_pca,
    transform_pca
)


def test_scaler_uses_training_data_only():
    train_cube = np.random.rand(8, 8, 5)
    val_cube = np.random.rand(8, 8, 5) + 10

    scaler = fit_scaler(train_cube)
    train_mean = scaler.mean_.copy()

    transform_cube(val_cube, scaler)

    np.testing.assert_array_equal(scaler.mean_, train_mean)


def test_pca_output_shape():
    train_cube = np.random.rand(8, 8, 5)

    scaler = fit_scaler(train_cube)
    pca, _ = fit_pca(train_cube, n_components=3, scaler=scaler)

    projection = transform_pca(train_cube, pca, scaler)

    assert projection.shape == (8, 8, 3)