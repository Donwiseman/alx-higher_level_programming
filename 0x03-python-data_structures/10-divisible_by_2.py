#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return []
    new_list = [x % 2 == 0 for x in my_list]
    return new_list
