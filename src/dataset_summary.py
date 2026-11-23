import zipfile
import io
import os
import json
import numpy as np
from PIL import Image

ARCHIVE = "data/raw/02_processed_patches.zip"
OUTPUT = "results/dataset_summary.json"


def generate_summary():
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

        image_names = {
            os.path.splitext(os.path.basename(f))[0]
            for f in images
        }

        mask_names = {
            os.path.splitext(os.path.basename(f))[0]
            for f in masks
        }

        matched = image_names & mask_names
        class_counts = {}
        empty_masks = 0
        valid_images = 0
        valid_masks = 0

        image_map = {
            os.path.splitext(os.path.basename(f))[0]: f
            for f in images
        }

        mask_map = {
            os.path.splitext(os.path.basename(f))[0]: f
            for f in masks
        }

        for name in matched:
            cube = np.load(io.BytesIO(z.read(image_map[name])))
            mask = np.array(
                Image.open(io.BytesIO(z.read(mask_map[name])))
            )

            if cube.shape == (224, 224, 6):
                valid_images += 1

            if mask.shape == (224, 224):
                valid_masks += 1

            if not np.any(mask):
                empty_masks += 1

            values, counts = np.unique(mask, return_counts=True)

            for value, count in zip(values, counts):
                key = str(int(value))
                class_counts[key] = (
                    class_counts.get(key, 0) + int(count)
                )

        summary = {
            "dataset": "UAV Multispectral Maize",
            "total_images": len(images),
            "total_masks": len(masks),
            "matched_pairs": len(matched),
            "missing_masks": len(image_names - mask_names),
            "missing_images": len(mask_names - image_names),
            "valid_image_shapes": valid_images,
            "valid_mask_shapes": valid_masks,
            "empty_masks": empty_masks,
            "mask_pixel_class_counts": class_counts,
        }

        os.makedirs("results", exist_ok=True)

        with open(OUTPUT, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=4)

        print(json.dumps(summary, indent=4))
        print("\nSaved to:", OUTPUT)


if __name__ == "__main__":
    generate_summary()