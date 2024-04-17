import inquirer
from models.quiz import Quiz
from models.answer import Answer
from models.user import User
from models.user_answer import User_Answer
from helpers.user_helper import clear_screen

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    PURPLE = '\033[95m'
    MAROON = '\033[91m'
    RESET = '\033[0m'


# Add a quiz to the database
def add_quiz():
    """Add a quiz to the database"""
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


# Edit a quiz in the database
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
    # list_quizzes()  # List all quizzes
    print(f"Quiz: {quiz.title} updated successfully.\n")  # Print a success message


# Delete a quiz from the database
def delete_quiz(quiz_id):
    """Delete a quiz from the database"""
    quiz = Quiz.find_by_id(quiz_id)  # Find the quiz by its ID
    quiz.delete_quiz_question_and_answers()  # Delete the quiz, its questions, and answers from the database
    clear_screen()
    list_quizzes()  # List all quizzes
    print(f"Quiz: {quiz.title} deleted successfully.\n")  # Print a success message


# List all quizzes and prompt the user to select a quiz
def list_quizzes_and_select_quiz():
    """List all quizzes and prompt the user to select a quiz"""
    quizzes = Quiz.get_all()
    quiz_options = [(quiz.title, quiz.id) for quiz in quizzes]  # Get the quiz options

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
            validate=lambda _, x: x.isdigit()  # Check if the input is a number
            and 1 <= int(x) <= len(quiz_options),  # Validate the input
        )
    ]

    # Ask the user to select a quiz
    answers = inquirer.prompt(questions)
    selected_quiz_id = quiz_options[int(answers["quiz_id"]) - 1][1]  # Get the quiz ID

    return selected_quiz_id


# List all quizzes in the database
def list_quizzes():
    """List all quizzes in the database"""
    quizzes = Quiz.get_all()  # Get all quizzes from the database
    print("List of Quizzes:\n")
    for quiz in quizzes:
        i = quizzes.index(quiz) + 1  # Get the index of the quiz
        print(f"{i}. {quiz.title}\n")  # Print the quiz's title
    return quizzes


# List a specific quiz in the database
def list_specific_quiz(quiz_id):
    """List a specific quiz in the database"""
    quiz = Quiz.find_by_id(quiz_id)  # Find the quiz by its ID
    print(
        f"Quiz: {quiz.title}\nDescription: {quiz.description}\n"  # Print the quiz's title and description
    )
    return quiz


# Get a quiz by its ID
def get_quiz(quiz_id):
    """Get a quiz by its ID"""
    quiz = Quiz.find_by_id(quiz_id)  # Find the quiz by its ID
    return quiz

def print_quiz_details(quiz, user):
    user_score = User.get_quiz_score(user, quiz)

    """Print the details of the quiz"""
    print("*" * 80)
    print(Color.BLUE + "Quiz Details".center(80) + Color.RESET)
    print("*" * 80)
    print(f"Quiz Title: {quiz.title}".center(80))
    print(f"Date Taken: {user_score.date_taken} \n".center(80))
    print(f"Average Score: {quiz.get_average_score()}")
    
    print(f"Your Score: {user_score.score} \n")
    
    questions = quiz.get_questions_and_answers()
    for question in questions:
        print(f"{Color.BLUE}Question:{Color.RESET} {question.content}")
        
        user_answer = question.get_user_answer()
        # Print the content of the user's answer if available
        if user_answer:
            answer = Answer.find_by_id(user_answer.user_answer)
            is_correct = Color.GREEN + "Correct!" + Color.RESET if answer.is_correct else Color.RED + "Incorrect." + Color.RESET
            overall_percentage = calculate_percentage_correct_for_question(question.id)
            print(f"{is_correct}  Your answer was '{answer.content}'")
            print(f"({Color.PURPLE}{overall_percentage}%{Color.RESET}) of users got this correct.")        
        else:
            print("No answer provided")
            
            
        print("*" * 80)
        print()





        
#Calculate % of correct answers from user answer for question
def calculate_percentage_correct_for_question(question_id):
    """Calculate the percentage of correct answers for a question"""
    # Retrieve all user answers for the given question
    user_answers = User_Answer.find_by_question_id(question_id)
    if not user_answers:
        print("No user answers found for this question.")
        return None

    total_answers = len(user_answers)
    # Retrieve the is_correct values for the user_answer_ids
    is_correct_values = [Answer.find_by_id(answer_id).is_correct for answer_id in user_answers]
    
    correct_answers = sum(is_correct_values)

    # Calculate the percentage of correct answers
    percentage_correct = (correct_answers / total_answers) * 100 if total_answers > 0 else 0.0

    return percentage_correct


