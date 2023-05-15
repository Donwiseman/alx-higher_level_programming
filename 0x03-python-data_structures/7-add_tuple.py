#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_a) == 1:
        x, y = tuple_a[0], 0
    else:
        x, y = tuple_a
    if len(tuple_b) == 1:
        a, b = tuple_b[0], 0
    else:
        a, b = tuple_b
    return ((x + a), (y + b))
