#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and displays the value
of the X-Request-Id variable found in the header
of the response."""

from urllib import request
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as resp:
        print(resp.getheader("X-Request-Id"))
