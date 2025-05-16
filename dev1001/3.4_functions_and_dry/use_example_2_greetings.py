# --- use_example_2_greetings.py ---

def generate_welcome_message(username, portal_name, login_attempts=1):
    """
    Generates a personalized welcome message.
    - username: The user's name (string, positional)
    - portal_name: The name of the portal (string, positional)
    - login_attempts: Number of times user tried to log in (int, optional/default)
    """
    message = f"Welcome, {username}, to the {portal_name} portal!"
    if login_attempts > 1:
        message += f" We noticed you had {login_attempts} login attempts. If this wasn't you, please secure your account."
    else:
        message += " Enjoy your session!"
    return message

# --- Main part of our script ---
# 1. Using positional arguments
user1_msg = generate_welcome_message("AliceWonder", "UniLibrary System")
print(f"User 1: {user1_msg}")

# 2. Using keyword arguments (order doesn't matter)
user2_msg = generate_welcome_message(portal_name="StudentHub", username="BobBuilder")
print(f"User 2: {user2_msg}")

# 3. Using a mix, and overriding the default parameter
user3_msg = generate_welcome_message("CharlieChap", "Course Enrolment", login_attempts=3)
print(f"User 3: {user3_msg}")

# 4. Using positional and letting default parameter apply
user4_msg = generate_welcome_message("DianaPrince", "MyUni Dashboard")
print(f"User 4: {user4_msg}") # login_attempts will be 1
