from lib.models.answer import Answer


def exit_program():
    print("Goodbye!")
    exit()


# We'll implement the answer functions in this lesson


# List all answers in the database
def list_answers():
    """List all answers in the database"""
    answers = Answer.get_all()  # Get all answers in the database
    for answer in answers:  # Loop through the answers
        print(answer)  # Print the answer


# Find an answer by its ID
def find_answer_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the answer's id: ")
    answer = Answer.find_by_id(id_)
    print(answer) if answer else print(f"Answer {id_} not found")


# Add an answer to the database
def create_answer():
    """Add an answer to the database"""
    content = input("Enter the answer's content: ")
    is_correct = input("Enter the answer's is_correct: ")
    question_id = input("Enter the answer's question_id: ")
    try:
        answer = Answer.create(content, is_correct, question_id)
        print(f"Success: {answer}")
    except Exception as exc:
        print("Error creating answer: ", exc)


# Edit an answer in the database
def update_answer():
    """Edit an answer in the database"""
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
            print(f"Success: {answer}")
        except Exception as exc:
            print("Error updating answer: ", exc)
    else:
        print(f"Answer {id_} not found")


# Delete an answer from the database
def delete_answer():
    """Delete an answer from the database"""
    id_ = input("Enter the answer's id: ")
    if answer := Answer.find_by_id(id_):
        answer.delete()
        print(f"Answer {id_} deleted")
    else:
        print(f"Answer {id_} not found")
        
        

