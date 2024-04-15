import inquirer
from models.question import Question
from models.quiz import Quiz
from helpers.user_helper import clear_screen
from helpers.quiz_helper import list_specific_quiz


def find_question_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the question's id: ")
    question = Question.find_by_id(id_)
    print(question) if question else print(f"Question {id_} not found")


def add_question(selected_quiz_id):
    """Add a question to the database"""
    content = input("Enter the question's content: ")
    quiz_id = selected_quiz_id
    question = Question.create(content, quiz_id)
    clear_screen()
    list_specific_quiz(selected_quiz_id)
    list_questions(selected_quiz_id)
    print("Question created successfully")


def update_question():
    """Edit a question in the database"""
    id_ = input("Enter the question's id: ")
    if question := Question.find_by_id(id_):
        try:
            content = input("Enter the question's new content: ")
            question.content = content
            quiz_id = input("Enter the question's quiz_id: ")
            question.quiz_id = quiz_id

            question.update()
            print(f"Success: {question}")
        except Exception as exc:
            print("Error updating question: ", exc)
    else:
        print(f"Question {id_} not found")


def delete_question(selected_question_id, selected_quiz_id):
    """Delete a question from the database"""
    question = Question.find_by_id(selected_question_id)
    question.delete_question_and_answers()
    clear_screen()
    list_questions(selected_quiz_id)
    print("Question deleted successfully\n")


def list_questions(selected_quiz_id):
    """List all questions of the selected quiz"""

    quiz = Quiz.find_by_id(selected_quiz_id)
    questions = quiz.get_questions()

    print("List of Questions:\n")

    for question in questions:
        print(f"{questions.index(question) + 1}. {question.content}\n")

    return questions


def list_questions_and_answers_of_the_quiz(selected_quiz_id):
    """List all questions of the selected quiz"""
    quiz = Quiz.find_by_id(selected_quiz_id)
    questions_and_answers = quiz.get_questions_and_answers()

    # for question in questions_and_answers:
    #     print(f"Question: {question.content}")
    #     print("Answers:")
    #     for answer in question.answers:
    #         print(f"Answer: {answer.content} - Correct: {answer.is_correct}")
    #     print()

    return questions_and_answers


def list_questions_and_select_question(selected_quiz_id):
    """List all questions of the selected quiz and prompt the user to select a question"""
    clear_screen()
    questions = list_questions_and_answers_of_the_quiz(selected_quiz_id)
    question_options = [(question.content, question.id) for question in questions]

    print("List of Questions:\n")

    for i, option in enumerate(question_options, start=1):
        print(f"{i}. {option[0]}\n")

    questions = [
        inquirer.Text(
            "question_id",
            message="Enter the question's id",
            validate=lambda _, response: response.isdigit()
            and 1 <= int(response) <= len(question_options),
        )
    ]

    answer = inquirer.prompt(questions)
    selected_question_id = question_options[int(answer["question_id"]) - 1][1]

    return selected_question_id
