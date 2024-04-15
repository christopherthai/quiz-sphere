import random
import sqlite3
import inquirer


def get_questions():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 10")
        questions = cursor.fetchall()
    except sqlite3.Error as error:
        print("Database error:", error)
        questions = []
    finally:
        if conn:
            conn.close()
    return questions

def start_quiz():
    questions = get_questions()
    score = 0
    for question in questions:
        print(question[1])  # assuming question[1] is the question text
        answer = input("Your answer: ")
        if answer.lower() == question[2].lower():  # assuming question[2] is the correct answer
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"Your score is {score}.")
    submit = inquirer.confirm("Submit score?", default=True)
    if submit:
        submit_score(score)
    else:
        retry = inquirer.confirm("Do it again?", default=False)
        if retry:
            start_quiz()
        else:
            main_menu()

def submit_score(score):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO scores (score) VALUES (?)", (score,))
        conn.commit()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        conn.close()

def main_menu():
    choices = ['Quiz Start', 'End']
    choice = inquirer.list_input("Select:", choices=choices)
    if choice == 'Quiz Start':
        start_quiz()
    elif choice == 'End':
        print("Exit Program.")
        exit()

if __name__ == "__main__":
    main_menu()






















# # import sys
# # import os
# import random
# import inquirer
# # import logging
# from sqlalchemy import create_engine

# from models.question import Question
# from models.answer import Answer



# def quiz_flow():
#     subjects = get_all_subjects()
#     choices = {str(i + 1): subject for i, subject in enumerate(subjects)}
#     questions = [
#         inquirer.List('subject',
#                       message="Choose the subject number you want to take a quiz on:",
#                       choices=[f"{i}. {subject}" for i, subject in choices.items()],
#                      )
#     ]
#     chosen_subject = inquirer.prompt(questions)['subject'].split('. ')[1]
#     quiz_questions = get_questions_by_subject(chosen_subject)
#     random.shuffle(quiz_questions)
#     quiz_questions = quiz_questions[:5]

#     score = 0
#     for idx, question in enumerate(quiz_questions, 1):
#         print(f"Question {idx}: {question.question_text}")
#         user_answer = input("Your answer: ")
#         correct_answer = next((answer.answer_text for answer in question.answers if answer.is_correct), None)
#         if user_answer.lower() == correct_answer.lower():
#             score += 1
#             print("Correct!")
#         else:
#             print(f"Incorrect. The correct answer is {correct_answer}.")
#     print(f"Your score is {score}/5.")

# def main_menu():
#     while True:
#         print("1. Take a Quiz")
#         print("2. Exit")
#         choice = input("Choose an option: ")
#         if choice == '1':
#             quiz_flow()
#         elif choice == '2':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid input. Please choose again.")

# if __name__ == '__main__':
#     main_menu()