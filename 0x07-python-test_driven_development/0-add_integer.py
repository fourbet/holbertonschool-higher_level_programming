#!/usr/bin/python3
""" Module doc """


def add_integer(a, b=98):
    """ adds 2 integer """
    if b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")
    if a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    if not isinstance(a, int):
        a = int(a)
    if not isinstance(b, int):
        b = int(b)
    return a+b
