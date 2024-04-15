import inquirer
from models.quiz import Quiz


def create_quiz(title):
    print(f"Quiz titled '{title}' created successfully.")


def delete_quiz(quiz_id):
    print(f"Quiz with ID {quiz_id} has been deleted.")


def list_quizzes():
    """List all the quizzes in the database"""
    quizzes = Quiz.get_all()
    quiz_options = [(quiz.title, quiz.id) for quiz in quizzes]

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

    print(f"You selected Quiz ID: {selected_quiz_id}")
