**CREATE Phase: Challenge Problem**

**Problem 3: Automated Cafe Order Summary**

**Scenario:**
You're building a system for a local cafe to quickly generate an order summary and calculate the total cost, including potential customizations and discounts.

**Task:**
Write a Python script that defines and uses several functions to achieve this.

**Data/Menu (You can hardcode this within your script or functions):**
*   **Coffee:**
    *   Small: $3.00
    *   Medium: $3.50 (default size if not specified)
    *   Large: $4.00
*   **Tea:**
    *   Regular: $2.50
    *   Herbal: $2.75
*   **Pastry:**
    *   Croissant: $3.25
    *   Muffin: $3.00
*   **Extras/Surcharges:**
    *   Soy Milk: +$0.50 (for coffee/tea)
    *   Almond Milk: +$0.75 (for coffee/tea)
    *   Extra Coffee Shot: +$1.00
*   **Discount:**
    *   Loyalty Members: 10% off the total order before GST.
    *   GST (Goods and Services Tax): 10% added to the final discounted price. (Typical in Australia)

**Functions to Create:**

1.  **`calculate_item_price(item_name, quantity, **options)`**
    *   **Parameters:**
        *   `item_name` (string, positional): e.g., "coffee", "tea", "croissant".
        *   `quantity` (int, positional): How many of this item.
        *   `**options` (keyword arguments): This will allow you to pass various options specific to the item. Examples:
            *   For "coffee": `size="large"`, `milk="soy"`, `extra_shot=True`
            *   For "tea": `type="herbal"`, `milk="almond"`
    *   **Logic:**
        *   Determine the base price of the `item_name`.
        *   Adjust the price based on `options` provided (e.g., coffee size, milk type, extra shot).
        *   Calculate the total price for this item line (base price + option surcharges) * quantity.
    *   **Returns:** The calculated price for that specific item line (float).
    *   **Hint:** You'll likely use `if/elif/else` or `match/case` within this function to handle different items and their options. You might find a dictionary useful for base prices.

2.  **`apply_discount_and_gst(subtotal, is_loyalty_member=False, loyalty_discount_rate=0.10, gst_rate=0.10)`**
    *   **Parameters:**
        *   `subtotal` (float, positional): The total cost of all items before any discounts or GST.
        *   `is_loyalty_member` (bool, keyword, default `False`): True if the customer is a loyalty member.
        *   `loyalty_discount_rate` (float, keyword, default `0.10`): The discount rate for loyalty members (e.g., 0.10 for 10%).
        *   `gst_rate` (float, keyword, default `0.10`): The GST rate (e.g., 0.10 for 10%).
    *   **Logic:**
        *   If `is_loyalty_member` is True, apply the `loyalty_discount_rate` to the `subtotal`.
        *   Calculate the GST amount on the (potentially discounted) subtotal.
        *   Calculate the final total (subtotal after discount + GST).
    *   **Returns:** A tuple containing three values: `(discounted_subtotal, gst_amount, final_total)`.

3.  **`generate_order_receipt(customer_name, order_items, is_loyalty_member=False)`**
    *   **Parameters:**
        *   `customer_name` (string, positional): The name of the customer.
        *   `order_items` (list of tuples, positional): A list where each tuple represents an item in the order. Each inner tuple should be structured as: `(item_name, quantity, options_dict)`.
            *   Example: `[("coffee", 2, {"size": "large", "milk": "soy"}), ("muffin", 1, {})]`
            *   The `options_dict` is what you will pass as `**options` to `calculate_item_price`. An empty dictionary `{}` means no special options.
        *   `is_loyalty_member` (bool, keyword, default `False`): Passed through to `apply_discount_and_gst`.
    *   **Logic:**
        *   Initialize an empty list to store formatted item lines for the receipt and a `current_subtotal = 0.0`.
        *   Iterate through `order_items`:
            *   For each item, call `calculate_item_price()` using the item name, quantity, and unpacking the `options_dict` (e.g., `calculate_item_price(name, qty, **opts_dict)`).
            *   Add the returned price to `current_subtotal`.
            *   Create a formatted string for this item line (e.g., "2 x Large Soy Coffee: $9.50") and add it to your list of item lines.
        *   Once all items are processed, call `apply_discount_and_gst()` with the `current_subtotal` and `is_loyalty_member` status.
        *   Construct a multi-line string for the receipt. It should include:
            *   Customer Name
            *   Each item line (from your list)
            *   Subtotal (before discount/GST)
            *   Discount applied (if any)
            *   Subtotal after discount
            *   GST Amount
            *   Grand Total
    *   **Returns:** The formatted multi-line receipt string.

**Main Script / How to Test:**

*   Define your menu data (perhaps as dictionaries).
*   Create a few sample `order_items` lists representing different customer orders.
*   For each sample order:
    *   Call `generate_order_receipt()` with the customer's name, their `order_items` list, and their loyalty status.
    *   Print the returned receipt string.

**Example `order_items` structure:**
```python
order1_items = [
    ("coffee", 1, {"size": "medium", "milk": "dairy"}), # 1 Medium Dairy Coffee
    ("croissant", 2, {})                                # 2 Croissants
]
order2_items = [
    ("tea", 1, {"type": "herbal", "milk": "almond"}),    # 1 Herbal Almond Tea
    ("coffee", 1, {"size": "large", "extra_shot": True}) # 1 Large Coffee with extra shot
]
```

**Example Output Snippet (for one order):**
```
--- Order for Alice ---
1 x Medium Dairy Coffee: $3.50
2 x Croissant: $6.50
-------------------------
Subtotal: $10.00
Loyalty Discount (10%): -$1.00
Subtotal After Discount: $9.00
GST (10%): +$0.90
-------------------------
GRAND TOTAL: $9.90
=========================
```

**Tips:**
*   Break the problem down. Implement and test each function one by one.
*   Start with `calculate_item_price` and test it with various inputs before moving on.
*   Use f-strings for formatting output neatly.
*   Don't be afraid to use helper variables within your functions.
