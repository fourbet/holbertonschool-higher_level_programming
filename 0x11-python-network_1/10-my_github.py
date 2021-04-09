#!/usr/bin/python3
""" Python Network #1 Project """
import requests as r
import sys


if __name__ == "__main__":
    req = r.get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2]))
    print(req.json().get('id'))
