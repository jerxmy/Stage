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

# Créer table si nécessaire 

# Manipulation de la table