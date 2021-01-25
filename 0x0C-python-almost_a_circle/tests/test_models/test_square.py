#!/usr/bin/python3
""" Project: Python Almost a Circle """
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import unittest
from unittest.mock import patch
from io import StringIO
import sys


class TestSquare(unittest.TestCase):
    """ Unit test Square class """

    def setUp(self):
        Base._Base__nb_objects = 0
        self.s_1 = Square(5)
        self.s_2 = Square(2, 3)
        self.s_3 = Square(4, 1, 1)
        self.s_4 = Square(2, 2, 1, 5)

    @patch('models.square')
    def test_display_1(self, mocked_print):
        s1 = Square(5)
        s1.display()
        self.assertEqual(sys.stdout.getvalue(), '#####\n#####\n#####\n#####\n#####\n')
        s2 = Square(2, 2)
        sys.stdout = StringIO()
        s2.display()
        self.assertEqual(sys.stdout.getvalue(), '  ##\n  ##\n')
        sys.stdout = StringIO()
        s3 = Square(3, 1, 3)
        s3.display()
        self.assertEqual(sys.stdout.getvalue(), '\n\n\n ###\n ###\n ###\n')

    def test_area(self):
        self.assertEqual(25, self.s_1.area())
        self.assertEqual(4, self.s_2.area())
        self.assertEqual(16, self.s_3.area())
        self.assertEqual(4, self.s_4.area())

    def test_to_dictionary(self):
        self.assertEqual(self.s_1.to_dictionary(),
                         {'size': 5, 'id': 1, 'x': 0, 'y': 0})
        self.assertEqual(self.s_2.to_dictionary(),
                         {'size': 2, 'id': 2, 'x': 3, 'y': 0})
        self.assertEqual(self.s_3.to_dictionary(),
                         {'size': 4, 'id': 3, 'x': 1, 'y': 1})
        self.assertEqual(self.s_4.to_dictionary(),
                         {'size': 2, 'id': 5, 'x': 2, 'y': 1})

    def test_str(self):
        self.assertEqual(self.s_1.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(self.s_2.__str__(), "[Square] (2) 3/0 - 2")
        self.assertEqual(self.s_3.__str__(), "[Square] (3) 1/1 - 4")
        self.assertEqual(self.s_4.__str__(), "[Square] (5) 2/1 - 2")  


    def test_id(self):
        self.assertEqual(1, self.s_1.id)
        self.assertEqual(2, self.s_2.id)
        self.assertEqual(3, self.s_3.id)
        self.assertEqual(5, self.s_4.id)

    def test_size(self):
        self.assertEqual(5, self.s_1.size)
        self.assertEqual(2, self.s_2.size)
        self.assertEqual(4, self.s_3.size)
        self.assertEqual(2, self.s_4.size)

    def test_x(self):
        self.assertEqual(0, self.s_1.x)
        self.assertEqual(1, self.s_3.x)
        self.assertEqual(3, self.s_2.x)
        self.assertEqual(2, self.s_4.x)

    def test_y(self):
        self.assertEqual(0, self.s_1.y)
        self.assertEqual(1, self.s_3.y)
        self.assertEqual(0, self.s_2.y)
        self.assertEqual(1, self.s_4.y)

    def test_not_integer(self):
        tuples = ("A", True, [5], None, (4,), {3, 4})
        for elem in tuples:
            self.assertRaises(TypeError, Square, elem, 5)
            self.assertRaises(TypeError, Square, 1, elem)
            self.assertRaises(TypeError, Square, 1, 1, elem)

    def test_under_equal(self):
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 0)

    def test_under(self):
        self.assertRaises(ValueError, Square, 4, -5)
        self.assertRaises(ValueError, Rectangle, 4, 5, -10)


    def test_update(self):
        self.s_1.update(1, 10, 10, 10)
        self.assertEqual(self.s_1.__str__(), "[Square] (1) 10/10 - 10")
        self.s_1.update()
        self.assertEqual(self.s_1.__str__(), "[Square] (1) 10/10 - 10")
        self.s_1.update(89)
        self.assertEqual(self.s_1.__str__(), "[Square] (89) 10/10 - 10")
        self.s_1.update(89, 2)
        self.assertEqual(self.s_1.__str__(), "[Square] (89) 10/10 - 2")
        self.s_1.update(89, 2, 3)
        self.assertEqual(self.s_1.__str__(), "[Square] (89) 3/10 - 2")
        self.s_1.update(89, 2, 3, 4)
        self.assertEqual(self.s_1.__str__(), "[Square] (89) 3/4 - 2")
        self.s_1.update(1, 10, 10, 10)
        self.s_1.update(size=1)
        self.assertEqual(self.s_1.__str__(), "[Square] (1) 10/10 - 1")
        self.s_1.update(x=2)
        self.assertEqual(self.s_1.__str__(), "[Square] (1) 2/10 - 1")
        self.s_1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(self.s_1.__str__(), "[Square] (89) 3/1 - 2")
        self.s_1.update(10, 5, 3, 4, x=1, size=2, y=3)
        self.assertEqual(self.s_1.__str__(), "[Square] (10) 3/4 - 5")

    def test_update_not_integer(self):
        tuples = ("A", True, [5], None, (4,), {3, 4})
        for elem in tuples:
            
            msg = "width must be an integer"
            with self.assertRaises(TypeError) as e:
                self.s_1.update(4, elem)
            self.assertEqual(msg, str(e.exception))

            self.assertRaises(TypeError, self.s_1.update, 5, elem)
            self.assertRaises(TypeError, self.s_1.update, 5, 5, elem)
            self.assertRaises(TypeError, self.s_1.update, 5, 5, 5, elem)

    def test_update_under_equal(self):
        msg = "width must be > 0"
        with self.assertRaises(ValueError) as e:
            self.s_1.update(4, -10)
        self.assertEqual(msg, str(e.exception))

        self.assertRaises(ValueError, self.s_1.update, 5, -5)
        self.assertRaises(ValueError, self.s_1.update, 5, 0)

    def test_update_under(self):
        msg = "x must be >= 0"
        with self.assertRaises(ValueError) as e:
            self.s_1.update(4, 4, -10)
        self.assertEqual(msg, str(e.exception))

        self.assertRaises(ValueError, self.s_1.update, 5, 5, -10)
        self.assertRaises(ValueError, self.s_1.update, 5, 5, 5, -10)
