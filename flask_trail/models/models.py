from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Question(db.Model):
    __tablename__ = "questionnaire"
    id = db.Column(db.Integer, primary_key=True)
    section_id = db.Column(db.Integer, primary_key=False)
    question = db.Column(db.String, primary_key=False)