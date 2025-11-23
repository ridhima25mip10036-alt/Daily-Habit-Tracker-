from storage import save_habit, load_habits
from utils import get_today

def mark_habit_done():
    habits = load_habits()
    if not habits:
        print("No habits to mark.")
        return

    print("Habits:")
    for habit in habits:
        print(f"- {habit}")
    habit_name = input("Enter habit to mark done: ")

    if habit_name in habits:
        today = get_today()
        habits[habit_name].append(today)
        save_habit(habits)
        print(f"Habit '{habit_name}' marked done for {today}.")
    else:
        print("Habit not found.")