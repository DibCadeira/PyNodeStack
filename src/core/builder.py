from src.core.parser import parse
import os
import json


def file_content(path):
    with open(path, "r") as file:
        return file.read()


def build(output: str):
    path = os.path.abspath("src/nodes")
    packages = {}

    for folder in os.listdir(path):
        folderpath = f"{path}\\{folder}"

        for filename in os.listdir(folderpath):
            content = file_content(f"{folderpath}\\{filename}")
            node = parse(folder.split("\\")[-1], content)
            name = filename.replace(".pyn", "")
            packages[name] = node

    with open(output, "w") as file:
        json.dump(packages, file, indent=4)
