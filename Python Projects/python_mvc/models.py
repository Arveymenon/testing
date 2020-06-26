from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = "questionnaire"
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey("questionnaire_sections.id"), primary_key=False)
    question = Column(String, primary_key=False)


    # def __repr__(self):
    #     return "<Book(section_id='{}', question='{}')>"\
    #             .format(self.section_id, self.question)

class Section(db.Model):
    __tablename__ = "questionnaire_sections"
    id = Column(Integer, primary_key=True)
    name = Column(Integer, primary_key=False)
    questions = db.relationship('Question', backref="section", lazy=True,
                primaryjoin="Question.section_id == Section.id")

    
    def addQuestion(self, question):
        question = Question(question=question, section_id=self.id)
        db.session.add(question)
        db.session.commit()