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
    t = zip(roman_string, roman_string[1:])
    for i, j in t:
        if i not in roman_dic.keys():
            return 0
        elif roman_dic[i] < roman_dic[j]:
            r -= roman_dic[i]
        else:
            r += roman_dic[i]
    r += roman_dic[roman_string[-1]]
    return r
