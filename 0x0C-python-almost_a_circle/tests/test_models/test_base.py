#!/usr/bin/python3
""" Project: Python Almost a Circle """
from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    """ Unit test Base class """

    def setUp(self):
        self.base = Base()

    def test_id(self):
        self.assertEqual(1, self.base.id)
