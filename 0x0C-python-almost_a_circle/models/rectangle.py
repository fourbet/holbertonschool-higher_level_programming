#!/usr/bin/python3
""" Project: Python - Almost a Circle """
from models.base import Base

class Rectangle(Base):
    """ Class Rectangle inheriths from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        self.integer_validator("width", width)
        self.under_equal_validator("width", width)
        self.integer_validator("height", height)
        self.under_equal_validator("height", height)
        self.integer_validator("x", x)
        self.under_validator("x", x)
        self.integer_validator("y", y)
        self.under_validator("y", y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character # """
        r = ""
        r += "\n" * self.__y
        for i in range(self.__height):
            r += " " * self.__x + "#" * self.__width + "\n"
        print(r, end="")

    def __str__(self):
        """ Print method """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        lists= ("id","width", "height", "x", "y")
        i = 0
        for arg in args:
            if (i > 4):
                break
            if arg is None and i == 0:
                super().__init__()
            else:
                setattr(self, lists[i], arg)
            i += 1
        if kwargs is not None and i == 0:
            for k, v in kwargs.items():
                if k == "id" and v is None:
                    super().__init__()
                else:
                    setattr(self, k, v)
        

    def integer_validator(self, name, value):
        """ Checks if the input is an integer """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def under_equal_validator(self, name, value):
        """ Checks if the input is under or equals 0"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def under_validator(self, name, value):
        """ Checks if the input is under 0 """
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """ getter width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter width """
        self.integer_validator("width", value)
        self.under_equal_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """ getter height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter height """
        self.integer_validator("height", value)
        self.under_equal_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """ getter x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter x """
        self.integer_validator("x", value)
        self.under_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """ getter y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter y """
        self.integer_validator("y", value)
        self.under_validator("y", value)
        self.__y = value
    
