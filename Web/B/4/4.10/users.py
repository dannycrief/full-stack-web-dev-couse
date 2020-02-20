import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///users.sqlite3"
Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'user'
    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.String(36), primary_key=True)
    # имя пользователя
    first_name = sa.Column(sa.Text)
    # фамилия пользователя
    last_name = sa.Column(sa.Text)
    # адрес электронной почты пользователя
    email = sa.Column(sa.Text)

engine = sa.create_engine(DB_PATH)
Sessions = sessionmaker(engine)
session = Sessions()

TARGET_USER_IDS = ["cc773b91-39b7-4294-b173-8379eb2cf00f", "8cd0ce40-33df-473c-a970-7bc8743fcd57"]

all_users_list = session.query(User).all()
target_user_names = ["{} {}".format(user.first_name, user.last_name) for user in all_users_list if user.id in TARGET_USER_IDS]
for name in target_user_names:
    print(name)