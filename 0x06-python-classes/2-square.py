#!/usr/bin/python3
"""defines a square by: (based on 1-square.py) and adds type checking"""


class Square(object):
    """A class that performs various actions related to a square"""
    def __init__(self, size=0):
        """ instantiation of the square class

        Args:
            __size (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
