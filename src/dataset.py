
import numpy as np
import torch
from torch.utils.data import Dataset

class HyperspectralDataset(Dataset):

    def __init__(self, file_path):

        data = np.load(file_path, allow_pickle=False)

        if "cubes" not in data or "labels" not in data:
            raise ValueError(
                "NPZ must contain cubes and labels"
            )

        self.cubes = data["cubes"]
        self.labels = data["labels"]

        if self.cubes.ndim != 4:
            raise ValueError(
                "Expected shape: (N, Bands, Height, Width)"
            )

        if len(self.cubes) != len(self.labels):
            raise ValueError(
                "Image and label counts do not match"
            )

        if not np.isfinite(self.cubes).all():
            raise ValueError(
                "Invalid values found in image cubes"
            )

        if not np.isfinite(self.labels).all():
            raise ValueError(
                "Invalid labels found"
            )

        if not np.issubdtype(self.labels.dtype, np.integer):
            raise ValueError(
                "Labels must contain integer class IDs"
            )

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):

        image = torch.as_tensor(
            self.cubes[index],
            dtype=torch.float32
        )

        label = torch.tensor(
            self.labels[index],
            dtype=torch.long
        )

        return image, label
    