
import yaml
import torch
import torch.nn as nn

from torch.utils.data import DataLoader, random_split

from src.dataset import HyperspectralDataset
from src.baseline import BaselineCNN

def main():

    with open("configs/config.yaml", "r") as f:
        config = yaml.safe_load(f)

    seed = config["training"]["random_seed"]
    torch.manual_seed(seed)

    device = torch.device(
        "cuda" if torch.cuda.is_available() else "cpu"
    )

    dataset = HyperspectralDataset(
        config["data"]["file_path"]
    )

    total = len(dataset)

    val_size = int(
        total * config["training"]["validation_split"]
    )

    train_size = total - val_size

    if train_size == 0 or val_size == 0:
        raise ValueError("Not enough samples for train/validation split")

    train_data, val_data = random_split(
        dataset,
        [train_size, val_size],
        generator=torch.Generator().manual_seed(seed)
    )

    train_loader = DataLoader(
        train_data,
        batch_size=config["training"]["batch_size"],
        shuffle=True
    )

    val_loader = DataLoader(
        val_data,
        batch_size=config["training"]["batch_size"]
    )

    model = BaselineCNN(
        input_channels=config["model"]["input_channels"],
        num_classes=config["model"]["num_classes"]
    ).to(device)

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=config["training"]["learning_rate"]
    )

    for epoch in range(config["training"]["epochs"]):

        model.train()

        total_loss = 0

        for images, labels in train_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        model.eval()

        correct = 0
        total_val = 0

        with torch.no_grad():

            for images, labels in val_loader:

                images = images.to(device)
                labels = labels.to(device)

                outputs = model(images)

                predictions = outputs.argmax(dim=1)

                correct += (predictions == labels).sum().item()
                total_val += labels.size(0)

        avg_loss = total_loss / len(train_loader)
        accuracy = correct / total_val

        print(
            f"Epoch {epoch + 1}: "
            f"Loss={avg_loss:.4f}, "
            f"Validation Accuracy={accuracy:.4f}"
        )

    print("Training completed.")

    torch.save(
        model.state_dict(),
        "models/checkpoints/baseline_cnn.pth"
    )

if __name__ == "__main__":
    main()
