from lib.models.question import Question

def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the question functions in this lesson

def list_questions():
    questions = Question.get_all()
    for question in questions:
        print(question)

def find_question_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the question's id: ")
    question = Question.find_by_id(id_)
    print(question) if question else print(f'Question {id_} not found')

def create_question():
    content = input("Enter the question's content: ")
    quiz_id = input("Enter the question's quiz_id: ")
    try:
        question = Question.create(content, quiz_id)
        print(f'Success: {question}')
    except Exception as exc:
        print("Error creating question: ", exc)


def update_question():
    id_ = input("Enter the question's id: ")
    if question := Question.find_by_id(id_):
        try:
            content = input("Enter the question's new content: ")
            question.content = content
            quiz_id = input("Enter the question's quiz_id: ")
            question.quiz_id = quiz_id

            question.update()
            print(f'Success: {question}')
        except Exception as exc:
            print("Error updating question: ", exc)
    else:
        print(f'Question {id_} not found')


def delete_question():
    id_ = input("Enter the question's id: ")
    if question := Question.find_by_id(id_):
        question.delete()
        print(f'Question {id_} deleted')
    else:
        print(f'Question {id_} not found')