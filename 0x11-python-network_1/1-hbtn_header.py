#!/usr/bin/python3
"""Script that takes in a URL,
then sends request to the URL,
and displays value of the X-Request-Id
variable found in header of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
