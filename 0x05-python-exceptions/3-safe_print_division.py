#!/usr/bin/python3
def safe_print_division(a, b):
    num = None

    try:
        num = a / b
        return num
    except ZeroDivisionError:
        return num
    finally:
        print("Inside result: {}".format(num))
