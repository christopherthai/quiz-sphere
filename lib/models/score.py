from models.__init__ import CURSOR, CONN


class Score:
    all = {}

    def __init__(self, score, date_taken, user_id, quiz_id, id=None):
        self.id = id
        self.score = score
        self.date_taken = date_taken
        self.user_id = user_id
        self.quiz_id = quiz_id
        type(self).all[score] = self

    # Method that returns representation of the object
    def __repr__(self):
        return f"<Score {self.id}: {self.score} for Quiz: {self.quiz_id},"

    # property method that returns the score
    @property
    def score(self):
        return self._score

    # property method that sets the score value
    @score.setter
    def score(self, value):
        self._score = value

    # property method that returns the date taken
    @property
    def date_taken(self):
        return self._date_taken

    # property method that sets the date taken value
    @date_taken.setter
    def date_taken(self, value):
        self._date_taken = value

    # property method that returns the user id
    @property
    def user_id(self):
        return self._user_id

    # property method that sets the user id value
    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    # property method that returns the quiz id
    @property
    def quiz_id(self):
        return self._quiz_id

    # property method that sets the quiz id value
    @quiz_id.setter
    def quiz_id(self, value):
        self._quiz_id = value

    # Insert a new record into the Scores table with the attributes of the Score instance
    def save(self):
        """Insert a new record into the Scores table with the attributes of the Score instance"""
        sql = """
        INSERT INTO Scores (id, score, date_taken, user_id, quiz_id) VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(
            sql,
            (
                self.id,
                self.score,
                self.date_taken,
                self.user_id,
                self.quiz_id,
            ),  # Execute the SQL statement
        )
        CONN.commit()  # Commit the changes to the database

        self.id = CURSOR.lastrowid  # Get the id of the last inserted row
        type(self).all[
            self.score
        ] = self  # Add the Score instance to the all dictionary

    # Update the record in the Scores table with the attributes of the Score instance
    def update(self):
        """Update the record in the Scores table with the attributes of the Score instance"""
        sql = """
        UPDATE Scores SET score = ?, date_taken = ?, user_id = ?, quiz_id = ? WHERE id = ?
        """
        CURSOR.execute(
            sql,
            (
                self.score,
                self.date_taken,
                self.user_id,
                self.quiz_id,
                self.id,
            ),  # Execute the SQL statement
        )
        CONN.commit()

    # Delete the record in the Scores table with the attributes of the Score instance
    def delete(self):
        """Delete the record in the Scores table with the attributes of the Score instance"""
        sql = """
        DELETE FROM Scores WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))  # Execute the SQL statement
        CONN.commit()  # Commit the changes to the database

    # Class method that creates a new instance of the Score class
    @classmethod
    def create(cls, score, date_taken, user_id, quiz_id):
        """Create a new instance of the Score class"""
        score = cls(score, date_taken, user_id, quiz_id)  # Create a new Score instance
        score.save()  # Save the Score instance to the database
        return score

    # Class method that returns a Score instance from a row in Scores table
    @classmethod
    def instance_from_db(cls, row):
        """Return a Score instance from a row in Scores table"""
        if row:  # If the row is not None
            return cls(
                row[1], row[2], row[3], row[4], id=row[0]
            )  # Create a Score instance
        return None

    # Class method that returns all records from the Scores table
    @classmethod
    def get_all(cls):
        """Return all records from the Scores table"""
        sql = """
        SELECT * FROM Scores
        """
        CURSOR.execute(sql)  # Execute the SQL statement
        rows = CURSOR.fetchall()  # Returns all rows
        return [
            cls.instance_from_db(row) for row in rows
        ]  # Create a User instance for each row

    # Class method that returns the record from the Scores table with the given id
    @classmethod
    def find_by_id(cls, id):
        """Return the record from the Scores table with the given id"""
        sql = """
        SELECT * FROM Scores WHERE id = ?
        """
        CURSOR.execute(sql, (id,))  # Execute the SQL statement
        row = CURSOR.fetchone()  # Returns the first row
        return cls.instance_from_db(row)  # Returns the first row
