from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base, engine  # engine을 임포트

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    question_text = Column(String)
    answers = relationship('Answer', back_populates='question')

# 엔진 인스턴스를 명시적으로 제공
Base.metadata.create_all(engine)
