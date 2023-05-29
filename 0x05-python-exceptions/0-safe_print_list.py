#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    if x == 0:
        return x
    for value in my_list:
        try:
            print("{}".format(value), end="")
            count += 1
            if count == x:
                break
        except TypeError:
            pass
    if count != 0:
        print()
    return count
