#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”"""


import requests
from sys import argv

if __name__ == "__main__":
    a = "https://api.github.com/repos"
    URL = "{}/{}/{}/commits".format(a, argv[2], argv[1])
    resp = requests.get(URL)
    commits = resp.json()
    print(commits)
