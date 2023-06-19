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

    def test_area(self):
        a = Rectangle(5, 4, 1, 1)
        self.assertEqual(a.area(), 20)

    def test_area2(self):
        a = Rectangle(5, 4, 1, 1)
        a.width = 6
        self.assertEqual(a.area(), 24)

    def test_str(self):
        a = Rectangle(5, 4, 1, 1, 12)
        self.assertEqual(str(a), "[Rectangle] (12) 1/1 - 5/4")

    def test_str2(self):
        a = Rectangle(5, 4, 1, 1, 12)
        a.height = 13
        a.x = 3
        self.assertEqual(str(a), "[Rectangle] (12) 3/1 - 5/13")

    def test_update_args(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89)
        self.assertEqual(str(a), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_args1(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 2)
        self.assertEqual(str(a), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_args2(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 2, 3)
        self.assertEqual(str(a), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_args3(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 2, 3, 4)
        self.assertEqual(str(a), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_args4(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 2, 3, 4, 5)
        self.assertEqual(str(a), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(id=89)
        self.assertEqual(str(a), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_kwargs1(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(id=89, width=2)
        self.assertEqual(str(a), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_kwargs2(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(id=89, width=2, height=3)
        self.assertEqual(str(a), "[Rectangle] (89) 10/10 - 2/3")

    def test_update_kwargs3(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(id=89, x=4, height=3, width=2)
        self.assertEqual(str(a), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_args4(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(height=3, width=2, id=89, y=5, x=4)
        self.assertEqual(str(a), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_toomany_kwargs(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(height=3, width=2, id=89, y=5, x=4, men="hard", perimeter=40)
        self.assertEqual(str(a), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_and_kwargs(self):
        a = Rectangle(10, 10, 10, 10, 10)
        a.update(89, 2, 3, 4, width=8, height=9)
        self.assertEqual(str(a), "[Rectangle] (89) 4/10 - 2/3")

    def test_update_wrong_kwargs1(self):
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg='width must be an integer'):
            a.update(height=3, width='2', id=89, y=5, x=4)

    def test_update_wrong_kwargs2(self):
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg='height must be an integer'):
            a.update(height=[3, 5], width=2, id=89, y=5, x=4)

    def test_update_wrong_kwargs3(self):
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg='x must be >= 0'):
            a.update(height=3, width=2, id=89, y=5, x=-4)

    def test_update_wrong_kwargs4(self):
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg='y must be >= 0'):
            a.update(y=-5, x=4)

    def test_update_wrong_args(self):
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg='y must be >= 0'):
            a.update(89, 2, 3, 4, -5)

    def test_update_wrong_args1(self):
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(ValueError, msg='width must be > 0'):
            a.update(89, 0)

    def test_update_wrong_args2(self):
        a = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError, msg='width must be an integer'):
            a.update(89, 10.235)

    def test_to_dictionary(self):
        r = Rectangle(4, 3, 1, 1, 19)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 19, 'width': 4, 'height': 3, 'x': 1,
                             'y': 1})

    def test_to_dictionary2(self):
        r = Rectangle(4, 3, 1, 1, 19)
        r.update(height=4)
        d = r.to_dictionary()
        self.assertEqual(d, {'id': 19, 'width': 4, 'height': 4, 'x': 1,
                             'y': 1})

    def test_to_dictionary3(self):
        r = Rectangle(4, 3, 1, 1)
        r2 = Rectangle(2, 4, 3, 3)
        r2.update(**r.to_dictionary())
        self.assertEqual(r.to_dictionary(), r2.to_dictionary())
