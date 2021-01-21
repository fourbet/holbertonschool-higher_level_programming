#!/usr/bin/python3
""" Project: Python - Inheritance """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Class BaseGeometry """

    def __init__(self, width, height):
        """ initialization """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
