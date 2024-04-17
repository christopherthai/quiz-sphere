import inquirer
from models.question import Question
from models.quiz import Quiz
from helpers.user_helper import clear_screen
from helpers.quiz_helper import list_specific_quiz
from models.user_answer import User_Answer


# Call the edit_question function
def find_question_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the question's id: ")
    question = Question.find_by_id(id_)
    print(question) if question else print(f"Question {id_} not found")


# Add a question to the database
def add_question(selected_quiz_id):
    """Add a question to the database"""
    clear_screen()
    list_specific_quiz(selected_quiz_id)
    list_questions(selected_quiz_id)  # List all questions in the database
    content = input("Enter the question's content: ")
    quiz_id = selected_quiz_id  # Get the quiz_id from the selected quiz
    question = Question.create(content, quiz_id)  # Create the question
    clear_screen()
    list_specific_quiz(selected_quiz_id)
    list_questions(selected_quiz_id)
    print("Question created successfully\n")

    return question


# Edit a question in the database
def edit_question(selected_question_id, selected_quiz_id):
    """Edit a question in the database"""
    clear_screen()
    list_specific_question(selected_question_id)
    question = Question.find_by_id(selected_question_id)  # Find the question by its ID
    content_value = input(
        "Enter the new content: "
    )  # Ask the user to enter the new content
    question.content = content_value  # Update the content of the question
    question.update()  # Update the question in the database
    clear_screen()
    print("Question updated successfully\n")


# Delete a question from the database
def delete_question(selected_question_id, selected_quiz_id):
    """Delete a question from the database"""
    question = Question.find_by_id(selected_question_id)  # Find the question by its ID
    question.delete_question_and_answers()  # Delete the question and its answers from the database
    clear_screen()
    list_questions(selected_quiz_id)
    print("Question deleted successfully\n")


# List all questions of the selected quiz
def list_questions(selected_quiz_id):
    """List all questions of the selected quiz"""

    quiz = Quiz.find_by_id(selected_quiz_id)
    questions = quiz.get_questions()  # Get all questions of the selected quiz

    print("List of Questions:\n")

    # Display the questions
    for question in questions:
        print(f"{questions.index(question) + 1}. {question.content}\n")

    return questions


# List all questions of the selected quiz and prompt the user to select a question
def list_questions_and_answers_of_the_quiz(selected_quiz_id):
    """List all questions of the selected quiz"""
    quiz = Quiz.find_by_id(selected_quiz_id)
    questions_and_answers = quiz.get_questions_and_answers()

    return questions_and_answers


def list_questions_and_select_question(selected_quiz_id):
    """List all questions of the selected quiz and prompt the user to select a question"""
    clear_screen()
    list_specific_quiz(selected_quiz_id)
    questions = list_questions_and_answers_of_the_quiz(selected_quiz_id)
    question_options = [(question.content, question.id) for question in questions] # Create a list of question options in the format (question_content, question_id)

    print("List of Questions:\n")

    # Display the questions
    for i, option in enumerate(question_options, start=1):
        print(f"{i}. {option[0]}\n")

    # Ask the user to select a question
    questions = [
        inquirer.Text(
            "question_id",
            message="Enter the question's number you want to select",
            validate=lambda _, response: response.isdigit()  # Check if the input is a number
            and 1
            <= int(response)
            <= len(
                question_options
            ),  # And if the input is within the range of the question_options
        )
    ]

    answer = inquirer.prompt(questions)
    selected_question_id = question_options[int(answer["question_id"]) - 1][1] # Get the selected question ID from the question options by index

    return selected_question_id


def get_user_answers_for_question(user, selected_question_id):
    """Get user answer for a question"""

    # Retrieve the user's answer from the User_Answers table
    user_answer = User_Answer.find_by_user_and_question(user.id, selected_question_id)
    if user_answer:
        return user_answer.user_answer
    else:
        print("User's answer not found.")
        return None


def list_specific_question(selected_question_id):
    """List a specific question in the database"""
    question = Question.find_by_id(selected_question_id)  # Find the question by its ID
    print(f"Question: {question.content}\n")  # Print the question's content
    return question
