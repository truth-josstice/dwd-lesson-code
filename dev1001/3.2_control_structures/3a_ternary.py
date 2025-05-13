# --- USE: Ternary Operator ---
age = 22
# category = "Adult" if age >= 18 else "Minor" # The ternary operator

if age >= 18:
    category = "Adult"
else:
    catergory = "Minor"

print(f"Age: {age}, Category: {category}")



#Ternary (3a): Rewrite the ternary assignment for category using a traditional if-else block to demonstrate equivalence. Then, change the condition in the ternary operator: if age < 13, category is "Child", else it's "Teen or Adult".