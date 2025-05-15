# Modify

## Dictionaries

*   **Tasks:**
    1.  **New Product & Sale:**
        *   A new product "webcam" arrives with a stock of 25 units. Add it to the inventory.
        *   A customer buys 3 "usb_c_hub". Update its quantity. What happens if they try to buy more than available? (Don't implement the check yet, just note the potential issue).
    2.  **Price Check:**
        *   Create a *separate* dictionary called `product_prices` storing prices for at least "laptop_stand" ($25), "usb_c_hub" ($30), and "ergonomic_keyboard" ($75).
        *   A customer asks for the price of "laptop_stand". Print its price.
        *   What if they ask for the price of "webcam" which isn't in `product_prices` yet? Use `.get()` to print "Price not available" if it's not found.
    3.  **Stock Alert:**
        *   For the "laptop_stand" in the `inventory`, check if its quantity is below 15. If it is, print a message like "Alert: Low stock for laptop_stand! Current quantity: [quantity]".

---

## Loops

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
