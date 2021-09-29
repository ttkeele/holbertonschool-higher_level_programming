#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
zero = "0"
great5 = "greater than 5"
less6 = "less than 6 and not 0"
if number > 0:
        last = number % 10
else:
        last = number % -10
        if last > 5:
                print("Last digit of {} is {} and is {}".format(number, last, great5))
        elif last == 0:
                print("Last digit of {} is {} and is {}".format(number, last, zero))
        else:
                print("Last digit of {} is {} and is {}".format(number, last, less6))
