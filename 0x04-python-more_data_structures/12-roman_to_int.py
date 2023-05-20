#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer"""
    r_d = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    num = 0

    if type(roman_string) != str:
        return 0
    size = len(roman_string)
    for index, value in enumerate(roman_string):
        if (index + 1) < size and r_d[value] < r_d[(roman_string[index + 1])]:
            num += r_d[value] * -1
        else:
            num += r_d[value]
    return num
