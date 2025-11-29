from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            chunks = node.text.split(delimiter)
            if len(chunks) < 3:
                raise Exception("Invalid Markdown syntax")
            for i in range(len(chunks)):
                SPECIAL_TEXT_INDEX = 1
                if i == SPECIAL_TEXT_INDEX:
                    new_nodes.append(TextNode(chunks[i], text_type))
                else:
                    new_nodes.append(TextNode(chunks[i], TextType.TEXT))
    return new_nodes

# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
# print(new_nodes)