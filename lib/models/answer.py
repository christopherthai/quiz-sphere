from models.__init__ import CURSOR, CONN

import sqlite3

DB_PATH = "lib/data/quiz_sphere_2.db"


class Answer:

    # Class attribute that stores all the instances of the Answer
    all = []

    def __init__(self, content, is_correct, question_id, id=None):
        self.id = id
        self.content = content
        self.is_correct = is_correct
        self.question_id = question_id
        type(self).all.append(self)

    # Method that returns representation of the object
    def __repr__(self):
        return f"<Answer {self.id} : {self.content} : {self.is_correct} : {self.question_id}>"

    @staticmethod  # 추가
    def get_answers_for_question(question_id):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT content, is_correct FROM answers WHERE question_id = ?",
            (question_id,),
        )
        answer_rows = cursor.fetchall()
        conn.close()
        return [Answer(question_id, *row) for row in answer_rows]

    # Property method that returns the content
    @property
    def content(self):
        return self._content

    # Property method that sets the content
    @content.setter
    def content(self, value):
        if value in self.all:
            raise ValueError("Content already exists")
        self._content = value

    # Property method that returns the is_correct
    @property
    def is_correct(self):
        return self._is_correct

    # Property method that sets the is_correct
    @is_correct.setter
    def is_correct(self, value):
        if value in self.all:
            raise ValueError("")
        self._is_correct = value

    # Property method that sets the question_id
    @property
    def question_id(self):
        return self._question_id

    # Property method that sets the question_id
    @question_id.setter
    def question_id(self, value):
        if value in self.all:
            raise ValueError("")
        self._question_id = value

    # Insert a new record into the Answers table with the attributes of the Answer instance
    def save(self):
        """Save the instance of the Answer to the database"""
        sql = """
        INSERT INTO Answers (content, is_correct, question_id) VALUES (?, ?, ?)
        """
        CURSOR.execute(
            sql, (self.content, self.is_correct, self.question_id)
        )  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database
        self.id = CURSOR.lastrowid  # Set the id of the instance to the last row id

    # Update the record in the Answers table with the attributes of the Answer instance
    def update(self):
        """Update the instance of the Answer in the database"""
        sql = """
        UPDATE Answers SET content = ?, is_correct = ? , question_id = ? WHERE id = ?
        """
        CURSOR.execute(
            sql, (self.content, self.is_correct, self.question_id, self.id)
        )  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    # Delete the record in the Answers table with the attributes of the Answer instance
    def delete(self):
        """Delete the instance of the Answer from the database"""
        sql = """
        DELETE FROM Answers WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    # Class method that creates a new instance of the Answer
    @classmethod
    def create(cls, content, is_correct, question_id):
        """Create a new instance of the Answer"""
        answer = cls(
            content, is_correct, question_id
        )  # Create a new instance of the Answer
        answer.save()  # Save the instance to the database
        return answer  # Return the instance

    # Class method that creates a new instance of the Answer from a database row
    @classmethod
    def instance_from_db_row(cls, row):
        """Create a new instance of the Answer from a database row"""
        if row is None:  # If the row is None
            return None  # Return None

        return cls(
            row[1], row[2], row[3], row[0]
        )  # Create a new instance of the Answer

    # Class method that returns all the instances of the Answer from the database
    @classmethod
    def get_all(cls):
        """Get all the instances of the Answer from the database"""
        sql = """
        SELECT * FROM Answers
        """
        CURSOR.execute(sql)  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Fetch all the rows from the database

        return [
            cls.instance_from_db_row(row) for row in rows
        ]  # Return a list of Answer instances

    # Class method that finds a Answer instance by its id
    @classmethod
    def find_by_id(cls, id):
        """Find a Answer instance by its id"""
        sql = """
        SELECT * FROM Answers WHERE id = ?
        """
        CURSOR.execute(sql, (id,))  # Execute the SQL statement
        row = CURSOR.fetchone()  # Fetch the first row from the result
        return (
            cls.instance_from_db_row(row) if row else None
        )  # Return the Answer instance
