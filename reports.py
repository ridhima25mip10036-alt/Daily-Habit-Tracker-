from storage import load_habits

def show_summary():
    habits = load_habits()
    if not habits:
        print("No habits to show.")
        return

    print("\nHabit Summary:")
    for habit, dates in habits.items():
        print(f"{habit}: Done {len(dates)} times")