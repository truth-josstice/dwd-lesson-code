'''
Problem 1: My Favorite Things (Text Files)

Objective: Practice writing to (creating/overwriting) and reading from basic text files.

Description:
1. Writes a list of your favorite things (e.g., hobbies, foods, books) to a file named favorites.txt. Each item should be on a new line.
2. Reads the favorites.txt file and prints each item to the console, prefixed with "I like: ".
'''

FAVORITES_FILE = "favorites.txt"

def write_favorites(my_favorite_things):
    """
    Writes each item in the my_favorite_things list to FAVORITES_FILE,
    one item per line. This will overwrite the file if it already exists.
    """
    # TODO 1: Open FAVORITES_FILE in 'write' mode ('w').
    # Use a 'with' statement.
    # Inside the 'with' block, loop through the my_favorite_things list.
    # For each item, write it to the file followed by a newline character ('\n').
    
    print(f"Your favorite things have been written to {FAVORITES_FILE}")


def read_and_print_favorites():
    """
    Reads FAVORITES_FILE and prints each line.
    Each printed line should be prefixed with "I like: ".
    """
    print("\n--- Reading Your Favorites ---")
    # TODO 2: Open FAVORITES_FILE in 'read' mode ('r').
    # Use a 'with' statement.
    # Inside the 'with' block, loop through each line in the file.
    # For each line, print "I like: " followed by the line (you might want to .strip() it).
    

# --- Test your functions ---
if __name__ == "__main__":
    favorite_items = ["Coding in Python", "Reading Sci-Fi Novels", "Hiking in the Mountains", "Drinking Coffee"]
    
    write_favorites(favorite_items)
    read_and_print_favorites()

    # Expected output (after running the script):
    # Your favorite things have been written to favorites.txt
    #
    # --- Reading Your Favorites ---
    # I like: Coding in Python
    # I like: Reading Sci-Fi Novels
    # I like: Hiking in the Mountains
    # I like: Drinking Coffee
