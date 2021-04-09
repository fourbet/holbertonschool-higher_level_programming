#!/usr/bin/python3
""" Python Network #1 Project """
import urllib.request as ur

if __name__ == "__main__":
    req = ur.Request('https://intranet.hbtn.io/status')
    with ur.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode()))
