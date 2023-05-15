#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints a list of integers in reverse to stdout"""
    if len(my_list) > 0:
        for value in my_list[-1::-1]:
            print("{:d}".format(value))
    else:
        print()
