from enum import Enum
import re

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
