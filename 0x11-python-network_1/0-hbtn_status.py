#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""


from urllib import request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as req:
        resp = req.read()
        print("Body resp:")
        print("\t- type: {}".format(type(resp)))
        print("\t- content: {}".format(resp))
        print("\t- utf8 content: {}".format(resp.decode("utf-8")))
