import unittest
from block_markdown import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_markdown_to_blocks_with_special_text(self):
        md = """
Blockquotes

Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
![This is an alt text.](/image/sample.webp "This is a sample image.").

Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.
You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

1. Item 1
2. Item 2
3. Item 3
    1. Item 3a
    2. Item 3b
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "Blockquotes",
                'Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.\n![This is an alt text.](/image/sample.webp "This is a sample image.").',
                "Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.\nYou may be using [Markdown Live Preview](https://markdownlivepreview.com/).",
                "1. Item 1\n2. Item 2\n3. Item 3\n    1. Item 3a\n    2. Item 3b"
            ],
        )

if __name__ == "__main__":
    unittest.main()