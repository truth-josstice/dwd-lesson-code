import csv

with open('grades.csv', newline='') as f:
    csv_reader = csv.reader(f)
    header = next(csv_reader)
    print(f"Header: {header}")
    for row in csv_reader:
        name, subject, grade = row
        print(f'{name} scored {grade} in {subject}')

# --- Writing to CSV ---
print("\n--- Writing to new_grades.csv ---")
new_data = [
    ["Name", "Subject", "Score"],
    ["David", "History", "88"],
    ["Eve", "Art", "92"]
]
with open("new_grades.csv", mode='w', newline='') as f:
    csv_writer = csv.writer(f)
    # csv_writer.writerow(new_data[0]) # Write header
    # csv_writer.writerow(new_data[1]) # Write data row
    csv_writer.writerows(new_data) # Write all rows
print("new_grades.csv created.")