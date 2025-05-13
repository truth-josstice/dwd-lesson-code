# Lists
#
# Like tuples, lists are also ordered sequences, but the key difference is
# they are **Mutable** - you *can* change them after creation.
# Syntax: Uses square brackets: []
# Use cases: Storing collections where items might be added, removed, or changed
#               (e.g., a list of tasks, scores, user names).

# Creating lists
shopping_list = ["apples", "bananas", "milk"]
scores = [88, 92, 75, 100]
mixed_list = [1, "hello", True, 3.14]
empty_list = []

print(f"Shopping List: {shopping_list}")

# Accessing elements (Zero-indexed) and Slicing
print(f"First item: {shopping_list[0]}")
print(f"Last item: {shopping_list[-1]}") # Negative indexing
print(f"First two scores: {scores[0:2]}")

# Common functions
print(f"Number of scores: {len(scores)}")
print(f"'milk' in shopping list? {'milk' in shopping_list}") # Membership test


"""
# --- MODIFY ---

print(f"Original shopping list: {shopping_list}")

# Change an item
shopping_list[1] = "blueberries"
print(f"Changed item: {shopping_list}")

# Add items
shopping_list.append("bread") # Adds to the end
print(f"Appended: {shopping_list}")
shopping_list.insert(1, "yogurt") # Inserts at index 1
print(f"Inserted: {shopping_list}")

# Remove items
removed_item = shopping_list.pop() # Removes and returns the last item
print(f"Popped '{removed_item}', list is now: {shopping_list}")
shopping_list.remove("apples") # Removes the first occurrence of 'apples'
print(f"Removed 'apples': {shopping_list}")

# Extending with another list
more_items = ["eggs", "cheese"]
shopping_list.extend(more_items) # Adds elements from another iterable
# Alternative: shopping_list = shopping_list + more_items (creates new list)
print(f"Extended: {shopping_list}")

# Sorting (in-place)
scores.sort()
print(f"Sorted scores: {scores}")
scores.sort(reverse=True)
print(f"Reverse sorted scores: {scores}")
"""
