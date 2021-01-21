#!/usr/bin/python3
""" Project: Python - Inheritance """

Rectangle = __import__('8-rectangle').Rectangle

class Rectangle(BaseGeometry):
    """ Class BaseGeometry """

    def __init__(self, width, height):
        """ initialization """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
