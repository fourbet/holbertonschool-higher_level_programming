#!/usr/bin/python3
""" Python Network #1 Project """
import requests as r
import sys

if __name__ == "__main__":
    req = r.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
