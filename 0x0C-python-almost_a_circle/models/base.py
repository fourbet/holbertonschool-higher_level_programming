#!/usr/bin/python3
""" Project: Python - Almost a Circle """


class Base:
    """ This class is the "base" of all other classes in this project.
    The goal is to manage id attributes in all classes and to avoid
    duplicating the same code """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
