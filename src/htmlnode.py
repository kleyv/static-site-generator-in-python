class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ''
        props_html = ' '.join(map(lambda a: f'"{a[0]}"="{a[1]}"',self.props.items()))
        return f" {props_html}"
    
    def __repr__(self):
        textContent = None
        if self.value == None and self.children == None:
            textContent = ""
        elif self.value == None:
            textContent = self.children
        else:
            textContent = self.value
        props = self.props_to_html()

        if self.tag == None:
            return self.value

        return f"<{self.tag}{props}>{textContent}</{self.tag}>"
    
# print(HTMLNode("p", None, None, {"style": "color: blue;"}))
# print(HTMLNode("h1", "Hello World", None, {"style": "padding: 1rem;"}))
# print(HTMLNode(None, "Just raw text", None, None))