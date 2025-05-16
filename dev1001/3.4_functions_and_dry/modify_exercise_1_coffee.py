# --- modify_exercise_1_coffee.py ---

# Inputs (already defined for you)
price_per_coffee = 3.50  # Price for one coffee
number_of_coffees = 8
service_fee_threshold = 5 # Orders above this many coffees incur a service fee
fixed_service_fee = 2.00

def calculate_bulk_coffee_order_total():
    """
    Calculates the total cost for a bulk coffee order.
    If the number of coffees is above the service_fee_threshold,
    a fixed_service_fee is added.
    This function uses the global variables defined above.
    """
    total_cost = 0.0
    # TODO 1: Calculate the base cost of all coffees (price_per_coffee * number_of_coffees)
    # TODO 2: Check if number_of_coffees is greater than service_fee_threshold
    # TODO 3: If it is, add the fixed_service_fee to the total_cost
    # TODO 4: Return the final total_cost

    # Remove the 'pass' statement below when you start coding
    pass

# --- Main part of the script (provided) ---
order_total = calculate_bulk_coffee_order_total()

# Outputs (already defined for you)
print(f"Number of coffees: {number_of_coffees}")
print(f"Price per coffee: ${price_per_coffee:.2f}")
if number_of_coffees > service_fee_threshold:
    print(f"Service fee applied: ${fixed_service_fee:.2f}")
else:
    print("No service fee applied.")
print(f"Total order cost: ${order_total:.2f}")
