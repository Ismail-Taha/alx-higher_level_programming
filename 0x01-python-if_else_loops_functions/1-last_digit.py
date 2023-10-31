#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_numb = abs(number) % 10
if number < 0:
    last_numb = -last_numb
print("Last digit of {} is {} and ".format(number, last_numb), end='')
if last_numb > 5:
    print('is greater than 5')
elif last_numb == 0:
    print('is 0')
else:
    print("is less than 6 and not 0")
