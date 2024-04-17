CREATE TABLE User_Answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_answer INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    answer_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (question_id) REFERENCES Quizzes(id),
    FOREIGN KEY (answer_id) REFERENCES Questions(id)
);