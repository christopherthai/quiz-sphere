import inquirer
import os
from models.user import User


# from models.score import Score
# from models.question import Question
# from models.answer import Answer


def user_login():
    """Login the user to the application"""
    questions = [
        inquirer.Text(
            "username", message="Enter your username"
        ),  # Ask for the username
    ]
    answers = inquirer.prompt(questions)  # Ask the user for the username
    username = answers["username"]  # Get the username from the answers
    user = User.find_by_username(username)
    if user:
        clear_screen()
        print(f"Welcome, {user.username}!\n")
    else:
        clear_screen()
        print("User not found.\n")
        user = user_login()  # Recursively call the function

    return user


def create_username():
    """Create a new username for the user"""
    questions = [
        inquirer.Text(
            "username", message="Enter your username"
        ),  # Ask for the username
        inquirer.Confirm(
            "is_admin", message="Are you an admin?"
        ),  # Ask if the user is an admin
    ]
    answers = inquirer.prompt(
        questions
    )  # Ask the user for the username and if they are an admin
    username = answers["username"]  # Get the username from the answers
    is_admin_input = answers["is_admin"]  # Get the is_admin from the answers

    # Check if the username already exists
    if User.find_by_username(username):
        print("Username already exists.\n")
        return create_username()  # Recursively call the function

    # Convert the is_admin input to a boolean
    is_admin = 1 if is_admin_input else 0

    user = User.create(username, is_admin)
    print(f"User {user.username} created successfully.\n")
    return user


def list_users():
    """List all users in the database"""
    users = User.get_all()  # Get all users from the database
    print("List of Users:\n")
    for user in users:
        i = users.index(user) + 1  # Get the index of the user
        print(f"{i}. {user.username}\n")  # Print the user's username
    return users


def add_user():
    """Add a user to the database"""

    questions = [
        inquirer.Text("username", message="Enter the username"),  # Ask for the username
        inquirer.Confirm(
            "is_admin", message="Is the user an admin?"
        ),  # Ask if the user is an admin
    ]
    answers = inquirer.prompt(
        questions
    )  # Ask the user for the username and if they are an admin
    username = answers["username"]  # Get the username from the answers
    is_admin_input = answers["is_admin"]  # Get the is_admin from the answers

    # Check if the username already exists
    if User.find_by_username(username):
        clear_screen()
        list_users()  # List all users in the database
        print("Username already exists.\n")
        return add_user()  # Recursively call the function

    # Convert the is_admin input to a boolean
    is_admin = 1 if is_admin_input else 0

    user = User.create(username, is_admin)
    clear_screen()
    list_users()  # List all users in the database
    print(f"User: {user.username} created successfully.\n")
    return user


def edit_user(user_id):
    """Edit a user in the database"""
    user = User.find_by_id(user_id)  # Find the user by its ID
    if user:
        questions = [
            inquirer.Text(
                "username", message="Enter the new username"
            ),  # Ask for the new username
            inquirer.Confirm(
                "is_admin", message="Is the user an admin?"
            ),  # Ask if the user is an admin
        ]
        answers = inquirer.prompt(
            questions
        )  # Ask the user for the new username and if they are an admin
        username = answers["username"]  # Get the new username from the answers
        is_admin_input = answers["is_admin"]  # Get the is_admin from the answers

        # Convert the is_admin input to a boolean
        is_admin = 1 if is_admin_input else 0

        user.username = username
        user.is_admin = is_admin
        user.update()  # Save the changes to the database
        clear_screen()
        list_users()  # List all users in the database
        print(f"User: {user.username} updated successfully.\n")
    else:
        clear_screen()
        list_users()  # List all users in the database
        print("Username not found.\n")


def delete_user(user_id):
    """Delete a user from the database"""
    user = User.find_by_id(user_id)  # Find the user by its ID
    if user:
        user.delete()  # Delete the user from the database
        clear_screen()  # Clear the screen
        list_users()  # List all users in the database
        print(f"User: {user.username} deleted successfully.\n")
    else:
        list_users()  # List all users in the database
        print("User not found.")


def list_users_and_select_user():
    """List all users and prompt the user to select a user"""
    users = User.get_all()
    user_options = [(user.username, user.id) for user in users]

    clear_screen()
    print("List of Users:\n")

    # Display the users
    for i, option in enumerate(user_options, start=1):
        print(f"{i}. {option[0]}\n")

    # Prompt the user to select a user
    questions = [
        inquirer.Text(
            "user_id",
            message="Enter the number of the User you want to select",
            validate=lambda _, x: x.isdigit() and 1 <= int(x) <= len(user_options),
        ),
    ]
    answers = inquirer.prompt(questions)
    user_id = user_options[int(answers["user_id"]) - 1][1]  # Get the user ID

    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        print("User not found.")
    return user_id


def clear_screen():
    """Use 'cls' for Windows and 'clear' for macOS and Unix/Linux"""
    command = "cls" if os.name == "nt" else "clear"
    os.system(command)
