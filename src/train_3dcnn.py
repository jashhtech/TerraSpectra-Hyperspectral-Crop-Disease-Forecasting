from pathlib import Path
import yaml
import torch
import torch.nn as nn

from torch.utils.data import DataLoader, random_split
from src.dataset import HyperspectralDataset
from src.model_3dcnn import Hyperspectral3DCNN


def get_config_value(config, section, key, default):
    """Read nested or top-level configuration values."""
    return config.get(section, {}).get(
        key, config.get(key, default)
    )


def train_model():

    # Load configuration
    with open("configs/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    batch_size = get_config_value(
        config, "training", "batch_size", 8
    )
    epochs = get_config_value(
        config, "training", "epochs", 10
    )
    learning_rate = get_config_value(
        config, "training", "learning_rate", 0.001
    )
    validation_split = get_config_value(
        config, "training", "validation_split", 0.2
    )
    num_classes = get_config_value(
        config, "model", "num_classes", 2
    )
    data_file = get_config_value(
        config, "data", "file", "data/train_data.npz"
    )

    # Select device
    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )
    print("Using device:", device)

    # Load dataset
    dataset = HyperspectralDataset(data_file)

    if len(dataset) < 2:
        raise ValueError("Dataset needs at least two samples.")

    # Split dataset
    val_size = int(len(dataset) * validation_split)
    val_size = max(1, val_size)
    train_size = len(dataset) - val_size

    if train_size < 1:
        raise ValueError("Training dataset is too small.")

    train_data, val_data = random_split(
        dataset,
        [train_size, val_size]
    )

    train_loader = DataLoader(
        train_data,
        batch_size=batch_size,
        shuffle=True
    )

    val_loader = DataLoader(
        val_data,
        batch_size=batch_size,
        shuffle=False
    )

    # Initialize 3D-CNN
    model = Hyperspectral3DCNN(
        num_classes=num_classes
    ).to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=learning_rate
    )

    # Training loop
    for epoch in range(epochs):

        model.train()
        total_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:

            # Convert (B, Bands, H, W) to (B, 1, Bands, H, W)
            images = images.unsqueeze(1).to(device)
            labels = labels.to(device)

            optimizer.zero_grad()

            outputs = model(images)
            loss = criterion(outputs, labels)

            loss.backward()
            optimizer.step()

            total_loss += loss.item()

            predictions = outputs.argmax(dim=1)
            correct += (predictions == labels).sum().item()
            total += labels.size(0)

        train_accuracy = 100 * correct / total

        # Validation
        model.eval()
        val_correct = 0
        val_total = 0

        with torch.no_grad():
            for images, labels in val_loader:

                images = images.unsqueeze(1).to(device)
                labels = labels.to(device)

                outputs = model(images)
                predictions = outputs.argmax(dim=1)

                val_correct += (
                    predictions == labels
                ).sum().item()

                val_total += labels.size(0)

        val_accuracy = 100 * val_correct / val_total

        average_loss = total_loss / len(train_loader)

        print(
            f"Epoch [{epoch + 1}/{epochs}] "
            f"Loss: {average_loss:.4f} "
            f"Train Accuracy: {train_accuracy:.2f}% "
            f"Validation Accuracy: {val_accuracy:.2f}%"
        )

    # Save checkpoint
    checkpoint_dir = Path("models/checkpoints")
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    torch.save(
        model.state_dict(),
        checkpoint_dir / "3dcnn_model.pth"
    )

    print("3D-CNN training completed.")
    print("Model checkpoint saved successfully.")


if __name__ == "__main__":
    train_model()
    