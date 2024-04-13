import inquirer
from helpers.user_helper import user_login, create_username


# Function that displays the user login menu
def user_login_menu():
    questions = [
        inquirer.List(
            "action",
            message="Welcome to the QuizSphere. Choose an option:",
            choices=["Register", "Login", "Exit"],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "Register":
        user = create_username()
    elif answer["action"] == "Login":
        user = user_login()
    elif answer["action"] == "Exit":
        print("Exiting application...")
        exit()

    return user
