import re
from block_markdown import block_to_block_type, markdown_to_blocks

def extract_title(markdown):
    title = ''
    blocks = markdown_to_blocks(markdown)
    heading_blocks = list(filter(lambda block: block_to_block_type(block).name == 'HEADING' ,blocks))
    if len(heading_blocks) == 0:
        raise Exception("Missing Heading 1!")
    elif len(heading_blocks) > 1:
        raise Exception("Too many Headings 1!")
    else:
        line = heading_blocks[0]
        split_line = re.split(r"#\s", line)
        title = split_line[-1].strip()

    return title

# print(extract_title("# Tolkien Fan Club"))
# print(extract_title("Tolkien Fan Club"))