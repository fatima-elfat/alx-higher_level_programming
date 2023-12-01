#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and
displays the body of the response."""


import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.get(argv[1])
    err = resp.status_code
    if err >= 400:
        print("Error code: {}".format(err))
    else:
        print(resp.text)
