import re
from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            chunks = node.text.split(delimiter)
            if len(chunks) % 2 == 0:
                raise ValueError("invalid markdown, formatted section not closed")
            for index in range(len(chunks)):
                if chunks[index] == "":
                    continue
                # >>> "This is text with a **bolded** word and **another**".split("**")
                # ['This is text with a ', 'bolded', ' word and ', 'another', '']
                if index % 2 == 0:
                    new_nodes.append(TextNode(chunks[index], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(chunks[index], text_type))
    return new_nodes

def extract_markdown_images(text):
    image_links = re.findall(r"!\[[^\(]+\]\([^\(]+\)", text)
    results = []
    for link in image_links:
        alt = re.findall(r"\[(.*)\]",link)[0]
        url = re.findall(r"\((.*)\)",link)[0]
        results.append((alt, url))
    return results

def extract_markdown_links(text):
    links = re.findall(r"\[[^\(]+\]\([^\(]+\)", text)
    results = []
    for link in links:
        alt = re.findall(r"\[(.*)\]",link)[0]
        url = re.findall(r"\((.*)\)",link)[0]
        results.append((alt, url))
    return results


# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
# print(new_nodes)

# node = TextNode(
#     "This is text with a **bolded** word and **another**", TextType.TEXT
# )
# new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
# print(new_nodes)

# node = TextNode("**bold** and _italic_", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
# new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
# print(new_nodes)

# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))
# # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))
# # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

