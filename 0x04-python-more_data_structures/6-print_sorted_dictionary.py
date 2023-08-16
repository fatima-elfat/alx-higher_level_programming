#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    it = = sorted(a_dictionary.items())
    for key, val in it:
        print("{}: {}".format(key, val))
