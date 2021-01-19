#!/usr/bin/python3
""" Project: Python - Inheritance """


class BaseGeometry:
    """ Class BaseGeometry """

    def area(self):
        """ Raises Error """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
