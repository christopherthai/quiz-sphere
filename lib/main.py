import inquirer

from cli.admin_cli import admin_menu
from cli.user_cli import user_login_menu
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
        admin_menu(user)
    elif answers["service"] == "Exit":
        print("Exiting application...")
        exit()


if __name__ == "__main__":
    user = user_login_menu()
    # print(f"Welcome, {user}!")
    while True:
        main_menu(user)
