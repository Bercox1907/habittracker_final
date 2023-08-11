Habit Tracker App


Overview

The Habit Tracker App is a Python command-line application designed to help users manage their habits, track their progress, and analyze their performance over time. This simple yet effective app allows users to create habits, mark tasks as completed, and view insightful analytics about their habits.



Features

Create new habits with different periodicities (daily or weekly).
Mark tasks as completed for each habit.
Store habit data persistently using JSON files.
Analyze habits to determine the longest streak for each habit.
Installation

Make sure you have Python 3.7 or later installed.
Download or clone this repository.
Open a terminal and navigate to the project directory.
Run the following command to install dependencies:
pip install -r requirements.txt



Usage

Open a terminal and navigate to the project directory.
Run the following command to start the Habit Tracker App:

python habittracker_final.py

Follow the on-screen menu options to create habits, complete tasks, and analyze habits.



Example

Here's a brief example of how to use the Habit Tracker App:

Create a habit: "Morning Run", with a daily periodicity.
Complete tasks for the habit each day over a period of 4 weeks.
Analyze the habits to see the longest streak for each habit.



Analytics Module

The analytics module uses functional programming to analyze habit data and calculate the longest streak for each habit. The analyze_habits function takes the HabitTracker instance as input and returns a list of tuples containing habit names and their longest streaks.


Data Persistence

Habit data is stored in JSON files. When you create habits or mark tasks as completed, the data is saved to a "habits.json" file. The app loads this data when started, allowing you to continue tracking your habits seamlessly.
















