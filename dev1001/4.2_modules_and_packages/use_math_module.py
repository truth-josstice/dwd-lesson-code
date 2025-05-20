# use_math_module.py
import math

# Using the math module for mathematical operations

# Calculate the square root of a number
number = 16
square_root = math.sqrt(number)
print(f"The square root of {number} is: {square_root}")

# Using the constant pi
radius = 5
area = math.pi * (radius ** 2)
print(f"The area of a circle with radius {radius} is: {area:.2f}")

# Another way to import (less common for standard libraries like math)
from math import pow, factorial
print(f"2 to the power of 3 is: {pow(2, 3)}")
print(f"Factorial of 5 is: {factorial(5)}")