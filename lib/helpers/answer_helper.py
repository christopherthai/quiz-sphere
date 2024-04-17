import inquirer
from models.answer import Answer
from models.question import Question
from helpers.user_helper import clear_screen
from helpers.question_helper import list_specific_question


# Add an answer to the database
def add_answer(selected_question_id):
    """Add an answer to the database"""
    content = input("Enter the answer's content: ")
    is_correct = input("Enter the answer's is_correct: ")
    question_id = selected_question_id  # Get the question_id from the selected question
    answer = Answer.create(content, is_correct, question_id)  # Create the answer
    clear_screen()
    list_specific_question(selected_question_id)
    list_answers(selected_question_id)
    print("Answer created successfully")

    return answer


# Edit an answer in the database
def edit_answer(selected_answer_id):
    """Edit an answer in the database"""
    answer = Answer.find_by_id(selected_answer_id)  # Find the answer by its ID
    content = input("Enter the new content: ")  # Ask the user to enter the new content
    is_correct = input("Enter the new is_correct (yes/no): ")
    while is_correct.lower() not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        is_correct = input("Enter the new is_correct (yes/no): ")
    answer.update(content, is_correct)  # Update the content of the answer
    clear_screen()
    list_specific_question(answer.question_id)
    list_answers(answer.question_id)
    print("Answer updated successfully\n")


# Delete an answer from the database
def delete_answer(selected_answer_id, selected_question_id):
    """Delete an answer from the database"""
    answer = Answer.find_by_id(selected_answer_id)  # Find the answer by its ID
    answer.delete()  # Delete the answer from the database
    clear_screen()
    list_specific_question(selected_question_id)
    list_answers(selected_question_id)
    print("Answer deleted successfully\n")


def list_answers(selected_question_id):
    """List all answers of the selected question"""

    question = Question.find_by_id(selected_question_id)
    answers = question.get_answers()  # Get all answers of the selected question

    print("List of Answers:\n")

    # Display the answers
    for answer in answers:
        print(f"{answers.index(answer) + 1}. {answer.content}\n")

    return answers


def list_answers_and_select_answer(selected_question_id):
    """List all answers of the selected question and prompt the user to select an answer"""
    answers = list_answers(selected_question_id)
    answer_options = [
        (answer.content, answer.id) for answer in answers
    ]  # Get the answer options

    print("List of Answers:\n")

    # Display the answers
    for i, option in enumerate(answer_options, start=1):
        print(f"{i}. {option[0]}\n")

    # Ask the user to select an answer
    questions = [
        inquirer.Text(
            "answer_id",
            message="Enter the ID of the answer you want to select",
            validate=lambda _, x: x.isdigit()  # Check if the input is a number
            and 1
            <= int(x)
            <= len(
                answer_options
            ),  # Check if the input is within the range of the answer options
        )
    ]

    answer = inquirer.prompt(questions)
    selected_answer_id = answer_options[int(answer["answer_id"]) - 1][1]

    return selected_answer_id
