from matplotlib import pyplot as plt
from sqlalchemy import select, join, func

from models.__init__ import CURSOR
from models.user import User
from models.quiz import Quiz
from models.question import Question
from models.answer import Answer
from models.score import Score


def get_user_scores(user_id):
    """Get the users scores"""
    user_scores = []
    query = (
        select([Score, Quiz.name, Score.date_taken])
        .select_from(Quiz.join(Score, Score.quiz_id == Quiz.id))
        .where(Score.user_id == user_id)
    )
    result = CURSOR.execute(query)
    for row in result:
        score_query = select([func.sum(Answer.is_correct)]).where(
            Answer.quiz_id == row[Score.quiz_id]
        )
        score_result = CURSOR.execute(score_query).fetchone()
        score = score_result[0] if score_result[0] is not None else 0
        user_scores.append(
            (score, row[Quiz.name], row[Score.date_taken], row[Score.quiz_id])
        )
    return user_scores


def get_average_score(quiz_id):
    """Get average score from all users for given quiz"""
    score_query = select([func.avg(Answer.is_correct)]).where(Answer.quiz_id == quiz_id)
    result = CURSOR.execute(score_query).fetchone()
    average_score = result[0] if result[0] is not None else 0
    return average_score


def compare_with_average(quiz_id, user_score):
    """Compares users average with all other users average"""
    average_score = Score.get_average_score(quiz_id)
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


def print_quiz_details(quiz_id):
    """Prints quiz details with incorrect and correct listed next to the question"""
    query = (
        select([Quiz.name, Score.date_taken, Question, Answer])
        .select_from(
            Quiz.join(Question, Quiz.id == Question.quiz_id).join(
                Answer, Question.id == Answer.question_id
            )
        )
        .where(Quiz.id == quiz_id)
    )
    result = CURSOR.execute(query)
    quiz_info = result.fetchone()
    print(f"Quiz: {quiz_info[Quiz.name]}")
    print(f"Date Taken: {quiz_info[Score.date_taken]}\n")
    for row in result:
        print(f"Question: {row[Question.question_text]}")
        print("Options:")
        for answer_row in result:
            is_correct = answer_row[Answer.is_correct]
            option = answer_row[Answer.option_text]
            print(f"{'[Correct]' if is_correct else '[Incorrect]'} {option}")
        print()


def get_scores_for_quiz(quiz_id):
    """Returns the scores for a given quiz"""
    score_query = select([func.sum(Answer.is_correct)]).where(Answer.quiz_id == quiz_id)
    result = CURSOR.execute(score_query)
    scores = [row[0] for row in result]
    return scores


def plot_score_comparison(quiz_id, user_id):
    """Plots results of users score against other users scores"""
    all_scores = Score.get_scores_for_quiz(quiz_id)
    user_score_query = select([func.sum(Answer.is_correct)]).where(
        Answer.quiz_id == quiz_id, Answer.user_id == user_id
    )
    user_score_result = CURSOR.execute(user_score_query).fetchone()
    user_score = user_score_result[0] if user_score_result[0] is not None else 0

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
#     query = (
#         select(
#             [
#                 Question.id,
#                 Question.question_text,
#                 func.avg(Answer.is_correct).label("percentage_correct"),
#             ]
#         )
#         .select_from(Question.join(Score, Question.id == Score.quiz_id))
#         .where(Score.quiz_id == quiz_id)
#         .group_by(Question.id)
#     )
#     result = CURSOR.execute(query)
#     return result.fetchall()


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
