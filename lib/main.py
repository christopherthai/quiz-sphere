import inquirer

from cli.user_cli import user_login_menu


def main_menu():
    questions = [
        inquirer.List(
            "service",
            message="Choose an option",
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
        pass
    elif answers["service"] == "Exit":
        exit()


if __name__ == "__main__":
    user = user_login_menu()
    while True:
        main_menu()
