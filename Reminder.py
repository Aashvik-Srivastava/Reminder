import time 
from datetime import datetime

FILE_NAME = "reminder.txt"

def add_reminder():
    message = input("Enter reminder msg:")
    date_time = input("Enter date & time(yyyy-mm-dd  hh:mm):")

    try:
        reminder_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        with open(FILE_NAME, "a") as file:
            file.write(f"{reminder_time}|{message}\n")
        print("✅ Reminder added successfully!\n")


    except:
        print("❌ Invalid date format!\n")
