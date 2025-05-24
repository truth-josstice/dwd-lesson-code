# Task: Read new_grades.csv (that was just created) and print only the
#       names of students who scored above 90.

import csv

with open('new_grades.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        name, subject, score = row
        if int(score) > 90:
            print(f'{name} scored above 90')
