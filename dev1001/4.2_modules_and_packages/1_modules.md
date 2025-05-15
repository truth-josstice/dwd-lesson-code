# Modules

## Modify

The e-commerce company now wants to offer a discount on orders over $50 before tax.

Your tasks:

1.  In `order_utils.py`, add a new function `apply_discount(subtotal, discount_threshold=50.0, discount_percentage=0.10)` that returns the discounted subtotal if `subtotal` is above `discount_threshold`.
2.  Modify `calculate_grand_total` in `order_utils.py` to first apply this discount to the subtotal *before* calculating tax.
3.  In `main_app.py`, create a `customer_order_2` with items that would qualify for the discount (e.g., `[30.00, 45.00]`) and print its summary.

---

## Create

Our e-commerce platform also needs to manage inventory.

Your tasks:

1.  Create a *new* module named `inventory_manager.py`.
2.  Inside `inventory_manager.py`, create a dictionary representing product stock (e.g., `product_stock = {"itemA": 10, "itemB": 5, "itemC": 0}`).
3.  Add a function `check_stock(product_id, quantity_needed)` to this module that returns `True` if enough stock exists, `False` otherwise.
4.  Add another function `update_stock(product_id, quantity_sold)` that reduces the stock for that product (ensure it doesn't go below zero).
5.  In `main_app.py` (or a new `inventory_test.py`), import your `inventory_manager` module.
6.  Demonstrate checking stock for "itemA" (e.g., 3 units), then "selling" 2 units of "itemA" (updating stock), and then checking stock again. Print the results.
