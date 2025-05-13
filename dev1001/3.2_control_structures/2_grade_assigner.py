# --- USE: Grade Assigner ---
score = 93 # Try 95, 72, 65, 40
letter_grade = ""
is_passing = not letter_grade == "F" # Simple pass/fail check
has_honors = False

print(f"Score: {score}")

if score >= 93 and is_passing: # Using 'and'
    letter_grade = "A"
    has_honors = True
elif score >=87 and is_passing:
    letter_grade = "B+"
elif score >= 80 and is_passing:
    letter_grade = "B"
elif score >= 70 and is_passing:
    letter_grade = "C"
elif score >= 60 and is_passing: # is_passing is redundant here if score >= 60 implies passing
    letter_grade = "D"
elif score <60: # Using 'not'
    letter_grade = "F"
else: # Catch-all, though unlikely with current logic
    letter_grade = "Error in grading"

print(f"Letter Grade: {letter_grade}")
if has_honors:
    print("Congratulations on achieving honors!")
if letter_grade == "B+" or letter_grade == "A":
    print("You may be eligible for a scholarship consideration.")
if not is_passing: # Example of 'or' could be: if score < 0 or score > 100: print("Invalid score")
    print("Student needs to retake the course.")
