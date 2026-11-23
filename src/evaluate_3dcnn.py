from pathlib import Path

import torch
from torch.utils.data import DataLoader
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from src.dataset import HyperspectralDataset
from src.model_3dcnn import Hyperspectral3DCNN


def evaluate_model():

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    # Dataset path
    dataset_path = Path("data/train_data.npz")

    # Check dataset availability
    if not dataset_path.exists():
        raise FileNotFoundError(
            "Dataset not found. Check data/train_data.npz"
        )

    # Load dataset
    dataset = HyperspectralDataset(str(dataset_path))

    dataloader = DataLoader(
        dataset,
        batch_size=8,
        shuffle=False
    )

    # Load trained model
    model = Hyperspectral3DCNN(num_classes=2).to(device)

    checkpoint_path = Path(
        "models/checkpoints/3dcnn_model.pth"
    )

    if not checkpoint_path.exists():
        raise FileNotFoundError(
            "Trained model checkpoint not found."
        )

    model.load_state_dict(
        torch.load(checkpoint_path, map_location=device)
    )

    model.eval()

    actual_labels = []
    predicted_labels = []

    # Prediction
    with torch.no_grad():

        for images, labels in dataloader:

            images = images.unsqueeze(1).to(device)

            outputs = model(images)

            predictions = torch.argmax(
                outputs, dim=1
            )

            actual_labels.extend(labels.tolist())
            predicted_labels.extend(
                predictions.cpu().tolist()
            )

    # Calculate metrics
    accuracy = accuracy_score(
        actual_labels, predicted_labels
    )

    precision = precision_score(
        actual_labels,
        predicted_labels,
        average="macro",
        zero_division=0
    )

    recall = recall_score(
        actual_labels,
        predicted_labels,
        average="macro",
        zero_division=0
    )

    f1 = f1_score(
        actual_labels,
        predicted_labels,
        average="macro",
        zero_division=0
    )

    matrix = confusion_matrix(
        actual_labels,
        predicted_labels
    )

    print("\n3D-CNN Evaluation Results")
    print("-------------------------")
    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")

    print("\nConfusion Matrix:")
    print(matrix)

    print("\nClassification Report:")
    print(
        classification_report(
            actual_labels,
            predicted_labels,
            zero_division=0
        )
    )


if __name__ == "__main__":
    evaluate_model()
    