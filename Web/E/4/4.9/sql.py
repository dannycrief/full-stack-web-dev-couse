from sqlalchemy import create_engine, MetaData, Table, and_, or_, asc
engine = create_engine('postgresql+psycopg2://postgres:211217ns@localhost:5433/movies')
conn = engine.connect()