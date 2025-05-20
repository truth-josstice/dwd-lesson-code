# Callbacks Exercise
#
# 1. Write a function: perform_operation(a, b, math_callback).
# 2. This function should take two numbers and a callback.
# 3. The callback function itself should accept two numbers and return their result
#       (e.g., sum, product).
# 4. perform_operation() should then print this result.
# 5. Create two simple callbacks (e.g., add_them, multiply_them) and
#       test perform_operation with both.

def add_numbers(a, b): 
    return a + b
def multiply_numbers(a, b): 
    return a * b
def divide_numbers(a, b):
    return a / b
def subtract_numbers(a, b):
    return a - b
def square_numbers(a, b):
    my_list = [(a ** 2), (b ** 2)]
    return my_list
def cube_numbers(a, b):
    my_list = [(a ** 3), (b ** 3)]
    return my_list

def perform_operation(a, b, math_callback):
    answer = math_callback(a, b)
    print(f"Result: {answer}")


perform_operation(2, 378, add_numbers)
perform_operation(73, 48, multiply_numbers)
perform_operation(4, 20000, divide_numbers)
perform_operation(597, 599, subtract_numbers)
perform_operation(7, 12, square_numbers)
perform_operation(4, 9, cube_numbers)