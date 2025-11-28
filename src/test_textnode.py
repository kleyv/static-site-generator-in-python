import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        bold_node = TextNode("**This is a bold text node**", TextType.BOLD)
        italic_node = TextNode("_This is a bold text node_", TextType.ITALIC)
        self.assertNotEqual(bold_node,italic_node)

    def test_is_not_none(self):
        image_node = TextNode("This is an image text node", TextType.IMAGE, "www.domain.com/image.jpg")
        self.assertIsNotNone(image_node.url)

    def test_is_code(self):
        code_block = TextNode("`print('Hello, world!')`", TextType.CODE)
        self.assertStartsWith(code_block.text,'`')

if __name__ == "__main__":
    unittest.main()