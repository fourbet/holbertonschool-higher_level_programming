#!/usr/bin/python3
""" Python Network #1 Project """
import urllib.request as ur
import sys

if __name__ == "__main__":
    req = ur.Request(sys.argv[1])
    with ur.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
