#!/usr/bin/python3
"""a module conatining definition of the square class with instantiation"""


class Square(object):
    """A class that performs various actions related to a square"""
    def __init__(self, size):
        """ instantiation of the square class

        Args:
            __size (int): size of the square

        """
        self.__size = size
