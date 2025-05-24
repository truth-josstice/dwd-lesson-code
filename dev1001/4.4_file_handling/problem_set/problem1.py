'''
Problem 1: My Favorite Things (Text Files)

Objective: Practice writing to (creating/overwriting) and reading from basic text files.

Description:
1. Writes a list of your favorite things (e.g., hobbies, foods, books) to a file named favorites.txt. Each item should be on a new line.
2. Reads the favorites.txt file and prints each item to the console, prefixed with "I like: ".
'''

FAVORITES_FILE = "favorites.txt"

def write_favorites(my_favorite_things):
    
    with open(FAVORITES_FILE, 'w') as f:
        my_list = []
        for x in my_favorite_things:
            my_list.append(x)
        f.write('\n'.join(my_list))
    
    
    print(f"Your favorite things have been written to {FAVORITES_FILE}")


def read_and_print_favorites():
    
    print("\n--- Reading Your Favorites ---")
    
    with open(FAVORITES_FILE) as f:
        for x in f:
            print(f'I like: {x.strip()}')

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
