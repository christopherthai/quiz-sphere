import inquirer
from helpers.user_helper import (
    list_users,
    delete_user,
    add_user,
    edit_user,
    clear_screen,
)


def admin_menu(user):
    from main import main_menu

    """Admin menu for the application"""
    questions = [
        inquirer.List(
            "action",
            message="Admin Menu - choose an option",
            choices=["List Users", "List Quizzes", "Return to Main Menu"],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "List Users":
        clear_screen()
        user_management_menu()
    elif answer["action"] == "List Quizzes":
        clear_screen()
        print("List Quizzes")
    elif answer["action"] == "Return to Main Menu":
        clear_screen()
        main_menu(user)


def user_management_menu():
    """Manage users in the application"""

    users = list_users()
    print("List of Users:\n")
    for user in users:
        i = users.index(user) + 1
        print(f"{i}. {user.username}\n")

    questions = [
        inquirer.List(
            "action",
            message="User Management - choose an option",
            choices=["Add User", "Edit User", "Delete User", "Return to Admin Menu"],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "Add User":
        add_user()
        user_management_menu()
    elif answer["action"] == "Edit User":
        username = input("Enter the username to edit: ")
        edit_user(username)
        user_management_menu()
    elif answer["action"] == "Delete User":
        username = input("Enter the username to delete: ")
        delete_user(username)
        user_management_menu()
    elif answer["action"] == "Return to Admin Menu":
        clear_screen()
        admin_menu(user)
