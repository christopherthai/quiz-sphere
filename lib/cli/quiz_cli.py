# import random
import sqlite3
import inquirer

from helpers.quiz_helper import list_quizzes, list_quizzes_and_select_quiz
from helpers.user_helper import clear_screen
from helpers.question_helper import list_questions_and_answers_of_the_quiz

DB_PATH = "data/quiz_sphere_1.db"


def get_questions():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Questions ORDER BY RANDOM() LIMIT 10")
        questions = cursor.fetchall()
    except sqlite3.Error as error:
        print("Database error:", error)
        questions = []
    finally:
        if conn:
            conn.close()
    return questions

def start_quiz(selected_quiz_id):
    questions = get_questions()
    score = 0
    for question in questions:
        print(question[1])  # assuming question[1] is the question text
        answer = input("Your answer: ")
        if (
            answer.lower() == question[2].lower()
        ):  # assuming question[2] is the correct answer
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
            quiz_menu()

def quiz_flow():
    """ Starts the quiz flow after selecting a quiz. """
    clear_screen()
    selected_quiz_id = list_quizzes_and_select_quiz()
    questions_and_answers = list_questions_and_answers_of_the_quiz(selected_quiz_id)
    total_questions = len(questions_and_answers)
    score = 0

    for question in questions_and_answers:
        clear_screen()
        print(f"Question: {question.content}")
        answers = question.answers
        choices = [answer.content for answer in answers]
        correct_answer = next((answer.content for answer in answers if answer.is_correct), None)

        answer = inquirer.list_input("Choose the correct answer", choices=choices)

        if answer == correct_answer:
            print("Correct!")
            score += 20
        else:
            print("Wrong! The correct answer was:", correct_answer)

        input("Press Enter to continue...")

    clear_screen()
    print(f"Your final score is {score}/{total_questions * 20}.")
    handle_score_submission(score, selected_quiz_id)

def handle_score_submission(score, selected_quiz_id):
    if score < 60:
        retry = inquirer.confirm("Your score is below 60. Do you want to take it again?", default=True)
        if retry:
            quiz_flow(selected_quiz_id)  # Pass the quiz ID to restart the same quiz
        else:
            return_to_main_menu()
    else:
        submit = inquirer.confirm("Submit score?", default=True)
        if submit:
            submit_score(score)
        return_to_main_menu()

def submit_score(score):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Scores (score) VALUES (?)", (score,))
        conn.commit()
    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if conn:
            conn.close()


# def submit_score(score):
#     try:
#         conn = sqlite3.connect(DB_PATH)
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO scores (score) VALUES (?)", (score,))
#         conn.commit()
#     except sqlite3.Error as error:
#         print("Failed to insert data into sqlite table", error)
#     finally:
#         conn.close()


def quiz_menu(user):
    from main import main_menu
    list_quizzes()
    choices = ["Select Quiz", "Return to Admin Menu"]
    choice = inquirer.list_input("Select", choices=choices)
    if choice == "Select Quiz":
        selected_quiz_id = list_quizzes_and_select_quiz()
        # start_quiz(selected_quiz_id)
        question_and_answers = list_questions_and_answers_of_the_quiz(selected_quiz_id)
        quiz_flow(question_and_answers)
        quiz_menu(user)
    elif choice == "Return to Admin Menu":
        clear_screen()
        main_menu(user)


if __name__ == "__main__":
    quiz_menu()


