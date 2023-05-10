#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        rem = ((number % 10) - 10) * -1
        if rem == 10:
            rem = 0
    else:
        rem = number % 10
    print(f"{rem}", end="")
    return rem
