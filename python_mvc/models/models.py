from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Question(Base):
    __tablename__ = "questionnaire"
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, primary_key=False)
    question = Column(String, primary_key=False)

    def __repr__(self):
        return "<Book(section_id='{}', question='{}')>"\
                .format(self.section_id, self.question)