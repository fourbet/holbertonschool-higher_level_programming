#!/usr/bin/python3
""" Simple rectangle """


class Rectangle:
    """ class Rectangle defines a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialization """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """ returns the rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns the rectangle perimetter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """ informal string representation """
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
                rec += str(self.print_symbol) * self.__width + "\n"
        rec = rec[:-1]
        return rec

    def __repr__(self):
        """ official string representation """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ called when an instance is deleted """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
