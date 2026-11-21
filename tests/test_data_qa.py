
import numpy as np
import pytest

from src.data_qa import class_balance_report, split_summary


def test_class_balance_report():
    report = class_balance_report([0, 0, 1, 1, 1])
    assert report["class_count"].sum() == 5
    assert report["percentage"].sum() == 100


def test_class_balance_ignores_missing_labels():
    report = class_balance_report([0, 1, np.nan, 1])
    assert report["class_count"].sum() == 3


def test_class_balance_rejects_empty_labels():
    with pytest.raises(ValueError):
        class_balance_report([])


def test_class_balance_rejects_all_missing_labels():
    with pytest.raises(ValueError):
        class_balance_report([np.nan, np.nan])


def test_split_summary():
    summary = split_summary([0, 0, 1, 1], [0, 1], [0, 0, 1])
    assert summary is not None
    assert len(summary) > 0


def test_split_summary_ignores_missing_labels():
    summary = split_summary(
        [0, 1, np.nan],
        [0, 1],
        [1, np.nan]
    )
    assert summary.loc["0.0", "Train"] == 50
    assert summary.loc["1.0", "Train"] == 50


def test_split_summary_handles_empty_split():
    summary = split_summary([0, 1], [], [0, 1])
    assert summary["Validation"].eq(0).all()


def test_split_summary_rejects_all_empty_splits():
    with pytest.raises(ValueError):
        split_summary([], [], [])


def test_split_summary_rejects_all_missing_splits():
    with pytest.raises(ValueError):
        split_summary(
            [np.nan],
            [np.nan],
            [np.nan]
        )