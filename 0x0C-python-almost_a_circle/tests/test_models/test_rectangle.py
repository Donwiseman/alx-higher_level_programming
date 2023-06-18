#!/usr/bin/python3
"""Unittest for the Rectangle class"""

from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Has various test cases for the rectangle class"""

    def test_instantiation_normal(self):
        a = Rectangle(10, 2)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)

    def test_instantiation_normal2(self):
        a = Rectangle(10, 2, 2, 2,)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 2)

    def test_instantiation_normal3(self):
        a = Rectangle(10, 2, 2, 0, 12)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 12)

    def test_wrong_instantiation(self):
        with self.assertRaises(TypeError, msg='width must be an integer'):
            a = Rectangle("2", 5)

    def test_wrong_instantiation2(self):
        with self.assertRaises(TypeError, msg='height must be an integer'):
            a = Rectangle(2, '5')

    def test_wrong_instantiation3(self):
        with self.assertRaises(TypeError, msg='x must be an integer'):
            a = Rectangle(2, 5, 'k')

    def test_wrong_instantiation4(self):
        with self.assertRaises(TypeError, msg='y must be an integer'):
            a = Rectangle(2, 5, 0, 'yu')

    def test_wrong_instantiation5(self):
        with self.assertRaises(ValueError, msg='width must be > 0'):
            a = Rectangle(0, 5)

    def test_wrong_instantiation6(self):
        with self.assertRaises(ValueError, msg='width must be > 0'):
            a = Rectangle(-10, 5)

    def test_wrong_instantiation7(self):
        with self.assertRaises(ValueError, msg='height must be > 0'):
            a = Rectangle(5, 0)

    def test_wrong_instantiation8(self):
        with self.assertRaises(ValueError, msg='height must be > 0'):
            a = Rectangle(5, -4)

    def test_wrong_instantiation9(self):
        with self.assertRaises(ValueError, msg='x must be >= 0'):
            a = Rectangle(5, 4, -1, 3)

    def test_wrong_instantiation10(self):
        with self.assertRaises(ValueError, msg='y must be >= 0'):
            a = Rectangle(5, 4, 1, -2)
