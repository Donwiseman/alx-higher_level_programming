#!/usr/bin/python3
"""This defines the Square class which inherits from Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from the Rectangle clas

    The Square class is a unique rectangle that has both width == height.

    Attributes:
        size (int): the size of the square denoting both it's width and height

    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates the square class

        Args:
            size (int): size of the square
            x (int, optional): horizontal spacing when displaying square
            y (int, optional): vertical spacing when displaying square
            id (optional): unique id of instance

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """updates the value of size which is the width and height of parent

        size must be an integer and be greater than 0 else a TypeError and
        Valueerror is raised respectively.
        """
        return super().width

    @size.setter
    def size(self, size):
        super().update(width=size, height=size)

    def __str__(self):
        """returns string representation of the class"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, super().x, super().y, super().width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the Square instance based on arguments

        This updates the various attributes of the Square class using either
        non keyword or keyword arguments
        Args:
            args: no-keyword positional argument
            kwargs: keyword positional argument.

        """
        if args:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    super().update(width=value)
                    super().update(height=value)
                elif index == 2:
                    super().update(x=value)
                elif index == 3:
                    super().update(y=value)
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                super().update(width=kwargs['size'])
                super().update(height=kwargs['size'])
            if 'x' in kwargs:
                super().update(x=kwargs['x'])
            if 'y' in kwargs:
                super().update(y=kwargs['y'])

    def to_dictionary(self):
        """Returns a dictionary conataining the attributes of the Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": super().x,
                "y": super().y
                }
