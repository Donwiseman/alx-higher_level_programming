#!/usr/bin/python3
"""This contains a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file.

    Args:
        filename (str): pathname of file to open
        text (str): text string to be appended to file

    Return:
        returns the number of characters added.

    """
    with open(filename, 'a', encoding='utf-8') as textfile:
        a = textfile.write(text)
        return a
