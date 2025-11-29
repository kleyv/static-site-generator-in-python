import unittest

from textnode import TextNode, TextType, text_node_to_html_node


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        image_node = TextNode("This is image description", TextType.IMAGE, "www.domain.com/image.jpg")
        html_node = text_node_to_html_node(image_node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props_to_html(), ' alt="This is image description" src="www.domain.com/image.jpg"')
    
    def test_code(self):
        code_node = TextNode("`print('Hello, world!')`", TextType.CODE)
        html_node = text_node_to_html_node(code_node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "`print('Hello, world!')`")

if __name__ == "__main__":
    unittest.main()