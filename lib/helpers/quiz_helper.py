import inquirer
from lib.models.quiz import Quiz

def create_quiz(title):
    print(f"Quiz titled '{title}' created successfully.")


def delete_quiz(quiz_id):
    print(f"Quiz with ID {quiz_id} has been deleted.")


def list_quizzes():
    """List all the quizzes in the database"""
    quizzes = Quiz.get_all()
    quiz_options = []
    for quiz in quizzes:
        quiz_options.append(
            {"name": f"Quiz ID: {quiz.id}, Title: {quiz.title}", "value": quiz.id}
        )
    questions = [
        inquirer.List("quiz_id", message="Select a quiz:", choices=quiz_options)
    ]
    answers = inquirer.prompt(questions)
    selected_quiz_id = answers["quiz_id"]
    print(f"You selected Quiz ID: {selected_quiz_id}")