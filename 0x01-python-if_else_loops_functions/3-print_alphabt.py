#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if ord('q') == i or ord('e') == i:
        continue
    print("{}".format(chr(i)), end="")
