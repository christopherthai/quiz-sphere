from matplotlib import pyplot as plt
from sqlalchemy import select, func

from models.__init__ import CURSOR
from models.user import User
from models.quiz import Quiz
from models.question import Question
from models.answer import Answer
from models.score import Score

from models.user import get_all_quizzes_and_scores, get_quiz_score
from models.quiz import get_average_score, print_quiz_details, get_scores



def get_user_scores(user_id):
    """Get the users scores"""
    user_scores = []
    
    quiz_scores = get_all_quizzes_and_scores(User(user_id))
    
    # Assuming quiz_scores returns a list of tuples in the format (Quiz, Score)
    for quiz, score in quiz_scores:
        user_scores.append((score, quiz.title, score.date_taken, quiz.id))
    
        
    return user_scores


def get_average_scores(quiz_id):
    """Get average score from all users for given quiz"""
    # score_query = select([func.avg(Answer.is_correct)]).where(Answer.quiz_id == quiz_id)
    # result = CURSOR.execute(score_query).fetchone()

    result = get_average_score(Quiz(quiz_id))
    
    average_score = result[0] if result[0] is not None else 0
    return average_score


def compare_with_average(quiz_id, user_score):
    """Compares users average with all other users average"""
    average_score = Score.get_average_scores(quiz_id)
    if user_score > average_score:
        return (
            f"Your score ({user_score}) is higher than the average score of {average_score}.",
            average_score,
            user_score,
        )
    elif user_score < average_score:
        return (
            f"Your score ({user_score}) is lower than the average score of {average_score}.",
            average_score,
            user_score,
        )
    else:
        return (
            f"Your score ({user_score}) is equal to the average score of {average_score}.",
            average_score,
            user_score,
        )


def print_quiz_details_user(quiz_id):
    """Prints quiz details with incorrect and correct listed next to the question"""
    result = print_quiz_details(Quiz(quiz_id))
    
    return result


def get_scores_for_quiz(quiz_id):
    """Returns the scores for a given quiz"""
    # score_query = select([func.sum(Answer.is_correct)]).where(Answer.quiz_id == quiz_id)
    # result = CURSOR.execute(score_query)
    # scores = [row[0] for row in result]
    scores = get_scores(Quiz(quiz_id))
    return scores


def plot_score_comparison(quiz_id, user_id):
    """Plots results of users score against other users scores"""
    all_scores = get_scores_for_quiz(quiz_id)
    
    user_score = get_quiz_score(User(user_id))

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
