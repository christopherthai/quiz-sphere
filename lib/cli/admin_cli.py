import inquirer
from helpers.user_helper import (
    list_users,
    delete_user,
    add_user,
    edit_user,
    clear_screen,
)


def admin_menu(user):
    """Admin menu for the application"""
    from main import main_menu

    questions = [
        inquirer.List(
            "action",
            message="Admin Menu - choose an option",
            choices=["List Users", "List Quizzes", "Return to Main Menu"],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "List Users":
        clear_screen()  # Clear the screen
        users_management_menu()  # Call the users_management_menu function
    elif answer["action"] == "List Quizzes":
        clear_screen()  # Clear the screen
        print("List Quizzes")
    elif answer["action"] == "Return to Main Menu":
        clear_screen()  # Clear the screen
        main_menu(user)  # Call the main_menu function


def users_management_menu():
    """Manage users in the application"""

    users = list_users()
    print("List of Users:\n")
    for user in users:
        i = users.index(user) + 1  # Get the index of the user
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
        users_management_menu()  # Call the users_management_menu function
    elif answer["action"] == "Edit User":
        username = input("Enter the username to edit: ")
        edit_user(username)
        users_management_menu()
    elif answer["action"] == "Delete User":
        username = input("Enter the username to delete: ")
        delete_user(username)
        users_management_menu()
    elif answer["action"] == "Return to Admin Menu":
        clear_screen()
        admin_menu(user)
