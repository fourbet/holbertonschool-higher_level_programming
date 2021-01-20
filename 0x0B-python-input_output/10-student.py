#!/usr/bin/python3
""" Project Python - Input Output """


class Student:
    """ class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student obj"""
        if attrs is not None:
            if all(isinstance(att, str) for att in attrs):
                return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
