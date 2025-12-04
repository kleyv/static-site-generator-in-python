import os
import shutil

def recursive_copy(source_directory_path,destination_directory_path):
    if not os.path.exists(destination_directory_path):
        os.mkdir(destination_directory_path)
   

    source_diretory_paths = os.listdir(source_directory_path)
    for filename in source_diretory_paths:
        full_source_path = os.path.join(source_directory_path, filename)
        full_destination_path = os.path.join(destination_directory_path, filename)

        print(f"from: {full_source_path}\nto-> {full_destination_path}")
        if os.path.isfile(full_source_path):
            shutil.copy(full_source_path, full_destination_path)
        else:
            recursive_copy(full_source_path, full_destination_path)