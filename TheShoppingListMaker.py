# Objective: The aim of this assignment is to create a program that helps users make a shopping list. 

# Task 1: Write a function that lets the user add items to the list.

def add_item(shopping_list, item):
    shopping_list.append(item)

# Task 2: Include a feature to remove items from the list:

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f"{item} is not in the shopping list.")

# Task 3: Add a function that prints out the entire list in a formatted way.

def print_list(shopping_list):
    print("Shopping List:")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{index}. {item}")

# Example usage:
my_shopping_list = []

add_item(my_shopping_list, "Apples")
add_item(my_shopping_list, "Milk")
add_item(my_shopping_list, "Bread")
print_list(my_shopping_list)

remove_item(my_shopping_list, "Milk")
print_list(my_shopping_list)