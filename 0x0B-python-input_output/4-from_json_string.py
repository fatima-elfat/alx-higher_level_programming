#!/usr/bin/python3
"""
the module 4. From JSON string to Object.
"""
import json


def from_json_string(my_str):
    """Returns python data structure from JSON string
    Args:
        my_str: json string representation
    Return:
        python object
    """
    return json.loads(my_str)
