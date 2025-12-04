from copy_static import recursive_copy
from generate_page import generate_page
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    recursive_copy(dir_path_static, dir_path_public)

    print("Writing to static files to public directory...")
    generate_page('./content/index.md', './template.html', './public/index.html')

main()