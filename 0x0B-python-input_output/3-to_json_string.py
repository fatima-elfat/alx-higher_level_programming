#!/usr/bin/python3
"""
the module 3. To JSON string.
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string).
    Args:
        my_obj: the input object.
    Return:
        json representation.
    """
    return json.dumps(my_obj)
