#!/usr/bin/python3
def pow(a, b):
    num = 1
    if b == 0:
        return 1
    if b < 0:
        for x in range((b * -1)):
            num *= a
        num = 1/num
    else:
        for x in range(b):
            num *= a
    return num
