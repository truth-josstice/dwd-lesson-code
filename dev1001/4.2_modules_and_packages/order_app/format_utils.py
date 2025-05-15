# format_utils.py
def format_currency(amount):
    """Formats a number as currency (e.g., $10.50)."""
    return f"${amount:.2f}"

def generate_order_summary(order_id, customer_name, items_prices, grand_total):
    """Generates a string summary of the order."""
    item_list_str = ", ".join([format_currency(p) for p in items_prices])
    return (
        f"Order ID: {order_id}\n"
        f"Customer: {customer_name}\n"
        f"Items: {item_list_str}\n"
        f"Total: {format_currency(grand_total)}"
    )
