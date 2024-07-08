import calendar
from datetime import datetime
import json

reminders = {}

def display_month(year, month):
    print(calendar.month(year, month))

def add_reminder(date, reminder):
    if date in reminders:
        reminders[date].append(reminder)
    else:
        reminders[date] = [reminder]

def view_reminders(date):
    if date in reminders:
        return reminders[date]
    else:
        return []

def delete_reminder(date, reminder):
    if date in reminders and reminder in reminders[date]:
        reminders[date].remove(reminder)
        if not reminders[date]:
            del reminders[date]

def save_reminders(filename='reminders.json'):
    with open(filename, 'w') as file:
        json.dump(reminders, file)

def load_reminders(filename='reminders.json'):
    global reminders
    try:
        with open(filename, 'r') as file:
            reminders = json.load(file)
    except FileNotFoundError:
        reminders = {}

def main():
    load_reminders()
    current_year = datetime.now().year
    current_month = datetime.now().month

    while True:
        print("\nCalendar and Reminder App")
        print("1. Display Calendar")
        print("2. Add Reminder")
        print("3. View Reminders")
        print("4. Delete Reminder")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_month(current_year, current_month)
        elif choice == '2':
            date = input("Enter date (YYYY-MM-DD): ")
            reminder = input("Enter reminder: ")
            add_reminder(date, reminder)
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            reminders_for_date = view_reminders(date)
            if reminders_for_date:
                print("Reminders for", date)
                for r in reminders_for_date:
                    print("-", r)
            else:
                print("No reminders for this date.")
        elif choice == '4':
            date = input("Enter date (YYYY-MM-DD): ")
            reminder = input("Enter reminder to delete: ")
            delete_reminder(date, reminder)
        elif choice == '5':
            save_reminders()
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
