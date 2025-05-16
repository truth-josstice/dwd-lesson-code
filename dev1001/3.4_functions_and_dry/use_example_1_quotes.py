# --- use_example_1_quotes.py ---
import random # We'll need this for a random choice

def get_daily_thought():
    """Returns a randomly selected thought for the day."""
    thoughts = [
        "The only way to do great work is to love what you do.",
        "Strive not to be a success, but rather to be of value.",
        "The mind is everything. What you think you become.",
        "Your time is limited, so don't waste it living someone else's life.",
        "Believe you can and you're halfway there."
    ]
    chosen_thought = random.choice(thoughts)
    return chosen_thought

# --- Main part of our script ---
print("Welcome to your Daily Inspirer!")

thought_for_today = get_daily_thought() # Calling the function
print(f"Today's thought: {thought_for_today}")

another_thought = get_daily_thought() # Calling it again gives another (or same) random thought
print(f"Another thought: {another_thought}")

print("Have a great day!")
