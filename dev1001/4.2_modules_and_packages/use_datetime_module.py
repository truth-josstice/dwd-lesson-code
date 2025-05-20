# use_datetime_module.py
import datetime

# Using the datetime module to work with dates and times

# Get the current date and time
now = datetime.datetime.now()
print(f"Current date and time: {now}")

# Get just the current date
today = datetime.date.today()
print(f"Today's date: {today}")

# Format the date and time
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted current time: {formatted_time}")

formatted_date = today.strftime("%A, %B %d, %Y")
print(f"Formatted today's date: {formatted_date}")