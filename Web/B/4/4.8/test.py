import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///b4_7.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """
    # указываем имя таблицы
    __tablename__ = "album"
    # Задаем колонки в формате
    # название_колонки = sa.Column(ТИП_КОЛОНКИ)
    # идентификатор строки
    id = sa.Column(sa.INTEGER, primary_key=True)
    # Год записи альбома
    year = sa.Column(sa.INTEGER)
    # артист или группа, записавшие альбом
    artist = sa.Column(sa.TEXT)
    # жанр альбома
    genre = sa.Column(sa.TEXT)
    # название альбома
    album = sa.Column(sa.TEXT)


engine = sa.create_engine(DB_PATH)
Sessions = sessionmaker(engine)
session = Sessions()

bionic = Album(year=2010, artist="Christina Aguilera", genre="Rhythm and blues", album="Bionic")
heaven_and_earth = Album(year=2010, artist="Kamasi Washington", genre="Jazz", album="Heaven and Earth")

session.add(bionic)
session.add(heaven_and_earth)

session.commit()

heaven_and_earth = session.query(Album).filter(Album.album == "Heaven and Earth").first()
print(heaven_and_earth.year)

heaven_and_earth.year = 2018
session.add(heaven_and_earth)
last_ship = Album(year=2013, artist="Sting", genre="Rock", album="The Last Ship")
magic = Album(year=2016, artist="Bruno Mars", genre="Rhythm and blues", album="24K Magic")
session.add_all([last_ship, magic])
session.commit()
