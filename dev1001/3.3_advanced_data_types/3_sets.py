# Sets
#
# Sets are collections of **unique** items, and they are **unordered**
#   (you can't rely on index positions)."
# Key characteristics: **Mutable**, **Unordered**, **Unique Elements**.
# Syntax: Uses curly braces `{}` like dictionaries, but *only* values.
#         An empty set must be created using `set()`.
# Use cases: Removing duplicates, fast membership testing,
#            mathematical set operations (union, intersection).

# Creating sets
numbers = {1, 2, 3, 2, 4, 1} # Duplicates are automatically removed
print(f"Numbers set: {numbers}")


letters = set("hello world") # Creates a set from a string (unique letters)
print(f"Unique letters: {letters}")

empty_set = set() # Correct way to make an empty set
# wrong_empty_set = {} # This creates an empty DICTIONARY!

# Membership testing (very fast!)
print(f"Is 3 in numbers? {3 in numbers}")
print(f"Is 'z' in letters? {'z' in letters}")

# Common functions
print(f"Number of unique letters: {len(letters)}")

# Note: No indexing! letters[0] -> TypeError
# print(letters[0])


# --- MODIFY ---

print(f"Original numbers set: {numbers}")

# Add an element
numbers.add(5)
print(f"Added 5: {numbers}")
numbers.add(3) # Adding existing element does nothing
print(f"Tried adding 3 again: {numbers}")

# Remove elements
numbers.remove(1) # Removes 1, raises KeyError if not found
print(f"Removed 1: {numbers}")
numbers.discard(10) # Removes 10 if present, does nothing otherwise (no error)
print(f"Discarded 10 (wasn't there): {numbers}")
popped_item = numbers.pop() # Removes and returns an *arbitrary* element
print(f"Popped '{popped_item}', set is now: {numbers}")

# Set Operations (Union, Intersection, Difference)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Union (A | B): {set_a | set_b} or {set_a.union(set_b)}")
print(f"Intersection (A & B): {set_a & set_b} or {set_a.intersection(set_b)}")
print(f"Difference (A - B): {set_a - set_b} or {set_a.difference(set_b)}")
print(f"Difference (B - A): {set_b - set_a}")
print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}") # Items in A or B, but not both
