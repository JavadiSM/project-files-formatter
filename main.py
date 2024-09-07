import os
from typing import Dict
import json
import module.module_project  # type: ignore


types_map_places: Dict[str, str]
with open("data-base.json") as info:
    types_map_places = json.load(info)
    for key, value in types_map_places.items():
        types_map_places[key] = value.replace("/", os.sep)


def main() -> None:
    # Create directories if they do not exist
    module.module_project.initialize_directories(types_map_places)
    # Traverse the directory tree
    module.module_project.traverse_directory_tree()
    # Clean unused directories
    module.module_project.clean_unused(types_map_places)


if __name__ == "__main__":
    main()
