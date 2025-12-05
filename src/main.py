from copy_static import recursive_copy
from generate_page import generate_page, generate_pages_recursively
import os
import shutil
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

if len(sys.argv) < 2:
    print("Static Site Generator")
    basepath = '/'
else:
    basepath = sys.argv[1]


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    recursive_copy(dir_path_static, dir_path_public)

    print("Writing to static files to public directory...")
    generate_pages_recursively(
        os.path.join(dir_path_content),
        template_path,
        os.path.join(dir_path_public),
        basepath
    )
main()