from enum import Enum
import re
from block_markdown import (
    markdown_to_blocks, 
    block_to_block_type,
    BlockType
)
from htmlnode import (
    ParentNode,
    LeafNode
)
from textnode import text_node_to_html_node, TextNode, TextType
from inline_markdown import text_to_textnodes

def markdown_to_blocks(markdown):
    blocks = map(lambda block: block.strip(),markdown.split("\n\n"))
    filter_empty_strings = filter(lambda block: len(block) > 0, blocks)
    return list(filter_empty_strings)


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown_text_block):
    lines = list(filter(lambda line: len(line) > 0,markdown_text_block.split("\n")))
    
    # starts with 1-6 #
    is_heading = all(
        map(lambda line: re.match(r"(^#{1,6}\s)", line), lines)
    )
    if is_heading:
        return BlockType.HEADING

    # starts and ends with ````
    first_and_last_line = [lines[0],lines[-1]]
    is_code_block = all(
        map(lambda line: re.match(r"(^```)", line) ,first_and_last_line)
    )
    if is_code_block:
        return BlockType.CODE

    # starts with >
    is_quote = all(list(
        map(lambda line: re.match(r"(^>)", line), lines)
    ))
    if is_quote:
        return BlockType.QUOTE
    
    # line starts with hypen-space
    is_unordered_list = all(map(lambda line: re.match(r"(^-\s)", line),lines))
    if is_unordered_list:
        return BlockType.UNORDERED_LIST
    
    ordered_list_rules = []
    for i in range(len(lines)):
        # start witha  digit-dot-space
        line_starts_with_digit_dot_space = re.match(r"(^\d\.\s)", lines[i])
        if i == 0:
            ordered_list_rules.append(re.match(r"(^\d\.\s)", lines[i]))
        elif line_starts_with_digit_dot_space:
            previous_digit = int(re.match(r"(^\d)", lines[i-1])[0])
            current_digit = int(re.match(r"(^\d)", lines[i])[0])
            condition = line_starts_with_digit_dot_space and (current_digit == previous_digit + 1)
            ordered_list_rules.append(condition)
        else:
            ordered_list_rules.append(False)
    is_ordered_list = all(ordered_list_rules)
    if is_ordered_list:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match(block_type):
            case(BlockType.HEADING):
                spilt_line = re.split(r"(^#{1,6}\s)", block)
                heading = spilt_line[1].strip()
                heading_number = f"h{len(heading)}"
                text = spilt_line[-1]
                children.append(LeafNode(heading_number, text))
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





# md = """
# ```
# let message = 'Hello world';
# alert(message);
# ```
# """
# print(block_to_block_type(md))
# md = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

# - This is a list
# - with items
# """
# blocks = markdown_to_blocks(md)
# print(blocks)
