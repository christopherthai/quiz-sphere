import random
import sqlite3

def get_questions():
    conn = sqlite3.connect('quiz_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 10")
    questions = cursor.fetchall()
    conn.close()
    return questions

def start_quiz():
    questions = get_questions()
    score = 0
    for question in questions:
        print(question[1])
        answer = input("Your answer: ")
        if answer.lower() == question[2].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!.")
    print(f"Your score is {score}.")
    submit = input("Submit score? (y/n): ")
    if submit.lower() == 'y':
        submit_score(score)
        main_menu()
    else:
        retry = input("Do it again? (y/n): ")
        if retry.lower() == 'y':
            start_quiz()
        else:
            main_menu()

def submit_score(score):
    conn = sqlite3.connect('quiz_db.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (score) VALUES (?)", (score,))
    conn.commit()
    conn.close()

def main_menu():
    print("1. Quiz Start")
    print("2. End")
    choice = input("Select: ")
    if choice == '1':
        start_quiz()
    elif choice == '2':
        print("Exit Program.")
        exit()
    else:
        print("Wrong choice.")
        main_menu()

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