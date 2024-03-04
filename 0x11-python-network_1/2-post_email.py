#!/usr/bin/python3
"""
 Python script that takes in a URL, sends a request to the URL and displays
 the value of the X-Request-Id variable found in the header of the response.
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    url, email = sys.argv[1:]

    data = urllib.parse.urlencode({"email": email})
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as resp:
        print(resp.read().decode('utf-8'))
