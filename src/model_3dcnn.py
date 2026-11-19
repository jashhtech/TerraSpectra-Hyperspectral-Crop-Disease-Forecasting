import torch
import torch.nn as nn


class Hyperspectral3DCNN(nn.Module):

    def __init__(self, num_classes=2):
        super(Hyperspectral3DCNN, self).__init__()

        self.features = nn.Sequential(

            # First 3D convolution layer
            nn.Conv3d(
                in_channels=1,
                out_channels=16,
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),
            nn.MaxPool3d(kernel_size=2),

            # Second 3D convolution layer
            nn.Conv3d(
                in_channels=16,
                out_channels=32,
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),

            # Third 3D convolution layer
            nn.Conv3d(
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                padding=1
            ),
            nn.ReLU(),

            nn.AdaptiveAvgPool3d((1, 1, 1))
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64, num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x


if __name__ == "__main__":

    # Dummy input for architecture testing only
    sample_input = torch.randn(2, 1, 32, 64, 64)

    model = Hyperspectral3DCNN(num_classes=2)

    output = model(sample_input)

    print("Input shape:", sample_input.shape)
    print("Output shape:", output.shape)
    