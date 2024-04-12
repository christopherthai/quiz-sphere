import inquirer
from admin_cli import admin_menu
from quiz_cli import quiz_menu
from score_cli import score_menu
from user_cli import user_menu


def main_menu():
    questions = [
        inquirer.List(
            "service",
            message="Welcome to the Quiz Management System. Choose an option:",
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


if __name__ == "__main__":
    while True:
        main_menu()
