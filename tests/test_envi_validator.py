import tempfile
import unittest
from pathlib import Path

from src.envi_validator import read_envi_header


class TestEnviValidator(unittest.TestCase):

    def create_header(self, content):
        temp = tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".hdr",
            delete=False,
            encoding="utf-8"
        )
        temp.write(content)
        temp.close()
        return Path(temp.name)

    def test_valid_header(self):
        path = self.create_header(
            "ENVI\nsamples = 64\nlines = 64\nbands = 6\n"
            "data type = 4\ninterleave = bsq\n"
        )
        try:
            result = read_envi_header(path)
            self.assertEqual(result["width"], 64)
            self.assertEqual(result["height"], 64)
            self.assertEqual(result["bands"], 6)
        finally:
            path.unlink()

    def test_missing_field(self):
        path = self.create_header(
            "ENVI\nsamples = 64\nlines = 64\nbands = 6\n"
        )
        try:
            with self.assertRaises(ValueError):
                read_envi_header(path)
        finally:
            path.unlink()

    def test_invalid_signature(self):
        path = self.create_header(
            "NOT_ENVI\nsamples = 64\nlines = 64\nbands = 6\n"
            "data type = 4\n"
        )
        try:
            with self.assertRaises(ValueError):
                read_envi_header(path)
        finally:
            path.unlink()

    def test_non_positive_dimensions(self):
        path = self.create_header(
            "ENVI\nsamples = 0\nlines = 64\nbands = 6\n"
            "data type = 4\n"
        )
        try:
            with self.assertRaises(ValueError):
                read_envi_header(path)
        finally:
            path.unlink()


if __name__ == "__main__":
    unittest.main()