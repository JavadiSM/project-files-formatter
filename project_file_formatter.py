import os
from typing import Dict
import json
import shutil
types_map_places: Dict[str, str]
with open('data-base.json') as info:
    types_map_places = json.load(info)
    for key,value in types_map_places.items():
        types_map_places[key] = value.replace('/',os.sep)


def initialize_directories(map: dict) -> None:
    """
    checking the project folder
    Create directories if they do not exist.
    """
    if not os.path.exists("res"):
        os.mkdir("res")
    for directory in map.values():
        try:
            if not os.path.exists(directory):
                os.mkdir(directory)
        except:
            print(f"examining directory,{directory}, failed unexpetedly")
            pass  # to handle possible future errors


def move_file(file_path: str, destination_dir: str) -> None:
    """
    Move a file to the specified destination directory.
    """

    try:
        shutil.move(file_path, os.path.join(destination_dir, os.path.basename(file_path)))  # Use shutil.move  
        print(f"Moved: {file_path} -> {destination_dir}")
    except Exception as e:
        print(f"Failed to move '{file_path}' to '{destination_dir}': {e}")


def traverse_directory_tree() -> None:
    for root, _, files in os.walk("."):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1]  # Get the file extension
            if file_path.endswith("project_file_formatter.py") or  file_path.endswith("data-base.json"):
                continue
            # Move the file if its type is in the mapping
            if file_extension in types_map_places:
                move_file(file_path, types_map_places[file_extension])
            else:
                # future handling
                pass
    dir_list: list[str] = os.listdir()
    for file in dir_list:
        if os.path.isfile(file):
            if file.endswith("project_file_formatter.py") or  file.endswith("data-base.json") or file.startswith(".") or file.endswith(".md"):
                continue
            os.rename(file, f"{types_map_places[file[file.rfind('.'):]]}{file}")


def clean_unused(map: Dict[str, str]) -> None:  
    """  
    Remove directories that are empty and do not exist in the mapping.  
    """
    for directory in map.values():  
        try:  
            # Check if the directory exists  
            if os.path.exists(directory):  
                # Check if the directory is empty  
                if not os.listdir(directory):  
                    os.rmdir(directory)  # Remove the empty directory
            else:  
                pass 
        except Exception as e:  
            print(f"Examining directory '{directory}' failed unexpectedly: {e}")  
    if not os.listdir("res"):
        os.rmdir("res")
        print("no files in res")
    print("cleaned succesfully")



def main() -> None:
    # Create directories if they do not exist
    initialize_directories(types_map_places)
    # Traverse the directory tree
    traverse_directory_tree()  
    # Clean unused directories
    clean_unused(types_map_places)


if __name__ == "__main__":
    main()