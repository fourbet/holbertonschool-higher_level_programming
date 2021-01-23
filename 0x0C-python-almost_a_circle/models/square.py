#!/usr/bin/python3
""" Project: Python - Almost a Circle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The class Square inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor of the class Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
