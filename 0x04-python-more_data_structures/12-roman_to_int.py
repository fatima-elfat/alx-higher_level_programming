#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dic = {
            "I": 1, "V": 5,
            "X": 10, "L": 50,
            "C": 100, "D": 500,
            "M": 1000
            }
    if roman_string == "":
        return 0
    r = 0

