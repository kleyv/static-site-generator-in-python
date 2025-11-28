import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_p(self):
        p_node = HTMLNode("p", None, None, {"style": "color: blue;"})
        self.assertEqual(
            '<p "style"="color: blue;"></p>', repr(p_node)
        )


    def test_value(self):
        h1_node = HTMLNode("h1", "Hello World", None, {"style": "padding: 1rem;"})
        self.assertEqual(
            '<h1 "style"="padding: 1rem;">Hello World</h1>', repr(h1_node)
        )

    def test_no_tag(self):
        raw_text_node = HTMLNode(None, "Just raw text", None, None)
        self.assertEqual(
            'Just raw text', repr(raw_text_node)
        )
