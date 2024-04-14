import sys
import os
import random
import inquirer
import logging
from sqlalchemy import create_engine

# 로깅 레벨을 설정합니다.
logging.basicConfig(level=logging.ERROR)

# 데이터베이스 엔진을 생성합니다.
engine = create_engine('sqlite:///quiz.db')

# 현재 파일의 위치를 기준으로 상위 디렉토리 경로를 구합니다.
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(base_path)

from lib.controllers.quiz_helper import get_all_subjects, get_questions_by_subject

def quiz_flow():
    subjects = get_all_subjects()
    choices = {str(i + 1): subject for i, subject in enumerate(subjects)}
    questions = [
        inquirer.List('subject',
                      message="Choose the subject number you want to take a quiz on:",
                      choices=[f"{i}. {subject}" for i, subject in choices.items()],
                     )
    ]
    chosen_subject = inquirer.prompt(questions)['subject'].split('. ')[1]
    quiz_questions = get_questions_by_subject(chosen_subject)
    random.shuffle(quiz_questions)
    quiz_questions = quiz_questions[:5]

    score = 0
    for idx, question in enumerate(quiz_questions, 1):
        print(f"Question {idx}: {question.question_text}")
        user_answer = input("Your answer: ")
        correct_answer = next((answer.answer_text for answer in question.answers if answer.is_correct), None)
        if user_answer.lower() == correct_answer.lower():
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
    print(f"Your score is {score}/5.")

def main_menu():
    while True:
        print("1. Take a Quiz")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            quiz_flow()
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please choose again.")

if __name__ == '__main__':
    main_menu()


