# create_problem1_product.py

"""
Problem 1: E-commerce Product

You are building a system for an e-commerce website.
Create a class called `Product`.

1.  The `__init__` method should accept:
    *   `name` (string)
    *   `price` (float)
    *   `quantity_in_stock` (integer)
    It should store these as instance variables.

2.  Add a method `display_product_info(self)` that prints the product's name,
    price, and quantity in stock in a user-friendly format.
    Example: "Product: Laptop, Price: $999.99, Stock: 50"

3.  Add a method `update_stock(self, new_quantity)` that updates the
    `quantity_in_stock` to the `new_quantity` provided.
    It should also print a message like "Stock for Laptop updated to 45 units."

4.  Add a method `calculate_total_value(self)` that returns the total value
    of this product currently in stock (price * quantity_in_stock).

Instructions:
- Fill in the `Product` class structure below.
- After defining the class, create at least two `Product` objects.
- Call all the methods on your objects to test them.
- Print the value returned by `calculate_total_value`.

Example Usage (you can uncomment and adapt this after defining your class):
# item1 = Product("Laptop", 999.99, 50)
# item2 = Product("Mouse", 25.50, 200)

# item1.display_product_info()
# item2.display_product_info()

# item1.update_stock(45)
# item1.display_product_info()

# total_value_item1 = item1.calculate_total_value()
# print(f"Total stock value for {item1.name}: ${total_value_item1:.2f}")

# total_value_item2 = item2.calculate_total_value()
# print(f"Total stock value for {item2.name}: ${total_value_item2:.2f}")
"""

# --- Your Product class definition goes here ---
class Product:
    # TODO: Implement the __init__ method
    pass

    # TODO: Implement the display_product_info method
    pass

    # TODO: Implement the update_stock method
    pass

    # TODO: Implement the calculate_total_value method
    pass


# --- Test your Product class here ---
# print("--- Testing Product Class ---")
# (Create objects and call methods as per instructions)
