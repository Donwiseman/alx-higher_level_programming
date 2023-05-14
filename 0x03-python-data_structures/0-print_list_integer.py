#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints a list of integers to stdout"""
    for value in my_list:
        print("{}".format(value))


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
