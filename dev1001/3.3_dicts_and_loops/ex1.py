# Create a dict where names are keys, values are second dictionary.
student_database = {
    "Geralt of Rivia": {"Alchemy": 60, "Sword Fighting": 80, "Art": 25},
    "Inigo Montoya": {"Sword Fighting": 90, "Art": 55, "Wine Tasting": 79},
    "Alicia Dessendre": {"Sword Fighting": 100, "Art": 100, "Philosophy": 10}
}
#print names and grades
for name, grades in student_database.items():
    print(f"Name: {name}")
    print(f"Grades: {grades}")
    #get the average score for one student
    for score in grades.values():
        if name == "Alicia Dessendre":
            total = sum(grades.values())
            average = total / len(grades.values())
            print (f"{name}'s average score was: {average:.2f}")
            break #this printed out three times but I only wanted one
    #get min and max grades    
    for subject, score in grades.items():
        max_score = max(grades.items())
        min_score = min(grades.items())
        print(f"{name}'s highest scoring subject was: {max_score}.")
        print(f"{name}'s lowest scoring subject was: {min_score}.\n")
        break      
