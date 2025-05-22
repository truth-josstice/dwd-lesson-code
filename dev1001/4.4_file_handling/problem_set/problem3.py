'''
Problem 3: My Simple Settings (JSON Files)

Objective: Practice writing a Python dictionary to a JSON file and then reading it back.

Description:
Create a Python script that:

1. Defines a Python dictionary representing some simple application settings (e.g., username, theme).
2. Writes this dictionary to a JSON file named settings.json in a human-readable (indented) format.
3. Reads the settings.json file back into a Python dictionary.
4. Prints one of the settings from the reloaded dictionary to verify it worked.
'''

import json

SETTINGS_JSON_FILE = "settings.json"

def save_settings_to_json(settings_dict):
    """
    Writes the settings_dict to SETTINGS_JSON_FILE.
    The JSON should be pretty-printed (e.g., with an indent of 4).
    """
    # TODO 1: Open SETTINGS_JSON_FILE in 'write' mode ('w').
    # Use a 'with' statement.
    # Inside the 'with' block:
    #     TODO 2: Use json.dump() to write the settings_dict to the file.
    #             Make sure to include the indent argument for pretty printing.
    
    print(f"Settings saved to {SETTINGS_JSON_FILE}")


def load_settings_from_json():
    """
    Reads SETTINGS_JSON_FILE and returns the data as a Python dictionary.
    """
    loaded_settings = {} # Initialize as an empty dictionary
    # TODO 3: Open SETTINGS_JSON_FILE in 'read' mode ('r').
    # Use a 'with' statement.
    # Inside the 'with' block:
    #     TODO 4: Use json.load() to read the data from the file into loaded_settings.
    
    print(f"Settings loaded from {SETTINGS_JSON_FILE}")
    return loaded_settings


# --- Test your functions ---
if __name__ == "__main__":
    my_app_settings = {
        "username": "pyStudent123",
        "theme": "dark",
        "notifications_enabled": True,
        "font_size": 14
    }

    save_settings_to_json(my_app_settings)
    
    reloaded_settings = load_settings_from_json()
    
    print("\n--- Verifying Loaded Settings ---")
    # TODO 5: Print the value associated with the "theme" key from the reloaded_settings dictionary.
    # Example: print(f"Loaded theme: {reloaded_settings['theme']}")
    

    # Expected content in settings.json (or similar pretty-printed format):
    # {
    #     "username": "pyStudent123",
    #     "theme": "dark",
    #     "notifications_enabled": true,
    #     "font_size": 14
    # }
    #
    # Expected console output:
    # Settings saved to settings.json
    # Settings loaded from settings.json
    #
    # --- Verifying Loaded Settings ---
    # Loaded theme: dark
