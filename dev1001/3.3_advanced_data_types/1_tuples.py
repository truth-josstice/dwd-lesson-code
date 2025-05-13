# Tuples
#
# A tuple is an **ordered**, **indexed** collection of values.
# Key characteristic: **Immutable** - once created, you cannot change their contents.
# Syntax: Uses parentheses `()`.
# Use cases: Representing fixed collections (coordinates, RGB values),
#            data integrity, sometimes faster than lists, usable as
#            dictionary keys (we'll see why later).

# Creating tuples
point = (10, 20)
rgb_color = (255, 0, 128, "Medium Magenta") # Can mix types
single_item_tuple = (99,) # Note the trailing comma! Important!
empty_tuple = ()

print(f"Point: {point}")
print(f"Color: {rgb_color}")

# Accessing elements (Zero-indexed)
print(f"X-coordinate: {point[0]}")
print(f"Blue value: {rgb_color[2]}")

# Common functions/methods
print(f"Number of items in color tuple: {len(rgb_color)}")
print(f"How many times 0 appears: {rgb_color.count(0)}")
print(f"Index of 'Medium Magenta': {rgb_color.index('Medium Magenta')}")

# Tuple Unpacking
r, g, b, name = rgb_color
print(f"Unpacked Red: {r}, Green: {g}, Blue: {b}, Name: {name}")

# --- MODIFY ---

point = (10, 20)
# Trying to change an element -> Causes TypeError!
# point[0] = 15 # This line will raise an error - uncomment to see

print(f"Original point: {point}")

# 'Modifying' often means creating a *new* tuple
# new_point = point + (30,) # Concatenation creates a new tupleclear 
# new_point = (15, point[1]) # Creates new tuple using previous tuple values
new_point = (*point, 30) # Same result using * to unpack point
print(f"New point (original unchanged): {new_point}")

# Slicing also creates new tuples
# Syntax: tuple_var[start_index:end_index]
#           start_index is inclusive, end_index is exclusive.
first_two_color_values = rgb_color[0:2]
print(f"First two color values: {first_two_color_values}")