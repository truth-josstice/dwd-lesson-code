import json
print("\n--- Reading config.json ---")
with open("config.json", 'r') as f:
    config_data = json.load(f)
print(f"Username: {config_data['username']}")
print(f'Recent files: {config_data['recent_files']}')
config_data['recent_files'].append('newfile.txt')

# --- Writing to JSON ---
print("\n--- Writing to updated_config.json ---")
with open("updated_config.json", 'w') as f:
    json.dump(config_data, f, indent=4) # indent for pretty printing
print("updated_config.json created.")