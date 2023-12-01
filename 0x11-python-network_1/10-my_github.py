#!/usr/bin/python3
"""script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""


import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    URL = "https://api.github.com/user"
    auth_ = HTTPBasicAuth(argv[1], argv[2])
    resp = requests.get(URL, auth=auth_)
    print(resp.json().get("id"))
