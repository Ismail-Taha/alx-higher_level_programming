#!/usr/bin/python3

"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as response:
        body_resp = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_resp)))
        print("\t- content: {}".format(body_resp))
        print("\t- utf8 content: {}".format(body_resp.decode("utf-8")))
