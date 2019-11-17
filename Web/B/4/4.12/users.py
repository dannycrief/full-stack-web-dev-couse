import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()


class User(Base):
    """
    Describe 'athlete' table structure
    """
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)


def connect_db():
    """
    Connect our DB. Create tables if we need it & return session obj
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def request_data():
    """
    Ask for data & add into user list
    :return: user
    """
    print("Hi, I'll need to write your data")
    first_name = input("Enter your name: ")
    last_name = input("Enter your surname: ")
    gender = input("Sex: (Male or Female): ")
    email = input("I'll also need your email: ")
    bithdate = input("Your birthday (YYYY-MM-DD format ex. 1999-01-28): ")
    height = input("Your height in metres. ex. 1.75: ")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=bithdate,
        height=height
    )
    return user


def main():
    """
    It interacts with the user, processes user input
    :return: nothing
    """
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Your data is in our database. Thank you!")


if __name__ == '__main__':
    main()
