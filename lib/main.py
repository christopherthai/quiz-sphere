import inquirer

from cli.user_cli import user_login_menu


def main_menu():
    questions = [
        inquirer.List(
            "service",
            message="Welcome to the QuizSphere. Choose an option",
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
        pass
    elif answers["service"] == "Quiz Management":
        pass
    elif answers["service"] == "Score Management":
        pass
    elif answers["service"] == "User Management":
        pass
    elif answers["service"] == "Exit":
        exit()


if __name__ == "__main__":

    while True:
        user_login_menu()
