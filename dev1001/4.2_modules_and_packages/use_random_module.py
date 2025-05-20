# use_random_module.py
import random

# Using the random module for generating random numbers and choices

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)
print(f"Random number between 1 and 10: {random_number}")

# Pick a random item from a list
choices = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(choices)
print(f"Randomly chosen fruit: {random_fruit}")

# Shuffle a list (in-place)
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")