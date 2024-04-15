from matplotlib import pyplot as plt
from sqlalchemy import select, func

from models.__init__ import CURSOR
from models.user import User
from models.quiz import Quiz
from models.question import Question
from models.answer import Answer
from models.score import Score

# from models.user import get_all_quizzes_and_scores, get_quiz_score
<<<<<<< HEAD


def get_user_scores(user):
    """Get the users scores"""

    user_scores = []

    quizzes_scores = user.get_all_quizzes_and_scores()
    for quiz, score in quizzes_scores:
        print(f"Quiz: {quiz}, Score: {score}")
=======
# from models.quiz import get_average_score, print_quiz_details, get_scores



def get_user_scores(user):
    """Get the users scores"""
    # user_scores = []
    
    quiz_scores = user.get_all_quizzes_and_scores()
    
    # Assuming quiz_scores returns a list of tuples in the format (Quiz, Score)
    # for quiz, score in quiz_scores:
    #     user_scores.append((score, quiz.title, score.date_taken, quiz.id))
    
        
    return quiz_scores
>>>>>>> development


def get_average_scores(quiz):
    """Get average score from all users for given quiz"""
    # score_query = select([func.avg(Answer.is_correct)]).where(Answer.quiz_id == quiz_id)
    # result = CURSOR.execute(score_query).fetchone()

<<<<<<< HEAD
    result = get_average_score(Quiz(quiz_id))

=======
    result = quiz.get_average_score()
    
>>>>>>> development
    average_score = result[0] if result[0] is not None else 0
    return average_score


def compare_with_average(score):
    """Compares users average with all other users average"""
    average_score = score.get_average_scores()
    # if user_score > average_score:
    #     return (
    #         f"Your score ({user_score}) is higher than the average score of {average_score}.",
    #         average_score,
    #         user_score,
    #     )
    # elif user_score < average_score:
    #     return (
    #         f"Your score ({user_score}) is lower than the average score of {average_score}.",
    #         average_score,
    #         user_score,
    #     )
    # else:
    #     return (
    #         f"Your score ({user_score}) is equal to the average score of {average_score}.",
    #         average_score,
    #         user_score,
    #     )
    return average_score

def print_quiz_details_user(quiz):
    """Prints quiz details with incorrect and correct listed next to the question"""
<<<<<<< HEAD
    result = print_quiz_details(Quiz(quiz_id))

=======
    result = quiz.print_quiz_details()
    
>>>>>>> development
    return result


def get_scores_for_quiz(quiz):
    """Returns the scores for a given quiz"""
    # score_query = select([func.sum(Answer.is_correct)]).where(Answer.quiz_id == quiz_id)
    # result = CURSOR.execute(score_query)
    # scores = [row[0] for row in result]
    scores = quiz.get_scores()
    return scores


def plot_score_comparison(quiz_id, user):
    from models.user import get_quiz_score
    """Plots results of users score against other users scores"""
    all_scores = get_scores_for_quiz(quiz_id)
<<<<<<< HEAD

    user_score = get_quiz_score(User(user_id))
=======
    
    user_score = user.get_quiz_score()
>>>>>>> development

    plt.hist(all_scores, bins=10, alpha=0.5, label="All Scores")
    plt.axvline(
        user_score, color="red", linestyle="dashed", linewidth=1, label="Your Score"
    )
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.title("Score Comparison")
    plt.legend()
    plt.show()


# def get_correct_answers_percentage(quiz_id):
#     """Gets the percentage of correct answers for a given question on a quiz"""
#     ans_percentage =


# def get_percentage_correct_list(quiz_id):
#     """Lists the users taken quiz and add the percentage of correct answers per given question"""
#     result = Score.get_correct_answers_percentage(quiz_id)
#     percentage_correct_list = []
#     for row in result:
#         percentage_correct_list.append(
#             {
#                 "question_number": row[Question.id],
#                 "question_text": row[Question.question_text],
#                 "percentage_correct": row["percentage_correct"],
#             }
#         )
#     return percentage_correct_list
