#!/usr/bin/python3
""" Module doc """
import math


class MagicClass:
    """ Magic calculation """
    def __init__(self, radius):
        """ initialization """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not (float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ area """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ circumference """
        return 2 * math.pi * self.__radius
