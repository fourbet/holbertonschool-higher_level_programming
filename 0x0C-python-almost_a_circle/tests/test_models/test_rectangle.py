#!/usr/bin/python3
""" Project: Python Almost a Circle """
from models.base import Base
from models.rectangle import Rectangle
import unittest
import sys
from unittest.mock import patch, call
from io import StringIO

class TestRectangle(unittest.TestCase):
    """ Unit test Rectangle class """

    def setUp(self):
        Base._Base__nb_objects = 0
        self.rect_1 = Rectangle(5, 8)
        self.rect_2 = Rectangle(2, 3, 1, 1)
        self.rect_3 = Rectangle(4, 4, 7, 9, 12)
        self.rect_4 = Rectangle(2, 5, 7)
        self.held, sys.stdout = sys.stdout, StringIO()

    @patch('models.rectangle')
    def test_display_1(self, mocked_print):
        r1 = Rectangle(1, 1)
        r1.display()
        self.assertEqual(sys.stdout.getvalue(), '#\n')
        r1 = Rectangle(2, 3, 2, 2)
        sys.stdout = StringIO()
        r1.display()
        self.assertEqual(sys.stdout.getvalue(), '\n\n  ##\n  ##\n  ##\n')
        sys.stdout = StringIO()
        r2 = Rectangle(3, 2, 1, 0)
        r2.display()
        self.assertEqual(sys.stdout.getvalue(), ' ###\n ###\n')


    def test_to_dictionary(self):
        self.assertEqual(self.rect_1.to_dictionary(),
                         {'width': 5, 'height': 8, 'id': 1, 'x': 0, 'y': 0})
        self.assertEqual(self.rect_2.to_dictionary(),
                         {'width': 2, 'height': 3, 'id': 2, 'x': 1, 'y': 1})
        self.assertEqual(self.rect_3.to_dictionary(),
                         {'width': 4, 'height': 4, 'id': 12, 'x': 7, 'y': 9})
        self.assertEqual(self.rect_4.to_dictionary(),
                         {'width': 2, 'height': 5, 'id': 3, 'x': 7, 'y': 0})
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

    def test_area(self):
        self.assertEqual(40, self.rect_1.area())
        self.assertEqual(6, self.rect_2.area())
        self.assertEqual(16, self.rect_3.area())
        self.assertEqual(10, self.rect_4.area())

    def test_str(self):
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (1) 0/0 - 5/8")
        self.assertEqual(self.rect_2.__str__(), "[Rectangle] (2) 1/1 - 2/3")
        self.assertEqual(self.rect_3.__str__(), "[Rectangle] (12) 7/9 - 4/4")
        self.assertEqual(self.rect_4.__str__(), "[Rectangle] (3) 7/0 - 2/5")

    def test_update(self):
        self.rect_1.update(1, 10, 10, 10, 10)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        self.rect_1.update()
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        self.rect_1.update(89)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        self.rect_1.update(89, 2)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        self.rect_1.update(89, 2, 3)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        self.rect_1.update(89, 2, 3, 4)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        self.rect_1.update(89, 2, 3, 4, 5)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        self.rect_1.update(89, 2, 3, 4, 5, 7)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        self.rect_1.update(1, 10, 10, 10, 10)
        self.rect_1.update(height=1)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        self.rect_1.update(width=1, x=2)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        self.rect_1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        self.rect_1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        self.rect_1.update(10, 5, 3, 4, x=1, height=2, y=3, width=4)
        self.assertEqual(self.rect_1.__str__(), "[Rectangle] (10) 4/3 - 5/3")


    def test_update_not_integer(self):
        tuples = ("A", True, [5], None, (4,), {3, 4})
        for elem in tuples:

            msg = "width must be an integer"
            with self.assertRaises(TypeError) as e:
                self.rect_1.update(4, elem)
            self.assertEqual(msg, str(e.exception))

            self.assertRaises(TypeError, self.rect_1.update, 5, elem)
            self.assertRaises(TypeError, self.rect_1.update, 5, 5, elem)
            self.assertRaises(TypeError, self.rect_1.update, 5, 5, 5, elem)
            self.assertRaises(TypeError, self.rect_1.update, 5, 5, 5, 5, elem)

    def test_update_under_equal(self):
        msg = "width must be > 0"
        with self.assertRaises(ValueError) as e:
            self.rect_1.update(4, -10)
        self.assertEqual(msg, str(e.exception))

        self.assertRaises(ValueError, self.rect_1.update, 5, -5)
        self.assertRaises(ValueError, self.rect_1.update, 5, 0)
        self.assertRaises(ValueError, self.rect_1.update, 5, 5, -4)
        self.assertRaises(ValueError, self.rect_1.update, 5, 5, 0)

    def test_update_under(self):
        msg = "x must be >= 0"
        with self.assertRaises(ValueError) as e:
            self.rect_1.update(4, 4, 4, -10)
        self.assertEqual(msg, str(e.exception))

        self.assertRaises(ValueError, self.rect_1.update, 5, 5, 5, -10)
        self.assertRaises(ValueError, self.rect_1.update, 5, 5, 5, 5, -10)

