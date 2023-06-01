#!/usr/bin/python3
"""defines a square by: (based on 5-square.py) and adds position attribute"""


class Square(object):
    """A class that performs various actions related to a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ instantiation of the square class

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        """
        self.size = size
        self.position = position

    def area(self):
        """calculates the current area of the square

        Returns:
            int: area of the square presntly

        """
        return self.__size ** 2

    @property
    def size(self):
        """returnsthe value of the square size

        setter methos raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints the size of square to the stdout using `#`"""
        index = 0

        if self.__position[1] > 0:
            for x in range(self.__position[1]):
                print()
        while (self.__size > 0):
            if self.__position[0] != 0:
                for x in range(self.__position[0]):
                    print(' ', end='')
            for x in range(self.__size):
                print("#", end='')
            print()
            index += 1
            if index == self.__size:
                break
        else:
            print()

    @property
    def position(self):
        """returns the value of the position

        Raises:
            TypeError: if not a tuple of 2 containing positive integers

        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
