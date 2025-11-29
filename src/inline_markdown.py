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

def split_nodes_image(old_nodes):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        chunks =re.split(pattern, old_node.text)
        split_nodes = []
        for index in range(len(chunks)):
            if chunks[index] == "":
                continue
            is_raw_text = index % 3 == 0
            is_image_alt = index % 3 == 1
            if is_raw_text:
                split_nodes.append(TextNode(chunks[index], TextType.TEXT))
            if is_image_alt:
                image_alt = chunks[index]
                image_url = chunks[index + 1]
                split_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url ))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        chunks = re.split(pattern, old_node.text)
        split_nodes = []
        for index in range(len(chunks)):
            if chunks[index] == "":
                continue
            is_raw_text = index % 3 == 0
            is_link_text = index % 3 == 1
            if is_raw_text:
                split_nodes.append(TextNode(chunks[index], TextType.TEXT))
            if is_link_text:
                link_text = chunks[index]
                link_url = chunks[index + 1]
                split_nodes.append(TextNode(link_text, TextType.LINK, link_url ))
        new_nodes.extend(split_nodes)
    return new_nodes


def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    filtered_image_nodes = split_nodes_image([text_node])
    filtered_link_nodes = split_nodes_link(filtered_image_nodes)
    filtered_bold_nodes = split_nodes_delimiter(filtered_link_nodes, "**", TextType.BOLD)
    filtered_italic_nodes = split_nodes_delimiter(filtered_bold_nodes, "_", TextType.ITALIC)
    filtered_code_nodes = split_nodes_delimiter(filtered_italic_nodes, "`", TextType.CODE)
    return filtered_code_nodes

sentence = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

print(text_to_textnodes(sentence))
"""
[
    TextNode(This is , text, None), 
    TextNode(text, bold, None), 
    TextNode( with an , text, None), 
    TextNode(italic, italic, None), 
    TextNode( word and a , text, None), 
    TextNode(code block, code, None), 
    TextNode( and an , text, None), 
    TextNode(obi wan image, image, https://i.imgur.com/fJRm4Vk.jpeg), 
    TextNode( and a , text, None), 
    TextNode(link, link, https://boot.dev)
]
"""


# link_node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_link_nodes = split_nodes_link([link_node])
# print(new_link_nodes)


# image_node = TextNode(
#     "This is text with an image ![image description](https://example.com/image.png) in it.",
#     TextType.TEXT,
# )
# new_image_nodes = split_nodes_image([image_node])
# print(new_image_nodes)


# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]

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
