# Objective: The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade. 

def calculate_average(grades):
    total_grades = sum(grades)
    num_grades = len(grades)
    if num_grades == 0:
        return 0  # Return 0 if the list is empty to avoid division by zero
    average_grade = total_grades / num_grades
    return average_grade

# Task 2: Implement a function to find the highest and lowest grade.

def find_highest_and_lowest(grades):
    if not grades:
        return None, None  # Return None for both highest and lowest if the list is empty
    highest_grade = max(grades)
    lowest_grade = min(grades)
    return highest_grade, lowest_grade

# Task 3: Create a feature that categorizes grades into letter grades.

def categorize_grades(grades):
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')
    return letter_grades

# Example usage:
my_grades = [85, 92, 78, 65, 95]

average = calculate_average(my_grades)
print("Average Grade:", average)

highest, lowest = find_highest_and_lowest(my_grades)
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)

letter_grades = categorize_grades(my_grades)
print("Letter Grades:", letter_grades)