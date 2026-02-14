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


def view_reminders():
    try:
        with open(FILE_NAME, "r") as file:
            reminders = file.readlines()

        if not reminders:
            print("No reminders found. \n")
            return

        print("\n Your Reminders:")
        for i, reminder in enumerates(reminders, 1):
            time_str, message = reminder.strip().split("|")
            print(f"{i}. {time_str} -> {message} ")  
        print() 


    except: FileNotFoundError:
    print("No reminders found. \n")


def delete_reminder():
    try:
        with open(FILE_NAME, "r") as file:
            reminders = file.readlines()

        view_reminders()
        choice = int(input("Enter reminder number to delete: "))

        reminders.pop(choice - 1)

        with open(FILE_NAME, "w") as file:
            file.writelines(reminders)

        print("🗑 Reminder deleted successfully!\n")

    except:
        print(" Invalid choice!\n")


def check_reminders():
    try:
        with open(FILE_NAME, "r") as file:
            reminders = file.readlines()

        now = datetime.now()

        updated_reminders = []

        for reminder in reminders:
            time_str, message = reminder.strip().split("|")
            reminder_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

            if now >= reminder_time:
                print(f"\n REMINDER: {message}\n")
            else:
                updated_reminders.append(reminder)

        with open(FILE_NAME, "w") as file:
            file.writelines(updated_reminders)

    except FileNotFoundError:
        pass


def main():
    while True:
        print("===== REMINDER MENU =====")
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Delete Reminder")
        print("4. Start Reminder Checker")
        print("5. Exit")

        choice = input("Choose an option: ")


        if choice == "1":
            add_reminder()
        elif choice == "2":
            view_reminders()
        elif choice == "3":
            delete_reminder()
        elif choice == "4":
            print("⏳ Reminder checker started (Press Ctrl+C to stop)")
            try:
                while True:
                    check_reminders()
                    time.sleep(60)  # Check every minute
            except KeyboardInterrupt:
                print("\nStopped reminder checker.\n")
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid option!\n")


if __name__ == "__main__":
    main()      