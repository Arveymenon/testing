from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


DATABASE_URI = 'postgres+psycopg2://postgres:arvey2509@localhost:5432/testing'
# engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine(DATABASE_URI)
db = scoped_session(sessionmaker(bind=engine))

# def main():
    # questions = db.execute("Select * from questionnaire").fetchall()
    # for question in questions:
    #     print(f'{ question.question }')