import re
from textnode import *
from block_markdown import (
    markdown_to_blocks, 
    block_to_block_type,
    BlockType
)
from htmlnode import (
    ParentNode,
    LeafNode
)
from inline_markdown import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match(block_type):
            case(BlockType.HEADING):
                value = re.split(r"(^#{1,6}\s)", block)[-1]
                if block.startswith('######'):
                    children.append(LeafNode('h6', value))
                elif block.startswith('#####'):
                    children.append(LeafNode('h5', value))
                elif block.startswith('####'):
                    children.append(LeafNode('h4', value))
                elif block.startswith('###'):
                    children.append(LeafNode('h3', value))
                elif block.startswith('##'):
                    children.append(LeafNode('h2', value))
                elif block.startswith('#'):
                    children.append(LeafNode('h1', value))
            case(BlockType.CODE):
                # value = block.strip("```")
                split_lines = block.split('\n')
                joined_lines = '\n'.join(split_lines[1:-1]) + "\n"
                code_leaf_node = text_node_to_html_node(TextNode(joined_lines, TextType.CODE))
                children.append(ParentNode('pre',[code_leaf_node]))
            case(BlockType.QUOTE):
                lines = block.split('\n')
                paragraphs = list(
                    map(
                        lambda line: LeafNode('p', line.strip('> ')),lines
                    )
                )
                children.append(ParentNode('blockquote',paragraphs))
            case(BlockType.UNORDERED_LIST):
                lines = block.split('\n')
                list_items = list(map(lambda line: LeafNode('li', line.strip('- ')),lines))
                children.append(ParentNode('ul', list_items))
            case(BlockType.ORDERED_LIST):
                lines = block.split('\n')
                strip_digits = lambda line: re.split(r"(^\d\.\s)", line)[-1]
                list_items = list(
                    map(lambda line: LeafNode('li', strip_digits(line)), lines))
                children.append(ParentNode('ol', list_items))
            case(BlockType.PARAGRAPH):
                text = ' '.join(block.split('\n'))
                text_nodes = text_to_textnodes(text)
                html_nodes = list(map(lambda text_node: text_node_to_html_node(text_node), text_nodes))
                
                children.append(ParentNode('p', html_nodes))
                

    return ParentNode('div', children)



def main():
    # new_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    # print(new_node)
    # markdown = "# heading one"
    # print(markdown_to_html_node(markdown))
#     md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """
#     node = markdown_to_html_node(md)
#     html = node.to_html()
#     print(html)
#         md = """
# - Item 1
# - Item 2
# - Item 2a
# - Item 2b
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         print(html)
#         md = """
# 1. Item 1
# 2. Item 2
# 3. Item 3
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         print(html)
#         md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         print(html)
    pass




main()