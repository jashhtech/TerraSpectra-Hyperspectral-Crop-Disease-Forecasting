import zipfile
import io
import os
import numpy as np
from PIL import Image

ARCHIVE = "data/raw/02_processed_patches.zip"


def validate_dataset():
    with zipfile.ZipFile(ARCHIVE) as z:
        files = z.namelist()

        images = [
            f for f in files
            if "/images/" in f and f.endswith(".npy")
        ]

        masks = [
            f for f in files
            if "/masks/" in f and f.endswith(".png")
        ]

        image_map = {
            os.path.splitext(os.path.basename(f))[0]: f
            for f in images
        }

        mask_map = {
            os.path.splitext(os.path.basename(f))[0]: f
            for f in masks
        }

        matched = set(image_map) & set(mask_map)
        missing_masks = set(image_map) - set(mask_map)
        missing_images = set(mask_map) - set(image_map)

        classes = set()
        valid_shapes = 0
        empty_masks = 0
        errors = []

        for name in matched:
            try:
                cube = np.load(io.BytesIO(z.read(image_map[name])))
                mask = np.array(
                    Image.open(io.BytesIO(z.read(mask_map[name])))
                )

                if cube.shape == (224, 224, 6):
                    valid_shapes += 1
                else:
                    errors.append(f"Invalid image shape: {name} {cube.shape}")

                if mask.shape == (224, 224):
                    pass
                else:
                    errors.append(f"Invalid mask shape: {name} {mask.shape}")

                classes.update(np.unique(mask).tolist())

                if not np.any(mask):
                    empty_masks += 1

            except Exception as e:
                errors.append(f"{name}: {e}")

        print("\n--- DATASET VALIDATION REPORT ---")
        print("Total images:", len(images))
        print("Total masks:", len(masks))
        print("Matched pairs:", len(matched))
        print("Missing masks:", len(missing_masks))
        print("Missing images:", len(missing_images))
        print("Valid image shapes:", valid_shapes)
        print("Empty masks:", empty_masks)
        print("Mask classes:", sorted(classes))
        print("Errors:", len(errors))

        for error in errors[:10]:
            print(error)


if __name__ == "__main__":
    validate_dataset()