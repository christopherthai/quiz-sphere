from lib.models.answer import Answer 

def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the answer functions in this lesson

def list_questions():
    answers = Answer.get_all()
    for answer in answers:
        print(answer)
        # 질문에 관련된 답변만 보이게 해야한다


def find_answer_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the answer's id: ")
    answer = Answer.find_by_id(id_)
    print(answer) if answer else print(f'Answer {id_} not found')


def create_answer():
    content = input("Enter the answer's content: ")
    is_correct = input("Enter the answer's is_correct: ")
    question_id = input("Enter the answer's question_id: ")
    try:
        answer = Answer.create(content, is_correct, question_id)
        print(f'Success: {answer}')
    except Exception as exc:
        print("Error creating answer: ", exc)


def update_answer():
    id_ = input("Enter the answer's id: ")
    if answer := Answer.find_by_id(id_):
        try:
            content = input("Enter the answer's new content: ")
            answer.content = content
            is_correct = input("Enter the answer's new is_correct: ")
            answer.is_correct = is_correct
            question_id = input("Enter the answer's new question_id: ")
            answer.question_id = question_id

            answer.update()
            print(f'Success: {answer}')
        except Exception as exc:
            print("Error updating answer: ", exc)
    else:
        print(f'Answer {id_} not found')


def delete_answer():
    id_ = input("Enter the answer's id: ")
    if answer := Answer.find_by_id(id_):
        answer.delete()
        print(f'Answer {id_} deleted')
    else:
        print(f'Answer {id_} not found')