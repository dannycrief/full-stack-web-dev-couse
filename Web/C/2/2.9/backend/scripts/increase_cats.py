import sqlalchemy as sa
import sys

sys.path.insert(0, r'/home/danny/Full-stack Pytho web developer/Web/C/2/2.9/backend')
from appp.db import metadata, vote_results

if __name__ == "__main__":
    engine = sa.create_engine("sqlite:///my_db.sqlite")
    with engine.begin() as connection:
        select = vote_results.select().where(vote_results.c.name == "cats")
        results = connection.execute(select)
        id, _, votes = results.fetchone()

        new_votes = votes + 1
        update = (
            vote_results.update().values(votes=new_votes).where(vote_results.c.id == id)
        )
        connection.execute(update)
