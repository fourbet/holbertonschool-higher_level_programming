#!/usr/bin/python3
""" Project: Python Almost a Circle """
from models.base import Base
from models.rectangle import Rectangle
import unittest

class TestBase(unittest.TestCase):
    """ Unit test Base class """

    def setUp(self):
        Base._Base__nb_objects = 0
        self.rect_1 = Rectangle(5, 8)
        self.rect_2 = Rectangle(2, 3, 1, 1)
        self.rect_3 = Rectangle(4, 4, 7, 9, 12)
        self.rect_4 = Rectangle(2, 5, 7)

    def test_id(self):
        self.assertEqual(1, self.rect_1.id)
        self.assertEqual(2, self.rect_2.id)
        self.assertEqual(12, self.rect_3.id)
        self.assertEqual(3, self.rect_4.id)

    def test_width(self):
        self.assertEqual(5, self.rect_1.width)
        self.assertEqual(2, self.rect_2.width)
        self.assertEqual(4, self.rect_3.width)
        self.assertEqual(2, self.rect_4.width)

    def test_height(self):
        self.assertEqual(3, self.rect_2.height)
        self.assertEqual(8, self.rect_1.height)
        self.assertEqual(4, self.rect_3.height)
        self.assertEqual(5, self.rect_4.height)

    def test_x(self):
        self.assertEqual(0, self.rect_1.x)
        self.assertEqual(7, self.rect_3.x)
        self.assertEqual(1, self.rect_2.x)
        self.assertEqual(7, self.rect_4.x)

    def test_y(self):
        self.assertEqual(0, self.rect_1.y)
        self.assertEqual(9, self.rect_3.y)
        self.assertEqual(1, self.rect_2.y)
        self.assertEqual(0, self.rect_4.y)

    def test_not_integer(self):
        tuples = ("A", True, [5], None, (4,), {3, 4})
        for elem in tuples:
            self.assertRaises(TypeError, Rectangle, elem, 5)
            self.assertRaises(TypeError, Rectangle, 1, elem)
            self.assertRaises(TypeError, Rectangle, 1, 1, elem)
            self.assertRaises(TypeError, Rectangle, 1, 1, 1, elem)

    def test_under_equal(self):
        self.assertRaises(ValueError, Rectangle, -1, 5)
        self.assertRaises(ValueError, Rectangle, 0, 5)
        self.assertRaises(ValueError, Rectangle, 4, -1)
        self.assertRaises(ValueError, Rectangle, 4, 0)

    def test_under(self):
        self.assertRaises(ValueError, Rectangle, 4, 5, -5)
        self.assertRaises(ValueError, Rectangle, 4, 5, 5, -10)
