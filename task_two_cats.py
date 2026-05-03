from pathlib import Path
from helpers import file_path
from helpers.data import parse_lines


def get_cats_info(path: Path):
    lines = parse_lines(path, "id,name,age")
    if lines is None:
        return None
    cats = []
    for line in lines:
        try:
            cat_id, name, age = line.split(",")
            cats.append({"id": cat_id, "name": name, "age": age})
        except ValueError:
            print(f"Invalid line format: '{line}'. Expected: id,name,age")
            return None
    return cats

path = file_path.get_file_path("cats.txt") 
print(get_cats_info(path))