import os
import shutil

def recursive_copy(source_directory_path,destination_directory_path):
    print(f"copying from: {source_directory_path}\n to: {destination_directory_path}")
    if os.path.exists(destination_directory_path):
        shutil.rmtree(destination_directory_path)
    os.mkdir(destination_directory_path)

    source_diretory_paths = os.listdir(source_directory_path)
    for source_path in source_diretory_paths:
        full_source_path = os.path.join(source_directory_path, source_path)
        if os.path.isfile(full_source_path):
            shutil.copy(full_source_path, destination_directory_path)
        if os.path.isdir(full_source_path):
            new_destination_directory_path = os.path.join(destination_directory_path, source_path)
            recursive_copy(full_source_path, new_destination_directory_path)

def copy_to_destination():
    source = "static"
    destination = "public"
    root = os.path.abspath('.')
    source_directory_path = os.path.join(root, source)
    destination_directory_path = os.path.join(root, destination)

    recursive_copy(source_directory_path, destination_directory_path)

def main():
    copy_to_destination()

main()