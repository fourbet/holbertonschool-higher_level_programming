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
