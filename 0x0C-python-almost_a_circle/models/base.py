#!/usr/bin/python3
""" This defines the base class of this package named `Base` which helps
    maintains the id of various instances of the class.
"""


class Base(object):
    """ This defines the base class used in this package.

    Attributes:
        id (int): the id of the class intance.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantiates the Base class

        Args:
            id (int, optional): the specific id for the class instance

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
