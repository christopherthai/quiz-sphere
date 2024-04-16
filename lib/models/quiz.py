from models.__init__ import CURSOR, CONN
from models.score import Score
from models.question import Question
from models.answer import Answer



class Quiz:

    # Class attribute that stores all the instances of the Quiz
    all = {}

    def __init__(self, title, description, id=None):
        self.title = title
        self.description = description
        self.id = id
        type(self).all[title] = self

    # Method that returns representation of the object
    def __repr__(self):
        return f"<Quiz {self.id}: {self.title}" + f"Description: {self.description}>"

    # Property method that returns the title
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    # Property method that returns the description
    @property
    def description(self):
        return self._description

    # Property method that sets the description
    @description.setter
    def description(self, value):
        self._description = value

    # Insert a new record into the Quizzes table with the attributes of the Quiz instance
    def save(self):
        """Save the instance of the Quiz to the database"""
        sql = """
        INSERT INTO Quizzes (title, description) VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.title, self.description))  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database
        self.id = CURSOR.lastrowid  # Set the id of the instance to the last row id

    # Update the record in the Quizzes table with the attributes of the Quiz instance
    def update(self):
        """Update the instance of the Quiz in the database"""
        sql = """
        UPDATE Quizzes SET title = ?, description = ? WHERE id = ?
        """
        CURSOR.execute(
            sql, (self.title, self.description, self.id)
        )  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    # Delete the record in the Quizzes table with the attributes of the Quiz instance
    def delete(self):
        """Delete the instance of the Quiz from the database"""
        sql = """
        DELETE FROM Quizzes WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,)) # Execute the SQL statement
        CONN.commit() # Commit the changes to the database

    # Class method that creates a new instance of the Quiz
    @classmethod
    def create(cls, title, description):
        """Create a new instance of the Quiz"""
        quiz = cls(title, description)  # Create a new instance of the Quiz
        quiz.save()  # Save the instance to the database
        return quiz  # Return the instance

    # Class method that creates a new instance of the Quiz from a database row
    @classmethod
    def instance_from_db_row(cls, row):
        """Create a new instance of the Quiz from a database row"""
        if row:
            return cls(row[1], row[2], row[0]) # Create a new instance of the Quiz

    # Class method that gets all the instances of the Quiz from the database
    @classmethod
    def get_all(cls):
        """Get all the instances of the Quiz from the database"""
        sql = """
        SELECT * FROM Quizzes
        """
        CURSOR.execute(sql)  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Fetch all the rows from the database

        return [
            cls.instance_from_db_row(row) for row in rows # Create a new instance of the Quiz for each row
        ]  # Return a list of Quiz instances

    # Class method that finds a Quiz instance by its id
    @classmethod
    def find_by_id(cls, id):
        """Find a Quiz instance by its id"""
        sql = """
        SELECT * FROM Quizzes WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()  # Fetch the first row from the result
        return (
            cls.instance_from_db_row(row) if row else None # Return the Quiz instance
        )  # Return the Quiz instance

    # Class method that finds a Quiz instance by its title
    @classmethod
    def find_by_title(cls, title):
        """Find a Quiz instance by its title"""
        sql = """
        SELECT * FROM Quizzes WHERE title = ?
        """
        CURSOR.execute(sql, (title,))  # Execute the SQL statement
        row = CURSOR.fetchone()  # Fetch the first row from the result
        return (
            cls.instance_from_db_row(row) if row else None
        )  # Return the Quiz instance

    # Method that gets all the questions for the quiz
    def get_questions(self):
        """Get all the questions for the quiz"""
        sql = """
        SELECT * FROM Questions WHERE quiz_id = ?
        """
        CURSOR.execute(sql, (self.id,)) # Execute the SQL statement
        rows = CURSOR.fetchall() # Fetch all the rows from the database
        return [
            Question.instance_from_db_row(row) for row in rows
        ]  # Return a list of Question instances

    # Method that gets all the questions and answers for the quiz
    def get_questions_and_answers(self):
        """Get all the questions and answers for the quiz"""
        questions = self.get_questions() # Get all the questions for the quiz
        for question in questions: # Iterate over the questions
            answers = question.get_answers() # Get all the answers for the question
            question.answers = answers # Set the answers attribute of the question
        return questions  # Return a list of Question instances

    # Method that gets all the scores for the quiz
    def get_scores(self):
        """Get all the scores for the quiz"""
        sql = """
        SELECT * FROM Scores WHERE quiz_id = ?
        """
        CURSOR.execute(sql, (self.id,)) # Execute the SQL statement
        rows = CURSOR.fetchall() # Fetch all the rows from the database
        return [
            Score.instance_from_db(row) for row in rows # Return a list of Score instances
        ]  # Return a list of Score instances

    # def get_average_score(self):
    #     """Get the average score for the quiz"""
    #     scores = self.get_scores()
    #     total = 0
    #     for score in scores:
    #         total += score.score
    #     return total / len(scores) if scores else 0  # Return the average score
    def get_average_score(self):
        """Get the average score for the quiz"""
        scores = self.get_scores()
        if not scores: # If there are no scores for the quiz
            return 0  # Return 0 if there are no scores for the quiz
        total = sum(score.score for score in scores) # Calculate the total score
        return total / len(scores) # Return the average score

    def print_quiz_details(self):
        """Print the details of the quiz"""
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Average Score: {self.get_average_score()}")
        print("Questions:")
        questions = self.get_questions_and_answers()
        for question in questions:
            print(f"Question: {question.content}")
            # print("Answers:")
            # for answer in question.answers:
            #     print(f"Answer: {answer.content} - Correct: {answer.is_correct}")
            # print()
            # Changed this so it will only print the user answer.  Not all answers.
            print("Your Answer:")
            user_answer = question.get_answers(self)
            for user_answer in question.answers:

                # Print user's answer to the question
                print(
                    f"Your Answer: {user_answer} - Correct: {question.answer_is_correct(user_answer)}"
                )

            print()

    # Method that deletes the quiz, its questions, and answers from the database
    def delete_quiz_question_and_answers(self):
        """Delete the quiz, its questions, and answers from the database"""
        questions = self.get_questions() # Get all the questions for the quiz
        for question in questions: # Iterate over the questions
            question.delete_question_and_answers() # Delete the question and its answers
        self.delete() # Delete the quiz
