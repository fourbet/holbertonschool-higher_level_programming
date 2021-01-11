#!/usr/bin/python3
""" Simple rectangle """


class Rectangle:
    """ class Rectangle defines a rectangle """

    def __init__(self, width=0, height=0):
        """ initialization """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
