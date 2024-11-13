'''
CREATE TABLE IF NOT EXIST stage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    poste TEXT NOT NULL,
    entreprise TEXT NOT NULL,
    expedition TEXT NOT NULL,
    text TEXT
)
'''
# bdd.py
from stage import Stage, fake_stage

from database import get_session
from sqlmodel import select


# INSERTION
with get_session() as session:
    for _ in range(0):
        new_stage = fake_stage()
        session.add(new_stage) #insert
        session.commit() #commit
        session.refresh(new_stage) #recup_id
        print(new_stage)
        print(new_stage.id)

# SELECT
with get_session() as session:
    statement = select(Stage)
    results = session.exec(statement).all()
    for stage in results :
        print(stage)

with get_session() as session:
    statement = select(Stage).where(Stage.entreprise == 'Jerem Corp')
    statement = select(Stage).where(Stage.entreprise.like("%ch"))
    results = session.exec(statement).all()
    for stage in results :
        print(stage)