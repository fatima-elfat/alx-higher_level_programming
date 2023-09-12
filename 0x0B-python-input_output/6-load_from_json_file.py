#!/usr/bin/python3
"""
the module of 6. Create object from a JSON file.
"""


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”.
    Args:
        filename: file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
