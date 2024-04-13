from lib.models.user import User


# Function that exits the application
def exit_application():
    """Exit the application"""
    print("Exiting application...")
    exit()


def user_login():
    """Login the user to the application"""
    username = input("Enter your username: ")
    user = User.find_by_username(username)
    if user:
        print(f"Welcome, {user.username}!")
    else:
        print("User not found.")


def create_username():
    """Create a new username for the user"""
    username = input("Enter your username: ")
    is_admin_input = input("Are you an admin? (y/n): ").lower() == "y"

    # Check if the username already exists
    if User.find_by_username(username):
        print("Username already exists.")
        return create_username()  # Recursively call the function

    # Check if the user is an admin
    if is_admin_input == "y":
        is_admin = 1
    else:
        is_admin = 0

    user = User.create(username, is_admin)
    print(f"User {user.username} created successfully.")
    return user
