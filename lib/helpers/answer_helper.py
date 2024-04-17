import inquirer
from models.answer import Answer
from models.question import Question
from helpers.user_helper import clear_screen
from helpers.question_helper import list_specific_question


# Add an answer to the database
def add_answer(selected_question_id):
    """Add an answer to the database"""
    clear_screen()
    list_specific_question(selected_question_id)
    list_answers(selected_question_id)  # List all answers in the database
    content = input("Enter the answer's content: ")
    is_correct = input("Is this the new correct answer? (y/n): ")
    while is_correct.lower() not in ["y", "n"]:
        print("Invalid input. Please enter 'y' or 'n'.\n")
        is_correct = input("Is this the new correct answer? (y/n): ")
    is_correct = 1 if is_correct.lower() == "y" else 0
    question_id = selected_question_id  # Get the question_id from the selected question
    answer = Answer.create(content, is_correct, question_id)  # Create the answer
    clear_screen()
    list_specific_question(selected_question_id)
    list_answers(selected_question_id)
    print("Answer created successfully\n")

    return answer


# Edit an answer in the database
def edit_answer(selected_answer_id):
    """Edit an answer in the database"""
    answer = Answer.find_by_id(selected_answer_id)  # Find the answer by its ID
    content_value = input(
        "Enter the new content: "
    )  # Ask the user to enter the new content
    is_correct = input("Is this the new correct answer? (y/n): ")
    while is_correct.lower() not in ["y", "n"]:
        print("Invalid input. Please enter 'y' or 'n'.\n")
        is_correct = input("Is this the new correct answer? (y/n): ")
    is_correct = 1 if is_correct.lower() == "y" else 0
    answer.content = content_value  # Set the new content
    answer.is_correct = is_correct  # Set the new is_correct
    answer.update()  # Update the answer in the database
    clear_screen()
    list_specific_question(answer.question_id)
    list_answers(answer.question_id)
    print("Answer updated successfully\n")


# Delete an answer from the database
def delete_answer(selected_answer_id, selected_question_id):
    """Delete an answer from the database"""
    id_ = input("Enter the answer's id: ")
    if answer := Answer.find_by_id(id_):
        answer.delete()
        print(f"Answer {id_} deleted")
    else:
        print(f"Answer {id_} not found")

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


def list_answers_and_select_answer(selected_question_id):
    """List all answers of the selected question and prompt the user to select an answer"""
    clear_screen()
    list_specific_question(selected_question_id)
    question = Question.find_by_id(selected_question_id)
    answers = question.get_answers()  # Get all answers of the selected question
    answer_options = [
        (answer.content, answer.id) for answer in answers
    ]  # Create a list of answer options in the format (answer_content, answer_id)

    print("List of Answers:\n")

    # Display the answers
    for i, option in enumerate(answer_options, start=1):
        print(f"{i}. {option[0]}\n")

    # Ask the user to select an answer
    questions = [
        inquirer.Text(
            "answer_id",
            message="Enter the number of the answer you want to select",
            validate=lambda _, x: x.isdigit()  # Check if the input is a number
            and 1
            <= int(x)
            <= len(
                answer_options
            ),  # Check if the input is within the range of the answer options
        )
    ]

    # Get the selected answer ID
    answer = inquirer.prompt(questions)
    selected_answer_id = answer_options[int(answer["answer_id"]) - 1][
        1
    ]  # Get the selected answer ID from the answer options by index

    return selected_answer_id
