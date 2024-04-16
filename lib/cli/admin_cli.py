import inquirer
from helpers.user_helper import (
    list_users,
    delete_user,
    add_user,
    edit_user,
    clear_screen,
    list_users_and_select_user,
)

from helpers.quiz_helper import (
    list_quizzes,
    delete_quiz,
    add_quiz,
    edit_quiz,
    list_specific_quiz,
    list_quizzes_and_select_quiz,
)

from helpers.question_helper import (
    add_question,
    delete_question,
    list_questions,
    list_questions_and_select_question,
)

# Admin menu for the application
def admin_menu(user):
    """Admin menu for the application"""
    from main import main_menu # Import the main_menu function

    # Set the questions to ask the user
    questions = [
        inquirer.List(
            "action",
            message="Admin Menu - choose an option",
            choices=["List Users", "List Quizzes", "Return to Main Menu"],
        ),
    ]
    
    # Ask the user for the action to take
    answer = inquirer.prompt(questions)
    if answer["action"] == "List Users":
        clear_screen()  # Clear the screen
        list_users()  # Call the list_users function
        users_management_menu(user)  # Call the users_management_menu function
    elif answer["action"] == "List Quizzes":
        clear_screen()  # Clear the screen
        list_quizzes()  # Call the list_quizzes function
        quizzes_management_menu(user)
    elif answer["action"] == "Return to Main Menu":
        clear_screen()  # Clear the screen
        main_menu(user)  # Call the main_menu function

# Users management menu for the application
def users_management_menu(user):
    """Manage users in the application"""

    # Set the questions to ask the user
    questions = [
        inquirer.List(
            "action",
            message="User Management - choose an option",
            choices=["Add User", "Edit User", "Delete User", "Return to Admin Menu"],
        ),
    ]
    
    # Ask the user for the action to take
    answer = inquirer.prompt(questions)
    if answer["action"] == "Add User":
        add_user() # Call the add_user function
        users_management_menu(user)  # Call the users_management_menu function
    elif answer["action"] == "Edit User":
        user_id = list_users_and_select_user() # List all users and prompt the user to select a user
        edit_user(user_id)
        users_management_menu(user)
    elif answer["action"] == "Delete User":
        user_id = list_users_and_select_user()
        delete_user(user_id)
        users_management_menu(user) # Call the users_management_menu function
    elif answer["action"] == "Return to Admin Menu":
        clear_screen()
        admin_menu(user) # Call the admin_menu function

# Quizzes management menu for the application
def quizzes_management_menu(user):
    """Manage quizzes in the application"""

    # Set the questions to ask the user
    questions = [
        inquirer.List(
            "action",
            message="Quiz Management - choose an option",
            choices=["Add Quiz", "Edit Quiz", "Delete Quiz", "Return to Admin Menu"],
        ),
    ]
    # Ask the user for the action to take
    answer = inquirer.prompt(questions) 
    if answer["action"] == "Add Quiz":
        add_quiz() # Call the add_quiz function
        quizzes_management_menu(user)  # Call the quizzes_management_menu function
    elif answer["action"] == "Edit Quiz":
        selected_quiz_id = list_quizzes_and_select_quiz() # List all quizzes and prompt the user to select a quiz
        clear_screen()
        edit_quiz_menu(user, selected_quiz_id) # Call the edit_quiz_menu function
        quizzes_management_menu(user)
    elif answer["action"] == "Delete Quiz":
        selected_quiz_id = list_quizzes_and_select_quiz()
        delete_quiz(selected_quiz_id)
        quizzes_management_menu(user)
    elif answer["action"] == "Return to Admin Menu":
        clear_screen()
        admin_menu(user) # Call the admin_menu function

# Edit quiz menu for the application
def edit_quiz_menu(user, selected_quiz_id):
    """Manage editing the quiz"""

    list_specific_quiz(selected_quiz_id)  # List the specific quiz

    # Set the questions to ask the user
    questions = [
        inquirer.List(
            "action",
            message="Edit Quiz Menu- choose an option",
            choices=[
                "Edit Quiz Content",
                "Edit Questions to Quiz",
                "Return to Quizzes Management Menu",
            ],
        ),
    ]
    
    # Ask the user for the action to take
    answer = inquirer.prompt(questions)
    if answer["action"] == "Edit Quiz Content":
        edit_quiz(selected_quiz_id) # Call the edit_quiz function
        edit_quiz_menu(user, selected_quiz_id) # Call the edit_quiz_menu function
    elif answer["action"] == "Edit Questions to Quiz":
        clear_screen()
        list_specific_quiz(selected_quiz_id)
        list_questions(selected_quiz_id)
        questions_management_menu(selected_quiz_id, user) # Call the questions_management_menu function
        edit_quiz_menu(user, selected_quiz_id)
    elif answer["action"] == "Return to Quizzes Management Menu":
        clear_screen()
        list_quizzes()  # Call the list_quizzes function
        quizzes_management_menu(user)

# Questions management menu for the application
def questions_management_menu(selected_quiz_id, user):
    """Manage questions in the quiz"""

    # Set the questions to ask the user
    questions = [
        inquirer.List(
            "action",
            message="Questions Management - choose an option",
            choices=[
                "Add Question",
                "Edit Question",
                "Delete Question",
                "Return to Edit Quiz Menu",
            ],
        ),
    ]
    answer = inquirer.prompt(questions)
    if answer["action"] == "Add Question":
        add_question(selected_quiz_id)
        questions_management_menu( # Call the questions_management_menu function
            selected_quiz_id, user
        )  
    elif answer["action"] == "Edit Question":
        # selected_question_id = list_questions_and_select_question()
        # # edit_question(selected_question_id)
        questions_management_menu(selected_quiz_id, user)
    elif answer["action"] == "Delete Question":
        selected_question_id = list_questions_and_select_question(selected_quiz_id)
        delete_question(selected_question_id, selected_quiz_id)
        questions_management_menu(selected_quiz_id, user)
    elif answer["action"] == "Return to Edit Quiz Menu":
        clear_screen()
        edit_quiz_menu(user, selected_quiz_id)
