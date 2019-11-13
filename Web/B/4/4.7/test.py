import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''
dialect+driver://username:password@host:port/database
sqlite:///filename
'''
DB_PATH = "sqlite:///b4_7.sqlite3"
Base = declarative_base()


class Album(Base):
    """
    Describes the structure of the album table for storing music library records
    """
    # specify the name of the table
    __tablename__ = "album"
    # We set the columns in the format
    # column_name = sa.Column (COLUMN_TYPE)
    # line identifier
    id = sa.Column(sa.INTEGER, primary_key=True)
    # albums year of record
    year = sa.Column(sa.INTEGER)
    # artist or group, that recorded that album
    artist = sa.Column(sa.TEXT)
    # album genre
    genre = sa.Column(sa.TEXT)
    # name of album
    album = sa.Column(sa.TEXT)


# create a database connection
engine = sa.create_engine(DB_PATH)
# create a factory session
Sessions = sessionmaker(engine)
# create a session
session = Sessions()

# pass the Album model to the session.query method and call the all method
albums = session.query(Album).all()
print(len(albums))

for album in albums:
    print(album.year, album.artist, album.genre, album.album)

for album in albums:
    print("{} group wrote the album called {} in {} genre in {} year".format(album.artist, album.album, album.genre, album.year))
