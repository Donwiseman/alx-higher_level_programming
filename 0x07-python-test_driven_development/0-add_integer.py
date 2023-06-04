#!/usr/bin/python3
""" This module contains a single function that adds integer

    doctest for this module available in tests/0-add_integer.txt

"""


def add_integer(a, b=98):
    """adds the value of two integers and returns it

    Args:
        a (int or float): An integer or float to be added
        b (int or float): An integer or float to be added, default of 98

    Raises:
        TypeError: raises error if args are not an int or float

    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    num1 = int(a)
    num2 = int(b)
    return num1 + num2
