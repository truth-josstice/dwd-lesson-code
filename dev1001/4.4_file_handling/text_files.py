# # Writing to a file
file_path = "my_first_file.txt"
with open(file_path, 'w') as f:
    f.write("Hello, Python File Handling!\n")
    f.write("This is the second line.\n")
print(f"'{file_path}' created and written to.")

# --- Reading from a file ---
print(f"\nReading from '{file_path}':")
with open(file_path, 'r') as f:
    # content_all = f.read(10) # Reads entire file into one string
    # print("--- Read all ---")
    # print(content_all)
    # print(f.read(5))
    # line_by_line (more common for larger files)
    print("--- Read line by line ---")
    # f.seek(0) # Reset cursor if you used f.read() above in same block
    first_line = f.readline() # Reads one line
    # print(list(first_line))
    print(f"First line: {first_line.strip()}") # .strip() removes newline
    second_line = f.readline()
    print(f"Second line: {second_line.strip()}")