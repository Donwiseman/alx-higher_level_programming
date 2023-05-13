#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
    else:
        print(f"{argc - 1} argument:")
        for index, value in enumerate(sys.argv):
            if index == 0:
                continue
            print(f"{index}: {value}")
