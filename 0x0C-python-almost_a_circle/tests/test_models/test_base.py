#!/usr/bin/python3
""" Project: Python Almost a Circle """
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestBase(unittest.TestCase):
    """ Unit test Base class """

    def setUp(self):
        Base._Base__nb_objects = 0
        self.base_1 = Base()
        self.base_2 = Base(15)
        self.base_3 = Base(None)

    def test_id(self):
        self.assertEqual(1, self.base_1.id)
        self.assertEqual(15, self.base_2.id)
        self.assertEqual(2, self.base_3.id)

    def test_nb_objects(self):
        self.assertEqual(2, Base._Base__nb_objects)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {'x': 2, 'width': 10, 'id': 1,
                                      'height': 7, 'y': 8})
        self.assertIsInstance(dictionary, dict)
        self.assertIsInstance(json_dictionary, str)
        Base.to_json_string([])
        Base.to_json_string([ { 'id': 12 }])

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertIsInstance(list_input, list)
        self.assertIsInstance(json_list_input, str)
        self.assertIsInstance(list_output, list)
