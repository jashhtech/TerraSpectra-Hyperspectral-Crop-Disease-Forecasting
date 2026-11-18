
import numpy as np
from src.data_qa import class_balance_report, split_summary


def test_class_balance_report():
    labels = np.array([0, 0, 1, 1, 1])

    report = class_balance_report(labels, split_name="Test")

    assert report is not None
    assert len(report) > 0


def test_split_summary():
    y_train = np.array([0, 0, 1, 1])
    y_val = np.array([0, 1])
    y_test = np.array([0, 0, 1])

    summary = split_summary(y_train, y_val, y_test)

    assert summary is not None
    assert len(summary) > 0
