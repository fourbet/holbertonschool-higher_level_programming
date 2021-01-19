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


class Rectangle(BaseGeometry):
    """ Class BaseGeometry """

    def __init__(self, width, height):
        """ initialization """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """ returns the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ print """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
