#!/usr/bin/python3
""" Project: Pyhton Input-Output """


def read_file(filename=""):
    """ reads a text file (utf8) and prints it to stdout """
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end="")
