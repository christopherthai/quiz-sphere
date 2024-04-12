# lib/models/score.py
from matplotlib import pyplot as plt
from sqlalchemy import select, join, func

from __init__ import CURSOR, CONN
from user import User
from quiz import Quiz
from question import Question
from answer import Answer

class Score:
    all = {}
    
    def __init__(self, score, date_taken, user_id, quiz_id):
        self.score = score
        self.date_taken = date_taken
        self.user_id = user_id
        self.quiz_id = quiz_id
        
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def date_taken(self):
        return self._date_taken

    @date_taken.setter
    def date_taken(self, value):
        self._date_taken = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def quiz_id(self):
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, value):
        self._quiz_id = value

        
        
# user can return user scores on all taken quizzes.  This will be the highest score earned on the quiz.
# the user then can select a quiz to show more info for each quiz
# user can see a graph showing their score to the average score on selected quiz by other users
# user can see a list of a selected quiz with correct answers labelled correct and incorrect answers labelled incorrect
# user can see a list which shows list of questions and percentage of correct answers from a selected quiz

    @staticmethod
    def get_user_scores(user_id):
        user_scores = []
        # Join scores table with quizzes table to get quiz names
        query = select([Score, Quiz.name, Score.date_taken]).select_from(join(Score, Quiz, Score.quiz_id == Quiz.id)).where(Score.user_id == user_id)
        result = CURSOR.execute(query)
        for row in result:
            # Calculate the score by querying the Answer table
            score_query = select([func.sum(Answer.is_correct)]).where(Answer.quiz_id == row[Score.quiz_id])
            score_result = CURSOR.execute(score_query).fetchone()
            score = score_result[0] if score_result[0] is not None else 0
            # Store the scores, quiz names, and date taken in a tuple
            user_scores.append((score, row[Quiz.name], row[Score.date_taken], row[Score.quiz_id]))
        return user_scores
    
    @staticmethod
    def get_average_score(quiz_id):
        # Query the database to calculate the average score for the quiz
        score_query = select([func.avg(Answer.is_correct)]).where(Answer.quiz_id == quiz_id)
        result = CURSOR.execute(score_query).fetchone()
        average_score = result[0] if result[0] is not None else 0  # If no scores are found, default to 0
        return average_score

    @staticmethod
    def compare_with_average(quiz_id, user_score):
        # Get the average score for the quiz
        average_score = Score.get_average_score(quiz_id)
        # Compare user's score with the average score
        if user_score > average_score:
            return f"Your score ({user_score}) is higher than the average score of {average_score}.", average_score, user_score
        elif user_score < average_score:
            return f"Your score ({user_score}) is lower than the average score of {average_score}.", average_score, user_score
        else:
            return f"Your score ({user_score}) is equal to the average score of {average_score}.", average_score, user_score

    @staticmethod
    def print_quiz_details(quiz_id):
        # Query the database to retrieve quiz details, including questions and answers
        query = select([Quiz.name, Score.date_taken, Question, Answer]).select_from(
            Quiz.join(Question, Quiz.id == Question.quiz_id).join(Answer, Question.id == Answer.question_id)
        ).where(Quiz.id == quiz_id)
        result = CURSOR.execute(query)
        
        # Print quiz name and date taken
        quiz_info = result.fetchone()  # Assuming one row contains quiz name and date taken
        print(f"Quiz: {quiz_info[Quiz.name]}")
        print(f"Date Taken: {quiz_info[Score.date_taken]}\n")

        # Print quiz details
        for row in result:
            print(f"Question: {row[Question.question_text]}")
            print("Options:")
            # Print options
            for answer_row in result:
                is_correct = answer_row[Answer.is_correct]
                option = answer_row[Answer.option_text]
                print(f"{'[Correct]' if is_correct else '[Incorrect]'} {option}")
            print()


    @staticmethod
    def get_scores_for_quiz(quiz_id):
        # Query the database to retrieve all scores for the quiz
        score_query = select([func.sum(Answer.is_correct)]).where(Answer.quiz_id == quiz_id)
        result = CURSOR.execute(score_query)
        scores = [row[0] for row in result]
        return scores
    
    @staticmethod
    def plot_score_comparison(quiz_id, user_score):
        # Get all scores for the quiz
        all_scores = Score.get_scores_for_quiz(quiz_id)
        
        # Plotting
        plt.hist(all_scores, bins=10, alpha=0.5, label='All Scores')
        plt.axvline(user_score, color='red', linestyle='dashed', linewidth=1, label='Your Score')
        plt.xlabel('Score')
        plt.ylabel('Frequency')
        plt.title('Score Comparison')
        plt.legend()
        plt.show()

    @staticmethod
    def get_correct_answers_percentage(quiz_id):
        # Query the database to calculate the percentage of correct answers for each question in the quiz
        query = select([
            Question.id,
            Question.question_text,
            func.avg(Answer.is_correct).label('percentage_correct')
        ]).select_from(
            Question.join(Score, Question.id == Score.quiz_id)
        ).where(
            Score.quiz_id == quiz_id
        ).group_by(
            Question.id
        )
        result = CURSOR.execute(query)
        return result.fetchall()

    @staticmethod
    def get_percentage_correct_list(quiz_id):
        # Get percentage of correct answers for each question
        result = Score.get_correct_answers_percentage(quiz_id)

        # Create a list containing the question number, question text, and percentage correct value
        percentage_correct_list = []
        for row in result:
            percentage_correct_list.append({
                'question_number': row[Question.id],
                'question_text': row[Question.question_text],
                'percentage_correct': row['percentage_correct']
            })
        return percentage_correct_list
