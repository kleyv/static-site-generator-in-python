from enum import Enum

def markdown_to_blocks(markdown):
    blocks = map(lambda block: block.strip(),markdown.split("\n\n"))
    filter_empty_strings = filter(lambda block: len(block) > 0, blocks)
    return list(filter_empty_strings)


# md = """
# This is **bolded** paragraph

# This is another paragraph with _italic_ text and `code` here
# This is the same paragraph on a new line

# - This is a list
# - with items
# """
# blocks = markdown_to_blocks(md)
# print(blocks)
