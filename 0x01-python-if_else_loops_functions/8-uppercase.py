#!/usr/bin/python3
def uppercase(str):
    r = ""
    for a in str:
        if (ord(a) >= ord('a')) and (ord(a) <= ord('z')):
            r += chr(ord(a) - 32)
        else:
            r += a
    print('{}'.format(r))
