#!/usr/bin/python3
""" This module contains an implementation of the reactangle class.

    It is simply declared and has a constructor for instantiation
    with property methods and two instant methods area and perimeter.
    Also includes a string representation of the class(str) and a repr
    representation of the class

"""


class Rectangle:
    """ A Rectangle class which creates a rectangle object

    This has two public methods area for calculating area of the rectangle
    and perimeter for calculating perimeter of the rectangle; public class
    attribute print_symbol: string to be used to print the rectangle and
    includes str and repr methods. includes a destructor

    Attributes:
        print_symbol: string to be used to print the rectangle
        number_of_instances (int): (class Attribute) number of rectangles
        width (int): width of rectangle
        height (int): height of rectangle

    """

    number_of_instances = 0
    print_symbol = '#'

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
        type(self).number_of_instances += 1

    def __del__(self):
        """Prints an output when instance id destroyed"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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

    def __str__(self):
        """returns a string representation of this rectangle instance"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return (((str(type(self).print_symbol) * self.__width) + '\n') *
                (self.__height - 1)) + (str(type(self).print_symbol) *
                                        self.__width)

    def __repr__(self):
        """Returns a string representation for repr function."""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height)\
            + ')'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): one of the Rectangle instance to be compared
            rect_2 (Rectangle): the other Rectangle instance to compare

        Returns:
            the relatively bigger rectangle instance based on their area

        Raises:
            TypeError: if one or both arguments are not an instance of
            Rectangle class

        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area >= rect_2.area:
            return rect_1
        else:
            return rect_2
