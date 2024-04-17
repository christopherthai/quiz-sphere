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

    # Extract scores and users
    scores = [score.score for score in all_scores]
    users = [score.id for score in all_scores]

    # Get the user's score
    user_score = user.get_quiz_score(quiz).score

    average_score = sum(scores) / len(scores)

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(users, scores, color="blue", label="All Scores")
    plt.scatter(user.id, user_score, color="red", label="Your Score")
    plt.axhline(
        y=average_score, color="red", linestyle="--", linewidth=1, label="Average Grade"
    )

    plt.xlabel("User")
    plt.ylabel("Grade")
    plt.title("Score Comparison")
    plt.legend()
    plt.xticks([], [])  # Rotate x-axis labels for better readability
    plt.grid(True)  # Show grid lines
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()


# Add a score to the database
def submit_score(score, date_taken, user, quiz_id):
    """Add a score to the database"""
    quiz = Quiz.find_by_id(quiz_id)
    if user.get_quiz_score(quiz):  # if the user has already taken the quiz
        return update_score(score, date_taken, user, quiz_id)  # update the score
    score = Score.create(score, date_taken, user.id, quiz_id)  # create a new score
    return score


# Update a score in the database
def update_score(score_value, date_taken, user, quiz_id):
    """Update a score in the database"""
    quiz = Quiz.find_by_id(quiz_id)  # quiz instance
    score = user.get_quiz_score(quiz)  # score instance
    score.score = score_value  # setting the score value
    score.date_taken = date_taken
    score.update()
    return score