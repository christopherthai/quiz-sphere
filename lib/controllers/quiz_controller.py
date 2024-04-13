from lib.models.question import Question
from lib.models.answer import Answer
from lib.models.database import Session  # 수정된 임포트

def get_all_questions():
    with Session() as session:
        return session.query(Question).all()

def get_all_subjects():
    with Session() as session:
        return [subject[0] for subject in session.query(Question.subject).distinct().all()]

def get_questions_by_subject(subject):
    with Session() as session:
        return session.query(Question).filter(Question.subject == subject).all()

def add_question(subject, question, answers):
    with Session() as session:
        new_question = Question(subject=subject, question=question)
        session.add(new_question)
        for answer, is_correct in answers:
            new_answer = Answer(answer=answer, is_correct=is_correct, question=new_question)
            session.add(new_answer)
        session.commit()





# from lib.models.quiz import Quiz


# def create_quiz(title):
#     print(f"Quiz titled '{title}' created successfully.")


# def delete_quiz(quiz_id):
#     print(f"Quiz with ID {quiz_id} has been deleted.")

