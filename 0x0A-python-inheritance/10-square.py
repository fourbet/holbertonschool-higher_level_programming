#!/usr/bin/python3
""" Project: Python - Inheritance """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size):
        """ initialization """
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """ returns the area of a square """
        return self.__size * self.__size

    def __str__(self):
        """ print """
        return super().__str__()
