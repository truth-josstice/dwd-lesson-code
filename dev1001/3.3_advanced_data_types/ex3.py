# Sets Exercise

required_skills = {"python", "git", "problem-solving"}
candidate_skills = {"python", "java", "communication"}
print(f"Required skills: {required_skills}")
print(f"Candidate skills: {candidate_skills}")

# Given the above sets, write code to:
# 1. Add "communication" to required_skills if it's not already there.
required_skills.add("communication")
print(f"Updated required skills: {required_skills}")

# 2. Find out which skills the candidate has that are also required.
print(f"Candidate's required skills: {required_skills & candidate_skills}")
# 3. Find out all unique skills possessed by either (required or candidate).
print(f"All unique skills in categories: {required_skills | candidate_skills}")
# 4. Which skills are required but the candidate doesn't have.
print(f"Required skills not shown by candidate: {required_skills - candidate_skills}")