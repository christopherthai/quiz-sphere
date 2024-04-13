import inquirer
from lib.models.user import User


# Function that exits the application
def exit_application():
    """Exit the application"""
    print("Exiting application...")
    exit()


def user_login():
    """Login the user to the application"""
    questions = [
        inquirer.Text(
            "username", message="Enter your username:"
        ),  # Ask for the username
    ]
    answers = inquirer.prompt(questions)  # Ask the user for the username
    username = answers["username"]  # Get the username from the answers
    user = User.find_by_username(username)
    if user:
        print(f"Welcome, {user.username}!")
    else:
        print("User not found.")


def create_username():
    """Create a new username for the user"""
    questions = [
        inquirer.Text(
            "username", message="Enter your username:"
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
        print("Username already exists.")
        return create_username()  # Recursively call the function

    # Check if the user is an admin
    is_admin = 1 if is_admin_input else 0

    user = User.create(username, is_admin)
    print(f"User {user.username} created successfully.")
    return user
