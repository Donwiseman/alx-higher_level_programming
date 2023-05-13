#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        print(0)
    else:
        sum = 0
        for index, value in enumerate(sys.argv):
            if index == 0:
                continue
            sum += (int(value))
        print(sum)
