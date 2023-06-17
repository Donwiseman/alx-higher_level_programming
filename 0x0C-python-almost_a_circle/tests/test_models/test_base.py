#!/usr/bin/python3
"""A unnittest for the base module in th emodels package"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Contains various test cases for the Base class in models package"""
    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual((b1.id, b2.id, b3.id, b4.id, b5.id), (1, 2, 3, 12, 4))
