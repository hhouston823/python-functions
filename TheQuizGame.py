# Objective: The aim of this assignment is to create a quiz game that asks questions and checks answers.

# Task 1: Develop a list of questions and answers.

questions: [
    ("What is the capital of France?", "Paris"),
    ("Where is Disney World located?", "Orlando"),
    ("Who created Mickey Mouse?", "Walt Disney")
]

# Task 2: Write a function that quizzes the user and takes their answers.

def quiz(questions):
    score = 0
    for question, answer in questions:
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    return score

# Task 3: Score the quiz and give the user feedback on their performance.

def score_quiz(score, total_questions):
    percentage = (score / total_questions) * 100
    print("You scored {} out of {} ({:.2f}%).".format(score, total_questions, percentage))
    if percentage >= 70:
        print("Congratulations! You passed the quiz!")
    else:
        print("You did not pass the quiz. Better luck next time!")

# Task 1
questions = [
    ("What is the capital of France?", "Paris"),
    ("Where is Disney World located?", "Orlando"),
    ("Who created Mickey Mouse?", "Walt Disney")
]

# Task 2
score = quiz(questions)

# Task 3
score_quiz(score, len(questions))