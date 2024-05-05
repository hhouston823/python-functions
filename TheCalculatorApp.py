# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.
# Task 1: Create functions for each arithmetic operation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed")
    return x / y

# Task 2: Implement user input to receive numbers and an operation choice

def get_user_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            return num1, num2, operation
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

# Task 3: Ensure your program can handle division by zero and other potential errors

def calculator():
    while True:
        try:
            num1, num2, operation = get_user_input()
            
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            
            print("Result:", result)
        
        except Exception as e:
            print("Error occurred:", e)
            continue
        
        if input("Do you want to perform another calculation? (yes/no): ").lower() != 'yes':
            break

# Run the calculator
calculator()
