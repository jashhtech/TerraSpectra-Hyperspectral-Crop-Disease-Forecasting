from pathlib import Path
import time
import yaml
import torch

from torch.utils.data import DataLoader
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from src.dataset import HyperspectralDataset
from src.baseline import BaselineCNN
from src.model_3dcnn import Hyperspectral3DCNN


def compare_models():

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    # Load configuration
    with open("configs/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    data_config = config.get("data", {})
    model_config = config.get("model", {})

    test_file = data_config.get(
        "test_file", "data/test_data.npz"
    )

    num_classes = model_config.get("num_classes", 2)
    input_channels = model_config.get("input_channels", 200)

    # Check test dataset
    if not Path(test_file).exists():
        raise FileNotFoundError(
            f"Test dataset not found: {test_file}"
        )

    dataset = HyperspectralDataset(test_file)

    loader = DataLoader(
        dataset,
        batch_size=8,
        shuffle=False
    )

    # Load baseline CNN
    baseline = BaselineCNN(
        input_channels=input_channels,
        num_classes=num_classes
    ).to(device)

    baseline_path = Path(
        "models/checkpoints/baseline_cnn.pth"
    )

    if not baseline_path.exists():
        raise FileNotFoundError(
            "Baseline CNN checkpoint not found."
        )

    baseline.load_state_dict(
        torch.load(baseline_path, map_location=device)
    )

    # Load 3D-CNN
    model_3d = Hyperspectral3DCNN(
        num_classes=num_classes
    ).to(device)

    model_3d_path = Path(
        "models/checkpoints/3dcnn_best.pth"
    )

    if not model_3d_path.exists():
        raise FileNotFoundError(
            "3D-CNN checkpoint not found."
        )

    model_3d.load_state_dict(
        torch.load(model_3d_path, map_location=device)
    )

    models = {
        "Baseline CNN": baseline,
        "3D-CNN": model_3d
    }

    results = {}

    # Compare both models
    for model_name, model in models.items():

        model.eval()

        actual = []
        predicted = []

        start_time = time.perf_counter()

        with torch.no_grad():

            for images, labels in loader:

                images = images.to(device)

                if model_name == "3D-CNN":
                    images = images.unsqueeze(1)

                outputs = model(images)

                predictions = outputs.argmax(dim=1)

                actual.extend(labels.tolist())
                predicted.extend(
                    predictions.cpu().tolist()
                )

        if device.type == "cuda":
            torch.cuda.synchronize()

        elapsed_time = time.perf_counter() - start_time

        results[model_name] = {
            "Accuracy": accuracy_score(actual, predicted),
            "Precision": precision_score(
                actual, predicted,
                average="macro",
                zero_division=0
            ),
            "Recall": recall_score(
                actual, predicted,
                average="macro",
                zero_division=0
            ),
            "F1-score": f1_score(
                actual, predicted,
                average="macro",
                zero_division=0
            ),
            "Inference Time (seconds)": elapsed_time
        }

    # Display comparison
    print("\nMODEL COMPARISON")
    print("-" * 65)

    for name, metrics in results.items():

        print(f"\n{name}")

        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")

    # Save results
    output_dir = Path("results")
    output_dir.mkdir(parents=True, exist_ok=True)

    import csv

    output_file = output_dir / "model_comparison.csv"

    with open(output_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Model",
            "Accuracy",
            "Precision",
            "Recall",
            "F1-score",
            "Inference Time"
        ])

        for name, metrics in results.items():

            writer.writerow([
                name,
                metrics["Accuracy"],
                metrics["Precision"],
                metrics["Recall"],
                metrics["F1-score"],
                metrics["Inference Time (seconds)"]
            ])

    print("\nComparison saved to:", output_file)


if __name__ == "__main__":
    compare_models()
    