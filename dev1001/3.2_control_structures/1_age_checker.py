# --- USE: Age Checker ---
user_age = 20 # Try changing this to 15, 18
required_age = 21
can_proceed = False

print(f"User's age: {user_age}, Required age: {required_age}")

if user_age >= required_age:
    print("Access granted. You meet the age requirement.")
    can_proceed = True
else:
    print("Access denied. You do not meet the age requirement.")
    print("Please try again when you're older")
    can_proceed = False

print(f"Can proceed with activity? {can_proceed}")

