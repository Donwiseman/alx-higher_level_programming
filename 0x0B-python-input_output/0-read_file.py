#!/usr/bin/python3
"""This conatins a function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str, optional): file path to the file to be read

    """
    with open(filename, 'r', encoding='UTF-8') as text:
        for line in text:
            print(line, end='')
