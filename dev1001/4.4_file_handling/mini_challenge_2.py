# Task: Read shopping.txt. For each line, if it contains a price (has a colon ':'), 
#       print Item: [Item Name], Price: $[Price]. Ignore lines without a price.
#
# Hint: Use split(':') and check the length of the resulting list.

with open ('shopping.txt') as f:
    for line in f:
        if ':' in line:
            splitline=line.split(":")
            print(f'Item: {splitline[0]}, Price: ${splitline[1].strip()}')


