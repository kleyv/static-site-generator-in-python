import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

# --------- LEAF NODE---------------
    def test_p(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None, {"style": "color: blue;"}).to_html()


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

# --------- PARENT NODE---------------

    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )




if __name__ == "__main__":
    unittest.main()