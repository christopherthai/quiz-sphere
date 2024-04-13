import inquirer
from controllers.admin_controller import list_users, delete_user


def admin_menu(user):
    from main import main_menu

    """Admin menu for the application"""
    questions = [
        inquirer.List(
            "action",
            message="Admin Menu - choose an option:",
            choices=["List Users", "List Quizzes", "Return to Main Menu"],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "List Users":
        user_management_menu()
    elif answer["action"] == "List Quizzes":
        pass
    elif answer["action"] == "Return to Main Menu":
        main_menu(user)


def user_management_menu():
    """Manage users in the application"""

    users = list_users()
    for user in users:
        print(f"Username: {user.username}")

    questions = [
        inquirer.List(
            "action",
            message="User Management - choose an option:",
            choices=["Add User", "Edit User", "Delete User", "Exit"],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "Add User":
        pass
    elif answer["action"] == "Edit User":
        pass
    elif answer["action"] == "Delete User":
        user_id = input("Enter the user ID to delete: ")
        delete_user(user_id)
    elif answer["action"] == "Exit":
        admin_menu()
