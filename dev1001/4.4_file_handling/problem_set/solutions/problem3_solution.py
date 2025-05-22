import json

SETTINGS_JSON_FILE = "settings.json"

def save_settings_to_json(settings_dict):
    """
    Writes the settings_dict to SETTINGS_JSON_FILE.
    The JSON should be pretty-printed (e.g., with an indent of 4).
    """
    # TODO 1: Open SETTINGS_JSON_FILE in 'write' mode ('w').
    with open(SETTINGS_JSON_FILE, 'w') as f:
        # TODO 2: Use json.dump() to write the settings_dict to the file.
        json.dump(settings_dict, f, indent=4)
    
    print(f"Settings saved to {SETTINGS_JSON_FILE}")


def load_settings_from_json():
    """
    Reads SETTINGS_JSON_FILE and returns the data as a Python dictionary.
    """
    loaded_settings = {} # Initialize as an empty dictionary
    # TODO 3: Open SETTINGS_JSON_FILE in 'read' mode ('r').
    with open(SETTINGS_JSON_FILE, 'r') as f:
        # TODO 4: Use json.load() to read the data from the file into loaded_settings.
        loaded_settings = json.load(f)
    
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
    if "theme" in reloaded_settings: # Good practice to check if key exists
        print(f"Loaded theme: {reloaded_settings['theme']}")
    else:
        print("Theme key not found in loaded settings.")
