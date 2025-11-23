from storage import save_habit, load_habits

def add_habit():
    habit = input("Enter habit name: ")
    habits = load_habits()
    habits[habit] = []
    save_habit(habits)
    print(f"Habit '{habit}' added successfully!")

def view_habits():
    habits = load_habits()
    if not habits:
        print("No habits found.")
    else:
        print("Your habits:")
        for habit in habits:
            print(f"- {habit}")