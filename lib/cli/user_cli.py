import inquirer
from controllers.user_controller import user_login, create_username


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
