#!/usr/bin/python3
""" Project: Python - Inheritance """


def is_same_class(obj, a_class):
    """ returns Ttue if obj is exactly an instance of a_class """
    if type(obj).__name__ == a_class.__name__:
        return True
    else:
        return False
