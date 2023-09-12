#!/usr/bin/python3
"""
the module of 7. Load, add, save.
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
    __import__('6-load_from_json_file').load_from_json_file
try:
    itm = load_from_json_file("add_item.json")
except FileNotFoundError:
    itm = []
itm.extend(sys.argv[1:])
save_to_json_file(itm, "add_item.json")
