from lib.models.answer import Answer 

def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the answer functions in this lesson

def list_questions():
    answers = Answer.get_all()
    for answer in answers:
        print(answer)


def find_answer_by_title():
    title = input("Enter the answer's title: ")
    answer = Answer.find_by_title(title)
    print(answer) if answer else print(
        f'Answer {title} not found')


def find_answer_by_id():
    #use a trailing underscore not to override the built-in id function
    id_ = input("Enter the answer's id: ")
    answer = Answer.find_by_id(id_)
    print(answer) if answer else print(f'Answer {id_} not found')


def create_answer():
    title = input("Enter the answer's title: ")
    location = input("Enter the answer's location: ")
    try:
        answer = Answer.create(title, location)
        print(f'Success: {answer}')
    except Exception as exc:
        print("Error creating answer: ", exc)


def update_answer():
    id_ = input("Enter the answer's id: ")
    if answer := Answer.find_by_id(id_):
        try:
            title = input("Enter the answer's new title: ")
            answer.title = title
            location = input("Enter the answer's new location: ")
            answer.location = location

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