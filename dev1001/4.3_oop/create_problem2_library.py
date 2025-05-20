# create_problem2_library.py

"""
Problem 2: Library Book System (Inheritance)

You are expanding a library management system.
You already have a basic `Book` class (provided below).
Your task is to create a `LibraryBook` class that *inherits* from `Book`.

The existing `Book` class:
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(f"Book '{self.title}' by {self.author} created.")

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

1.  Create the `LibraryBook` class which inherits from `Book`.

2.  The `__init__` method for `LibraryBook` should accept:
    *   `title` (string)
    *   `author` (string)
    *   `pages` (integer)
    *   `shelf_location` (string, e.g., "A102", "Fiction-3B")
    *   `is_checked_out` (boolean, defaults to `False`)
    It should call the parent's `__init__` method for title, author, and pages,
    and then store `shelf_location` and `is_checked_out` as instance variables.

3.  Add a method `check_out(self)` to `LibraryBook`:
    *   If the book is already checked out, print a message like
        "'The Great Gatsby' is already checked out."
    *   Otherwise, set `is_checked_out` to `True` and print
        "'The Great Gatsby' has been checked out."

4.  Add a method `return_book(self)` to `LibraryBook`:
    *   If the book is not checked out (i.e., it's already in the library),
        print a message like "'The Great Gatsby' was not checked out."
    *   Otherwise, set `is_checked_out` to `False` and print
        "'The Great Gatsby' has been returned."

5.  Override the `display_info(self)` method from the `Book` class.
    The new `display_info` in `LibraryBook` should first call the parent's
    `display_info` method (using `super()`) and then also print the
    `shelf_location` and the current checkout status (e.g., "Status: Available"
    or "Status: Checked Out").

Instructions:
- Define the `Book` class as provided.
- Fill in the `LibraryBook` class structure below, making sure it inherits from `Book`.
- After defining the classes, create at least two `LibraryBook` objects.
- Call all the methods on your `LibraryBook` objects to test them, including
  checking out, trying to check out again, returning, and trying to return again.
- Call `display_info()` at various stages to see the status changes.

Example Usage (you can uncomment and adapt this after defining your class):
# book1 = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 180, "FIC-FITZ-01", False)
# book2 = LibraryBook("1984", "George Orwell", 328, "DYS-ORW-01") # is_checked_out defaults to False

# book1.display_info()
# book2.display_info()
# print("-" * 20)

# book1.check_out()
# book1.check_out() # Try checking out again
# book1.display_info()
# print("-" * 20)

# book2.return_book() # Try returning a book not checked out
# book2.check_out()
# book2.display_info()
# print("-" * 20)

# book1.return_book()
# book1.display_info()
"""

# --- Provided Book class (Parent) ---
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(f"Book '{self.title}' by {self.author} created.")

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

# --- Your LibraryBook class definition goes here (Child) ---
# TODO: Define the LibraryBook class, inheriting from Book
class LibraryBook(Book): # Example of inheritance
    # TODO: Implement __init__, check_out, return_book, and override display_info
    pass


# --- Test your LibraryBook class here ---
# print("\n--- Testing LibraryBook Class ---")
# (Create objects and call methods as per instructions)
