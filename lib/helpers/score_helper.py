from matplotlib import pyplot as plt
from sqlalchemy import select, func

from models.__init__ import CURSOR
from models.quiz import Quiz
from models.score import Score


# prints out the users scores and quizzes when they enter the scores menu
def get_user_scores(user):
    """Get the users scores"""

    quizzes_scores = user.get_all_quizzes_and_scores()

    return quizzes_scores


# Function to get/store the average score for all users and the users score for given quiz
def get_average_scores(quiz_id, user):
    """Get average score from all users for given quiz"""

    quiz = Quiz.find_by_id(quiz_id)

    average_score = quiz.get_average_score()
    user_score = user.get_quiz_score(quiz)
    return user_score, average_score


# Prints statement comparing user score vs average score
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


# Returns all scores for all quizzes
def get_scores_for_quiz(quiz):
    """Returns the scores for a given quiz"""

    scores = quiz.get_scores()
    return scores


# #Plots histogram with users score against other scores
# def plot_score_comparison(quiz, user):
#     """Plots results of users score against other users scores"""
#     all_scores = get_scores_for_quiz(quiz)

#     all_scores = [score.score for score in all_scores]

#     user_score = user.get_quiz_score(quiz).score

#     plt.hist(all_scores, bins=10, alpha=0.5, label="All Scores")
#     plt.axvline(
#         user_score, color="red", linestyle="dashed", linewidth=1, label="Your Score"
#     )
#     plt.xlabel("Score")
#     plt.ylabel("Frequency")
#     plt.title("Score Comparison")
#     plt.legend()
#     plt.show()


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
