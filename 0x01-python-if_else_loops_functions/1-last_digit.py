#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    rem = (number % 10) - 10
    if rem == -10:
        rem = 0
else:
    rem = number % 10
print(f"Last digit of {number} is {rem} and is ", end="")
if rem > 5:
    print("greater than 5")
elif rem == 0:
    print("0")
elif rem < 6 and not 0:
    print("less than 6 and not 0")
