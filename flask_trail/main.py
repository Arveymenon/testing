from flask import Flask, render_template, request, session
from flask_session import Session
import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.models import Question


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# engine = create_engine(os.getenv("DATABASE_URL"))
DATABASE_URI = 'postgres+psycopg2://postgres:arvey2509@localhost:5432/testing'
engine = create_engine(DATABASE_URI)
db = scoped_session(sessionmaker(bind=engine))
# db = SQLAlchemy(app)
# db.init_app(app)
Session(app)


def main():
    questions = db.execute("Select * from questionnaire").fetchall()
    for question in questions:
        print(f'{ question.question }')

@app.route('/questions')
def questions():
    questions = db.execute("Select * from questionnaire").fetchall()
    for question in questions:
        print(f'{ question.question }')

    db.commit()
    return render_template("home.html", titles= session["titles"] ,title = name, questions = questions)

@app.route("/")
def index():
    return "Hello!"

@app.route("/home", methods=['GET','POST'])
def home():
    if session.get("titles") is None:
        session["titles"] = []

    if request.method == 'GET':
        name = "Home"

    elif request.method == 'POST':
        name = request.form.get("title")
        session["titles"].append(name)
        # question = Question(section_id='2', question=name)
        # db.session.add(question)
        db.session.execute('select * from questionnaire')
        db.session.commit()

    request.form.clear
    return render_template("home.html", titles= session["titles"] ,title = name)

# @app.route('/submit', methods=['POST'])
# def submit():
#     name = request.form.get("title")
#     titles.append(name)
#     # return path('/home', VIEW.as_view("bhel"), name='home'),
#     return render_template("home.html", titles= titles ,title = name)





@app.route("/<string:name>")
def name(name):
    today = datetime.datetime.now()
    my_bday = today.day == 25 and today.month == 9
    name = name.capitalize()
    return render_template("index.html", date = today, my_bday = my_bday, arrey = name)
    # return f"Hello {name}!"