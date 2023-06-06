#!/usr/bin/python3
""" This module contains an implementation of the reactangle class.

    It is simply declared and has a constructor for instantiation
    with property methods and two instant methods area and perimeter

"""


class Rectangle:
    """ A Rectangle class which creates a rectangle object

    This has two public methods area for calculating area of the rectangle
    and perimeter for calculating perimeter of the rectangle

    Attributes:
        width (int): width of rectangle
        height (int): height of rectangle

    """

    def __init__(self, width=0, height=0):
        """ Instantiates the Rectangle class

        Args:
            width (int, optional): width of rectangle
            height (int, optional): height of rectangle

        Raises:
            TypeError: if attributes are not integer
            ValueError: if attributes has a negative value

        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Returns the height of rectangle

        Raises:
            TypeError: if height are not integer
            ValueError: if height has a negative value

        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Returns the width of the Rectangle

        Raises:
            TypeError: if width are not integer
            ValueError: if width has a negative value

        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ returns the area of this rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of this rectangle."""
        return 2 * (self.__width + self.__height)
