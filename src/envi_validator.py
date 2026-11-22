from pathlib import Path
import sys


def read_envi_header(header_path):
    header_path = Path(header_path)

    if not header_path.exists():
        raise FileNotFoundError(f"Header not found: {header_path}")

    text = header_path.read_text(encoding="utf-8", errors="replace")

    if not text.strip().startswith("ENVI"):
        raise ValueError("Invalid ENVI header signature")

    fields = {}

    for line in text.splitlines():
        if "=" not in line:
            continue

        key, value = line.split("=", 1)
        fields[key.strip().lower()] = value.strip()

    required = ["samples", "lines", "bands", "data type"]

    for key in required:
        if key not in fields:
            raise ValueError(f"Missing header field: {key}")

    info = {
        "width": int(fields["samples"]),
        "height": int(fields["lines"]),
        "bands": int(fields["bands"]),
        "data_type": int(fields["data type"]),
        "interleave": fields.get("interleave", "unknown"),
    }

    if min(info["width"], info["height"], info["bands"]) <= 0:
        raise ValueError("Image dimensions must be positive")

    return info


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python src/envi_validator.py <header.hdr>")
        sys.exit(1)

    try:
        info = read_envi_header(sys.argv[1])
        print("\nENVI Header Validation Successful")
        for key, value in info.items():
            print(f"{key}: {value}")

    except (ValueError, FileNotFoundError) as error:
        print(f"Validation failed: {error}")
        sys.exit(1)