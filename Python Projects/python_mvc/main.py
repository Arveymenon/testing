from flask import Flask, render_template, session, jsonify
from flask_session import Session
from flask_socketio import SocketIO, emit
from models import *


import json

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:arvey2509@localhost:5432/testing'
db.init_app(app)

socketio = SocketIO(app, cors_allowed_origins="*")

# DATABASE_URI = 'postgres+psycopg2://postgres:arvey2509@localhost:5432/testing'
# engine = create_engine(DATABASE_URI)

# db = scoped_session(sessionmaker(bind=engine))

# Session(app)

@socketio.on('send-message')
def message(message):
    emit('recieve_message', message, broadcast=True)
    return 

def main():
    print("called main")
    # questions = Question.query.all()
    # for question in questions:
    #     print({question.question})


@app.route('/questions', methods=['GET'])
def getAll():
    # filter = Question.section_id.in_([1, 2])
    # questions = Question.query.filter(filter).all()
    filter = Section.id.in_([1,2])

    sections = Section.query.filter(filter).all()
    # print(sections)

    # questions.question
    

    return jsonify({
        "sections": sections
        })

    # for section in sections:
    #     questions = section.questions
    #     for question in questions:
    #         print(f'{section.name} - {question.question}')
            # db.session.
            # db.session.commit()

    # db.commit()

    # return questions


if __name__ == "__main__":
    with app.app_context():
        getAll()
        pass
