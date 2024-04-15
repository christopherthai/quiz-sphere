from matplotlib import pyplot as plt
from sqlalchemy import select, func

from models.__init__ import CURSOR
from models.user import User
from models.quiz import Quiz
from models.question import Question
from models.answer import Answer
from models.score import Score

# from models.user import get_all_quizzes_and_scores, get_quiz_score


def get_user_scores(user):
    """Get the users scores"""

    quizzes_scores = user.get_all_quizzes_and_scores()

    return quizzes_scores


def get_average_scores(quiz_id, user):
    """Get average score from all users for given quiz"""
    # score_query = select([func.avg(Answer.is_correct)]).where(Answer.quiz_id == quiz_id)
    # result = CURSOR.execute(score_query).fetchone()
    quiz = Quiz.find_by_id(quiz_id)

    average_score = quiz.get_average_score()
    user_score = user.get_quiz_score(quiz) 
    
    return user_score, average_score


def compare_with_average(average_score, user_score):
    user_score_value = user_score.score
    """Compares users average with all other users average"""
    if user_score_value > average_score:
        return (
            f"Your score ({user_score_value}) is higher than the average score of {average_score}.",
            average_score,
            user_score_value,
        )
    elif user_score_value < average_score:
        return (
            f"Your score ({user_score_value}) is lower than the average score of {average_score}.",
            average_score,
            user_score_value,
        )
    else:
        return (
            f"Your score ({user_score_value}) is equal to the average score of {average_score}.",
            average_score,
            user_score_value,
        )


def print_quiz_details_user(quiz_id, user):
    """Prints quiz details with incorrect and correct listed next to the question"""
    result = user.print_quiz_details(quiz_id)

    return result


def get_scores_for_quiz(quiz):
    """Returns the scores for a given quiz"""
    # score_query = select([func.sum(Answer.is_correct)]).where(Answer.quiz_id == quiz_id)
    # result = CURSOR.execute(score_query)
    # scores = [row[0] for row in result]
    scores = quiz.get_scores()
    return scores


def plot_score_comparison(quiz, user):
    """Plots results of users score against other users scores"""
    all_scores = get_scores_for_quiz(quiz)

    all_scores = [score.score for score in all_scores]


    user_score = user.get_quiz_score(quiz).score

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
