#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    resp = get(argv[1])
    print(resp.headers.get('X-Request-Id'))
