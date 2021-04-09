#!/usr/bin/python3
""" Python Network #1 Project """
import requests as r

if __name__ == "__main__":
    req = r.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(req.text.__class__))
    print("\t- content: {}".format(req.text))
