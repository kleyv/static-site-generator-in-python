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


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_content = read_file_content(from_path)
    template_content = read_file_content(template_path)
    html = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    updated_template = template_content.replace("{{ Title }}", title)
    updated_template = updated_template.replace("{{ Content }}", html)
    updated_template = updated_template.replace('href="/', f'href="{basepath}')
    updated_template = updated_template.replace('src="/', f'src="{basepath}')
    write_file_content(dest_path, updated_template)

def generate_pages_recursively(from_path, template_path, dest_path, basepath):
    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(os.path.dirname(dest_path))
    
    print(f"Creating {dest_path} from {from_path}")
    source_directory_paths = os.listdir(from_path)
    for filename in source_directory_paths:
        full_source_path = os.path.join(from_path, filename)

        if os.path.isfile(full_source_path):
            html_filename = filename.replace(".md", ".html")
            full_destination_path = os.path.join(dest_path, html_filename)
            generate_page(full_source_path, template_path, full_destination_path, basepath)
        else:
            full_destination_path = os.path.join(dest_path, filename)
            generate_pages_recursively(full_source_path, template_path, full_destination_path, basepath)


# print(extract_title("# Tolkien Fan Club"))
# print(extract_title("Tolkien Fan Club"))
