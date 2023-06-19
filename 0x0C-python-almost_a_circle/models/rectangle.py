#!/usr/bin/python3
""" This defines a Rectangle class which inherits from the Base class."""

from models.base import Base


class Rectangle(Base):
    """Defines the rectangle class which inherits from the Base class

    This class has the __str__ method which returns the string representation
    of the class instance, area method which returns the area of the rectangle
    instance, the display method which displays the rectangle using `#` symbol
    and attributes x and y for horizontal and vertical spacing respectively

    Attributes:
        width (int): propety which defines the width of the rectangle
        height (int): property which defines the height of the rectangle
        x (int, optional): defines the horizontal printing space for the shape
        y (int, optional): defines the vertical printing space before the shape

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates the class with it's attributes

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int, optional): horizontal space when printing rectangle
            y (int, optional): vertical space when printing
            id (optional): id for the rectangle instance

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ The width property for the rectangle class

        Raises:
            TypeError: if width is not an int
            ValueError: if width is less tahn 0

        """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ The height property for the rectangle class

        Raises:
            TypeError: if height is not an int
            ValueError: if height is less tahn 0

        """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ The x property for the rectangle class

        Raises:
            TypeError: if x is not an int
            ValueError: if x is less tahn 0

        """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ The y property for the rectangle class

        Raises:
            TypeError: if x is not an int
            ValueError: if x is less tahn 0

        """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of this rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints a rectangle representation usin `#` symbol to the stdout
        and vlaue of x and y attributes to determine the horizontal and
        vertical spacing when printing respectively
        """
        if self.__y > 0:
            for y in range(self.__y):
                print()
        for height in range(self.__height):
            if self.__x > 0:
                print((" " * self.__x), end='')
            print(("#" * self.__width))

    def __str__(self):
        """Prints the string representation of the class instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle instance based on arguments

        This updates the various attributes of the rectange class using a
        combination of non keyword and keyword arguments
        Args:
            args: no-keyword positional argument
            kwargs: keyword positional argument.

        """
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.width = value
                elif index == 2:
                    self.height = value
                elif index == 3:
                    self.x = value
                elif index == 4:
                    self.y = value
        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
