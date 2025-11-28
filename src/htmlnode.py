class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ''
        props_html = ' '.join(map(lambda a: f'{a[0]}="{a[1]}"',self.props.items()))
        return f" {props_html}"
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("invalid HTML: no value")
        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("invalid HTML: no tag")
        if self.children == None:
            raise ValueError("invalid HTML: no children")
        
        return f"<{self.tag}{self.props_to_html()}>{''.join(map(lambda child: child.to_html(),self.children))}</{self.tag}>"

# print(HTMLNode("p", None, None, {"style": "color: blue;"}))
# print(HTMLNode("h1", "Hello World", None, {"style": "padding: 1rem;"}))
# print(HTMLNode(None, "Just raw text", None, None))
# print(HTMLNode("a", "Boot.dev Dashboard", None, {"href": "https://www.boot.dev/dashboard", "target": "_blank"}).props_to_html())

# print(LeafNode("span", "Boot.dev Dashboard",{"href": "https://www.boot.dev/dashboard", "target": "_blank"}).to_html())
# print(LeafNode(None, "Boot.dev Dashboard", {"href": "https://www.boot.dev/dashboard", "target": "_blank"}).to_html())
# print(LeafNode(None, None, {"href": "https://www.boot.dev/dashboard", "target": "_blank"}).to_html())


# print(LeafNode("p", "This is a paragraph of text.").to_html())
# "<p>This is a paragraph of text.</p>"

# print(LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html())
# "<a href="https://www.google.com">Click me!</a>"


# node = ParentNode(
#     "p",
#     [
#         LeafNode("b", "Bold text"),
#         LeafNode(None, "Normal text"),
#         LeafNode("i", "italic text"),
#         LeafNode(None, "Normal text"),
#     ],
# )

# print(node.to_html())