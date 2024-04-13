import inquirer

from cli.admin_cli import admin_menu
from cli.quiz_cli import quiz_menu
from cli.score_cli import score_menu
from cli.user_cli import user_menu


def login_screen():
    questions = [
        inquirer.List(
            "service",
            message="Welcome to the QuizSphere. Choose an option:",
            choices=[
                "Admin",
                "Quiz Management",
                "Score Management",
                "User Management",
                "Exit",
            ],
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers["service"] == "Admin":
        admin_menu()
    elif answers["service"] == "Quiz Management":
        quiz_menu()
    elif answers["service"] == "Score Management":
        score_menu()
    elif answers["service"] == "User Management":
        user_menu()
    elif answers["service"] == "Exit":
        exit()


def main_menu():
    questions = [
        inquirer.List(
            "service",
            message="Welcome to the QuizSphere. Choose an option:",
            choices=[
                "Take Quiz",
                "View Scores",
                "Admin Menu",
                "Exit",
            ],
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers["service"] == "Admin":
        admin_menu()
    elif answers["service"] == "Quiz Management":
        quiz_menu()
    elif answers["service"] == "Score Management":
        score_menu()
    elif answers["service"] == "User Management":
        user_menu()
    elif answers["service"] == "Exit":
        exit()


if __name__ == "__main__":
    while True:
        main_menu()
