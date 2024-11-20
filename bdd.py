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
from stage_model import Stage, fake_stage
from project_model import Project, Proj

from database import get_session
from sqlmodel import select


with get_session() as session:
    session.add(Proj(
        rubrique="vue.js",
        nom="Jerem",
        image="img/jerem.jpg",
        rendu="2024-11-15"
    ))


# INSERTION
with get_session() as session:
    for _ in range(10):
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