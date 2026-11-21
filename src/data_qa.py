
import numpy as np
import pandas as pd


def _clean_labels(labels):
    """Flatten labels and remove missing values."""
    labels = np.asarray(labels).ravel()
    return labels[pd.notna(labels)]


def class_balance_report(labels, split_name="Dataset"):
    """Report class counts and percentages for a dataset split."""

    labels = _clean_labels(labels)

    if len(labels) == 0:
        raise ValueError("No valid labels available.")

    counts = pd.Series(labels).value_counts().sort_index()
    percentages = (counts / counts.sum()) * 100

    report = pd.DataFrame({
        "class_count": counts,
        "percentage": percentages.round(2)
    })

    print(f"\n{split_name} Class Balance")
    print(report)
    return report


def split_summary(y_train, y_val, y_test):
    """Compare valid sample counts and class distribution across splits."""

    splits = {
        "Train": _clean_labels(y_train),
        "Validation": _clean_labels(y_val),
        "Test": _clean_labels(y_test)
    }

    all_labels = np.concatenate(list(splits.values()))

    if len(all_labels) == 0:
        raise ValueError("No valid labels available in any split.")

    classes = sorted(pd.unique(all_labels), key=str)
    summary = {}

    for name, labels in splits.items():
        counts = pd.Series(labels).value_counts()
        total = len(labels)

        summary[name] = {
            str(cls): round(counts.get(cls, 0) / total * 100, 2)
            if total else 0
            for cls in classes
        }

    report = pd.DataFrame(summary).fillna(0)

    print("\nValid split sizes:")
    for name, labels in splits.items():
        print(f"{name}: {len(labels)} valid samples")

    print("\nClass distribution (%):")
    print(report)

    return report
