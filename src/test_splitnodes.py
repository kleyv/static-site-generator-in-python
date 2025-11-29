import unittest
from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType
class TestSplitNodes(unittest.TestCase):
    def test_missing_closing_delimiter(self):
        node = TextNode("This is text with a ` single back-tick", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold inline** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold inline", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_italic_delimiter(self):
        node = TextNode("This is text with a _italic inline_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("italic inline", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ]
        )

if __name__ == "__main__":
    unittest.main()