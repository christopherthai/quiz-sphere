from models.__init__ import CURSOR, CONN
from models.score import Score
from models.user import User
from models.quiz import Quiz
from models.answer import Answer


class Question:

    # Class attribute that stores all the instances of the Questions
    all = {} 

    def __init__(self, content, quiz_id, id=None):
        self.id = id
        self.content = content
        self.quiz_id = quiz_id
        type(self).all.append(self)

    # Method that returns representation of the object
    def __repr__(self):
        return f"<Question {self.id}:{self.content}:{self.quiz_id}>"

    # Property method that returns the title
    @property
    def content(self):
        return self._content

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

    def save(self):
        """Save the instance of the Question to the database"""
        sql = """
        INSERT INTO Questions (content, quiz_id) VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.content, self.quiz_id))  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database
        self.id = CURSOR.lastrowid  # Set the id of the instance to the last row id

    def update(self):
        """Update the instance of the Question in the database"""
        sql = """
        UPDATE Questions SET content = ?, quiz_id = ? WHERE id = ?
        """
        CURSOR.execute(
            sql, (self.content, self.quiz_id, self.id)
        )  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    def delete(self):
        """Delete the instance of the Question from the database"""
        sql = """
        DELETE FROM Questions WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]  # Remove the instance from the all dictionary

        self.id = None

    @classmethod
    def create(cls, content, quiz_id):
        """Create a new instance of the Question"""
        question = cls(content, quiz_id)  # Create a new instance of the Question
        question.save()  # Save the instance to the database
        return question  # Return the instance

    @classmethod
    def instance_from_db_row(cls, row):
        """Create a new instance of the Question from a database row"""
        if row is None:
            return None

        return cls(row[1], row[2], id=row[0])

    @classmethod
    def get_all(cls):
        """Get all the instances of the Question from the database"""
        sql = """
        SELECT * FROM Questions
        """
        CURSOR.execute(sql)  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Fetch all the rows from the database

        return [
            cls.instance_from_db_row(row) for row in rows
        ]  # Return a list of Question instances

    @classmethod
    def find_by_id(cls, id):
        """Find a Question instance by its id"""
        sql = """
        SELECT * FROM Questions WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()  # Fetch the first row from the result
        return (
            cls.instance_from_db_row(row) if row else None
        )  # Return the Question instance

    def get_answers(self):
        """Get all the answers for the question"""
        sql = """
        SELECT * FROM Answers WHERE question_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()

        return [Answer.instance_from_db_row(row) for row in rows]
