import inquirer
from user_controller import register_user, login_user


def user_menu():
    questions = [
        inquirer.List(
            "action",
            message="User tasks - select an option:",
            choices=["Register", "Login", "Exit"],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "Register":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        register_user(username, password)
    elif answer["action"] == "Login":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login_user(username, password)
    elif answer["action"] == "Exit":
        return
