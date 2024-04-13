from models.__init__ import CURSOR, CONN


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

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of the Quiz instance"""
        sql = """
        CREATE TABLE IF NOT EXISTS Quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        )
        """

        CURSOR.execute(sql)  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    @classmethod
    def drop_table(cls):
        """Drop the table that persists the attributes of the Quiz instance"""
        sql = "DROP TABLE IF EXISTS Quizzes"
        CURSOR.execute(sql)  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

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

        return cls(row[1], row[2], id=row[0])

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
