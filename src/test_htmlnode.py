import unittest

from htmlnode import HTMLNode

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
    # def test_p(self):
    #     p_node = HTMLNode("p", None, None, {"style": "color: blue;"})
    #     self.assertEqual(
    #         '<p "style"="color: blue;"></p>', repr(p_node)
    #     )


    # def test_value(self):
    #     h1_node = HTMLNode("h1", "Hello World", None, {"style": "padding: 1rem;"})
    #     self.assertEqual(
    #         '<h1 "style"="padding: 1rem;">Hello World</h1>', repr(h1_node)
    #     )

    # def test_no_tag(self):
    #     raw_text_node = HTMLNode(None, "Just raw text", None, None)
    #     self.assertEqual(
    #         'Just raw text', repr(raw_text_node)
    #     )

if __name__ == "__main__":
    unittest.main()