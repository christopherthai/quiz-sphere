import inquirer
import os

from cli.admin_cli import admin_menu
from cli.user_cli import user_login_menu
from helpers.user_helper import clear_screen

# from cli.quiz_cli import quiz_menu


def main_menu(user):
    questions = [
        inquirer.List(
            "service",
            message="Main Menu: Choose an option",
            choices=[
                "Take Quiz",
                "View Scores",
                "Admin Menu",
                "Exit",
            ],
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers["service"] == "Take Quiz":
        pass
    elif answers["service"] == "View Scores":
        pass
    elif answers["service"] == "Admin Menu":
        clear_screen()
        admin_menu(user)
    elif answers["service"] == "Exit":
        print("Exiting application...")
        exit()


if __name__ == "__main__":
    user = user_login_menu()
    # print(f"Welcome, {user}!")
    while True:
        clear_screen()
        main_menu(user)
