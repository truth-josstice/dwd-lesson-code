import order_utils
import format_utils # Using 'import module_name'

# Alternative: from order_utils import calculate_grand_total, calculate_subtotal
# from format_utils import generate_order_summary

customer_order_1 = {
    "id": "ORD123",
    "customer": "Alice Wonderland",
    "items": [10.00, 25.50, 5.75] # list of prices
}

# Process order 1
subtotal1 = order_utils.calculate_subtotal(customer_order_1["items"])
# If using 'from x import y':
# subtotal1 = calculate_subtotal(customer_order_1["items"])

grand_total1 = order_utils.calculate_grand_total(subtotal1)
summary1 = format_utils.generate_order_summary(
    customer_order_1["id"],
    customer_order_1["customer"],
    customer_order_1["items"],
    grand_total1
)
print("--- Order 1 ---")
print(summary1)
print(f"Default Tax Rate from module: {order_utils.TAX_RATE}")
