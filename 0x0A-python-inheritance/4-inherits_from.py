#!/usr/bin/python3
""" Project: Python - Inheritance """


def inherits_from(obj, a_class):
    """ Checks if obj is an instance of a class that inherited
    from the specified class a_class """
    a = (issubclass(type(obj), a_class) and
         type(obj).__name__ != a_class.__name__)
    return a
