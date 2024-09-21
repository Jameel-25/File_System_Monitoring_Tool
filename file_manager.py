import os
from pathlib import Path

def create_directory(dir_name):
    Path(dir_name).mkdir(exist_ok=True)
    print(f"Directory {dir_name} created.")

def create_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File {file_path} created with content.")

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted.")
    else:
        print(f"File {file_path} not found.")
