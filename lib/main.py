import inquirer
import os

from cli.admin_cli import admin_menu
from cli.user_cli import user_login_menu
from cli.score_cli import display_quiz_options, display_quiz_scores
from helpers.user_helper import clear_screen

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
        else:
            # Add your code here to implement the logic for taking the quiz
            print("Take Quiz\n")
    elif answers["service"] == "View Scores":
        clear_screen()
<<<<<<< HEAD
        display_quiz_scores(user)
        display_quiz_options(user)
=======
        print({user}, {user.id}, {user.is_admin})
        display_quiz_scores(user)
        # display_quiz_options(user)
>>>>>>> 8b49486d836808f377b6c5340a4224287b770f67
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
    clear_screen() # Clear the screen
    user = user_login_menu()
    while True:
        main_menu(user)
