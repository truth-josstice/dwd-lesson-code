# --- USE: Loop Examples ---
print("--- LOOPS: USE PHASE ---")

# 1. `while` loop: Simple countdown
print("--- While Loop ---")
countdown = 3
while countdown > 0:
    print(f"T-minus {countdown}...")
    countdown -= 1 # Crucial: update the condition variable
print("Lift off!")
print("-" * 20)

# 2. `for...in range()`: Processing a fixed number of times
print("--- For...in range() Loop ---")
num_students = 4
for i in range(num_students):
    print(f"Processing data for student #{i + 1}") # i is 0-indexed
print("-" * 20)

# 3. `for...in iterable` (list): Processing items in a collection
print("--- For...in iterable (List) ---")
shopping_list = ["apples", "bananas", "milk", "bread"]
for item in shopping_list:
    print(f"Need to buy: {item.capitalize()}")
print("-" * 20)

# 4. `for...in iterable` (dictionary items): Accessing keys and values
# (Re-using product_prices from dictionary section for context)
product_prices = {"laptop_stand": 25, "usb_c_hub": 30, "ergonomic_keyboard": 75}
print("--- For...in iterable (Dictionary items) ---")
print("Product Pricelist:")
for product, price in product_prices.items():
    print(f"- {product.replace('_', ' ').title()}: ${price}")
print("-" * 20)

# 5. `enumerate()`: Getting item and its index
print("--- Enumerate Loop ---")
tasks_today = ["Reply to emails", "Attend meeting", "Code feature X"]
print("Today's Tasks:")
for index, task in enumerate(tasks_today):
    print(f"{index + 1}. {task}") # User-friendly 1-based indexing
print("-" * 30 + "\n")

# #while loop for a temperature 
current_temp = 18

while current_temp <= 22:
    print(f"Current temperature: {current_temp}")
    current_temp += 1

print(f"Current temperature: Optimal\n")

# #for odd numbers
for i in range(1, 10):
    if i % 2 != 0:
        print(i)
print()

#print order more message
inventory = {"laptop_stand": 12, "usb_c_hub": 32, "webcam": 8, "ergonomic_keyboard": 18}

for product, quantity in inventory.items():
    if quantity < 10:
        print(f"Order more {product.replace("_", " ").capitalize()}!")
    else:
        print(f"{product.replace("_", " ").capitalize()} stock is OK.")

'''
*   **Tasks:**
    1.  **`while` Loop Temperature Check:**
        *   Imagine a sensor reading. Start with `current_temp = 18`.
        *   Write a `while` loop that keeps printing "Temperature ({current_temp}°C) is cool, increasing..." and increments `current_temp` by 1, as long as `current_temp` is less than 22.
        *   Once it reaches 22 or more, print "Temperature ({current_temp}°C) is optimal."
    2.  **`for...in range()` Odd Numbers:**
        *   Print all odd numbers between 1 and 10 (inclusive) using a `for` loop with `range()`. (Hint: `range()` can take a step argument).
    3.  **`for...in iterable` (dictionary) with Conditional Logic:**
        *   Using the `inventory` dictionary from earlier:
            ```python
            inventory = {"laptop_stand": 12, "usb_c_hub": 32, "webcam": 8, "ergonomic_keyboard": 18}
            ```
        *   Iterate through the inventory. For each item, if its quantity is less than 10, print an "Order more [item_name]!" message. Otherwise, print "[item_name] stock is OK."
    4.  **`enumerate()` with a Twist:**
        *   Given `guest_list = ["Alice", "Bob", "Charlie", "Diana"]`.
        *   Use `enumerate` to print an invitation list like:
            *   "Invitation 1 for Alice"
            *   "Invitation 2 for Bob"
            *   ...etc.
'''