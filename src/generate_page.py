import os
import re
from block_markdown import block_to_block_type, markdown_to_blocks, markdown_to_html_node

def extract_title(markdown):
    title = ''
    blocks = markdown_to_blocks(markdown)
    heading_blocks = list(
        filter(lambda block: block_to_block_type(block).name == 'HEADING' ,blocks)
    )
    heading_one_blocks = list(
        filter(
            lambda block: re.match( r"^#\s" , block) ,heading_blocks)
    )
    if len(heading_one_blocks) == 0:
        raise Exception("Missing Heading 1!")
    elif len(heading_one_blocks) > 1:
        raise Exception("Too many Headings 1!")
    else:
        line = heading_one_blocks[0]
        split_line = re.split(r"#\s", line)
        title = split_line[-1].strip()

    return title

def read_file_content(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def write_file_content(file_path, content):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    try:

        with open(file_path, "w") as file:
            file.write(content)
        return f"Successfully wrote to {file_path}"
    except Exception as e:
        return f"Error: {e}"


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_content = read_file_content(from_path)
    template_content = read_file_content(template_path)
    html = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    updated_template = template_content.replace("{{ Title }}", title)
    updated_template = updated_template.replace("{{ Content }}", html)
    write_file_content(dest_path, updated_template)
    print(html[:10])


# print(extract_title("# Tolkien Fan Club"))
# print(extract_title("Tolkien Fan Club"))
