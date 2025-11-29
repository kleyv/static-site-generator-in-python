import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)
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

    def test_multiple_bold_delimeters(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD)
            ]
        )

    def test_bold_and_italic_delimeters(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )


    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "You may be using [Markdown Live Preview](https://markdownlivepreview.com/)"
        )
        self.assertListEqual([("Markdown Live Preview", "https://markdownlivepreview.com/")], matches)


    def test_extract_markdown_multiple_links(self):
        matches = extract_markdown_links(
            "[First link](https://firstlink.com/) and [Second link](https://secondlink.com/)"
        )
        self.assertListEqual([
            ("First link", "https://firstlink.com/"),
            ("Second link", "https://secondlink.com/")], matches)

if __name__ == "__main__":
    unittest.main()