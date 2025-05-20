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
"""

# --- Provided Book class (Parent) ---
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        # Modified slightly to avoid double printing when LibraryBook calls super().__init__
        # print(f"Book '{self.title}' by {self.author} created.")

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

# --- Your LibraryBook class definition goes here (Child) ---
class LibraryBook(Book):
    def __init__(self, title, author, pages, shelf_location, is_checked_out=False):
        super().__init__(title, author, pages) # Call parent constructor
        self.shelf_location = shelf_location
        self.is_checked_out = is_checked_out
        print(f"LibraryBook '{self.title}' created, located at {self.shelf_location}.")


    def check_out(self):
        if self.is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")

    def return_book(self):
        if not self.is_checked_out:
            print(f"'{self.title}' was not checked out (already in library).")
        else:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned.")

    def display_info(self):
        super().display_info() # Call parent's display_info method
        print(f"Shelf Location: {self.shelf_location}")
        status = "Checked Out" if self.is_checked_out else "Available"
        print(f"Status: {status}")


# --- Test your LibraryBook class here ---
print("\n--- Testing LibraryBook Class ---")
book1 = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", 180, "FIC-FITZ-01")
book2 = LibraryBook("1984", "George Orwell", 328, "DYS-ORW-01", is_checked_out=True) # Start as checked out
print("-" * 20)

book1.display_info()
print("-" * 10)
book2.display_info()
print("-" * 20)

# Test book1 checkout process
print("Testing book1 checkout:")
book1.check_out()       # Should check out
book1.check_out()       # Should say already checked out
book1.display_info()
print("-" * 20)

# Test book2 return process
print("Testing book2 return:")
book2.return_book()     # Should return
book2.return_book()     # Should say was not checked out
book2.display_info()
print("-" * 20)

# Further tests for book1
print("Further tests for book1:")
book1.return_book()     # Should return
book1.display_info()
print("-" * 20)

# Further tests for book2
print("Further tests for book2:")
book2.check_out()       # Should check out
book2.display_info()
print("-" * 20)

# Test a book that starts with default is_checked_out=False
book3 = LibraryBook("Brave New World", "Aldous Huxley", 311, "DYS-HUX-01")
book3.display_info()
book3.return_book() # Try returning a book not checked out
book3.check_out()
book3.display_info()
