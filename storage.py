import csv
import os

FILE = "habits.csv"

def load_habits():
    habits = {}
    if os.path.exists(FILE):
        with open(FILE, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                habit, *dates = row
                habits[habit] = dates
    return habits

def save_habit(habits):
    with open(FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        for habit, dates in habits.items():
            writer.writerow([habit, *dates])