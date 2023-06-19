#!/usr/bin/python3

from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """various test cases for the Square class"""
    def test_instantiation(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_instantiation2(self):
        s1 = Square(5, 1, 1, 2)
        self.assertEqual(str(s1), "[Square] (2) 1/1 - 5")

    def test_instantiation3(self):
        s1 = Square(3, 4)
        self.assertEqual(s1.y, 0)

    def test_wrong_instantiation(self):
        with self.assertRaises(TypeError, msg='width must be an integer'):
            s1 = Square('5')

    def test_wrong_instantiation2(self):
        with self.assertRaises(TypeError, msg='x must be an integer'):
            s1 = Square(5, '7', 7)

    def test_wrong_instantiation3(self):
        with self.assertRaises(ValueError, msg='x must be >= 0'):
            s1 = Square(5, -7, 7)

    def test_wrong_instantiation4(self):
        with self.assertRaises(ValueError, msg='width must be > 0'):
            s1 = Square(0, 7, 7)

    def test_wrong_instantiation5(self):
        with self.assertRaises(Exception):
            s1 = Square()

    def test_wrong_instantiation6(self):
        with self.assertRaises(Exception):
            s1 = Square(5, 2, 2, 19, 56, 2)

    def test_property(self):
        s1 = Square(5, 1, 1, 190)
        s1.size = 8
        self.assertEqual(str(s1), "[Square] (190) 1/1 - 8")

    def test_property(self):
        s1 = Square(5, 1, 1, 190)
        self.assertEqual(s1.size, 5)

    def test_update_args(self):
        s1 = Square(5)
        s1.update(190)
        self.assertEqual(str(s1), "[Square] (190) 0/0 - 5")

    def test_update_args2(self):
        s1 = Square(5)
        s1.update(190, 10)
        self.assertEqual(str(s1), "[Square] (190) 0/0 - 10")

    def test_update_args3(self):
        s1 = Square(5)
        s1.update(190, 10, 2)
        self.assertEqual(str(s1), "[Square] (190) 2/0 - 10")

    def test_update_args4(self):
        s1 = Square(5)
        s1.update(190, 10, 2, 2)
        self.assertEqual(str(s1), "[Square] (190) 2/2 - 10")

    def test_update_kwargs(self):
        s1 = Square(5)
        s1.update(id=190, size=10)
        self.assertEqual(str(s1), "[Square] (190) 0/0 - 10")

    def test_update_kwargs1(self):
        s1 = Square(5)
        s1.update(id=190, size=10, y=2)
        self.assertEqual(str(s1), "[Square] (190) 0/2 - 10")

    def test_update_kwargs2(self):
        s1 = Square(5)
        s1.update(id=190, x=10)
        self.assertEqual(str(s1), "[Square] (190) 10/0 - 5")

    def test_update_kwargs3(self):
        s1 = Square(5)
        s1.update(id=190, size=10, x=2, y=2)
        self.assertEqual(str(s1), "[Square] (190) 2/2 - 10")

    def test_update_args_kwargs(self):
        s1 = Square(5)
        s1.update(190, 10, 2, id =24, size=7)
        self.assertEqual(str(s1), "[Square] (190) 2/0 - 10")

    def test_update_args_kwargs1(self):
        s1 = Square(5)
        s1.update(190, 10, 2, id =24, size=7, y=2)
        self.assertEqual(str(s1), "[Square] (190) 2/0 - 10")

    def test_update_toomany_kwargs(self):
        s1 = Square(5)
        s1.update(id=190, perimeter=50, height=10, x=2, y=2)
        self.assertEqual(str(s1), "[Square] (190) 2/2 - 5")
