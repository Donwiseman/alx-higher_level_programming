#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints a list of integers in reverse to stdout"""
    for value in my_list[-1::-1]:
        print("{:d}".format(value))
