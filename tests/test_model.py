
import sys
from pathlib import Path

import torch
import torch.nn as nn

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1])
)

from src.baseline import BaselineCNN

def test_model():

    torch.manual_seed(42)

    # Dummy input for architecture testing
    images = torch.randn(8, 200, 64, 64)

    labels = torch.randint(0, 2, (8,))

    model = BaselineCNN(
        input_channels=200,
        num_classes=2
    )

    # Forward pass
    outputs = model(images)

    print("Input shape:", images.shape)
    print("Output shape:", outputs.shape)

    assert outputs.shape == (8, 2)

    # Loss calculation
    criterion = nn.CrossEntropyLoss()

    loss = criterion(outputs, labels)

    print("Loss:", loss.item())

    # Backpropagation
    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=0.001
    )

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    print("Backward pass successful")
    print("Model test passed!")

if __name__ == "__main__":
    test_model()
    