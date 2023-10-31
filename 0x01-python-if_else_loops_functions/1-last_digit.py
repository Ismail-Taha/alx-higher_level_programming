#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

classification = ""

if last_digit > 5:
    classification = "greater than 5"
elif last_digit == 0:
    classification = "0"
else:
    classification = "less than 6 and not 0"

print("Last digit of {} is {} and is {}.".format(number, last_digit, classification))
