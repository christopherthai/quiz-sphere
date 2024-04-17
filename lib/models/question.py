from models.__init__ import CURSOR, CONN
from models.user_answer import User_Answer
from models.answer import Answer

import sqlite3

DB_PATH = "lib/data/quiz_sphere_database.db"


class Question:

    # Class attribute that stores all the instances of the Questions
    all = []

    def __init__(self, content, quiz_id, id=None):
        self.id = id
        self.content = content
        self.quiz_id = quiz_id
        type(self).all.append(self)

    # Method that returns representation of the object
    def __repr__(self):
        return f"<Question {self.id}:{self.content}:{self.quiz_id}>"

    @staticmethod  # 추가
    def get_random_questions(limit=10):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, content, quiz_id FROM questions ORDER BY RANDOM() LIMIT ?",
            (limit,),
        )
        question_rows = cursor.fetchall()
        conn.close()
        return [Question(*row) for row in question_rows]

    # Property method that returns the title
    @property
    def content(self):
        return self._content

    # Property method that sets the title
    @content.setter
    def content(self, value):
        if value in self.all:
            raise ValueError("Content already exists")
        self._content = value

    # Property method that returns the description
    @property
    def quiz_id(self):
        return self._quiz_id

    # Property method that sets the description
    @quiz_id.setter
    def quiz_id(self, value):
        self._quiz_id = value

    # Insert a new record into the Questions table with the attributes of the Question instance
    def save(self):
        """Save the instance of the Question to the database"""
        sql = """
        INSERT INTO Questions (content, quiz_id) VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.content, self.quiz_id))  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database
        self.id = CURSOR.lastrowid  # Set the id of the instance to the last row id

    # Update the record in the Questions table with the attributes of the Question instance
    def update(self):
        """Update the instance of the Question in the database"""
        sql = """
        UPDATE Questions SET content = ?, quiz_id = ? WHERE id = ?
        """
        CURSOR.execute(
            sql, (self.content, self.quiz_id, self.id)
        )  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    # Delete the record in the Questions table with the attributes of the Question instance
    def delete(self):
        """Delete the instance of the Question from the database"""
        sql = """
        DELETE FROM Questions WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))  # Execute the SQL statement
        CONN.commit()

    # Class method that creates a new instance of the Question
    @classmethod
    def create(cls, content, quiz_id):
        """Create a new instance of the Question"""
        question = cls(content, quiz_id)  # Create a new instance of the Question
        question.save()  # Save the instance to the database
        return question  # Return the instance

    # Class method that creates a new instance of the Question from a database row
    @classmethod
    def instance_from_db_row(cls, row):
        """Create a new instance of the Question from a database row"""
        if row is None:
            return None

        return cls(row[1], row[2], id=row[0])  # Create a new instance of the Question

    # Class method that returns all the instances of the Question from the database
    @classmethod
    def get_all(cls):
        """Get all the instances of the Question from the database"""
        sql = """
        SELECT * FROM Questions
        """
        CURSOR.execute(sql)  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Fetch all the rows from the database

        return [
            cls.instance_from_db_row(row)
            for row in rows  # Create a new instance of the Question for each row
        ]

    # Class method that finds a Question instance by its id
    @classmethod
    def find_by_id(cls, id):
        """Find a Question instance by its id"""
        sql = """
        SELECT * FROM Questions WHERE id = ?
        """
        CURSOR.execute(sql, (id,)) # Execute the SQL statement
        row = CURSOR.fetchone()  # Fetch the first row from the result
        return (
            cls.instance_from_db_row(row) if row else None
        )  # Return the Question instance

    # Get all the answers for the question
    def get_answers(self):
        """Get all the answers for the question"""
        sql = """
        SELECT * FROM Answers WHERE question_id = ?
        """
        CURSOR.execute(sql, (self.id,)) # Execute the SQL statement
        rows = CURSOR.fetchall() # Fetch all the rows from the database

        return [
            Answer.instance_from_db_row(row) for row in rows # Create a new instance of the Answer for each row
        ]  # Return a list of Answer instances

    # Get the correct answer for the question
    def get_correct_answer(self):
        """Get the correct answer for the question"""
        sql = """
        SELECT * FROM Answers WHERE question_id = ? AND is_correct = 1
        """
        CURSOR.execute(sql, (self.id,)) # Execute the SQL statement
        row = CURSOR.fetchone() # Fetch the first row from the result

        return (
            Answer.instance_from_db_row(row) if row else None
        )  # Return the Answer instance

    # Add an answer to the question
    def add_answer(self, content, is_correct):
        """Add an answer to the question"""
        answer = Answer.create(content, self.id, is_correct) # Create a new instance of the Answer
        return answer # Return the Answer instance

    # Delete a specific answer from the question
    def delete_specific_answer(self, answer_id):
        """Delete a specific answer from the question"""
        answer = Answer.find_by_id(answer_id) # Find the answer by its id
        if answer: # If the answer is found
            answer.delete() # Delete the answer
        else:
            print(f"Answer {answer_id} not found")

    # Delete the question and all its answers from the database
    def delete_question_and_answers(self):
        """Delete the question and all its answers from the database"""
        answers = self.get_answers() # Get all the answers for the question
        for answer in answers: # Iterate over the answers
            answer.delete() # Delete the answer
        self.delete() # Delete the question
        
    # Gets users answers for a question
    def get_user_answer(self):
        """Get the user answer for the question"""
        sql = """
        SELECT * FROM User_Answers WHERE question_id = ? 
        """
        CURSOR.execute(sql, (self.id,)) # Execute the SQL statement
        row = CURSOR.fetchone() # Fetch the first row from the result

        return (
            User_Answer.instance_from_db_row(row) if row else None
        )  # Return the Answer instance
