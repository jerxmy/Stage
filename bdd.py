'''
CREATE TABLE IF NOT EXIST stage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    poste TEXT NOT NULL,
    entreprise TEXT NOT NULL,
    expedition TEXT NOT NULL,
    text TEXT
)
'''

from sqlmodel import SQLModel, Field, create_engine, Session
from typing import Optional

file_name = "database.sqlite"

class Stage(SQLModel, table=True):
    # Definition de la structure de la table = une classe
    __tablename__ = "Stages"
    id: Optional[int] = Field(default=None, primary_key=True)
    poste : str
    entreprise : str
    expedition : str
    url : Optional[str] = None

# Initialiser le moteur 
engine = create_engine(f"sqlite:///{file_name}")

# Créer tables si nécessaire 
SQLModel.metadata.create_all(engine)

# Manipulation de la table
with Session(engine) as session:
    new_stage = Stage(
        poste="Dévloppeur Web",
        entreprise="Jerem Corp",
        expedition="2024-11-10",
        url="https://jerem.com/jobs"
    )
    session.add(new_stage) #insert
    session.commit() #commit
    session.refresh(new_stage) #recup_id
    print(new_stage)
    print(new_stage.id)