import json
from datetime import datetime, timedelta

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.creation_date = datetime.now()
        self.completed_tasks = []

    def complete_task(self):
        self.completed_tasks.append(datetime.now())

class HabitTracker:
    def __init__(self):
        self.habits = []

    def create_habit(self, name, periodicity):
        habit = Habit(name, periodicity)
        self.habits.append(habit)

    def save_data(self):
        data = []
        for habit in self.habits:
            habit_data = {
                "name": habit.name,
                "periodicity": habit.periodicity,
                "creation_date": habit.creation_date.strftime("%Y-%m-%d %H:%M:%S"),
                "completed_tasks": [task.strftime("%Y-%m-%d %H:%M:%S") for task in habit.completed_tasks]
            }
            data.append(habit_data)

        with open("habits.json", "w") as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open("habits.json", "r") as f:
                data = json.load(f)
                for habit_data in data:
                    habit = Habit(habit_data["name"], habit_data["periodicity"])
                    habit.creation_date = datetime.strptime(habit_data["creation_date"], "%Y-%m-%d %H:%M:%S")
                    habit.completed_tasks = [datetime.strptime(task, "%Y-%m-%d %H:%M:%S") for task in habit_data["completed_tasks"]]
                    self.habits.append(habit)
        except FileNotFoundError:
            pass

    def get_longest_streak(self, habit):
        streaks = []
        current_streak = 0
        last_date = None
        for task in habit.completed_tasks:
            if last_date is None or (task - last_date).days == 1:
                current_streak += 1
            else:
                streaks.append(current_streak)
                current_streak = 0
            last_date = task
        streaks.append(current_streak)
        return max(streaks)

def analyze_habits(tracker):
    return [(habit.name, tracker.get_longest_streak(habit)) for habit in tracker.habits]

def main():
    tracker = HabitTracker()
    tracker.load_data()

    # Adding predefined habits
    tracker.create_habit("Morning Run", "daily")
    tracker.create_habit("Read a Chapter", "daily")
    tracker.create_habit("Weekly Reflection", "weekly")
    tracker.create_habit("Practice Guitar", "daily")
    tracker.create_habit("Drink Water", "daily")

    # Simulate tracking data for 4 weeks
    today = datetime.now()
    for _ in range(28):
        tracker.habits[0].complete_task()  # Morning Run
        tracker.habits[1].complete_task()  # Read a Chapter
        tracker.habits[2].complete_task()  # Weekly Reflection
        tracker.habits[3].complete_task()  # Practice Guitar
        tracker.habits[4].complete_task()  # Drink Water
        today += timedelta(days=1)

    while True:
        print("\nMenu:")
        print("1. Create Habit")
        print("2. Complete Task")
        print("3. Analyze Habits")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter habit name: ")
            periodicity = input("Enter periodicity (daily/weekly): ")
            tracker.create_habit(name, periodicity)
        elif choice == "2":
            for idx, habit in enumerate(tracker.habits):
                print(f"{idx + 1}. {habit.name}")
            habit_idx = int(input("Select a habit: ")) - 1
            if 0 <= habit_idx < len(tracker.habits):
                tracker.habits[habit_idx].complete_task()
        elif choice == "3":
            habit_analytics = analyze_habits(tracker)
            for habit_name, longest_streak in habit_analytics:
                print(f"Habit: {habit_name}, Longest Streak: {longest_streak}")
        elif choice == "4":
            tracker.save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
