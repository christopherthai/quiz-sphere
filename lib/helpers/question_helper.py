from models.question import Question
from models.quiz import Quiz


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
    print(f"Question: {question} created successfully")


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


# def delete_question(selected_quiz_id):
#     """Delete a question from the database"""
#     quiz = Quiz.find_by_id(selected_quiz_id)


def list_questions_and_answers_of_the_quiz(selected_quiz_id):
    """List all questions of the selected quiz"""
    quiz = Quiz.find_by_id(selected_quiz_id)
    questions_and_answers = quiz.get_questions_and_answers()
    
    for question in questions_and_answers:
        print(f"Question: {question.content}")
        print("Answers:")
        for answer in question.answers:
            print(f"Answer: {answer.content} - Correct: {answer.is_correct}")
        print()

    return questions_and_answers
