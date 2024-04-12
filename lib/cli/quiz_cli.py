import inquirer
from quiz_controller import create_quiz, delete_quiz


def quiz_menu():
    questions = [
        inquirer.List(
            "action",
            message="Quiz management - select an option:",
            choices=["Create Quiz", "Delete Quiz", "Exit"],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "Create Quiz":
        title = input("Enter the title of the quiz: ")
        create_quiz(title)
    elif answer["action"] == "Delete Quiz":
        quiz_id = input("Enter the quiz ID to delete: ")
        delete_quiz(quiz_id)
    elif answer["action"] == "Exit":
        return
