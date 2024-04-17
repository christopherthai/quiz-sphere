from models.user_answer import User_Answer


# List all answers in the database
def list_user_answers():
    """List all user answers in the database"""
    user_answers = User_Answer.get_all()  # Get all answers in the database
    for user_answer in user_answers:  # Loop through the answers
        print(user_answer)  # Print the answer


# Find an answer by its ID
def find_user_answer_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the answer's id: ")
    user_answer = User_Answer.find_by_id(id_)
    print(user_answer) if user_answer else print(f"Answer {id_} not found")
