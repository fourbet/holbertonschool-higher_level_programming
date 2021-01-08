"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unittest class """
    def test_positiv_result(self):
        """ test list of positive integers """
        list_a = [8, 5, 45, 1, 13]
        self.assertAlmostEqual(max_integer(list_a), 45)

    def test_negative_result(self):
        """ test list of negative integers """
        list_b = [-7, -7, -10, -41]
        self.assertAlmostEqual(max_integer(list_b), -7)

    def test_empty_list(self):
        """ test for empty list """
        list_c = []
        self.assertAlmostEqual(max_integer(list_c), None)
