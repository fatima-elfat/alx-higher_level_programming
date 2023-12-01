#!/usr/bin/python3
"""script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter."""


import requests
from sys import argv

if __name__ == "__main__":
    URL = "http://0.0.0.0:5000/search_user"
    letter = "" if len(argv) < 2 else argv[1]
    l_val = {"q": letter}
    resp = requests.post(URL, data=l_val)
    try:
        resp_dict = resp.json()
        if resp_dict:
            print("[{}] {}".format(
                resp_dict.get("id"),
                resp_dict.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
