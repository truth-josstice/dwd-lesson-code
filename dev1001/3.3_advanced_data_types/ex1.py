# Tuples Exercise

# Student Info: (ID, Name, Major)
student_record = (101, "Alice Wonderland", "Computer Science")

# 1. Access and print the student's name.
# 2. Create a new tuple that includes the student's current term.
#       Remember, tuples are immutable, so you'll create a NEW one.
#       Hint: You can concatenate tuples using '+'
#       (Challenge) Use unpack operator instead of concatenation.
# 3. Unpack the original student_record into three separate variables.
# 4. Use the slice operator to extract the student name only.

print(f"Student Name: {student_record[1]}")
# student_record_new = student_record + ("Term 4",) # Concetenate
student_record_new = (*student_record, "Term 4") # Unpack
ID, Name, Major = student_record #Unpacked into seperate Variables
name_only = student_record[1:2]

print(student_record_new)
print(ID)
print(Name)
print(Major)
print(name_only)