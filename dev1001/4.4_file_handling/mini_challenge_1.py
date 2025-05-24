diary_file = "diary_entry.txt"

# 1. Write two lines about your day (use 'w' mode)
with open(diary_file, 'w') as f:
    f.write('This morning I woke up for class.' +'\n' + 'This morning I started class!')

# 2. Read and print content (use 'r' mode)
with open(diary_file, 'r') as f:
    for line in f:
        print(line.strip())
