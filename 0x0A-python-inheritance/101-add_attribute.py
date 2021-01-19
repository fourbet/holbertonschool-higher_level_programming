#!/usr/bin/python3
""" Project: Python - Inheritance """


def add_attribute(a_class, attr, value):
    """ adds a new attribute to an object if its possible """
    if dir(a_class)[0] is not "__class__":
        raise TypeError("can't add new attribute")
    setattr(a_class, attr, value)
