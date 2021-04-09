#!/usr/bin/python3
""" Python Network #1 Project """
import urllib.request as ur
import urllib.parse as up
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    values = {'email': email}
    data = up.urlencode(values)
    data = data.encode('ascii')
    req = ur.Request(sys.argv[1], data)
    with ur.urlopen(req) as response:
        html = response.read()
        print(html)
