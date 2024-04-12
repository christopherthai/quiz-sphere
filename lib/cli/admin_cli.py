import inquirer
from admin_controller import list_users, delete_user


def admin_menu():
    questions = [
        inquirer.List(
            "action",
            message="Admin tasks - choose an option:",
            choices=["List Users", "Delete User", "Exit"],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "List Users":
        users = list_users()
        for user in users:
            print(user)
    elif answer["action"] == "Delete User":
        user_id = input("Enter user ID to delete: ")
        delete_user(user_id)
    elif answer["action"] == "Exit":
        return
