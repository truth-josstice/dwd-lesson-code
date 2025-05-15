# order_utils.py
TAX_RATE = 0.07 # 7% sales tax

def calculate_subtotal(items_prices):
    """Calculates subtotal from a list of item prices."""
    return sum(items_prices)

def calculate_tax(subtotal_amount):
    """Calculates tax based on the subtotal."""
    return subtotal_amount * TAX_RATE

def calculate_grand_total(subtotal_amount):
    """Calculates grand total including tax."""
    tax = calculate_tax(subtotal_amount)
    return subtotal_amount + tax
