#!/usr/bin/python3
"""
the module of 14. Log parsing.
Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption
(CTRL + C), prints those statistics since the beginning
"""
import sys


def print_stats(size, valid_codes):
    """
    prints computes metrics.

    Args:
        size : ...
        valid_codes : ...
    """
    print("File size: {:d}".format(size))
    for k, v in sorted(valid_codes.items()):
        if v:
            print("{:s}: {:d}".format(k, v))


if __name__ == "__main__":

    size = 0
    lines = 0
    valid_codes = {
            "200": 0, "301": 0,
            "400": 0, "401": 0,
            "403": 0, "404": 0,
            "405": 0, "500": 0
            }
    try:
        for line in sys.stdin:
            col = list(map(str, line.strip().split(" ")))
            try:
                size += int(col[-1])
            except (IndexError, ValueError):
                pass
            try:
                if col[-2] in valid_codes:
                    valid_codes[col[-2]] += 1
            except IndexError:
                pass
            lines += 1
            if lines % 10 == 0:
                print_stats(size, valid_codes)
    except KeyboardInterrupt:
        print_stats(size, valid_codes)
        raise
    print_stats(size, valid_codes)
