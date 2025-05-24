# Task: Read updated_config.json. Change the theme to "light" and add a new
#       key-value pair "font_size": 12. Write this modified data to a new
#       file user_prefs.json.

import json

with open('updated_config.json') as f:
    config_data = json.load(f)
    config_data['theme'] = 'light'
    config_data['font_size'] = 12
    with open('user_prefs.json', 'w') as f:
        json.dump(config_data, f, indent=4)
