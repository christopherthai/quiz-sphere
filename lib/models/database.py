from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# 데이터베이스 엔진 설정
engine = create_engine('sqlite:///../data/quiz_sphere.db', echo=True)

# 세션 생성
Session = scoped_session(sessionmaker(bind=engine))

# 베이스 클래스 생성
Base = declarative_base()