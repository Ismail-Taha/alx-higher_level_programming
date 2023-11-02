#!/usr/bin/python3

# Import functions from calculator_1 module
from calculator_1 import add, sub, mul, div

# Define variables a and b
a = 10
b = 5

# Perform mathematical operations using the imported functions
addition = add(a, b)
substraction = sub(a, b)
multiplication = mul(a, b)
devision = div(a, b)

# Print the results with a single print statement for each
print(f"{a} + {b} = {addition}")
print(f"{a} - {b} = {substraction}")
print(f"{a} * {b} = {multiplication}")
print(f"{a} / {b} = {devision}")

