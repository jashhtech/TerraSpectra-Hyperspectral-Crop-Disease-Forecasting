from pathlib import Path
import random
import yaml
import numpy as np
import torch
import torch.nn as nn

from torch.utils.data import DataLoader, random_split
from src.dataset import HyperspectralDataset
from src.model_3dcnn import Hyperspectral3DCNN


def train_model():

    # Reproducibility
    seed = 42
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

    # Load configuration
    with open("configs/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    training_config = config.get("training", {})
    model_config = config.get("model", {})
    data_config = config.get("data", {})

    batch_size = training_config.get("batch_size", 8)
    epochs = training_config.get("epochs", 15)
    learning_rate = training_config.get("learning_rate", 0.001)
    validation_split = training_config.get("validation_split", 0.2)
    num_classes = model_config.get("num_classes", 2)
    data_file = data_config.get("file", "data/train_data.npz")

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    print("Using device:", device)

    # Load dataset
    dataset = HyperspectralDataset(data_file)

    if len(dataset) < 2:
        raise ValueError("Dataset must contain at least two samples.")

    val_size = max(1, int(len(dataset) * validation_split))
    train_size = len(dataset) - val_size

    if train_size < 1:
        raise ValueError("Not enough samples for training.")

    generator = torch.Generator().manual_seed(seed)

    train_data, val_data = random_split(
        dataset,
        [train_size, val_size],
        generator=generator
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

    # Initialize model
    model = Hyperspectral3DCNN(
        num_classes=num_classes
    ).to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=learning_rate,
        weight_decay=0.0001
    )

    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer,
        mode="min",
        patience=2,
        factor=0.5
    )

    best_val_loss = float("inf")
    patience = 5
    epochs_without_improvement = 0

    checkpoint_dir = Path("models/checkpoints")
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    checkpoint_path = checkpoint_dir / "3dcnn_best.pth"

    # Training
    for epoch in range(epochs):

        model.train()
        train_loss = 0.0

        for images, labels in train_loader:

            images = images.unsqueeze(1).to(device)
            labels = labels.to(device)

            optimizer.zero_grad()

            outputs = model(images)
            loss = criterion(outputs, labels)

            loss.backward()
            optimizer.step()

            train_loss += loss.item()

        avg_train_loss = train_loss / len(train_loader)

        # Validation
        model.eval()
        val_loss = 0.0
        correct = 0
        total = 0

        with torch.no_grad():

            for images, labels in val_loader:

                images = images.unsqueeze(1).to(device)
                labels = labels.to(device)

                outputs = model(images)
                loss = criterion(outputs, labels)

                val_loss += loss.item()

                predictions = outputs.argmax(dim=1)
                correct += (predictions == labels).sum().item()
                total += labels.size(0)

        avg_val_loss = val_loss / len(val_loader)
        val_accuracy = 100 * correct / total

        scheduler.step(avg_val_loss)

        print(
            f"Epoch [{epoch + 1}/{epochs}] "
            f"Train Loss: {avg_train_loss:.4f} "
            f"Validation Loss: {avg_val_loss:.4f} "
            f"Validation Accuracy: {val_accuracy:.2f}%"
        )

        # Save best model
        if avg_val_loss < best_val_loss:

            best_val_loss = avg_val_loss
            epochs_without_improvement = 0

            torch.save(model.state_dict(), checkpoint_path)

            print("Best model checkpoint saved.")

        else:
            epochs_without_improvement += 1

        # Early stopping
        if epochs_without_improvement >= patience:
            print("Early stopping activated.")
            break

    print("\nTraining completed.")
    print("Best validation loss:", best_val_loss)
    print("Best model saved at:", checkpoint_path)


if __name__ == "__main__":
    train_model()
    