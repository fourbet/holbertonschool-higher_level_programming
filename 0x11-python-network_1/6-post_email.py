#!/usr/bin/python3
""" Python Network #1 Project """
import requests as r
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    values = {'email': email}
    req = r.post(sys.argv[1], data=values)
    print(req.text)
