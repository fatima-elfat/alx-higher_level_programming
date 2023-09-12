#!/usr/bin/python3
"""
the moduleof 5. Save Object to a file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write a function that writes an Object
    to a text file, using a JSON representation.
    Args:
        my_obj: the object.
        filename: the name of the file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
