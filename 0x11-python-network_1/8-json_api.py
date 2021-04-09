#!/usr/bin/python3
""" Python Network #1 Project """
import requests as r
import sys


if __name__ == "__main__":
    values = {'q': sys.argv[1] if len(argv) > 1 else ""}
    req = r.post("http://0.0.0.0:5000/search_user", data=values)
    try:
        json = req.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
