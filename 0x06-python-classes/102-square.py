#!/usr/bin/python3
""" Module doc """


class Square:
    """ Class square that defines a square"""

    def __init__(self, size=0):
        """ initialization of the class square"""
        if not isinstance(size, (int, float)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns the current square area """
        return self.__size * self.__size

    def __eq__(self, other):
        """ equal comparison """
        return self.__size * self.__size == other.size * other.size

    def __lt__(self, other):
        """ strict inferior comparison """
        return self.__size * self.__size < other.size * other.size

    def __le__(self, other):
        """ inferior or equal to zero """
        return self.__size * self.__size <= other.size * other.size

    def __ne__(self, other):
        """ different comparison"""
        return self.__size * self.__size != other.size * other.size

    def __gt__(self, other):
        """ strict superior """
        return self.__size * self.__size > other.size * other.size

    def __ge__(self, other):
        """ superior or equal to zero """
        return self.__size * self.__size >= other.size * other.size

    @property
    def size(self):
        """ retieve size """
        return self.__size

    @size.setter
    def size(self, value):
        """ set size"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
