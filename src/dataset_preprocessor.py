
from pathlib import Path

import numpy as np
from PIL import Image


def load_image_mask_pair(image_path, mask_path):
    """
    Load and validate one multispectral image and its segmentation mask.

    Image format:
        Input:  (Height, Width, Channels)
        Output: (Channels, Height, Width)

    Mask labels are preserved without modification.
    """

    image_path = Path(image_path)
    mask_path = Path(mask_path)

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    if not mask_path.exists():
        raise FileNotFoundError(f"Mask not found: {mask_path}")

    # Load multispectral image
    image = np.load(image_path, allow_pickle=False)

    # Load mask without changing its pixel values
    with Image.open(mask_path) as mask_file:
        mask = np.array(mask_file)

    # Validate image
    if image.ndim != 3:
        raise ValueError(
            f"Expected a 3D image, received shape {image.shape}"
        )

    if image.shape[2] != 6:
        raise ValueError(
            f"Expected 6 channels, received {image.shape[2]}"
        )

    if not np.issubdtype(image.dtype, np.number):
        raise ValueError("Image must contain numeric values")

    if not np.isfinite(image).all():
        raise ValueError("Image contains NaN or infinite values")

    # Validate mask
    if mask.ndim != 2:
        raise ValueError(
            f"Expected a 2D grayscale mask, received shape {mask.shape}"
        )

    if image.shape[:2] != mask.shape:
        raise ValueError(
            f"Image and mask dimensions do not match: "
            f"{image.shape[:2]} vs {mask.shape}"
        )

    # Convert image from HWC to CHW
    image = np.ascontiguousarray(image.transpose(2, 0, 1))

    return image, mask
