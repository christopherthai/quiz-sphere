from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base, engine  # engine을 임포트

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    answer_text = Column(String)
    is_correct = Column(Boolean)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship('Question', back_populates='answers')

# 엔진 인스턴스를 명시적으로 제공
Base.metadata.create_all(engine)
