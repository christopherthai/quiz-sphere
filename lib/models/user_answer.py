from models.__init__ import CURSOR, CONN

import sqlite3

DB_PATH = "lib/data/quiz_sphere_3.db"


class User_Answer:

    # Class attribute that stores all the instances of the Answer
    all = []

    def __init__(self, user_answer, user_id, question_id, answer_id, id=None):
        self.id = id
        self.question_id = question_id
        self.answer_id = answer_id
        self.user_answer = user_answer
        self.user_id = user_id
        type(self).all.append(self)

    # Method that returns representation of the object
    def __repr__(self):
        return f"<User Answer {self.id} : {self.question_id} : {self.answer_id} :{self.user_answer} : {self.user_id}>"

    @staticmethod  # 추가
    def get_user_answers_for_question(question_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT user_answer FROM User_Answers WHERE question_id = ?",
            (question_id,),
        )
        user_answer_rows = cursor.fetchall()
        conn.close()
        return [User_Answer(question_id, *row) for row in user_answer_rows]

    # Property method that returns the user_answer
    @property
    def user_answer(self):
        return self._user_answer

    # Property method that sets the user_answer
    @user_answer.setter
    def user_answer(self, value):
        self._user_answer = value

    # Property method that returns the question_id
    @property
    def question_id(self):
        return self._question_id

    # Property method that sets the question_id
    @question_id.setter
    def question_id(self, value):
        self._question_id = value
        
    # Property method that returns the answer_id
    @property
    def answer_id(self):
        return self._answer_id

    # Property method that sets the answer_id
    @answer_id.setter
    def answer_id(self, value):
        self._answer_id = value

    # Property method that sets the user_id
    @property
    def user_id(self):
        return self._user_id

    # Property method that sets the user_id
    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    # Insert a new record into the User Answers table with the attributes of the Answer instance
    def save(self):
        """Save the instance of the User Answer to the database"""
        sql = """
        INSERT INTO User_Answers (user_answer, user_id, question_id) VALUES (?, ?, ?)
        """
        CURSOR.execute(
            sql, (self.user_answer, self.user_id, self.question_id, self.answer_id)
        )  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database
        self.id = CURSOR.lastrowid  # Set the id of the instance to the last row id

    # Update the record in the Answers table with the attributes of the Answer instance
    def update(self):
        """Update the instance of the User Answer in the database"""
        sql = """
        UPDATE User_Answers SET user_answer = ?, user_id = ? , question_id = ? answer_id = ? WHERE id = ?
        """
        CURSOR.execute(
            sql, (self.user_answer, self.user_id, self.question_id, self.answer_id)
        )  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    # Delete the record in the Answers table with the attributes of the Answer instance
    def delete(self):
        """Delete the instance of the User Answer from the database"""
        sql = """
        DELETE FROM User_Answers WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    # Class method that creates a new instance of the Answer
    @classmethod
    def create(cls, user_answer, user_id, question_id, answer_id):
        """Create a new instance of the User Answer"""
        user_answer = cls(
            user_answer, user_id, question_id, answer_id
        )  # Create a new instance of the User Answer
        user_answer.save()  # Save the instance to the database
        return user_answer  # Return the instance

    # Class method that creates a new instance of the Answer from a database row
    @classmethod
    def instance_from_db_row(cls, row):
        """Create a new instance of the Answer from a database row"""
        if row is None:  # If the row is None
            return None  # Return None

        return cls(
            row[1], row[2], row[3], row[0]
        )  # Create a new instance of the User Answer

    # Class method that returns all the instances of the User Answer from the database
    @classmethod
    def get_all(cls):
        """Get all the instances of the User Answer from the database"""
        sql = """
        SELECT * FROM User_Answers
        """
        CURSOR.execute(sql)  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Fetch all the rows from the database

        return [
            cls.instance_from_db_row(row) for row in rows
        ]  # Return a list of User Answer instances

    # Class method that finds a User Answer instance by its id
    @classmethod
    def find_by_question_id(cls, question_id):
        """Find a User Answer instance by its question id"""
        sql = """
        SELECT answer_id FROM User_Answers WHERE question_id = ?
        """
        CURSOR.execute(sql, (question_id,))  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Fetch the first row from the result
        return [row[0] for row in rows] if rows else []
