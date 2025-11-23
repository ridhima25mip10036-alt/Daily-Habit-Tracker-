from habits import add_habit, view_habits
from tracker import mark_habit_done
from reports import show_summary

def main():
    while True:
        print("\n--- Daily Habit Tracker ---")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Mark Habit Done")
        print("4. Show Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_habit()
        elif choice == '2':
            view_habits()
        elif choice == '3':
            mark_habit_done()
        elif choice == '4':
            show_summary()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()