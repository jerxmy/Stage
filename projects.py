'''
CREATE TABLE IF NOT EXIST Project (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    poste TEXT NOT NULL,
    entreprise TEXT NOT NULL,
    expedition TEXT NOT NULL,
    text TEXT
)
'''
# bdd.py
from project_model import Project, Proj

from database import get_session
from sqlmodel import select


# INSERTION
with get_session() as session:
    for _ in range(10):
        new_Project = Proj()
        session.add(new_Project) #insert
        session.commit() #commit
        session.refresh(new_Project) #recup_id
        print(new_Project)
        print(new_Project.id)

# SELECT
with get_session() as session:
    statement = select(Project)
    results = session.exec(statement).all()
    for Project in results :
        print(Project)