#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if a is not (ord('q')) and a is not (ord('e')):
        print('{}'.format(chr(a)), end='')
