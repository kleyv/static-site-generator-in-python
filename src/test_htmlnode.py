import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        link_node = HTMLNode("a", "Boot.dev Dashboard", None, {"href": "https://www.boot.dev/dashboard", "target": "_blank"})
        self.assertEqual(
            link_node.props_to_html(),
            ' href="https://www.boot.dev/dashboard" target="_blank"'
            )
        
    def test_repr(self):
        div_node = HTMLNode(
            "ul",
            None,
            [
                HTMLNode("li",'Dashboard',None,None),
                HTMLNode("li",'Courses',None,None),
            ],
            {"id": "menu", "class": "nav-list"}
        )
        self.assertEqual(
            div_node.__repr__(),
            "HTMLNode(ul, None, children: [HTMLNode(li, Dashboard, children: None, None), HTMLNode(li, Courses, children: None, None)], {'id': 'menu', 'class': 'nav-list'})"
        )

    def test_values(self):
        span_node = HTMLNode("span", "Happy holidays", None, None)
        self.assertEqual(span_node.tag, "span")
        self.assertEqual(span_node.value, "Happy holidays")
        self.assertEqual(span_node.children, None)
        self.assertEqual(span_node.props, None)

# ------------------------
    def test_p(self):
        # p_node = LeafNode("p", None, {"style": "color: blue;"})
        # self.assertEqual(
        #     '<p style="color: blue;"></p>', p_node.to_html()
        # )
        with self.assertRaises(ValueError):
            LeafNode("p", None, {"style": "color: blue;"})


    def test_value(self):
        h1_node = LeafNode("h1", "Hello World", {"style": "padding: 1rem;"})
        self.assertEqual(
            '<h1 style="padding: 1rem;">Hello World</h1>', h1_node.to_html()
        )

    def test_no_tag(self):
        raw_text_node = LeafNode(None, "Just raw text")
        self.assertEqual(
            'Just raw text', raw_text_node.to_html()
        )


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()