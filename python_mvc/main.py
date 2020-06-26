import os
from flask import Flask, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from models.models import Question
from config import DATABASE_URI


engine = create_engine(DATABASE_URI)
Base = declarative_base()

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def main():
    print("WORKING")
    # questions = Question.query.all()
    # questions = db.execute().fetchall()
    # print(questions)
    # for question in questions:
    #     print({question.question})
    # db.session.commit(question)
    # return json.dumps(questions)

if __name__ == "__main__":
        main()
        pass