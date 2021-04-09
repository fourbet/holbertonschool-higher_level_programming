#!/usr/bin/python3
""" Python Network #1 Project """
import urllib.request as ur
import urllib.error as ue
import sys

if __name__ == "__main__":
    req = ur.Request(sys.argv[1])
    try:
        ur.urlopen(req)
    except ue.HTTPError as e:
        print("Error code: {}".format(e.code))
    else:
        with ur.urlopen(req) as response:
            html = response.read()
            print(html.decode())
