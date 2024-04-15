import inquirer
from models.quiz import Quiz
from helpers.user_helper import clear_screen


def add_quiz():

    clear_screen()
    list_quizzes()  # List all quizzes in the database

    """Add a quiz to the database"""
    title = input("Enter the title of the quiz: ")  # Ask for the title of the quiz
    description = input(
        "Enter the description of the quiz: "
    )  # Ask for the description of the quiz

    quiz = Quiz.create(title, description)  # Create the quiz
    clear_screen()
    list_quizzes()  # List all quizzes
    print(f"Quiz: {quiz.title} created successfully.\n")  # Print a success message


def edit_quiz(quiz_id):
    """Edit a quiz in the database"""
    quiz = Quiz.find_by_id(quiz_id)  # Find the quiz by its ID
    title = input(f"Enter the new title for {quiz.title}: ")  # Ask for the new title
    description = input(
        f"Enter the new description for {quiz.title}: "
    )  # Ask for the new description

    quiz.title = title  # Set the new title
    quiz.description = description  # Set the new description
    quiz.update()  # Update the quiz
    clear_screen()
    list_quizzes()  # List all quizzes
    print(f"Quiz: {quiz.title} updated successfully.\n")  # Print a success message


def delete_quiz(quiz_id):
    """Delete a quiz from the database"""
    quiz = Quiz.find_by_id(quiz_id)  # Find the quiz by its ID
    quiz.delete()  # Delete the quiz
    clear_screen()
    list_quizzes()  # List all quizzes
    print(f"Quiz: {quiz.title} deleted successfully.\n")  # Print a success message


def list_quizzes_and_select_quiz():
    """List all quizzes and prompt the user to select a quiz"""
    quizzes = Quiz.get_all()
    quiz_options = [(quiz.title, quiz.id) for quiz in quizzes]

    clear_screen()
    print("List of Quizzes:\n")

    # Display the quizzes
    for i, option in enumerate(quiz_options, start=1):
        print(f"{i}. {option[0]}\n")

    # Prompt the user to select a quiz
    questions = [
        inquirer.Text(
            "quiz_id",
            message="Enter the number of the Quiz you want to select",
            validate=lambda _, x: x.isdigit()
            and 1 <= int(x) <= len(quiz_options),  # Validate the input
        )
    ]
    answers = inquirer.prompt(questions)
    selected_quiz_id = quiz_options[int(answers["quiz_id"]) - 1][1]  # Get the quiz ID

    return selected_quiz_id


def list_quizzes():
    """List all quizzes in the database"""
    quizzes = Quiz.get_all()  # Get all quizzes from the database
    print("List of Quizzes:\n")
    for quiz in quizzes:
        i = quizzes.index(quiz) + 1  # Get the index of the quiz
        print(f"{i}. {quiz.title}\n")  # Print the quiz's title
    return quizzes


def get_quiz(quiz_id):
    quiz = Quiz.find_by_id(quiz_id)
    return quiz
