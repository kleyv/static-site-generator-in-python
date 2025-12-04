import unittest
from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# Tolkien Fan Club")
        self.assertEqual(title, "Tolkien Fan Club")

    def test_extract_title_no_heading1(self):
        with self.assertRaises(Exception):
            extract_title("Tolkien Fan Club")

    def test_extract_title_multiple_heading1s(self):
        with self.assertRaises(Exception):
            extract_title("# Tolkien Fan Club\n\n# Tolkien Hate Club")


if __name__ == "__main__":
    unittest.main()
