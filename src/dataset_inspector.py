
from pathlib import Path
import zipfile
import csv

def inspect_dataset(path):
    path = Path(path)

    if not path.exists():
        print("Path does not exist.")
        return

    if path.is_file():
        inspect_file(path)
    elif path.is_dir():
        print(f"Inspecting directory: {path}")

        for file in path.iterdir():
            if file.is_file():
                inspect_file(file)


def inspect_file(path):
    print(f"\n{'=' * 40}")
    print(f"File: {path.name}")
    print(f"Size: {path.stat().st_size} bytes")

    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as archive:
            print("ZIP contents:")
            for name in archive.namelist()[:20]:
                print("-", name)

    elif path.suffix.lower() == ".csv":
        try:
            with open(path, newline="", encoding="utf-8-sig") as file:
                reader = csv.reader(file, delimiter=";")
                rows = list(reader)
        except UnicodeDecodeError:
            with open(path, newline="", encoding="cp1252") as file:
                reader = csv.reader(file, delimiter=";")
                rows = list(reader)

        if rows:
            print(f"Rows: {len(rows) - 1}")
            print(f"Columns ({len(rows[0])}):")
            print(rows[0])

            print("\nFirst 3 data rows:")
            for row in rows[1:4]:
                print(row)
        else:
            print("Empty CSV file.")

    else:
        print("Detailed inspection not supported for this file.")


if __name__ == "__main__":
    inspect_dataset("data/metadata")
