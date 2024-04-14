from models.__init__ import CURSOR, CONN
from models.score import Score
from models.question import Question


class Quiz:

    # Class attribute that stores all the instances of the Quiz
    all = {}

    def __init_(self, title, description, id=None):
        self.id = id
        self.title = title
        self.description = description
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
        if value in self.all:
            raise ValueError("Title already exists")
        self._title = value

    # Property method that returns the description
    @property
    def description(self):
        return self._description

    # Property method that sets the description
    @description.setter
    def description(self, value):
        self._description = value

    def save(self):
        """Save the instance of the Quiz to the database"""
        sql = """
        INSERT INTO Quizzes (title, description) VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.title, self.description))  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database
        self.id = CURSOR.lastrowid  # Set the id of the instance to the last row id

    def update(self):
        """Update the instance of the Quiz in the database"""
        sql = """
        UPDATE Quizzes SET title = ?, description = ? WHERE id = ?
        """
        CURSOR.execute(
            sql, (self.title, self.description, self.id)
        )  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    def delete(self):
        """Delete the instance of the Quiz from the database"""
        sql = """
        DELETE FROM Quizzes WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]  # Remove the instance from the all dictionary

        self.id = None

    @classmethod
    def create(cls, title, description):
        """Create a new instance of the Quiz"""
        quiz = cls(title, description)  # Create a new instance of the Quiz
        quiz.save()  # Save the instance to the database
        return quiz  # Return the instance

    @classmethod
    def instance_from_db_row(cls, row):
        """Create a new instance of the Quiz from a database row"""
        if row is None:
            return None

        return cls(row[1], row[2], row[0])

    @classmethod
    def get_all(cls):
        """Get all the instances of the Quiz from the database"""
        sql = """
        SELECT * FROM Quizzes
        """
        CURSOR.execute(sql)  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Fetch all the rows from the database

        return [
            cls.instance_from_db_row(row) for row in rows
        ]  # Return a list of Quiz instances

    @classmethod
    def find_by_id(cls, id):
        """Find a Quiz instance by its id"""
        sql = """
        SELECT * FROM Quizzes WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()  # Fetch the first row from the result
        return (
            cls.instance_from_db_row(row) if row else None
        )  # Return the Quiz instance

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

    def get_questions(self):
        """Get all the questions for the quiz"""
        sql = """
        SELECT * FROM Questions WHERE quiz_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [Question.instance_from_db_row(row) for row in rows]

    def get_questions_and_answers(self):
        """Get all the questions and answers for the quiz"""
        questions = self.get_questions()
        for question in questions:
            answers = question.get_answers()
            question.answers = answers
        return questions

    def get_scores(self):
        """Get all the scores for the quiz"""
        sql = """
        SELECT * FROM Scores WHERE quiz_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        return [Score.instance_from_db(row) for row in rows]

    def get_average_score(self):
        """Get the average score for the quiz"""
        scores = self.get_scores()
        total = 0
        for score in scores:
            total += score.score
        return total / len(scores) if scores else 0

    def print_quiz_details(self):
        """Print the details of the quiz"""
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"Average Score: {self.get_average_score()}")
        print("Questions:")
        questions = self.get_questions_and_answers()
        for question in questions:
            print(f"Question: {question.content}")
            print("Answers:")
            for answer in question.answers:
                print(f"Answer: {answer.content} - Correct: {answer.is_correct}")
            print()
