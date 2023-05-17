#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = []
    u_add = 0
    for x in my_list:
        if x in uniq:
            continue
        u_add += x
        uniq.append(x)
    return u_add
