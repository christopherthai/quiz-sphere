import inquirer
import os

from cli.admin_cli import admin_menu
from cli.user_cli import user_login_menu
from cli.quiz_cli import quiz_menu

from cli.score_cli import scores_menu
from helpers.user_helper import clear_screen
from models.user import User

# from cli.quiz_cli import quiz_menu


def main_menu(user):
    """Main menu for the application"""
    questions = [
        inquirer.List(
            "service",
            message="Main Menu: Choose an option",
            choices=[
                "Take Quiz",
                "View Scores",
                "Admin Menu",
                "Exit Application",
            ],
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers["service"] == "Take Quiz":
        clear_screen()
        if user.is_admin == 1:
            print("Admin users cannot take the quiz.\n")
            main_menu(user)
        else:
            # Add your code here to implement the logic for taking the quiz
            quiz_menu(user)
    elif answers["service"] == "View Scores":
        clear_screen()
        scores_menu(user)
        # display_quiz_options(user)
    elif answers["service"] == "Admin Menu":
        if user.is_admin == 1:
            clear_screen()
            admin_menu(user)
        else:
            clear_screen()
            print("Only admin users can access the admin menu.")
    elif answers["service"] == "Exit Application":
        print("Exiting application...")
        exit()


if __name__ == "__main__":
    clear_screen()  # Clear the screen
    user = user_login_menu()
    while True:
        main_menu(user)
