#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    vals = []
    if my_list:
        for i in my_list:
            if i % 2 is 0:
                vals.append(True)
            else:
                vals.append(False)
        return vals
