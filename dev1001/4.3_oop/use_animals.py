# use_animals.py

'''
--- MODIFY TASKS ---

1. Create a new class LoudDog that inherits from Animal.

2. Its __init__ should take name and bark_volume (e.g., "loud", "very loud"). Call super().__init__(name) and store bark_volume.

3. Override the speak method for LoudDog to print a bark that includes its bark_volume.

4. Add a new method fetch(self, item) that prints a message about fetching.

5. Create instances of LoudDog and test the methods.
'''

class Animal:
    def __init__(self, name):
        print(f"Animal '{name}' created.")
        self.name = name

    def speak(self):
        # Generic sound
        print(f"{self.name} makes a sound.")

    def eat(self):
        print(f"{self.name} is eating.")

# Cat inherits from Animal
class Cat(Animal):
    def __init__(self, name, fur_color):
        # Call the parent class's __init__ method
        super().__init__(name)
        self.fur_color = fur_color # Cat-specific attribute
        print(f"It's a cat with {self.fur_color} fur!")

    # Overriding the parent's speak method
    def speak(self):
        print(f"{self.name} (the cat) says: Meow!")

    # Cat-specific method
    def purr(self):
        print(f"{self.name} purrs contentedly.")

# --- Let's USE the Animal and Cat classes ---
print("--- Creating and Using Animal and Cat Objects ---")
generic_animal = Animal("Creature")
generic_animal.eat()
generic_animal.speak()

print("-" * 10)

my_cat = Cat("Whiskers", "tabby")
my_cat.eat()      # Inherited from Animal
my_cat.speak()    # Overridden in Cat
my_cat.purr()     # Specific to Cat
print(f"{my_cat.name} has {my_cat.fur_color} fur.")
