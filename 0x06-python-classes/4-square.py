#!/usr/bin/python3
class Square:
    "Class square that defines a square"

    def __init__(self, size=0):
        """ initialization of the class square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size

    @property
    def size(self):
        """ retieve size """
        return self.__size

    @size.setter
    def size(self, value):
        """ set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
