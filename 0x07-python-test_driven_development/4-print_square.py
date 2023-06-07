#!/usr/bin/python3
"""Contains a single function which prints a square using "#"."""


def print_square(size):
    """prints a square with the character `#`

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size is not an int
        ValueError: if size is < 0

    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
        return
    for height in range(size):
        print('#' * size)
