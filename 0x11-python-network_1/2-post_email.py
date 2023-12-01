#!/usr/bin/python3
"""script that takes in a URL and an email,
sends a POST request to the passed URL with
the email as a parameter, and displays the
body of the response (decoded in utf-8)"""


from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    eml = {"email": argv[2]}
    eml_data = parse.urlencode(eml).encode("ascii")
    req = request.Request(argv[1], eml_data)
    with request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
