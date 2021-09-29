#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modnum = number % 10 if number > 0 else number % -10
if modnum > 5:
            print("Last digit of {} is {} and is greater than 5".format(
                            number, modnum))
elif modnum == 0:
            print("Last digit of {} is {} and is 0".format(
                            number, modnum))
else:
            print("Last digit of {} is {} and is less than 6 and not 0".format(
                            number, modnum))
