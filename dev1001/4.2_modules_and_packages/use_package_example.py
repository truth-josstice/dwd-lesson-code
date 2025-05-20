# use_package_example.py
# Before running:
# 1. Create and activate a virtual environment.
# 2. In your activated venv, run: pip install pyjokes
# 3. Then run this script: python use_package_example.py

import pyjokes

# Get a random joke
joke = pyjokes.get_joke()
print("Here's a random joke for you:")
print(joke)

# You can also try to get a joke in a specific language or category if supported
# For pyjokes, it primarily offers English jokes, but some categories exist.
# joke_neutral = pyjokes.get_joke(language='en', category='neutral')
# print("\nHere's a neutral joke:")
# print(joke_neutral)

# joke_chuck = pyjokes.get_joke(language='en', category='chuck')
# print("\nHere's a Chuck Norris joke:")
# print(joke_chuck)