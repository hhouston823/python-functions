# Objective: The aim of this assignment is to create a program that tracks fitness activities and calories burned.

# Task 1: Log fitness activities and durations

def log_activities(activities, durations):
    log = dict(zip(activities, durations))
    return log

# Task 2: Estimate calories burned
def calculate_calories_burned(activity, duration):
    calories_burned = duration * 3.5
    return calories_burned

# Task 3: Generate summary report
def generate_summary(log):
    total_calories = 0
    print("Fitness Activity Summary:")
    for activity, duration in log.items():
        calories_burned = calculate_calories_burned(activity, duration)
        total_calories += calories_burned
        print(f"{activity}: {duration} minutes | Calories burned: {calories_burned}")
    print("Total calories burned for the day:", total_calories)

# Task 1: 
activities = ['Dancing', 'Swimming', 'Biking']
durations = [10, 20, 15]
activity_log = log_activities(activities, durations)

# Task 2:
# Directly estimate calories burned using the formula: Duration * 3.5

# Task 3: 
generate_summary(activity_log)