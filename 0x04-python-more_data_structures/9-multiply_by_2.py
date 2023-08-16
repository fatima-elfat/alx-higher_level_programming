#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    b_dictionary = a_dictionary.copy()
    for key, val in b_dictionary.items():
        b_dictionary[key] = val * 2
    return b_dictionary
