#!/usr/bin/python3
""" Project: Pyhton Input-Output """


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8) and returns
    the number of characters added"""
    with open(filename, mode='a', encoding='utf-8') as f:
        before = f.tell()
        f.write(text)
        return f.tell() - before
