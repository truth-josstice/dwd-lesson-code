# dog.py

'''
--- MODIFY TASKS ---

1. Add a new instance variable age to our Dog.

2. Add a new method 'celebrate_birthday' that increases the dog's age by 1 and prints a message.
'''

class Dog: # Pascal case
    # This is the constructor method
    def __init__(self, name_param, breed_param, age_param):
        print(f"A new dog named {name_param} is being created!")
        self.name = name_param  # Instance variable
        self.breed = breed_param # Instance variable
        self.age = age_param # Instance variable

    # This is a method
    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is a {self.breed}. They are {self.age} years old.")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! You have turned {self.age} years old today!")

# --- Let's USE the Dog class ---
print("--- Creating and Using Dog Objects ---")
# Create an object (instance) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever", 13)

# Create another object
dog2 = Dog("Lucy", "Poodle", 7)
dog3 = Dog("Scooby-Doo", "Talking Dog", 999)

# Call methods on the objects
dog1.describe()
dog1.bark()
dog1.celebrate_birthday()

print("-" * 10) # Separator

dog2.describe()
dog2.bark()
dog2.celebrate_birthday()

print("-" * 10) # Separator

dog3.describe()
dog3.bark()
dog3.celebrate_birthday()

print("\n--- Accessing Instance Variables (generally done via methods) ---")
print(f"Dog 1's name is: {dog1.name}.")
print(f"Dog 2's breed is: {dog2.breed}.")
print(f'Dog 3 is {dog3.age} years old.')
