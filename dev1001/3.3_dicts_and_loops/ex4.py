users = [
    {"id": "user1", "name": "Alice", "email_verified": True, "logins_last_month": 15},
    {"id": "user2", "name": "Bob", "email_verified": False, "logins_last_month": 3},
    {"id": "user3", "name": "Charlie", "email_verified": True, "logins_last_month": 22},
    {"id": "user4", "name": "David", "email_verified": True, "logins_last_month": 8},
    {"id": "user5", "name": "Eve", "email_verified": False, "logins_last_month": 30},
]

inactive_user_ids = {}


for items in users:
    if items.get("logins_last_month") < 5:
       inactive_user_ids["Inactive username"] = items.get("id")
print(f"{inactive_user_ids}")

needs_verification_reminder = []

for items in users:
    if items.get("email_verified") is False:
        needs_verification_reminder.append(items.get("name"))
for names in needs_verification_reminder:
    print(f"Sent a verification reminder to {names}.")

total_logins = 0

for items in users:
    total_logins += items.get("logins_last_month")
print(f"Total logins: {total_logins}")

highest_logins = {}

for items in users:
    names = items.get("name")
    logins = items.get("logins_last_month")
    highest_logins[f"{names}: {logins}"] = items.get("logins_last_month")

print(f"Highest logins this month: {max(highest_logins)}")    

engagement_segments = {
    "low": [],
    "medium": [],
    "high": []
}

for items in users:
    if items.get("logins_last_month") <= 9:
        engagement_segments["low"].append(items.get("id"))
    elif items.get("logins_last_month") <= 19:
        engagement_segments["medium"].append(items.get("id"))
    elif items.get("logins_last_month") >= 20:
        engagement_segments["high"].append(items.get("id"))

print(f"{engagement_segments}")