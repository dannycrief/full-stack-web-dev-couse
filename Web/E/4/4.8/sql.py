from sqlalchemy import create_engine, MetaData, Table, and_, or_, asc
engine = create_engine('postgresql+psycopg2://postgres:211217ns@localhost:5433/movies')
conn = engine.connect()

metadata = MetaData(bind=None)
movies_table = Table('movies', metadata, autoload=True, autoload_with=engine)

"""
request = movies_table.select()
res = conn.execute(request)

print([row for row in res])

res = conn.execute("SELECT * FROM movies WHERE movie_id > 3;")
print([row for row in res])

request = movies_table.select().where(movies_table.columns.movie_id > 2)
print(request)
"""



# res = conn.execute("SELECT * FROM movies WHERE movie_id > 3 AND movie_id < 5;")

"""
request = movies_table.select().where(and_(movies_table.c.movie_id>3, movies_table.c.movie_id<5))
res = conn.execute(request)
print([row for row in res])
"""


# res = conn.execute("SELECT * FROM movies WHERE movie_id > 3 OR movie_id < 5;")

"""
request = movies_table.select().where(or_(movies_table.c.movie_id>3, movies_table.c.movie_id<5))
res = conn.execute(request)
print([row for row in res])
"""

# res = conn.execute("SELECT * FROM movies WHERE movie_id > 3 ORDER BY movie_id ASC;")

request = movies_table.select().where(movies_table.c.movie_id>5).order_by(asc(movies_table.c.movie_id))
res = conn.execute(request)
print([row for row in res])
