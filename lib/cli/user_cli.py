import inquirer
from controllers.user_controller import user_login, create_username, exit_application


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
        exit_application()

    return user
