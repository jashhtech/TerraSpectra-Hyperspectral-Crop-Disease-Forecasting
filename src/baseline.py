
import torch
import torch.nn as nn

class BaselineCNN(nn.Module):

    def __init__(
        self,
        input_channels=200,
        num_classes=2
    ):

        super().__init__()

        self.features = nn.Sequential(

            nn.Conv2d(
                input_channels,
                32,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.MaxPool2d(2),

            nn.Conv2d(
                32,
                64,
                kernel_size=3,
                padding=1
            ),

            nn.ReLU(),

            nn.AdaptiveAvgPool2d((1, 1))
        )

        self.classifier = nn.Linear(
            64,
            num_classes
        )

    def forward(self, x):

        x = self.features(x)

        x = torch.flatten(x, 1)

        x = self.classifier(x)

        return x
    