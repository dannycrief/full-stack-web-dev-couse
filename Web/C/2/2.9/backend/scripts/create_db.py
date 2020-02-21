import sys
sys.path.insert(0, r'/home/danny/Full-stack Pytho web developer/Web/C/2/2.9/backend')
from appp.db import metadata, vote_results
import sqlalchemy as sa

if __name__ == "__main__":
    engine = sa.create_engine('sqlite:///my_db.sqlite')
    metadata.create_all(engine)

    with engine.begin() as connection:
        for i, animal in enumerate(['cats', 'dogs', 'parrots'], start=1):
            statement = vote_results.insert().values(
                id=i,
                name=animal,
                votes=0
            )
            connection.execute(statement)
