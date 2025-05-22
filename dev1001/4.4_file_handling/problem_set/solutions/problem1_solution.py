FAVORITES_FILE = "favorites.txt"

def write_favorites(my_favorite_things):
    """
    Writes each item in the my_favorite_things list to FAVORITES_FILE,
    one item per line. This will overwrite the file if it already exists.
    """
    # TODO 1: Open FAVORITES_FILE in 'write' mode ('w').
    with open(FAVORITES_FILE, 'w') as f:
        # Inside the 'with' block, loop through the my_favorite_things list.
        for item in my_favorite_things:
            # For each item, write it to the file followed by a newline character ('\n').
            f.write(item + "\n")
    
    print(f"Your favorite things have been written to {FAVORITES_FILE}")


def read_and_print_favorites():
    """
    Reads FAVORITES_FILE and prints each line.
    Each printed line should be prefixed with "I like: ".
    """
    print("\n--- Reading Your Favorites ---")
    # TODO 2: Open FAVORITES_FILE in 'read' mode ('r').
    with open(FAVORITES_FILE, 'r') as f:
        # Inside the 'with' block, loop through each line in the file.
        for line in f:
            # For each line, print "I like: " followed by the line (you might want to .strip() it).
            print(f"I like: {line.strip()}")
    

# --- Test your functions ---
if __name__ == "__main__":
    favorite_items = ["Coding in Python", "Reading Sci-Fi Novels", "Hiking in the Mountains", "Drinking Coffee"]
    
    write_favorites(favorite_items)
    read_and_print_favorites()
