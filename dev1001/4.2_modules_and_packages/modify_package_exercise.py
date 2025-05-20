"""
MODIFY Exercise: Using an External Package and Managing Dependencies

Background:
You've learned to install packages using pip into a virtual environment.
This exercise uses the 'pyjokes' package.

Tasks:
1.  Ensure you have a virtual environment. If not, create one (e.g., `python -m venv venv_jokes`)
    and activate it (e.g., `source venv_jokes/bin/activate` or `venv_jokes\Scripts\activate`).
2.  Install the `pyjokes` package if you haven't already: `pip install pyjokes`
3.  Import the `pyjokes` package in this script.
4.  Modify the script to:
    a. Get and print one joke of category 'neutral'.
    b. Get and print one joke of category 'chuck' (for Chuck Norris jokes).
    c. Get and print a list of 3 jokes using `pyjokes.get_jokes()`.
5.  After running your script successfully, update/create a `requirements.txt` file
    for your current project directory. It should contain `pyjokes` and its version.
    Command: `pip freeze > requirements.txt`
"""

# Task 3: Import pyjokes
# import pyjokes

# Task 4a: Get and print a neutral joke
# neutral_joke = ...
# print("Neutral Joke:")
# print(neutral_joke)

# Task 4b: Get and print a Chuck Norris joke
# chuck_joke = ...
# print("\nChuck Norris Joke:")
# print(chuck_joke)

# Task 4c: Get and print a list of 3 jokes
# list_of_jokes = ...
# print("\nList of 3 Jokes:")
# for i, joke_item in enumerate(list_of_jokes):
#    print(f"{i+1}. {joke_item}")

print("--- Modify Package Exercise Complete (Placeholder) ---")
# Expected output (jokes will vary):
# Neutral Joke:
# Why did the web developer break up with the graphic designer? They didn't see eye to eye on the UI.
#
# Chuck Norris Joke:
# Chuck Norris can skydive into a volcano.
#
# List of 3 Jokes:
# 1. Why was the JavaScript developer sad? Because he didn't Node how to Express himself.
# 2. Want to hear a joke about Python? Sorry, I'm not a ssssspeaker.
# 3. How many programmers does it take to change a lightbulb? None, that's a hardware problem.

# Task 5: After running, create/update requirements.txt in your terminal
# `pip freeze > requirements.txt`