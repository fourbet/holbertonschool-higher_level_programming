#!/usr/bin/python3
""" Project: Python - Almost a Circle """
import json
import os.path
from os import path


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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        with open("{}.json".format(cls.__name__),
                  mode='w', encoding='utf-8') as file:
            list_dict = []
            for obj in list_objs:
                list_dict.append(cls.to_dictionary(obj))
            file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == {}:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """  returns an instance with all attributes already set """
        rect = cls(10, 10, 10, 10)
        cls.update(rect, **dictionary)
        return rect

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        if path.exists("{}.json".format(cls.__name__)) is False:
            return []
        with open("{}.json".format(cls.__name__), mode='r',
                  encoding='utf-8') as f:
            list_instance = []
            list_dict = f.read()
            list_output = cls.from_json_string(list_dict)
            for elem in list_output:
                list_instance.append(cls.create(**elem))
        return list_instance
