import sqlalchemy as sa
import sys
sys.path.insert(0, r'/home/danny/Full-stack Pytho web developer/Web/C/2/2.9/backend')
from appp.db import metadata, vote_results

if __name__ == "__main__":
    engine = sa.create_engine("sqlite:///my_db.sqlite")
    with engine.begin() as connection:
        select = vote_results.select()
        results = connection.execute(select)
        for id, name, votes in results.fetchall():
            print(id, name, votes)
