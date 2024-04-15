from models.__init__ import CURSOR, CONN
from models.score import Score
from models.quiz import Quiz
from models.question import Question
from models.answer import Answer


class User:

    # Class attribute that stores all the instances of the User
    all = {}

    def __init__(self, username, is_admin=0, id=None):
        self.id = id
        self.username = username
        self.is_admin = is_admin
        type(self).all[username] = self

    # Method that returns representation of the object
    def __repr__(self):
        return f"<User {self.id}: {self.username}, " + f"Is_admin: {self.is_admin}>"

    # Property method that returns the username
    @property
    def username(self):
        return self._username

    # Property method that sets the username
    @username.setter
    def username(self, value):
        self._username = value

    # Property method that returns the is_admin value
    @property
    def is_admin(self):
        return self._is_admin

    # Property method that sets the is_admin value
    @is_admin.setter
    def is_admin(self, value):
        if value not in (0, 1):
            raise ValueError("Invalid value for is_admin")
        self._is_admin = value

    def save(self):
        """Insert a new record into the Users table with the attributes of the User instance"""
        sql = """
        INSERT INTO Users (username, is_admin) VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.username, self.is_admin))  # Execute the SQL statement
        CONN.commit()

        self.id = CURSOR.lastrowid  # Get the id of the last inserted row
        type(self).all[
            self.username
        ] = self  # Add the User instance to the all dictionary

    def update(self):
        """Update the record in the Users table with the attributes of the User instance"""
        sql = """
        UPDATE Users SET username = ?, is_admin = ? WHERE id = ?
        """
        CURSOR.execute(
            sql, (self.username, self.is_admin, self.id)
        )  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    def delete(self):
        """Delete the record in the Users table with the attributes of the User instance"""
        sql = """
        DELETE FROM Users WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    @classmethod
    def create(cls, username, is_admin):
        """Create a new instance of the User class"""
        user = cls(username, is_admin)  # Create a new User instance
        user.save()  # Save the User instance to the database
        return user  # Return the User instance

    @classmethod
    def instance_from_db(cls, row):
        """Return a User instance from a row in the Users table"""
        if row:
            return cls(row[1], row[2], row[0])
        return None

    @classmethod
    def get_all(cls):
        """Return all records from the Users table"""
        sql = """
        SELECT * FROM Users
        """
        CURSOR.execute(sql)  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Returns all rows
        return [
            cls.instance_from_db(row) for row in rows
        ]  # Create a User instance for each row

    @classmethod
    def find_by_id(cls, id):
        """Return the record from the Users table with the given id"""
        sql = """
        SELECT * FROM Users WHERE id = ?
        """
        CURSOR.execute(sql, (id,))  # Execute the SQL statement
        row = CURSOR.fetchone()  # Returns the first row
        return (
            cls.instance_from_db(row) if row else None
        )  # Create a User instance if row is not None

    @classmethod
    def find_by_username(cls, username):
        """Return the record from the Users table with the given username"""
        sql = """
        SELECT * FROM Users WHERE username = ?
        """
        CURSOR.execute(sql, (username,))  # Execute the SQL statement
        row = CURSOR.fetchone()  # Returns the first row
        return (
            cls.instance_from_db(row) if row else None
        )  # Return a User instance if row is not None

    def get_all_scores(self):
        """Return all the scores of the user"""
        sql = """
        SELECT * FROM Scores WHERE user_id = ?
        """
        CURSOR.execute(sql, (self.id,))  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Returns all rows
        return [
            Score.instance_from_db(row) for row in rows
        ]  # Return a Score instance for each row

    def get_quiz_score(self, quiz):
        """Return the score of the user in a particular quiz"""
        sql = """
        SELECT * FROM Scores WHERE user_id = ? AND quiz_id = ?
        """
        CURSOR.execute(sql, (self.id, quiz.id))
        row = CURSOR.fetchone()
        return Score.instance_from_db(row)  # Return a Score instance

    def get_all_quizzes(self):
        """Return all the quizzes of the user"""
        sql = """
        SELECT * FROM Scores WHERE user_id = ?
        """
        CURSOR.execute(sql, (self.id,))  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Returns all rows
        return [
            Quiz.find_by_id(row[2]) for row in rows
        ]  # Return a Quiz instance for each row

    def get_all_quizzes_and_scores(self):
        """Return all the quizzes and scores of the user"""
        sql = """
        SELECT * FROM Scores WHERE user_id = ?
        """
        CURSOR.execute(sql, (self.id,))  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Returns all rows
        return [
            (Quiz.find_by_id(row[4]), Score.instance_from_db(row)) for row in rows
        ]  # Return a tuple of Quiz and Score instance for each row

    def print_quiz_details(self, quiz_id):
        """Print the details of the quizzes and scores of the user"""
        quiz = Quiz.find_by_id(quiz_id)
        score = self.get_quiz_score(quiz)
        print(f"Quiz: {quiz.title}")
        print(f"Score: {score.score}")
        print(f"Date taken: {score.date_taken}")
        print(f"Average score: {quiz.get_average_score()}")
        questions = quiz.get_questions_and_answers()
        for question in questions:
            print(f"Question: {question.content}")
            for answer in question.answers:
                print(f"Answer: {answer.content}")
        print("\n")

    # @classmethod
    # def get_all_quizzes_and_scores(cls, user_id):
    #     """Return all quizzes and scores for a given user"""
    #     sql = """
    #     SELECT Quizzes.title, Scores.score
    #     FROM Quizzes
    #     JOIN Scores ON Quizzes.id = Scores.quiz_id
    #     WHERE Scores.user_id = ?
    #     """
    #     CURSOR.execute(sql, (user_id,))
    #     return CURSOR.fetchall()
