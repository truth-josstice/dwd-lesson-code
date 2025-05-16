text = """
This is a sample text. This text is for a sample programming exercise.
The exercise is to count words in this text.
Ignore case and punctuation for simplicity.
"""

text_processed = text.lower().replace(".", "").replace(",", "").split()

text_dict = {}

for words in (text_processed):    
    if words not in (text_dict):
        text_dict[words]=1
    else:
        text_dict[words]+=1

print(text_dict)
print("Word count:")
print("-" * 30)
for word, count in text_dict.items():
    print(f"{word}: {count}")
print("-" * 30 + "\n")

word_list = list(text_dict.items())
print("Alphabetically sorted word list:")
print("-" * 30)
for word, count in sorted(word_list):
    print(f"{word.capitalize()}: {count}")

number_list = list(text_dict.items())

    