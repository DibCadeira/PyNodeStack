import os
import json
from parser import parse


def _read_content(path: str) -> str:
    """Reads and returns the content of the file at the given path."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def bundler(output: str) -> None:
    """
    Reads .pyn files from the src/nodes directory, parses them,
    and writes the results to a JSON file.

    Args:
        output (str): The path to the output JSON file.
    """
    path = os.path.abspath("src/nodes")
    bundle = {}

    for folder in os.listdir(path):
        folderpath = os.path.join(path, folder)

        if os.path.isdir(folderpath):
            for filename in os.listdir(folderpath):
                if filename.endswith(".pyn"):
                    filepath = os.path.join(folderpath, filename)

                    try:
                        content = _read_content(filepath)
                        node = parse(folder, content)
                        name = filename.replace(".pyn", "")
                        node["name"] = name
                        bundle[name] = node

                    except Exception as e:
                        print(f"Error processing file {filepath}: {e}")

    try:
        with open(output, "w", encoding="utf-8") as file:
            json.dump(bundle, file, indent=4)

    except Exception as e:
        print(f"Error writing to output file {output}: {e}")


if __name__ == "__main__":
    bundler("bundle.json")
    print("nodes bundled!")
