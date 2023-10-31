#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    classification = "positive"
elif number == 0:
    classification = "zero"
else:
    classification = "negative"

print("{:d} is {}".format(number, classification))
