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

# This test creates two TextNode objects with the same properties and asserts that they are equal. Notice the missing url argument which should have a default value of None. If you run your tests with ./test.sh, you should see that the test passes.

# Add some test cases by adding methods to the TestTextNode class to verify that the TextNode class works as expected. You can use the following methods to compare the objects:
# self.assertEqual - if the inputs are equal the test passes
# self.assertNotEqual - if the inputs are not equal the test passes
# Add even more test cases (at least 3 in total) to check various edge cases, like when the url property is None, or when the text_type property is different. You'll want to make sure that when properties are different, the TextNode objects are not equal.