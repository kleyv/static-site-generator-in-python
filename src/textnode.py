from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


# TextType = Enum('TextType', ['TEXT', 'BOLD', 'ITALIC', 'CODE', 'LINK', 'IMAGE'])
class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text  
        
        self.text_type = text_type
        self.url = url  

    def __eq__(self, node):
        return (self.text == node.text
                and self.text_type == node.text_type
                and self.url == node.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case(TextType.TEXT): 
            return LeafNode(None, text_node.text)
        case(TextType.BOLD):
            return LeafNode("b", text_node.text)
        case(TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case(TextType.CODE):
            return LeafNode("code", text_node.text)
        case(TextType.LINK):
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case(TextType.IMAGE):
            return LeafNode("img", '',  {"alt": text_node.text, "src": text_node.url} )
        case _:
            raise ValueError(f"invalid text type: {text_node.text_type}")

# node = TextNode("This is a text node", TextType.TEXT)
# html_node = text_node_to_html_node(node)
# print(html_node.to_html())


image_node = TextNode("This is image description", TextType.IMAGE, "www.domain.com/image.jpg")
html_image_node = text_node_to_html_node(image_node)
print(html_image_node.to_html())