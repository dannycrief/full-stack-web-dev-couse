import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    Opisuje strukturę tabeli albumów do przechowywania rekordów biblioteki muzycznej
    """

    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)


def connect_db():
    """
    Ustanawia połączenie z bazą danych, tworzy tabele, jeśli je nie ma, i zwraca obiekt sesji
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def find(artist):
    """
    Znajduje wszystkie albumy w bazie danych dla danego wykonawcy
    """
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums



