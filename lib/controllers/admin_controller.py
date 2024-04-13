import inquirer
from models.user import User
from models.quiz import Quiz


# from models.score import Score
# from models.question import Question
# from models.answer import Answer


def list_users():
    """List all users in the database"""
    users = User.get_all()  # Get all users from the database
    for user in users:
        print(f"Username: {user.username}")


def add_user():
    """Add a user to the database"""
    questions = [
        inquirer.Text(
            "username", message="Enter the username:"
        ),  # Ask for the username
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
        print("Username already exists.")
        return add_user()  # Recursively call the function

    # Convert the is_admin input to a boolean
    is_admin = 1 if is_admin_input else 0

    user = User.create(username, is_admin)
    print(f"User {user.username} created successfully.")
    return user


def edit_user(user_id):
    """Edit a user in the database"""
    user = User.find_by_id(user_id)  # Find the user by id
    if user:
        questions = [
            inquirer.Text(
                "username", message="Enter the new username:"
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

        # Check if the new username already exists
        if User.find_by_username(username):
            print("Username already exists.")
            return edit_user(user_id)  # Recursively call the function

        # Convert the is_admin input to a boolean
        is_admin = 1 if is_admin_input else 0

        user.username = username
        user.is_admin = is_admin
        user.save()  # Save the changes to the database
        print(f"User {user.username} updated successfully.")
    else:
        print("User not found.")


def delete_user(user_id):
    """Delete a user from the database"""
    user = User.find_by_id(user_id)  # Find the user by id
    if user:
        user.delete()  # Delete the user from the database
        print(f"User {user.username} deleted successfully.")
    else:
        print("User not found.")
